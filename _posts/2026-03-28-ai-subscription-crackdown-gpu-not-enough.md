---
layout: post
title: "一个月前我写了 AI 订阅收紧，现在它真的全面崩了"
date: 2026-03-28
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260328-ai-subscription-crackdown-cover.webp
tags: [featured, AI 订阅, Claude, Anthropic, Google, Antigravity, GPU, 限流, 封号, 订阅经济]
slug: ai-subscription-crackdown-gpu-not-enough
description: "一个月前写 AI 订阅收紧是趋势，现在 Claude Max 用户一条提示词额度清零，Antigravity Pro 配额被砍 97%。250 万人逃离 ChatGPT 投奔 Claude，结果发现 GPU 不够就是不够。充钱不一定是大爷，GPU 才是。"
faq:
  - question: "Claude Max 用户为什么额度异常消耗？"
    answer: "3 月 23 日起 Max 订阅用户发现额度加速消耗。Anthropic 称工作日太平洋时间 5-11 点实施高峰限流，约 7% 用户受影响，但具体消耗倍率未公布。"
  - question: "Google Antigravity Pro 用户配额被砍了多少？"
    answer: "Gemini Pro 用户周配额从 3 亿输入 token 降至不足 900 万，降幅达 97%。达到限额后最长需等 7 天恢复。"
---

2 月 23 号我写了篇文章，标题叫《AI 订阅收紧潮：免费午餐真的结束了》。当时的结论是——Anthropic、Google、智谱同步收紧，这不是巧合，是结构性趋势。

一个月过去了。**<mark>不是趋势了，是崩盘了。</mark>**

![一个月前写收紧，现在全面崩了](/assets/images/screenshot-20260328-ai-subscription-crackdown-cover.webp)

---

## 一、Claude 用户，又被背刺了

3 月 23 日开始，大量 Max 订阅用户发现 5 小时额度莫名加速消耗。有人花 $200/月买的 Max 20x，一条提示词下去，用量从 21% 跳到 100%。Max 5x 用户正常写代码，90 分钟额度就见底。

三天后 Anthropic 终于回应。技术团队的 Thariq Shihipar 发了澄清帖：**工作日太平洋时间 5 点到 11 点，你的 5 小时配额会「消耗得更快」。**

| 细节 | 内容 |
|------|------|
| 高峰时段 | 太平洋 5:00-11:00（北京 20:00-02:00） |
| 影响范围 | 约 7% 用户，Pro 首当其冲 |
| 消耗倍率 | **未公布** |
| 计量维度 | 上下文长度 + 任务复杂度 + 模型选择 |

「消耗得更快」具体多快？1.5 倍？2 倍？4 倍？有人问了。**没有回复。** 这很 Anthropic。

![Claude 高峰限流：你的额度被静默加速消耗](/assets/images/screenshot-20260328-claude-rate-limiting-peak.webp)

开发者 Alexey Pelykh 算了一笔账——用 Claude Code 正常写一天代码，按 API 价格折算约 $200。一个月 20 个工作日，月消耗约 $4000。而月费才 $200。**Anthropic 请不起自助餐了。但请不起和不说清楚是两回事。**

---

## 二、时间线拉长：从逃离 ChatGPT 到挤爆 Claude

把视角拉到一个月前，整条链路就清楚了：

| 时间 | 事件 |
|------|------|
| 2.28 | OpenAI 与五角大楼签约，ChatGPT 卸载量飙升 295% |
| 3.1 | Claude 登顶美国 App Store，付费用户翻倍 |
| 3.13 | Anthropic 推出「错峰双倍」——非高峰时段额度翻倍 |
| 3.23 | Max 用户大面积报告额度异常消耗 |
| 3.26 | Thariq 发帖解释高峰期限流政策 |

**250 万人逃离 ChatGPT 投奔 Claude。** 但 GPU 不会因为你换了阵营就变多。3 月 13 日的「错峰双倍」官方说法是「感谢用户支持」，实际是服务器扛不住了。先砍再送，评论区有人直接骂出来：「三周前所有人的 token 消耗突然暴涨，然后你们搞一出额度翻倍。」

![从逃离 ChatGPT 到挤爆 Claude：一条完整的崩盘链路](/assets/images/screenshot-20260328-chatgpt-exodus-claude-overload.webp)

封号也在同步加速。Anthropic 2025 下半年封禁了 **145 万个账号**，申诉通过率仅 **3.3%**。最近多位用户反馈账号存活周期从半年缩短到不到一个月。注意——**海外账号照封不误。**

---

## 三、不只是 Claude——Antigravity 也扛不住了

谷歌的 AI 编程 IDE Antigravity（反重力）同样崩了。

| 指标 | 变化 |
|------|------|
| Gemini Pro 周配额 | 3 亿 → 不足 900 万（**降 97%**） |
| 恢复等待 | 最长 **7 天** |
| 新计费 | AI 积分系统，$25 买 2500 积分 |
| Ultra 用户（$250/月） | 同样工作流，5 小时 → 90 分钟清零 |

一个积分等于多少 token？**没说。** Google AI 开发者论坛高赞帖标题——「暗砍配额，信任崩盘，生产环境彻底废了」。

评论区有人说每条提示词的体感成本在 $5 到 $15。「提示词 → 充值 → 提示词 → 再充值。」有人直接退订：「太迟了。」

![Antigravity 配额暴降 97%：AI 编程 IDE 的信任危机](/assets/images/screenshot-20260328-antigravity-quota-crash.webp)

---

## 四、自助餐模式，撑不住了

一个月前我说「分层定价是趋势」。现在再看——分层都不够了，**按量计费才是终局。**

月付 $200，用出 $4000 的算力。这个商业模式的数学不成立。Anthropic 先用双倍额度试探错峰意愿，再正式推高峰限流，下一步可能就是更细的分层定价。

这是 Claude 最近的服务状态——**10 天有 7 天在出问题。**

**<mark>GPU 不够就是不够。不管你从 ChatGPT 跑到 Claude，还是从 Claude 跑到 Antigravity——充钱不一定是大爷，GPU 才是。</mark>**

---

## 写在最后

一个月前写那篇文章的时候，我觉得「收紧」可能会是一个缓慢的过程。结果速度远超预期。

现在我的做法更激进了：**核心生产任务锁定 API 按量计费，订阅只保留一个主力平台，剩下的需求全部走开源。** 不是因为穷——是因为订阅制的算力承诺正在变成空头支票。

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>AI 订阅收紧不是黑天鹅——是我一个月前就写过的灰犀牛。只是没想到，犀牛跑得比所有人都快。</mark>**

---

## 相关阅读

**AI 订阅与算力系列**
- [AI 订阅收紧潮：从 Anthropic 到 Google、GLM，免费午餐真的结束了]({{ site.baseurl }}/ai-subscription-tightening-free-lunch-over)
- [月投 650 刀订阅 AI Agent：当 Token 不再有限制，生产力到底能有多大？]({{ site.baseurl }}/agent-arms-race-650-dollars-per-month)
- [黄仁勋：年薪 50 万的工程师，Token 消耗不到 25 万，我会非常担忧]({{ site.baseurl }}/jensen-huang-token-economy-engineer-cad-ai-era)
