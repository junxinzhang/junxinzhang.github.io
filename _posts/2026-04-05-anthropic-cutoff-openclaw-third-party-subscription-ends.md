---
layout: post
title: "最后一刀落下来了：Anthropic 正式切断 Claude 订阅对第三方工具的支持"
date: 2026-04-05
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260405-anthropic-openclaw-cutoff-cover.webp
tags: [featured, Claude, Anthropic, OpenClaw, 第三方工具, 订阅经济, OAuth, API Key, Boris Cherny, Claude Code]
slug: anthropic-cutoff-openclaw-third-party-subscription-ends
description: "Anthropic 正式宣布：太平洋时间 4 月 4 日中午 12 点起，Claude Pro 和 Max 订阅不再覆盖 OpenClaw 等第三方工具用量。从 1 月技术屏蔽到 2 月条款更新再到今天正式断供——三刀下来，第三方 AI 工具的灰色地带彻底封死。"
faq:
  - question: "Claude 订阅还能用第三方工具吗？"
    answer: "不能了。自太平洋时间 2026 年 4 月 4 日中午 12 点起，Claude Pro 和 Max 订阅不再覆盖通过 OpenClaw 等第三方工具产生的用量。用户需购买额外用量包或使用 API Key 按量付费。"
  - question: "Anthropic 给了什么补偿？"
    answer: "现有订阅用户会获得一笔等于月费金额的一次性额度作为过渡补偿。不满意的用户可通过次日邮件中的链接申请全额退款。"
---

昨晚刷到 Boris Cherny 的公告，愣了三秒。

**Claude Code 负责人亲自下场宣布：太平洋时间 4 月 4 日中午 12 点起，Claude Pro 和 Max 订阅将不再覆盖通过 OpenClaw 等第三方工具产生的用量。**

不是警告，不是灰度测试，是即刻生效。

**<mark>从 1 月技术屏蔽、2 月条款更新，到今天 Boris Cherny 亲自出面断供——Anthropic 用三个月的时间，把第三方工具接入 Claude 订阅的灰色地带彻底封死了。最后一刀，落下来了。</mark>**

![Anthropic 断供：第三方工具时代终结](/assets/images/screenshot-20260405-anthropic-openclaw-cutoff-cover.webp)

---

## 一、发生了什么：Boris Cherny 的公告

事情很简单，但影响面极大。

Claude Code 负责人 Boris Cherny 在官方渠道发布公告，核心信息三条：

| 项目 | 内容 |
|------|------|
| 生效时间 | 太平洋时间 4 月 4 日 12:00 PM（北京时间 4 月 5 日凌晨 3:00） |
| 影响范围 | Claude Pro、Max 订阅不再覆盖 OpenClaw 等第三方工具用量 |
| 替代方案 | ① 购买额外用量包（当前有折扣）② 使用 API Key 按量付费 |

**补偿方案**：现有订阅用户获得等于月费金额的一次性额度。嫌不够？第二天邮件里有全额退款链接。

Anthropic 的说辞很直白——**「不可持续的需求」和「对系统的超额压力」。** 订阅计划的设计初衷，从来不是为了承接第三方工具那种 7×24 小时、Agent 驱动的重度用量模式。

![用户的两条路：用量包 vs API Key](/assets/images/screenshot-20260405-anthropic-user-options-comparison.webp)

**<mark>翻译成人话：你用 $20 的 Pro 订阅，通过 OpenClaw 跑出了 $200 的算力消耗。Anthropic 说，这笔账我不认了。</mark>**

---

## 二、三刀封堵：从 1 月到 4 月的完整链路

这不是突发事件。Anthropic 从今年 1 月就开始有计划地封堵这个口子——

| 时间 | 动作 | 性质 |
|------|------|------|
| 1 月 | 技术层屏蔽第三方工具伪装 Claude Code 的行为 | 技术封堵 |
| 2 月 | 更新消费者服务条款，明确禁止订阅 OAuth token 用于第三方产品 | 法律封堵 |
| 4 月 4 日 | Boris Cherny 正式宣布断供，即刻生效 | 行政封堵 |

三步走，每一步都在收紧绞索。

**1 月的技术屏蔽**很有针对性。OpenClaw 等工具之前的做法是模拟 Claude Code 客户端的请求特征，让 Anthropic 的服务端以为这是官方工具在调用。Anthropic 更新了检测机制，识别并阻断了这种伪装行为。

