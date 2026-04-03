---
layout: post
title: "太卷了，谷歌凌晨直接王炸：Gemma 4 开源，本地跑，推理成本接近零"
date: 2026-04-03
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260403-gemma4-cover.jpg
tags: [featured, Gemma 4, Google, 开源模型, 本地推理, Function Calling, AI Agent, Apache 2.0, MoE]
slug: google-gemma4-open-source-local-agent-zero-cost
description: "谷歌凌晨发布 Gemma 4 开源模型家族，Apache 2.0 许可、原生函数调用、支持本地运行。从 2B 边缘设备到 31B 旗舰，推理成本被压到接近于零。OpenAI、Anthropic 们的 API 收费模式，正面临前所未有的挑战。"
faq:
  - question: "Gemma 4 是什么？和 Gemini 有什么关系？"
    answer: "Gemma 4 是谷歌基于 Gemini 3 技术发布的开源模型家族，采用 Apache 2.0 许可证。包含 E2B、E4B、26B MoE 和 31B Dense 四个版本，覆盖从手机到工作站的全场景。"
  - question: "Gemma 4 可以在本地运行吗？需要什么硬件？"
    answer: "可以。E2B/E4B 可在手机、树莓派等边缘设备运行；26B MoE 和 31B Dense 可在消费级 GPU 和工作站运行。支持 Ollama、vLLM、llama.cpp 等本地推理工具。"
---

凌晨刷到消息，睡意全无。

**谷歌没有任何预热，直接甩出了 Gemma 4 全家桶——四个模型，Apache 2.0 开源，原生支持函数调用，从手机到工作站全覆盖。**

不是 demo，不是预览版，是可以立刻下载、本地跑、商用的正式发布。

**<mark>当 OpenAI 和 Anthropic 还在靠 API 调用按 Token 收费时，谷歌直接把模型送到了你的设备上。推理成本？接近于零。这不是技术发布——这是一次商业模式层面的降维打击。</mark>**

![谷歌凌晨王炸：Gemma 4 开源发布](/assets/images/screenshot-20260403-gemma4-cover.jpg)

---

## 一、四个模型，一次到位

Gemma 4 不是单一模型，是一个完整的模型家族。四个版本，各有定位：

| 模型 | 参数量 | 定位 | 上下文窗口 |
|------|--------|------|-----------|
| E2B | 等效 2B | 手机、IoT、边缘设备 | 128K |
| E4B | 等效 4B | 手机、树莓派、Jetson | 128K |
| 26B MoE | 26B（每 Token 激活 3.8B） | 消费级 GPU、离线工作站 | 256K |
| 31B Dense | 31B 全量激活 | 高性能推理、复杂任务 | 256K |

**E2B/E4B 能在手机上跑，还支持原生音频输入。** 26B MoE 用 MoE 架构，每个 Token 只激活 3.8B 参数，效率拉满——**跑出来的效果是 31B 的 97%，但推理成本砍了一大半。**

31B Dense 是旗舰，在 Arena AI 排行榜开放权重模型里排第三。AIME 2026 数学推理 89.2%，LiveCodeBench v6 编程能力 80%，GPQA Diamond 科学推理 84.3%。

**<mark>一个模型家族覆盖手机到服务器，这不是在发产品——这是在铺生态。谷歌要的不是某个场景的胜利，是全场景通吃。</mark>**

![Gemma 4 模型家族全景：从边缘到旗舰](/assets/images/screenshot-20260403-gemma4-model-family.jpg)

---

## 二、函数调用 + 本地运行 = AI Agent 脱离云端

Gemma 4 全系标配两个能力：**原生函数调用** 和 **结构化 JSON 输出**。

这意味着什么？模型不只是能聊天——**它可以主动调用工具、查询 API、执行代码、浏览网页。** 不需要云端转发，不需要第三方中间件，模型本身就是一个 Agent。

| 能力 | 传统云端模型 | Gemma 4 本地 |
|------|------------|-------------|
| 函数调用 | 需 API 中转 | 原生支持 |
| 工具使用 | 依赖云端编排 | 本地直接执行 |
| 数据隐私 | 数据上云 | 数据不出设备 |
| 延迟 | 网络往返 | 本地毫秒级 |
| 成本 | 按 Token 计费 | 仅硬件成本 |

配合 Ollama、vLLM、llama.cpp 等工具，**一条命令就能在本地把 Gemma 4 跑起来**——而且它还支持多模态输入（文本、图片、视频、音频），上下文窗口最长 256K Token。

中文文档也已同步发布。谷歌这次不是只面向英文开发者——中文生态的接入门槛，被拉到了和英文一样低。

