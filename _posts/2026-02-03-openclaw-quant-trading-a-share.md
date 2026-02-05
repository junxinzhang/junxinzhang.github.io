---
layout: post
title: "用OpenClaw做A股量化？我试了试，聊聊真实感受"
date: 2026-02-03
author: Jason Zhang
categories: [AI, OpenClaw, 量化交易, A股]
tags: [OpenClaw, AI Agent, 量化交易, A股, Python, vnpy, 浏览器自动化, TradingAgents]
image: assets/images/screenshot-20260203-openclaw-quant-cover.png
slug: openclaw-quant-trading-a-share
description: "有三年美股经验的我，最近在琢磨A股量化。传统策略用腻了，AI Agent这么火，能不能用OpenClaw搞点不一样的？这篇文章聊聊我的探索，以及圈里已经在用的一些方案。"
---

玩美股三年了，最近我对A股量化产生了兴趣。

美股玩得挺顺手，但A股这个市场……T+1、涨跌停、政策敏感、信息差大——<mark>把美股那套直接照搬过来，基本不行</mark>。

正好最近在折腾OpenClaw（之前的[踩坑记录]({{ site.baseurl }}/openclaw-bugs-and-local-fixes)和[Mac Mini体验]({{ site.baseurl }}/openclaw-macos-best-environment)都写过），突然想到：**这玩意能不能用来做量化？**

调研了一圈，发现已经有人在做了，而且玩法比我想象的成熟。

![AI量化交易流程](/assets/images/screenshot-20260203-openclaw-quant-header.png)
*AI量化交易的核心流程：从量化分析到代码策略，再到交易执行*

---

## 先说结论：有搞头，但得找对方向

如果你问我"AI Agent能不能用来做A股量化"：

- **信息收集和舆情分析**：最成熟，已经有开源框架在跑
- **多Agent协作决策**：有人搞出了模拟"交易公司"的架构，挺有意思
- **自动化下单**：能做，但延迟是硬伤——2-5秒的调用延迟，抢不过高频
- **替代专业量化平台**：想多了，不现实

下面展开讲。

---

## 圈里已经在用的方案

调研过程中发现，AI Agent+量化这个方向，<mark>已经有人跑通了</mark>。

### TradingAgents-CN：多Agent协作的A股量化框架

这是我找到的最完整的方案——[TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)，一个专门针对A股的多Agent LLM量化框架。

它的设计思路很有意思：**模拟一家专业交易公司的团队协作**。

系统里有这些Agent角色：
- **基本面分析师**：分析财报、估值
- **情绪分析师**：监控舆情、新闻情感
- **技术分析师**：看K线、技术指标
- **研究员**：整合各方信息，形成研报
- **交易员**：执行交易决策
- **风控经理**：监控风险敞口

这些Agent不是各干各的，而是通过"结构化沟通和辩论"来协作决策。比如基本面分析师说"这公司财报不错"，情绪分析师说"但社交媒体上骂声一片"，然后研究员综合判断。

![多Agent协作架构](/assets/images/screenshot-20260203-multi-agent-architecture.png)
*多Agent协作架构：不同角色的Agent各司其职，通过协作形成决策*

<!-- 图片提示词：Flat vector illustration, Minimalist, Line art style. A diagram showing multi-agent collaboration architecture: 6 connected agent icons in a circular arrangement - each represented by simple geometric avatars with different symbols (chart icon for analyst, shield for risk manager, terminal for trader, magnifying glass for researcher, heart for sentiment analyst, gear for technical analyst). Arrows showing communication flow between agents. Center hub with brain/AI icon. Color: Warm pastel colors - soft coral, peach, lavender, mint. Beige background. Aspect Ratio 2.35:1. -->

技术栈也挺现代：
- 支持多种LLM（OpenAI、Claude、阿里百炼都行）
- 整合了国内金融数据源：**Tushare、AkShare、BaoStock**
- 有智能新闻分析模块
- 支持Docker部署，还有模拟交易环境

<mark>这套方案的定位是"学习和研究"，不是让你直接拿去实盘炒股</mark>。但架构设计值得参考。

### Claude Code做算法交易：YouTube上有人出教程了

搜了下发现，已经有人用Claude Code构建算法交易系统，还出了完整教程。

主要思路是：
- 用Claude快速生成交易策略代码
- 接入数据层获取清算信息、持仓变化、鲸鱼动向、订单流
- 自动化执行回测和模拟交易

**但有个关键限制要注意**：Claude的调用延迟在2-5秒。

这意味着什么？<mark>毫秒级的高频交易别想了</mark>。要做实时交易，得配合WebSocket连接来获取live数据，Claude只能做分析和决策，执行层走别的通道。

### 鲸鱼追踪+订单流分析

还有一个有意思的方向：用AI Agent追踪"鲸鱼"（大户）的动向。

有人用ElizaOS + Claude Code搭了个鲸鱼追踪器：
- 监控特定钱包地址的链上活动
- 设置阈值，检测大额交易
- 识别订单簿里的"鲸鱼墙"
- 自动发Telegram警报

