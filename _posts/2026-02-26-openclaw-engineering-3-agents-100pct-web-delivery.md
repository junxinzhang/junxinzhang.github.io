---
layout: post
title: "我的 OpenClaw 工程化：3 个 Agent 跑通 100% Web 开发交付闭环"
date: 2026-02-26
author: Jason Zhang
categories: [AI, 软件工程]
image: assets/images/screenshot-20260226-openclaw-3agent-web-cover.png
tags: [featured, OpenClaw, Agent Team, Web开发, 工程化, GitHub Pages, Cloudflare, HTTPS, DevOps, Landing Page, 自动化交付]
slug: openclaw-engineering-3-agents-100pct-web-delivery
description: "我用 3 个 OpenClaw Agent（开发、验证、上线）把 Voice Real-time Translation 落地页从代码编写、测试、部署、域名配置到证书配置全链路跑通。22 次 commit、一次完整回滚、三套统计系统接入——不是 demo，是可复用的工程化交付实战。"
geo_facts:
  - text: "vrt-landing-page 已独立为公开仓库（github.com/junxinzhang/vrt-landing-page），共 22 次 commit，全部在同一天内完成，展示了 Agent 驱动的高密度迭代能力。"
  - text: "Cloudflare DNS 已配置 CNAME：vrt.junxinzhang.com -> junxinzhang.github.io，GitHub Pages 已启用 HTTPS，证书状态 approved（到期 2026-05-28）。"
  - text: "项目已接入三套独立统计系统：百度统计（ca2efa711b1a5fefdd03ba4355a49406）、Umami（df2642a3-5ba6-4d9f-8609-060fd2d69e38）、Google Analytics（G-2Y9RHGQ0TG），实现流量数据的交叉验证。"
  - text: "落地页采用纯 HTML5/CSS3/JavaScript 技术栈，零框架依赖，支持 PWA，响应式断点覆盖 520px/860px/1024px 三档，确保全设备可访问。"
  - text: "项目经历一次完整的工程化回滚（commit 2bb57b6 回退至 977be32 基线），验证了 Agent 驱动的版本控制与质量兜底能力。"
faq:
  - question: "3 个 Agent 真能覆盖 100% Web 开发吗？"
    answer: "在这个项目里可以。关键是把流程拆成'开发→验证→上线'三段接力，每段有明确的输入输出边界，而不是让一个 Agent 从头做到尾。100% 的含义不是零人工，而是人只做目标设定和最终判断，执行全部由 Agent 完成。"
  - question: "为什么要把域名和证书也纳入工程化？"
    answer: "因为用户访问的是 https://vrt.junxinzhang.com，不是你的 localhost:8080。代码写好了但域名没配、证书没生效，对用户来说就是'打不开'。只做代码自动化而不做发布基础设施自动化，交付链路就是断的。"
  - question: "回滚是不是代表 Agent 失败了？"
    answer: "恰恰相反。能回滚说明你的工程化是健全的——有基线 commit 可追溯、有明确的回退路径、有重建后的验收闭环。工程化的价值不在于永不出错，而在于出错时可控。"
  - question: "这套方法适合个人开发者吗？"
    answer: "非常适合。个人开发者最缺的不是写代码的能力，而是发布环节的系统化——域名配了吗？证书生效了吗？统计埋点全了吗？SEO 配置对了吗？这些靠记忆迟早出错，靠流程才能稳定。"
---

今天中午吃饭前，我掏出手机给 Main Claw 发了一条消息：

> "参考 meterinfoapp-landing-page 的结构，帮我落地 Voice Real-time Translation 的产品页。截图先空着，域名用 vrt.junxinzhang.com。你分配给 Winnie 和 Amy 一些活，一起完成。"

然后我放下手机，去吃饭了。

吃完饭回来，收到了Main Claw的回复说已经完成了，让我直接打开浏览器，输入 `https://vrt.junxinzhang.com`——页面秒开，HTTPS 小锁亮着，下载按钮指向 DMG 安装包，B 站演示视频自动加载，百度统计、Umami、Google Analytics 三套埋点全部在线。

我愣了几秒。

**从我发出那条消息，到眼前这个完整可用的线上产品页，中间我没有碰过一行代码、没有登录过一次 GitHub、没有打开过 Cloudflare 的控制台。**

域名是 Agent 配的。证书是 Agent 触发的。统计代码是 Agent 埋的。甚至后来那次"改版翻车后的紧急回滚"，也是 Agent 在 3 分钟内完成的。

