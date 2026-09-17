---
layout: post
title: "GPT 订阅号池服务，可以写入历史了"
date: 2026-09-17
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260917-subscription-pool-dead.webp
tags: [featured, AI, OpenAI, Pro, 按量付费, ARR, IPO, Zaokit]
slug: pro-subscription-pool-dead-pay-per-use-era
description: >
  算力不足之后 OpenAI 对号池账号直接 cooldown，不管你有多少号，检测到就冷却，没有商量。
  GPT 订阅号池模式走到了尽头。ToB/ToC 按量付费时代开启，OpenAI 营收跳升几个量级。怪不得今年不上市——先把收入做上去，再谈 IPO 估值。
faq:
  - question: "GPT 订阅号池是什么？"
    answer: "多个 Pro 账号共享使用的中转服务模式。服务商购买多个 200 美元/月的 Pro 账号，通过路由分配给下游用户，以远低于 API 价格提供 GPT 服务。本质是利用固定月费的成本优势做二次分发。"
  - question: "为什么说订阅号池模式要写入历史了？"
    answer: "算力紧张后，OpenAI 对号池账号直接做 cooldown——检测到号池行为（高频轮转、多 session 共享）就冷却，不管你有多少号。同时暂停 Pro 新订阅、收紧限额，号池的生存基础已经不在了。"
  - question: "OpenAI 按量付费对营收有什么影响？"
    answer: "固定月费模式下，Pro 用户越活跃 OpenAI 越亏。切换到按量付费后，每一次推理调用都产生收入，营收与使用量正相关。这种模式下 ARR 的天花板远高于订阅制。"
  - question: "OpenAI 为什么 2026 年不上市？"
    answer: "在订阅制模式下，Pro 用户越多亏损越大，财务报表不好看。转向按量付费后，需要时间让收入结构优化、毛利率提升，等财务数据足够漂亮再启动 IPO，可以拿到更高估值。"
---

三天了。

打开 ChatGPT，server_is_overloaded。换个账号，server_is_overloaded。切到 Codex，server_is_overloaded。Pro 账号、Plus 账号、企业版——全线趴窝。

![连续三天 server_is_overloaded——OpenAI 全线产品集体趴窝](/assets/images/cover-20260917-subscription-pool-dead.webp)

<!--more-->

---

算力不足之后，OpenAI 动了刀子。

不是"服务器忙，请稍后再试"那种客气话。是直接对号池里的账号做 cooldown。你有 10 个号也好，100 个号也好，只要被检测到号池行为——高频轮转、多 session 共享、请求模式异常——直接冷却。没有预警，没有商量。

我后台的 10 个 Pro 轮转账号，上周错误率 10%。这三天，cooldown 一来，直接瘫了。不是偶尔排不上队，是 OpenAI 从算力分配层面把号池模式掐死了。

---

说一个已经在发生的事。

做 GPT 中转的服务商，过去一年靠什么活？靠号池。买一批 Pro 账号，200 美元一个月一个，通过路由分配给下游客户。客户付的价格比 API 便宜，服务商赚中间差价。

这个模式的前提是：Pro 账号能正常跑，不被针对。

![号池模式的前提崩了——Pro 账号不再稳定出活](/assets/images/illust-20260917-pool-model-collapse.webp)

前提崩了。

不是"偶尔慢一点"的问题。算力一紧，OpenAI 对号池账号做 cooldown——你有多少号都一样，检测到号池行为就冷却，整池报废。服务商手里几十个 Pro 号，一夜之间全部进入冷却状态。客户投诉，服务商只能切到 API 渠道兜底——API 按 token 收费，成本是 Pro 号池的十倍不止。兜底一兜，利润全没。

不止如此。OpenAI 从 9 月 11 号暂停 Pro 新订阅开始，信号已经摆在明面上：**固定月费的无限量模式，走不下去了。**

200 美元/月的 Pro，用户跑满的话，OpenAI 每个月亏几百到上千美元。用户越活跃，亏得越多。GPT-6 Astra 上线之后，用户活跃度暴涨，亏损跟着暴涨。

号池服务商把这个漏洞用到了极致——用固定成本吃无限量的推理资源，再转卖。OpenAI 亏了两次：一次亏给了 Pro 用户，一次亏给了号池的下游客户。

现在 OpenAI 不亏了。cooldown 机制一上，号池里的号集体冷却，服务商的成本优势一夜归零。

**这笔账算不下去了。**

---

看 OpenAI 最近的动作。

9 月 3 号，GPT-6 Astra 上线。9 月 9 号，Pro 限额收紧——我上周写过，一周 200 条共用限额，一个下午就能见底。9 月 11 号，暂停 Pro 新订阅。9 月 14-15 号，连续两天 server_is_overloaded。9 月 15-17 号，overloaded 持续三天。

![时间线：从 Astra 上线到号池模式终结](/assets/images/illust-20260917-timeline-to-payperuse.webp)

把这条时间线连起来看，方向很清楚。

OpenAI 在做一件事：**把 Pro 订阅从"无限自助餐"变成"有限配给"，同时把真正的算力分配给按量付费的 API 客户。**

换句话说——ToB 和 ToC 的按量付费时代，要开了。

---

按量付费对 OpenAI 意味着什么？

