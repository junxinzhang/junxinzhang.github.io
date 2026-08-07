---
layout: post
title: "AI应用最尴尬的账单，可能正在被翻过来"
date: 2026-08-02
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260804-ai-app-cost-curve-flip.webp
tags: [featured, AI, Gavin Baker, Atreides, Legora, Harvey, 开源模型, 模型路由, 后训练, 垂直AI, Fireworks, Zaokit]
slug: gavin-baker-ai-app-cost-curve-flip
description: >
  押中过英伟达、特斯拉和 SpaceX 的 Gavin Baker 判断：模型路由、开源模型、专业化后训练同时成熟，
  AI 应用公司不必永远给大模型交租。客户增长，有机会从「账单增长」变成「模型变强、成本下降」。
faq:
  - question: "Gavin Baker 说的三件成熟的事是什么？"
    answer: "模型路由（Routers）、开源模型、基于真实业务数据的专业化后训练（post-training）。三者组合，让垂直 AI 应用能在更低成本下逼近甚至局部超过纯前沿模型调用。"
  - question: "为什么说 AI 应用的成本曲线在翻转？"
    answer: "旧模式是客户多用一次就多交一笔 API 费，增长等于账单增长；新模式是高频任务走专用开源/后训练模型，难任务才调前沿模型，用得越多、数据与评测越厚，模型可继续变强、单位成本可继续降。"
  - question: "Harvey 和 Fireworks 的实验说明了什么？"
    answer: "开源 worker + 稀疏调用前沿 advisor + 后训练，在法律 Agent 基准上可做到质量不低于甚至优于端到端前沿模型，而成本显著更低。前沿模型变成可调用工具，而不是产品唯一底座。"
  - question: "Legora 的增长和护城河有什么关系？"
    answer: "ARR 同比超 10 倍、7 月净新增 ARR 比此前纪录高 90%+ 说明客户在把产品建进工作流。真正护城河是客户、数据、评测、工作流与专用模型叠在一起，而不只是套一层 prompt。"
---

过去做 AI 应用，有个很土、却很致命的问题：

**产品卖得越好，模型账单越贵。**

客户多用一次，你就多给 OpenAI、Anthropic 交一笔钱。更麻烦的是，底层模型每升级一次，你辛苦做出来的功能，还有可能被直接吃掉。

圈子里因此形成一种半共识：**AI 应用没有护城河，只是给大模型厂商打工。**

但最近，一位押中过英伟达、特斯拉和 SpaceX 的科技投资人，给出了更激进的判断：**垂直聚焦的 AI 原生公司，可能要迎来一轮集体加速。**

> **不是「套壳突然变香了」，而是成本曲线、数据闭环和模型归属，开始同时改写。**