这个思路在A股也能用——监控龙虎榜、大宗交易、股东变动，用Agent做实时分析和预警。

---

## 传统量化的几个痛点

说了别人怎么做的，再聊聊我为什么想折腾AI Agent。

传统量化——不管是趋势跟踪、因子投资还是统计套利——核心都是对历史数据建模。这套方法有效，但也有明显的瓶颈：

**数据太同质化**

大家都在用同样的量价数据，策略越来越卷，超额收益越来越难找。

**市场变了策略就废了**

去年管用的策略，今年可能直接失效。市场结构一变，参数调来调去也救不回来。

**只看结构化数据**

K线、财报、技术指标……这些大家都在看。但市场信息远不止这些——新闻、政策、社交媒体舆情、研报观点——<mark>这些"非结构化数据"往往更有信息量，但传统量化工具用不上</mark>。

---

## OpenClaw能帮上什么忙？

OpenClaw本质上是个能自己动手的AI助手。它的核心能力是**浏览器自动化**——能像人一样浏览网页、抓取信息、甚至操作界面。

结合上面调研到的方案，我想到几个具体场景。

### 场景一：信息收集和舆情监控

这是我觉得最靠谱的用法，也是TradingAgents-CN里"情绪分析师"Agent在做的事。

让OpenClaw每天自动浏览：
- **财经网站**：东方财富、同花顺、雪球
- **券商研报平台**：抓取最新研报摘要
- **交易所公告**：巨潮资讯、上交所、深交所
- **社交媒体**：微博财经大V、股吧热帖

![浏览器自动化抓取](/assets/images/screenshot-20260203-browser-data-collection.png)
*OpenClaw Browser Relay：能像人一样浏览网页，抓取信息*

<!-- 图片提示词：Flat vector illustration, Minimalist, Line art style. A browser window icon with multiple floating data cards being collected: news headlines, stock tickers, social media posts, and document icons flowing into a funnel or collector. Include elements: web crawler spider icon, RSS feed symbol, and sentiment indicators (thumbs up/down). Color: Warm pastel colors - peach, cream, soft blue, mint green. Beige background. Clean tech aesthetic. Aspect Ratio 2.35:1. -->

它不只是抓数据，还能结合NLP能力做情感分析——这条新闻是利好还是利空？社交媒体对这个事件的反应是积极还是消极？

<mark>把这些信息转化成量化因子</mark>，比如"政策利好因子"、"舆情热度因子"，就能给传统策略加一个维度。

### 场景二：多Agent协作（模仿TradingAgents-CN的思路）

OpenClaw本身不是多Agent框架，但可以作为其中的"执行层"。

设想这样一个架构：
- **信息收集Agent**：OpenClaw负责，浏览器自动化抓数据
- **分析Agent**：Claude负责，做NLP分析和研判
- **执行Agent**：对接vnpy或其他量化平台

各司其职，通过API或消息队列协作。

![OpenClaw 工作环境](/assets/images/screenshot-20260203-workspace-setup.png)
*我的 OpenClaw 日常工作环境：Mac Mini + 宽屏显示器*

<!-- 图片提示词：Flat vector illustration, Minimalist, Line art style. A clean desk setup showing: Mac Mini (simple rounded rectangle), widescreen monitor displaying terminal window with code and stock charts side by side, keyboard, and coffee cup. Floating elements: AI brain icon, chart trending up, and notification bells. Color: Warm pastel colors - soft beige, cream, coral accents, mint highlights. Beige background. Cozy tech workspace vibe. Aspect Ratio 2.35:1. -->

### 场景三：监控和报警

让Agent实时盯着市场和策略状态：

- 行情数据有没有异常
- 策略跑着有没有报错
- 持仓风险敞口是不是超限
- 关注的股票有没有重大公告

一旦发现问题，自动发警报（微信、Telegram、邮件都行）。

### 场景四：自动化下单？

理论上，OpenClaw可以跟量化平台（比如vnpy）对接，策略生成信号后自动下单。

**但说实话，我对这个场景持保留态度。**

两个原因：

1. **延迟问题**：前面说了，Claude调用延迟2-5秒。A股虽然不是毫秒级高频，但关键时刻这几秒也够呛。
2. **稳定性问题**：之前踩过Chrome Relay的坑——<mark>连接不稳定、经常断线</mark>。量化交易对稳定性要求极高，关键时刻掉链子可不是闹着玩的。

如果要用，建议只拿来做辅助，核心交易逻辑还是走传统API。

---

## A股的"特色"怎么应对？

A股跟美股不一样的地方很多。OpenClaw能帮上忙吗？

### T+1交易制度

买了今天不能卖，限制了日内交易的灵活性。这个OpenClaw帮不上忙，策略层面要调整思路——更注重波段和趋势。

### 政策敏感性强

这倒是OpenClaw能发挥的地方。

让Agent专门监控证监会、交易所官网、主流财经媒体，一旦有政策发布，第一时间抓取、分析，跟持仓股票做关联。

A股政策影响大，<mark>信息早一步，决策就多一分从容</mark>。

