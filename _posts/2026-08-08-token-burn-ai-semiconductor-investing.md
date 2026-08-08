---
layout: post
title: "没烧过 token，就别说看懂 AI 半导体"
date: 2026-08-08
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260808-token-burn-ai-investing.webp
tags: [featured, AI, 投资, token, Agent Team, AI半导体, post-training, NVDA, HBM, MoE, Zaokit]
slug: token-burn-ai-semiconductor-investing
description: >
  从 LLM infra 到硬件原理再接回投资，能把这些讲透的人在中文圈凤毛麟角。
  作为每天泡在 post-training 一线的人，补一个体会：一线信息是双刃剑。
  没烧过 token 就看不懂供应链——这篇讲我怎么每天烧 3 亿 token 做 AI 投研。
faq:
  - question: "为什么说没烧过 token 就看不懂 AI 半导体？"
    answer: "AI 半导体投资的核心判断——GPU 定价权、云厂商利润率、内存供应链、光互联价值——都建立在对推理成本、KV Cache 调度、MoE 通信等技术细节的真实体感上。这些体感只能从实际使用中来，不是读研报能替代的。"
  - question: "每天 3 亿 token 用在哪里？"
    answer: "主要用在自建的 Agent Team 投研系统上。多个 Agent 分别扮演不同投行分析师角色，对标的公司的收入、财务、风险、估值进行多轮对抗评审，每天自动化运行一遍以纳入最新变量。"
  - question: "AI 现在到底是吃存量还是做增量？"
    answer: "目前大部分是存量再分配——替代白领工作、优化现有流程。全新的增量市场还没看到规模化案例。这不是悲观判断，而是阶段性事实，直接影响 AI 半导体的 capex 定价是否合理。"
  - question: "Agent Team 投研流程是什么？"
    answer: "三步：第一步收集所有公开资料（研报、财报、10-K 等）；第二步派发 Agent Team，各 Agent 分别评估收入、风险、估值后由 Team Leader 对抗评审；第三步人工逐行校验并迭代，直到通过。"
---

关注芒格君有一阵子了。

中文圈能把 LLM 的 training/inference infra 讲透，能从软硬件 system co-design 一路讲到底层硬件原理，最后还能接回投资逻辑的人，凤毛麟角。芒格君算一个。这种跨层穿透的分享，在中文内容里非常稀缺。

> **但作为同样在做 AI、每天泡在 post-training 一线的人，我想补一个芒格君没有展开的角度：一线信息有时候是把双刃剑。好处是能更早嗅到机会；坏处是信息茧房非常重——把「内部需求炽热」直接外推成「这种需求会很快扩展到其他产业」，太自然了。**

![没烧过 token，就别说看懂 AI 半导体](/assets/images/cover-20260808-token-burn-ai-investing.webp)

## 一、一线信息的双刃剑

好处明摆着：离前沿越近，越早知道产业链上的真实 bottleneck，知道大家在 push 的技术方向是什么。

坏处也是真的：**信息茧房非常重。**

做 AI 的人每天接触的圈子都在往同一个方向跑。GPU 不够用、推理成本居高不下、内存是最大瓶颈——这些是真实的。但「圈内需求炽热」和「这种需求会很快扩散到其他产业」之间，隔着一道巨大的鸿沟。

一线的人太容易把自己的体感直接外推成整个市场的状态。**这是做投资最危险的事情之一。**

所以我一直纠结一个问题——

![一线信息的双刃剑](/assets/images/illust-20260808-double-edged-sword.webp)

## 二、AI 到底在吃存量，还是做增量？

需要说清楚：我知道这两者不是非此即彼。历史上几乎所有通用技术——电力、互联网、智能手机——都是先再分配、后做大蛋糕。这不是争论。

**我真正想追问的，不是最终「有没有新蛋糕」，而是：扩散到了哪一步？进度是否符合当前的 capex 定价？**

从目前来看，大部分还是在吃存量。替代白领工作、替代人工的数据标注、优化现有流程——这些确实在发生。但全新的、不靠替代而是靠创造的增量市场？目前还没看到有说服力的规模化案例。

这不是悲观。这是一个阶段性的事实判断。而这个判断直接影响你怎么给 AI 半导体公司定价。

**这也是我和纯技术视角最大的分歧：技术人看到的是「这东西太强了，一定会改变一切」；做投资要追问的是「改变的速度，是否匹配了当前花出去的钱」。**

## 三、没烧过 token 的人，看不懂供应链

之前的文章分享过如何借助 AI 做基本面分析和投研。那只是我投资布局中的一环。每天大概会花掉 3 亿 token，日复一日。

2026 年的今天，如果团队里的人每天烧不掉 1 亿 token，我会怀疑他对 AI 的认知深度和抽象能力。

**一个人对 AI 的理解，基本等于他被 token 账单教育过的次数。** 无论是跟着技术走，还是做投资，只有把 AI 用透——或者至少知道一线的人到底怎么用 AI——才谈得上做 AI 半导体的布局。

