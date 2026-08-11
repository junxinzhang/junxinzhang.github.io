---
layout: post
title: "训得出模型，训不明白 Post-training"
date: 2026-08-11
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260811-post-training-chaos.webp
tags: [featured, AI, Post-training, Pre-training, 模型训练, RL, 组织文化, Coding, 智谱, Zaokit]
slug: post-training-chaos-reward-clarity
description: >
  和一位模型厂 post-training researcher 深聊后的核心发现：国内 Pre-training 已经会做了，
  但 Post-training 还在混沌期。根本原因是 reward 的清晰程度完全不同。
  而决定谁能走出混沌的，可能不是技术，是组织文化。
faq:
  - question: "为什么说国内 Post-training 还处于混沌期？"
    answer: "Pre-training 的 reward 非常明确——单位时间内把 Next Token Loss 降到最低，同时降低训练成本。但 Post-training 要解决的是'让模型在下游应用中更好'，而如何定义和评估'更好'、如何确认模型是真的变强而不是在 hacking 指标，都极其 tricky。这种混沌导致拿不到足够资源，资源不够又无法解决混沌，形成恶性循环。"
  - question: "为什么说'大厂一定会赢'是偷懒的推论？"
    answer: "模型竞争不是比身价。更多的钱、卡和人，不等于一定能训出最好的模型。真正起决定性作用的，是组织里有多少人发自内心想把模型训好，以及组织摩擦会不会消耗掉这些人的热情。"
  - question: "Coding 浪潮为什么给独立模型厂商带来了窗口期？"
    answer: "Coding 把按 token 计费的需求真正引爆。智谱定价提高一倍、调用量反涨八倍；Kimi K3 模型 API 输出价与 Claude Sonnet 5 一样。而 BAT 在长达半年的时间里拿不出第一梯队的 coding 模型，这给了独立模型厂商宝贵的时间窗口。"
  - question: "Agent 在 AI Lab 里替代了哪些工作？"
    answer: "以 Infra 为例，现在可以直接告诉 Agent'每秒只能输出 50 个 Token，请优化到 60 个'，然后让它自己检查 Kernel 和整条链路。一些 Infra 工程师因此开始主动转型，跑去研究算法、理解训练需求——Agent 正在模糊数据、算法和 Infra 之间的边界。"
---

今天和一位模型厂的 post-training researcher 聊了两个小时。

聊之前有一个模糊的判断：国内 Pre-training 已经追得很近，Post-training 明显落后。聊完之后判断没变，但理由变得更具体了——**落后的原因不是技术差距，是两件事的 reward 清晰度完全不一样。**

> **Pre-training 的反馈像射靶——靶心在哪清清楚楚。Post-training 的反馈像在雾里找路——你甚至不确定脚下有没有路。**

![训得出模型，训不明白 Post-training](/assets/images/cover-20260811-post-training-chaos.webp)

## 一、Reward 落差：一个清晰，一个混沌

Pre-training 的 reward 非常明确：在单位时间内，把 Next Token Loss 降得越低越好，同时尽可能降低训练成本。方向清楚、指标可量化、进步肉眼可见。

Post-training 要解决的则是另一类问题：怎么让模型在下游应用中表现得更好。但这个「更好」本身就是一团迷雾——

| | Pre-training | Post-training |
|--|-------------|---------------|
| Reward 定义 | Next Token Loss，越低越好 | 「让模型更好」——好在哪？好多少？ |
| 可量化程度 | 极高，loss 曲线一目了然 | 极低，指标容易被 hack |
| 反馈周期 | 实时，每个 step 都有信号 | 滞后，需要复杂的评估流程 |
| 创新可见性 | 架构开源、写 Paper、做 PR | 数据清洗和 Recipe 通常不外传 |

怎么定义「更好」？怎么评估「更好」？怎么确认模型是真的变强了，还是在 hacking 某个指标？每一个都极其 tricky。

