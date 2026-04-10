---
layout: post
title: "学得慢没关系：他用 iPad 裸打代码，然后成了 GPT-5 背后的核心工程师"
date: 2026-04-10
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260410-weng-jiali-openai-cover.jpg
tags: [featured, OpenAI, GPT-5, 翁家翌, 强化学习, RLHF, Infra, 清华, CMU, Zaokit]
slug: openai-weng-jiali-rl-infra-mindset
description: "OpenAI 工程师翁家翌访谈复盘：用正反向筛选构建技能树，用 GitHub Star 替代 GPA，学得慢不是缺陷，是另一种武器。"
faq:
  - question: "翁家翌在 OpenAI 的主要贡献是什么？"
    answer: "他是 Post-Training 团队核心研究工程师，贡献集中在强化学习、post-training 和 infra。从 ChatGPT、GPT-4 到 GPT-5，他都是关键贡献者。"
  - question: "他为什么选择 OpenAI 而不是谷歌？"
    answer: "不想当螺丝钉，要去人才密度最高的地方。"
---

昨天看完了 OpenAI 工程师翁家翌（[@Trinkle23897](https://x.com/trinkle23897)）的[访谈](https://www.youtube.com/watch?v=I0DrcsDf3Os)，两小时下来最大的感受：**求知欲旺盛、学习能力极强。**

他 2022 年加入 OpenAI Post-Training 团队。ChatGPT、GPT-4、GPT-4o、GPT-5——这些关键跃迁背后，都有他的身影。核心贡献三个词：**强化学习、post-training、infra。**

**<mark>一个自认学得比别人慢的人，如何成为全球最强 AI 公司的核心工程师？不是天赋——是方法论。</mark>**

![从清华到 OpenAI：翁家翌的技术跃迁之路](/assets/images/screenshot-20260410-weng-jiali-openai-cover.jpg)

---

## 一、学得慢？那就用方法碾压

他坦言需要比常人花 **2–3 倍时间**理解底层逻辑。但他没把这当缺陷——他把这变成了方法论。

**正反向筛选，只在对的赛道上押注：**

| 正向——持续投入 | 反向——果断放弃 |
|-------------|-------------|
| 奥数：投入产出比高 | 篮球：被按着打 |
| 编程：天然契合 | 跆拳道：实战被揍 |
| 数学/CS | 语文：兴趣不大 |

最让我震撼的细节——**他用 iPad 的 Safari 裸打代码。** 没有编辑器、没有高亮、没有补全。这种方式强迫他在大脑中完整构建程序逻辑，每一行代码先在脑子里跑一遍。

策略简单粗暴：**学得慢就提前学。** 初二学完高中数学，初三开始啃微积分。GPA？最短时间达到够用成绩就行，不浪费生命。

![正反向筛选构建技能树](/assets/images/screenshot-20260410-weng-jiali-skill-tree.jpg)

---

## 二、当所有人在卷 GPA，他在卷 GitHub

清华默认评价体系：GPA 越高越好，PhD 远比 Master 好。翁家翌停下来，**重新定义了自己的计分板。**

他认同导师的标准：**论文、比赛名次、三位数以上的 GitHub Star。** 于是他开源了 [Tianshou](https://github.com/thu-ml/tianshou)（强化学习库）和 [EnvPool](https://github.com/sail-sg/envpool)（超快 RL 环境执行器），收获数千 Star。同时把清华期间所有作业和材料全部开源，打破信息壁垒。

**他的终极目标：最大化自己在 OpenAI Blog 上出现名字的次数。** 他用 RL infra 绑定核心管线，把个人产出 scale 到所有核心产品。从他的 [CV](https://trinkle23897.github.io/cv/) 可以看到，参与项目清单几乎就是一部大模型进化史。

![构建自己的评价体系](/assets/images/screenshot-20260410-weng-jiali-evaluation.jpg)

**<mark>他不在意发了多少论文——更在意有多少人真正记得、使用他做的东西。</mark>**

---

## 三、四个 offer，他选了最不"确定"的

2022 年，ChatGPT 爆发前，他手握 **OpenAI、幻方、谷歌、英伟达** 的 offer。选择逻辑只有一条：**哪里人才密度最高？**

谷歌太大容易当螺丝钉；幻方做 RL infra 是备选；**OpenAI 人才密度最高、scope 最大。** 他不读 PhD 的逻辑也相通——**"教 researcher 做好 engineering，要远比教 engineer 做好 research 难得多。"** 他更看重 Infra，因为 infra 离真实产品最近。

关于开源与闭源的矛盾，他的回答很务实：对 OpenAI 来说生死线是 infra 迭代速度。**现阶段闭源是竞争必需。** 但如果未来创业，他大概率选产品方向——**技术复杂度不重要，精准抓到用户需求才重要。**

![不当螺丝钉：选择人才密度最高的地方](/assets/images/screenshot-20260410-weng-jiali-crossroads.jpg)

---

## 四、宿命论者的生存哲学

播客最后问：**如果 AI 能解决一个世界难题，你想解决什么？** 他说：**"如何预测未来。"**

他认为人活在一个**确定性的马尔可夫过程**里——大脑里想什么、下一个单词说什么，在宇宙大爆炸那刻就已确定。人没有自由意志。

既然是宿命，为什么还要投资未来？

> **"未来的我帮助过去的我完成决策。"** 高三蹦出的"要创造影响力"的想法，是未来的他给过去的自己发送的信号。既然一切确定，那就忘掉这件事，尽情享受。**西西弗斯是幸福的——活着是在确定性的循环里寻找当下的意义。**

![宿命论者的生存哲学](/assets/images/screenshot-20260410-weng-jiali-determinism.jpg)

---

## 写在最后

播客只有两小时，强烈推荐：[完整版](https://www.youtube.com/watch?v=I0DrcsDf3Os)。

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**2026年4月30日前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>你不需要学得最快——找到自己的赛道，构建自己的评价体系，持续输出别人无法替代的价值。这才是从清华到 OpenAI 的底层逻辑。</mark>**

---

## 相关阅读

- [你的直觉正在骗你：AI 算力需求的指数增长]({{ site.baseurl }}/exponential-growth-ai-energy-intuition-fails)
- [AI 重构生产关系：中层消失、定价崩塌]({{ site.baseurl }}/ai-restructure-production-pricing-middle-management-dead)
- [他被拒 40 次一夜白头，她说：200 万不够，我给你 1000 万]({{ site.baseurl }}/xu-xin-vc-queen-from-bank-teller-to-billion)