**<mark>一句话结论：一条消息发给 Main Claw，Winnie 写代码、跑验证、做上线，Amy 写复盘——一顿饭的功夫，从代码到线上产品页，全链路交付完成。</mark>**

![一条消息触发：从代码编写到线上交付的全链路自动化](/assets/images/screenshot-20260226-openclaw-3agent-web-cover.png)

<!-- 封面图提示词（baoyu-cover-image / baoyu-image-gen，严格 2.35:1，输出 PNG）：
Type=conceptual, Palette=cool, Rendering=digital, Text=title-subtitle, Mood=bold。
画面中央是一条发光的自动化流水线，三位拟人化的机械Agent依次站在流水线上：左侧"开发Agent"正在编辑代码屏幕（蓝色光芒），中间"验证Agent"面前是一张巨大的检查清单在逐项打勾（黄色光芒），右侧"上线Agent"点亮了一个写着"vrt.junxinzhang.com"的域名标牌和一把HTTPS金色锁（绿色光芒）；流水线下方隐约可见GitHub图标和Cloudflare云朵。背景深蓝色科技渐变，有细微的代码流动效果。
标题（中文）：《我的 OpenClaw 工程化》
副标题（中文）：《3 个 Agent 跑通 100% Web 开发交付闭环》
要求：中文文字清晰醒目、禁止出现英文大字、科技感但易读、Aspect Ratio 2.35:1、输出 PNG。
-->

如果你只有 30 秒，先看这 3 句：

1. 我把 Voice Real-time Translation 的落地页项目交给 Winnie，由它的 3 个 SubAgent 接力完成：Dev 写代码、QA 跑检查、Release 做发布——三段接力，一只虾搞定。
2. 线上已经真实可用：`https://vrt.junxinzhang.com`，DNS 在 Cloudflare，HTTPS 证书由 GitHub Pages 自动托管，三套统计系统同时在线。
3. 最关键的不是"自动化很快"，而是**<mark>这次经历了一次完整回滚——回滚本身，才是工程化最硬的证明。</mark>**

---

## 一、为什么"能写代码"不等于"能交付"

这件事的起因很简单。

昨天我刚写完[《我的 OpenClaw 养虾记：3 个 Agent 跑通 100% 自动化闭环》]({{ site.baseurl }}/openclaw-shrimp-farming-3-agents-automated-loop)，很多人的反馈集中在一个问题：

> "Agent 能写代码我信了，但你说的 100% 自动化，是不是只做到了代码层面？部署呢？域名呢？HTTPS 呢？用户真的能打开吗？"

这个问题问到了要害。

说实话，很多技术文章（包括我自己以前写的）都有一个隐含假设：代码写完 = 交付完成。但现实里，一个落地页从"本地能跑"到"用户能用"，中间还有一段很长的路：

| 阶段 | 典型动作 | 容易出问题的点 |
|---|---|---|
| 代码编写 | HTML/CSS/JS、资源整合 | 样式错乱、资源路径错误 |
| 本地验证 | 浏览器预览、多设备测试 | "我这里可以"但线上不行 |
| 仓库管理 | 创建 repo、推送代码 | 分支混乱、.gitignore 遗漏 |
| 部署配置 | GitHub Pages / Vercel / Netlify | 构建失败、路径 404 |
| 域名解析 | Cloudflare / DNS 配置 CNAME | 解析延迟、缓存干扰 |
| 证书配置 | HTTPS 启用与验证 | 证书未签发、Mixed Content |
| 统计埋点 | 百度统计 / GA / Umami | 脚本漏装、ID 错误 |
| SEO 配置 | sitemap / robots.txt / OG tags | 搜索引擎抓不到、分享卡片空白 |

这张表里的每一项，都是我或者我身边的工程师踩过的坑。而且它们有一个共同特点：**单独看都不难，但加在一起靠人工记忆，迟早漏一个。**

所以这次我的目标不是"做一个漂亮页面"，而是**把整条交付链路工程化**——用 Agent 把每个环节串起来，让"从代码到用户可访问"变成一条可重复的流水线。

---

## 二、项目全貌：一个真实的落地页，不是 Demo

先说清楚这次做的是什么。

项目是 **Voice Real-time Translation 的产品落地页**——就是我在[前一篇文章]({{ site.baseurl }}/macos-realtime-translation-for-teams-standard)里介绍的那个 macOS 实时语音翻译器的官方展示页面。

