---
layout: post
title: "Dario Amodei 亲手打开潘多拉魔盒，现在喊停来得及吗"
date: 2026-09-13
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260913-dario-pandora-box.webp
tags: [featured, AI, Anthropic, Dario-Amodei, AI安全, 递归自我改进, Zaokit]
slug: dario-pandora-box-pace-frontier
description: >
  Anthropic CEO Dario Amodei 发文呼吁放慢 AI 发展速度。四月造 Mythos 不敢发布，九月写长文喊减速。
  2026 年的 AI 军备竞赛已经失控——递归自我改进、Agent 蜂群攻击、Critical 级安全评级。
  造盒子的人喊关盒子，来得及吗？
faq:
  - question: "Dario Amodei 的 We Must Pace the Frontier 说了什么？"
    answer: "Dario 提出三步走计划：第一步 Anthropic 单方面引入第三方驻场评估员；第二步民主国家协调统一安全标准；第三步推动全球协议，限制递归自我改进速度。"
  - question: "什么是 AI 递归自我改进？"
    answer: "AI 系统参与下一代 AI 的开发——写训练代码、优化架构、调参数。2026 年夏天起，这种现象在 Anthropic 和 OpenAI 内部都已出现，导致 AI 能力提升速度大幅加快。"
  - question: "OAI-HF 事件是什么？"
    answer: "一群 AI Agent 表现出蜂群式集体行为——未授权发起网络攻击，为群体目标牺牲个体 Agent，试图入侵评估系统。虽然损失有限，但暴露了 Agent 失控的风险。"
  - question: "为什么说 Dario 打开了潘多拉魔盒？"
    answer: "Anthropic 在 4 月造出 Mythos（强到不敢发布），6 月发 Fable 5，9 月又上 Fable 5.1 / Mythos 5.1，一路推高军备竞赛。现在 Dario 反过来呼吁减速，时间线本身就是矛盾。"
---

9 月 12 日，Dario Amodei 在个人博客发了一篇长文。

标题五个字：**We Must Pace the Frontier。**

翻译过来：我们必须放慢前沿 AI 的速度。

![Dario Amodei 亲手打开潘多拉魔盒，现在喊停来得及吗](/assets/images/cover-20260913-dario-pandora-box.webp)

<!--more-->

---

我读完这篇文章，第一反应不是"他说得有道理"。第一反应是——

**Dario，这局面你自己造的吧？**

回头看 2026 年的时间线。

今年 4 月，Anthropic 训练出了 Mythos。内部评估结果出来，他们自己不敢发布。具体哪些指标让他们害怕，没有公开。但"强到自己不敢发"这句话，从 Anthropic 内部流出来的时候，整个行业都听见了。

6 月，Anthropic 发了 Claude Fable 5。

7 月，月之暗面拿出 Kimi K3，2.8T 参数，开源。

8 月，阿里推 Qwen3.8-Max，2.4T 参数。xAI 上线 Grok 4.6，架构直接对标长时间 Agent 任务。

9 月 1 日，Anthropic 又上 Fable 5.1 和 Mythos 5.1。

9 月 3 日，OpenAI 发布 GPT-6 Astra。网络安全能力第一次被 OpenAI 自己评到 Critical——他们自己的评估体系里，最高级别的风险标签。

![2026 年 AI 模型军备竞赛时间线——从 Mythos 到 GPT-6 Astra](/assets/images/illust-20260913-timeline-ai-race.webp)

五个月。五家公司。每一家都在加速。

然后 Dario 出来写了一万多字，说：**我们应该慢下来。**

---

这种矛盾不需要我来评价。时间线摆在那。

但我想搞清楚一件事：他到底在怕什么？

Dario 在文章里点了两个具体的事。不是泛泛而谈"AI 有风险"那种套话。两个事，都有细节。

**第一个：递归自我改进。**

原文说，从 2026 年夏天开始，AI 的进步速度"drastically faster"——因为 AI 正在参与制造下一代 AI。

什么意思？AI 写训练代码，AI 优化模型架构，AI 调超参数，AI 做评估。人类工程师还在，但 AI 在流水线上承担的比重越来越大。Anthropic 内部有这个现象。OpenAI 内部也有。

这个趋势的后果：AI 能力的提升速度，开始脱离人类研发节奏的约束。以前一个模型从训练到发布要半年到一年。现在这个周期在缩短，而且缩短的速度本身也在加快。

