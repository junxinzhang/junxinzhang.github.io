---
layout: post
title: "你还在切 chunk 做向量？RAG 早就不是这回事了"
date: 2026-08-06
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260808-rag-agentic-evolution.webp
tags: [featured, AI, RAG, Agentic RAG, GraphRAG, Self-RAG, 检索增强生成, 知识图谱, 向量检索, Zaokit]
slug: rag-to-agentic-rag-evolution
description: >
  2023 年我开始做 RAG，全网就一套动作：切 chunk、灌向量库、取 top-k。今天再看，那只是 RAG 的婴儿期。
  从无脑检索到会自己决定"用什么工具、查几轮"的 Agentic RAG，这条路走了不到三年，但差了两个范式。
faq:
  - question: "RAG 和 Agentic RAG 有什么本质区别？"
    answer: "传统 RAG 是固定管道：切 chunk → 向量检索 → 取 top-k → 塞进 prompt 生成。Agentic RAG 是让 AI 智能体自己决定用什么工具（向量库/网页/API/SQL）、查几轮、怎么合成，是从固定流程到自主决策的范式跳跃。"
  - question: "GraphRAG 解决了什么问题？"
    answer: "传统向量检索只做局部语义匹配，碰到多跳推理、全局总结类问题就无力。GraphRAG 把文本抽成实体–关系知识图谱，用图结构做多跳推理，但全量构建成本高，LazyGraphRAG 把成本降到了 0.1%。"
  - question: "Self-RAG 和 CRAG 是什么？"
    answer: "都是给 RAG 加'质检员'。Self-RAG 用反思 token 让模型自己决定要不要检索、检索到的内容对不对；CRAG 用轻量评估器三路径纠正——正确的直接用、错误的重写或联网、模糊的混合处理。解决的是'检索到垃圾也不知道'的问题。"
  - question: "现在企业做 RAG 应该从哪一代开始？"
    answer: "别从 2020 年的基础 RAG 起步。最低标准是带重排和质量评估的 Modular RAG；如果业务有多跳推理需求，考虑 LightRAG 或 GraphRAG；如果查询复杂度差异大，加 Adaptive RAG 路由。2026 年入场，至少跳到第三代。"
---

2023 年我开始做 RAG 的时候，全网教程就一套动作：

**把文档切成 chunk，灌进向量库，查询时取 top-k，拼进 prompt，完事。**

那时候觉得这就是 RAG。今天回头看，那只是 RAG 的婴儿期。

> **大部分人还停在"切 chunk 做向量"的阶段，以为自己在用 RAG。真正的 RAG 已经进化到 AI 自己决定用什么工具、查几轮、怎么合成。这中间差的不是几篇论文，是"固定管道"和"自主智能体"之间的范式鸿沟。**

![从切 chunk 到自己找信息：RAG 这三年走了多远](/assets/images/cover-20260808-rag-agentic-evolution.webp)

## 一、先给结论：RAG 不是一种技术，是一条进化路线

很多人把 RAG 当成一个固定方案——检索增强生成，不就是"先搜后答"吗？

不是。RAG 是一条还在快速分裂的技术树。从 2020 年 Lewis 等人的原始论文到今天，它至少分化出了五代，每一代解决的问题都不一样：

| 阶段 | 时间 | 核心解决的问题 | 一句话 |
|------|------|--------------|--------|
| 基础 RAG | 2020 | 知识不在模型里 | 先搜后答 |
| 模块化 RAG | 2022–2023 | 管道太僵硬 | 像乐高一样组合 |
| 反思+图谱 | 2023–2024 | 检索到垃圾也不知道 | 给 RAG 装质检员和结构 |
| 路由优化 | 2024–2025 | 什么都走 RAG 太贵 | 简单直答，复杂才检索 |
| Agentic RAG | 2025–2026 | 固定流程不够用 | AI 自己决定怎么找 |

这条线的走向很清楚：**从人设计管道，到 AI 自己决定怎么找信息。**