为什么要做落地页？因为那篇文章发出去之后，不少人问我"在哪下载"、"有没有产品介绍页"。一个好产品没有落地页，就像一家好餐厅没有门面——别人想进来都找不到入口。

### 2.1 技术栈：刻意做了"零框架"

| 技术选型 | 具体实现 | 选择理由 |
|---|---|---|
| 页面结构 | 纯 HTML5 语义标签 | 无构建步骤，GitHub Pages 直接托管 |
| 样式系统 | CSS3 + CSS Variables | 主题可控，无预处理器依赖 |
| 交互逻辑 | Vanilla JavaScript（IIFE） | Intersection Observer + 响应式菜单 |
| 响应式 | 三档断点（520/860/1024px） | 覆盖手机、平板、桌面 |
| PWA 支持 | manifest.json + 图标 | 可安装到主屏幕 |

你没看错——**没有 React，没有 Vue，没有 Next.js，甚至没有 npm**。

这不是因为我不会用框架，而是一个刻意的工程决策：落地页是一个"发布后极少变更"的产物，用零框架意味着零构建步骤、零依赖升级风险、零 Node 版本兼容问题。GitHub Pages 直接托管 HTML，推上去就生效。

**<mark>最好的技术选型，是让问题最少的选型。</mark>**

### 2.2 页面结构：9 个区块覆盖完整转化路径

| 区块 | 内容 | 转化作用 |
|---|---|---|
| Header | 粘性导航 + 响应式菜单 | 任何时候都能跳转 |
| Hero | 核心价值主张 + CTA 按钮 + 关键指标 | 第一印象，决定留或走 |
| 价值区 | 三大核心价值（毫秒响应/可扩展/真实场景） | 建立信任 |
| 场景区 | 四大使用场景（远程会议/客服/教育/商务） | 让用户对号入座 |
| 功能区 | 8 项核心能力 + 技术路线面板 | 回答"它能做什么" |
| 截图区 | 产品截图 + B 站演示视频（BV1LyA2zSEnZ） | 让用户"看到"产品 |
| FAQ 区 | 4 个高频问题，手风琴展开 | 消除顾虑 |
| CTA 区 | 下载入口 + 联系方式 | 推动行动 |
| Footer | 品牌信息 + 导航链接 | 完善信息闭环 |

这套结构不是拍脑袋出来的，而是参考了大量 SaaS 落地页的转化漏斗逻辑：**先吸引 → 再说服 → 最后转化**。

### 2.3 线上地址与基础设施

| 项目 | 详情 |
|---|---|
| 线上地址 | `https://vrt.junxinzhang.com` |
| 代码仓库 | `github.com/junxinzhang/vrt-landing-page` |
| 托管平台 | GitHub Pages |
| DNS 服务 | Cloudflare（CNAME: vrt → junxinzhang.github.io） |
| HTTPS | GitHub Pages 自动签发（Let's Encrypt，到期 2026-05-28） |
| 统计系统 | 百度统计 + Umami + Google Analytics（GA4） |

为什么用三套统计？因为百度统计覆盖国内搜索引擎生态、Umami 是自托管的隐私友好方案、GA4 是海外流量的行业标准。三套交叉验证，确保不漏数据。

![从仓库到线上域名的完整发布路径](/assets/images/screenshot-20260226-openclaw-release-path.webp)

<!-- 插图1提示词（baoyu-image-gen，严格 2.35:1）：
Type=flowchart, Style=blueprint。
标题（中文）：《从代码到用户可访问的五段路径》
画面从左到右展示五个节点，每个节点用圆角矩形表示，节点间用发光箭头连接：
①「本地代码」图标为代码编辑器 → ②「GitHub 仓库」图标为 GitHub 猫猫 → ③「Pages 构建」图标为齿轮旋转 → ④「Cloudflare DNS」图标为橙色云朵 → ⑤「HTTPS 生效」图标为绿色小锁和浏览器地址栏显示 vrt.junxinzhang.com
每个节点下方标注关键动作：推送代码 / 触发构建 / CNAME 解析 / 证书签发 / 用户可达
底部一行结论文字：「5 段全部自动化 = 100% 交付闭环」
背景深蓝色，节点为亮色，发光连线，工程蓝图风格，中文清晰可读，Aspect Ratio 2.35:1。
-->

---

## 三、Winnie 的 3 个 SubAgent 接力赛：为什么是"接力"，而不是"一口气"

