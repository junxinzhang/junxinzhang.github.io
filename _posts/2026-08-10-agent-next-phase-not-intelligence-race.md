---
layout: post
title: "Agent 下一程，打在云上"
date: 2026-08-10
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260810-agent-next-phase.webp
tags: [featured, AI, Agent, OpenAI, Codex, Manus, 季逸超, 云端Agent, Agent Runtime, Zaokit]
slug: agent-next-phase-not-intelligence-race
description: >
  OpenAI 收购 Ona、招 Cloud Agents 工程师、Tibo 暗示 Codex 即将过时——三条线索拼在一起，
  指向同一个判断：Agent 的下一程不是比模型聪明，是比谁先给 Agent 造出云端的身体。
  而 Manus 的季逸超，一年前就在造了。
faq:
  - question: "OpenAI 收购 Ona 意味着什么？"
    answer: "Ona 的核心能力是让 Agent 在客户的云环境里持续运行——笔记本合上，Agent 不停。OpenAI 官方称之为'Codex 的下一阶段'，这意味着 Codex 正在从本地 CLI 工具演进为云原生的 Agent 基础设施。"
  - question: "Manus 为什么被认为提前看到了 Agent 终局？"
    answer: "Manus 从 2025 年初发布起就完全运行在云上，2025 年中引入 wide research 增加任务拓扑密度，年底开始做主动式 Agent，并很早就建立了 evaluation 团队。这些决策在当时看是超前的，现在看恰好是 OpenAI 正在追赶的方向。"
  - question: "Manus 订阅用户为什么会下降？"
    answer: "ChatGPT 更新 GPT 5.6 之后模型能力上限大幅提升。Agent 产品的用户体验天花板由底座模型决定——产品形态领先不能弥补模型代差。这是所有 Agent 创业公司面对的核心矛盾。"
  - question: "Agent 下一阶段的竞争维度是什么？"
    answer: "三个维度同时比拼：模型智能（决定任务复杂度上限）、云端执行能力（决定 Agent 能否独立持续工作）、计算资源配额（决定并行规模和持续时间）。只有模型不够，只有产品也不够。"
---

最近盯着 OpenAI 的动作看了一周。三件事串在一起，一个判断就清楚了。

> **Agent 的下一程，不是比谁的模型更聪明。是比谁先给 Agent 造出一个云端的身体——让它合上你的笔记本之后，还能继续干活。**

![Agent 下一程，比的不是智商](/assets/images/cover-20260810-agent-next-phase.webp)

## 一、OpenAI 的三条线索

第一条：**收购 Ona。** 官方说法是「Codex 下一阶段」。Ona 做的事情很具体——让 Agent 在客户的云环境里持续运行。你的笔记本合上，Agent 不停。

第二条：**在招 Cloud Agents 工程师。** 岗位描述四个关键词：编排、沙箱、身份、成本。这不是在做一个 CLI 工具，是在造一套基础设施。

第三条：**Codex 负责人 Tibo 那句话**（[之前文章引用过](/what-did-they-see-jeff-dean-new-paradigm)）——Codex 是个好 harness，但两三个月后会显得原始，下一代模型需要的不只是你的笔记本。

三条放在一起看，其实在讲同一件事：

**模型将拉起临时 workspace——机器、Agent、共享内存、权限——连续工作数天。**

这不是「Codex 变快一点」。是运行范式的切换。从「你打开终端给 Agent 下指令」变成「Agent 自己拉起一整套执行环境，干完了把结果交给你」。

![OpenAI 三条信号指向同一个方向](/assets/images/illust-20260810-three-signals.webp)

## 二、季逸超一年前就在造这个东西

回过头看 Manus，它从产品形态上，基本就是朝着这个「终局」去的。

| 时间 | Manus 做了什么 | 对应的终局能力 |
|------|---------------|---------------|
| 2025 年初 | 完全运行在云上，本地无打扰 | 云原生 Agent 执行环境 |
| 2025 年中 | 引入 wide research | 任务拓扑方向的智能调用密集度 |
| 2025 年底 | 开始做主动式 Agent | 时间维度的智能调用密集度 |
| 很早 | 建立 evaluation 团队 | Agent 产品的迭代地基 |

2025 年初发布 Manus，意味着 2024 年季逸超团队对整体方向已经有比较强的判断和投入。**OpenAI 今天在追的东西——云端持续运行、容器隔离、评估体系——Manus 一年前就在造了。**

季逸超牛逼。产品经理的眼界，在 25 年初发布这个产品，说明 24 年对方向已经有了清晰判断。连续创业者的市场洞察力就是强。他们很早就意识到三件事要分开做：容器、评估、架构。还有一个很多人没看到的区分——增强人和替代人的区别。Manus 走的是替代路线：Agent 独立完成任务，人只看结果。

这个判断在当时是超前的。大部分团队还在做「辅助写代码」，季逸超已经在做「Agent 独立干活」。

![Manus 的终局直觉](/assets/images/illust-20260810-manus-endgame.webp)

## 三、但模型上限才是留存——Manus 的困局

说完 Manus 的强，也要说它的难。

Manus 订阅用户在下降。原因不复杂：ChatGPT 更新了 GPT 5.6 之后，模型上限太高了。

