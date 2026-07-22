---
layout: post
title: "AI 扫盲：半小时基础知识培训"
date: 2026-07-23
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260723-ai-beginner-literacy.webp
tags: [featured, AI, 扫盲, 入门, 基础知识, 培训, 大模型, 提示词, Zaokit]
slug: ai-beginner-literacy-basics-training
description: >
  给完全不懂 AI 的人做一次扫盲：它是什么、能干什么、怎么开口问、哪里容易踩坑。
  半小时走完基础知识地图，先建立判断，再谈高级词。
faq:
  - question: "完全不懂 AI，先学什么？"
    answer: "先搞清四件事：大模型是什么、能帮你做什么、怎么写清楚需求、输出不可全信时怎么办。不必先背参数和 AGI。"
  - question: "大模型一句话怎么理解？"
    answer: "它根据你给的上下文，持续生成下一段合适内容。会写、会改、会总结；但不等于全知，也不等于自动接进你的业务系统。"
  - question: "新手第一次怎么用？"
    answer: "说清角色、任务、材料、格式和验收标准。例如：你是编辑，请把下面材料压成 200 字摘要，分三条，只保留事实。"
  - question: "最容易踩的坑有哪些？"
    answer: "把流畅当正确、把隐私随手粘贴、一次要它做完一切、从不检查关键数字与结论。"
---

这篇不是观点辩论，是**AI 扫盲**：给完全不懂的人做一次基础知识培训。目标：读完能打开对话产品，完成第一批有用的活，并知道哪里必须自己盯。进阶词另有专文；今天只铺底座。

![AI 扫盲：半小时基础知识培训](/assets/images/cover-20260723-ai-beginner-literacy.webp)
<!-- baoyu-skill prompt: 2.35:1培训封面。五块课卡「是什么」「能做什么」「三层」「提问」「避坑」。中央「AI扫盲」。顶部「半小时基础知识培训」。--ar 2.35:1 -->

## 一、它是什么

别从「会不会有意识」开始。入门一句话够用：

> **大模型（LLM）会根据你给的上下文，持续生成下一段最合适的内容。**

ChatGPT、Claude、Kimi、豆包一类，大多是：大模型 + 对话界面 + 工具包装。

| 词 | 入门理解 |
|---|---|
| **AI** | 很宽；眼下常指生成式大模型产品 |
| **大模型** | 核心引擎：读上下文，写后续 |
| **提示词** | 你给它的任务说明与材料 |
| **幻觉** | 说得像真的，但不一定对 |
| **Agent** | 不只聊天，会多步调用工具 |

预训练分层见[预训练是别人的工厂](/llm-pretrain-posttrain-skill-workflow-agent)。入门先会用、会验。

![大模型是什么](/assets/images/illust-20260723-what-is-llm.webp)
<!-- baoyu-skill prompt: 2.35:1输入→预测下一段→输出。中央「大模型一句话」。底部「会写≠全知」。--ar 2.35:1 -->

## 二、它能做什么

按「你交什么 → 它回什么」记：

| 场景 | 你给它 | 它常能帮你 |
|---|---|---|
| **写作** | 要点、对象、语气 | 草稿、改写、翻译、提纲 |
| **理解** | 长文、纪要、邮件 | 摘要、对照、找矛盾 |
| **学习** | 不懂的概念 | 分层解释、举例、自测题 |
| **办公** | 表格、方案框架 | 结构整理、清单、PPT 大纲 |
| **编程** | 报错、需求描述 | 改代码、写脚本、解释逻辑 |

边界：不自动知道公司内部最新事实；不自动拥有邮箱/ERP/审批权；可能把不确定说得很自信。

![能做什么](/assets/images/illust-20260723-can-do-map.webp)
<!-- baoyu-skill prompt: 2.35:1五宫格「写作」「理解」「学习」「办公」「编程」。中央「应用面一览」。--ar 2.35:1 -->

## 三、能力三层

| 层 | 含义 | 你怎么用 |
|---|---|---|
| **1. 会聊天** | 文本进，文本出 | 写稿、解释、头脑风暴 |
| **2. 会用工具** | 查、读、调系统 | 搜资料、读文件、接接口 |
| **3. 会循环干活** | 计划→执行→复盘→再改 | 多步任务、Agent 类产品 |

企业再加一句：**接进真实流程才算交付。** 细节见[给老板讲清楚 AI Agent](/agent-loop-skill-token-explained-for-everyone)、[你说的 Agent，八成只是个 Workflow](/workflow-vs-agent-what-is-ai-agent)。

![能力三层](/assets/images/illust-20260723-ability-three-layers.webp)
<!-- baoyu-skill prompt: 2.35:1阶梯 L1聊天 L2工具 L3循环。中央「能力三层」。--ar 2.35:1 -->

## 四、怎么提问

新手差距往往不在模型，在说明是否完整。用五件套：

1. **角色**——希望它扮演谁  
2. **任务**——要完成什么  
3. **材料**——已知信息贴全  
4. **格式**——条数、字数、表格、语气  
5. **验收**——什么叫做好，哪些不能编

示例：

> 你是企业培训助教。请把下面材料整理成新人 10 分钟能懂的说明：分「是什么 / 能做什么 / 注意什么」三节，每节不超过 80 字，不出现黑话。材料：……

坏问法：`帮我弄一下`、`写个方案`——缺对象、缺标准、缺材料。

![怎么提问](/assets/images/illust-20260723-how-to-ask.webp)
<!-- baoyu-skill prompt: 2.35:1五步「角色」「任务」「材料」「格式」「验收」。中央「提示词五件套」。--ar 2.35:1 -->

## 五、避坑与行动

| 坑 | 正确习惯 |
|---|---|
| **流畅当正确** | 关键事实、数字要复核 |
| **隐私随手贴** | 证件、密钥、未公开商业数据不进公共对话 |
| **一次要做完** | 先大纲，再分段，再润色 |
| **只看一次答案** | 要备选、列风险、标不确定 |
| **只追新名词** | 先稳定完成三类真实任务 |

本周行动：选定一个对话产品；做 3 个真实小任务（纪要、邮件、学习解释）；每次写清五件套；关键输出人工过一遍；再决定要不要上工具或流程接入。

## 写在最后

1. **大模型**——按上下文生成后续内容  
2. **产品**——模型 + 界面 + 工具包装  
3. **价值**——写作、理解、学习、办公、编程初稿  
4. **三层**——聊天、工具、循环；企业要接流程  
5. **提问**——角色、任务、材料、格式、验收  
6. **底线**——流畅≠正确；隐私与关键事实自己负责

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，把能力送进真实交付。唯一网站：[https://zaokit.app](https://zaokit.app)。企业服务：[grok.zaokit.com](https://grok.zaokit.com) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)。稳定靠谱的 AI 全家桶，开箱即用。

---

延伸：[预训练是别人的工厂](/llm-pretrain-posttrain-skill-workflow-agent) · [给老板讲清楚 AI Agent](/agent-loop-skill-token-explained-for-everyone) · [程序员在提效，老板在赚钱](/workflow-agent-programmer-vs-boss) · [你说的 Agent，八成只是个 Workflow](/workflow-vs-agent-what-is-ai-agent)

*我是 Jason，自己一个人做 AI 产品。AI 扫盲别追热闹词，先把基础知识走通。*
