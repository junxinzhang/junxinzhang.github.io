---
layout: post
title: "同时开 5 个 Agent 之后，我让它们用飞机维修手册的语言给我汇报"
date: 2026-10-03
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20261003-ste100-explain.webp
tags: [featured, AI, Agent, ASD-STE100, 简化技术英语, Claude Code, Codex, Grok Bot, Zaokit]
slug: ste100-make-agents-explain-clearly
description: >
  同时开着五个 Agent，卡住我的是读汇报。我拿 Zaokit 产品架构做了一次测试：同一段说明，先让 Agent 按飞机维修手册的规范 ASD-STE100 重写，再让它直接输出可交互的 HTML 架构图。文字读两遍没找到的答案，图上一条虚线就交代了。这篇记录测试过程、翻车点和我现在固定用的提示词。
faq:
  - question: "ASD-STE100 是什么？"
    answer: "ASD-STE100 又叫简化技术英语（Simplified Technical English），由欧洲航空航天与防务工业协会（ASD）维护，最早用于飞机维修文档。当前版本 Issue 9 在 2025 年 1 月发布。规范包含约 900 个批准词和 53 条写作规则，每个词只允许一个意思、一个词性，步骤类句子不超过 20 个词，描述类句子不超过 25 个词。官网 asd-ste100.org 可以免费申请 PDF。"
  - question: "让 LLM 用 ASD-STE100 写中文汇报有用吗？"
    answer: "有用，但要改造。规范针对英文，按词数限制句长，中文没有这个概念。我的做法是保留它的精神：一句只说一件事、步骤用动词开头、同一个东西始终用同一个名字、要你做的事放在最前面，句长改成按字数控制。规范偏严，要求做到 80% 的程度更顺手。"
  - question: "除了改写文字，还有哪些办法能更快看懂 Agent 的输出？"
    answer: "按理解成本排：精简文字、Mermaid 图表、交互式 HTML 网页、带配音的讲解视频。后两种过去成本太高没人做，现在模型写前端和动画脚本的能力够用，可以按需生成、看完就扔。"
---

<!-- baoyu-skill cover prompt: 2.35:1清新知识漫画封面，奶油底到天蓝渐变，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面左侧五个小机器人各自举着长长的文字纸卷，纸卷缠绕成一团乱麻飘向中间。中间画一个漏斗，漏斗上标「ASD-STE100」。漏斗右侧流出整齐的短句卡片、一张流程图、一个网页窗口和一个播放按钮。右侧一个人物坐在桌前，手里拿着一张短句卡片，表情放松。顶部中文大标题「让AI说人话」，底部「看懂输出 才能管住Agent」。中文清晰可读。 --ar 2.35:1 -->

大家好，我是 Just Jason。

我平时同时开着四五个 Agent：Claude Code 写主力代码，Codex 接复杂工程，Agy 干文档和调研，Cursor 改小东西，Grok Bot 在云上 24 小时跑着几个岗位。

机器早就够了。现在卡住的是我自己：五个窗口轮流亮，每个都在等我看完汇报再拍板。它们写得比我读得快。

![3个Agent之后，瓶颈换成了你](/assets/images/illust-20261003-agent-flood.webp)

<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底到蜜桃渐变，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面中央一个人物坐在三块并排的显示器前，每块屏幕里探出一个小机器人，同时往外吐长长的文字纸带，纸带在桌面上堆成小山，淹到人物的胸口。人物左手端着凉掉的咖啡，右手捏着一支红笔。墙上时钟指向深夜。顶部中文「3个Agent之后 瓶颈换成了你」，底部「它们写得越快 你读得越慢」。中文清晰可读。 --ar 2.35:1 -->

---

今天下午有个现成的例子。我让 Agent 梳理 Zaokit 的产品架构，它交回来的文字说明是这样：

