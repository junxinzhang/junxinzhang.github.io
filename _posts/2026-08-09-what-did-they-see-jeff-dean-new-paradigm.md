---
layout: post
title: "他们到底看到了什么？让 Jeff Dean 离开待了 27 年的 Google"
date: 2026-08-09
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260809-what-did-they-see.webp
tags: [featured, AI, Jeff Dean, Discovery Loop, Agent, 范式跳跃, Codex, Claude Code, 递归自我改进, Zaokit]
slug: what-did-they-see-jeff-dean-new-paradigm
description: >
  Jeff Dean 在 Google 待了 27 年，走了。Sanjay Ghemawat、Quoc Le、Oriol Vinyals 跟着一起走了。
  他们成立了 Discovery Loop，要做 AI 自动化科学研究。据报道 Anthropic 签了约 100 亿美金算力合同。
  所有人都在问同一个问题：他们到底看到了什么？
faq:
  - question: "Jeff Dean 为什么离开 Google？"
    answer: "2026 年 8 月 5 日，Jeff Dean 与 Sanjay Ghemawat、Quoc Le、Oriol Vinyals 一起离开 Google，成立了公益公司 Discovery Loop，专注 AI 自动化科学研究。Dean 说：'我们认为 AI 有机会更完整地自动化传统上非常依赖人力的实验循环。'方向是用 AI 自动化完整实验循环，并探索用 AI 构建更强 AI。"
  - question: "什么是递归自我改进？"
    answer: "递归自我改进是指 AI 系统自主改进自身的能力——不是人写代码让模型变强，而是 AI 自己做实验、自己发现规律、自己迭代。Discovery Loop 公开方向是自动化完整实验循环，并关注 AI 构建更强 AI；把人从循环里移出去，是对这条线的进一步判断。"
  - question: "为什么说 Codex 和 Claude Code 即将成为过去式？"
    answer: "这是判断，不是已发生事实。当前的 Agent 工具本质上还是'人下指令、AI 执行'的模式；前沿实验室的信号指向下一代系统可能变成 AI 自己定义任务、自己选择工具、自己迭代改进。差距不在工具好不好用，而在范式本身可能变了。"
  - question: "这对普通开发者意味着什么？"
    answer: "短期内 Codex 和 Claude Code 仍然是最好的工具，但要意识到它们可能是过渡形态。真正要建的能力不是'会用某个 Agent 工具'，而是'理解 Agent 系统设计'——因为工具会换，但理解范式迁移的能力不会过时。"
---

这周 X 上有一种奇怪的氛围。

不是吵架，不是发新品。是一群在前沿实验室工作的人，密集地发了很多意味深长的推文。大意都差不多：

**「我最近看到的一些东西，让我觉得现在的工具很快就会显得原始。」**

然后什么都不说了。

> **当 Google 第 30 号员工决定离开待了 27 年的公司去创业，当 Anthropic 据报道签下约 100 亿美金的算力合同并开始招芯片团队，当 Google Maps 开始跑 Agent——他们到底看到了什么？最合理的解释，可能指向 AI 智能体的下一个范式。**

![他们到底看到了什么？让 Jeff Dean 离开待了 27 年的 Google](/assets/images/cover-20260809-what-did-they-see.webp)

## 一、Jeff Dean 走了——这才是最大的信号

8 月 5 日，一条新闻炸了整个 AI 圈：

**Jeff Dean、Sanjay Ghemawat、Quoc Le、Oriol Vinyals，四个人一起从 Google 离职，成立了一家叫 Discovery Loop 的公益公司。**

这不是普通的跳槽。Jeff Dean 是 Google 第 30 号员工，1999 年加入，待了 27 年。MapReduce、TensorFlow、TPU、Google Brain——他参与或主导了 Google 技术史上几乎所有重大节点。Sanjay Ghemawat 是他合作了二十多年的搭档。Quoc Le 是 Google Brain 早期核心成员。Oriol Vinyals 是 DeepMind 核心研究员。

四个人同时走，我的判断是：**他们在 Google 内部看到了某种东西，但判断这件事更适合在小团队、新结构里做。**

Dean 说了一句话：

> **"我们认为 AI 有机会更完整地自动化那个传统上非常依赖人力的实验循环。"**

他们的联合声明更直接：

> **"AI 的下一个伟大前沿，不是回答问题，而是做出发现。"**

Discovery Loop 公开方向是：**用 AI 自动化完整实验循环，并探索用 AI 构建更强的 AI。** 报道把它放在「递归自我改进」这条线上——不是人写代码让模型变强，而是 AI 自己做实验、自己迭代。Radical Ventures 和 Khosla Ventures 领投，Alphabet 参与。母公司跟投前员工创业公司，说明这件事至少被允许、被支持；至于为什么不在 Google 内部做，那是另一层判断。

![Jeff Dean 27年后的选择](/assets/images/illust-20260809-jeff-dean-departure.webp)

## 二、不止 Jeff Dean——所有人都在动

Jeff Dean 走了是最大的信号，但不是唯一的。把最近两周的事情摊开看：

