---
layout: post
title: "Stripe 70 亿买 OpenRouter：X 上吵的是贵不贵，被买走的是计量器"
date: 2026-08-17
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260817-stripe-openrouter-meter.webp
tags: [featured, AI, Stripe, OpenRouter, Token Hub, 模型路由, 计量器, 一人公司, Zaokit]
slug: stripe-buys-openrouter-meter-not-router
description: >
  彭博 8 月 16 日：Stripe 敲定收购 OpenRouter，报价超 70 亿美元。Stripe 没官宣。
  X 上吵的是贵不贵、有没有护城河。我的读法：买的不是中转站，是开发者和模型之间那块电表。
faq:
  - question: "Stripe 真的买下 OpenRouter 了吗？"
    answer: "彭博 8 月 16 日引述知情人士说交易已敲定，报价超 70 亿美元。Stripe 对 TechCrunch 的口径是不评论传闻。价格还可能变。当传闻写，不当新闻稿写。"
  - question: "X 上对这笔交易怎么看？"
    answer: "两派。空头说路由没护城河、140 倍市销太贵；多头说 Stripe 买的是 AI 推理时代的收费站。开发者这边多了一句玩笑：ClosedRouter，担心中立没了。"
  - question: "OpenRouter 到底靠什么赚钱？"
    answer: "底层模型价原价过手，按需付费时收大约 5.5% 平台费。它不训模型，做路由、故障切换、用量记账和结算。Stripe 本来就是它的支付、发票和风控底座。"
  - question: "对企业意味着什么？"
    answer: "公共入口可以被买走。公司自己的用量、路由策略、成功失败轨迹，不该长期写在别人的电表上。模型可以换，计量器最好自己留。"
---

刷到这条的时候，我第一反应不是「70 亿」。

是把这周的 token 账单又翻出来看了一眼。

彭博 8 月 16 日引述知情人士：Stripe 敲定收购 OpenRouter，报价超过 70 亿美元。5 月刚按 13 亿估值融完 B 轮，82 天，溢价五倍。Stripe 对 TechCrunch 说不评论传闻。价格还可能变。

所以这篇不当新闻稿写。当一张已经烧过的账单写。

> **X 上吵的是贵不贵。我盯的是另一件事：开发者和模型之间那块电表，被支付公司买走了。**

