---
layout: post
title: "从 PE 到 Graph：不是新词接力，是失败变贵了"
date: 2026-07-28
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260728-pe-to-graph.webp
tags: [featured, AI, Prompt Engineering, Context Engineering, Harness, Loop, Graph, Agent, LangGraph, Anthropic, Zaokit]
slug: pe-context-harness-loop-graph-evolution
description: >
  从 PE 到 Context、Harness、Loop、Graph，不是概念时尚，是上一层失败变贵后工程杠杆外移。
  多数「模型不行」的抱怨，其实是标错了楼层。
faq:
  - question: "这五层分别解决什么问题？"
    answer: "PE 解决说清楚；Context 解决喂对信息；Harness 解决长跑漂移与假完成；Loop 解决人不在时继续跑；Graph 解决多专长协同。嵌套楼层，不是互替版本号。"
  - question: "为什么说不是 buzzword 接力？"
    answer: "每一层都是被上一层硬瓶颈逼出来的。漂亮 prompt 变不出窗外事实；干净上下文挡不住第 N 步漂移；稳 harness 仍要人按启动键；单 loop 装不下多专长。失败变贵，杠杆外移。"
  - question: "什么时候才该上 Graph？"
    answer: "任务天然多专长、需要并行与可审计路由、或必须独立 verifier 节点时再上。多数日常任务一个好 loop 就够。过早上图，是在制造分布式系统问题。"
  - question: "和 Workflow / Agent 怎么对应？"
    answer: "Workflow 人写死下一步；Agent 模型动态决定下一步。Loop 是验证条件下反复跑；Graph 把多个节点用边连起共享状态。能降级就降级。"
---

社区每隔半年到一年，就会冒出一个新词。

Prompt Engineering 火的时候，大家天天改 system prompt。后来是 Context Engineering，Karpathy 一句话，风向就偏过去了。再后来是 Harness，Agent = Model + Harness 被讲成公式。接着是 Loop——有人说自己已经不 prompt 了，只写循环。到了 2026 年中，Graph 又上了桌面：多节点、共享状态、可恢复执行。

表面看是名词接力。我更愿意把它看成一件更土的事：

> **不是新词更好听，是上一层的失败变贵了，工程杠杆被迫外移。**

五月我写过 [从 Prompt 到 Harness](/ai-cognition-blind-spot-from-prompt-to-harness)，六月写过 [循环工程](/loop-engineering-ai-fde-must-know)，七月写过 [Harness 自我迭代](/harness-continuous-learning-self-iteration)。那几篇分别钉住单层。这篇只做一件事：**把五层串成同一条因果链，并回答——你现在卡在哪一层。**

![从 PE 到 Graph：不是新词接力，是失败变贵了](/assets/images/cover-20260728-pe-to-graph.webp)
<!-- baoyu-skill prompt: 2.35:1电影感横版封面，深蓝到暗青渐变背景，冷静厚重的科技质感。画面一条从左到右上升的五层台阶，每层发光标签中文「PE」「Context」「Harness」「Loop」「Graph」，台阶边缘有裂纹标中文「失败变贵」。中央粗体大字中文「失败变贵，杠杆外移」。顶部副标中文「PE→Context→Harness→Loop→Graph」。底部中文「多数模型不行，其实是标错楼层」。中文清晰可读。 --ar 2.35:1 -->

## 一、先把五层钉成诊断表，别当词汇表

很多人把这五个词当「升级路线图」：PE 过时了上 Context，再上 Harness，一直叠到 Graph。错。它们是**嵌套楼层**，不是互相作废的版本号。还有一句要先钉死：**这是瓶颈叙事，不是严格编年史**——ReAct 的 loop（2022）和 LangGraph（2024）在日历上早于 context/harness 的正名潮（2025–2026）。命名滞后于实践。

