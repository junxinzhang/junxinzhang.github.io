---
layout: post
title: "2月14日观察：Cloudflare 开放 Markdown for Agents 后，个人站为什么必须做一次 Agent 化升级"
date: 2026-02-14
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260214-cf-agent-cover.webp
tags: [featured, Cloudflare, Markdown for Agents, llms.txt, AI SEO, Agent, 个人站]
slug: cloudflare-markdown-for-agents-personal-site-upgrade
description: "作为 Cloudflare 深度用户，我从实操角度拆解 Markdown for Agents 的真正价值：它不是一个小功能，而是个人站从‘仅人类可读’走向‘人类+Agent双可读’的关键拐点。文末给出30天落地路线图。"
geo_facts:
  - text: "Cloudflare 官方示例显示，同一页面从 HTML 转为 Markdown 后，输入 token 可从 16,180 降到 3,150，约减少 80%。"
  - text: "Markdown for Agents 目前面向 Cloudflare 付费计划（Pro、Business、Enterprise），并支持 SSL for SaaS。"
  - text: "Cloudflare 支持两种获取方式：请求 /cdn-cgi/llm 路径，或对原 URL 发送 Accept: text/markdown 内容协商。"
  - text: "当开启内容信号策略时，Cloudflare 默认会附加 X-Robots-Tag: noai，并可按策略对允许的 AI Bot 附加可选的 content signal header。"
  - text: "Cloudflare 文档列出转换条件：页面需为 text/html、包含 Content-Length 且不超过 1MB，且源站不能直接返回压缩后的 HTML。"
faq:
  - question: "有了 Cloudflare Markdown for Agents，还需要 llms.txt 吗？"
    answer: "需要。Cloudflare 的边缘转换很重要，但 llms.txt / llms-full.txt 仍是稳定、可控、可长期维护的站点级 AI 入口，建议同时保留。"
  - question: "个人站是否应该直接允许所有 AI 训练抓取？"
    answer: "不建议一刀切。建议先区分‘搜索/检索’与‘训练抓取’两类用途，按内容价值和授权策略分层开放。"
  - question: "免费计划可以使用 Markdown for Agents 吗？"
    answer: "截至本文写作日期（2026-02-14），Cloudflare 文档显示该功能面向付费计划（Pro、Business、Enterprise）。"
  - question: "如何快速验证我的站点是否已经成功输出 Markdown？"
    answer: "可用 curl 对同一 URL 分别请求默认头和 Accept: text/markdown 进行对比，再检查返回 content-type 与 body 是否仍含完整 HTML 标签。"
---

## 前言：这不是“又一个小开关”，而是发布通道的代际变化

今天是 2026 年 2 月 14 日。过去几个月，我在自己的站点上持续做了 AI 入口改造：`llms.txt`、`llms-full.txt`、`for-agents` 页面、结构化摘要，以及面向 Agent 的验证脚本。

Cloudflare 在 **2026 年 2 月 12 日**发布了 [Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/)。很多人把它理解成“把 HTML 转成 Markdown 的便利功能”。

我的结论更激进一点：**它是个人站从“只服务人类读者”，升级为“同时服务人类读者 + AI Agent”的关键基础设施。**

![Cloudflare 打开 Agent 入口后的个人站升级方向](/assets/images/screenshot-20260214-cf-agent-cover.webp)

<!-- 封面图提示词（2.35:1）：概念化技术封面，中心是橙色云朵演变为蓝色数据流，左右分别代表“传统网页”与“Agent可读结构化世界”，大标题“个人站进入Agent时代”，副标题“Cloudflare打开了第一道门”，所有文字简体中文，数字插画风，Aspect Ratio 2.35:1。 -->

---

## 一、为什么这件事对个人站是“刚需”，不是“可选项”

过去做内容分发，我们默认“入口只有人”。

现在不同了。越来越多流量先经过 AI 搜索、答案引擎、站内 Agent，再决定要不要把用户导向你的原文页面。也就是说，**你的第一读者，很多时候已经不是人，而是模型。**

Cloudflare 官方给了一个非常直观的数据：同样内容，HTML 输入大约 16,180 tokens，Markdown 约 3,150 tokens，减少接近 80%。

这不是数字游戏，而是三个直接结果：

1. 模型读取更快，摘要与引用延迟更低。
2. 解析噪音更少，答案稳定性更高。
3. 推理成本下降后，你的内容被“完整读完”的概率会更大。

![传统网站与 Agent 网站的核心差异对比](/assets/images/screenshot-20260214-cf-agent-compare.png)

<!-- 插图1提示词（2.35:1）：左右对比信息图，标题“传统网站 vs Agent网站”，左侧“HTML+JS、Token高、结构不稳定”，右侧“llms.txt、Markdown协商输出、结构化事实块、引用更稳定”，中文大字，扁平矢量风格，Aspect Ratio 2.35:1。 -->

---

## 二、Cloudflare 到底开放了什么？先把能力边界讲清楚

如果只记一句话：**Cloudflare 给了你一个“边缘层翻译器”。**

你可以通过两种方式拿到 Markdown：

1. 请求 `https://your-domain.com/cdn-cgi/llm`
2. 对原 URL 发 `Accept: text/markdown` 进行内容协商

除此之外，还有两个很关键但容易被忽略的点：

