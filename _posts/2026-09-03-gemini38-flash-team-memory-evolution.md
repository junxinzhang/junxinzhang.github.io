---
layout: post
title: "Gemini 3.8 Flash 发了，聊一个我攒了半年的 toA 创业想法"
date: 2026-09-03
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260903-team-memory-evolution.webp
tags: [featured, AI, Gemini, Agent, toA, 创业, 团队协作, Zaokit]
slug: gemini38-flash-team-memory-evolution
description: >
  Gemini 3.8 Flash 今天发布，硅谷 toA（to Agent）赛道火得发烫。分享一个我从团队真实数据里沉淀了半年的创业方向：团队共同记忆演化。
  明星员工的 AI 工作流不可迁移、团队领域知识不可演化、AI 大材小用——这三个问题纠缠在一起，指向一个还没人做对的缝隙。
faq:
  - question: "什么是团队共同记忆演化？"
    answer: "团队在使用 AI Agent 过程中积累的领域知识、踩过的坑、沉淀出的工作流，自动变成团队共享资产，并通过 skill 录制或小模型微调持续演化，让所有成员都能用上。"
  - question: "为什么通用大模型解决不了团队的领域问题？"
    answer: "团队的业务数据分布、API 怪癖、客户触发的边界条件等领域知识不在通用模型的训练集里。即便是 Fable 5.1 或 GPT-5.6 级别的模型，也无法自动解决这类私有化问题。"
  - question: "toA 是什么？"
    answer: "toA 即 to Agent，指做给 AI Agent 使用的产品和基础设施。在硅谷当前是非常火热的创业赛道。"
  - question: "如何降低团队使用 AI 的成本？"
    answer: "通过 Record as a Skill 或 Post-training，把成功的问题解决路径蒸馏到极小、极便宜的本地模型中，让它在高频重复场景下做到和顶级模型一样的表现，成本可以降低两个数量级。"
---

Gemini 3.8 Flash 今天发了。

