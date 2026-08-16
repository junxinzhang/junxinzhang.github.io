---
layout: post
title: "苹果和阿里联合训练：Siri 核心层，最后时刻不外包"
date: 2026-08-16
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260816-apple-alibaba-siri.webp
tags: [featured, AI, Apple, Alibaba, Qwen, Siri, Apple Intelligence, 中国区, Zaokit]
slug: apple-alibaba-siri-core-not-outsourced
description: >
  路透 8 月 14 日独家：苹果为中国区自己训了一层大模型，阿里提供技术支持。
  我的读法：最后时刻，Siri 最核心那一层不长期外包。云可以租，芯自己留。
faq:
  - question: "苹果是不是在中国用通义换皮？"
    answer: "不是。路透写的是苹果自己训了一层，阿里提供支持。通义进云端，百度补搜索。三层栈，不是一张皮。"
  - question: "「最后时刻不外包」是苹果说的吗？"
    answer: "不是官方原话。路透的事实是原先靠第三方，后来苹果自己下场训。核心层不长期租，是我的读法。"
  - question: "中国区 Apple Intelligence 上线了吗？"
    answer: "还没正式开。7 月网信办登记了苹果上海的生成式服务。8 月 8 日支持页短暂放出 Mac 接千问，第二天撤了。"
  - question: "这跟昨天测的 Qwen3.8 27B 有什么关系？"
    answer: "昨天只证明 27B 在 M5 Pro 上能跑，24G 是入场券。今天不复测。端侧能跑，才敢把核心层留在自己手里。"
---

路透 8 月 14 日独家：苹果为中国区自己训了一层大模型，阿里提供技术支持。三位知情人士，两边都没评论。

很多人读成「通义进 iPhone」。那是 7 月的旧闻。

> **联合训练是真的。我的读法：最后时刻，苹果不让 Siri 最核心那一层长期外包。云可以租，芯自己留。**

![苹果和阿里联合训练：Siri 核心层，最后时刻不外包](/assets/images/cover-20260816-apple-alibaba-siri.webp)

## 一、路透爆的不是通义进苹果

别把两件事焊成一件。

| 时间 | 公开事实 | 说明 |
|------|----------|------|
| 2025 年 2 月 | 蔡崇信说苹果中国区选了阿里 | 当时听起来像通义给 iPhone 供电 |
| 2026 年 7 月 | 网信办登记苹果上海；通义进 Apple Intelligence，百度补搜索 | 监管过了，方案还是第三方 |
| 2026 年 8 月 8–9 日 | 支持页放出 Mac 接千问，第二天撤掉 | 云端接法写进说明书，功能没开 |
| 2026 年 8 月 14 日 | 路透：苹果自己训，阿里提供支持 | 靠第三方的策略，被改了一刀 |

主语是苹果自己的模型过了门，不是通义。参数、上线日、哪类 Siri 请求走端侧，都没公布，我不编。

## 二、为什么说最后时刻

「最后时刻」不是新闻稿里的词，是我读时间线的判断。

2 月定成外包，7 月方案仍是通义进机。8 月 14 日多出一层苹果自己的。中间几周，说明书都写到登录千问了。

路透说这是对「靠第三方供电」的偏离。我读成一句：云端语言可以继续用通义，Siri 最核心那一层不愿写成长期外包合同。

租得越久，Siri 越像别人的助手套了个苹果壳。华为已经把这个缺口撕开了。中国区卖了快两年 Apple Intelligence，功能没落地。再把核心层也租出去，入口还在，脑子是租的。

所以它把合作往外推一层：阿里帮训，通义仍进云端，核心层自己留。

![核心层不长期外包](/assets/images/illust-20260816-core-not-outsourced.webp)

## 三、中国区是三层栈，不是一张皮

路由没公布。下表只写已经公开的。

| 层 | 谁 | 已经公开的 |
|----|----|------------|
| 端侧 / 自有模型 | 苹果自己训的 | 路透 8 月 14 日：阿里提供支持，更大控制权 |
| 云端语言 | 通义 | 7 月：进中国区 iPhone / iPad / Mac / Vision Pro |
| 搜索 / 视觉 | 百度 | 7 月路透：同时接入 |

被撤掉的支持页还写过：macOS 26.6，千问账号或通过 Apple 登录；阿里不得用这些材料训练自己的模型。说明书不是发版。

**通义进 iPhone，不等于通义成为 Siri。** 云可以租，搜索可以租，核心层不放手。

![中国区是三层栈](/assets/images/illust-20260816-three-layer-stack.webp)

## 四、端侧能跑，才敢自己留

[昨天那篇](/qwen38-27b-m5pro-local) 的数字不在这里重跑。27B 在 M5 Pro 上能跑，24G 是入场券。

今天只借一句：端侧真能跑，才敢把核心层留在自己手里。如果这个量级只能躺在云上，所谓自己的模型就是换了签名的云合同。

阿里是联合训练、提供支持，不是把模型卖断。苹果要收得回，阿里要云端入口。各拿一层，谁都没交底牌。

[14 号](/grok46-gemini37-flash-model-knockout) 说中间地带在消失。苹果这步是反面：巨头可以租云，不能把判断层也租掉。

![端侧能跑，才敢自己留](/assets/images/illust-20260816-ondevice-sovereignty.webp)

## 五、对企业：最核心那一层，不能长期租

别读成苹果新闻。这是一张合同分类。

| 可以租 | 不能长期租 |
|--------|------------|
| 算力、通用模型、搜索 | 判断层：产品拿什么做决定 |
| 润色、闲聊、外挂问答 | 身份、权限、私有数据 |
| 地板价 token | 入口后面那一层「这是不是我的产品」 |

通义可以进机，百度可以补搜索，Siri 核心层不写成长期外包。租云可以，租完把用户交互再喂回去，不行。

我做 [Zaokit](https://zaokit.ai) 也是这句：模型谁便宜接谁，价值不能沉淀在调用上。调用是原材料。能留下的是判断层。

过不了这张表，就是在给别人的模型打工。过得了，云越便宜对你越有利。

![对企业也一样](/assets/images/illust-20260816-dont-rent-core.webp)

## 写在最后

压成五句：

1. **路透爆的是苹果自己训**——不是通义进 iPhone 的旧闻
2. **最后时刻不外包，是我的读法**——说明书都写到登录千问了，核心层仍自己留
3. **中国区是三层栈**——端侧苹果、云端通义、搜索百度
4. **端侧能跑，才敢自己留**——昨天是门票，今天是主权
5. **对企业也一样**——云可以租，判断层不能长期外包

土话一句：

**厨房可以外包，配方不能租。**

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

延伸：[Qwen3.8 27B 在 M5 Pro 64G 上：能跑不是新闻，MLX 快了四成才是](/qwen38-27b-m5pro-local) · [Grok 4.6 和 Gemini 3.7 Flash：模型竞争进入淘汰赛](/grok46-gemini37-flash-model-knockout) · [Grok Bot 上线：这场战争才刚刚开始](/grok-bot-cloud-pc-agent-war)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。云可以租——最核心那一层，别写成长期合同。*