**2 月的条款更新**是法律层面的补刀。新条款明确写了：用 Free、Pro、Max 订阅获取的 OAuth token，不允许用于任何第三方产品、工具或服务。想做商业集成？走 API Key，按量付费。

**4 月 4 日的公告**则是最后的行政执行。此前虽然有技术屏蔽和法律条款，但部分用户和工具仍在打擦边球。Boris Cherny 这次是把话讲死了——**即刻停止覆盖，不留缓冲期。**

![Anthropic 三步封堵时间线](/assets/images/screenshot-20260405-anthropic-timeline-three-steps.webp)

**<mark>技术封、法律封、行政封——三道防线全拉满。Anthropic 不是在「调整政策」，是在系统性地消灭第三方工具寄生订阅的可能性。</mark>**

---

## 三、为什么要封：GPU 不是慈善，Token 不是自来水

这件事的底层逻辑，我在 2 月和 3 月的文章里反复写过——**GPU 不够用。**

让我拉几个数据：

| 维度 | 数据 |
|------|------|
| Claude Code 重度用户日消耗 | 约 $200 API 等值（Alexey Pelykh 测算） |
| Max 20x 月费 | $200 |
| 工作日月消耗（20 天） | 约 $4,000 |
| 倍率 | **月费的 20 倍** |

这还只是正常使用。第三方工具 OpenClaw 的场景更夸张——它本质上是一个自主运行的 AI Agent，可以 24 小时不间断调用 Claude，执行浏览器自动化、代码生成、数据抓取等任务。

**一个 $20/月的 Pro 用户，通过 OpenClaw 能产生等价于 API 按量付费数百甚至上千美元的用量。** 这对 Anthropic 来说在商业上完全不可持续。

从资本市场的角度看，Anthropic 估值超过 600 亿美元。投资人要的是营收增长，而不是让订阅费被第三方工具「蒸馏」成廉价算力的通道。**「不可持续的需求」不是客气话——是财务事实。**

**<mark>你用月费买到了「无限自助餐」的体验，但 GPU 的账单是按盘子算的。当第三方工具帮你一盘接一盘地端，餐厅就只能把门关了。</mark>**

---

## 四、对你意味着什么：三种人、三条路

### 如果你是 OpenClaw 用户

两个选项摆在面前：

1. **买用量包**：Anthropic 目前提供折扣价的额外用量包，绑定 Claude 账号，按用量扣减。好处是不用改工作流；坏处是价格透明度不高，而且长期成本可能远超你的想象。
2. **走 API Key**：注册 Anthropic 开发者平台，获取 API Key，在 OpenClaw 中配置。纯按量付费，用多少扣多少。价格透明，但没有了「无限量」的心理安全感。

### 如果你是 Claude Code 纯正用户

**短期影响不大。** Boris Cherny 的公告针对的是第三方工具，Claude Code 本身作为 Anthropic 官方产品，仍在订阅覆盖范围内。但要注意——Anthropic 3 月已经实施过高峰期限流，Claude Code 的用量也不是真正「无限」的。

### 如果你是开发者/创业者

这是一个信号：**AI 平台正在从开放走向收窄。** 如果你的产品依赖某个 AI 平台的订阅认证体系，今天是 Anthropic 断供，明天可能就是 OpenAI 或 Google 跟进。**平台风险，必须认真对待。**

![订阅经济的围墙正在收紧](/assets/images/screenshot-20260405-anthropic-subscription-wall-closing.webp)

---

## 写在最后

从 2 月写订阅收紧潮，到 3 月写全面崩盘，再到今天写断供落地——三篇文章，三个月，一条完整的链路。

**结论没变过：AI 订阅的「自助餐模式」正在消亡。** Anthropic 只是走得最快的那一个。

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>当 Anthropic 亲手把第三方工具赶出订阅体系时，它其实在告诉所有人一件事——GPU 算力不是福利，而是稀缺资源。谁想用，就得按真实成本买单。免费寄生的时代，到此为止。</mark>**

---

## 相关阅读

**AI 订阅与算力系列**
- [一个月前我写了 AI 订阅收紧，现在它真的全面崩了]({{ site.baseurl }}/ai-subscription-crackdown-gpu-not-enough)
- [AI 订阅收紧潮：从 Anthropic 到 Google、GLM，免费午餐真的结束了]({{ site.baseurl }}/ai-subscription-tightening-free-lunch-over)
- [月投 650 刀订阅 AI Agent：当 Token 不再有限制，生产力到底能有多大？]({{ site.baseurl }}/agent-arms-race-650-dollars-per-month)
