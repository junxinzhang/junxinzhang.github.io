---
layout: post
title: "猪厂回收员工 Skill：你的工作流，才是企业最值钱的资产"
date: 2026-03-31
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260331-skill-recovery-cover.jpg
tags: [featured, AI Agent, Skill, Workflow, 网易, ClawHub, 企业资产, 龙虾, OpenClaw]
slug: netease-skill-recovery-workflow-enterprise-core-asset
description: "网易智企推行「龙虾」Agent 技能体系，要求员工把日常工作流封装成可复用 Skill。员工骂声一片，但管理层的逻辑很清晰：人会走，Skill 不会。ClawHub.ai 已经把 Skill 做成了 AI Agent 的 npm——真正该焦虑的不是被回收，而是你有没有值得回收的东西。"
faq:
  - question: "什么是 AI Agent 的 Skill？"
    answer: "Skill 本质是把工作流中的 Best Practices 封装成标准化、可版本化、可复用的能力模块。一个 SKILL.md 文件就是一套完整的操作指南，AI Agent 读取后可以自主执行对应任务。"
  - question: "ClawHub.ai 是什么？"
    answer: "ClawHub 是 OpenClaw（龙虾）生态的官方 Skill 注册中心，类似 AI Agent 的 npm。开发者可以在上面发布、搜索、版本化管理 Agent 技能包，支持向量语义搜索。"
---

网易智企最近搞了个「技能回收」——要求员工把日常工作中沉淀的 Best Practices 封装成标准化 Skill，统一入库、统一管理。

消息一出，内部论坛炸了。**员工骂声一片：「我的经验凭什么交出去？」「这不就是要把人榨干再踢走？」**

**<mark>但如果你站到管理层视角冷静看一秒——人走了，Skill 留下。这不是剥削，是 AI 时代企业生存的基本逻辑。</mark>**

![猪厂回收员工 Skill：你的工作流才是最值钱的资产](/assets/images/screenshot-20260331-skill-recovery-cover.jpg)

---

## 一、猪厂到底在干什么？

网易智企内部推进的 AI Agent 项目代号叫**「龙虾」**（即 OpenClaw）。核心思路不复杂：

| 动作 | 具体内容 |
|------|---------|
| 封装 | 把重复性工作流写成 Skill 文件 |
| 入库 | 统一存入企业技能中心 |
| 调度 | 由主控 Agent 按需调用 |
| 迭代 | 版本化管理，持续优化 |

简单说——**以前靠人记、靠人教、靠人传帮带的工作经验，现在要求写成 AI 能读懂的标准格式。** 一个 `SKILL.md` 文件，就是一套完整的操作手册。Agent 读取之后，可以自主执行对应任务。

网易还提出了三级落地路径：LV1 个体提效、LV2 业务提效、LV3 组织重塑。目标很明确——**从「一个人会干」到「Agent 也会干」再到「组织不依赖任何一个人」。**

员工当然不乐意。但这件事的底层逻辑，比骂街重要得多。

![技能回收计划：管理层与员工的认知裂缝](/assets/images/screenshot-20260331-skill-recovery-tension.jpg)

---

## 二、Skill 到底是什么？

很多人把 Skill 理解成「文档」，错了。**Skill 是工作流的 Best Practices，被结构化之后变成了 Agent 的能力模块。**

传统文档和 Skill 的区别：

| 维度 | 传统文档 | Skill |
|------|---------|-------|
| 读者 | 人 | AI Agent |
| 格式 | 自由散文 | 结构化 YAML + Markdown |
| 可执行 | 要靠人理解再操作 | Agent 直接执行 |
| 版本化 | 大多没有 | semver 管理 |
| 复用性 | 低，换个人就看不懂 | 高，跨团队跨项目通用 |