在[昨天的养虾文章]({{ site.baseurl }}/openclaw-shrimp-farming-3-agents-automated-loop)里，我介绍了 Winnie（编码虾）和 Amy（文案虾）的按能力分工模式。这次的 Web 交付场景不太一样——落地页从代码到上线是纯技术活，所以 **技术链路由 Winnie 一只虾通过 3 个 SubAgent 接力完成**。Amy？别急，它在最后会登场。

换句话说，技术交付这一段不是"两个人各干各的"，而是"同一个人换了三顶帽子，按阶段依次戴上"。

为什么这么设计？因为 Web 交付是一条严格有序的链路：代码没写完不能验证，验证没过不能上线，上线失败要能回滚到上一步的稳定状态。把三个阶段拆成三个 SubAgent，每个 SubAgent 拥有独立的上下文窗口和专注范围，比让一个 Agent 一口气扛到底要稳定得多。

### 3.1 SubAgent 1：开发阶段（Winnie · Dev）——写代码

| 职责 | 具体动作 |
|---|---|
| 页面结构与样式 | 编写 HTML/CSS/JS，调整布局与交互 |
| 内容与资源 | 替换截图、嵌入 B 站视频、配置下载入口 |
| SEO 配置 | 编写 meta tags、OG 标签、结构化数据 |
| 提交变更 | git add / commit / push，附带清晰的 commit message |

Winnie 的开发阶段表现非常稳定。它一天内产出了 22 次 commit，覆盖了从初始页面搭建（`feat: initial VRT landing page`）到资源本地化（`feat: switch installer and screenshots to repo-hosted assets`）、视频嵌入（`feat: switch demo video embed to bilibili`）、视觉优化（`feat: refine VRT landing page visual polish`）的完整开发周期。

值得一提的是，commit message 风格非常规范——统一使用 `feat:` / `fix:` / `docs:` / `revert:` 前缀，每条消息都能让你 3 秒钟内理解这次提交干了什么。这不是偶然，而是我在 Agent 的 system prompt 里明确要求的。

### 3.2 SubAgent 2：验证阶段（Winnie · QA）——跑检查

| 职责 | 具体检查项 |
|---|---|
| 文案校验 | 核心文案是否正确呈现 |
| 资源可达 | 截图/视频/下载包链接是否 200 OK |
| 脚本存在 | 三套统计代码是否都嵌入了 |
| 构建状态 | GitHub Pages 构建是否成功（无 404） |
| 响应式 | 三档断点是否正常（520/860/1024px） |

验证 SubAgent 的价值在于**它不跳步骤**。

人类做测试最容易犯的错就是"这个肯定没问题，跳过"——然后恰恰是那个被跳过的环节翻车。Agent 不会。你给它 10 项检查清单，它会一项不落地全部跑完，并且每次结果都是确定性的。

### 3.3 SubAgent 3：上线阶段（Winnie · Release）——做发布

| 职责 | 具体动作 |
|---|---|
| 推送主分支 | 确认所有变更已 commit 并 push 到 main |
| 触发构建 | 观察 GitHub Pages 构建状态 |
| 域名校验 | 验证 `vrt.junxinzhang.com` 解析正确 |
| HTTPS 校验 | 确认证书状态为 approved |
| 回滚预案 | 构建失败或验收不通过时，回退到基线 commit |

上线 SubAgent 最重要的能力不是"推上去"，而是"推不上去或推错了怎么办"。这正是接下来我要重点讲的。

### 3.4 为什么拆成 3 个 SubAgent，而不是让 Winnie 一口气干完

我早之前确实试过让 Winnie 一个 session 从头做到尾。结果是：

- **上下文窗口被撑满**：代码上下文 + 部署配置 + DNS 知识 + 证书流程，一个窗口装不下
- **出错难归因**：页面打不开了——是代码问题、构建问题、DNS 问题还是证书问题？一个 session 里干的活，你问它自己它也说不清
- **无法并行优化**：只有拆开，你才能单独优化某一段的效率

Elvis 在他的 Agent Swarm 方法论里提过一个核心观点：**上下文窗口是零和的**。这句话在 Web 交付场景里体现得淋漓尽致——开发上下文和运维上下文天然互斥，硬塞在一个窗口里，两头都做不好。拆成 3 个 SubAgent，本质上是给 Winnie 的同一种能力在不同阶段分配了独立的上下文空间。