![Stripe 70 亿买 OpenRouter：被买走的是计量器](/assets/images/cover-20260817-stripe-openrouter-meter.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平封面，奶油到天蓝渐变，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。左侧一座小收费站/电表亭，牌子写中文「OpenRouter」，开发者小人把 token 硬币投进去；右侧一座更大的金色收费站，牌子写中文「Stripe」，电表数字狂跳。中央粗体中文「买的不是中转站，是电表」。顶部「70亿美元 · 82天溢价五倍」。底部「X上吵贵不贵，被买走的是计量器」。中文清晰可读。 --ar 2.35:1 -->

## 一、先把事实摆桌上

OpenRouter 是干什么的，用过的人都清楚：一个 API，四百多个模型。贵的、便宜的、挂了的、刚出的，写一次接口就能换。CEO Alex Atallah 以前是 OpenSea 的联合创始人，今年早些时候把自己叫「AI 领域的 Stripe」。

| 时间 | 公开事实 |
|------|----------|
| 2023 | Atallah 离开 OpenSea 后创办 OpenRouter |
| 2024 年 10 月 | 和 Stripe 正式合作：发票、税务、风控都走 Stripe |
| 2026 年 5 月 | B 轮 1.13 亿美元，估值约 13 亿；自称 800 万用户、400+ 模型 |
| 2026 年 7 月 | 《华尔街日报》说双方在谈，数字传到 100 亿附近 |
| 2026 年 8 月 16 日 | 彭博：敲定，超过 70 亿 |

赚钱方式很土：模型价原价过手，充值时抽大约 5.5%。不训模型，做路由、切换、记账、结算。

市场对收入口径很乱。有人按年化 5000 万算，市销 140 倍；也有报道说到年化 1.4 亿。我两边都不当真——没看到他们自己的财报。只记住一句：Stripe 本来就给它收钱，后台曲线它自己看得见。

## 二、X 上其实在吵两件事

我把时间线往后翻了几个小时。热闹，但不散。核心就两派，外加开发者自己的一句脏话。

**空头说：中转站，没护城河。**

加密圈里那位「白发股神」Serenity 写得很直：编排和调度谁都能做，几乎没有护城河。他也不否认用户和数据现在很值钱，只是问十年后还在不在。Crémieux 更狠：独立路由层本身就给调用加复杂度，结果还可能更差。模型稳定了、每家云都自带 Router，中间商凭什么继续抽成？

还有一个百万粉投资人直接说看不懂。贵，是这一派的第一反应。

**多头说：别把它当中转站，当收费站。**

硅谷增长顾问 Aakash Gupta 算的是费率：OpenRouter 抽 5.5%，Stripe 自己做支付才抽 2.9%。Stripe 在自己的后台里看着这条曲线往上冲，再出价。他收尾那句被转得最多——Stripe 当年给互联网商业修了收费站，现在花 70 亿买 AI 推理时代的收费站。

@Zevryn0 和韩国用户 @cozybearlog 说得更准：Stripe 买的不是下一个前沿模型，是开发者和模型之间那块**计量器**。Lago 联合创始人 byAnhtho 补了一刀：当 API 代理看，这价荒谬；当推理流量的调度权看，账是另一本。

分析师 @danizhu 把两家叠在一起：Stripe 当年把分散的金融基础设施变成可编程服务，OpenRouter 在对数百个模型做同一件事。买下来，Stripe 更靠近 AI 经济的交易层。

**开发者这边，多了一个词：ClosedRouter。**

Hacker News 几个小时几百条，中心不是估值，是中立还在不在。OpenRouter 被喜欢，是因为它不站队。Stripe 给 OpenAI、Anthropic 收过钱，也给 DeepSeek、Qwen 过手流量。路由算法还按成本走，还是会悄悄偏向自己的账单关系？没人能证明后者。但这个问题，从今天开始会一直被问。

![X 上两派：没护城河，还是收费站](/assets/images/illust-20260817-x-two-camps.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画对决图，奶油底、清线描边扁平色。左侧冷灰帐篷标中文「空头：没护城河」，小人举牌「谁都能做路由」「140倍市销」；右侧暖金帐篷标中文「多头：收费站」，小人举牌「5.5%过路费」「买的是电表」。中间一条马路，路上一个写着 ClosedRouter 的路障。顶部中文「X上其实在吵两件事」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读。禁止深色赛博风。 --ar 2.35:1 -->

## 三、我的读法：贵不贵是假问题

空头说得对的那一半，我认。转发请求的代码，值不了 70 亿。LiteLLM、各家云网关、开源 Router，都能做一层。

多头说得对的那一半，我也认。难复制的不是代码，是已经聚在上面的用户、请求、支付关系和那本实时账本：谁在用哪个模型、什么价、什么时候切走。

所以我不太想加入「贵不贵」这场。贵，是相对于今天的收入；便宜，是相对于明天的推理流水。两边都在猜蛋糕有多大。我猜不准。

我比较确定的是另一句：

**Stripe 买的不是一个更好的 API。它买的是「每一次调用发生时，谁记账、谁路由、谁结算」。**

[6 月那篇](/ai-token-hub-enterprise-first-step) 我写过：企业上 AI 的第一步不是给每个人买 Pro，是先建一个 Token Hub。当时不少人觉得小题大做。今天市场给这件事标了个价——70 亿。

[昨天](/apple-alibaba-siri-core-not-outsourced) 写苹果：云可以租，Siri 核心层不长期外包。今天是同一张表的另一格。模型可以租。计量器最好自己留。

![买的不是中转站，是电表](/assets/images/illust-20260817-meter-not-router.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画，奶油到天蓝渐变。画面中央一块巨大的老式电表，表盘写中文「Token」，指针狂转；电表后面隐约是一排模型插座，分别淡标「Claude」「GPT」「Qwen」「DeepSeek」。电表上方一只手正在盖章，章上写中文「Stripe」。底部大字中文「每一次调用，谁记账」。禁止品牌logo。中文清晰可读。 --ar 2.35:1 -->

## 四、中立这件事，我也不敢打包票

有人已经在说：赶紧迁走，别把生产流量押在一个被支付公司买下的入口上。

我理解这个本能。但今天就拔线，也像应激。API 没变，价格没变，官方还没出声。迁不迁，看的是以后三件事有没有动：

1. **默认路由还敢不敢把便宜的开源模型放在前面**
2. **账单和用量数据还让不让你完整导出**
3. **企业合同里的零数据保留，还算不算数**

这三件动了，再迁。没动之前，先把自己的计量留一份。

我自己这边更实际的变化是：OpenRouter 从「默认入口」降成「上游之一」。号池、官方 API、云网关，本来就该多条腿。公共路由被买走，只是把这件事从建议变成了必做。

有一件事我现在说不清，也不装懂：Stripe 会不会为了照顾和 OpenAI、Anthropic 的账单关系，慢慢把流量从便宜的中国开源模型上拨走。商业上说得通，政治上更说得通。开发者要的刚好相反。这个结，他们自己都还没解。

## 五、对企业：公共电表可以被买，自己的电表别出租

别读成 Stripe 新闻。这是一张所有权分类。

| 可以过手别人 | 最好自己留 |
|--------------|------------|
| 某个模型的调用 | 这个月公司烧了多少、烧在哪 |
| 某次故障自动切换 | 路由策略：贵的留给难活，便宜的留给批量 |
| 充值、发票、汇率 | 谁在用、用成了什么、失败在哪一步 |
| 地板价 token | 这套能力算不算你们公司的 |

[7 月那篇](/enterprise-agent-build-choose-token-hub) 钉过一句：工具可以分部门，心脏只能有一颗。今天补半句——**心脏别长在别人身上。**

我做 [Token Hub](https://tokenhub.zaokit.ai) 不是因为预见到 Stripe 会买 OpenRouter。是因为给企业看账单时，经常发现他们连「这个月到底烧了多少」都说不利索。公共入口越强，这个问题越容易被掩盖：用着很爽，账在别人那里。

模型谁便宜接谁。能留下的是自己的用量、权限和轨迹。

![公共电表可以被买，自己的电表别出租](/assets/images/illust-20260817-keep-your-own-meter.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底。左侧一座被挂上「已售」牌子的公共电表站，标中文「OpenRouter · 公共入口」；右侧一间公司配电房，墙上自己的电表发光，标中文「Token Hub · 自己的心脏」，几条整齐电缆通向「研发」「销售」「运营」。顶部中文「公共电表可以被买」。底部「自己的用量、路由、轨迹，别长期写在别人账上」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读。 --ar 2.35:1 -->

## 写在最后

1. **交易还没官宣**——彭博说敲定，Stripe 说不评论
2. **X 上两派都有道理**——代码不值 70 亿，电表可能值
3. **ClosedRouter 不是段子**——中立从今天开始要被持续追问
4. **贵不贵我猜不准**——确定的是计量权被标了价
5. **对企业**——模型可以换，自己的电表别出租

土话一句：

**别人的收费站可以过，自己的电表不能卖。**

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

延伸：[企业上 AI 的第一步，是先建一个 Token Hub](/ai-token-hub-enterprise-first-step) · [工具可以分部门，心脏只能有一颗](/enterprise-agent-build-choose-token-hub) · [苹果：Siri 核心层，最后时刻不外包](/apple-alibaba-siri-core-not-outsourced)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。公共入口可以被买走——自己烧了多少、烧在哪，别只写在别人的账上。*
