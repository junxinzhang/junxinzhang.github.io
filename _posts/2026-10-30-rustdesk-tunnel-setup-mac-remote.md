---
layout: post
title: "远程桌面试了一圈，我把所有机器切到了自建RustDesk"
date: 2026-10-30
author: Jason Zhang
categories: [技术, 思考]
image: assets/images/cover-20261030-rustdesk-tunnel-setup.webp
tags: [featured, RustDesk, 远程桌面, Mac Studio, 开源, 运维, 踩坑, 思考]
slug: rustdesk-tunnel-setup-mac-remote
description: >
  试过 ToDesk 付费版、HopToDesk、TeamViewer 和 VNC，最后我把家里和手头的 Mac 全部切到了自建 RustDesk。不碰商业软件的限速与弹窗，靠一台轻量云服务器和几处系统底层配置，把延迟压到 3 毫秒，搞定无头 Mac 鼠标重影与代理冲突。
faq:
  - question: "自建 RustDesk 相比商业远程软件的核心差异在哪？"
    answer: "商业软件对免费版限制帧率、压缩画质，晚高峰容易排队中转。自建节点把信令与中继握在自己手里，端到端采用 Ed25519 加密，同网段或打洞成功走直连，画质不被动态压缩。"
  - question: "服务端搭建必须放行哪些端口？"
    answer: "云防火墙需放行 TCP 21115（NAT测试）、TCP/UDP 21116（注册与打洞信令，UDP常漏）、TCP 21117（数据中继）以及 TCP 21114（轻量API）。"
  - question: "无头运行的 Mac 为什么会出现鼠标重影？"
    answer: "虚拟显示器缺少硬件光标层，系统 WindowServer 将鼠标绘制为顶层软件窗口。传统捕获接口会将该窗口压入视频流，产生本地光标与视频光标双重叠。需在后台调用底层接口隐藏光标入流渲染层。"
---

<!-- baoyu-skill cover prompt: 2.35:1小清新治愈知识漫画封面，柔和米白到浅青灰渐变底色，干净纤细线稿，薄荷绿/淡暖杏/天蓝清新平涂，留白充足。禁止品牌logo与深色赛博UI。画面左侧一位开发者坐在桌前操作笔记本，屏幕显示清晰的代码与终端；一条透明的发光管道穿过云朵直达右侧桌上的银色Mac Studio主机；管道上方标着「3ms」与「60 FPS」，没有多余弯折；窗外是平静的清晨天色。顶部居中中文大标题「远程桌面试了一圈」，底部辅助文字「我把所有机器切到了自建RustDesk」。中文文字端正清晰可读。 --ar 2.35:1 -->

大家好，我是 Jason。

上一篇我写了添置 M5 Ultra 跑 Agent，后台收到不少私信，问我出门在外怎么连回家里的这堆机器。

这几年我把市面上的工具用了一遍：ToDesk 付费版、HopToDesk、TeamViewer、VNC。测到最后，我把所有主力设备切到了自建 RustDesk。

代码开源，中继自己搭，连接走自己的云服务器。Rust 写的底层组件占资源极低，点开窗口画面直接出来。

把用到的配置、脱敏后的参数和踩坑过程写在这里。

![远程桌面试了一圈封面](/assets/images/cover-20261030-rustdesk-tunnel-setup.webp)

---

<!-- baoyu-skill prompt: 2.35:1小清新知识漫画，淡暖杏向米白微光渐变，清线描边，薄荷绿/蜜桃粉/天蓝平涂，留白充足。画面左侧画着几个被锁链和计时器困住的屏幕，标注着商业软件限速、卡顿、弹窗和画质变糊的提示框；右侧是一条绿草铺就的直道，一台轻巧的金属小车贴地疾驰，车身标着「RustDesk 自建直连」，直奔远处的银色主机。顶部中文「告别公共通道」，底部「流量与密钥留在自己手里」。中文文字工整清晰。 --ar 2.35:1 -->

### 商业工具的卡点