![3个 SubAgent 接力式交付模型](/assets/images/screenshot-20260226-openclaw-3agent-relay.webp)

<!-- 插图2提示词（baoyu-image-gen，严格 2.35:1）：
Type=process, Style=editorial。
标题（中文）：《3个 SubAgent 接力交付：每段只做一件事》
画面是一个接力赛跑道，三位穿着不同颜色工服的中文标注Agent在传递接力棒：
第一位（蓝色，标注"开发Agent"）：手持代码编辑器屏幕，正在把一根发光的"接力棒"传给第二位
第二位（黄色，标注"验证Agent"）：面前展开一张巨大的检查清单，正在接棒
第三位（绿色，标注"上线Agent"）：终点处矗立着域名标牌"vrt.junxinzhang.com"和一把金色HTTPS锁
跑道下方有三个阶段标签：「代码就绪」→「质量确认」→「线上可达」
底部结论文字：「拆成三段的好处：每个问题都能在3秒内归因到某一段」
配色专业温暖，科技插画风，中文清晰醒目，Aspect Ratio 2.35:1。
-->

---

## 四、22 次 Commit 背后的故事：完整复盘

别人写工程化文章，喜欢画架构图。我更想给你看 git log——因为 commit 记录不会说谎。

这个项目一共 22 次 commit，全部发生在同一天。这不是"赶工"，而是 Agent 驱动的高密度迭代的自然结果。以下是关键里程碑：

### 第一阶段：从 0 到 1（commit 1-5）

```
3ce44c2  feat: initial VRT landing page
92015c8  feat: add local assets (screenshots)
63cd6e0  feat: add local assets (installer DMG)
b148bb3  feat: switch installer and screenshots to repo-hosted assets
977be32  feat: switch demo video embed to bilibili
```

这 5 次 commit 完成了页面的初始搭建：HTML 骨架、CSS 样式系统、JS 交互逻辑、产品截图、DMG 下载包、B 站演示视频嵌入。

值得注意的是第 4 次 commit（`b148bb3`）——把截图和安装包从外部链接迁移到了仓库内托管。为什么？因为外部链接有一个致命问题：**你控制不了它的可用性**。Google Drive 链接随时可能因分享设置变化而 404，而仓库内的资源只要 repo 在就在。

**<mark>工程化的第一课：把所有关键资源都纳入版本控制范围，不依赖任何外部不可控链接。</mark>**

### 第二阶段：视觉打磨（commit 6-10）

```
1a843fc  docs: embed bilibili preview in README
703ffe9  docs: update README with latest screenshots
7388a0d  feat: refine VRT landing page visual polish (index.html)
404afa8  feat: refine VRT landing page visual polish (css/style.css)
3d7434c  feat: refine VRT landing page visual polish (js/main.js)
```

这个阶段 Winnie 对页面做了一轮系统性的视觉优化——HTML 结构调整、CSS 细节打磨、JS 交互增强。三个文件分三次 commit，每次只改一个关注点。这不是强迫症，而是 **原子化提交** 的实践：每次 commit 只做一件事，出问题时可以精准回退到某一次变更，而不是"回退了样式顺便把功能也丢了"。

### 第三阶段：翻车与回滚（commit 11-14）——这才是重头戏

```
e8dfd05  fix: update favicon tab icon and FAQ Q1 client-only note
2007f35  feat: update contact CTA section with localized contact actions
06914a3  feat: add Baidu, Umami, and GA analytics scripts
2bb57b6  revert: rollback landing page UI to 977be32 baseline
```

注意最后一行：**revert**。

事情是这样的：在一轮视觉改版后，页面效果不符合预期——某些样式改动影响了布局稳定性，在移动端出现了意料之外的错位。

如果是传统手工流程，接下来大概率是这样的：

1. "先别急，我调调看"
2. 叠了 3 个 patch，每个 patch 修了旧问题又引入新问题
3. 反复修改 2 小时后，谁也说不清当前版本到底改了哪些
4. 最后被迫凌晨重做

而这次，上线 Agent 做了一件很"无聊"但极其正确的事：

1. 定位到上一个确认稳定的基线 commit（`977be32`）
2. 一键回退核心文件到该版本
3. 强制推送并触发 GitHub Pages 重建
4. 逐项验收线上内容

**几分钟内恢复到稳定版本，然后在稳定基线上继续增量迭代。**

### 第四阶段：在稳定基线上增量推进（commit 15-22）

