---
layout: post
title: "AI 订阅收紧潮：从 Anthropic 到 Google、GLM，免费午餐真的结束了"
date: 2026-02-23
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260223-ai-subscription-tightening-cover-v2.webp
tags: [featured, AI 订阅, Anthropic, Google, GLM, 智谱, OpenAI, Claude Max, AI Ultra, 订阅经济, 定价策略]
slug: ai-subscription-tightening-free-lunch-over
description: "2026 年 2 月，Anthropic 推出 $200/月的 Max 计划并限制第三方工具，Google 祭出 $250/月的 AI Ultra，智谱 GLM-5 涨价 30%-60%，OpenAI 测试 $100/月的 Pro Lite。当所有 AI 公司都在收紧免费额度、拉高付费门槛时，背后的逻辑是什么？普通用户又该怎么应对？"
geo_facts:
  - text: "Anthropic 官网显示：Claude Max 5x 定价 $100/月，Max 20x 定价 $200/月，Pro 保持 $20/月。"
  - text: "Google 2026 年推出 AI Ultra 计划，定价 $249.99/月，包含 30TB 存储和最高模型访问权限；AI Pro 为 $19.99/月。"
  - text: "智谱 GLM Coding Plan 于 2026 年 2 月发布涨价公告，整体涨幅 30% 起，海外 API 价格涨幅达 30%-60%。"
  - text: "OpenAI 于 2026 年 2 月 21 日测试 ChatGPT Pro Lite 计划，定价 $100/月，填补 Plus（$20）与 Pro（$200）之间的价格空档。"
  - text: "Anthropic 于 2026 年 2 月明确限制第三方工具通过 OAuth 订阅认证使用 Claude，要求商业集成必须走 API 密钥认证。"
faq:
  - question: "为什么 AI 公司突然集体涨价或收紧订阅？"
    answer: "核心原因是算力成本持续飙升、模型参数规模指数膨胀、用户使用量爆发式增长，以及资本市场对商业化回报的压力。免费或低价策略在用户增长阶段有效，但在模型能力跃升后已不可持续。"
  - question: "普通用户最应该关注哪些变化？"
    answer: "三个关键变化：① 免费额度持续缩减；② 高端模型正在被锁在更贵的订阅层里；③ 第三方工具和反向代理的使用空间正在收窄。"
  - question: "我现在该不该锁定年付订阅？"
    answer: "如果你是重度用户，锁定当前价格是明智的（尤其是 Google AI Pro 年付五折到 $99.99/年的窗口）。但如果你只是轻度使用，先评估实际用量再决定。"
  - question: "开源模型能替代订阅吗？"
    answer: "部分场景可以。GLM-5 开源版、MiniMax M2.5 等模型在特定任务上已接近闭源旗舰水平。但在长程 Agent 任务、超大上下文窗口等场景，闭源旗舰仍有优势。"
---

这两天刷信息流，一条接一条看到的全是涨价、限额、收紧。

先是有人转了 Anthropic 的 TOS 更新——不让第三方工具用 OAuth 认证了；然后是 Google AI Ultra $250/月 的截图在社群里炸开；紧接着智谱 GLM-5 涨价 30%-60% 的公告也出来了；昨天 OpenAI 又被爆出在测试 $100/月的 Pro Lite。

**<mark>一句话结论：2026 年 2 月，AI 行业正在经历一轮系统性的「订阅收紧潮」。免费午餐的窗口在快速关闭，付费门槛在快速拉高。</mark>**

![AI 订阅收紧潮封面](/assets/images/screenshot-20260223-ai-subscription-tightening-cover-v2.webp)

<!-- 封面图提示词（baoyu-cover-image，严格 2.35:1）：
Type=conceptual, Palette=dark, Rendering=digital, Text=title-subtitle, Mood=bold。
画面中央是一把巨大的金色钥匙和银色锁链的组合体，钥匙上刻着"订阅"二字，锁链缠绕着三家公司的抽象图标（紫色水晶体/蓝色光环/绿色立方体）。背景深空渐变色，上方飘浮价格标签"$20""$100""$200""$250"。
标题（中文）：《AI 订阅收紧潮：免费午餐结束了》
副标题（中文）：《从 Anthropic 到 Google、GLM，你的钱包准备好了吗？》
要求：中文文字清晰、禁止英文大字、科技紧迫感、Aspect Ratio 2.35:1、输出 PNG。
-->