Google 在 Flash 这条线上没停过。速度更快，成本更低，API 兼容性做得比上一代干净不少。我收到消息后在 [Token Hub](https://tokenhub.zaokit.ai) 上做了接入，第一时间可用。

![Gemini 3.8 Flash 发布与 toA 赛道](/assets/images/cover-20260903-team-memory-evolution.webp)

但今天不聊模型评测。想聊另一件事。

在硅谷做 AI 创业，这半年有一个方向热得发烫：toA。to Agent——给 AI Agent 用的产品和基础设施。每周都有新项目拿到融资，赛道拥挤。我自己做 [Zaokit](https://zaokit.app) 做了快两年，每天都在这个生态里泡着，近距离看各家在做什么。

今天想分享一个我攒了半年的想法。不是从报告里看来的，是从我团队的真实数据里长出来的。我管它叫——**团队共同记忆演化**。

---

先说痛点。

我团队里有几个工程师，AI 用得极好。Claude Code、Codex、各种 Agent 全副武装。Context → Dev → Skill → Eval → Loop，整条链路打通，一个人能干以前三四个人的活。

这种人在硅谷每个团队都有。他们是推着整个团队往前走的发动机。

然后我看了一眼团队其他人的数据。

差距大到让我重新审视整件事。

![明星员工 vs 团队其他人：同一支队伍，两种速度](/assets/images/illust-20260903-skill-gap.webp)

同一个任务，明星员工十分钟搞定，其他人花一天还在手动试错。不是智力差距——是认知门槛。怎么写 prompt、怎么配 skill、怎么设 eval loop，这些东西在明星员工的脑子里，没有标准化的迁移路径。大部分 p50 水平的同事学不会，或者说没有环境让他们学会。

团队内部的能力撕裂，带来大量重复劳动。明星员工觉得"这不是很简单吗"，其他人觉得"我已经在拼命学了"。两边都没错，但团队整体的人效被这个 gap 拖住了。

这个问题叫：**不可迁移**。

---

第二个问题更隐蔽。

AI Agent 在 Loop 里跑任务的时候，不断踩坑。有些坑是 PM 在验收时发现的，有些是 QA 在回归测试里捞出来的，有些是工程师自己跑着跑着撞上的。每次都 ad hoc 修一下——调个 prompt、加个 edge case 判断、手动纠正一次输出。打个补丁，继续跑。

问题在于，这些坑是你自己的。

你的业务数据长什么样、你的 API 有什么怪癖、你的客户在什么场景下触发边界条件——这些领域知识不在任何通用模型的训练集里。Fable 5.1 不知道你的 API 在周末会返回一个不同格式的 response。GPT-5.6 不知道你的客户习惯在金额字段里输入带逗号的数字。

每次 ad hoc 修完就过去了。知识留在了修的那个人脑子里，或者留在了某条 Slack 消息的角落里。下一次同样的坑再出现，另一个人会重新踩一遍。

![领域知识散落各处，每个人都在重新踩同一批坑](/assets/images/illust-20260903-domain-knowledge-scatter.webp)

我预计这类私有化领域问题会持续很长时间。大模型的通用能力在涨，但你的私有领域知识不在它的训练集里。这个 gap 不会因为模型更新自动消失。

这个问题叫：**不可演化**。

---

还有一个问题跟成本有关。

团队成员用 AI 的时候有一个本能选择：用最好的。

但很多任务根本不需要顶级智能。格式化一份报告、提取结构化数据、跑一个已知模式的代码变更——这些活，理论上小模型够了。

可是，现在的小模型在特定业务场景下做不好。GLM、Kimi、一些开源 7B 模型，一次性做对的概率太低。试两三次才能拿到合格输出，时间成本反而更高。

所以团队的选择很理性：用贵的。用 Claude Opus，用 GPT-5.6。一次做对，省下来的时间比多花的 token 钱值。

但这笔账，放到团队规模上算，成本曲线陡峭。一个人用 Opus 没感觉，十个人每天调几百次，月底账单会让你重新审视这件事。

![用大炮打蚊子：任务不需要顶级智能，但小模型接不住](/assets/images/illust-20260903-overkill-cost.webp)

这个问题叫：**大材小用**。

---

这三件事纠缠在一起，指向同一个缝隙。

明星员工踩过的坑、沉淀出的 prompt 和工作流，能不能自动变成团队资产？每一个 domain-specific 的问题，解决之后能不能回灌到系统里，让下次遇到同类问题时自动处理？需要顶级模型才能做对的任务，解决路径能不能被蒸馏到一个极小、极便宜的本地模型里？

我管这整件事叫：**团队共同记忆演化。**

做法有两条路。

一条是 Record as a Skill。把一次成功的问题解决过程录下来，抽象成 skill，挂到团队里任何人的 Agent 上。明星员工解了一个 bug，这个解法变成一条 skill，下次其他人遇到同类问题，Agent 自动调用。知识从个人脑子里流进系统。

另一条是 Post-training。用团队自己的业务数据做微调，让一个极小的本地模型——参数量可能只有 1B 甚至更小——在某个特定场景下做到和顶级模型一样的表现。那种重复性高、调用频率高的任务，不需要每次都请 Opus 出手。蒸馏完的小模型跑在本地，成本降两个数量级。

这两条路不矛盾。Skill 解决知识迁移，Post-training 解决成本。两个一起做，团队的 AI 能力才能从"几个人会用"变成"整个团队都在同一个水平线上"。

---

这个方向不是我凭空想的。已经有好几个开源项目在做类似的事。

我全拉下来跑了一遍。

差强人意。

每一个在 demo 数据集上都跑得不错。但换成我自己的业务数据，准确率掉得很快。fine-tuning pipeline 的假设和我的数据分布对不上，prompt 模板太通用，覆盖不了业务里的边界情况。

![开源方案：demo 里跑得通，换上真实数据就漏](/assets/images/illust-20260903-opensource-gap.webp)

这不是某个开源项目的问题。这是 toA 赛道目前的通病——给 Agent 用的工具铺天盖地，但给 Agent 做 domain adaptation 的基础设施太少。大家都在做更聪明的 Agent，没人做让 Agent 在你的地盘上变聪明的事。

这是我 side project 在探索的方向。Gemini 3.8 Flash 发了，模型越来越便宜，这件事对 toA 赛道是利好。但成本降了不等于问题消失。你的团队知识没有进到模型里，你的 domain-specific 的坑还在那，你的 p50 员工和明星员工之间的 gap 还在那。

团队共同记忆演化，就是在解这个缝隙里的问题。

如果你知道有好的产品在做这件事，分享给我。如果你有好的 idea，也让我知道。

做了快两年 [Zaokit](https://zaokit.app)，我很清楚一件事：值钱的创业方向，不是坐在那里想出来的。是从自己团队的痛点里长出来的。

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

延伸：[Fable-5.1 发了，GPT-5.6 明天到——好模型不是 KPI 压出来的](/fable-gpt6-aha-not-kpi) · [OpenClaw 2.0 Team 模式来了](/openclaw-team-vs-hermes) · [桌子对面没有人](/one-person-company-story)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。值钱的方向，从痛点里长出来。*
