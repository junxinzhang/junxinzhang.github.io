---
layout: post
title: "预训练是别人的工厂，你能摸到的是后训练"
date: 2026-07-22
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260722-llm-pretrain-posttrain.webp
tags: [featured, AI, 大模型, 预训练, 后训练, SFT, Skill, Workflow, Agent, 微调, Zaokit]
slug: llm-pretrain-posttrain-skill-workflow-agent
description: >
  预训练是别人的工厂，后训练才是你能摸到的装配线。有条件的用户才走厂商微调：训练付费 →
  model ID → API 再付费；多数人更常靠提示词、检索与 Skill。Skill 是 SOP，Workflow 是人定下一步，Agent 是模型定下一步。
faq:
  - question: "预训练和后训练分别在干什么？"
    answer: "预训练在大规模语料上做 next-token prediction，先学会语言与常识；后训练再用 SFT、RL/偏好对齐等方法，把底座塑成会听话、会干活的助手。你日常用的聊天模型，几乎都是预训练加后训练之后的产品。"
  - question: "普通人怎么做后训练？要自己搭训练集群吗？"
    answer: "一般不用自己搭集群。有条件时走厂商微调接口：准备示范数据、创建训练任务、按训练用量付费，拿到 fine-tuned model ID 后再按 API 付费调用。但自助微调并不人人可开——OpenAI 在收紧、Anthropic 官方不提供；多数人更常靠提示词、检索与 Skill。"
  - question: "Skill、Workflow、Agent 怎么分？"
    answer: "Skill 是可复用的 SOP/能力包；Workflow 是人写死每一步的编排；Agent 是由 LLM 在运行时动态决定下一步。Skill 不负责「谁决定下一步」，它嵌在 Workflow 或 Agent 里被调用。"
  - question: "是不是上了 Agent 就比 Workflow 更先进？"
    answer: "不是。能降级就降级：路径能画清、要审计，优先 Workflow + Skill；路径写不全、环境动态，再上小范围 Agent。复杂会放大延迟、成本与错误。"
---

最近身边几个朋友来问，如何区分这些概念：预训练、SFT、强化学习、Skill、Workflow、Agent。

有人拿它们互相解释，越解释越像玄学；有人直接宣布「Agent 取代一切」，把半自动脚本也叫 Agent。更常见的是另一种情况——既被要求「懂大模型」，又分不清：自己到底该调 API、该微调，还是该上编排。

我这篇只做扫盲底座，不重复我写过的[程序员提效 vs 老板赚钱](/workflow-agent-programmer-vs-boss)。先把账本摊开：

**模型怎么变听话；Skill、Workflow、Agent 各管哪一层。**

![预训练是别人的工厂，你能摸到的是后训练](/assets/images/cover-20260722-llm-pretrain-posttrain.webp)
<!-- baoyu-skill prompt: 2.35:1电影感横版封面，深蓝夜色到冷青渐变，冷静厚重的科技质感。画面三层横截面：底层冷灰基岩标中文「预训练·工厂」，中层装配线标中文「后训练·SFT/RL」，上层三工位分别标中文「Skill」「Workflow」「Agent」。中央粗体大字中文「先别吵Agent，先分清账本」。顶部副标中文「大模型扫盲」，底部中文「预训练是别人的，后训练你才摸得着」。中文清晰可读。 --ar 2.35:1 -->

## 一、大模型先拆两段：预训练与后训练

别一上来谈「智能」。把模型想成两段工。

**预训练（Pre-training）** 是打地基。  
在海量文本（以及越来越多的多模态数据）上，模型做一件事：给定上文，预测下一个 token。这一步吃算力、吃数据、吃工程，几乎是少数实验室和云厂商的事。产出是 base model——会续写、见过很多模式，但**不天然会当助手，也不天然会按你的规矩办事**。

**后训练（Post-training）** 是上岗培训。  
底座已经在了，后训练要解决：更听话、更有用、更安全。常见路径：

| 路径 | 在干什么 | 数据形态 |
|---|---|---|
| **SFT 监督微调** | 用「问题 → 标准答案」示范，教格式与指令跟随 | 对话对 / 示范样本 |
| **RL / RLHF 等** | 用排序、打分或可验证奖励，偏向「更好」的回答 | 偏好对、奖励信号 |
| **DPO 等偏好优化** | 用不同数学路径逼近偏好对齐 | chosen / rejected |

Anthropic 的公开 glossary 把预训练写得很直：在大规模无标注语料上先学会 next-token prediction。Claude 这类产品本身也不是裸语言模型——做过 fine-tuning / RLHF 之后，才变成你看到的助手。

类比只记一句：