如果你只有 30 秒，先看这 3 条：

1. 这轮不是某一家在涨价，而是 Anthropic、Google、智谱、OpenAI **<mark>同时在收紧</mark>**——方向一致，节奏高度同步。
2. 收紧的不只是价格，还有使用方式：第三方工具限制、用量上限、模型分层锁定，三管齐下。
3. 对普通用户来说，现在最重要的不是"选哪家"，而是**<mark>搞清楚自己的真实用量，然后决定锁不锁价</mark>**。

---

## 一、到底发生了什么：先看事实

我先把这一轮各家的动作摆出来。这些信息来自各家官网、官方公告和公开报道，我尽量标注了来源。

### 1.1 Anthropic：Max 计划 + 第三方工具限制

Anthropic 在这一轮里做了两件事：

**第一件：推出 Claude Max 计划。**

| 计划 | 月费 | 核心权益 |
|---|---|---|
| Claude Pro | $20/月 | 5 倍免费额度，优先访问，200K 上下文 |
| Claude Max 5x | $100/月 | Pro 的 5 倍额度（约免费 25 倍），完整 Claude Code |
| Claude Max 20x | $200/月 | Pro 的 20 倍额度（约免费 100 倍），最高优先级 |

Max 计划的定位很清楚：给那些把 Claude 当核心生产工具的重度用户。Extended Thinking、Memory、Agent Team、最新的 Opus 4.6——都锁在 Max 层级里。

**第二件：限制第三方工具使用 OAuth 认证。**

2026 年 2 月，Anthropic 明确更新了消费者条款：用 Free/Pro/Max 订阅获取的 OAuth token，**<mark>不允许用于第三方产品、工具或服务的商业用途</mark>**。想做商业集成？必须走 API 密钥认证。

这条规则直接打击了一个灰色地带：有人用 $20/月的 Pro 订阅，通过反向代理或第三方工具享受本该走 API 按量计费的服务——Anthropic 称之为「token 套利」。

同时，Anthropic 还在 2 月份公开指控部分中国实验室通过代理网络和大量伪造账号对 Claude 进行「蒸馏攻击」，用来训练自己的模型。2 月 24 日凌晨，Anthropic 官方推特直接点名 DeepSeek、Moonshot AI 和 MiniMax，称这些实验室创建了超过 24,000 个伪造账号，与 Claude 进行了超过 1600 万次对话，用以提取能力并训练自家模型。这条推文在发布几小时内就获得了 3.2 万个点赞和 866 万次查看。

![Anthropic 官方推文：指控工业级蒸馏攻击](/assets/images/screenshot-20260223-anthropic-distillation-tweet.webp)

![2026年2月 AI 订阅变动时间线](/assets/images/screenshot-20260223-ai-subscription-timeline-v2.webp)

<!-- 插图1提示词（baoyu-article-illustrator，严格 2.35:1）：
Type=timeline, Style=sci-fi。
标题（中文）：《2026年2月 AI 订阅变动时间线》
内容：从左到右五个事件节点，每个节点用公司代表色标注，节点间发光连线。
要求：中文信息图，深蓝底色，节点清晰，Aspect Ratio 2.35:1。
-->

### 1.2 Google：AI Ultra $250/月，三级火箭

Google 在这一轮的动作更大——直接把订阅体系拆成了三级：

| 计划 | 月费 | 核心定位 |
|---|---|---|
| Google AI Plus | $7.99/月 | 入门级，200GB 存储，基础 Gemini 3 Pro |
| Google AI Pro | $19.99/月 | 主力，2TB 存储，Gemini 2.5 Pro/3.1 Pro，Deep Research |
| Google AI Ultra | $249.99/月 | 旗舰，30TB 存储，Veo 3.1，Deep Think，Agent Mode |

$250/月的 AI Ultra 是什么概念？比 Anthropic 的 Max 20x 还贵 $50。它给的东西确实多——30TB 云存储、最强模型全开、每月 $100 Google Cloud 积分——但这个价格已经不是"个人订阅"的逻辑了，更像是"个人工作站"的定价。

另一个值得注意的细节：Google 给美国大学生**免费提供 AI Pro**（到 2026 年春截止），并且把这个优惠扩展到了日本、巴西、印尼和英国的学生。这是典型的「先培养使用习惯，再转化为付费用户」的策略。

### 1.3 智谱（GLM）：GLM-5 发布当天就涨价