这是看任何小作文和 K 线都给不了你的东西。

具体讲几个例子：

| 你没做过的事 | 你就算不清的账 |
|------------|--------------|
| 没在「一卡难求」时排过队 | 不会真正理解 $NVDA 的定价权从哪来 |
| 没自己 host 过模型、没为 token 账单付过钱 | 算不清云厂商从「卖机器小时」变成「卖 token」后，$MSFT $AMZN $GOOGL 部署 Kimi、Qwen 这类开源权重，利润率能抬多少个点 |
| 没用 vLLM 真跑过推理 | 不知道 KV Cache 调度有多讲究、HBM 每一 GB 有多贵——关于内存供应链的所有判断，都从这里来 |
| 没研究过 MoE 的 all-to-all 通信 | 不明白 $MRVL $COHR 这些光互联玩家解决的根本不是「把机器连起来」，而是让上万张卡表现得像一台机器 |

**一线的手感，最后都会变成仓位。看懂才能心中有数。**

![token 账单即认知深度](/assets/images/illust-20260808-token-bill-depth.webp)

## 四、怎么把一家公司的投资价值研究透

手感要变成仓位，中间需要一套系统。光靠体感和朋友圈信息做判断，迟早翻车。

下面是我自己跑了大半年的投研流程。

**第一步：收集资料。**

找到研究标的最近的新闻、各大投行能找到的所有研报（高盛、大摩、小摩、UBS 等）、财报、公司公告、10-K，一网打尽。

**第二步：派发 Agent Team。**

我的 Agent 会化身成各个投行的分析师，分别持有一方观点。我仿照华尔街投行搭建了一套自己的 Agent Team：

- 有的 Agent 蒸馏了我的思想
- 有的 Agent 蒸馏了我的专业知识

它们分别去评估公司的收入、财务、风险、基本面和估值，最后再汇总给 Agent Team Leader 进行对抗评审。如此反复。

这一步我只用 Fable 5 或 GPT 5.6 Sol Ultra。

**第三步：人工校验。**

每一个 Sub Agent 和最后的 Agent Leader 都会给我一个 report。我会逐行根据实际经验人工校验，给整个团队新的输入，由 Agent Team 评估是否需要重做第二步。如此往复，直到我认为通过。

经过这三步，任何人都可以在几天之内把一家标的研究透彻。**而我每天 Agent Team 都会自动化运行一遍，确保每天的新变量被纳入我的 agent 大脑。**

![Agent Team 投研三步](/assets/images/illust-20260808-agent-team-workflow.webp)

## 五、这套东西能不能复制？

坦率说，有门槛。

1. **数据源。** 你得知道去哪找研报、财报、10-K，怎么把非结构化的信息喂给 Agent。垃圾进垃圾出，数据源的质量就是分析的天花板。
2. **基本功。** 没有经济学和技术的底子，你连问题都提不对——Agent 再强，也需要人告诉它该从哪些维度拆解一家公司。
3. **自己的判断框架。** 照搬别人的 thesis 没用。你得有自己的投资逻辑，并且能坚持纪律性执行。

这三条加在一起，门槛确实不低。

**所以我在考虑另一条路：把整套流程封装成一个开放接口或者 skill，让任何人的豆包、ChatGPT 都能直接调用我的 Agent Team Leader——24 小时在线，随时拆解任意一家公司的基本面。**

不用自己搭系统，不用自己找数据，直接问就行。我敢说这套东西跑出来的结论，比网上绝大多数财经博主的分析都要扎实——因为它背后不是一个人拍脑袋，是一群 Agent 反复对抗校验的结果。

## 写在最后

压成五句：

1. **一线信息是双刃剑**——好处是更早嗅到 bottleneck，坏处是把圈内需求直接外推成全市场
2. **AI 目前大部分在吃存量**——全新增量市场还没看到规模化案例，这个判断直接影响 capex 定价
3. **你对 AI 的理解 ≈ 你被 token 账单教育过的次数**——没烧过 token，看不懂供应链的每一环
4. **我的投研用 Agent Team**——每天 3 亿 token，仿照华尔街投行搭的对抗评审系统
5. **计划开源这套系统**——让所有人都能接入 Agent Team Leader，做到任何公司的基本面全解

土话一句：

**别看 K 线了。先看看你的 token 账单。**

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

延伸：[他们到底看到了什么？让 Jeff Dean 离开待了 27 年的 Google](/what-did-they-see-jeff-dean-new-paradigm) · [你还在切 chunk 做向量？RAG 早就不是这回事了](/rag-to-agentic-rag-evolution) · [WorkBuddy 和 Codex 谁更强？你问错了](/workbuddy-codex-positioning-threshold)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。一线手感变成仓位——你的 token 账单，就是你对 AI 最诚实的理解。*