一笔简单的账。

Pro 模式：一个用户一个月 200 美元，用多用少都是 200。用得多 OpenAI 亏钱，用得少 OpenAI 赚闲置差价。总营收 = 用户数 × 200。天花板肉眼可见。

按量付费模式：每次推理调用都产生收入。GPT-6 Astra 的 API 定价大约每百万 token 15 到 30 美元。一个重度用户一个月的推理消耗，按 token 算可能是 500 到 2000 美元——远超 200 美元的 Pro 月费。

**模式一切换，同样的用户量，营收翻几倍。**

![订阅制 vs 按量付费——同样的用户量，收入天壤之别](/assets/images/illust-20260917-subscription-vs-payperuse.webp)

Pro 时代，OpenAI 的营收受限于订阅人数。按量付费时代，营收跟着使用量走。用户用得越多，OpenAI 赚得越多。正向飞轮。

这也解释了一件事：**OpenAI 为什么今年不上市。**

订阅制的财务报表不好看——用户越多亏损越大，毛利率被 Pro 的定价锁死。拿着这张报表去 IPO，估值打折。

但如果切到按量付费，花半年到一年时间让收入结构优化——毛利率提升，营收增速上去，亏损收窄——再去 IPO，估值可以高出几个量级。

**不是上不了市，是现在上不划算。**

Sam Altman 看得很清楚。9 月 12 号他在公开场合说了一句话："2026 年上市不明智（ill-advised）。" OpenAI 的年化营收在今年 7 月已经突破 400 亿美元——2025 年底还只有 200 亿，七个月翻了一倍。Q2 季度收入 67 亿，Q1 是 57 亿，增速在加快。但这里面大量收入来自固定月费的 Pro 和 Plus，毛利率被锁死。

7 月底 OpenAI 做了一件事：GPT-5.6 Luna 的 API 价格直降 80%——输入 token 从 1 美元/百万降到 0.20 美元。Terra 降了 20%。同时 8 月底在印度的免费版和 Go 版上线了广告，广告收入年化已经到 10 亿美元。

API 降价 + 广告变现 + 企业端按量收入季度增长 50%。这三条线拉满，再带着按量付费的收入结构去 IPO，和带着订阅制的 400 亿去 IPO，估值差的不是一星半点。

![不是上不了市——是先把收入做漂亮再 IPO](/assets/images/illust-20260917-ipo-valuation-strategy.webp)

---

对我们这些用 GPT 做产品的人来说，号池模式终结不是坏事。

号池模式的本质是套利——利用 Pro 定价和推理成本之间的价差赚钱。套利窗口关了，行业反而会走向健康。

按量付费意味着：你用多少，付多少。成本可控，预算可算。不用担心某天 OpenAI 突然收紧限额把你的服务打垮。

我在 [Zaokit Token Hub](https://tokenhub.zaokit.ai) 做的事，从第一天开始就是按量计费的商业模式。多模型、多渠道、自动路由——OpenAI 贵了切 Anthropic，Anthropic 慢了切 Bedrock。不赌某一家的定价策略，只帮你找每一次调用的最优解。

号池死了，Token Hub 活了。不是因为我聪明，是因为按量付费才是长期可持续的商业模式。

---

还有一层影响。

ToC 端已经在变了。OpenAI 上线了积分充值模式——充值积分，按用量扣费，用完再充。不用每月被扣 200 美元，也不用因为某个月没怎么用而心疼钱。

这对 OpenAI 的用户增长是实打实的利好。200 美元/月的门槛，挡住了大量轻度用户。积分充值制，10 美元也能用，1 美元也能试。用户基数可以扩大一个数量级。

**用户基数 × 使用量 × 单价 = 营收。** 三个变量同时放大，ARR 的天花板打开了。

---

回到今天的 overloaded。

三天了。群里有人骂，有人笑，有人说"这下 200 美元的 Pro 真成智商税了"。

我的看法不一样。

这三天的 overloaded 和 cooldown，是一个时代的收尾声。GPT 订阅号池服务——靠固定月费薅无限量推理的模式——可以写入历史了。

接下来是按量付费的时代。对 OpenAI，对用户，对整个行业，都是更健康的模式。OpenAI 赚到钱，GPU 有着落；用户按需付费，不被月费绑架；服务商靠真本事而不是套利活着。

三赢。

---

如果你的 AI 工作流还在依赖号池——趁现在切换。不是号池不好用了的问题，是 OpenAI 在主动掐死这条路。cooldown 没有商量，号多号少都一样。

[Zaokit AI Token Hub](https://tokenhub.zaokit.ai)——多模型、多渠道、按量计费、自动路由。不薅羊毛，不赌号池，稳定靠谱。

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

延伸：[server_is_overloaded 的最新解决方案](/openai-overloaded-pro-wool-impossible-triangle) · [ChatGPT Pro 停了，但 Agents API 来了](/pro-paused-agents-api-landed) · [Dario Amodei 亲手打开潘多拉魔盒](/dario-pandora-box-pace-frontier)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。号池时代结束了——不是慢慢消失，是被 cooldown 一刀切掉的。按量付费的时代开始了。长远来看，顶尖模型的定价和 Token Efficiency 依然是最具性价比的选择。懂的人自然懂。*