这里面有一个残酷的逻辑：

**产品形态可以领先，但模型能力是天花板。**

Manus 的 Agent 架构做得再好，底座模型如果和 GPT 5.6 有代差，用户体验的上限就被锁死了。模型能力一拉开，订阅留存差距立刻可见。

| | Manus | ChatGPT (GPT 5.6) |
|--|-------|-------------------|
| 产品形态 | 领先（云原生、主动式） | 在追（Codex 整合中） |
| 模型上限 | 受限于接入的底座模型 | 自家最强模型 |
| 订阅留存 | 下降 | 稳定 |

这也是所有 Agent 创业公司面对的核心矛盾：**你能把编排做到极致，但推理能力的上限不在你手里。** 模型是别人家的，天花板也是别人定的。

但这不影响季逸超的判断力。产品方向没看错——只是模型底座不是他能决定的变量。

## 四、下一程的竞争维度

那下一阶段到底比什么？我的判断是三个维度同时比拼：

**智能 × 云端执行能力 × 计算资源配额。**

光有聪明的模型不够——没有云端身体，Agent 就困在你的笔记本里。光有好的产品形态也不够——底座模型有代差，体验上限直接打折。光有算力也不够——没有好的编排和评估体系，算力就是浪费。

国内能对标的玩家：月之暗面没有计算资源，字节跳动没有创新力。Manus 有眼光有执行，但缺模型底座。

这也引出一个关于连续创业者的思考。所谓「连续」，不是「在大厂杀死这个行业之前快速融资赚钱」——而是 **pivot 的能力**。比如 OpenAI 在 Sora 2 没盈利的时候砍掉它，在趋势明显的时候把 ChatGPT 和 Codex 合并。方向判断 + 执行果断，才是连续创业者真正的护城河。

![竞争维度：智能 × 执行 × 算力](/assets/images/illust-20260810-competition-axis.webp)

## 五、终局形态：Agent 成为独立 Control Plane

顺着这条线想下去，Agent 的终局形态正在变清晰：

**Agent 成为一个独立的 control plane——按任务动态调度本地和云端 execution environments，同时可以无限横向扩展 worker。**

容器、评估、架构分开。Agent 不再是跑在你电脑上的一个进程，而是一套独立系统。它自己决定用什么执行环境、自己拉起资源、自己释放。

但这里面有一个被严重低估的难题：**怎么把你本地机器的身份、授权、文件和运行环境，打包交给云端沙箱？**

每个人的本地机器，本质上就是自己的分身和记忆。你的 SSH key、你的 git 凭证、你的 `.env` 文件、你跑了三天才配好的开发环境、你本地分支上昨晚改到一半的代码——这些不是数据，是上下文。把它们安全、完整地同步给一个云端容器，远比听起来要难。

| 需要打包的 | 难在哪 |
|-----------|-------|
| 身份与授权 | SSH key、API token 不能明文上传，需要安全注入 |
| 文件系统 | 本地未提交的改动、.gitignore 里的配置文件 |
| 运行环境 | 依赖版本、系统级工具链、自定义脚本 |
| 隐性上下文 | 你脑子里知道但没写在文档里的东西 |

这就是为什么 OpenAI 招的 Cloud Agents 工程师要懂身份和沙箱——不是造一个能跑代码的容器就完了，是要让这个容器**变成你的分身**。

我自己也在做 Agent Runtime（[Zaokit](https://zaokit.ai)），感受很直接：本地和云上各有优劣。云上 24 小时随叫随到，本地还要开电脑；但本地访问文件和凭证更有优势。云上可以通过链接外部存储和安全凭证注入来平衡——所以我坚信云 Agent 有其发展空间，但谁先把「本地分身上云」这件事做顺，谁就占住了真正的入口。

Manus 团队的很多工作，都让我后知后觉。终局形态的演进路径值得持续追踪。

![Agent 作为独立 Control Plane](/assets/images/illust-20260810-control-plane.webp)

## 写在最后

压成五句：

1. **OpenAI 三条线索指向同一件事**——收购 Ona、招 Cloud Agents 工程师、Tibo 暗示 Codex 即将过时，都在说 Agent 要搬进云里
2. **Manus 一年前就看到了这个方向**——云原生、wide research、主动式 Agent、evaluation 团队，季逸超的产品判断力值得尊重
3. **但模型上限才是留存的命门**——GPT 5.6 一出，产品形态领先也扛不住模型代差
4. **下一程三维比拼**——智能 × 云端执行能力 × 计算资源配额，缺任何一个都打不赢
5. **终局是 Agent 成为独立 control plane**——动态调度本地和云端执行环境，无限横向扩展

说直白点：

**下一代 Agent 不住在你电脑里，住在云上——带着你的身份、你的记忆、你的环境。谁先把这件事做顺，谁赢。**

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

延伸：[你的公司电脑，可能连 Agent 的门都进不了](/agent-runtime-beyond-laptop-infrastructure) · [他们到底看到了什么？让 Jeff Dean 离开待了 27 年的 Google](/what-did-they-see-jeff-dean-new-paradigm) · [没烧过 token，就别说看懂 AI 半导体](/token-burn-ai-semiconductor-investing)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Agent 的下一程，打在云上——谁先让你的分身住进去，谁赢。*
