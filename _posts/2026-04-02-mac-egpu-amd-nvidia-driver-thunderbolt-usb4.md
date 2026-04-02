---
layout: post
title: "苹果终于松口了：Mac 外接 AMD / NVIDIA 显卡驱动正式放行，一根线就够"
date: 2026-04-02
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260402-mac-egpu-amd-nvidia-cover.avif
tags: [featured, Mac, eGPU, AMD, NVIDIA, Thunderbolt, USB4, Apple Silicon, AI算力, TinyCorp, tinygrad]
slug: mac-egpu-amd-nvidia-driver-thunderbolt-usb4
description: "如果你有一台 Apple Silicon Mac 和一块闲置的 AMD/NVIDIA 显卡，今天就是你等了五年的日子。通过 Thunderbolt/USB4 接口加社区驱动，Mac 终于能外接显卡跑 AI 算力。一根线、一条命令，算力翻倍。"
faq:
  - question: "Apple Silicon Mac 现在能用外接显卡了吗？"
    answer: "可以了。通过 TinyCorp 开发的用户态驱动，Mac 可以经 Thunderbolt/USB4 接口连接 AMD RDNA 或 NVIDIA RTX 显卡，用于 AI 计算。但目前不支持图形加速和外接显示器。"
  - question: "支持哪些显卡型号？"
    answer: "NVIDIA 支持 RTX 30/40/50 系列，AMD 支持 RDNA 2/3/4 架构。需要 Thunderbolt 4 或 USB4 接口，配合 PCIe 转接适配器。"
---

如果你手边有一块闲置的 AMD 或 NVIDIA 显卡，再加一台有 Thunderbolt 或 USB4 接口的 Mac——**今天，你等了五年的日子来了。**

社区终于把 Mac 外接显卡的驱动做通了。**不是虚拟机，不是 Bootcamp，是实打实在 macOS 上用一根 Thunderbolt 线接上显卡，跑 AI 推理。**

**<mark>苹果没有官宣，但事实上放行了——用户态驱动不触碰内核，不需要关闭 SIP，一根线、一条命令，外接显卡就能工作。这是技术倒逼生态开放的经典案例。</mark>**

![Mac 外接 AMD/NVIDIA 显卡：五年等待终于成真](/assets/images/screenshot-20260402-mac-egpu-amd-nvidia-cover.avif)

---

## 一、到底发生了什么？

TinyCorp 团队（tinygrad 框架开发者）完成了一套面向 Apple Silicon 的**用户态 GPU 驱动**。核心突破：

| 维度 | 内容 |
|------|------|
| 连接方式 | Thunderbolt 4 / USB4（原生 PCIe 通道） |
| 支持显卡 | NVIDIA RTX 30/40/50、AMD RDNA 2/3/4 |
| 驱动形式 | 用户态驱动，无需关闭 SIP |
| 使用场景 | AI/ML 计算（tinygrad 框架） |
| 限制 | 不支持图形加速、游戏、外接显示器 |

简单说——**它让你的 Mac 多了一块专用 AI 算力 GPU。** 不是替代内置 GPU，是给它加一块"外挂引擎"。

![Mac 外接 GPU 驱动架构：用户态绕过内核](/assets/images/screenshot-20260402-mac-egpu-driver-architecture.avif)

---

## 二、怎么接？五分钟搞定

硬件清单：

| 硬件 | 推荐方案 |
|------|---------|
| Mac | 任何 M1/M2/M3/M4/M5 芯片 Mac |
| 显卡 | NVIDIA RTX 4090 / AMD RX 7900 XT |
| 转接器 | ADT-UT3G（TB 转 PCIe x16） |
| 供电 | 显卡独立电源（ATX 或 eGPU 坞站） |

软件三步走：

```bash
pip install tinygrad
python -c "from tinygrad import Device; print(Device.DEFAULT)"
python -c "from tinygrad import Tensor; print(Tensor.ones(4,4).realize())"
```

**接线→安装→运行，五分钟搞定。** 连配置文件都不用改。

**<mark>五年前想在 Mac 上用外接显卡，只能 Bootcamp 装 Windows。今天，一条 pip install 就够了。时代变了。</mark>**

![五分钟安装指南：从接线到跑通全流程](/assets/images/screenshot-20260402-mac-egpu-setup-guide.avif)

---

## 三、接上之后能干什么？

Mac 内存够大，但推理速度受内置 GPU 限制。外接 RTX 4090 之后：

| 场景 | 仅 Apple Silicon | + 外接 RTX 4090 |
|------|-----------------|------------------|
| LLM 推理（7B） | 35 token/s | 120+ token/s |
| 图像生成（SDXL） | 45 秒/张 | 8 秒/张 |
| 模型微调 | 不实用 | 可用 |

**核心价值：Mac 负责内存和编排，外接 GPU 负责暴力计算。** 两者各取所长。

我的方案是 Mac Studio M3 Ultra 256GB + 外接 RTX 4090。Mac 把千亿参数模型加载到统一内存，推理交给 4090。**内存归苹果，算力归英伟达——这才是最优解。**

**<mark>Mac 的内存优势 + NVIDIA 的算力优势，终于不再互斥。一台设备同时拥有两个生态的顶级能力，半年前不可想象。</mark>**

![算力翻倍：Mac + 外接 GPU 联合架构的威力](/assets/images/screenshot-20260402-mac-egpu-performance-boost.avif)

---

## 四、为什么现在才成？

苹果 2020 年转向 Apple Silicon 时，**直接砍掉了 eGPU 支持**。态度很明确：统一内存不需要外接 GPU。

但 AI 时代打了苹果的脸：

| 苹果的预判 | 现实 |
|-----------|------|
| 内置 GPU 够用 | AI 推理需要海量并行算力 |
| 统一内存解决一切 | 内存够大但计算不够快 |
| 用户不需要 eGPU | 开发者用脚投票 |

TinyCorp 的做法很聪明——**在用户态实现 GPU 驱动，绕过内核。** 不碰 macOS 安全机制，苹果没有理由也没有动力封杀。

**<mark>苹果不是"批准"了驱动——而是社区找到了苹果无法拒绝的路。用户态不触碰内核，封不了，也不想封。技术倒逼生态开放，这才是真正的破局。</mark>**

---

## 写在最后

Mac 外接显卡这件事，等了整整五年。从 Intel 时代的 eGPU 被砍，到 Apple Silicon 的完全封锁，再到今天社区驱动突破——**Mac 用户终于不用在「生态」和「算力」之间二选一了。**

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>AI 时代的算力格局正在被重写。Mac 不再是孤岛——一根 Thunderbolt 线，就能连接整个 GPU 生态。苹果没说行，但也没说不行。这就够了。</mark>**

---

## 相关阅读

**Mac 与 AI 算力系列**
- [苹果无心插柳：Mac Studio 快断货了，因为 Token 已经是生产力]({{ site.baseurl }}/mac-studio-ai-era-fortress-token-productivity)
- [一个月前我写了 AI 订阅收紧，现在它真的全面崩了]({{ site.baseurl }}/ai-subscription-crackdown-gpu-not-enough)
- [月投 650 刀订阅 AI Agent：当 Token 不再有限制，生产力到底能有多大？]({{ site.baseurl }}/agent-arms-race-650-dollars-per-month)
