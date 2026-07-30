---
layout: post
title: "LLM 不会给你最优排产，求解器会"
date: 2026-07-30
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260730-or-aps-llm.webp
tags: [featured, AI, 运筹学, APS, 排产, 排程, 库存调拨, OR-Tools, Agent, 求解器, Zaokit]
slug: or-aps-scheduling-inventory-llm-agent
description: >
  七月写过 AI 不止大模型，其中点名运筹学。今天落到 APS 排产排程与库存调拨：
  LLM 负责翻译约束和异常，MILP/CP-SAT 求解器负责算最优——别让聊天框替求解器。
faq:
  - question: "LLM 能不能直接做排产？"
    answer: "能聊计划、能写模型、能解释结果，但组合爆炸的最优解要交给 MILP / CP-SAT 等求解器。把 ChatGPT 当排产引擎，是选型错位。"
  - question: "APS 和运筹学是什么关系？"
    answer: "APS 是业务系统名；底下常见引擎是混合整数规划、约束规划、启发式。没有优化内核，APS 只是好看的甘特图。"
  - question: "库存调拨里 LLM 和求解器怎么分工？"
    answer: "LLM 整理多仓规则、缺货优先级、异常说明；网络流 / 多级库存优化算调拨量与路径。Agent 负责触发重算与解释，不负责硬算最优。"
  - question: "企业落地先做什么？"
    answer: "先钉目标函数与硬约束，再接 OR-Tools / 商用求解器；LLM/Agent 放在建模、数据对齐、异常闭环和人机解释层。能降级就别上全自动。"
---

七月我写过 [AI 被大模型绑架了](/ai-is-not-just-llm-full-landscape)：选型表里有一行很土——路径规划、资源调度，先考虑**运筹优化 + 强化学习**，而不是让 ChatGPT 算最优路线。

那一行很多人划过去了。今天把它落到真正会烧钱的场景：**APS 排产排程**，以及**库存调拨**。

两年前我写过一版 [APS 基础介绍](/aps)，偏系统模块视角。这篇不重复名词解释，只钉一件事：

> **LLM 负责把业务约束翻译成可求解问题；求解器负责在约束里找最优。把这两层搅在一起，排产项目最容易死在「看起来很智能」。**

![LLM 不会给你最优排产，求解器会](/assets/images/cover-20260730-or-aps-llm.webp)
<!-- baoyu-skill prompt: 2.35:1电影感横版封面，深蓝到墨黑渐变，冷静厚重工业科技质感。左侧聊天对话框半透明标中文「LLM·翻译约束」，右侧工业求解器芯片/甘特网格发光标中文「求解器·算最优」。中央粗体大字中文「LLM不会给你最优排产」。顶部副标中文「运筹学 × APS × Agent」。底部中文「翻译归模型，最优归求解器」。中文清晰可读。 --ar 2.35:1 -->

## 一、先把账算清：APS 吃的是运筹，不是聊天

APS（Advanced Planning and Scheduling，高级计划与排程）解决的是一类很硬的问题：

- 订单交期、产能、换型时间、模具、人员技能、物料齐套  
- 哪些工单先上哪台设备、什么时候开、开多久  
- 插单、设备故障、物料晚到时，怎么重排还不把整厂打乱  

这类问题在运筹学里通常落成：

| 方法 | 在 APS 里干什么 | 典型工具 |
|------|-----------------|----------|
| **MILP / MIP**（混合整数规划） | 产能、批量、交期、成本目标一起建模求最优或近似最优 | Gurobi、CPLEX、SCIP |
| **CP / CP-SAT**（约束规划） | 工序先后、机器独占、班次规则等离散约束很强时 | Google OR-Tools CP-SAT |
| **启发式 / 元启发式** | 规模太大、实时性要求高，求「够好且够快」 | 遗传算法、禁忌搜索、局部搜索 |
| **仿真 + 优化** | 先仿真瓶颈，再优化关键资源 | 数字孪生 / 产线仿真 |