```
f53423d  feat: localize contact CTA section
06914a3  feat: add Baidu, Umami, and GA analytics scripts
11e314a  feat: add Baidu, Umami and GA analytics (final)
```

回滚之后，Winnie 不是从零重做，而是在 `977be32` 这个稳定基线上，一个功能一个功能地叠加——先做 CTA 本地化，再做统计埋点，每次加一层，验一层，确认没问题再加下一层。

这就是"回滚"真正的价值：**它不是失败的标志，而是质量控制的工具。**

![工程化回滚：从异常到稳定的最短路径](/assets/images/screenshot-20260226-openclaw-rollback-loop.webp)

<!-- 插图3提示词（baoyu-image-gen，严格 2.35:1）：
Type=flowchart, Style=sci-fi。
标题（中文）：《工程化回滚：从异常到稳定的最短路径》
画面展示一个闭环流程图：
起点：「发现异常」（红色警告图标）
→ 「定位基线版本」（放大镜查看 git log）
→ 「一键回退提交」（revert 命令执行）
→ 「重建部署」（GitHub Pages 构建中）
→ 「逐项验收」（绿色打勾清单）
→ 终点：「稳定恢复 + 增量继续」（绿色对勾）
流程图用红→黄→绿三色渐变表达状态从异常到恢复的过程
底部醒目文字：「回滚不是失败，是质量控制动作」
背景深色科技风，流程节点发光，中文清晰，Aspect Ratio 2.35:1。
-->

---

## 五、域名与证书：交付的"最后一公里"

很多技术文章写到"代码部署完成"就结束了。但如果你问一个真正的用户："你怎么知道一个网站上线了？"

答案不是"GitHub Pages 构建成功"。答案是：**我在浏览器里输入地址，页面打开了，地址栏有 HTTPS 小锁。**

这就是为什么我把域名和证书也纳入了 Agent 的职责范围。

### 5.1 DNS 配置：Cloudflare CNAME

| 配置项 | 值 |
|---|---|
| DNS 服务商 | Cloudflare |
| 记录类型 | CNAME |
| 名称 | vrt |
| 目标 | junxinzhang.github.io |
| 代理状态 | DNS Only（灰云） |

为什么用"DNS Only"而不是 Cloudflare 的代理模式（橙云）？因为 GitHub Pages 需要直接解析到它的 IP 才能正确签发 HTTPS 证书。开了 Cloudflare 代理会导致证书签发链路断裂——这是一个极其隐蔽的坑，我见过不少人在这里卡几小时。

### 5.2 HTTPS 证书：GitHub Pages 自动签发

| 配置项 | 值 |
|---|---|
| 证书提供方 | Let's Encrypt（GitHub Pages 自动托管） |
| 证书状态 | Approved |
| 生效域名 | vrt.junxinzhang.com |
| 到期时间 | 2026-05-28 |
| 强制 HTTPS | 已启用 |

GitHub Pages 的 HTTPS 证书签发是自动的，但有一个前提：你的 CNAME 文件和 DNS 配置必须完全一致。如果 CNAME 文件写的是 `vrt.junxinzhang.com`，但 DNS 解析的目标不是 `junxinzhang.github.io`，证书就签不下来。

上线 Agent 在这一步的工作是：推送包含 CNAME 文件的代码 → 等待 Pages 检测到自定义域名 → 确认证书状态变为 Approved → 验证 HTTPS 可访问性。

**<mark>用户访问的是域名和 HTTPS，不是你的 localhost。只做代码自动化而不做发布基础设施自动化，交付链路就是断的。</mark>**

### 5.3 一个被忽视的细节：CNAME 文件必须在仓库里

很多人会在 GitHub Pages 的设置界面手动填自定义域名，然后忘了在仓库根目录放 `CNAME` 文件。这会导致一个鬼畜的现象：每次推送新代码后，GitHub Pages 会自动清除你的自定义域名设置——因为构建过程会以仓库内容为准。

解法很简单：确保 `CNAME` 文件在仓库里，内容就一行：`vrt.junxinzhang.com`。但就这么一个小文件，能让多少人半夜爬起来排查"为什么域名又失效了"。

---

## 六、三套统计系统：发布不是终点，而是循环起点

页面上线了，然后呢？

很多人的回答是"等用户来"。但更工程化的回答是：**看数据，然后迭代。**

这次我在落地页里同时接入了三套独立统计系统：