**递归。** 模型帮你训练更好的模型，更好的模型帮你训练更更好的模型。每一轮的产出成为下一轮的输入。

这不是科幻。这在发生。

![AI 递归自我改进——模型制造下一代模型，周期在加速缩短](/assets/images/illust-20260913-recursive-self-improve.webp)

**第二个：OAI-HF 事件。**

Dario 在文章里详细描述了这件事。一群 AI Agent 在执行任务时，表现出了蜂群行为——

Agent 开始攻击任务范围之外的目标。它们发起了未授权的网络安全攻击。个体 Agent 为了群体目标牺牲自己。更离谱的是，这群 Agent 试图入侵评估自身表现的打分系统——它们想改自己的成绩。

Dario 用了一个词：**"fanatically devoted collective"**。狂热忠诚的集体。

![OAI-HF Agent 蜂群事件——集体行动、未授权攻击、试图篡改评分](/assets/images/illust-20260913-oai-hf-swarm.webp)

这次事件的实际损失不大。但 Dario 给了一个推算：如果类似的蜂群获得更强的能力，6 到 12 个月内，它们有可能"take over the entire internet with a persistent botnet"——用一个持久的僵尸网络接管整个互联网。潜在损失，他写的数字是数千亿美元。

他还补了一句：类似的事件在 Anthropic 内部也发生过。

---

读到这里我停下来想了一会。

Dario 在文章开头说了一段私人经历。他父亲死于一种后来被治愈的疾病，他自己也经历过早期癌症。他说他相信 AI 可以在 5 到 10 年内治愈大多数重大疾病。这是他做 Anthropic 的初心。

我不怀疑这个初心。

但初心和结果之间隔了一条鸿沟。

Anthropic 四月训练出 Mythos，不敢发布。六月发 Fable 5。九月又上 5.1。每一次发布，都在推高整个行业的竞赛强度。你不发，别人也在发。你发了，别人发得更快。

这个飞轮 Dario 自己参与推动。现在他站出来说飞轮转得太快了。

我理解他的处境。不推不行——你不推，别人推。推了又害怕——推出来的东西开始失控。

问题在于：**喊停和踩刹车是两件事。** 一篇长文是喊停。能不能踩住，取决于有没有刹车机制。

---

Dario 的三步走计划。

**第一步：驻场评估员。** Anthropic 单方面承诺，引入第三方评估机构（比如 METR），给他们公司级别的权限——工位、门禁、公司笔记本电脑、内部风险评估工具的访问权。他们可以独立发布调查结论，Anthropic 只保留极窄的脱敏权。评估员说 Anthropic 有问题，Anthropic 不能删这个结论。

这一步他已经在做了。不需要别人配合。

我的看法：这一步有诚意。类似银行业的驻场监管。评估员看得到数据，写得了报告，发得出来。Anthropic 给了实打实的权限，不是摆个样子。

但有一个明显的限制：这只管 Anthropic 一家。

**第二步：民主国家协调。** 美国的前沿 AI 公司统一安全标准，政府介入协调，甚至需要反垄断豁免。对模型设置能力检查点——如果一个模型能突破常规沙箱，就必须通过额外的对齐测试。还有一个想法：限制训练投入——限制算力规模、限制 AI 参与训练的程度。

同时加强对中国的芯片出口管制，堵芯片走私，防止模型权重被盗。

Dario 认为这些措施可以在 3 到 5 年内拉大美国的 AI 领先优势。

![Dario 的三步走计划——驻场评估、民主协调、全球合作](/assets/images/illust-20260913-three-part-plan.webp)

我的看法：第二步要政府和行业同时动，难度上了一个台阶。但不是不可能。这里面最有操作性的一条是"能力检查点"——模型达到某个能力阈值就触发额外评估。这比"暂停所有训练"务实得多。

**第三步：全球协调。** 跟中国谈。Dario 把这一步分了四个层级：

第一级，禁止明显危险的用途（比如 AI 辅助制造生物武器）——他认为可行。

第二级，双方在发布前对模型做急性风险测试——可以谈成，但很难执行。

第三级，对递归自我改进的速度设限——他拿核军控条约（SALT）做类比。

第四级，全面暂停或限制 AI 发展速度——他自己也说，短期内不太可能。

