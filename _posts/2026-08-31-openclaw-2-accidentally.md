---
layout: post
title: "OpenClaw 发布了 2.0，你还在用吗？"
date: 2026-08-31
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260831-openclaw-2.webp
tags: [featured, AI, OpenClaw, Agent, 开源, 协作, Zaokit]
slug: openclaw-2-accidentally
description: >
  OpenClaw 停更七周，扔出 2.0。933 位贡献者、16000 个 PR，把项目翻了一半。
  本来只想改安装和浏览器，改着改着把整个架构拆了重建。真正值得盯的不是功能列表，是开源 Agent 从个人工具走向多人协作。
faq:
  - question: "OpenClaw 2.0 最大的变化是什么？"
    answer: "表面上是功能全面升级，实质是架构推倒重建。安装简化、浏览器重做、新增 Shared Cloud Sessions 多人协作。整个项目从个人 Agent 工具转向团队协作平台。"
  - question: "Shared Cloud Sessions 是什么？"
    answer: "多人可以加入同一个 Agent 的实时工作会话，共享任务和上下文。OpenClaw 官方称之为 multiplayer。Agent 不再是一个人的事。"
  - question: "为什么停更了七周？"
    answer: "团队原本只想简化安装和重构浏览器端，结果牵一发动全身，改动波及整个系统。此前 230 天发了 106 个版本，这次被迫停下来做一次性的大规模重构。"
  - question: "OpenClaw 和闭源 AI 工作空间的区别？"
    answer: "OpenClaw 开源、不绑定单一模型和 AI 厂商。用户可以接入 ChatGPT、Claude、本地模型等任意组合。这是它和闭源 AI 工作空间产品最根本的差异。"
---

OpenClaw 停更了七周。

对一个平均两天就发一个版本的项目来说，七周没动静，几乎等于失踪。

然后它一声不吭，扔出了 2.0。

![OpenClaw 2.0：改着改着把房子拆了](/assets/images/cover-20260831-openclaw-2.webp)

这个版本有多大？933 位贡献者参与，其中 569 人是第一次给 OpenClaw 提交代码。合并超过 16000 个 PR——这个数字差不多是 OpenClaw 从诞生到现在全部 PR 的一半。

一个版本，重写了半个项目。

更有意思的是，2.0 原本根本没计划做这么大。

团队最开始只想干两件事：简化安装流程，重做浏览器端。按照他们此前 230 天发 106 个版本的节奏，这顶多是两三个小版本的活。结果动刀以后发现，入口改了，底层也得跟着改。底层改了，中间层也撑不住。一层一层剥下去，最后把整个项目翻了个底朝天。

![推倒重来：修门变成了拆房子](/assets/images/illust-20260831-rebuild.webp)

这件事做过工程的人都见过——你以为只是修个门框，撬开一看，承重墙有裂缝。修墙的时候发现地基也在晃。你被迫做一个决定：是糊上去继续住，还是索性拆了重盖。

OpenClaw 选了拆。

在那之前两天一更的节奏，其实已经在暗示问题了。更新越快，债务积累越快。快到某个临界点，你不停下来还债，后面每一步都在往屎山上堆。

这跟过去一年 Vibe Coding 是同一个故事。写得快、发得快、堆得快，直到有一天回头看，发现没人敢碰那坨代码了。OpenClaw 团队用七周时间做了一个正确但痛苦的选择：停下来，把债还了。

---

改完以后到底变了什么？

最直接的：上手门槛砍掉了。

以前装 OpenClaw 是一件让人头疼的事——配 API Key、选模型、调参数，光前置步骤就能劝退一半人。2.0 的做法很聪明：首次安装时，它会自动扫描你电脑里已经有的东西。ChatGPT 订阅、Claude 订阅、API Key、本地跑的模型——能用的直接用上，不需要你再从头配一遍。

装好就能聊。剩下的配置，边用边调。

![安装简化：装好就能用](/assets/images/illust-20260831-easy-setup.webp)

浏览器端被完整重做了。以前的 Web 版更像个管理后台，2.0 打开就是聊天界面，可以继续之前没完成的任务，可以实时看 Agent 在干什么。不用非得装桌面端，打开浏览器就能接着工作。