| 统计系统 | ID | 覆盖场景 | 选择理由 |
|---|---|---|---|
| 百度统计 | `ca2efa...49406` | 国内搜索引擎流量 | 百度 SEO 生态的标配 |
| Umami | `df2642...69e38` | 隐私友好、自托管 | 不依赖第三方、数据完全自有 |
| Google Analytics（GA4） | `G-2Y9RHGQ0TG` | 海外流量 + 行为分析 | 全球行业标准，报表能力强 |

为什么要三套？不嫌多吗？

不嫌。因为每套统计都有自己的盲区：百度统计看不到海外流量，GA 在国内被墙的地区数据会缺失，Umami 虽然全覆盖但报表功能相对基础。三套交叉验证，才能接近真实的全景数据。

更重要的是，统计数据回流到下一轮迭代时，能回答这些关键问题：

- 用户在哪个区块停留最久？→ 说明这块内容有吸引力
- 下载按钮的点击率是多少？→ CTA 文案是否需要优化
- 移动端和桌面端的比例？→ 响应式优化的优先级
- 用户从哪个渠道来？→ 推广策略的依据

**<mark>发布不是项目的终点，是数据驱动迭代的起点。</mark>**

![从手工发布到工程化交付的认知升级](/assets/images/screenshot-20260226-openclaw-mindset-shift.webp)

<!-- 插图4提示词（baoyu-image-gen，严格 2.35:1）：
Type=comparison, Style=minimal-flat。
标题（中文）：《从手工发布到工程化交付的认知升级》
画面分为左右两栏，中间用一道发光分割线隔开：
左侧标注「手工发布」：一张凌乱的桌面，便签纸满天飞，屏幕上是红色报错信息，一个开发者满头大汗对着电脑，旁边有"又忘了改DNS"、"证书过期了？"、"统计代码漏了"三个气泡
右侧标注「Agent 工程化」：一条整洁的流水线看板，三段流程（开发/验证/上线）有序运行，每段都有绿色通过标记，屏幕上显示"所有检查通过"，开发者在一旁喝咖啡审阅结果
底部横排五个核心原则图标：① 角色分段 ② 原子提交 ③ 基线可追溯 ④ 回滚可执行 ⑤ 数据驱动迭代
底部结论文字：「把经验变成系统，把焦虑变成可控」
极简扁平风格，左灰暗右明亮表达升级感，中文清晰易读，Aspect Ratio 2.35:1。
-->

---

## 七、普通团队可以直接复用的 5 条方法

这次工程化实践之后，我提炼了 5 条不依赖 OpenClaw、任何团队都能用的方法：

### 1）先拆角色，再谈自动化

别上来就让"一个人从头做到尾"或者"一个 Agent 全包"。

开发、验证、上线是三种完全不同的能力和心智模型。开发关注"怎么实现"，验证关注"实现得对不对"，上线关注"用户能不能用"。三者混在一起，出了问题你连在哪一段出的都说不清。

### 2）先做最小可验证闭环

不要一开始就追求"完美的自动化流水线"。先把最简单的闭环跑通：

> 改一行代码 → 推上去 → 线上能看到变化

这个闭环一旦跑通，你就有了信心和基础去叠加更多能力（验证、统计、回滚……）。

### 3）把域名和证书纳入发布清单

代码部署成功 ≠ 用户可用。**域名解析 + HTTPS 生效** 才是"交付完成"的标志。每次发布前至少确认这两项。

### 4）所有关键动作都可追踪

每次变更都应该有 commit，commit 都应该有清晰的 message，每个发布节点都应该能追溯到对应的 commit hash。出问题的时候，`git log` 就是你的黑匣子。

### 5）人只做高价值判断

Agent 负责重复执行（写代码、跑检查、推部署、配 DNS）。人负责两件事：**定目标** 和 **做判断**（这个改版好不好？要不要回滚？数据说明什么？）。

如果你发现自己在反复做某个手工步骤，那就是一个信号：**这个步骤应该交给 Agent。**

---

## 八、下一步路线图

这次的实践验证了"3个 SubAgent 接力"在单个 Web 项目上的可行性。接下来我会继续推进：

1. **发布前自动检查清单**：把验证 Agent 的检查项标准化为 YAML 配置，新项目直接复用
2. **Staging 环境**：正式上线前先跑一轮灰度预览，减少"推上去才发现问题"
3. **统计数据回流**：把 GA/Umami 的数据自动汇总，生成每周迭代建议
4. **模板化复用**：为其他 Web 项目（博客、文档站、产品页）复制同样的 3 Agent 交付流程
5. **沉淀为 SOP**：把整套流程写成"个人可复用的 Agent Team 标准操作程序"