**<mark>当模型能在本地运行并直接调用工具时，「AI Agent」就不再是一个需要云端支撑的概念。它变成了每台设备上的原生能力。</mark>**

![本地 AI Agent 架构：Gemma 4 脱离云端](/assets/images/screenshot-20260403-gemma4-local-agent.jpg)

---

## 三、推理成本归零，冲击的是谁？

Gemma 4 真正的杀伤力不在技术参数——**在于它把推理成本压到了接近于零。**

现有 AI 产品的商业模式大多建立在一个前提上：用户每次调用模型，都要付费。OpenAI 靠 API 调用收费，Anthropic 靠订阅 + API 双轨制，国内厂商也在跟进类似模式。

但 Gemma 4 打破了这个前提：

| 维度 | API 调用模式 | Gemma 4 本地模式 |
|------|------------|----------------|
| 推理成本 | 按 Token 计费 | 仅电费 + 硬件折旧 |
| 边际成本 | 每次调用都有 | 趋近于零 |
| 商业模式 | SaaS 订阅 / 按量付费 | 一次部署，无限使用 |
| 数据风险 | 数据离境 | 数据不出本地 |

市场的反应很直接——**当你有一个免费的、可商用的、能力不差的模型可以本地跑时，你还会每月付 20 美元订阅 ChatGPT 吗？**

这不是说 OpenAI 和 Anthropic 会立刻消失。**但它们的定价权，从今天开始被稀释了。** 开源模型的性能追上闭源模型只是时间问题，而 Apache 2.0 许可意味着——**任何人都可以拿 Gemma 4 去做产品、做服务，不需要向谷歌交一分钱。**

**<mark>谷歌不是在做慈善。它的真正意图是：用免费模型摧毁竞争对手的收入来源，把流量引回自己的云和搜索生态。这是一场用开源打闭源的战争。</mark>**

![推理成本归零：API 收费模式面临的冲击](/assets/images/screenshot-20260403-gemma4-cost-disruption.jpg)

---

## 四、社区实测：V2EX 网友已经跑起来了

发布当天，V2EX 上就有人用「洗车测试」验证 Gemma 4 的推理能力——「你的车需要去 50 米外的洗车店，你应该走路还是开车？」结果如下：

| 模型 | 是否通过 | 备注 |
|------|---------|------|
| Gemma4 31B Dense | ✅ 通过 | 推理清晰，给出走路原因 |
| Gemma4 26B MoE | ✅ 通过 | 表现与 31B 接近 |
| Gemma4 E4B | ❌ 未通过 | 小模型推理不稳定 |
| Qwen3.5 35B | ✅ 通过 | 对照组同样通过 |

硬件门槛方面，社区反馈很真实：

- **12GB 显存跑不动 31B**——有用户尝试后直言「显存只有 12GB，难受」
- **M5 MacBook Air 32GB 跑 Qwen3.5 35B 约 35 token/s**——本地完全可用
- **31B 推荐 FP8 量化**——模型权重约 30GB 显存，性能损失极小
- **多模态能力确认**——有用户测试 Gemma 4 成功识别复杂漫画图片中的中文文字

也有人提出质疑：这类「陷阱题」是否已被纳入训练数据？但多数实测结果表明，**31B 和 26B 版本的综合推理能力确实达到了同级别闭源模型的水准。**

**<mark>社区实测数据说明一件事：Gemma 4 不是 PPT 模型。31B 版本在消费级硬件上可以跑，能力经得起真实场景验证。开源模型追上闭源模型的那一天，比很多人预想的都要快。</mark>**

---

## 写在最后

Gemma 4 发布不到 12 小时，Hugging Face 上的下载量已经爆了。开发者社区的兴奋程度，和去年 DeepSeek 开源时如出一辙——**但这次更猛，因为 Apache 2.0 许可证意味着零商业限制。**

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>AI 行业的成本结构正在被重写。谷歌用 Gemma 4 告诉所有人：推理不应该是一门收费生意。当模型免费、推理本地化、Agent 原生化——旧世界的收费站，就该拆了。</mark>**

---

## 相关阅读

**AI 模型与开源系列**
- [苹果终于松口了：Mac 外接 AMD / NVIDIA 显卡驱动正式放行]({{ site.baseurl }}/mac-egpu-amd-nvidia-driver-thunderbolt-usb4)
- [一个月前我写了 AI 订阅收紧，现在它真的全面崩了]({{ site.baseurl }}/ai-subscription-crackdown-gpu-not-enough)
- [苹果无心插柳：Mac Studio 快断货了，因为 Token 已经是生产力]({{ site.baseurl }}/mac-studio-ai-era-fortress-token-productivity)
