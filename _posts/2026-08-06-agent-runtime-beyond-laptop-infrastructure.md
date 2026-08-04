---
layout: post
title: "你的公司电脑，可能连 Agent 的门都进不了"
date: 2026-08-06
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260806-agent-runtime-beyond-laptop.webp
tags: [featured, AI, Agent, Codex, Claude Code, 运行环境, 基础设施, 本地Agent, 云端推理, Zaokit]
slug: agent-runtime-beyond-laptop-infrastructure
description: >
  外企办公设备装不了本地 Agent、读不到凭证、跑不了 runtime——这不是 IT 刁难你，是 Agent 的运行环境
  正在从「个人电脑上的一个程序」升级成需要专属基础设施的重系统。下一代模型的能力已经强到，
  单靠本地笔记本电脑 + 简单循环已经不够用了。
faq:
  - question: "为什么外企办公电脑跑不了 AI Agent？"
    answer: "不是模型问题，是运行环境问题。公司设备通常锁死管理员权限、禁止安装非白名单软件、限制网络出口。Agent 需要本地 runtime（Node/Python）、需要读取你的代码仓库凭证和项目状态、需要长时间占用进程——这些在管控设备上全被卡死。"
  - question: "Agent 为什么不能完全在云端跑？"
    answer: "云端 Agent 可以跑通用推理和代码生成，但真正干活需要接触你的本地文件系统、你的 git 状态、你的环境变量、你的私有仓库凭证。WorkBuddy 也好 Codex 也好，不带本地 runtime 的 Agent 永远差最后一公里。"
  - question: "Tibo 那条 1.6M 浏览的帖子说了什么？"
    answer: "科技领域知名创作者 Tibo（@thsottiaux）8 月 4 日在 X 上公开发言：Codex 是一个好的 harness，但两三个月后会显得原始；下一代模型需要的不止是你的笔记本。意思是 Agent 的使用方式马上要再跳一次台阶，本地级别的 harness 很快触到天花板。"
  - question: "Agent 运行环境升级意味着什么？"
    answer: "意味着 Agent 从「电脑上装个程序」变成「需要专属算力、持久状态、多机协作」的重系统。一百个并行任务不可能挤在一台笔记本上跑，需要云端大规模推理、更复杂的工具生态、更持久的记忆与状态管理。"
---

最近在外企工作的朋友问我：你天天说 Agent 能干这干那，我公司电脑连 Claude Code 都装不上，怎么玩？

**不是你不想装。是公司设备根本不给你装。**

没有管理员权限，没有 Node 环境，没有 Python runtime，git 凭证走公司代理读不到，连终端都是阉割版。你有一个最聪明的大脑，但它没有手、没有眼睛、读不到你桌上的任何一张纸。

这不是 IT 在刁难你。这是一个更大的问题的缩影：

> **Agent 的运行环境，正在从「个人电脑上的一个程序」升级成需要专属基础设施的重系统。你的笔记本，可能真的不够用了。**

![你的公司电脑，可能连 Agent 的门都进不了](/assets/images/cover-20260806-agent-runtime-beyond-laptop.webp)

## 一、没有 runtime 的 Agent，就是个聊天框

先把问题摊开。为什么 Agent 不是装个 app 就完事？

Agent 要真正帮你干活，至少需要四样东西：

| 需要 | 干什么 | 公司电脑给不给 |
|------|--------|--------------|
| **本地 runtime** | 跑脚本、装依赖、起服务 | 多数锁死 |
| **凭证与身份** | 读 git 仓库、调 API、访问内部系统 | 代理+白名单拦住 |
| **文件系统访问** | 读你的代码、改你的文件、写测试 | 部分只读或沙箱 |
| **持久进程** | 长任务不断、状态不丢 | 休眠策略会杀掉 |

少了任何一样，Agent 就退化成聊天框——你问它一句，它答你一句，但它**干不了活**。

这就是为什么很多人装了 Copilot 觉得「也就那样」：不是模型不行，是**运行环境被阉割了**，模型的手脚被绑住了。

想象一下：你招了一个顶级程序员，但不给他电脑、不给他代码权限、不让他进办公室。他能帮你干什么？最多隔着门给你喊两句建议。

这就是今天大部分外企员工用 AI 的真实状态。