Memory 和 Skills 也动了大手术。Agent 能记住之前聊过什么，后台自动整理长期记忆，还能把重复任务沉淀成 Skill——等于 Agent 给自己写了一份 SOP。这个方向我觉得走对了。AI Agent 如果每次开聊都像新认识你一样，跟搜索引擎有什么区别？记忆和技能积累才是 Agent 真正值钱的地方。

自动化也加强了。定时任务、循环任务、邮件和 Slack 事件触发，更适合无人值守地长期运行。它想让 Agent 不只是你问一句它答一句，而是真的能独立跑一段完整的工作流。

但以上这些，说到底还是"做得更好"。真正让我觉得 OpenClaw 方向变了的，是另一个东西。

---

Shared Cloud Sessions。OpenClaw 官方管它叫 multiplayer。

![Multiplayer：Agent 从个人工具变成团队工作空间](/assets/images/illust-20260831-multiplayer.webp)

你可以把另一个人拉进你当前的 Agent 工作会话。不是分享一段对话记录，是实时加入——任务在跑、上下文在，对方进来直接接着干。Agent 已经积累的信息、已经走过的步骤，不需要从头交接，整个 Session 连人带活一起共享。

这个能力看着不起眼，但它改变了 Agent 的定位。

OpenClaw 最早就是一个个人 Agent。你一个人装，一个人用，一个人和 AI 聊。现在市面上几乎所有 AI Agent 工具都是这个模式——单人、单机、单线程。

Shared Cloud Sessions 把这个边界打破了。Agent 从"我的工具"变成"我们的工作空间"。

我自己做 [Zaokit Cowork](https://cowork.zaokit.app) 的时候也想过这个问题。AI Agent 如果永远只能一个人用，它的天花板就是个人效率的上限。真正能撬动更大价值的，是 Agent 进入团队协作——一个人启动的任务，另一个人能接；AI 跑了三天的调研，换个同事来直接看结果接着推。

OpenClaw 团队自己就是这么用的。他们现在用 OpenClaw 来开发 OpenClaw。团队内部的真实协作需求，倒逼出了 multiplayer。

这跟闭门造车设计出来的功能不一样。它来自自己的痛点。

---

还有一件事值得说。OpenClaw 2.0 继续开源，继续不绑定任何一家模型厂商。

你可以用 ChatGPT，可以用 Claude，可以接本地模型，可以混着用。它的定位很清楚：我是运行层，不是模型层。你选择信任谁的模型是你的事，我只负责把 Agent 跑起来。

![开源不绑模型：你选谁的脑子是你的事](/assets/images/illust-20260831-open-source.webp)

这条路线在商业上不一定最聪明。绑定一个模型做深度优化，用户体验更容易做好。但从用户角度看，不被锁死在一家厂商手里，长期来看更安全。

我观察到一个趋势：开源 Agent 项目正在从"技术爱好者的玩具"往"能用的生产工具"走。OpenClaw 2.0 把安装简化到装好就用、浏览器做成一等入口、加上多人协作，这些都不是在秀技术，是在降门槛、拉用户。

但我也有个疑问：真的还有多少人在用？

在国内，OpenClaw 的存在感一直不算高。做类似方向的项目起了又死，死了又起。每次有大版本更新，一波人冲上去装，折腾两天发现配置太复杂、模型调用太贵、Agent 干不了什么正经活，然后卸载。

OpenClaw 2.0 能不能打破这个循环，得看接下来几个月的留存数据。

不过有一点我比较确定：Agent 从单人工具走向多人协作，这个方向是对的。不是因为 OpenClaw 做了，是因为这就是工具演化的自然路径。编辑器从单人用到多人协同用了二十年，代码仓库从单人到多人用了十年，AI Agent 这条路会走得更快。

OpenClaw 2.0 可能不是最终赢家。但它指了一个方向：**Agent 的未来不是一个人对着屏幕聊天，是一群人围着同一个 Agent 干活。**

---

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)、[你的数字分身](https://cowork.zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。**

---

延伸：[桌子对面没有人](/one-person-company-story) · [传统企业做 AI 转型，卡点不在工具，在组织](/enterprise-ai-org-conflict) · [硬件为王：从 SpaceX 造涡轮机到 AGI 逼近](/hardware-is-king-spacex-agi)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Agent 的未来不是一个人聊天，是一群人围着它干活。*
