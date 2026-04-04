---
layout: post
title: "三分钟搞定：iPhone 上直接跑 Gemma 4 大模型，端侧 AI 彻底变天了"
date: 2026-04-04
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260404-iphone-gemma4-edge-cover.webp
tags: [featured, Gemma 4, iPhone, Google AI Edge Gallery, 端侧AI, On-Device, Agent Skills, 大模型]
slug: iphone-gemma4-edge-gallery-on-device-ai
description: "iPhone 上直接运行 Gemma 4 大模型，不需要云端、不需要 API Key、不需要折腾环境。App Store 下载 Google AI Edge Gallery，三分钟内完成部署。端侧 AI 不再是概念——它已经跑在你口袋里了。"
faq:
  - question: "iPhone 上怎么运行 Gemma 4？"
    answer: "在 App Store 搜索并下载 Google AI Edge Gallery，打开后点击 Agent Skills，下载 Gemma-4-E2B-it 模型（约 2.54GB），下载完成即可离线使用，支持中文对话。"
  - question: "Google AI Edge Gallery 支持哪些功能？"
    answer: "支持 AI Chat（多轮对话）、Agent Skills（工具调用）、Ask Image（图片问答）、Audio Scribe（语音转文字）和 Prompt Lab（参数调试），所有功能均在设备端完成，无需联网。"
---

昨天刚写完 Gemma 4 开源发布，今天就有人问我：**这东西能在 iPhone 上跑吗？**

能。而且简单到离谱。

**App Store 搜索「Google AI Edge Gallery」→ 下载 → 打开 → 点 Agent Skills → 下载模型 → 完事。** 三分钟，不需要科学上网，不需要 API Key，不需要配任何环境。

**<mark>端侧大模型不再是 PPT 上的概念。Gemma 4 跑在 iPhone 上，完全离线，支持中文，带工具调用——这件事今天每个人都能做到。彻底变天了。</mark>**

![iPhone 运行 Gemma 4：端侧 AI 彻底变天](/assets/images/screenshot-20260404-iphone-gemma4-edge-cover.webp)

---

## 一、三步搞定：小白也能上手

先说结论——**这是我见过门槛最低的大模型体验方式，没有之一。**

| 步骤 | 操作 | 耗时 |
|------|------|------|
| 1 | App Store 搜索「Google AI Edge Gallery」，下载安装 | 30 秒 |
| 2 | 打开 App，点击「Agent Skills」 | 5 秒 |
| 3 | 选择 Gemma-4-E2B-it，点击下载（约 2.54GB） | 2-3 分钟 |

![实际操作截图：Google AI Edge Gallery 界面、Agent Skills 模型选择与初始化](/assets/images/screenshot-20260404-iphone-gemma4-real-screenshots.webp)

下载完就能用。**没有注册、没有登录、没有 Token 额度限制。** 模型跑在你手机的芯片上，数据不出设备，完全离线工作。

对比一下传统方式：

| 维度 | 云端 API 方式 | iPhone 端侧方式 |
|------|-------------|----------------|
| 前置条件 | 注册账号 + API Key + 信用卡 | App Store 下载 |
| 网络要求 | 必须联网 | 下载后完全离线 |
| 使用成本 | 按 Token 计费 | 免费，无限使用 |
| 隐私保护 | 数据上云 | 数据不出手机 |
| 上手时间 | 30 分钟起 | 3 分钟 |

**<mark>以前想体验大模型，门槛是技术；现在门槛只剩一个——你的 iPhone 储存空间够不够放 3GB 模型。</mark>**

![三步上手：从下载到对话的完整流程](/assets/images/screenshot-20260404-iphone-gemma4-setup-flow.webp)

---

## 二、不只是聊天——Agent Skills 才是真正的杀器

大多数人用大模型就是「聊天」。但 Google AI Edge Gallery 的核心功能不是 AI Chat——**是 Agent Skills。**

什么意思？**模型不只是回答你的问题，它还能主动调用工具帮你做事。**

| 功能 | 说明 |
|------|------|
| **AI Chat** | 多轮对话，支持「Thinking Mode」展示推理过程 |
| **Agent Skills** | 工具调用，可查维基百科、生成地图、展示信息卡片 |
| **Ask Image** | 拍照或选图，模型直接看图回答问题 |
| **Audio Scribe** | 语音实时转文字，支持翻译 |
| **Prompt Lab** | 调参数（temperature、top-k），测试特定场景 |

重点说 Agent Skills。它让手机上的模型第一次具备了**「行动能力」**——不只是生成文本，而是能像一个助手一样操作工具、查询信息、组合行动。

举个例子：你问它「上海明天天气怎么样」，传统聊天模型只能瞎编一个答案。但带 Agent Skills 的 Gemma 4，**可以调用工具去查真实数据，再把结果整理给你。**