> **预训练 = 先丢进图书馆学会说话；后训练 = 再上岗学怎么当客服、怎么拒危险请求、怎么按规范交付。**

对绝大多数人：

**预训练不是你的战场。你能参与的，是后训练结果的使用，以及——在有条件时——对特定模型做轻量定制。**

![预训练 vs 后训练](/assets/images/illust-20260722-pretrain-vs-posttrain.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅对比信息图，深色背景，冷静科技质感。左栏冷蓝「预训练」标签中文「海量语料」「预测下一个token」「底座会说话」；右栏暖金「后训练」标签中文「SFT示范」「RL/偏好对齐」「助手才听话」。中央大字中文「不是同一道工序」。顶部标题中文「预训练 vs 后训练」。底部中文「预训练是工厂，后训练是上岗」。中文清晰可读。 --ar 2.35:1 -->

## 二、普通人真能摸到的后训练：厂商微调接口

这里要同时泼冷水、给实路。

**冷水：** 你几乎不会自己搭完整后训练流水线。那需要数据工程、训练基础设施、评估体系和对齐经验。把它当周末副业，通常会惨败。

**实路：** 不少厂商把监督微调做成了接口或控制台能力。形态大体一致：

1. 准备高质量示范数据（输入 → 期望输出）  
2. 上传数据集，校验格式  
3. 创建微调作业，选基座与训练参数  
4. 用你自己的评测集看是否比默认模型更稳  
5. **得到一个 fine-tuned model ID / endpoint，接入业务**

计费也拆成两段，别混：

| 阶段 | 你在买什么 | 常见付费方式 |
|---|---|---|
| **训练** | 用你的数据改一版模型行为 | 按训练 token × epoch，或按训练作业/时长 |
| **使用** | 调用这个定制模型 ID 做推理 | 再按 API 的 input/output token 付费 |

产出物不是「又一个聊天网页」，而是**可部署、可调用的模型标识**。后续和调用普通模型一样走 API，只是 model 字段换成你的 `ft:...` 或云上的 tuned endpoint。

三家现实差别，以 2026 年中官方文档为准：

| 厂商 | 一般用户自助微调 | 你得到什么 | 一句话 |
|---|---|---|---|
| **OpenAI** | 自助 fine-tuning 平台在收紧/关停中，新 org 已难新建 job | 存量可训用户 job 完成后仍为 `ft:...` model id | 训练+推理分计；**新人基本进不去** |
| **Anthropic** | Claude API **官方明确不提供** fine-tuning | 无标准 self-serve 产物 | 定制主路径是 prompt / tools / Skills |
| **Google** | Cloud 上提供 supervised fine-tuning 等 | tuned model / endpoint | 有，但绑云账号与配额 |

所以判断要反过来看：

> **多数人所谓「定制模型」，真实杠杆常常是提示词、检索、Skill 与工具，不是人人改权重。**  
> 微调适合「格式、语气、分类边界总对不齐」；  
> 缺最新事实、缺系统权限，优先 RAG 和工具调用，别先烧训练费。

数据脏、评测虚、任务本该靠检索，微调只会变成昂贵安慰剂。先问一句：问题是模型不懂你的格式，还是模型根本看不见你的业务系统？

![微调：训练付费 → model ID → 调用再付费](/assets/images/illust-20260722-finetune-api-flow.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅流程信息图，深色背景，冷静科技质感。五个节点从左到右发光箭头连接：中文「示范数据」→「创建训练」→「按训练付费」→「得到model ID」→「按API调用付费」。中央大字中文「训练一次，调用反复计费」。顶部标题中文「普通人能摸到的后训练」。底部中文「不是自己盖工厂，是买装配线工位」。中文清晰可读。 --ar 2.35:1 -->

## 三、Skill、Workflow、Agent：三层，不是三个竞品

如果问题出在「模型看不见你的业务系统」，那接下来三个词才是你真正该分清的。

后训练解决的是**模型本身听不听话**；落地业务还要解决**系统怎么组织调用**。  
Skill、Workflow、Agent 常被混称，其实对应三层不同问题。

Anthropic 在 [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) 里把边界钉得很白：

- **Workflow**：LLM 与工具沿**预定义代码路径**被编排  
- **Agent**：LLM **动态决定**自己的流程与工具使用  

他们还反复强调：先找最简单的解法；只有简单方案不够用时，再加复杂度。Agent 会带来更高延迟、更高成本，以及错误被放大的风险。

**Skill** 是另一层——不是「谁决定下一步」，而是**可复用的 SOP / 能力包**。  
Anthropic 后来把 Agent Skills 说成：给通用 agent 的 onboarding guide——一个文件夹，核心是 `SKILL.md`（名称、描述、指令），可附脚本与资料，按需加载。像新人入职手册：遇到这类事，按这套字段、校验、失败重试来。

对齐成一张表：

| 概念 | 一句话 | 谁决定下一步 | 典型形态 | 不是什么 |
|---|---|---|---|---|
| **Skill** | 可复用的 SOP / 能力包 | 不负责决策路径 | `SKILL.md`、提示+工具约定、技能包 | 不是完整系统，不是模型权重 |
| **Workflow** | 人写死编排路径 | **人** | 链式、路由、人工卡点、固定图 | 不是模型当场规划 |
| **Agent** | 运行时动态规划与用工具 | **LLM** | tool-use 循环、开放目标 | 不是任意多步骤脚本 |

嵌套关系只记一句：

> **Skill 提供「这一类事怎么做」；  
> Workflow 把步骤串成固定流水线；  
> Agent 在运行时自己决定调用哪个 Skill、哪件工具、是否重试。**

反共识的一点：

**不是 Agent 越强越先进，而是你越能把任务降级成 Workflow 和 Skill，系统通常越稳、越便宜、越好维护。**  
Agent 留给「真的写不全」的那一段，不是默认皇冠。

这和我写过的[你说的 Agent，八成只是个 Workflow](/workflow-vs-agent-what-is-ai-agent)同一条线，只是今天补底座：没有后训练讲清楚的「会听话的模型」，上面三层都在空转。

![Skill / Workflow / Agent 三层](/assets/images/illust-20260722-skill-workflow-agent.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅三栏架构信息图，深色背景，冷静科技质感。左栏冷青「Skill」标签中文「SOP·能力包」「不决定路径」；中栏冷蓝「Workflow」标签中文「人写死下一步」「可审计」；右栏暖金「Agent」标签中文「模型定下一步」「开放目标」。中央竖排大字中文「三层不是竞品」。顶部标题中文「Skill · Workflow · Agent」。底部中文「能降级就降级」。中文清晰可读。 --ar 2.35:1 -->

## 四、选型只看三问，别先买名词

词混用的代价是买错方案。销售说 Agent，交付做的是 Workflow；老板要「自己的模型」，团队其实只需要更好的 Skill 和检索。

落地前只问三问：

1. **知识会变吗？**  
   会变 → 优先检索/工具，别把事实硬微调进权重。  
   不变且极稳的格式/语气 → 才考虑 SFT。

2. **路径能不能画出来？**  
   能画清、要审计 → Workflow + 节点内调用模型 + Skill。  
   画不清、环境动态 → 小范围 Agent，并给预算、工具白名单与人工接管。

3. **失败代价有多大？**  
   代价高 → 减少自主循环，增加确认节点与可回放日志。  
   代价低 → 才允许更激进的自动重试。

很多「我们要上 Agent」的项目，第一版其实是：

**Skill（稳定输出）+ Workflow（稳定路由）。**  
Agent 可以后置，等真实分支数据积累后再加。

## 写在最后

压成六句：

1. **预训练**——别人的工厂，产出通用底座  
2. **后训练**——SFT / RL 等把底座变成助手  
3. **普通人的后训练入口**——厂商微调接口：训练付费 → model ID → 调用再付费  
4. **Skill**——SOP / 能力包，不负责「谁决定下一步」  
5. **Workflow**——人决定下一步；**Agent**——模型决定下一步  
6. **工程原则**——能降级就降级；复杂只在必要时上

土话一句：

**先搞清模型怎么变听话，再谈要不要 Agent。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，核心仍是把能力送进真实交付链路，而不是停在聊天窗口。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)  
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)  
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)  
- [gift.junxinzhang.com](https://gift.junxinzhang.com)  
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。重点仍是那句：

**预训练是别人的工厂；你能摸到的是后训练与编排——Skill 管会不会这招，Workflow 管路怎么走，Agent 管路走不通时谁来改道。**

---

参考与延伸：

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)  
- [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)  
- [Agent Skills 开放标准](https://agentskills.io/home)  
- [OpenAI Supervised fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning) · [Deprecations](https://developers.openai.com/api/docs/deprecations)  
- [Claude Glossary](https://platform.claude.com/docs/en/docs/resources/glossary)  
- 站内：[你说的 Agent，八成只是个 Workflow](/workflow-vs-agent-what-is-ai-agent) · [程序员在提效，老板在赚钱](/workflow-agent-programmer-vs-boss) · [给老板讲清楚 AI Agent](/agent-loop-skill-token-explained-for-everyone)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，一个自己一个人做 AI 产品的创业者。预训练是别人的工厂，Agent 也不是默认皇冠。如果你也在分不清微调、Skill 和 Workflow，欢迎聊聊你现在卡在模型定制、流程编排，还是开放任务。*