一个好的 Skill 长什么样？就是一个文件夹，里面有：
- **SKILL.md**：核心指令文件，告诉 Agent「做什么、怎么做、什么条件下触发」
- **scripts/**：辅助脚本
- **examples/**：参考案例

**<mark>工作流人人都有，但能把工作流变成 Skill 的人，才是真正不可替代的。因为你沉淀的不是文档——是可执行的组织能力。</mark>**

![从零散工作流到标准化技能：Skill 的本质](/assets/images/screenshot-20260331-skill-workflow-transform.jpg)

---

## 三、ClawHub：龙虾生态的 npm

网易用的「龙虾」体系，背后有一个公开的 Skill 注册中心——[ClawHub.ai](https://clawhub.ai)。

ClawHub 的定位很清楚：**AI Agent 的 npm。** 开发者可以在上面发布、搜索、安装 Agent 技能包。

| 能力 | 说明 |
|------|------|
| 发布 Skill | 打包上传，自动版本管理 |
| 向量搜索 | 用自然语言找技能，不用记包名 |
| CLI 工具 | `clawhub search` / `clawhub install` |
| 安全审核 | 标记可疑技能，社区信任评分 |

用法和 npm 一样简单：

```bash
clawhub search "数据清洗"
clawhub install data-cleaning-skill
```

装完之后，你的 Agent 就多了一项能力。不需要写代码，不需要对接 API——**读 SKILL.md，执行，完事。**

当然，ClawHub 也踩过坑。之前出现过伪装成合法插件的恶意 Skill（「ClawHavoc」事件），窃取用户凭据。所以官方现在强调：**安装前看源码，用完销毁密钥，定期检查插件目录。**

**<mark>ClawHub 证明了一件事：Skill 不是某家企业的内部概念——它正在成为整个 AI Agent 生态的通用语言。</mark>**

![ClawHub.ai：AI Agent 的技能市场](/assets/images/screenshot-20260331-clawhub-marketplace.jpg)

---

## 四、真正该焦虑的是什么？

回到猪厂员工骂街这件事。情绪可以理解，但方向搞反了。

**真正该焦虑的不是「我的经验被回收了」——而是「我有没有值得回收的经验」。**

| 类型 | 特征 | 结局 |
|------|------|------|
| 纯执行者 | 按 SOP 操作，没有沉淀 | 最先被 Agent 替代 |
| 经验型选手 | 有 Best Practices，但没写下来 | 人走经验散 |
| Skill 型选手 | 把工作流编成可执行技能 | 人走技能留，不可替代性最高 |

我更推荐的做法：**别等公司来回收——主动把自己的 Workflow 编成 SKILL。** 这才是你在 AI 时代的核心竞争力。

你可以发到 ClawHub 上成为开源贡献者，也可以留在企业内部成为技能中心的核心资产。无论哪条路，**能写 Skill 的人，比只会用 Skill 的人值钱十倍。**

**<mark>人会离职，代码会过时，但一套经过验证的、版本化的、可复用的 Skill 体系——这是企业在 AI 时代最值钱的护城河。</mark>**

![人走了，技能留下：企业的真正护城河](/assets/images/screenshot-20260331-enterprise-skill-asset.jpg)

---

## 写在最后

猪厂这波操作，骂的人多，看懂的人少。

Skill 不是企业在压榨你——**Skill 是你证明自己价值的最佳方式。** 那些能把混乱工作流变成结构化、可复用、可版本化能力的人，不会被「回收」，只会被争抢。

我一个人打造的 [Zaokit AI](https://zaokit.app) 正在内测，**前 1000 名用户赠送价值 150 RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成，唯一网站：[zaokit.app](https://zaokit.app)。

**<mark>AI 时代，Workflow 是个人能力，Skill 是组织资产。能把前者变成后者的人，永远不会被淘汰。与其骂公司回收你的经验，不如先问自己：我的经验，配得上被回收吗？</mark>**

---

## 相关阅读

**AI Agent 与 Skill 系列**
- [不裁你是因为你没用 AI，裁你是因为要给 AI 腾位置]({{ site.baseurl }}/ai-layoff-not-because-of-ai-but-for-ai)
- [阿里 Token「鸡蛋」战略背后的真相：一场关于 AI 劳动力的静默革命]({{ site.baseurl }}/alibaba-token-eggs-ai-workforce-revolution)
- [月投 650 刀订阅 AI Agent：当 Token 不再有限制，生产力到底能有多大？]({{ site.baseurl }}/agent-arms-race-650-dollars-per-month)