| 时间 | 事件 | 信号 |
|------|------|------|
| 7 月 24 日 | Anthropic 发布 Claude Opus 5 | 偏长程 Agent 能力，强调自验证、多步迭代 |
| 8 月 4 日 | 据报道 Anthropic 与云创业公司 Volta 签下约 100 亿美金算力合同 | Agent 工作负载需要大规模专属算力 |
| 8 月 5 日 | Anthropic 开始招芯片设计团队 | 垂直整合，不满足于只租算力 |
| 8 月 5 日 | Jeff Dean 等四人离职创业 | AI 自动化科学研究 |
| 8 月 6 日 | Google Maps 上线 Agentic 功能 | 从导航工具变成能订餐、订酒店的助手 |

这些事件单独看都是新闻。放在一起看，指向同一个方向：

**前沿实验室不是只在打磨现有的 Agent 工具，而是在给下一量级的系统补能力、补算力、补基础设施。**

Claude Opus 5 的发布说明里，有几个细节值得注意：官方示例里，它**自己搭了一套计算机视觉流水线**去还原 FreeCAD 零件；在 Frontier-Bench 上刷新了成绩；JetBrains 的工程师说，这是他们见过的 Claude 代际里最清晰的一次解题能力跃迁。

这不是「更快更强」四个字就能概括的。**模型开始更像会自己验证、自己迭代的执行者。**

![三大前沿实验室齐发力](/assets/images/illust-20260809-three-labs-racing.webp)

## 三、Tibo 那条 1.6M 浏览的帖子，说穿了什么