社区还在 GitHub Discussions 上分享自定义 Skill，你甚至可以通过 URL 加载第三方 Skill。**这不是一个聊天 App——这是一个可扩展的端侧 AI Agent 平台。**

**<mark>当模型跑在手机上，还能调工具、查信息、做决策——「AI Agent」就不再是需要服务器支撑的概念了。它已经装进了你的口袋。</mark>**

![Agent Skills：端侧 AI 的工具调用能力](/assets/images/screenshot-20260404-iphone-gemma4-agent-skills.webp)

---

## 三、中文实测：到底能不能用？

很多人对端侧模型的印象还停留在「英文还行，中文拉胯」。

实测结论：**Gemma-4-E2B-it 的中文能力完全可用。** 日常对话、知识问答、文本摘要、简单推理——表现超出预期。

当然，E2B 毕竟是等效 2B 参数的轻量模型，**复杂数学推理和长篇代码生成不是它的强项。** 但作为一个跑在手机上的离线助手，它的性价比无敌：

| 能力 | 表现 |
|------|------|
| 日常中文对话 | ✅ 流畅自然 |
| 知识问答 | ✅ 基本准确 |
| 文本摘要 | ✅ 抓重点能力强 |
| 简单推理 | ✅ 逻辑清晰 |
| 复杂数学 | ⚠️ 偶有错误 |
| 长篇代码 | ⚠️ 不如大参数模型 |
| 图片理解 | ✅ 识别准确，中文描述 |

**另一个让我惊喜的功能是 Thinking Mode。** 打开后，模型会展示逐步推理过程——你能看到它是怎么「想」的。这不只是一个 debug 工具，更是理解 AI 推理逻辑的窗口。

还有 Ask Image 功能：对着一张菜单拍照，模型直接告诉你每道菜是什么、大概多少钱。**在手机上，离线状态下。**

**<mark>端侧模型的中文能力已经跨过了「能用」的门槛。对于不想按 Token 付费、不想数据上云的用户来说，这就是最好的选择。</mark>**

![中文实测：端侧 Gemma 4 的真实表现](/assets/images/screenshot-20260404-iphone-gemma4-chinese-test.webp)

---

## 四、这意味着什么？端侧 AI 格局正在重写

谷歌做这件事的意图很清楚——**把 AI 的入口从云端拉回设备端。**

| 维度 | 云端时代 | 端侧时代 |
|------|---------|---------|
| 模型入口 | 浏览器 / API | 手机 App |
| 算力位置 | 数据中心 | 手机芯片 |
| 使用成本 | 按量付费 | 一次下载，无限使用 |
| 数据主权 | 平台控制 | 用户自持 |
| 可用性 | 依赖网络 | 随时随地 |

苹果的 Apple Intelligence 还在磨磨蹭蹭，谷歌已经把 Gemma 4 送进了 iPhone。**这不是技术PR——这是在苹果的地盘上抢占端侧 AI 的入口。**

更深层的影响在于：**当每台手机都能跑大模型时，AI 的基础设施就从「云」变成了「端」。** API 调用模式不会消失，但它不再是唯一选择。用户有了第二条路——免费、离线、数据不出设备。

对开发者来说，这意味着一件事：**你的下一个 AI 应用，不一定要接 API。** Gemma 4 + AI Edge Gallery 的组合，已经可以支撑相当多的应用场景，而且零成本。

**<mark>端侧 AI 不是云端 AI 的降级替代品——它是另一条路。当谷歌把 Gemma 4 塞进 iPhone 时，这条路已经铺好了。苹果该紧张了。</mark>**

---

## 写在最后

从昨天 Gemma 4 开源发布，到今天三分钟在 iPhone 上跑起来——**谷歌用 48 小时完成了从「模型发布」到「人人可用」的闭环。**

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>AI 正在从云端迁移到口袋里。Gemma 4 跑在 iPhone 上这件事，标志着一个时代的分水岭——端侧 AI 不再是实验室的玩具，而是每个人手中的工具。下载一个 App，三分钟，你就拥有了一个永远在线、永远免费的 AI 助手。</mark>**

---

## 相关阅读

**AI 模型与端侧部署系列**
- [太卷了，谷歌凌晨直接王炸：Gemma 4 开源，本地跑，推理成本接近零]({{ site.baseurl }}/google-gemma4-open-source-local-agent-zero-cost)
- [苹果终于松口了：Mac 外接 AMD / NVIDIA 显卡驱动正式放行]({{ site.baseurl }}/mac-egpu-amd-nvidia-driver-thunderbolt-usb4)
- [苹果无心插柳：Mac Studio 快断货了，因为 Token 已经是生产力]({{ site.baseurl }}/mac-studio-ai-era-fortress-token-productivity)