这里有一个被忽视的不对称：**Pre-training 的创新更容易被外界看到。** 模型架构没有那么强的机密性，一开源大家就能看到，也可以写成论文做 PR。但一家模型公司的数据清洗方案、具体的训练 Recipe——Post-training 真正的核心竞争力——没有人会拿出来讲。

Pre-training 既有清晰的 reward，又有清晰的声量。Post-training 两样都缺。

加上众所周知的缺卡问题，模型的绝对能力又是生死线，大家自然把更多资源投入反馈更明确、也更容易获得声量的 Pre-training。

**Post-training 因此陷入了一个尴尬的循环：因为混沌，所以拿不到足够多的资源；因为资源不够，这种混沌迟迟无法被解决。**

![Pre-training 靶心清晰 vs Post-training 雾中找路](/assets/images/illust-20260811-reward-clarity-gap.webp)

## 二、「大厂一定赢」是偷懒的推论

聊到竞争格局，有一种声音很常见：大厂有钱有卡有人，最终一定会赢。

这位 researcher 不这么看。

模型竞争不是比身价。更多钱、更多卡、更多人，不等于一定能训出最好的模型。**真正起决定性作用的，可能是组织里到底有多少人发自内心想把模型训好，以及组织摩擦会不会消耗掉这些人的热情。**

这个判断放在当下的市场里，正在被验证——大模型的机会看上去正在重新回到创业公司手里。半年多前这一切还难以想象。

窗口期来自编程。Coding 浪潮把按 token 计费的需求真正引爆，算账方式彻底改变了。智谱定价提高一倍，调用量反而涨了八倍，与海外前沿模型的价差在逐渐缩小。Kimi 比智谱更激进，K3 模型 API 输出价每百万 token 15 美元，与 Claude Sonnet 5 的标准定价一模一样。而 Anthropic 此前推出的 $2/MTok 输入、$10/MTok 输出的限时推广价已决定永久保留，不再按原计划在 9 月 1 日上调——前沿模型的价格战，已经从国内烧到了美国。

窗口期的另一面是大厂的缺位：**在长达半年的时间里，BAT 拿不出一个第一梯队的 coding 模型。** 2 月时人们津津乐道的叙事还是春节红包大战，而智谱 2025 年春天就已经把研究方向聚焦到编程上来。

但窗口期不会一直敞开。字节已宣布不做蒸馏，但在视频模型上已拿出 SOTA 成果，对 Coding 的投入肉眼可见地坚定。大厂只要赢一次，整个叙事就可能重新改写。

更不用说算力采购与人力的结构性优势：阿里今年 5 月表示对算力中心的投入将远超之前承诺的三年 3800 亿；腾讯 Q1 经营性资本支出同比增长 18%、环比增长 84%。而独立模型厂商至今还受困于算力瓶颈，有时甚至向潜在对手租卡。

![Coding 窗口期：创业公司的短暂领跑](/assets/images/illust-20260811-coding-window-startups.webp)

## 三、Agent 正在模糊 AI Lab 的内部边界

我们还聊到了一个正在发生的变化：**Agent 已经开始替代 AI Lab 里的一部分工作。**

拿 Infra 举例。现在可以直接告诉 Agent：「每秒只能输出 50 个 Token，请优化到 60 个」，然后让它自己检查 Kernel 和整条链路。

结果就是，一些 Infra 工程师开始自己给自己找事干——跑去研究算法、理解训练需求。跟一些 researchers 交流下来，有些人确实已经有了失业焦虑。

从这里往外延伸一步：如果说 AI Coding 模糊了产品、研发和设计之间的边界，那么 **AI for AI（RSI）也在逐渐模糊数据、算法和 Infra 之间的边界。**

还有一个更根本的观察：**Model Research 本身，可能就是最 Science 的 AI for Science。** 模型研究不是在解决某个特定领域的问题，而是在研究「通用智能」本身。

![Agent 替代 AI Lab 工作：边界正在模糊](/assets/images/illust-20260811-agent-replacing-lab-work.webp)