### 公告效应显著

业绩预告、高送转、股权变动……这些公告往往能引发股价剧烈波动。

设定Agent监控特定股票的重大公告，结合历史数据做回溯分析，搞事件驱动策略。

TradingAgents-CN里就有"智能新闻分析模块"，专门干这个。

---

## 几个现实问题

说了好处，也得说说坑。

### 延迟是硬伤

再强调一遍：<mark>AI Agent的调用延迟在2-5秒</mark>。

这意味着：
- 高频交易别想了
- 抢涨停板别想了
- 盘中急跌止损可能来不及

只能做中低频策略，或者把AI Agent定位成"分析师"而不是"交易员"。

### 数据质量参差不齐

非结构化数据虽然信息量大，但噪音也多。假消息、标题党、情绪化言论……<mark>垃圾进，垃圾出</mark>，数据清洗和筛选是个大工程。

TradingAgents-CN整合了Tushare、AkShare、BaoStock这些专业数据源，这块可以借鉴。

### 黑箱问题

AI Agent的决策过程往往不透明。在金融交易里，你不光要知道"怎么做"，还得说清"为什么这么做"——合规审查、风险控制都需要这个。

### 系统稳定性

之前说了，Chrome Relay目前稳定性不够。跑复杂的自动化任务，出问题的概率不小。

我在[Mac Mini那篇文章]({{ site.baseurl }}/openclaw-macos-best-environment)里提过，M芯片的能效比和稳定性确实不错，但软件层面的坑还是要注意。

![Mac Mini vs 服务器对比](/assets/images/screenshot-20260203-mac-mini-vs-server.png)
*Mac Mini vs 传统服务器：功耗低、稳定，但Chrome Relay本身的坑还是存在*

<!-- 图片提示词：Flat vector illustration, Minimalist, Line art style. Split comparison layout: Left side shows a compact Mac Mini icon with checkmarks (low power, quiet, stable), Right side shows a traditional server rack with warning signs (complex, high power, noisy). Center dividing line with "VS" text. Include simple icons: lightning bolt for power, sound waves for noise, clock for uptime. Color: Warm pastel colors - Mac Mini side in soft mint/green tones (positive), Server side in soft coral/orange tones (cautionary). Beige background. Aspect Ratio 2.35:1. -->

---

## 给不同读者的建议

**如果你是技术背景，想尝试AI+量化：**
- 先看看[TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)，架构设计很有参考价值
- 从信息收集和舆情分析入手，这块最成熟
- 核心交易逻辑还是用传统平台（vnpy这些），OpenClaw做辅助
- 做好踩坑的心理准备

**如果你是纯投资者，不太懂技术：**
- 目前还不是开箱即用的阶段
- 建议再观望一段时间，等工具更成熟
- 可以先关注一些AI量化的科普内容，了解基本概念

---

## 写在最后

OpenClaw能不能用来做量化？能，但目前更适合做"外挂"而不是"主力"。

调研下来，我觉得最靠谱的路径是：

1. **用OpenClaw做信息收集**——这是它的强项
2. **结合专业框架做分析**——比如TradingAgents-CN的多Agent协作思路
3. **用传统平台做执行**——vnpy、聚宽这些，稳定性有保障

<mark>AI Agent的价值不在于替代传统量化，而在于补足它的短板</mark>——尤其是非结构化数据的处理能力。

工具在进化，玩法也在进化。我会继续折腾，有新发现再更新。

---

## 相关阅读

**OpenClaw 系列**
- [Mac Mini被AI圈抢光了，真的值得买吗？我的OpenClaw实测体验]({{ site.baseurl }}/openclaw-macos-best-environment)
- [OpenClaw尝鲜报告：这款爆火的AI工具，现在能用吗？]({{ site.baseurl }}/openclaw-bugs-and-local-fixes) - 踩坑与修复
- [OpenClaw之父的AI Agent实战手册]({{ site.baseurl }}/moltbot-father-agentic-engineering-insights) - Peter Steinberger 访谈精华
- [Clawdbot刷屏AI圈，我为什么劝你别急着用]({{ site.baseurl }}/clawdbot-why-you-should-wait) - 安全风险分析

**AI Agent 系列**
- [通用AGI工具已经到来]({{ site.baseurl }}/claude-code-general-agi-tool-has-arrived) - Claude Code 深度分析
- [你觉得AI不行？也许是你的'使用姿势'还停在2023年]({{ site.baseurl }}/ai-usage-posture-evolution) - AI 使用姿势演进

**延伸资源**
- [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) - A股多Agent量化框架（GitHub）

---

## 联系方式

如果你也在琢磨AI+量化，欢迎交流：

- 邮箱：jason2023zhang@gmail.com
- 微信：winnielove2020
- 博客：[https://junxinzhang.com](https://junxinzhang.com)

特别想听听：
- 你有没有用AI Agent做量化的经验？
- TradingAgents-CN这类框架实际跑起来效果如何？
- A股量化有哪些特别的坑？

---

> **关注我，后续分享更多 AI Agent 的真实体验和踩坑记录。**