在 Jeff Dean 官宣离职的前一天，8 月 4 日，**OpenAI Codex 负责人 Tibo**（Thibault Sottiaux，[@thsottiaux](https://x.com/thsottiaux)）在 X 上发了一条帖子，**1.6M 浏览**，原文是：

> **"Given some of the results I'm seeing recently, it's pretty clear Codex is a good harness. But it will seem primitive in 2-3 months and we're about to go through another major evolution in how we use AI at the frontier. The next generation of models need more than your laptop."**

翻译成大白话：**Codex 确实是个好工具——但两三个月后它就会显得原始。我们即将经历又一次 AI 使用方式的重大演化。下一代模型需要的，不止是你的笔记本。**

注意身份：Tibo 不是站在外面评 Codex 的人。公开报道里，他是 Codex 的 engineering lead / Head of Codex 之一，参与并主导了现代 agentic Codex 的建设。

**所以这句话的分量完全不一样：造 Codex 的人，在说自己做的东西很快会显得原始。**

我前两天在 [你的公司电脑，可能连 Agent 的门都进不了](/agent-runtime-beyond-laptop-infrastructure) 里引用过这条帖子，当时还没把身份钉死。结合 Jeff Dean 离职创办 Discovery Loop 的消息，现在拼图完整了。

**Tibo 这条帖子至少传递了三层信号：**

**第一层：Codex 不是终态，只是一个过渡性的好工具。** 他用了 "harness"（套具）这个词——不是 "platform"、不是 "system"，是套在马身上的工具。工具好用，但马要换了。自己造 harness 的人这么说，比任何测评都狠。

**第二层：时间窗口极短——两三个月。** 不是「未来某天」，是 2026 年底之前。他说 "I'm seeing recently"——已经看到了，不是猜测。这意味着前沿实验室内部已经跑出了某种和现在完全不同的东西。

**第三层：本地笔记本级别的 harness 很快触到天花板。** "The next generation of models need more than your laptop" 这句话，呼应了第二节那些基础设施信号——据报道的百亿算力合同、芯片团队、Opus 5 对长程任务的强化——**算力需求正在从「单机」往「集群」走。**

这条帖子之所以引爆讨论，不是因为结论多惊人，而是因为**发帖的人既在造 Codex，又用「我最近看到的结果」这种现在时说话**。他不像在空谈时间表，更像在提前给市场打信号。

评论区也是同一类气氛：很多人点头，很少人公开细节。没人把内部 demo 摊开讲，但「我也有同感」的味道很浓。

**这种「先有内部体感、后有公开产品」的氛围，上一次大规模出现，是 2022 年底 ChatGPT 发布前。**

## 四、最合理的解释：他们看到了自动化实验循环

把 Jeff Dean 的行动、Codex 负责人 Tibo 的暗示、Anthropic 的基础设施布局叠在一起，**最合理的解释**不是「模型再大一点」，而是：

**AI 正在被推向「自己改进研究循环」这条线。**

不是「参数更多」那种改进。是**AI 自己做实验、自己验证假设、自己迭代方案**——把过去需要一个团队花很久的研究循环，压缩到更短的时间。

这就是 Jeff Dean 说的「自动化实验循环」。也是把 Tibo 那句「Codex 两三个月后会显得原始」接上的那根线。

**当前的 Agent 工具——Codex、Claude Code、WorkBuddy——本质上还是「人下指令，AI 执行」。** 你告诉它做什么，它去做。你不说，它不动。

下一代系统如果按这条线走，就不是这样了。**AI 自己定义任务、自己选择工具、自己迭代改进。** 人的角色从「指挥官」变成「审计员」——你不再事无巨细地告诉它怎么做，而是检查它做得对不对。

这个跳跃的量级，可能和从 ChatGPT 聊天到 Agent 自主执行一样大。

## 五、为什么说 Codex 和 Claude Code 即将成为过去式

我不是在贬低这些工具。我自己每天都在用。八月初 [用 Codex 两小时交三端](/codex-stitch-two-hours-three-ends-recall)，杠杆约 50 倍，体感非常强。

但冷静下来想：**50 倍杠杆，本质上还是「人 × 50」。**

下一代系统要做的事情不是给你 50 倍杠杆。是**把你从循环里拿出去**。

| 现在 | 下一跳 |
|------|--------|
| 人下指令，AI 执行 | AI 自己定义任务 |
| 人审代码，AI 改 | AI 自己验证、自己迭代 |
| 一次对话完成一个任务 | 持续运行，自主探索 |
| 工具是 Agent | Agent 是同事 |

这也是为什么 Anthropic 一边签大规模算力合同，一边招芯片团队。不是因为今天的聊天框已经吃不下这些资源——而是因为**下一代 Agent 如果真的长时间运行、并行多任务、自己搭工具链，算力需求会完全换一个量级**。

一台笔记本，扛不住那种工作负载。

这话不是空谈。我自己就有亲身体会。

三月我写过 [月投 650 刀订阅 AI Agent](/agent-arms-race-650-dollars-per-month)：Claude Code + Codex + Gemini Ultra，固定月费约 650 刀；同时跑 20+ Agent 时，M2 Max 已经扛不住，只能再入一台 64G M5 Pro 专门跑 Agent 集群。六月又写了 [那台 M5 Pro 三个月涨了 6000](/ai-storage-baseline-macbook-price-up)——内存和存储才是 AI 时代真正在变贵的东西。

**月花 650 刀、两台 Mac 并行，都只是今天这一代 Agent 的门槛。** Tibo 说下一代需要的不止是笔记本，我信——因为我已经在今天这一代上，被笔记本卡过一次了。

![从工具到同事：Agent 范式跳跃](/assets/images/illust-20260809-paradigm-shift.webp)

## 六、这件事对你意味着什么

先别焦虑。三件事值得现在想清楚：

**第一，短期内 Codex 和 Claude Code 仍然是最好的工具。** 「即将成为过去式」不等于「今天就不能用」。下一代系统商业化还需要时间，而你手上的项目不等人。该用就用。

**第二，要建的能力不是「会用某个 Agent 工具」，而是「理解 Agent 系统设计」。** Codex 会过时，Claude Code 会迭代，但理解范式迁移的能力不会过时。弄清楚 Agent 需要什么运行环境、怎么做状态管理、怎么设计工具链——这些才是可迁移的能力。

**第三，Jeff Dean 用脚投票的方向值得认真看。** 一个在 Google 待了 27 年、参与过几乎所有重大技术决策的人，判断「AI 自动化科学研究」是下一个伟大前沿——这不是空话，这是他把职业生涯压上去了。

## 写在最后

压成五句：

1. **Jeff Dean 走了——Google 第 30 号员工，27 年后带着三个顶级研究员创办 Discovery Loop，做 AI 自动化科学研究**
2. **Codex 负责人 Tibo 那条 1.6M 帖子更像预告——造工具的人自己说 Codex 两三个月后会显得原始**
3. **Anthropic 据报道签约 100 亿算力合同、并招芯片团队——下一代 Agent 更可能需要专属基础设施，不是你的笔记本**
4. **最合理的解释是：自动化实验循环——AI 自己做实验、自己迭代，而不只是回答问题**
5. **Codex 和 Claude Code 还是好工具，但它们本质仍是「人 × 50」——下一跳如果成立，是把人从循环里拿出去**

土话一句：

**别再只问哪个 Agent 工具更好用了。造工具的人，已经在往下一个世代押注了。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[你的公司电脑，可能连 Agent 的门都进不了](/agent-runtime-beyond-laptop-infrastructure) · [月投 650 刀订阅 AI Agent](/agent-arms-race-650-dollars-per-month) · [我那台 M5 Pro，三个月涨了 6000](/ai-storage-baseline-macbook-price-up) · [WorkBuddy 和 Codex 谁更强？你问错了](/workbuddy-codex-positioning-threshold)

公开参考：[TechCrunch — Jeff Dean and other top AI researchers are leaving Google](https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/) · [Anthropic — Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) · [TechCrunch — Google Maps agentic features](https://techcrunch.com/2026/08/06/google-maps-adds-agentic-features-including-food-ordering-and-hotel-bookings/) · [Reuters — Anthropic chip design team](https://www.reuters.com/business/anthropic-build-in-house-chip-design-team-claude-hire-engineers-2026-08-05/)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。造工具的人已经在往下一个世代押注了——你准备好了吗？*