商业软件有统一的商业模式：免费版限制帧率在 30 帧，画质开动态自适应。网络有一点抖动，屏幕立刻糊成一片。

买过付费版，高峰期照样会绕进公共中继服务器。代码和操作在谁的机器里过了一道，谁心里也没底。

自建 RustDesk 的逻辑相反：设备能直连就走局域网或者打洞，打不通才走自己的云服务器中继。传输走 Ed25519 加密，两端握手靠私钥认证。

![告别公共通道与私有链路](/assets/images/illust-20261030-commercial-vs-selfhost.webp)

---

<!-- baoyu-skill prompt: 2.35:1小清新知识漫画，柔和米白底色，细线条勾勒，薄荷绿/淡天蓝/浅灰平涂，留白充足。画面中央一张原木工作台，左边摆着云服务器方盒，标注端口21115、21116与21117；右边两台银色Mac笔记本，屏幕中间拉起一条带锁的绿色连线，连线上挂着一把小巧铜锁，上面写着「Key 鉴权」。顶部中文「极简中继拓扑」，底部「四个端口撑起私有专线」。中文文字端正清晰可读。 --ar 2.35:1 -->

### 服务端跑起来

服务端找一台带独立公网 IP 的轻量云服务器。

安全组放行四个端口：

| 端口 | 协议 | 作用 |
|---|---|---|
| `21115` | TCP | NAT 类型探测 |
| `21116` | TCP / UDP | 设备注册与打洞信令（UDP 容易漏配） |
| `21117` | TCP | 流量中继转发 |
| `21114` | TCP | 心跳与状态接口 |

部署用 systemd 启动两个二进制文件 `hbbs` 和 `hbbr`。

在启动命令后加 `-k _`，强制客户端携带 Key 才能连入，避免 IP 暴露后被扫描抓去当中继。

启动后在数据目录拿到生成的公钥：

```bash
cat /opt/rustdesk-server/data/id_ed25519.pub
```

拿到公钥字符串，服务端配置就结束了。

![服务端端口与连接拓扑](/assets/images/illust-20261030-server-ports-topology.webp)

---

<!-- baoyu-skill prompt: 2.35:1小清新知识漫画，浅青向米白渐变，清线描边，薄荷绿/暖黄平涂，留白充足。画面展示一台Mac的屏幕设置窗口，界面里填入中继地址与Key，下方一行醒目的配置开关「硬件加速启用」「锁定60帧」「关闭ABR降低画质」逐一点亮绿色指示灯；右侧放大显示代码编辑器里的每一行字符，边缘锐利如刀切。顶部中文「画质拉满」，底部「文字锐利，操作跟手」。中文文字工整清晰。 --ar 2.35:1 -->

### 客户端配置与画质锁死

在主控 Mac 和被控 Mac 打开 RustDesk 设置，进入网络面板，填入自建服务器 IP 和刚刚拿到的公钥 Key。

要做到操作跟手、文字清晰，不要留默认参数。

打开客户端配置文件 `RustDesk2.toml` 与对应设备的 `peers` 文件，改写这几项：

```toml
[options]
custom-rendezvous-server = '47.103.x.x'
key = '0E9Haq4cDf+dxFq2D2eJkc8mkQdEhGy0LfpSwvda02s='
direct-server = 'Y'
enable-hwcodec = 'Y'
enable-abr = 'N'
codec-preference = 'h265'
custom-fps = '60'
```

- `direct-server = 'Y'`：开启本地监听。同一局域网或者通过内网穿透直达时，直接建立点对点连接，不消耗云服务器带宽。
- `enable-hwcodec = 'Y'`：调用 Apple Silicon 的硬件编解码器，编码延迟压在 5 毫秒内，机器不发烫。
- `enable-abr = 'N'`：关掉自适应码率，锁死 60 帧，编辑器里的代码不再出现马赛克。

连上家里的 Mac Studio 实机看一眼状态监控面板：