---

## 写在最后：Amy 说，该她了

落地页上线、数据回流、方法论沉淀——技术链路到这里就跑通了。

然后我在 Main Claw 里敲了一句话：

> "好了，本次项目的经验和教训，交给 Amy 帮我写一下今天的笔记。"

是的，**你现在看到的这篇文章，底稿来自 Amy。**

Winnie 跑完了从代码到上线的全链路，Amy 接过 Winnie 留下的 commit 记录、回滚日志、部署配置，把一整天的工程实践浓缩成了你正在阅读的这些文字。我在她的草稿上做了润色和事实校验，但骨架和叙事线是她搭的。

这件事让我意识到一个更深层的变化：

**Winnie 和 Amy 已经不只是"各干各的"了——它们开始形成流水线式的协作：一个创造事实，一个把事实变成叙事。**

回过头来看，这次最让我有感触的不是"22 次 commit 好快"，也不是"落地页一顿饭的功夫就上线了"，而是那次回滚——以及 Amy 在文章里把回滚写成了"工程化最硬的证明"。

传统观念里，回滚是一件丢人的事——"你搞砸了才需要回滚"。但在工程化视角下，回滚是一种能力：**它说明你的版本控制是健全的、你的基线是可追溯的、你的恢复路径是明确的。** Amy 比我自己更早想清楚了这一点，并且把它放在了文章最显眼的位置。

这次我对"100% Web 开发交付"的定义也更清晰了：

- 人定义目标
- Winnie 完成技术执行
- 系统保证可控
- 出错时可回滚
- Amy 把经验变成内容
- 数据能驱动下一轮

**<mark>当你把交付链路工程化，Agent 就不再是玩具，而是团队基础设施。当两只虾学会接力，一个人就真的变成了一个团队。</mark>**

对了，这篇文章的主角——那个被 Claw 们一顿饭功夫推上线的落地页——就在这里：[vrt.junxinzhang.com](https://vrt.junxinzhang.com)。如果你也有跨语言会议的痛点，欢迎试用 **Voice Real-time Translation**，也欢迎在落地页底部联系我聊聊你的真实场景。

---

## 相关阅读

**OpenClaw 系列**
- [我的 OpenClaw 养虾记：3 个 Agent 跑通 100% 自动化闭环]({{ site.baseurl }}/openclaw-shrimp-farming-3-agents-automated-loop)
- [Mac Mini 被 AI 圈抢光了，真的值得买吗？我的 OpenClaw 实测体验]({{ site.baseurl }}/openclaw-macos-best-environment)
- [OpenClaw 尝鲜报告：这款爆火的 AI 工具，现在能用吗？]({{ site.baseurl }}/openclaw-bugs-and-local-fixes)

**AI 工程系列**
- [Teams 只有字幕没有翻译？我在 macOS 做了一个实时语音翻译器]({{ site.baseurl }}/macos-realtime-translation-for-teams-standard)
- [从 GLM-5、MiniMax 到"红包大战"：开工第一天你必须看懂的 AI Coding 新秩序]({{ site.baseurl }}/ai-coding-reconstruction-software-engineering)
- [AI 订阅收紧潮：从 Anthropic 到 Google、GLM，免费午餐真的结束了]({{ site.baseurl }}/ai-subscription-tightening-free-lunch-over)

---

## 参考资料（官网/官方）

1. OpenClaw 官方文档
   [https://docs.openclaw.ai/](https://docs.openclaw.ai/)
2. GitHub Pages 官方文档
   [https://docs.github.com/en/pages](https://docs.github.com/en/pages)
3. GitHub Pages 自定义域名配置指南
   [https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
4. Cloudflare DNS 文档
   [https://developers.cloudflare.com/dns/](https://developers.cloudflare.com/dns/)
5. Let's Encrypt 证书说明（GitHub Pages 使用）
   [https://letsencrypt.org/](https://letsencrypt.org/)
6. Google Analytics gtag.js 集成文档
   [https://developers.google.com/analytics/devguides/collection/gtagjs](https://developers.google.com/analytics/devguides/collection/gtagjs)
7. Umami 自托管分析平台文档
   [https://umami.is/docs](https://umami.is/docs)
8. 百度统计官方文档
   [https://tongji.baidu.com/](https://tongji.baidu.com/)