| 层级 | 工程对象 | 核心问题 | 典型失败 |
|---|---|---|---|
| **PE** | 单次指令 | 说清楚了吗 | 误解意图、格式跑偏 |
| **Context** | 调用时看到的一切 | 看到对的信息了吗 | 缺事实、噪声、context rot |
| **Harness** | 一次完整运行 | 长跑会不会漂 | 错误复利、假完成、权限失控 |
| **Loop** | 可重复的运行 | 人不在时还动吗 | 人成 cron、成本失控 |
| **Graph** | 多节点协作 | 多专长如何协同 | 职责污染、路由混乱 |

> **Prompt 是 Context 的一部分；Context 管道是 Harness 的子系统；Harness 撑起一次 Loop；Loop 往往只是 Graph 里的一个节点。**

![五层不是替代，是嵌套](/assets/images/illust-20260728-five-layers-nested.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景，冷静科技质感。五个同心或嵌套模块从内到外标中文「PE」「Context」「Harness」「Loop」「Graph」，箭头标注中文「包含而非取代」。右侧一列失败模式小标签中文「误解」「缺信息」「漂移」「人成瓶颈」「协调失败」。顶部标题中文「五层是楼层，不是版本号」。底部中文「烂 Prompt 仍会毒死漂亮 Graph」。中文清晰可读。 --ar 2.35:1 -->

## 二、根本原因：每一层都在给上一层的硬伤买单

### 1）PE：把话说清楚——然后撞上「窗口外没有事实」

Prompt Engineering 解决的是采样分布问题：角色、few-shot、输出格式、拒绝边界。同一模型，换说法，输出可以天差地别。天花板很干净：

**再完美的措辞，也变不出上下文里没有的事实。**

任务从「写一段文案」变成「用我的代码库/工单/合同做事」时，瓶颈立刻从「表达」变成「信息」。PE 没死，它只是从主角变成了外层系统里的一个被管理对象——Harrison Chase 的说法更直：PE 是 context engineering 的子集。

### 2）Context：把对的东西喂进去——然后撞上「长了会烂」

Karpathy 在 X 上那句被反复引用的话，把风向说得很白：

> **I really like the term "context engineering" over prompt engineering. It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.**  
> —— [Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626)

Anthropic 写得更硬：context 是**有限且有成本的注意力预算**；窗口越长，越容易 **context rot**——不是断崖，是召回与专注的渐变衰减。原则也很土：找**尽可能小的高信号 token 集合**。出处：[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)。

这一层的进步，是把「写一句 prompt」升级成「每一次 inference 都重新策展：什么进窗、什么压缩、什么落盘、什么按需检索」。`CLAUDE.md`、git 状态、按需读文件，本质都是 context 工程。

但 Context 仍有硬伤：**输入再干净，也没人盯执行过程。** 第 1 步对、第 7 步漂、第 20 步在错误上盖楼、最后自信「做完了」——不是「再喂两段文档」能治的。

### 3）Harness：给一次运行上缰绳——然后撞上「你还是那个启动按钮」

LangChain 把公式写得很干净：

> **Agent = Model + Harness。**  
> **If you’re not the model, you’re the harness.**  
> —— [The anatomy of an agent harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)

Harness 是模型之外的一切：工具注册与校验、权限门、状态与记忆、compaction、重试与恢复、日志与可观测性。模型提议，Harness 执行、观察、决定能不能继续。

Anthropic 在长程 agent 文里点名真实失败：一上来想 one-shot 整个项目、跨 session 失忆、过早宣布完成。应对很工程化——initializer 先搭环境与 feature list，coding agent 每次只啃一块，用 progress 文件和 git 交接，并用真实端到端检查而不是自评。出处：[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)。

这一层回答的是：**一次 run 能不能持续做对。** 天花板也清楚：再完美的 harness，默认仍控制「这一次」。启动、看结果、决定要不要再开一轮——人还在回路里。对高 stakes 单次任务没问题；一旦工作变成每天的 issue triage、每周的报表刷新，**你就变成了 cron。**

### 4）Loop：把自己从循环里拿出来——然后撞上「单专长装不下」

Loop 层的公开信号已经很明确。OpenClaw 作者 Peter Steinberger 的方向是：别再一条条 prompt coding agent，去设计那些**替你 prompt 它们的循环**。Claude Code 负责人 Boris Cherny 更直：自己不再亲自 prompt，有一堆 loops 在跑，活是写 loops。LangChain 随后把 loop engineering 收成可叠加的层：agent loop、verification loop、event-driven loop、hill-climbing loop。出处：[The art of loop engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)。

边界要钉死：

| | Loop | Harness |
|---|---|---|
| 管什么 | 做什么、何时做、何时算完 | 在哪跑、能碰什么、怎么恢复 |
| 像什么 | 节拍与裁判 | 舞台与护栏 |
| 缺了会怎样 | 安全但等你按按钮 | 无人看管却可能有 root |

Loop 真正难的不是画圆，是 **verifier 与终止条件**。弱验证的无人 loop，不会只是「给个坏答案」——它会整夜自信地生产垃圾，并按 token 计费。我在[循环工程](/loop-engineering-ai-fde-must-know)里写过：循环不难设计，难在养得起；今天再补一句——

> **Loop 的瓶颈往往不是模型，是裁判。**

单 loop 的天花板：它擅长**一个专长的重复**。研究、写作、评审、测试天然要不同上下文、不同工具、不同成功标准时，一个 loop 会开始什么都沾一点，什么都做不稳。

### 5）Graph：把多个节点织成组织——然后撞上「分布式系统税」

Graph 不是 2026 年凭空发明的词。LangGraph 的定位一直是：面向长程、有状态 agent 的**编排运行时**——节点做功、边负责路由、共享 state 在图上流动，并强调 durable execution、human-in-the-loop、失败后可恢复。出处：[LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)。

一个 loop，本质上是「单节点 + 自环」的最简图。Graph 是你需要 fan-out / fan-in、条件回环、确定性步骤与 agentic 步骤混跑、显式审计路由时，才真正必要的结构。它解决的是：**多专长如何可靠协同。**

它引入的新税也真实：状态契约、失败回边、并发冲突、职责污染、可观测性。过早上 Graph，常常不是更智能，是更贵、更难排障。

![失败变贵，杠杆外移](/assets/images/illust-20260728-failure-cost-shift.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅流程图，深色背景，冷静科技质感。从左到右五个阶段箭头连接，每段上方中文标签「PE」「Context」「Harness」「Loop」「Graph」，每段下方对应失败成本中文「误解变贵」「缺事实变贵」「漂移假完成变贵」「人成瓶颈变贵」「协调失败变贵」。中央大字中文「失败成本上移，工程杠杆外移」。顶部标题中文「五次跃迁的真正发动机」。底部中文「不是概念时尚，是账单在投票」。中文清晰可读。 --ar 2.35:1 -->

## 三、公开信号在收敛：大家其实在修同一栋楼

近一两年的高信号材料，表述不同，结构很像：Karpathy 推 context engineering；Anthropic 写注意力预算与 long-running harness；LangChain 钉 Agent = Model + Harness，并把 loop 叠成 agent / verification / event / hill-climb；LangGraph 管状态图与可恢复执行。

Claude Code、Cursor、OpenAI Agents SDK 路线不同，但 harness 要管的东西在趋同：loop、工具、状态压缩、权限门、恢复与可观测。OpenAI 更偏显式 multi-agent handoff；Claude Code / Cursor 更偏强单 agent + 深集成；组织级复杂交付，才会真正需要图与状态机。

> **模型在变强，但拉开差距的，越来越是模型周围那套系统能不能撑过第 50 步。**

同样一个模型，换 harness / loop / graph，端到端完成率可以差一截。评估 agent，只报模型名几乎不可复现，得报完整壳。

## 四、一张诊断图：别再把「模型不行」当万能锅

日常最有用的不是背定义，是**标楼层**：

| 你看到的现象 | 先修哪层 | 别先干什么 |
|---|---|---|
| 完全听不懂你的要求 | PE | 别先上多 agent |
| 话说得漂亮，事实错/过时/看不见业务系统 | Context | 别先微调权重 |
| 开头对，后面漂；或自信完成但一跑就挂 | Harness（多半是 verifier 弱） | 别只加更长 prompt |
| 结果其实还行，但必须你亲手启动才动 | Loop | 别只堆人工值守 |
| 单 agent 怎么调都平庸，任务天然多角色 | Graph | 别在 context 还烂时织大网 |

多数「模型能力不够」的吐槽，拆开后是：指令含糊；该看的没进窗、不该看的噪声进了窗；没有独立验收，只有模型自评；人还在当启动器和质检员；过早把一个团队问题塞进一个大脑。

我自己做产品时的默认顺序也很土：

**先把单任务的 context 和 harness 做扎实 → 再写带 verifier 的 loop → 最后在确实需要时才拆 graph。**

这和 Anthropic「先找最简单的解法」是同一纪律，也和我在 [Skill / Workflow / Agent](/llm-pretrain-posttrain-skill-workflow-agent) 里说的「能降级就降级」同构：路径能画清、要审计 → Workflow + Skill；路径写不全、环境动态 → 小范围 Agent + 强 harness；要无人值守重复 → Loop；要多专长并行与汇合 → Graph。

![你卡在哪一层](/assets/images/illust-20260728-diagnosis-floors.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅诊断信息图，深色背景，冷静科技质感。左侧电梯楼层示意图，五层按钮中文「5 Graph」「4 Loop」「3 Harness」「2 Context」「1 PE」，当前高亮某一层并标中文「先修最低卡点」。右侧对应现象条目中文「听不懂」「事实错」「长跑漂移」「等人启动」「多角色打架」。顶部标题中文「别把模型不行当万能锅」。底部中文「先标楼层，再动手术」。中文清晰可读。 --ar 2.35:1 -->

## 五、Graph 该不该上：三问比口号管用

Graph 最容易被写成「更高级」。我更建议用三问过滤：

1. **任务是否天然多专长？** 研究、写作、评审、测试是否需要不同工具集与成功标准？同一类活重复做，单 loop 通常更稳。
2. **是否需要显式路由与审计？** 合规、财务、发布闸这类场景，边和状态比「让模型自由发挥」更重要。确定性节点该手写就手写。
3. **有没有独立 verifier 节点？** 没有裁判的多 agent，只是把错误复利从串行变成并行。生成便宜，**判定够不够好**才贵。

若三问里你一个都答不硬，却已经在画六七个 agent 的漂亮拓扑——停一下。你可能不是在做编排，是在给自己制造分布式系统。反过来，若单 agent 上下文互相污染、串行太慢、关键步骤必须可回放，那 Graph 不是炫技，是必要的组织图。

## 写在最后

压成五句：

1. **不是 buzzword 接力**——是失败成本上移后的杠杆外移  
2. **五层嵌套不互替**——烂 prompt 仍会毒死漂亮 graph  
3. **公开材料已收敛**——Karpathy / Anthropic / LangChain / LangGraph 修同一栋楼  
4. **先标楼层再施工**——听不懂、缺事实、长跑漂、等人启动、多角色打架，手术不同  
5. **Graph 要克制**——多专长、要审计、有独立 verifier 再上；否则单 loop 更诚实

**模型是发动机。发动机不会自己赢。车会。2026 年拉开差距的，是谁先把失败变贵的那一层，工程化成壳、循环与图。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，做的也是同一条外移：把能力送进可交付的 harness 与工作流，而不是停在聊天窗口。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

延伸：[从 Prompt 到 Harness](/ai-cognition-blind-spot-from-prompt-to-harness) · [别再写提示词，去写循环](/loop-engineering-ai-fde-must-know) · [会学习的是外面那圈壳](/harness-continuous-learning-self-iteration) · [预训练是别人的工厂](/llm-pretrain-posttrain-skill-workflow-agent)

公开参考：[Karpathy](https://x.com/karpathy/status/1937902205765607626) · [Anthropic context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [Anthropic harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · [LangChain harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) · [Loop engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) · [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai) · 企业服务见 [projects](https://junxinzhang.com/projects.html)

---

*我是 Jason，自己一个人做 AI 产品。新词会过时，失败账单不会。先找准你卡在哪一层，再决定是改一句话，还是改整张图。*