Google 公开文档把调度写得很直白：员工排班、**Job Shop（车间作业排序）** 都是 OR-Tools 的标准场景；CP-SAT 面向整数与约束问题，常被用作调度主力——Interval、`AddNoOverlap`、工序先后，目标常是压 makespan。出处：[OR-Tools Scheduling](https://developers.google.com/optimization/scheduling) · [Job shop](https://developers.google.com/optimization/scheduling/job_shop) · [CP-SAT](https://developers.google.com/optimization/cp/cp_solver)。

工业级不是玩具题。Gurobi 公开的[宇通客车排产案例](https://www.gurobi.com/resources/case-studies/yutong-bus-production-planning)：定制客车约 **170–180 台/日开工**、约 **100 款并发车型**、**10 条产线**；网络流拆成 **6–10 个 MIP 序列**，单个规模大约 **10 万约束 / 6 万变量**；**Gurobi 约 45 分钟** 跑完序列，对照原先 **5 人团队约 9 小时** 手工排程。市售通用 APS 包，曾被评估为盖不住这种定制化与多目标。

翻译成厂长能听懂的话：

**APS 的灵魂不是「会说话的计划员」，是「在约束下给出可执行最优（或近似最优）方案」的引擎。**

大模型很擅长解释「为什么这单要插」「换型为什么贵」。它不擅长在上百台设备、上千道工序、无数互斥约束里，稳定给出**可证明更优**的排程。组合爆炸是数学题，不是语感题。

![APS 吃运筹不是聊天](/assets/images/illust-20260730-aps-or-stack.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景冷静科技。四层栈从下到上中文「数据·订单库存产能」「模型·目标与硬约束」「求解·MILP/CP-SAT/启发式」「界面·甘特与解释」。右侧大箭头指向中文「LLM在顶层·求解器在中层」。顶部标题中文「APS吃的是运筹，不是聊天」。底部中文「没有优化内核，只是好看的甘特图」。中文清晰可读。 --ar 2.35:1 -->

## 二、排产现场：三个真实卡点，对上三种数学武器

别从「AI 赋能制造」空谈。车间里常见三类题，对应不同武器：

### 1）Job Shop / 产线排序——工序先后 + 机器独占

工件要过车、铣、磨；每台机器同时只能干一件；换型要时间。这是经典 **Job Shop Scheduling**。约束密、离散强，CP-SAT 或专用调度启发式往往比「让模型自由发挥」靠谱。

### 2）有限产能主计划——交期、齐套、加班成本一起算

更上层是 MPS / 有限产能计划：本周接哪些单、外协多少、周末开不开线。目标函数通常是**延期惩罚 + 加班成本 + 库存持有**，变量多是整数（开不开线、做不做这批）。这是 MILP 主场。

### 3）实时重排——故障、插单、缺料

优化模型要能**热启动**：固定已开工、只动未开工、加软约束保护原计划稳定。Agent 的价值在这里开始露头——监听事件、拉齐数据、触发重算、把结果翻译成人话——但**重算本身仍是求解器的事**。

| 业务现象 | 先别做什么 | 更该做什么 |
|----------|------------|------------|
| 插单一句「帮我重新排」 | 直接让 LLM 输出完整甘特 | 更新约束 → 调求解器 → LLM 解释差异 |
| 设备坏了 2 小时 | 凭经验口头改三单 | 锁定在制、重优化后续、评估交期冲击 |
| 领导要「最优」 | 聊天框里拍脑袋排序 | 先定义目标函数：交期？换型最少？负荷均衡？ |

> **「最优」不是形容词，是目标函数写清楚之后，求解器在可行域里比出来的结果。**

![三类排产题三种武器](/assets/images/illust-20260730-three-weapons.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅对比信息图，深色背景。三列卡片中文标题「Job Shop排序」「有限产能主计划」「实时重排」，副标分别「CP-SAT/启发式」「MILP主场」「热启动+事件触发」。每列底部小字中文「机器独占」「交期·加班·齐套」「故障·插单·缺料」。顶部标题中文「三类题，三种数学武器」。底部中文「最优是算出来的，不是聊出来的」。中文清晰可读。 --ar 2.35:1 -->

## 三、库存调拨：另一张运筹试卷

排产解决「厂里怎么造」。调拨解决「货在网里怎么动」。

多仓、多级（工厂仓 → 区域仓 → 门店 / 客户）、缺货替代、运输时效、批次效期——这是供应链里的 **network optimization / multi-echelon inventory** 题：

- 从哪几个仓调多少到哪  
- 先保谁的服务水平  
- 调拨成本 vs 缺货损失 vs 积压风险  

经典做法仍是运筹与库存论：

| 层级 | 常见做法 | 说明 |
|------|----------|------|
| 单点补货 | 安全库存、再订货点、(s, S) | 规则简单，局部有效 |
| 多级库存（MEIO） | 跨节点同时定安全库存与内部服务水平 | 库存放在哪一层，往往比「各点各囤一点」更关键 |
| 网络调拨 | 多商品网络流 / 运输与库存联合优化 | 跨仓、跨线路、跨时效 |
| 滚动重算 | 定期或事件驱动 re-optimize | 和 APS 一样，要能热更新 |

单级各自最优，浪费常藏在**节点缝里**。MEIO 要的是网络总成本与服务水平，不是局部 KPI。对照见 [MEIO vs IO](https://www.microsoft.com/en-us/microsoft-cloud/blog/manufacturing/2018/06/22/multi-echelon-inventory-optimization-vs-inventory-optimization/)。SAP IBP 一类产品把 multi-stage inventory optimization 写成正式能力，而不是「大模型随便搬货」。

LLM 的位置仍是三块：**规则与例外入口**、**异常叙事**、**方案解释**。不该替代的是：运力、库存、服务水平下的**可执行调拨量**。

厂商叙事也收敛：在计划与优化底座上叠 agentic AI，做解释、异常与编排。Blue Yonder 2025 的 Ops Agent 话术是 See–Analyze–Decide–Act，不是替换求解器（[新闻稿](https://blueyonder.com/media/2025/blue-yonder-transforms-supply-chain-management-with-new-ai-agents)）；SAP 侧 Joule / agentic AI 往规划延伸（[Sapphire 报道](https://www.cio.com/article/3990312/sap-goes-all-in-on-agentic-ai-at-sap-sapphire.html)）。

![库存调拨是另一张运筹试卷](/assets/images/illust-20260730-inventory-network.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景冷静科技。左侧三层仓储节点中文「工厂仓」「区域仓」「门店」，箭头网络标中文「调拨量·路径·时效」。右侧两栏对比：上栏中文「LLM」条目「规则入口」「异常叙事」「方案解释」；下栏中文「求解器」条目「服务水平」「运力约束」「最优调拨」。顶部标题中文「货在网里怎么动」。底部中文「解释归模型，数量归优化」。中文清晰可读。 --ar 2.35:1 -->

## 四、LLM 和 Agent 到底干什么：四层分工，别抢方向盘

把系统拆成四层，选型会清爽很多：

| 层 | 谁主责 | 典型工作 | 失败长什么样 |
|----|--------|----------|--------------|
| **交互与意图** | LLM | 听懂「优先保大客户交期」「今晚只动 3 号线」 | 听错目标，排得再优也是错题 |
| **建模与数据对齐** | LLM + 工程师规则 | 自然语言 → 变量/约束/目标；主数据清洗 | 模型写错约束，求解器一本正经算错题 |
| **求解** | OR 引擎 | MILP / CP-SAT / 启发式求可行与更优 | 不可行、超时、局部最优 |
| **闭环与编排** | Agent / Workflow | 事件触发、重试、人审、回写 ERP/MES | 人成 cron；或无人乱改计划 |

这和我在 [从 PE 到 Graph](/pe-context-harness-loop-graph-evolution) 里说的「失败变贵，杠杆外移」是同一逻辑：  
排产场景里，**失败最贵的一层往往是「算错约束」和「算不动最优」**——前者靠建模纪律，后者靠求解器，不是靠更大的聊天模型。

研究侧两条线互相印证：

1. **OptiMUS**：LLM Agent 从自然语言建立并迭代 (MI)LP 与求解代码，再交 Gurobi。困难集相对既有方法提升超 30%；后续版 NLP4LP 上 GPT-4o 约 **73.7%** vs 标准约 **33.2%**——增益在**建模**，不是取消求解。出处：[arXiv:2402.10172](https://arxiv.org/abs/2402.10172) · [0.3 版](https://arxiv.org/html/2407.19633v3)。  
2. **Microsoft OptiGuide**：自然语言 what-if → LLM 改求解代码 → **组合优化求解器**出数 → LLM 解释；专有数据不必直接塞给模型。论文 GPT-4 端到端问答约 **93%**（不是排产最优率）。出处：[arXiv:2307.03875](https://arxiv.org/abs/2307.03875) · [MSR](https://www.microsoft.com/en-us/research/project/optiguide-genai-for-supply-chain-optimization/)。

> **LLM 擅长写/修优化模型；可行与更优解仍来自求解器。**

车间同构五步：**Agent 收集 → LLM 建模 → 求解器重算 → LLM 解释 + 人审 → Workflow 回写 ERP/MES/WMS**。能画清路径用 Workflow；动态工具调用用小范围 Agent——和 [Skill / Workflow / Agent](/llm-pretrain-posttrain-skill-workflow-agent) 的「能降级就降级」同构。

![四层分工别抢方向盘](/assets/images/illust-20260730-four-layers.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅流程图，深色背景冷静科技。从左到右四段箭头中文「意图理解」「建模对齐」「求解优化」「闭环回写」，角色标签分别「LLM」「LLM+规则」「MILP/CP-SAT」「Agent/Workflow」。中央大字中文「别让聊天框抢方向盘」。顶部标题中文「四层分工」。底部中文「OptiMUS证明：模型写题，求解器答题」。中文清晰可读。 --ar 2.35:1 -->

## 五、落地清单：比「上一个排产大模型」管用

1. **先写目标函数**——交期 / 换型 / 负荷 / 库存，权重不写清后面全是扯皮。  
2. **硬软约束分开**——安全与工艺是硬的；少改原计划、均匀加班用惩罚。全写成硬约束，求解器只会报不可行。  
3. **求解器匹配结构**——离散调度偏 CP-SAT；成本产能批量偏 MILP；极大规模用分解 + 启发式 + 滚动窗口；只要解释与 what-if，别假装在求最优。  
4. **Agent 先触发与解释，再自动下发**——建议→人审→低风险自动→跨仓/外协/改交期仍人在回路。裁判是业务指标与可行性，不是模型自信。  
5. **ERP/MES 接口与主数据**——工艺、节拍、换型矩阵脏，再强求解器也是精密地算错。

> **排产 AI 的竞争，表面是模型，底下是约束库、主数据和重算闭环。**

## 写在最后

压成五句：

1. **APS 的内核是运筹**——宇通级 MIP 序列用 45 分钟对 9 小时人工，不是聊天补全  
2. **库存调拨是网络 / MEIO 题**——服务水平与运力约束下求调拨量，浪费常在节点缝里  
3. **LLM 的主场是翻译与解释**——意图、规则、异常、what-if 叙事  
4. **Agent 的主场是闭环**——监听、建模、调求解器、人审、回写  
5. **OptiMUS / OptiGuide 证明的分工**——大模型写/修优化模型，求解器给可行与更优；别反着用来

土话一句：

**大模型让更多人「说得清约束」；运筹学让系统「算得动最优」。前者降低门槛，后者守住质量。少了求解器的 APS，只是会说话的 Excel。**

再补一句更硬的：

**排产的难点从来不是「生成一个计划」，而是「证明这个计划在约束下可执行」。LLM 会写约束，但不会替你承担不可行解的产线停机。**

两年前写 APS，是把它当制造系统模块。今天补刀，是因为 2026 年的空气里，「万物皆可 Agent」太容易把求解器挤出架构图。挤出去的那一天，你得到的不是智能工厂，是**自信的乱排**。

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，做的是把可用的 AI 能力送进真实交付——该接工作流接工作流，该接工具接工具，而不是让聊天窗口假装成排产引擎。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

延伸：[AI 被大模型绑架了](/ai-is-not-just-llm-full-landscape) · [制造型企业 APS](/aps) · [从 PE 到 Graph](/pe-context-harness-loop-graph-evolution) · [预训练是别人的工厂](/llm-pretrain-posttrain-skill-workflow-agent)

公开参考：[OR-Tools Job shop](https://developers.google.com/optimization/scheduling/job_shop) · [CP-SAT](https://developers.google.com/optimization/cp/cp_solver) · [Gurobi 宇通案例](https://www.gurobi.com/resources/case-studies/yutong-bus-production-planning) · [OptiMUS](https://arxiv.org/abs/2402.10172) · [OptiGuide](https://arxiv.org/abs/2307.03875) · [MEIO vs IO](https://www.microsoft.com/en-us/microsoft-cloud/blog/manufacturing/2018/06/22/multi-echelon-inventory-optimization-vs-inventory-optimization/) · [Blue Yonder Agents](https://blueyonder.com/media/2025/blue-yonder-transforms-supply-chain-management-with-new-ai-agents) · [SAP agentic AI 报道](https://www.cio.com/article/3990312/sap-goes-all-in-on-agentic-ai-at-sap-sapphire.html)

---

*我是 Jason，自己一个人做 AI 产品。排产要的是约束下的最优，不是对话里的自信。翻译归模型，最优归求解器。*