智谱的操作最直接：GLM-5 发布，同步涨价。

- GLM Coding Plan **整体涨幅 30% 起**
- 海外 API 价格涨幅 **30%-60%**
- 取消首购优惠折扣
- 已有订阅用户保持原价

涨价的理由也写得很坦诚：用户需求和使用量强劲增长，算力投入和模型优化成本不断攀升，原有定价无法覆盖。

但引发争议的不只是涨价本身。GLM-5 作为更大、更复杂的模型（7440 亿参数），在高峰时段的资源消耗是 GLM-4.7 的 **3 倍**，非高峰时段也要 **2 倍**。这意味着同一份订阅，你实际能用到的量变少了。

用户反弹之后，智谱发了道歉信，承认了规则透明度不够、升级机制设计不合理、GLM-5 上线节奏太慢等问题，并为 Lite 和 Pro 用户提供了 2026 年 1 月 1 日至 2 月 22 日期间的退款通道。

### 1.4 OpenAI：测试 Pro Lite，免费用户看广告

OpenAI 这边有两个动作：

1. **测试 ChatGPT Pro Lite**：$100/月，填补 Plus（$20）和 Pro（$200）之间的巨大价格断层。
2. **在免费和 Go 用户中测试广告**：2026 年 2 月开始在美国地区测试。

这两个动作加在一起，信号很清楚：OpenAI 认为 $20 到 $200 之间还有一批愿意付费、但不愿付到最高档的用户——这正是 Anthropic Max 5x（$100）瞄准的同一群人。

同时，GPT-4o 在 2 月被 GPT-5.2 替代成为默认模型，免费用户的额度进一步收紧到每 5 小时 10 条消息。

---

## 二、为什么是现在：四个驱动力

很多人的第一反应是「资本家嘴脸」。但如果你冷静看，这一轮收紧不是贪婪，而是**<mark>结构性的成本压力</mark>**终于传导到了定价层。

![为什么 AI 公司集体收紧订阅](/assets/images/screenshot-20260223-ai-subscription-drivers.webp)

<!-- 插图2提示词（baoyu-article-illustrator，严格 2.35:1）：
Type=framework, Style=sci-fi。
标题（中文）：《为什么 AI 公司集体收紧订阅？》
内容：四大驱动力框架——算力成本飙升、模型规模扩张、用量爆发式增长、商业化压力——汇聚到结论"分层定价+使用限额+第三方限制"。
要求：中文框架图，暗底亮字，极简信息完整，Aspect Ratio 2.35:1。
-->

### 2.1 算力成本在指数级增长

训练 GLM-5 需要多少算力？7440 亿参数，全昇腾芯片训练。训练 Opus 4.6？百万级 token 上下文窗口。Gemini 3 Deep Think？多轮推理链路、搜索增强。

这些能力不是免费的。GPU/TPU 的需求在以比摩尔定律更快的速度增长，而芯片供应链的扩产远远跟不上。

### 2.2 模型参数量在膨胀

2024 年头部模型还在千亿级别。现在？GLM-5 是 7440 亿，而且这还只是一个"中等大小"的选手。参数量翻倍，推理成本不是翻倍——可能是 3 倍甚至更多（智谱自己承认了 GLM-5 的资源消耗倍率）。

### 2.3 用户使用量在爆发

春节期间，豆包除夕当天 AI 互动 19 亿次，千问连续多日登顶 App Store，Claude Code 的重度用户每周使用超过 40 小时。

当「有事先问 AI」成为习惯，每个用户消耗的算力都在大幅增长。Anthropic 专门提到了「power users」的 24/7 全天候使用模式是收紧限额的直接原因之一。

### 2.4 商业化压力到了兑现窗口

Anthropic 的估值超过 600 亿美元，OpenAI 的估值超过 1500 亿美元。这些估值建立在一个前提上：**这些公司能把用户转化为稳定的付费收入**。

投资人不会永远等下去。2026 年，是「烧钱换增长」转向「验证商业闭环」的元年。各家同时收紧，不是巧合，是投资人在后面推着走。

---

## 三、收紧的不只是价格：三个维度的「围城」

如果你只看到了「涨价」，那你只看到了冰山一角。这一轮收紧是三维的：

### 3.1 维度一：价格阶梯越拉越长

以前的选择很简单：免费或者 $20/月。

现在呢？