## 四、两个没有答案的问题

最后聊了两个真正开放的问题，欢迎有想法的朋友分享你的见解。

**Q1：怎么让模型拥有时间概念？**

如果模型不交卷，它就可以一直保持「我没错」的状态。反正模型不老不死，从它自己的视角看，磨洋工可能并不是什么坏事。

就像《葬送的芙莉莲》里，对于一个能活几千年的精灵来说，花十年寻找一枚戒指完全合理。但我们这些凡胎肉体，根本等不起。

（GPT-5.6 一直写测试，是不是就是深刻践行了这一点 doge）

**Q2：OpenAI 是怎么持续相信 RL，并最终把 o1 做出来的？**

好奇的不是具体 Recipe，而是背后的组织问题。之前请清华叉院助理教授 @jxwuyi 录过一期[播客](https://xiaoyuzhoufm.com/episode/67efcaf5f9578163d601286a)，他提到 OpenAI 很早就在做 RL，但之前做了很久都没有得到结果。

在一个方向连续失败很多年以后，团队为什么还能继续相信它，招到人、说服老板、拿到资源，然后真的把事情做出来？

**这个问题的答案，又绕回了组织文化。**

![两个没有答案的问题](/assets/images/illust-20260811-open-questions.webp)

## 五、组织文化才是真正的变量

跟很多 researchers 交流，尤其是问他们觉得哪家模型更有希望时，大家最后都会强调同一件事：组织文化。

在一个快速变化、资源永远不够的行业里，**怎么把人和算力分给那些还没有答案的创新，以及愿意等这些创新多久**——可能和技术判断本身一样重要。

智谱和 DeepSeek 预计都将在 8 月发布新模型。据了解，智谱 MaaS 开放平台注册用户近 700 万，七月以来增长约 200 万，其中 2.3 万家企业客户；对标 Codex 的 ZCode 上线一个月用户破百万。今年以来智谱 ARR 增长 15 倍。

Coding 的商业模式本身也在快速变化。越来越多企业开始搭建「内部路由」，按任务复杂度把不同价位的模型组合使用。Palantir 则在教育客户只用 API、不用模型厂商的其他工具——它的逻辑是模型最终会大宗商品化，数据和工作流才是企业最珍贵的资产。

**企业用 AI 的第一步，一定要有自己的 MaaS 平台。** 按需分配算力，好钢用在刀刃上。

假如 Scaling Law 的提升真没有尽头，那意味着超级人工智能的实现，届时讨论的就不再是谁的毛利率高几个点了。但在 ASI 到来之前，眼下可以确定的似乎只有一件事——以越来越快的速度不断刷新的顶尖模型排行榜。

**窗口还开着，算力依旧紧缺，人们依然渴望新的顶尖模型出现。而下一次发布，已经排上了日程。**

## 写在最后

压成五句：

1. **Pre-training 的 reward 清晰，Post-training 还在混沌**——不是技术差距，是反馈信号的清晰度差了一个量级
2. **混沌导致恶性循环**——拿不到资源因为说不清价值，说不清价值因为没资源去做
3. **「大厂一定赢」是偷懒的推论**——组织效率比组织规模重要，Coding 窗口期正在证明这一点
4. **Agent 正在模糊 AI Lab 的内部边界**——数据、算法、Infra 的分工正在被 RSI 重新定义
5. **组织文化才是真正的变量**——愿意为没有答案的创新等多久，决定了谁能走出混沌

土话一句：

**模型训出来不算完。训不明白 Post-training，就是在雾里开车——油门踩得再猛，也不知道往哪开。**

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

延伸：[Agent 下一程，打在云上](/agent-next-phase-not-intelligence-race) · [模型天天更新，你的数学呢？](/ai-needs-math-physics-information-theory) · [没烧过 token，就别说看懂 AI 半导体](/token-burn-ai-semiconductor-investing)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。模型训出来不算完——Post-training 的混沌里，藏着这个行业真正的胜负手。*