> 用户经品牌入口进入 Zaokit AI PPT、Cowork、AI Education 三个应用；PPT 与 Cowork 通过 Zaokit AI Gateway 按需调用文本推理、图像生成、语音等外部模型能力；Zaokit Token Hub 以旁路治理方式提供团队用量、额度分配与成本可视；各应用分别产出演示文稿、工作成果与学习实践。本图为产品能力示意，不代表生产部署拓扑。

信息全对。可一句话塞了五层关系，我读到"旁路治理方式"停住了：Token Hub 到底在不在调用链上？

这件事要紧：在链上，Token Hub 挂了 PPT 和 Cowork 一起停；在旁路，它挂了只影响看账。两套运维预案。我往回读了两遍，这段话没给答案。

---

前几天在 X 上看到一条建议：让 LLM 用 ASD-STE100 来解释东西。

ASD-STE100 叫简化技术英语，上世纪 80 年代欧洲航空业为飞机维修手册定的写作规范，最新版 Issue 9 在 2025 年 1 月发布，[官网](https://www.asd-ste100.org/)可以免费申请。规矩很硬：词典只收约 900 个词，一个词只准有一个意思，步骤句不超过 20 个词，主动语态，一句只写一件事，总共 53 条规则。

模型读过大量航空和制造业文档，点出这个名字，它就知道该怎么收着写。

![航空维修手册的写作纪律](/assets/images/illust-20261003-ste-rules.webp)

<!-- baoyu-skill prompt: 2.35:1清新知识漫画信息图，奶油底到薄荷绿渐变，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。左侧画一架小飞机停在机库里，一位维修工拿着扳手翻看一本手册。右侧画四张规则卡片竖排：卡片一「一个词 只有一个意思」，卡片二「步骤句 不超过20词」，卡片三「主动语态 动词开头」，卡片四「一句话 只说一件事」。手册与卡片之间用虚线箭头连接。顶部中文「航空维修手册的写作纪律」，底部「约900个词 53条规则」。中文清晰可读。 --ar 2.35:1 -->

我把那段架构说明丢回去，加一句"按 ASD-STE100 的规则重写，中文"：

> 入口：用户从 zaokit.com、zaokit.app、zaokit.ai 进入。任一入口可进任一产品。
>
> 应用：AI PPT、Cowork、AI Education。每个产品可独立使用，也可组合。
>
> 调用：AI PPT 和 Cowork 经 Gateway 调用外部模型。
>
> 治理：Token Hub 查看用量、分配额度、显示成本。Token Hub 不在调用链上。
>
> 注意：本图只表示产品能力，不表示部署结构。

我读了两遍没找到的答案，单独占了半行。

好用的地方在拆分，不在字数。五层关系拆成五行，每行一个标签，想查哪层，眼睛直接落过去。

翻车的地方在"为什么"。严格版里 Education 只剩"可独立使用"，它为什么不走 Gateway 被删了。原因就半句：Education 的实践训练放在 Cowork 和 AI PPT 里做。少了这半句，读的人会以为它是一座没接模型的孤岛。

那条建议里的解法我照搬了：要求做到"80% 的 ASD-STE100"。松一点，原因能保住。规范按英文词数卡句长，中文我改成按字数。现在固定下来的提示词：

```
按 80% 的 ASD-STE100 规则写汇报，中文。
第一行写需要我做的事，没有就写"无"。
一句只说一件事，不超过 30 个字。动词开头。
同一个东西始终用同一个名字。
每个问题保留一句原因。
```

---

STE 解决了"在不在链上"，可五层关系怎么串起来，五行字还得靠脑子拼。我又追了一句：用 HTML 输出，做成能点的架构图。

它交回来一个单文件 `index.html`，顺手导出了 SVG 和 PNG：

![Agent 交回来的 Zaokit 产品架构图，左侧虚线框就是 Token Hub 的旁路关系](/assets/images/screenshot-20261003-zaokit-architecture.webp)

答案在图上。Token Hub 单独放在左边一列，跟应用层、Gateway 之间连的是虚线，旁边一行小字："旁路治理，不代理内容，不是调用必经环节"。Education 的箭头绕过 Gateway，直接落到"学习实践"，底部场景路径补上了那半句原因。

我读两遍文字没找到的东西，图上用一种线型就交代了。

页面顶上有四个场景按钮。点 PPT 创作，其他产品暗下去，从"个人"开始，zaokit.app、AI PPT、Gateway、文本推理、图像生成一格格亮起来，一直走到"演示文稿"，底部的演示事件跟着往下滚。下面是我把四个场景切了一遍的录屏：

<video autoplay muted loop playsinline preload="metadata" poster="/assets/images/screenshot-20261003-zaokit-architecture.webp" style="width:100%;border-radius:12px;border:1px solid #27272A;">
  <source src="/assets/images/anim-20261003-zaokit-architecture-scenes.mp4" type="video/mp4">
  <img src="/assets/images/anim-20261003-zaokit-architecture-scenes.gif" alt="Zaokit 架构页四个场景依次播放：PPT 创作、Cowork 协作、教学学习">
</video>

原页面也放上来了，按 1 到 4 切场景，点产品框看详情：

<div style="position:relative;width:100%;aspect-ratio:1600/1180;border-radius:12px;overflow:hidden;border:1px solid #27272A;background:#09090B;margin:1.2em 0;">
  <iframe src="/assets/demos/zaokit-architecture/index.html" title="Zaokit AI 产品架构交互页" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;border:0;"></iframe>
</div>

手机上看得窄，可以[全屏打开](/assets/demos/zaokit-architecture/index.html)。

目录里还有一个 `selftest.json`：它给自己的页面跑了 60583 项检查，零报错。

两年前，这种页面得排前端工期，没人会为"我想看懂自己的架构"批预算。今天它是一句提示词，看完就扔。

建议里还有一级是讲解视频：3Blue1Brown 风格的动画，配 ElevenLabs 或本地 TTS 的旁白。这一级我还没跑通，下周试。

---

这次测试让我想明白一件事。

那段文字说明里，每个点都对。值钱的是点和点之间的线：Token Hub 和调用链之间那条虚线，Education 和 Gateway 之间那条没连上的线。

连线恰好是 AI 最擅长的。它能把所有可能的线都画出来。哪条线要停下来处理，哪条先放着，哪条看着不对劲，这一步还在我手里。

说白了就是品味。被 Claude 封过 17 个号的人，看到"所有订阅绑在同一个支付通道上"这条线，后背会发紧。模型画得出这条线，它的后背不会发紧。

![体力活交给Agent，看懂留给自己](/assets/images/illust-20261003-disposable-artifacts.webp)

<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底到暖黄渐变，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面分上下两层：下层是一个工坊，几个小机器人在流水线上组装网页窗口、图表和小视频卡片，组装完的产品被放进一个标「用完即弃」的纸箱。上层是一个瞭望台，一个人物拿着望远镜俯看流水线，手边一块白板写着「看懂 判断 拍板」。顶部中文「体力活交给Agent 看懂留给自己」，底部「一次性软件 不再是浪费」。中文清晰可读。 --ar 2.35:1 -->

我现在的规矩就一条：Agent 交上来的东西，两分钟没看懂，不往下读，让它换个形式重交。STE 不行就画图，图不行就做网页。

省下来的时间，留给挑线。

---

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)、[你的数字分身](https://cowork.zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[被 Claude 封了 17 个账号之后，我把它的家搬到了澳洲](/claude-17-bans-australia-homecoming) · [Grok Bot：一人公司第一次被做成了产品](/grok-bot-one-person-company) · [OpenClaw 2.0 Team 模式来了，Grok Bot 用户该不该换？](/openclaw-team-vs-hermes)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，一个人做 AI 产品。每天开着 Claude Code、Codex、Agy、Cursor 和 Grok Bot 干活，最先扛不住的是我自己的阅读速度。现在它们都按飞机维修手册的规矩给我汇报，要我做的事写在第一行。点和线交给模型，挑哪条线，我自己来。*
