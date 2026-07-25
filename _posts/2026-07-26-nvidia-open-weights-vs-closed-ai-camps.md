---
layout: post
title: "黄仁勋人生第一条帖子，直接对着闭源阵营开炮"
date: 2026-07-26
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260726-nvidia-open-weights-vs-closed.webp
tags: [featured, AI, NVIDIA, 黄仁勋, 开放权重, 闭源, Meta, OpenAI, Google, DeepSeek, Zaokit]
slug: nvidia-open-weights-vs-closed-ai-camps
description: >
  黄仁勋在 X 上发了人生第一条帖子，转发 NVIDIA 签署的公开信《Open Weights and American AI Leadership》。
  此前 Hassabis 要建安全标准限制开放模型，黄仁勋直接反过来：开放权重才是正路。两个阵营公开站队。
faq:
  - question: "NVIDIA 这封公开信说了什么？"
    answer: "核心主张：开放权重模型让 AI 更可及、更安全、更有竞争力。闭源模型不天然更安全，它们也会被攻破、被滥用、以外界无法发现的方式失败。把先进 AI 集中在少数闭源提供商手里只会制造更多单点故障。"
  - question: "Hassabis 的信跟这封什么关系？"
    answer: "Hassabis 主张建立全球安全标准机构，所有前沿模型包括 DeepSeek 和 Qwen 都要通过安全评估才能上市。NVIDIA 这封信立场相反：不要搞限制，开放权重本身就是安全路径。"
  - question: "信里替蒸馏说话是什么意思？"
    answer: "蒸馏是用一个模型的输出训练另一个模型的技术，公开信说这是合法的模型改进手段，跟开源软件传统一脉相承，不应该跟偷窃混为一谈。这被广泛解读为替 DeepSeek 说话。"
  - question: "哪些公司签了，哪些没签？"
    answer: "签了的包括 NVIDIA、Meta、Microsoft、a16z、Hugging Face、Mistral、Y Combinator 等 25 家。没签的有 OpenAI、Anthropic、Google。"
---

黄仁勋在 X 上发了人生中第一条帖子。

不是产品发布，不是财报晒单，是转发了一封 NVIDIA 签署的公开信——《Open Weights and American AI Leadership》。几个小时浏览量冲到 1742 万。

一个在公众视野里只穿皮衣、不玩社交媒体的人，选择用这封信作为自己在 X 上的第一次发声。这件事本身就值得多看一眼。

![黄仁勋人生第一条帖子，直接对着闭源阵营开炮](/assets/images/cover-20260726-nvidia-open-weights-vs-closed.webp)
<!-- baoyu-skill prompt: 2.35:1电影感横版封面，深黑到深蓝渐变背景，冷静厚重的科技质感。画面左侧黄仁勋标志性皮衣人物剪影，右侧一封发光公开信文档图标。中央粗体大字中文「开放 VS 闭源：公开站队」。顶部副标中文「黄仁勋人生第一条X帖子」。底部中文「NVIDIA · Meta · Microsoft VS OpenAI · Anthropic · Google」。中文清晰可读。 --ar 2.35:1 -->

## 一、两封信，正面对撞

要看懂这封信的分量，先看它在回应谁。

此前不久，Google DeepMind CEO Demis Hassabis 发了一封公开信，主张建立一个全球性的安全标准机构。核心意思：所有前沿 AI 模型——包括中国的 DeepSeek 和阿里的 Qwen——都必须通过统一的安全评估，才能上市部署。

翻译成大白话：先过我定的考试，才能上路。

黄仁勋这封信，几乎是逐点反驳：

| Hassabis 的立场 | NVIDIA 公开信的立场 |
|---|---|
| 建全球安全标准机构，统一评估 | 不要搞过早的限制，会扼杀竞争 |
| 闭源更可控，安全更有保障 | 闭源不天然更安全，开放才是安全路径 |
| 所有前沿模型必须通过评估 | 开放权重让更多人参与审查和改进 |
| 暗示蒸馏是"窃取" | 蒸馏是合法技术，不应跟偷窃混为一谈 |