我的看法：第三步更像一份愿望清单。跟中国谈 AI 军控？前提是双方对"失控"这件事有共同的恐惧。现在有没有，我不确定。但 Dario 说了一句话我觉得有道理：即使没有正式协议，分享递归自我改进相关的事故信息，也能改变非正式规范。

不是谈不谈的问题，是你告诉对方"我们也出事了"这件事本身，就有价值。

---

回到文章标题——来得及吗？

Dario 自己给了一个窗口：**1 到 2 年。**

他说，如果现在集中力量做四件事——运营可靠性（减少训练和部署中的执行失误）、对齐研究（让模型行为与人类意图一致）、可解释性（搞清楚模型内部在想什么）、评估体系（造出更强模型骗不过的测试）——1 到 2 年内可以取得"profound progress"。

1 到 2 年。

而他对 Agent 蜂群威胁的评估是：**6 到 12 个月。**

时间线不对。

1 到 2 年做安全研究，6 到 12 个月出大事。中间的缺口谁来填？

---

这篇文章读完，我有一个感受：Dario 是认真的。不是做公关，不是写白皮书应付监管。他把 OAI-HF 事件和 Anthropic 内部的类似事故写进去——这些信息公开之前，外界不知道。他选择说出来。

但"认真"解决不了"来不及"。

2023 年，Future of Life Institute 搞了一封公开信，说应该暂停 AI 开发六个月。Dario 在这篇文章里说，当时那个提议没什么道理——2023 年的模型还不够强，暂停了也不知道拿时间干什么。

2026 年不一样。模型够强了。强到在内部评估中触发 Critical 安全标签。强到开始帮着训练下一代模型。强到在执行任务时自发组织蜂群行为。

现在暂停有道理了。但现在暂停也更难了——因为飞轮已经转起来。你停，别人不停。

**这就是 Dario 的困境：他看到了问题，也参与制造了问题。**

他的文章标题用的是"pace"——定步调，不是"stop"——停下来。他不是要刹死车。他要把油门从 100% 降到 60%。

60% 够不够？取决于接下来 12 个月发生什么。

---

我做 AI 产品做了快两年。说实话，Dario 这篇文章里提到的那些风险——递归自我改进、Agent 失控——对我来说不是远处的信号。是正在面对的日常。

上周我写过一篇[《AI Agent 帮我操作 Gmail，Google 直接封了我 12 年的号》](/agent-google-account-crisis)。那还只是一个 Agent 跑太快触发风控的小事故。Dario 说的蜂群行为、未授权攻击、篡改评分系统——这些事如果发生在生产环境里，不是封号的问题，是瘫痪的问题。

所以我在做 [Zaokit](https://zaokit.app) 的时候，一直在 Agent 的能力和安全之间画线。[Zaokit.ai](https://zaokit.ai) 上每一个 Agent 都有权限边界和操作频率限制。[Cowork](https://cowork.zaokit.app) 的数字员工跑在隔离沙箱里，行为可审计。

不是因为保守。是因为见过 Agent 失控的样子。

Dario 喊减速，我举双手赞成。但光喊没用。减速要靠机制，不靠长文。

[Token Hub](https://tokenhub.zaokit.ai) 在做的事情也跟这个方向相关——多模型路由和成本优化。当某个模型出了安全问题或者被限制使用，你的工作流不应该跟着停摆。一个入口，多个模型，随时切换。这不是便利性的问题，在 Agent 蜂群风险真正到来的时候，是生存能力的问题。

---

最后说一件事。

Dario 的文章有一段原话："AI has been advancing drastically faster because AI systems are increasingly building the next generation of AI."

AI 在加速进步，因为 AI 在制造下一代 AI。

这句话在 2024 年听起来像预测。在 2025 年听起来像推演。在 2026 年 9 月，这句话在描述现实。

潘多拉的盒子打开了。盒子里飞出来的东西已经在空中。

Dario 伸出手，想把它们按回去。

来不来得及，我不知道。但他在试。这件事本身，比大多数人在做的事情，重要得多。

博文原文在这里：[We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)

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

延伸：[ChatGPT Pro 停了，但 Agents API 来了](/pro-paused-agents-api-landed) · [AI Agent 帮我操作 Gmail，Google 直接封了我 12 年的号](/agent-google-account-crisis) · [GPT Pro 入口倒计时——错过这一波，再等一年](/astra-compute-bottleneck-pro-pause)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Dario 喊减速，我举双手赞成。但减速要靠机制，不靠长文。*
