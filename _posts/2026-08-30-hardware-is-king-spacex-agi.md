---
layout: post
title: "硬件为王：从 SpaceX 造涡轮机到 AGI 逼近"
date: 2026-08-30
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260830-hardware-is-king.webp
tags: [featured, AI, SpaceX, 硬件为王, AGI, OpenAI, Cursor, 蒸馏, Zaokit]
slug: hardware-is-king-spacex-agi
description: >
  SpaceX 自己铸涡轮叶片，把发电机组投产时间砍掉 18 个月。AGI 信号越来越密。OpenAI 断供 Cursor 揭开了模型蒸馏的底牌。
  算法可以蒸馏，数据可以积累，但一条能铸造单晶涡轮叶片的产线，三年搭不起来。硬件为王，从芯片到叶片，一以贯之。
faq:
  - question: "SpaceX 为什么能做燃气涡轮发电机？"
    answer: "SpaceX 造了十几年火箭引擎，Raptor 发动机涡轮泵的铸造工艺和材料技术，与燃气涡轮叶片高度相通。这套经验直接降维到发电设备领域。"
  - question: "AGI 真的快来了吗？"
    answer: "黄仁勋认为很多具体任务上 AGI 已经实现。OpenAI 首席研究官 Mark Chen 判断已达 80% AGI 程度。Astra 模型被设计为能连续工作数天到数周。这些信号越来越密集。"
  - question: "OpenAI 为什么断供 Cursor？"
    answer: "表面是流量纠纷，深层原因是模型蒸馏。Cursor 用 OpenAI 模型输出来训练自己的编码引擎，等于把 OpenAI 最值钱的能力搬走了。"
  - question: "硬件为王具体指什么？"
    answer: "算法可以蒸馏复制，数据可以慢慢积累，但铸造涡轮叶片的产线、芯片制造工艺、算力基础设施——这些硬件能力需要十年以上才能建立，搬不走，复制不了。"
---

SpaceX 开始自己造燃气涡轮发电机了。

这条消息在很多人的信息流里一闪而过。我盯着看了半天，因为它印证了我一直在说的一个判断：**硬件为王。**

不是软件不重要。是在 AI 时代，谁握着硬件的生产能力，谁说了算。

![硬件为王：从火箭到发电机](/assets/images/cover-20260830-hardware-is-king.webp)

SpaceX 为什么能做这件事？因为他们造了十几二十年火箭引擎。Raptor 发动机里的涡轮泵，工作温度超过 1000°C，材料是镍基高温合金，铸造精度按微米算。这套技术放到燃气涡轮发电机的叶片上，几乎是降维打击。

燃气涡轮机生产的瓶颈在哪？叶片和导向叶片的铸造。全世界能做这件事的工厂，订单排到两年以后。GE Vernova、西门子能源、三菱重工的产能全部爆满。

SpaceX 说：我自己铸。

通过在内部做铸造作业，新机组投产时间可以缩短 18 个月。

![SpaceX 的降维打击：火箭引擎技术造发电机叶片](/assets/images/illust-20260830-spacex-turbine.webp)

18 个月是什么概念？一座数据中心从批地到上线，卡在电力上的时间往往比卡在建筑上还长。你把发电机组交付缩短 18 个月，等于把整个数据中心的上线节奏提前了一大截。

马斯克的逻辑一直很清楚：哪里赚的钱最多，就往哪里走。自己用，降低 xAI 和 Tesla 数据中心的电力成本和建设周期。卖给别人，直接吃下新能源基建的利润。两头都能做。

SpaceX 和 Tesla 现在都在拼命建太阳能产能，目标是尽可能快地达到每年 100 吉瓦的生产能力。但太阳能有个死角——晚上不发电，阴天打折扣。未来几年，天然气得补上这个缺口。谁能最快造出涡轮机，谁就掌握了从规划到上线的时间差。

这就是硬件为王的意思。你的算法再强，数据中心没电，等于零。

---

说完硬件，说说 AGI。

