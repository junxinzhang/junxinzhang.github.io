---
layout: post
title: "Grok 4.6 肉眼可见地变慢了"
date: 2026-08-19
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260819-grok46-slower.webp
tags: [featured, AI, Grok, xAI, 算力, 调用量, SuperGrok, Zaokit]
slug: grok46-slower-usage-surge
description: >
  Grok 4.6 上线一周，体感变慢不是错觉。花了 300 刀的 Heavy 用户一样排队。
  调用量是真的上来了——但这是 xAI 的好消息，不是你的。
faq:
  - question: "Grok 4.6 真的变慢了吗？"
    answer: "体感明显。同样的编程任务，上线首日几秒出结果，现在动辄十几秒甚至排队。Heavy 用户一样排。"
  - question: "变慢是模型本身退步了吗？"
    answer: "不是。输出质量没有下降，慢在排队和首 token 延迟。这是算力被摊薄的典型表现，不是权重劣化。"
  - question: "xAI 会扩容吗？"
    answer: "孟菲斯超算中心还在扩建，Colossus 二期的 GPU 在上架。扩容是确定的，只是追不上短期涌入的调用量。"
---

上周我用 Grok 4.6 一句话搓了四个游戏，10 分钟内全套完成。这周同样复杂度的任务，动不动就卡住，长对话中间反复停顿。

我是 SuperGrok Heavy 用户，月付 300 刀。**花了钱，一样排队。**

> **调用量上来了是 xAI 的好消息，不是你的。**

![花了钱，一样排队](/assets/images/cover-20260819-grok46-slower.webp)
<!-- baoyu-skill prompt: 2.35:1大胆高对比清线漫画封面。饱和珊瑚红/电光薄荷绿/明黄/天蓝大色块，粗黑描边，构图满。禁止品牌logo与深色赛博UI。过热服务器写「请排队」，长队小机器人，最前举「300刀」票。顶部超大中文「花了钱，一样排队」，底部「Grok 4.6 · SuperGrok Heavy」。 --ar 2.35:1 -->

## 一、不是错觉

作为每天拿 Grok 4.6 干活的人，这一周的体感变化很清楚：

- **TPS 断崖下跌**：上线首周 token 生成速度能跑到 600 TPS，现在只有二三十
- **首 token 延迟**：首日 2-3 秒，现在经常 10 秒以上
- **长任务卡顿**：跑复杂编程任务时中间会停住几秒，首日没有

输出质量没退步。同一个 prompt 跑出来的代码和推理跟首日一样好。慢的不是脑子，是你前面排着的人。

![TPS 断崖：600 → 二三十](/assets/images/illust-20260819-tps-cliff.webp)
<!-- baoyu-skill prompt: 2.35:1大胆高对比清线漫画。左绿仪表 600 TPS 机器人飞快打字，右红仪表 20-30 TPS 机器人对着转圈发呆，中间断崖裂缝。顶部「TPS 断崖」，底部「600 → 二三十」。 --ar 2.35:1 -->

## 二、原因就一个：用的人太多了

质量没变，慢在排队。**Grok 的调用量是真的上来了。**

不是发布会 PPT，是你每天等的那十几秒。调用量增长造不了假——它直接体现在你排的队里。

Grok 4.6 质量跳升太猛，Cursor Ultra 集成又把编程场景直接灌进来，两个增量同时砸在同一批 GPU 上。Colossus 二期还在扩建，扩容追不上涌入。

![调用量是真的上来了](/assets/images/illust-20260819-usage-surge.webp)
<!-- baoyu-skill prompt: 2.35:1大胆高对比清线漫画。无数彩色小机器人挤向同一台冒烟 GPU 机柜，门口写「满了」。顶部「调用量是真的上来了」，底部「质量没变，慢在排队」。 --ar 2.35:1 -->

## 三、但这跟你有什么关系

调用量上来了，xAI 融资故事更好讲。**你呢？你花了 300 刀，换来的是更慢的响应。**

每一家 AI 公司都会走到这个坎：用户增长和服务质量直接冲突。OpenAI 2023 年初经历过，解法是推 Plus 分流。xAI 的解法是 SuperGrok Heavy 分层——但 Heavy 用户一样慢，说明分层没解决总量问题。

付费用户排队，本质是你在用等待时间替 xAI 承担扩容成本。

![xAI 的好消息，不是你的](/assets/images/illust-20260819-paid-wait.webp)
<!-- baoyu-skill prompt: 2.35:1大胆高对比清线漫画。左老板机器人踩上涨曲线举「融资故事」，右付费用户举「300刀」月票还在排队。顶部「xAI 的好消息，不是你的」，底部「花了钱，用等待扛扩容」。 --ar 2.35:1 -->

## 写在最后

压成三句：

1. **Grok 4.6 变慢了**——TPS 从 600 跌到二三十，首 token 延迟翻了好几倍，Heavy 用户一样排队，不是错觉
2. **原因是调用量真的上来了**——质量没退步，算力被打满，扩容追不上涌入
3. **这是 xAI 的好消息，不是你的**——你花了 300 刀，用等待时间替他们扛着扩容缺口

如果你也觉得慢，试试切到 Gemini 3.7 Flash。我自己的 Agent 编排已经切过去了...

---

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

延伸：[用 Grok 4.6 一句话搓了牛来、羊来、熊来、猪来](/grok46-one-prompt-four-games) · [Grok 4.6 和 Gemini 3.7 Flash 同周落地：模型竞争进入淘汰赛](/grok46-gemini37-flash-model-knockout) · [Stripe 收购 OpenRouter：买的不是路由器，是计量表](/stripe-buys-openrouter-meter-not-router)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。300 刀买的是算力，不是排队的资格。*