## 二、2020–2023：从"无脑检索"到"模块化乐高"

2020 年 Lewis 等人的 RAG 论文是起点：DPR 稠密检索 + 向量相似度 + 生成器。它第一次让 LLM 能"外接知识库"，缓解幻觉和时效性。

但这一代的问题很明显：**无脑检索**。所有文本切成 chunk 做向量索引，查询时取 top-k 就完事。chunk 彼此孤立，检索粗糙，对复杂问题无力。

2022 年 ColBERTv2 把"单向量匹配"改成 token 级多向量 + MaxSim 延迟交互，匹配精度上了一个台阶；残差压缩把存储降 6–10 倍。检索器本身从"粗"变"准"。

同期，Modular RAG 的思路出来了：RAG 不该是一条固定管道，而是一堆可编排模块——检索、重排、生成，像乐高一样按需组合。

**这一代解决的是"怎么让检索更准"和"怎么让管道更灵活"。但它还是个固定流程——你设计好管道，它就照着跑。**

![基础 RAG 到模块化 RAG](/assets/images/illust-20260808-basic-to-modular-rag.webp)

## 三、2023–2024：给 RAG 装上"质检员"和"知识图谱"

上一代最大的坑是：**检索到垃圾也不知道。**

top-k 返回的结果质量参差不齐，但生成器不管三七二十一全都拿来用——结果就是"一本正经地胡说八道"，而且引了来源看起来还挺靠谱。

Self-RAG 和 CRAG 就是给 RAG 装的"质检员"：

| 方案 | 做法 | 解决什么 |
|------|------|----------|
| **Self-RAG** | 用反思 token 让模型自己判断：要不要检索？检索到的对不对？ | 模型不再无脑用检索结果 |
| **CRAG** | 轻量评估器三路径：正确→直接用；错误→重写或联网；模糊→混合 | 检索到垃圾时自动纠偏 |

同一时期，另一条线在解决"结构"问题。

**RAPTOR** 用递归摘要树组织文档，适合全局性、多跳、总结类问题——向量检索擅长局部匹配，但"这篇文档整体在说什么"它答不了。

**GraphRAG** 走得更远：把文本抽成实体–关系知识图谱，用图谱做多跳推理。微软的 GraphRAG 用 Leiden 社区摘要做全局问答；HippoRAG2 用个性化 PageRank 做精准路由。

但图谱路线有个硬伤：**全量构建太贵。** 这也催生了后面 LazyGraphRAG 的出现。

![Self-RAG 质检流程](/assets/images/illust-20260808-self-rag-quality.webp)

## 四、2024–2025：不是什么问题都值得 RAG

前三代的进化方向都是"更准、更强、更结构化"。但到了 2024 年，大家发现一个土问题：

**简单问题也走 RAG，太贵了。**

"今天周几"不需要检索向量库；"这段代码有没有 bug"不需要知识图谱。Adaptive RAG 的思路很直接：**按查询复杂度动态路由——简单问题直接 LLM 答，复杂问题才走多步检索。**

与此同时，LazyGraphRAG 把图谱路线的成本问题解决了：社区摘要不在索引时预算，而是延迟到查询时才算。**索引成本降到 GraphRAG 的 0.1%。** 这意味着图谱不再是大厂专属。

2M token 上下文窗口出来后，很多人问：长上下文能不能直接替代 RAG？

答案是**不能替代，但可以分工**：

- 简单查询 → RAG（几分钱）
- 复杂多跳 → 长上下文（更贵但更准）
- 视觉文档 → ColPali

ICLR 2026 的 GraphRAG-Bench 给出了经验法则：**图的价值随查询复杂度上升。** 简单问题上图谱没优势，复杂多跳上它碾压纯向量。

同期火过一阵的 SAG（Search-Augmented Generation），本质是绕开向量库直接用搜索引擎——思路对但格局小，到了 Agentic RAG 阶段，搜索只是工具箱里的一个选项。SAG 不是主线进化，更像是 RAG 管道越来越复杂时的一次实用主义反弹。