最近越来越多信号挤在一起，指向同一个方向：AGI 可能真的快了。

黄仁勋在这次英伟达财报会议上说了一句——他认为对于很多具体任务而言，AGI 已经实现了。注意用词，不是"即将"，是"已经"。

OpenAI 马上要发布的 Astra 模型，被认为是迈向 AGI 的关键一步。它和现有大模型最大的不同：**能连续工作数天甚至数周，不需要人类干预。** 这跟我们现在用的聊天模型完全不是一个物种。聊天模型是你问一句它答一句，Astra 是你给它一个目标，它自己拆任务、自己调工具、自己跑完整个流程。

OpenAI 首席研究官 Mark Chen 的判断更直接：已经达到了 80% 的 AGI 程度。

![AGI 的信号越来越密集](/assets/images/illust-20260830-agi-signals.webp)

我记得一年多以前，只要有人在公开场合提 AGI，评论区就冒出一堆人冷嘲热讽。"AGI 是资本画饼""纯粹割韭菜"，各种阴谋论满天飞。

这一年发生了什么？

Coding Agent 全面落地。AI 从一个只会聊天问答的机器人，变成了能理解需求、调用工具、执行复杂任务、直接交付结果的 Agent。我自己每天都在用 Claude Code 写代码、做交付，体感非常明确——很多一年前被认为"至少还要五到十年"的能力，今天已经在生产环境里跑了。

**你可以对 AI 泡沫保持警惕，但对技术发展速度，得保持敬畏。**

人总习惯用过去的经验线性外推未来。但 AI 的进化从来不是线性的。硅基迭代的速度，一次又一次超过碳基大脑的预期。今天你觉得激进的判断，可能只是明天最保守的现实。

---

再说一件事。OpenAI 断供 Cursor。

表面看是流量纠纷——Cursor 占了 OpenAI API 调用量的 5%，比例确实不小。但真正让 OpenAI 动刀的原因，不只是流量。

这件事藏着两个信号：

**模型的能力可以通过蒸馏复制。** 用大模型的输出来训练小模型，把"聪明"从一个脑子搬到另一个脑子。这在技术上已经成熟了。

**Cursor 和 Grok 已经掌握了这种复制的能力。** Cursor 用 OpenAI 的模型输出来强化自己的编码引擎，Grok 在用类似的路径追赶。

![模型蒸馏：把聪明搬走](/assets/images/illust-20260830-model-distillation.webp)

OpenAI 急了，因为它发现自己最值钱的东西——模型能力——正在被下游客户"搬走"。这不是 5% 流量的问题，这是商业模式的命门。

有意思的是，这件事跟 SpaceX 造涡轮机是同一个道理，只不过方向相反。

SpaceX 掌握了铸造叶片的硬件能力，可以绕开整条供应链的排队，自己定节奏。Cursor 掌握了模型蒸馏的软件能力，可以逐步摆脱对 OpenAI 的依赖。

**谁掌握了生产能力，谁就不用看别人脸色。**

硬件如此，软件也如此。但在 AI 时代，硬件的权重被重新拉高了。算力、电力、芯片、涡轮叶片——这些你摸得着的东西，才是真正搬不走的护城河。算法可以蒸馏，数据可以积累，但一条能铸造单晶涡轮叶片的产线，你花三年也不一定搭得起来。

---

马斯克造涡轮机，不是心血来潮。他在用十几年火箭引擎的硬件积累，去切一个被 AI 算力需求撑大的万亿市场。AGI 的信号越来越密，时间窗口在收窄。OpenAI 断供 Cursor 告诉我们，模型能力可以被搬走。真正搬不走的，是硬件。

**硬件为王。从芯片到叶片，从火箭到发电机，一以贯之。**

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

延伸：[桌子对面没有人](/one-person-company-story) · [传统企业做 AI 转型，卡点不在工具，在组织](/enterprise-ai-org-conflict) · [网页自己报工具：WebMCP 这周被 OpenAI 推上台](/webmcp-openai-this-week)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。算法可以蒸馏，硬件搬不走。*