![没有 runtime 的 Agent 就是个聊天框](/assets/images/illust-20260806-agent-no-runtime.webp)

## 二、纯云端能完成 100% 的工作吗？

有人会说：那直接用云端 Agent 不就行了？Codex 不就是云端跑的吗？

云端 Agent 能做很多事。但它有一个结构性的短板：

**它不在你的工作现场。**

你的项目状态、你的 `.env` 文件、你本地分支上昨晚改到一半的代码、你私有仓库的访问令牌、你跑了三天才配好的开发环境——这些东西不在云端。

| 云端 Agent 能做 | 云端 Agent 做不到 |
|----------------|-----------------|
| 通用代码生成 | 读你本地未提交的代码 |
| 沙箱内运行测试 | 用你的数据库凭证连真实环境 |
| 独立 repo 的任务 | 跨多个私有仓库协作 |
| 标准环境的项目 | 你公司特殊的构建链和 CI |

WorkBuddy 也好、Codex 也好、任何云端方案——**不带本地 runtime 的 Agent，永远差最后一公里。**

真正高效的 Agent 工作流，是**本地与云端的混合体**：本地 harness 读你的状态、管你的凭证、守你的上下文；云端提供算力、推理、长任务执行。缺任何一端，都跑不满。

这不是理论讨论。我自己每天用 Claude Code 和 Codex，最大的体感就是：**本地 runtime 才是 Agent 能力的地基。** 没有它，再强的模型也只是在空中画饼。

## 三、有人已经看到了下一跳

现在说一件更大的事。