| 价位段 | 代表 | 核心差异 |
|---|---|---|
| 免费 | ChatGPT Free / Claude Free / Gemini Free | 极低额度，降级模型，可能看广告 |
| $8/月 | ChatGPT Go / Google AI Plus | 基础模型无限制，无高级功能 |
| $20/月 | ChatGPT Plus / Claude Pro / Google AI Pro | 主力模型，中等额度 |
| $100/月 | Claude Max 5x / ChatGPT Pro Lite（测试中） | 高额度，高级功能全开 |
| $200/月 | Claude Max 20x / ChatGPT Pro | 接近无限制 |
| $250/月 | Google AI Ultra | 全模型全功能，含云存储和云积分 |

**从 $0 到 $250，跨度是 2024 年的 12 倍以上。** 这不是简单的涨价，而是在建立一套完整的「能力分层」体系——你付多少钱，就能用多强的模型、多大的额度、多高的优先级。

![AI 订阅阶梯全景](/assets/images/screenshot-20260223-ai-subscription-comparison.webp)

<!-- 插图3提示词（baoyu-article-illustrator，严格 2.35:1）：
Type=comparison, Style=blueprint。
标题（中文）：《AI 订阅阶梯：从免费到月付 $250 的全景》
内容：三列对比（入门层/专业层/旗舰层），底部标注"模型能力↑ 使用限额↑ 月费↑"。
要求：中文对比图，工程化蓝图风格，层次清晰，Aspect Ratio 2.35:1。
-->

### 3.2 维度二：使用限额越做越细

以前的限额是粗放的：每天多少条消息。

现在的限额越来越精细：

- **按模型分级计量**：GLM-5 消耗是 GLM-4.7 的 3 倍，意味着同一份订阅用 GLM-5 跑得更快见底
- **按时段差异计价**：高峰/非高峰消耗倍率不同
- **按功能分别设限**：Thinking 提示词和 Pro 提示词分开计数（Google 做了这个区分）
- **按周计量**：Anthropic 的 Claude Code 引入了周累计小时上限

这些精细化限额的本质是：**同一个月费下，你的实际可用量在缩水。** 尤其是当你用的是最新、最强的模型时。

### 3.3 维度三：第三方工具空间在收窄

Anthropic 限制 OAuth 认证用于第三方工具，是这一轮最值得关注的信号。

为什么？因为它打击的不只是「token 套利」，还包括了大量依赖 Claude 认证的第三方 AI 工具和集成方案。这些工具如果不走 API 按量计费，就失去了合法接入的途径。

这背后的逻辑是：**<mark>AI 公司正在从「获客阶段」进入「收入保护阶段」。</mark>** 在获客阶段，第三方生态是扩大影响力的助手；在收入保护阶段，第三方生态是利润的「漏洞」。

---

## 四、对你意味着什么：分三种情况

### 4.1 如果你是轻度用户（每天用几次，主要查信息/写文档）

**你暂时不需要紧张。** $20/月的 Pro/Plus 层仍然是性价比最高的选择，各家都没有大幅削减这一层的核心权益。

但要注意一件事：免费层的可用性在持续下降。ChatGPT 免费用户已经被限到每 5 小时 10 条消息，Google 免费用户的高级模型访问也在收紧。如果你是"能不付费就不付费"的类型，体验会越来越差。

### 4.2 如果你是中度用户（每天高频使用，涉及编码/分析/创作）

**现在是评估并锁价的窗口。**

- Google AI Pro 年付五折到 $99.99/年（约 $8.3/月），这个价格可能不会持续很久
- 如果你依赖 Claude Code，$100/月的 Max 5x 可能比你想象的更快成为刚需
- 密切关注 OpenAI Pro Lite 的正式上线，$100/月可能是重度 ChatGPT 用户的最优解

### 4.3 如果你是重度用户/开发者（把 AI 当核心生产工具）

**你需要重新审视成本结构。**

$200-$250/月 的订阅，年化就是 $2400-$3000。如果你有多个需求场景，可能需要同时订多个平台——年化成本轻松突破 $5000-$10000。

这时候要认真考虑几个替代路径：

1. **API 按量计费**：如果你的使用模式是波动性的（有些天重度、有些天不用），按量计费可能比固定月费更经济
2. **开源模型本地部署**：GLM-5 开源版、MiniMax M2.5 等模型在很多场景下够用，尤其是你有 GPU 资源的话
3. **多模型路由**：简单任务用便宜模型（Flash/Haiku），复杂任务才用旗舰模型，用编排层控制成本