![AI应用最尴尬的账单，可能正在被翻过来](/assets/images/cover-20260804-ai-app-cost-curve-flip.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平封面，奶油到天蓝渐变，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。左侧漫画账单卡上扬曲线标中文「旧：增长=账单涨」；右侧友好机器人与下降成本曲线标中文「新：用得越多越便宜」。中央粗体中文「成本曲线在翻转」。顶部「Gavin Baker · 垂直AI加速」。底部「路由·开源·后训练，三件事同时成熟」。中文清晰可读。 --ar 2.35:1 -->

## 一、谁在说：Gavin Baker 不是口号型投资人

**Gavin Baker** 是美国科技投资圈里偏「硬」的那一类。他在富达工作约 18 年，管理过规模约 **170 亿美元** 的科技基金（Fidelity OTC 相关时期常被这样描述），后来创办 **Atreides Management**，也是英伟达、特斯拉和 SpaceX 的早期重要投资者之一。

他最近公开判断的大意是：接下来会看到**一大批垂直聚焦的 AI 原生公司加速**。驱动不是口号，而是三件同时成熟的工程现实——

1. **模型路由（Routers）**  
2. **开源模型**  
3. **专业化后训练（post-training）**

他点名了像 [Fireworks AI](https://fireworks.ai/) 这类把训推与后训练打通的平台，也点到法律 AI 等垂直场景已经在跑通这条路。原文语境可对照其 X 账号 [@GavinSBaker](https://x.com/GavinSBaker) 近期发言。

翻译成大白话：

| 以前 | 现在开始成立 |
|------|--------------|
| 一个最强模型通吃所有任务 | 简单任务走便宜专用模型 |
| 应用层几乎不拥有模型 | 用自己的业务数据后训练开源基座 |
| 增长 = API 账单线性上涨 | 增长 = 数据与评测变厚，单位成本可压 |

**游戏规则变了：AI 应用公司不必永远只给大模型厂商交租。**

![旧账单逻辑 vs 新成本逻辑](/assets/images/illust-20260804-old-vs-new-cost.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画对比图，奶油/天蓝底，干净描边扁平色。左卡中文「旧模式」三条；右卡中文「新模式」三条；中央箭头中文「成本曲线翻转」；顶标「卖得越好，账单越贵？」；底标「规则正在改写」。禁止深色赛博风。中文清晰可读。 --ar 2.35:1 -->

## 二、三件事同时成熟：路由、开源、后训练

别被术语吓住。拆开看，都是很土的工程选择。

### 1）模型路由：别让最贵的模型干最简单的活

不是「所有请求都打 Claude Opus / GPT 最强档」，而是按难度、延迟、合规、成本，把任务分给不同模型：

- 抽取、分类、格式化、高频改写 → 便宜专用模型  
- 高风险推理、复杂综合、客户可见关键交付 → 再 escalate 到前沿模型  

路由做好了，**质量可以接近「全上最强」**，账单却不是按最强单价线性放大。

### 2）开源模型：终于能扛一部分常规任务

过去开源模型「能聊，不敢上生产」。现在一批开源权重在常规任务上已经够用，关键是：

**你能私有部署、能控数据、能后训练，而不是永远只做 prompt 租户。**

我前几天写 [Kimi K3 开源与私有化成本](/kimi-k3-open-weights-private-deploy-cost) 时强调过另一面：前沿权重开源 ≠ 普通公司能私有化最强模型。这里说的不是「人人自建 64 卡超节点」，而是——

**垂直应用可以用「够强且可训」的开源基座，吃掉自己业务里那一大截高频 token。**

### 3）后训练：把「通用聪明」拧成「懂你的行当」

真正拉开差距的，是用**真实业务轨迹**做 SFT / RFT 一类后训练：合同怎么审、条款怎么抽、报告怎么过 rubric、失败案例怎么回灌。

结果不是「又一个通用助手」，而是：

**在你的评测集、你的工作流、你的错误代价上，专用模型开始比通用大模型更省、更稳、更可控。**

![路由·开源·后训练三件套](/assets/images/illust-20260804-three-pillars.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画信息图，三卡横排中文「模型路由」「开源基座」「专业化后训练」及副标，下方箭头「垂直AI原生公司加速」，顶「三件事同时成熟」，底「质量接近前沿，成本砍掉一大截」。奶油底、薄荷绿/天蓝/蜜桃平涂，清线描边。中文清晰可读。 --ar 2.35:1 -->

## 三、工程侧证据：Harvey × Fireworks 把账算清楚了

判断再漂亮，也要有可核对的实验。

法律 AI 公司 **Harvey** 与 **Fireworks** 公开了一组很硬的对照（见 [Fireworks 博客：Open-Source Agents, Frontier Advisors](https://fireworks.ai/blog/open-source-agents-frontier-advisors)）：在 Harvey 的 Legal Agent Benchmark（LAB）切片上——

| 配置 | 大致结果 | 成本量级（100 tasks 切片） |
|------|----------|----------------------------|
| 端到端 Claude Opus 4.7 | all-pass **14/100**，mean 约 0.91 | 约 **$954** |
| 开源 worker（如 GLM）+ 稀疏调用 Opus 作 advisor | all-pass **18/100** | 约 **$368**（约 Opus 的 **39%**） |
| 开源基座 + SFT / RFT 后训练 | all-pass / mean 明显抬升，推理成本接近基座档 | 远低于「全程前沿」 |

两层意思叠在一起：

1. **混合 harness**：开源模型当工人，前沿模型当顾问，平均每个任务只稀疏调用顾问（公开实验里约 0.83 次/任务量级）  
2. **后训练**：用通过 rubric 的轨迹做 SFT，再用评测标准做 RFT，把开源模型往法律任务上拧  

文中那句结构很干净，值得记：

**open weights at the core, frontier intelligence called in only where it changes the answer.**  
（开源权重在核心，前沿智能只在能改变答案的地方被叫进来。）

这几乎就是 Baker 判断的工程版说明书。

![开源工人 + 前沿顾问](/assets/images/illust-20260804-hybrid-harness.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画流程图。左「法律任务」→「路由」分路「开源worker·高频」与「前沿advisor·稀疏」汇合「可验收交付」；角标「质量≥纯Opus · 成本约39%」；顶「前沿模型变成可调用工具」；底「不是永远绑在一个最贵API上」。奶油底、清线扁平、可爱图标。中文清晰可读。 --ar 2.35:1 -->

## 四、商业侧证据：Legora 的增速在说工作流，不只是 demo

如果说 Harvey × Fireworks 证明**技术路径**，**Legora**（法律 AI，前身常被称作 Leya 一脉）更像在证明**客户愿不愿意把预算和工作流迁过来**。

可核对的公开节点大致是：

- 约 **18 个月** 内 ARR 跨过 **1 亿美元** 量级（公司 [新闻稿](https://legora.com/newsroom/legal-teams-adoption-of-ai-propels-legora-past-100-million-in-annual-recurring-revenue) 口径）  
- Series D 及后续 extension 后，公开报道估值进入约 **55–56 亿美元** 区间，投资方包括 Accel，后续还有 Atlassian、NVIDIA NVentures 等（[Series D extension 新闻](https://legora.com/newsroom/legora-extends-series-d-with-additional-50-million-welcomes-atlassian-and-nventures-as-investors)）  
- 团队公开披露：**ARR 同比增长超过 10 倍**；**7 月净新增 ARR 比此前纪录高 90%+**  

这些数字要打折听——垂直 AI 赛道披露节奏快、口径各异——但方向一致：

**不是「又一个法律聊天框」，而是进入律所与公司法务的日常工作流：审查、表格化抽取、Word 内协作、多步 agent 流程。**

Baker 点名这类公司时，核心不是「法律赛道永远正确」，而是：

> 当一家公司同时掌握**客户、数据、评测、工作流和专用模型**，它就不再只是套壳应用。它开始拥有自己的模型能力。

Cognition 一类 coding agent 公司身上，也能看到同构趋势：产品深度嵌入专业工作流，模型侧走向「自有/可训 + 路由 + 尖峰调用前沿」。路径细节各家不同，结构越来越像。

![护城河刚开始形成](/assets/images/illust-20260804-moat-forming.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画信息图。五齿轮中文「客户」「业务数据」「评测基准」「工作流」「专用模型」，外环「护城河」；右增长「ARR同比10x+」「净新增纪录+90%」；顶「过去担心没护城河」；底「真正的护城河可能才刚开始形成」。奶油底、薄荷绿/蜜桃、清线扁平。中文清晰可读。 --ar 2.35:1 -->

## 五、翻转点：客户越多，不再只等于账单越大

把逻辑压成一条链：

1. 高频任务被专用模型吃掉 → **边际 token 成本下降**  
2. 客户用得越多 → **轨迹、纠错、评测越厚**  
3. 后训练继续跑 → **专用模型更强，路由更敢把流量留在便宜侧**  
4. 前沿模型仍会用，但更像「尖峰保险」而不是「全量底座」  

旧世界：

**客户增长 → API 账单增长 → 毛利被模型厂抽走。**

新世界（开始成立的那部分）：

**客户增长 → 数据飞轮 → 模型变强 → 单位成本可继续下降。**

这不是说 OpenAI / Anthropic 没生意了。恰恰相反：最难的那截推理、最强的那截智能，仍会很贵、很稀缺。变的是——

**应用公司第一次有机会，把「租户身份」改成「部分模型所有权 + 工作流所有权」。**

过去大家担心 AI 应用没有护城河。  
现在看，**真正的护城河可能才刚刚开始形成**——不在一句 prompt，而在数据闭环、评测体系、行业工作流，以及你敢不敢把路由和后训练做成产品内核。

## 写在最后

压成五句：

1. **旧尴尬仍真实**——卖得越好、账单越贵，功能还可能被模型升级吃掉  
2. **Baker 的判断很硬**——路由 + 开源 + 专业化后训练，在推垂直 AI 原生公司加速  
3. **Harvey × Fireworks 算清了工程账**——开源工人 + 稀疏前沿顾问，可更好且更便宜  
4. **Legora 在算商业账**——ARR 同比 10x+、7 月净新增破纪录，说明工作流迁移是真的  
5. **护城河换定义了**——客户 / 数据 / 评测 / 工作流 / 专用模型叠在一起，才开始像壁垒  

土话一句：

**以前 AI 应用怕增长；现在增长，有机会变成你的模型资产。**

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，做的也是同一方向：把可用能力送进真实交付，而不是永远只做最贵 API 的二道贩子。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[Kimi K3 开源了，私有化却和普通公司无关了](/kimi-k3-open-weights-private-deploy-cost) · [黄仁勋说五年内很难泡沫](/jensen-huang-axios-chip-bubble-discount) · [LLM 预训练后训练与 Agent](/llm-pretrain-posttrain-skill-workflow-agent)

公开参考：[Gavin Baker on X](https://x.com/GavinSBaker) · [Fireworks × Harvey 实验](https://fireworks.ai/blog/open-source-agents-frontier-advisors) · [Legora 过 1 亿美元 ARR](https://legora.com/newsroom/legal-teams-adoption-of-ai-propels-legora-past-100-million-in-annual-recurring-revenue) · [Legora Series D extension](https://legora.com/newsroom/legora-extends-series-d-with-additional-50-million-welcomes-atlassian-and-nventures-as-investors)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。应用层真正翻身的时候，往往不是模型突然变神，而是账单逻辑和工作流归属先变了。*