两封信不是学术讨论。是两个阵营在抢话筒，争的是 AI 未来的游戏规则由谁来定。

![两封信正面对撞](/assets/images/illust-20260726-two-letters-clash.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅对比信息图，深色背景，冷静科技质感。左栏冷红标中文「Hassabis·闭源阵营」副标中文「建标准·统一评估·限制开放」；右栏冷青标中文「黄仁勋·开放阵营」副标中文「开放权重·不要限制·透明更安全」。中央一道闪电裂痕标中文「正面对撞」。顶部标题中文「两封公开信」。底部中文「争的是游戏规则由谁来定」。中文清晰可读。 --ar 2.35:1 -->

## 二、闭源不等于安全，这句话才是重点

公开信里有一段话，我觉得比整篇文章的政治站位都重要：

> **仅仅依赖闭源模型并不天然更安全：它们也会被攻破、被滥用、以外界无法发现的方式失败。把先进 AI 集中在少数闭源模型手里，只会制造更多单点故障。**

这句话戳的不是技术问题，是安全叙事里最大的一个假设——「关起门来就安全」。

闭源模型确实更难被直接复制权重。但安全不只是防复制：

- **闭源模型被攻破的案例不少。** Prompt 注入、越狱攻击、API 滥用，闭源没有因为「不公开」而少挨打。
- **出了问题外界看不见。** 闭源模型的偏见、幻觉、安全漏洞，如果提供商不主动披露，用户根本无从发现。
- **单点故障风险集中。** 全世界都依赖三五个闭源 API，任何一个出问题，波及面是系统性的。

公开信的逻辑是：**开放权重让更多人能检查模型行为、发现漏洞、开发防护，就像开源软件证明的那样——透明比黑箱更安全。**

这个论点是不是绝对正确？不一定。但它至少把「闭源 = 安全」这个默认假设打了一个问号。而这个问号，一直没人敢公开打。

![闭源不等于安全](/assets/images/illust-20260726-closed-not-safe.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景，冷静科技质感。中央一个巨大的锁图标，锁上出现裂纹，裂纹处标中文「被攻破」「被滥用」「无法发现的失败」。锁下方标中文「闭源≠安全」。右侧一个透明的开放模型图标发光，标中文「开放→更多人检查→更多人修复」。顶部标题中文「安全叙事最大的假设」。底部中文「透明比黑箱更安全」。中文清晰可读。 --ar 2.35:1 -->

## 三、替蒸馏说公道话——在替谁说话？

信里还有一段专门替「蒸馏」正名：

> 蒸馏，即用一个模型的输出来训练或改进另一个模型，是广泛使用的模型改进技术。它延续了从开源软件运动以来的学习、借鉴、改进传统，不应与非法窃取混为一谈。

这段话的潜台词，懂的人都懂。

DeepSeek 被指控通过蒸馏 OpenAI 的模型来提升自己的能力。OpenAI 公开表态「这是偷窃」，并推动政策层面对蒸馏行为的限制。

NVIDIA 这封信直接说：蒸馏是合法技术手段。真正有问题的是非法提取闭源模型的价值——但这应该用针对性的法律和商业框架解决，而不是一刀切禁止蒸馏本身。

再看签名名单，就更明白了。

![替蒸馏说句公道话](/assets/images/illust-20260726-distillation-defense.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景，冷静科技质感。中央一个蒸馏瓶图标发光，瓶身标中文「蒸馏」，左侧箭头标中文「大模型输出」，右侧箭头标中文「小模型改进」。瓶下方标中文「合法技术手段」。右下角一个小天平图标标中文「不等于偷窃」。顶部标题中文「替蒸馏说句公道话」。底部中文「开源传统·学习借鉴改进」。中文清晰可读。 --ar 2.35:1 -->

## 四、签名名单才是真正的信号

签了的：

**NVIDIA、Meta、Microsoft、a16z（Andreessen Horowitz）、Hugging Face、Mistral、Y Combinator、IBM、Dell、Mozilla、Palantir、Perplexity、Replit、The Linux Foundation、CrowdStrike、ServiceNow、Box** 等 25 家。

没签的：

**OpenAI、Anthropic、Google。**

三家没签的，恰好是当前最大的三家闭源前沿模型提供商。

| 阵营 | 代表 | 核心利益 |
|---|---|---|
| **开放阵营** | NVIDIA、Meta、Microsoft、a16z | 卖算力、卖云、卖生态——开放模型越多，需求越大 |
| **闭源阵营** | OpenAI、Anthropic、Google | 卖 API、卖订阅——护城河建在模型独占上 |

这不是「开放好还是闭源好」的哲学辩论。这是商业利益驱动的阵营划分。

NVIDIA 卖 GPU，开放模型越多、跑模型的人越多，GPU 需求越大。Meta 推 Llama 开源，是要用开放生态对冲 OpenAI 的先发优势。a16z 投了一堆开源 AI 创业公司。

反过来，OpenAI 和 Anthropic 的收入几乎全靠 API 和订阅。模型权重一旦开放，它们的核心壁垒就被拆了。Google 卖云卖广告，Gemini 的闭源是保住 AI 搜索的关键筹码。

这不是对错之争，是利益之争。

![两个阵营公开站队](/assets/images/illust-20260726-two-camps-lineup.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅对比信息图，深色背景，冷静科技质感。左栏冷青高亮标中文「开放阵营」，下方Logo排列标中文「NVIDIA」「Meta」「Microsoft」「a16z」「Hugging Face」「Mistral」「Y Combinator」，底部中文「卖算力·卖云·卖生态」；右栏冷红标中文「闭源阵营」，下方标中文「OpenAI」「Anthropic」「Google」，底部中文「卖API·卖订阅·护城河在模型独占」。中央大字中文「利益决定立场」。顶部标题中文「谁签了·谁没签」。中文清晰可读。 --ar 2.35:1 -->

## 五、黄仁勋选这封信发第一条帖子，说明什么

黄仁勋不是随便发帖的人。他连社交媒体账号都几乎不用。

人生第一条 X 帖子，不发产品、不发财报、不发鸡汤，选了一封关于开放权重的政策公开信。这个选择本身就是信号：

**AI 的战场正在从技术竞赛转向规则制定。**

模型能力的差距在缩小——DeepSeek、Llama、Mistral 已经证明开放模型可以接近甚至某些场景超过闭源前沿。当技术差距不再是绝对壁垒，谁来定规则、谁的模型需要"通过评估"才能上市，才是真正的制高点。

Hassabis 推的安全标准机构，表面是「让所有人都安全」，潜台词是：评估标准由我们来定，通过门槛由我们来设。如果标准足够高、流程足够长，开放模型和后来者天然处于劣势。

NVIDIA 这封信反过来说：别搞准入限制，让市场和社区来检验。

> **争的不是开放好还是闭源好。争的是下一个十年，AI 的规则由谁来写。**

## 写在最后

压成五句：

1. **黄仁勋第一条帖子**——转发 NVIDIA 签署的开放权重公开信，几小时 1742 万浏览
2. **正面对撞 Hassabis**——一个要建标准限制，一个说开放才是正路
3. **闭源不等于安全**——也会被攻破、被滥用、以外界无法发现的方式失败
4. **替蒸馏正名**——合法技术手段，不是偷窃，懂的都懂
5. **签名名单是真信号**——NVIDIA/Meta/Microsoft 签了，OpenAI/Anthropic/Google 没签

**这不是技术辩论，是利益之争。AI 的下一个十年，谁来定规则，比谁的模型跑分高，重要一百倍。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，核心是把 AI 能力送进真实交付，不站队、不依赖单一闭源 API。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

延伸：[AI 被大模型绑架了](/ai-is-not-just-llm-full-landscape) · [语音不是聊天附件，是 Agent 调度台](/chatgpt-desktop-voice-gpt-live-appshots) · [预训练是别人的工厂](/llm-pretrain-posttrain-skill-workflow-agent)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。开放还是闭源，别看嘴上喊的，看谁签了、谁没签。利益决定立场，永远比口号诚实。*