**这一代的核心认知是：RAG 不该一刀切，该按需分流。**

![RAG 路由分流](/assets/images/illust-20260808-adaptive-rag-routing.webp)

## 五、2025–2026：AI 自己决定怎么找信息

终于到了今天这一代：**Agentic RAG。**

前面所有代际的共同点是——**人设计管道，系统按管道跑。** 管道更灵活了、有质检了、会路由了，但本质还是人在设计流程。

Agentic RAG 把最后这层也交出去了：让 AI 智能体自己决定"用什么工具（向量库/网页/API/SQL）、查几轮、怎么合成"。

更激进的是 RL 端到端训练路线：

| 方案 | 做法 | 效果 |
|------|------|------|
| **Search-R1** | 用 RL 训练 LLM 学会"何时搜、搜什么" | Qwen2.5-7B 上比普通 RAG 提升 41% |
| **DeepRetrieval** | 直接以检索指标（recall@k、NDCG）为奖励优化查询 | 查询质量本身被强化学习优化 |
| **MCTS-RAG** | 蒙特卡洛树搜索融进推理 | 把"找信息"变成搜索树博弈 |

这条线的意义不在于某个方案提升了多少百分点，而在于**范式本身的跳跃**：

**从"固定流程"走向"会自己找信息的智能体"。**

这和 Agent 领域的大趋势完全一致。我在 [组织还在信息化，别人已经在跑智能体](/agentic-org-vs-informatization-six-months) 里写过：核心变化不是工具更强，而是执行主体从人变成了 AI。RAG 这条线，走的是同一个方向。

![Agentic RAG：AI 自主决策](/assets/images/illust-20260808-agentic-rag-agent.webp)

## 六、2023 年做 RAG 的体感

说回我自己。

2023 年我开始做 RAG，踩过的坑现在看全是教科书级别的：

- **chunk 切太小**，检索出来的全是碎片，模型拼不出完整答案
- **chunk 切太大**，噪音太多，top-k 里一半是废话
- **没有重排**，向量相似度高不等于语义相关
- **没有质量评估**，检索到错误信息照样生成，用户根本分不出来

这些问题在 2024 年都有了系统性的解决方案。但**大部分企业的 RAG 系统，到今天还停在 2022 年的水平**——切 chunk、灌向量、取 top-k，一条管道走到底。

不是因为不知道有更好的方案，是因为**没有人告诉他们"你的 RAG 只是婴儿期"。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，在内部的知识检索、PPT 生成、图文创作流水线里，已经从基础 RAG 迁到了带路由和质量评估的架构。不是因为技术信仰，是因为**基础 RAG 的幻觉率在真实业务里根本扛不住。**

## 写在最后

压成五句：

1. **RAG 不是一种技术，是一条还在快速分裂的进化路线**——从 2020 年到 2026 年，至少五代
2. **大部分企业还停在 2022 年的"切 chunk 做向量"**——以为自己在用 RAG，其实只碰到了起点
3. **Self-RAG、CRAG 给检索装了质检员**——检索到垃圾也不知道，是最常见也最致命的坑
4. **GraphRAG 走结构化路线，LazyGraphRAG 把成本打下来了**——图的价值随查询复杂度上升
5. **Agentic RAG 是当前终态**——AI 自己决定用什么工具、查几轮、怎么合成，从固定管道到自主智能体

土话一句：

**别再跟人说"我们上了 RAG"了。先看看你的 RAG 是哪一代的。**

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

延伸：[组织还在信息化，别人已经在跑智能体](/agentic-org-vs-informatization-six-months) · [你的公司电脑，可能连 Agent 的门都进不了](/agent-runtime-beyond-laptop-infrastructure) · [WorkBuddy 和 Codex 谁更强？你问错了](/workbuddy-codex-positioning-threshold)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。2023 年切 chunk 做向量，2026 年 AI 自己找信息。技术在进化，你的 RAG 也该升级了。*