---

## 五、往远看一步：这不是终点，而是新秩序的起点

![普通用户的应对策略指南](/assets/images/screenshot-20260223-ai-subscription-strategy.webp)

<!-- 插图4提示词（baoyu-article-illustrator，严格 2.35:1）：
Type=framework, Style=minimal-flat。
标题（中文）：《普通用户的应对策略指南》
内容：左侧"短期策略"四点建议，右侧"长期趋势"三个预测，底部核心原则。
要求：中文策略图，实操导向，清晰易读，Aspect Ratio 2.35:1。
-->

我认为这一轮收紧之后，AI 订阅市场会形成三个长期趋势：

### 5.1 分层会更细，而不是更简单

现在的 5-6 个层级可能只是开始。未来可能出现按功能模块付费（单独付 Code/Vision/Voice）、按项目付费、甚至按结果付费的模式。混合定价（订阅 + 用量）已经被 56% 的 AI 行业领导者认为是最优解。

### 5.2 开源成为真正的平衡力量

每一次闭源模型涨价，都是开源模型的获客窗口。GLM-5 开源版在 SWE-Bench Verified 上达到开源 SOTA，MiniMax M2.5 发布不到 24 小时就全球开源。当闭源旗舰越来越贵，开源的「good enough」替代就越有吸引力。

### 5.3 广告模式会成为"第三条路"

OpenAI 已经开始在免费和 Go 用户中测试广告。这个方向的逻辑是：不是所有人都愿意或有能力付 $20+/月，但 AI 公司也不愿意完全放弃这批用户——广告补贴是折中方案。可以预见，「免费 + 看广告 = 使用基础模型」会成为标配。

---

## 写在最后

这篇文章写到一半的时候，我自己也在想：我到底应该锁哪家的年付？

想了一圈，最后的答案是：**先别急着锁，先搞清楚你到底在用哪些能力。**

很多人（包括我）在 2025 年养成了一个习惯：什么都往 AI 里丢，不管是查个菜谱还是重构一个系统架构。但这两件事消耗的算力差了几个数量级。当免费额度充裕时，你不需要区分；当每一次调用都有成本时，你必须区分。

所以我现在的做法是：

1. 把日常轻量任务（查信息、翻译、简单问答）交给免费层或最便宜的模型
2. 把核心生产任务（编码、分析、长文写作）留给付费订阅的旗舰模型
3. 持续关注开源模型的进展——它们是你的议价筹码

**<mark>AI 不会回到免费时代了，但你不必为用不到的能力买单。</mark>**

按需选型、避免锁定、保持灵活——这可能是 2026 年最实用的 AI 消费策略。

---

## 参考资料（官网/官方）

1. Anthropic Claude Pricing（Pro / Max 计划定价）
   https://claude.ai/pricing
2. Anthropic Consumer Terms of Service（第三方工具使用限制）
   https://claude.ai/legal
3. Google AI Subscriptions（AI Plus / AI Pro / AI Ultra）
   https://gemini.google/pricing
4. Google Blog：AI Subscriptions Announcement
   https://blog.google/products/gemini/
5. 智谱 GLM Coding Plan 价格调整公告（2026-02）
   https://zhipuai.cn/
6. 智谱 Z.AI Docs：GLM-5 API Pricing
   https://docs.z.ai/guides/llm/glm-5
7. OpenAI ChatGPT Plans（Free / Go / Plus / Pro）
   https://openai.com/chatgpt/pricing
8. TestingCatalog：OpenAI 测试 ChatGPT Pro Lite（$100/月）
   https://testingcatalog.com/
9. Anthropic：Economic Analysis of AI Distillation Attacks
   https://www.anthropic.com/
10. 行业报告：2026 AI Pricing Trends（混合定价模型占比 56%）
    https://prompts.ai/

## 版权声明

本文所引用的定价数据和政策信息均来源于各公司官网和公开报道，主要用于行业分析和信息参考。价格和政策可能随时变化，请以各家官方最新信息为准。

---

> 💡 **福利时间**：既然说到 Google AI Ultra，我自己的 **Google AI Ultra 家庭计划目前还有 2 个位置**。如果你正好有主力需求，又想省心、省钱地用上 30TB 存储和最强模型，欢迎私信我（或在评论区留言）。**先到先得，满员即止！**