![RustDesk 真实连接状态：55FPS，延迟19ms，H.265编码，30M目标码率](/assets/images/photo-20261030-rustdesk-interface.webp)

网络打洞直连，帧率拉满，H.265 硬件编解码开启，画质和在本地屏幕前写代码没区别。

![锁定硬件编码与高帧率参数](/assets/images/illust-20261030-client-codec-config.webp)

---

<!-- baoyu-skill prompt: 2.35:1小清新知识漫画，奶油白向浅湖蓝渐变，干净细线稿，薄荷绿/珊瑚粉/淡蓝平涂，留白充足。画面左侧展示一把剪刀剪断了重叠虚影的慢动作鼠标，只留下一只精准点击代码的轻巧箭头；右侧两根网线避开了一个标着代理软件的绕路陷阱，径直扎入底层的物理网卡插槽。顶部中文「拔掉暗刺」，底部「消除延迟确认与虚拟屏重影」。中文文字工整清晰。 --ar 2.35:1 -->

### 踩过的坑与底层修正

很多人搭完觉得卡，问题通常不在 RustDesk 自身，在系统层。

**1. 关掉延迟确认（Delayed ACK）**

macOS 默认会对小数据包做延迟确认，攒满或者超时再回包。打字和移动鼠标的微小动作，会被系统拖出几十毫秒的粘滞感。

在终端执行：

```bash
sudo sysctl -w net.inet.tcp.delayed_ack=0
sudo sysctl -w net.inet.tcp.sendspace=524288
sudo sysctl -w net.inet.tcp.recvspace=524288
```

关掉延迟等待，把 TCP 缓冲扩容到 512KB，鼠标移动立刻顺畅。

**2. 绕开代理软件的 Fake-IP 拦截**

Mac 如果常驻 TUN 模式的代理工具，自建服务器的流量会被抓进虚拟网卡，甚至绕出国兜一圈，延迟从几毫秒涨到几百毫秒。

写一个启动守护脚本，开机把服务器 IP 绑定到物理网卡网关：

```bash
GW=$(route -n get default -ifscope en0 | awk "/gateway:/ {print \$2}")
route -n add -host 47.103.x.x "$GW"
```

同时把物理网卡的真实内网 IP 写进 RustDesk 配置，避免上报给中继服务器的是代理网卡的假 IP。

**3. 无头 Mac Studio 的光标重影**

机房或家里的 Mac Studio 不接物理屏幕，可以用虚拟屏幕工具挂载一个 Retina 虚拟显示器。

但虚拟屏没有物理 GPU 光标层，WindowServer 会把鼠标画成一个软件顶层窗口。老接口抓屏时，会把这个窗口录进视频画面。

你在主控端移动鼠标，会看到一个本地的真实光标，后面跟着一个延迟 30 毫秒的视频虚影，双鼠标在屏幕上追逐。

写一个轻量常驻工具，在后台调用 SkyLight 接口将光标从视频合成层隐藏，保留系统当前指针形状的事件传递。画面里的第二只假鼠标消失，主控端本地光标直接操控，手感和坐在这台机器前一致。

![消除延迟与修复虚拟屏重影](/assets/images/illust-20261030-latency-and-cursor-fix.webp)

---

### 最后

云服务器选按流量计费，峰值带宽拉到 50M 或 100M。

平时两端能直连就不走中继，一个月中继流量花不到两块钱。

出门掏出笔记本，点开家里的 Mac Studio，3 毫秒延迟，满帧 60 帧。工具放在自己手里，干活踏实。

---

### 相关阅读

- [今年买了近40万的苹果设备跑Agent：10月24日，我又添了一台M5 Ultra]({{ site.baseurl }}/m5-ultra-96g-agent-machine-400k-apple)
- [一人公司生存图鉴：我是如何做到年入100万的]({{ site.baseurl }}/one-person-company-million-claude-code)
- [写在公司营收第一个100万：创业头三年，除了你自己哪还有什么团队]({{ site.baseurl }}/first-million-revenue-three-years)