1. [内容信号策略（Content Signals）](https://developers.cloudflare.com/content-signals/setup/content-signals-policy/)可以细化 AI 爬虫行为，并附加信号头。
2. [转换条件有明确限制](https://developers.cloudflare.com/agents/markdown-infra/markdown-for-agents/)：`text/html`、`Content-Length <= 1MB`、源站不要直接给压缩 HTML，否则可能回退原始 HTML。

这意味着：它不是“万能魔法”。你仍然要做好源站结构、页面体积、内容组织和缓存策略。

![Cloudflare Markdown for Agents 请求链路流程图](/assets/images/screenshot-20260214-cf-markdown-flow.png)

<!-- 插图2提示词（2.35:1）：流程图，标题“Markdown for Agents 请求链路”，节点包含“Agent请求(Accept:text/markdown)→Cloudflare Edge→条件检查→Markdown输出/HTML回退”，右下角加“内容信号策略：默认X-Robots-Tag:noai，可配置AI Bot信号头”，全部简体中文，Aspect Ratio 2.35:1。 -->

---

## 三、作为 Cloudflare 深度用户，我给个人站的升级建议是“四层栈”

我参考了自己最近几篇文章的实操路径（例如 [《AI Agent Skill 与 MCP 新手指南》]({{ site.baseurl }}/ai-agent-skill-mcp-beginner-guide)、[《独立开发者AI军备竞赛实录》]({{ site.baseurl }}/solo-dev-ai-arms-race-survival)、[《Gemini-3 Deep Think 实测》]({{ site.baseurl }}/gemini-3-deep-think-real-experience)），总结出一套更稳的升级框架：

### 第 1 层：内容层（Content）

每篇文章至少提供：
- 可复述的一句话摘要
- 关键事实块（可被直接引用）
- FAQ（覆盖高频追问）

### 第 2 层：协议层（Protocol）

保证这些入口长期稳定：
- `llms.txt`
- `llms-full.txt`
- `sitemap.xml`
- `feed.xml`

### 第 3 层：边缘层（Edge）

在 Cloudflare 侧启用与治理：
- Markdown for Agents
- Content Signals Policy
- 针对 AI Bot 的抓取策略与权限边界

### 第 4 层：观测层（Observability）

别只看 PV，要看 Agent 指标：
- Markdown 命中率
- token 成本变化
- 被引用率（被答案引擎引用的频次）
- 引用后回流转化（点击/订阅/咨询）

![个人站 Agent 化四层升级栈](/assets/images/screenshot-20260214-cf-upgrade-stack.png)

<!-- 插图3提示词（2.35:1）：四层框架图，标题“个人站Agent化四层升级栈”，从下到上“内容层、协议层、边缘层、观测层”，右侧目标“更快理解、被引用率提升、分发链路变长”，全部中文大字，现代信息图风，Aspect Ratio 2.35:1。 -->

---

## 四、给普通创作者也能执行的 30 天落地计划

很多人觉得“Agent 优化”很难，是因为一上来就做平台级改造。

我的建议是：**先做低成本、可复用、可验证的动作**。

- Day 1-3：盘点现有内容与入口，补齐 `for-agents` 页面
- Day 4-10：给高价值文章补摘要、事实块、FAQ
- Day 11-20：启用 Cloudflare Markdown for Agents，执行 `curl` 验证
- Day 21-30：观测抓取与引用数据，集中优化高潜文章

![个人站 Agent 化 30 天路线图](/assets/images/screenshot-20260214-cf-roadmap-30d.png)

<!-- 插图4提示词（2.35:1）：时间线信息图，标题“个人站Agent化30天路线图”，四阶段“基线盘点、内容重构、边缘接入、观测优化”，底部标语“先可读，再可检索，最后可执行”，全部简体中文，Aspect Ratio 2.35:1。 -->

---

## 五、几个容易踩的坑：越早知道，越省时间

### 1) 把“AI 搜索”与“AI 训练”混为一谈

检索曝光和训练授权是两件不同的事。建议用策略分层，不要一次性全开或全关。

### 2) 只做边缘转换，不做内容结构

Markdown for Agents 可以降低噪音，但不会替你写出“可引用结构”。源内容杂乱，输出照样杂乱。

### 3) 把 llms.txt 当成过时方案

恰恰相反。边缘转换是“动态通道”，`llms.txt` 是“稳定目录”。两者叠加才是长期方案。

### 4) 只看访问量，不看“被机器理解后的传播能力”

Agent 时代，真正的竞争指标是：**你是否被正确理解、准确引用、持续复用。**

---

## 六、最小验证清单（可以直接抄）

```bash
# 默认请求（通常是 HTML）
curl -I https://junxinzhang.com/

# 请求 markdown 协商输出
curl -I https://junxinzhang.com/ -H 'Accept: text/markdown'

# 看 body 前 40 行是否仍是完整 HTML 标签
curl -s https://junxinzhang.com/ -H 'Accept: text/markdown' | head -n 40
```

如果你在 Cloudflare 上托管站点，建议把这套检查做成日常巡检脚本。我的站点已经有 `scripts/verify-markdown-for-agents.sh`，可以直接跑。

---

## 结语：面向 Agent 不是“迎合机器”，而是扩大你的真实受众

我把这轮升级理解为一次“协议升级”：

- 对人，继续保留高质量阅读体验。
- 对 Agent，提供低噪音、可验证、可引用的内容通道。

当 Cloudflare 把这条边缘通道打开后，个人站最该做的不是观望，而是尽快把内容从“可读”推进到“可执行”。

**未来的内容竞争，不只是写得好，而是谁先成为 Agent 生态里“可被稳定调用的节点”。**

---

## 参考资料（官方）

1. Cloudflare Blog: [Introducing markdown for agents](https://blog.cloudflare.com/markdown-for-agents/)
2. Cloudflare Docs: [Markdown for Agents](https://developers.cloudflare.com/agents/markdown-infra/markdown-for-agents/)
3. Cloudflare Docs: [Content Signals Policy](https://developers.cloudflare.com/content-signals/setup/content-signals-policy/)
4. Cloudflare Blog: [Control how AI crawlers and bots access your content](https://blog.cloudflare.com/control-content-use-for-ai-training/)
