---
layout: post
title: "Codex 不只是写代码了：它现在能像真人一样操作你的 Mac"
date: 2026-04-18
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260418-codex-computer-use-cover.jpg
tags: [featured, OpenAI, Codex, Computer Use, AI Agent, 图像生成, Zaokit]
slug: codex-computer-use-not-just-coding-anymore
description: "Codex 最新支持 Computer Use，能在 Mac 上浏览屏幕、点鼠标、打字。整合图像生成、持久记忆和任务调度，从编码工具进化为全能 AI 操作系统。"
faq:
  - question: "Codex Computer Use 是什么？"
    answer: "Codex 现在能通过 macOS Accessibility API 看到屏幕、移动光标、点击和打字，像真人一样操作桌面应用，不需要 API 接入。"
  - question: "Codex 的图像生成能力怎么用？"
    answer: "Codex 内置 GPT-Image-1.5，在同一个工作流里直接生成和修改图片，无需切换工具或单独配置 API Key。"
---

这两天Codex 的更新频率已经到了让人焦虑的程度——**几乎一天好几个版本**。不是小修小补，是整个产品形态在变。

上周它还是一个「帮你写代码」的桌面应用，这周直接变成了——**一个能像真人一样操作你电脑的 AI Agent。**

**<mark>Codex 不再只是一个编码助手。它在向全能 AI 操作系统进化，而这个速度，正在全面对标 Claude Code。</mark>**

![Codex 不只是写代码了：它正在向全能 AI 操作系统进化](/assets/images/screenshot-20260418-codex-computer-use-cover.jpg)

---

## 一、Computer Use：像真人一样操作你的 Mac

这次更新最炸裂的功能叫 **Computer Use**——Codex 现在能**看你的屏幕、移动光标、点击按钮、打字**，跟你自己操作电脑没有区别。

**不需要 API。** 很多应用根本没有公开 API，Codex 直接通过 macOS Accessibility API 读取界面层级，像人一样操作。

![像人一样操作：看屏幕、点鼠标、打字](/assets/images/screenshot-20260418-codex-human-like-ops.jpg)

| 以前 | 现在 |
|------|------|
| 只能操作有 API 的工具 | 任何有界面的应用都能操作 |
| 需要写脚本做自动化 | 自然语言描述就行 |
| 需要人盯着 | 后台独立运行，不抢你的鼠标 |

**它不会抢你的鼠标键盘。** 运行在隔离工作区里，你该干嘛干嘛，还能同时开几个 Agent 并行跑任务。收集竞品信息、批量录入数据、自动测试前端、迭代 UI——**原来需要人一步步点的活儿，现在全甩给 Codex。**

---

## 二、图像生成打通了：不用再切工具

Codex 这次把 **GPT-Image-1.5** 直接整合进了工作流。以前生成图要切到 DALL·E 或 Midjourney，现在——**同一个对话里直接说「帮我生成首页 banner」，图就出来了。** 不满意接着改，它直接在原图上修。

![一个流程，全部打通：代码、图像、浏览、调度](/assets/images/screenshot-20260418-codex-unified-workflow.jpg)

| 能力 | 说明 |
|------|------|
| 图像生成 | 内置 GPT-Image-1.5，直接出图 |
| 图像迭代 | 同一对话里修改优化 |
| 代码+图像联动 | 设计完直接转代码 |
| 无需额外配置 | 不用单独搞 API Key |

**真实的开发流程从来不是纯写代码。** 设计稿、原型图、素材、文档——以前每个环节切一个工具，现在全在一个上下文里搞定。工具链断裂的痛，Codex 正在消灭。

---

## 三、持久记忆 + 任务调度：AI 终于有了「连续工作」的能力

之前 AI 工具的共同痛点：**对话一关，啥都忘了。** Codex 这次上了两个杀手级特性：**持久记忆** 和 **任务调度**。

持久记忆：Codex 能记住你的偏好、技术栈、项目结构。说过一次「我用 Next.js 15 + Tailwind」，下次不用再说。

任务调度更猛——**Codex 可以安排自己在未来执行任务：**

- 「每天早上检查 PR queue，有新的就做 code review」
- 「爬虫跑完把结果汇总发给我」
- 「每周五自动跑回归测试」

![记住上下文，持续执行，安排未来](/assets/images/screenshot-20260418-codex-persistent-automation.jpg)

**这不是 cron job，是理解上下文的 cron job。** 它知道项目状态、上次做到哪、出了问题该怎么处理。

| 特性 | 旧模式 | Codex 新模式 |
|------|--------|-------------|
| 上下文 | 每次重新交代 | 自动记忆偏好和历史 |
| 任务连续性 | 单次对话即结束 | 同一线程持续执行 |
| 未来任务 | 需要外部调度 | 内置安排，自动执行 |
| 工作跨度 | 分钟级 | 天级甚至周级 |

---

## 四、全面对标 Claude Code

Anthropic 的 Claude Code 最近凭 Computer Use 火得一塌糊涂。OpenAI 这次的回应速度令人咋舌：从宣布到推送，几乎没给市场反应时间。

上述更新已于本周四（4月16日）开始推送，面向 Codex 桌面应用用户，**目前仅支持 macOS**。加上 90 多个新插件（Jira、GitLab、Microsoft Suite 等），Codex 的野心很清晰：**不做编码工具，做 AI 原生的工作操作系统。**

---

## 五、国内大厂的困局

看完 Codex 再回头看国内大厂，有点替他们着急。

**技术好解决，真正难的是组织。** 顶层决策者还被上一个时代的成功经验束缚着，负责组织形态设计的关键角色，还被不真正懂 AI 的人把持着。他们不是不知道 AI 重要——是没有体感。

![率先突破禁锢的组织，将赢得未来](/assets/images/screenshot-20260418-codex-org-evolution.jpg)

不过我的判断是：**这种进化一旦发生，速度不可阻挡，回不去从前。** 就像移动互联网来时，有人说「手机屏幕那么小能干啥」，几年后整个商业世界被重构。**就看哪个组织能率先突破这一禁锢了。**

---

## 写在最后

Codex 这轮更新的核心信号：**AI 正在从「帮你写东西」进化到「帮你做事情」。** 看屏幕、点鼠标、生成图片、记住上下文、安排未来任务——加在一起，这已经不是「工具」，是数字员工的雏形。

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**2026年4月30日前1000名用户赠送价值150RMB的Pro计划**，助力大家高效完成图文创作和PPT生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>工具在进化，组织在被倒逼。你不需要等所有人都准备好——你只需要比你的竞争对手早一步，开始用 AI 帮你做事。</mark>**

---

## 相关阅读

- [模型都差不多了，凭什么 Codex 还能赢？]({{ site.baseurl }}/codex-infra-speed-real-moat-ai-companies)
- [给老板讲清楚AI Agent：说白了就是一个死循环]({{ site.baseurl }}/agent-loop-skill-token-explained-for-everyone)
- [AI 重构生产关系：中层消失、定价崩塌]({{ site.baseurl }}/ai-restructure-production-pricing-middle-management-dead)