8 月 4 日，科技领域知名创作者 **Tibo**（[@thsottiaux](https://x.com/thsottiaux)）在 X 上发了一条帖子，**1.6M 浏览**，原文是：

> **Given some of the results I'm seeing recently, it's pretty clear Codex is a good harness. But it will seem primitive in 2-3 months and we're about to go through another major evolution in how we use AI at the frontier. The next generation of models need more than your laptop.**

![Tibo (@thsottiaux) on X — 1.6M 浏览](/assets/images/screenshot-20260806-tibo-codex-harness.webp)

翻译成大白话：**他最近看到的一些结果表明，Codex 确实是个好工具——但两三个月后它就会显得原始。我们即将经历又一次 AI 使用方式的重大演化。下一代模型需要的，不止是你的笔记本。**

这条帖子引爆了讨论，因为它点出了三层意思：

**第一层：Codex 不是终态，只是一个过渡性的好工具。**

Codex 已经很能干了——我八月一号写过 [用 Codex 两小时交三端](/codex-stitch-two-hours-three-ends-recall)，体感杠杆约 50 倍。但即便如此，在前沿玩家的眼里，它已经是「很快会显得原始」的东西。

**第二层：使用方式要再跳一次台阶，不是线性小改。**

不是「Codex 变快一点、聪明一点」，而是整个使用范式要变。就像从 ChatGPT 聊天到 Agent 自主执行是一次跳跃，下一次跳跃的量级至少一样大。

**第三层：本地笔记本级别的 harness 很快触到天花板。**

这才是最关键的一句。下一代模型的能力已经强到，单靠本地笔记本电脑的算力加上简单的 Agent 循环，已经不够用了。

![Codex 只是起点，不是终态](/assets/images/illust-20260806-codex-just-beginning.webp)

## 四、为什么你的笔记本不够用了

把技术细节摊开，不绕概念。

**问题不是模型太笨，而是模型太能干。**

当 Agent 能力跳到下一代，它不是只帮你写一个函数、改一个 bug。它要同时做的事可能是：

- 并行跑 10 个子任务，每个都需要独立的运行环境
- 持续运行数小时，不能因为你合上笔记本就断掉
- 调用多个外部工具和 API，每个都有自己的认证链路
- 维持跨任务的记忆和状态，不是每次从零开始
- 遇到卡点时自动 escalate 到更强模型或人工审批

一台笔记本能扛住一个 Agent 跑一个任务。但如果你有一百个任务呢？

**你需要不止一台电脑。否则会卡死，会 OOM，会网络超时。**

这就是为什么 Agent 的运行环境正在升级：

| 现在 | 很快 |
|------|------|
| 笔记本上装一个 CLI | 需要专属算力实例 |
| 单 Agent 单任务 | 多 Agent 并行协作 |
| 跑完关掉 | 7×24 持续运行 |
| 状态在内存里 | 需要持久化状态和记忆系统 |
| 简单工具调用 | 复杂工具生态 + 权限管理 |
| 人盯着终端看 | 需要可观测 + 自动告警 |

换句话说：

**Agent 正在从「你电脑上的一个程序」，变成「一套需要基础设施支撑的系统」。**

就像网站从单机部署到上云、到微服务、到 K8s，Agent 的运行环境也在走同一条路——只不过快得多。

![Agent 运行环境升级路线](/assets/images/illust-20260806-runtime-evolution.webp)

## 五、这件事对你意味着什么

别把上面这些当远期预测。两三个月，很快。

### 1）外企员工：别等 IT 开口，先把本地环境搞定

如果你的公司电脑跑不了 Agent，那就用自己的设备。一台能装 Claude Code 或 Codex CLI 的开发机，现在是**生产力工具**，不是爱好。

这不是空话。三月我写过 [Agent 军备竞赛：每月 650 刀，还得再入一台 M5 Pro](/agent-arms-race-650-dollars-per-month)：M2 Max 扛不住多 Agent 并行，只能再加一台 64G M5 Pro 专门跑 Agent 集群。六月又写了 [那台 M5 Pro 三个月涨了 6000](/ai-storage-baseline-macbook-price-up)——内存和存储才是 AI 时代真正在变贵的东西。

工作电脑搞不定的，先用个人设备把非敏感任务跑通。等公司策略跟上来，你已经有了成熟的工作流可以平移。

### 2）技术负责人：Agent 基础设施该提上日程了

不是「给每个人买个 Copilot 账号」就叫 Agent 化。你需要考虑的是：

- Agent 跑在哪里？本地还是云端？混合比例怎么分？
- 凭证和权限怎么安全地交给 Agent？
- 长任务怎么管理、怎么监控、怎么回滚？
- 成本怎么控制——100 个 Agent 并行跑，token 费用谁买单？

我前天写过 [组织还在信息化，别人已经在跑智能体](/agentic-org-vs-informatization-six-months)：工具已经换成 Agent 了，但组织图纸还是信息化时代的。Agent 基础设施也一样——**你不能用管「桌面应用」的方式管 Agent。**

### 3）所有人：理解「运行环境」比理解「模型」更重要

大部分讨论聚焦在模型多聪明、参数多大、评测多高。但在实际工作中，瓶颈往往不是模型——

**而是 Agent 有没有手、有没有眼睛、有没有一个不会被杀掉的进程。**

模型是大脑。运行环境是身体。没有身体的大脑，干不了活。

## 写在最后

压成五句：

1. **外企办公设备装不了本地 Agent 环境——没有 runtime、没有凭证、没有持久进程，Agent 就是个聊天框**
2. **纯云端也补不全——你的项目状态、本地代码、私有凭证不在云上**
3. **Tibo 那条 1.6M 帖子说得很直白：Codex 两三个月后会显得原始，下一代模型需要的不止是笔记本**
4. **Agent 正在从「个人电脑上的程序」升级成「需要基础设施支撑的系统」**
5. **理解运行环境，比理解模型参数更重要——模型是大脑，环境是身体**

土话一句：

**别再争哪个模型更聪明了。先问问你的 Agent，有没有一台不会被公司 IT 杀掉的电脑。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，做的就是帮你不需要折腾本地环境，直接用上稳定靠谱的 AI 能力。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[Agent 军备竞赛：每月 650 刀，还得再入一台 M5 Pro](/agent-arms-race-650-dollars-per-month) · [我那台 M5 Pro，三个月涨了 6000](/ai-storage-baseline-macbook-price-up) · [产品召回三端，我用 Codex 和 Stitch 两小时交了](/codex-stitch-two-hours-three-ends-recall) · [组织还在信息化，别人已经在跑智能体](/agentic-org-vs-informatization-six-months)

公开参考：[Tibo (@thsottiaux) on X — Codex harness 原文](https://x.com/thsottiaux)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Agent 再聪明，没有运行环境就是空谈。大脑要有身体，才能干活。*
