---
layout: post
title: "企业已经有了 M365 Copilot，还要不要 OpenClaw、Hermes 和客户端 Agent？"
date: 2026-07-18
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260718-m365-openclaw-hermes.webp
tags: [featured, AI, Agent, M365 Copilot, OpenClaw, Hermes, Claude Code, Codex, 企业AI, TokenHub, 数字员工, Zaokit]
slug: m365-copilot-openclaw-hermes-layers
description: >
  很多企业已经买了 Microsoft 365 Copilot，仍被反复追问：还要不要上 OpenClaw、Hermes，
  还要不要给研发发 Claude Code / Codex。真正的问题不是三选一，而是它们处在不同层级。
  这篇接昨天「工具可分部门、心脏只能一颗」，把办公协作层、Agent Gateway、Agent Runtime
  和专业执行器拆开，说清楚什么该组合、什么别互相替代。
faq:
  - question: "企业已经有 M365 Copilot，还要不要单独建 OpenClaw 或 Hermes？"
    answer: "要不要建，取决于你的任务有没有超出 Microsoft 365 办公上下文。Copilot 擅长邮件、会议、文档、Teams/SharePoint 内的知识协作；跨 IM 渠道、本地文件、终端脚本、长任务记忆与调度、多执行器路由，通常仍需要 Agent Gateway / Runtime 层。不是替代 Copilot，是补它原生边界之外的能力。"
  - question: "OpenClaw 和 Hermes 是同类产品吗？该选哪个？"
    answer: "不是同类。OpenClaw 更偏多渠道 Agent Gateway：统一会话、渠道接入、多 Agent 路由。Hermes 更偏可执行、可记忆、可调度的 Agent Runtime：长任务、技能沉淀、定时与工具闭环。常见做法是组合使用，而不是二选一硬砍。"
  - question: "Claude Code、Codex 这类客户端 Agent 又算哪一层？"
    answer: "它们是专业执行器。高复杂度研发、多文件工程、终端与工具调用密集的任务，更适合交给 Claude Code / Codex 一类深度执行器；它们不替代 Copilot 的办公入口，也不替代 Gateway 的渠道调度。"
  - question: "这和昨天说的 Token Hub 是什么关系？"
    answer: "昨天讲的是：前台工具可以分部门选，企业要有一颗 Token Hub 把轨迹、成本、权限收回来。今天讲的是前台之上的分层：办公协作层、接入调度层、执行运行层、专业执行器。Token Hub 是心脏；这些层是器官。器官可以分工，心脏仍只能有一颗。"
---

昨天写[企业端 Agent 怎么建、怎么选](/enterprise-agent-build-choose-token-hub)时，我把观点压成一句：

**工具可以分部门选，心脏只能有一颗 Token Hub。**

写完之后，企业侧又有一个更具体、也更常见的问题被反复抛出来：

> 我们已经买了 Microsoft 365 Copilot。  
> 还要不要搞 OpenClaw？还要不要上 Hermes？研发是不是还得再发 Claude Code / Codex？

这个问题听起来像采购清单，其实是架构问题。

很多人默认它们是同一货架上的三个牌子：买了 A 就不必买 B，买了 B 就不必再碰 C。  
真正容易做错的，恰恰是这个默认。

**M365 Copilot、OpenClaw、Hermes 不是同类产品，也不在同一层。**  
客户端 Agent 工具更不是“第四个 Copilot”，而是专业执行器。

核心目标只有一句：

**搞清楚三者不是同级替代，而是不同层级、不同适用场景；组合使用，通常比互相替代更合理。**

![不是三选一，是分层组合](/assets/images/cover-20260718-m365-openclaw-hermes.webp)
<!-- baoyu-skill prompt: 2.35:1电影感横版封面，深蓝夜色到冷青渐变，冷静厚重的科技质感。画面三层横向分层结构：上层冷蓝「M365 Copilot」办公协作层（邮件/文档剪影），中层青绿「OpenClaw」多渠道网关节点与连接线，下层暖金「Hermes」Runtime 齿轮与记忆环。三者用细线串联而非对撞。中央大字中文「已有Copilot，还要不要Agent层」，顶部主标题中文「不是三选一，是分层组合」，底部副标题中文「办公协作层 · Agent Gateway · Agent Runtime」。中文清晰可读。 --ar 2.35:1 -->

## 一、先把问题问对：不是“还要不要买”，是“缺的是哪一层”

企业里最常见的讨论姿势，是把所有带 AI 字样的东西都丢进一张选型表：

| 名称 | 谁在推 | 听起来像什么 |
|---|---|---|
| M365 Copilot | IT / 办公数字化 | 全员办公助手 |
| OpenClaw | 技术 / 自动化团队 | 本地 Agent / 多渠道助手 |
| Hermes | 技术 / Agent 基建 | 可长期跑的 Agent Runtime |
| Claude Code / Codex | 研发负责人 | 编程与工程 Agent |

表一拉出来，老板很容易问一句：

**“我们不是已经有 Copilot 了吗？为什么还要这么多？”**

这句话本身没错。错在后面默认的结论：  
“有了办公助手，就等于有了 Agent 架构。”

微软对 [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot/enterprise) 的定位很清楚：它是嵌在 Word、Excel、PowerPoint、Outlook、Teams 等应用里的企业办公 AI，回答与动作尽量 grounded 在 Microsoft Graph 与企业权限体系里；公开架构说明也强调它在租户权限边界内做 grounding（[Microsoft 365 Copilot architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture)）。Copilot Studio 还能继续扩自定义 Agent 与工作流。企业侧常见的是按席位附加许可，而不是“装一个就覆盖所有 Agent 场景”。

这非常强。  
但它强的是 **M365 办公上下文里的协作与知识入口**，不是“任意系统、任意渠道、任意长任务、任意执行器”的通用 Agent 底座。

所以更准确的问法不是：

- 还要不要再买一个更强的？

而是：

1. 你们 80% 的高价值任务，是不是都发生在 Outlook / Teams / SharePoint / OneDrive 里？  
2. 有没有大量请求从企微、飞书、Slack、Telegram、手机 IM 进来？  
3. 有没有跨本地文件、终端、遗留系统、内部工具的长链路任务？  
4. 有没有需要持续记忆、定时调度、技能沉淀、失败回退的自动化？  
5. 研发侧有没有高复杂度工程任务，必须交给深度执行器？

只要后四条里有一条成立，**只靠 M365 Copilot 就不够**。  
不是 Copilot 不行，是它本来就不是那一层。

## 二、一张图看清：三层定位，不是三选一

先把结论摊开。公开产品定位与社区对比里，可以把三者压成下面这张表：

![M365 Copilot vs OpenClaw vs Hermes 分层对比](/assets/images/chart-20260718-m365-openclaw-hermes.webp)

| 维度 | A. M365 Copilot | B. OpenClaw | C. Hermes |
|---|---|---|---|
| **产品本质** | 企业办公智能助手 / Microsoft 365 工作入口 | 自托管 Agent Gateway / 多渠道接入层 | Agent Runtime / 任务执行与学习引擎 |
| **核心强项** | 邮件、会议、文档、PPT、Excel、Teams、SharePoint、OneDrive 内容理解与协作 | 连接 Teams、Slack、Telegram、微信类入口；统一会话；多 Agent 路由；把请求送给合适执行器 | 长期记忆、技能沉淀、定时任务、终端/文件/工具调用、并行子 Agent、持续执行 |
| **最适合场景** | 总结会议、写邮件、生成文档、办公问答、基于 M365 内容协作 | 个人/团队助理入口、消息渠道统一接入、手机/IM 发起任务、Agent 分发与路由 | 长任务自动化、跨系统执行、文件处理、终端脚本、监控巡检、流程自动化 |
| **原生边界** | 强依赖 Microsoft 365 / Graph / Copilot Studio 生态 | 更偏通信、接入、会话与路由，不是最强的复杂任务执行引擎 | 需要企业自行治理权限、安全、运行环境和审计 |
| **不擅长** | 作为统一的跨系统 Agent 执行底座；复杂终端执行；长时间自主运行任务 | 单独承担复杂长任务、技能沉淀、深度执行闭环 | 单独承担企业办公门户体验；M365 原生内容协作体验不如 Copilot |
| **一句话定位** | 办公与知识协作层 | Agent 接入与调度层 | Agent 执行与运行层 |

OpenClaw 官方与文档把自己放得很明确：它是跑在你自己机器/服务器上的 [multi-channel gateway](https://docs.openclaw.ai)，一个 Gateway 进程承接 Discord、Telegram、WhatsApp、Signal、Slack、Teams 等渠道，管理会话、路由与多 Agent 分发；文档把 Gateway 写成 sessions、routing、channel connections 的 single source of truth。站点原话也直白——open source，runs on your machine，the AI that really does things。安全文档还写得很干脆：默认更接近**单用户 / 单信任操作员**模型，不是开箱即用的敌对多租户边界——企业若多人共用，要自己拆分信任域、做隔离与审计。

Hermes（[Nous Research](https://hermes-agent.nousresearch.com)）则更强调 Runtime：持久记忆、技能从经验中沉淀、定时与无人值守任务、子 Agent 并行、多沙箱后端执行。官方 slogan 是 “The Agent That Grows With You”，公开仓库也提供从 OpenClaw 迁入的路径（如 `hermes claw migrate`），侧面说明社区场景里二者常被衔接，而不是天然互斥。公开对比里常见的说法是：Hermes 把 gateway 包在一个会学习的 agent 外面；OpenClaw 把 agent 能力包在一个常驻 messaging gateway 外面。

**一个偏接入与控制面，一个偏执行与学习环。**  
都重要，但职责不同。

再往下，还有第四块经常被误塞进同一表格的东西：

**Claude Code / Codex / 企业专用 Agent = 专业执行器。**

它们擅长高复杂度研发、工程交付、多文件修改、终端与工具闭环。  
把它们拿去当全员办公入口，浪费；拿去替代 Gateway，也不合适。

推荐理解方式，不是“选一个赢家”，而是：

![推荐理解方式：不是三选一，而是分层组合](/assets/images/illust-20260718-layered-stack.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅架构信息图，深色背景，冷静科技质感。从左到右四段发光流程：1用户工作入口（Teams/Outlook/飞书/企微）2交互知识层（M365 Copilot）3 Agent Harness/Runtime（OpenClaw+Hermes）4专业执行器（Claude Code/Codex/企业专用Agent）。每段下方中文小标签。顶部大字中文「推荐理解方式：不是三选一，而是分层组合」。底部小字中文「入口→协作→运行→执行」。中文清晰可读。 --ar 2.35:1 -->

```text
用户工作入口
Teams / Outlook / 飞书 / 企微 / Web / Mobile
        ↓
交互 / 知识层
M365 Copilot（办公协作与企业知识入口）
        ↓
Agent Harness / Runtime
OpenClaw（接入与路由） + Hermes（执行、记忆、调度）
        ↓
专业执行器
Claude Code / Codex / 企业专用 Agent
```

这和我前面写 [Harness Engineering](/one-person-agent-world-class-company) 时的体感是一致的：模型只是原料，真正决定能不能稳定干活的，是外面那圈壳——接入、记忆、权限、调度、验收、回流。

## 三、为什么“已经有 Copilot”仍不够

这一节不攻击微软。相反，Copilot 在它该强的地方确实强。

问题在于企业真实工作，从来不只发生在 M365 里。

![为什么不能只用 M365 Copilot](/assets/images/illust-20260718-why-not-only-copilot.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景，冷静科技质感。左侧一个发光的 M365 Copilot 窗口被边界框圈住，框外标中文「原生边界：Graph / M365 生态」；右侧散落的本地文件、终端、遗留系统、IM多渠道图标无法直接连入。中央大字中文「为什么不能只用M365 Copilot」。底部四条中文要点：「办公上下文为主」「跨系统需集成」「长任务缺闭环」「难扛多执行器架构」。中文清晰可读。 --ar 2.35:1 -->

### 1. 主要面向 Microsoft 365 办公上下文

总结会议、改 PPT、查邮件线程、基于 SharePoint 文档问答——这些 Copilot 很合适。

但一旦任务变成：

- 从企微群里接一个运维告警；  
- 到某台机器上跑脚本核对配置；  
- 回写内部工单系统；  
- 夜里定时巡检并把结果推到多个渠道；

你需要的就不是“更会写邮件的助手”，而是 **可接入、可路由、可执行、可回传** 的 Agent 链路。

### 2. 跨本地文件、终端、遗留系统，往往要额外集成

企业里总有一批“不在 Graph 里”的东西：

- 本地目录与导出文件；  
- 老 ERP / 自研系统；  
- 运维脚本与 CLI；  
- 浏览器里才能点的后台；  
- 只存在于 IM 群里的半结构化指令。

Copilot Studio、连接器、Power Platform 能扩一部分。  
但很多团队最终仍会发现：真正卡脖子的不是“会不会聊天”，是 **执行边界与系统边界**。

这正是 Gateway + Runtime + 专业执行器存在的理由。

### 3. 复杂任务更吃持续执行、记忆、调度与工具闭环

一次生成会议纪要，和连续三天推进一个跨系统变更，是两种完全不同的负载。

后者需要：

- 记住上次卡在哪；  
- 定时醒来继续做；  
- 调用终端/文件/浏览器/API；  
- 失败可回退、可人工接管；  
- 成功路径沉淀成技能，而不是沉进某次聊天记录。

[Hermes](https://hermes-agent.nousresearch.com) 一类 Runtime 强调的，就是这条线：memory、skills、scheduling、sandboxed execution、subagents。  
[OpenClaw](https://openclaw.ai) 一类 Gateway 强调的，则是把这些能力接进人们已经在用的聊天入口，并做好会话与路由。

### 4. 很难单独承载“多渠道 + 多执行器 + 跨系统”的 Agent 架构

企业最后真正想要的，往往不是一个超级聊天窗口，而是一张可控的能力网：

- 请求从哪里进；  
- 交给谁执行；  
- 用哪套权限；  
- 结果回到哪里；  
- 成本与轨迹记在哪。

M365 Copilot 可以是这张网里很重要的办公节点。  
但它很难单独充当整张网的骨架。

这也呼应我之前写[数字员工平台](/enterprise-digital-employee-department)时的判断：企业买的不是模型下拉框，是可治理的岗位交付。岗位交付一旦跨出办公套件，就一定会碰到 Gateway、Runtime 和专业执行器的分工。

## 四、推荐用法：各层各司其职

把“还要不要”改成“谁负责什么”，决策会顺很多。

![推荐使用方式：各层各司其职](/assets/images/illust-20260718-recommended-combo.webp)
<!-- baoyu-skill prompt: 2.35:1宽幅信息图，深色背景，冷静科技质感。四个并列职责卡片：1 M365 Copilot 中文「办公协作与企业知识入口」2 OpenClaw 中文「消息入口·会话·Agent路由」3 Hermes 中文「任务执行·记忆·调度·技能沉淀」4 Claude Code/Codex 中文「高复杂度研发与工程任务」。顶部大字中文「推荐使用方式：各层各司其职」。底部小字中文「组合使用比互相替代更合理」。中文清晰可读。 --ar 2.35:1 -->

### 1. M365 Copilot：办公协作与企业知识入口

适合：

- 全员办公提效；  
- 会议、邮件、文档、表格、演示文稿；  
- 基于已有 M365 权限与内容的问答；  
- 需要强合规、强身份、强审计的办公场景。

不适合硬扛：

- 统一承接所有 IM 渠道的 Agent 请求；  
- 长时间跨系统自主作业；  
- 替代研发侧深度工程执行器。

一句话：**让它做办公层，别逼它做操作系统。**

### 2. OpenClaw：消息入口、会话管理、Agent 路由

适合：

- 把 Telegram / Slack / Teams / 微信类入口统一进来；  
- 同一套会话与权限策略；  
- 多 Agent / 多 workspace 分发；  
- 手机或 IM 里发起任务，而不是所有人挤进同一个 Web 聊天框。

公开文档把它描述成 self-hosted multi-channel gateway，核心价值就是：**一个 Gateway，服务多个渠道与多个 Agent 会话。**

不适合单独指望它：

- 把所有复杂长任务执行、技能自我沉淀都包圆。

一句话：**它更像前台总机 + 调度台，不是整座工厂。**

### 3. Hermes：任务执行、记忆、调度、技能沉淀

适合：

- 需要跨天、跨会话继续推进的任务；  
- 定时报告、巡检、备份、批处理；  
- 终端/文件/工具调用密集；  
- 希望 Agent 把做成过的事沉淀成可复用 skill。

公开材料强调 persistent memory、auto-generated skills、unattended scheduling、isolated subagents、多种 sandbox backend。  
这是典型 Runtime 语言，不是办公套件语言。

不适合单独指望它：

- 直接提供企业级 M365 原生协作体验；  
- 替代安全、IAM、审计与组织治理本身。

一句话：**它更像能长期上班、会记经验的执行引擎。**

### 4. Claude Code / Codex 等：专业执行器层（客户端 Agent）

到了执行层，又会撞上另一张表：Claude Code、Codex、Qoder、WorkBuddy/CodeBuddy、TRAE、Dumate……看起来又是一堆“智能体工具”。

别和前面的 M365 / OpenClaw / Hermes 搅在一起。  
**这张表比的是专业执行器怎么选，不是再找一个办公入口或 Gateway。**

![主流 AI 编程智能体工具全景对比](/assets/images/chart-20260718-ai-coding-agents-compare.webp)

公开的主流编程智能体对比，可以压成几条选型直觉（与[昨天文章](/enterprise-agent-build-choose-token-hub)同一套读法）：

1. **高复杂度、工程化、结果质量要求高的研发任务**  
   优先看 Claude Code、Codex：代码理解、多文件操作、任务完成度、终端/工具调用更硬。

2. **办公自动化 + IM 协同 + 日常提效**  
   更看生态打通与上手成本。腾讯系 WorkBuddy + CodeBuddy 一类，适合要快速铺开、又重度依赖内部沟通协同的组织。

3. **产品 / 设计 / 研发一体化**  
   需要办公、编程、设计三端一体与多模态协作时，TRAE 这类“工作台”定位更贴跨角色团队。

4. **研发提效 + 知识沉淀、本地优先与可控**  
   Qoder / QoderWork 一类更强调代码理解、项目管理与研发协同，适合中大型研发组织。

5. **企业知识整合、搜索增强、多智能体应用构建**  
   Dumate 一类更贴近知识密集岗位与企业级智能体构建。

适合交给专业执行器的，仍是：

- 多文件代码库；  
- 端到端实现、返工、可维护交付；  
- 终端、测试、工具链密集的工程活。

不适合：

- 当全公司唯一 AI 入口；  
- 替代 M365 办公知识协作；  
- 替代 OpenClaw / Hermes 的接入与运行职责；  
- 替代企业统一轨迹与成本治理。

一句话：**专业手术刀，不是办公前台，也不是 Gateway。**  
国内组合可以按场景互补；核心研发质量与完成度，仍优先国际领先的深度执行器，再用国内工具补协同、生态与成本。

### 5. 中美两条线：别只比“谁跑分高”

把视野再抬一层，会看到同一套 Agent 时代里，其实有两种常见打法：

![中美智能体发展趋势：同一个 Agent 时代，两种打法](/assets/images/chart-20260718-us-cn-agent-two-paths.webp)

- **美国一侧**更常追求能力上限：闭源大厂主导、Agent 工程化、企业级深集成、高算力高溢价。代表路径很清楚——OpenAI 的 Codex / Work 偏编码与计算机操作，Anthropic 的 Claude Code / Cowork 偏 Agent 工程标杆，Google 的 Agy IDE / Agy Agent 继续押 Gemini 多模态原生。  
- **中国一侧**更常强调落地效率：应用场景驱动、开源普惠、成本可控、快速适配。字节 Trae / Work、阿里 Qoder / Work、腾讯 CodeBuddy / WorkBuddy，把开发者平台、企业智能体与办公协同做成可铺开的组合，是这条线上的常见形态。  
- **开源力量**则横跨两边：OpenClaw（自托管、可定制、数据自主）、Hermes（开源智能体、轻量可托管），把“去中心化与数据自主”从口号变成可部署组件。

对企业采购来说，这句话比榜单有用：

**选型不再只比“谁跑分高”，而要比“场景适配 · 成本 · 数据自主”。**

这也解释了为什么企业会同时碰到 M365 Copilot、国产工作台、OpenClaw/Hermes、Claude Code/Codex：  
它们不是重复造轮子，而是分别回答了办公合规入口、落地效率、自托管控制面、能力上限这几类不同问题。

### 6. 组合关系怎么落

一个可落地的最小组合可以是：

1. **全员办公**：M365 Copilot  
2. **多渠道接入与路由**：OpenClaw（或同类 Gateway）  
3. **长任务 / 记忆 / 调度**：Hermes（或同类 Runtime）  
4. **研发工程**：Claude Code / Codex  
5. **心脏**：Token Hub——统一模型路由、权限、成本、使用轨迹与沉淀

注意：第 5 点不是可选项。  
昨天那篇已经说过了——没有心脏，前四层再漂亮，也只是各部门各自变强，组织能力仍然散。

## 五、和昨天那篇怎么搭配：器官可以分工，心脏只能一颗

把两天的文章并排放，结构就清楚了。

| 昨天（7/17） | 今天（7/18） |
|---|---|
| 工具可以分部门选 | 不同层的产品别互相替代 |
| 价值从个人 ROI 验证起 | 每层有自己的验收对象 |
| Token Hub 是心脏 | M365 / Gateway / Runtime / 执行器是器官 |
| 脚手架做薄、边界做厚 | 边界就是层级职责与权限 |
| 轨迹必须回流 | 各层产生的轨迹最终仍应汇入 Token Hub |

也就是说：

- **选型问题**：研发用 Claude Code，运营用生态更熟的办公与 IM 组合，完全可以。  
- **架构问题**：办公层、接入层、运行层、执行层，职责不要搅成一锅。  
- **治理问题**：无论前台几套壳，成本、权限、轨迹、沉淀最好回到同一颗 Token Hub。

如果只记两句：

1. **有了 Copilot，不等于有了 Agent 架构。**  
2. **有了 OpenClaw / Hermes / Claude Code，不等于有了组织能力——还得有 Token Hub。**

前者解决“层有没有齐”。  
后者解决“齐了之后会不会散”。

这也和[主权 AI](/enterprise-ai-sovereignty-karp-nadella)那条线相连：  
你租到的如果只是办公套件里的助手能力，而执行路径、记忆、技能、轨迹都不在自己可控的位置上，那你拥有的仍是便利，不是可迁移的机构智能。

## 六、一张决策表：你的企业缺的是哪一层

别从品牌偏好开始。从任务结构开始。

| 你的真实情况 | 优先补哪一层 | 典型动作 |
|---|---|---|
| 全员主要痛点在邮件/会议/文档 | M365 Copilot / 办公协作层 | 先把办公入口用深，设好权限与场景验收 |
| 请求大量来自 IM / 手机 / 多群 | OpenClaw 类 Gateway | 统一渠道、会话、路由与允许名单 |
| 任务跨天、要记忆、要定时、要工具闭环 | Hermes 类 Runtime | 上执行引擎、沙箱、技能沉淀与调度 |
| 研发交付质量与速度是瓶颈 | Claude Code / Codex | 按团队发专业执行器，先量个人 ROI |
| 各部门都在用，但老板看不清成本与沉淀 | Token Hub | 统一入口、账单、轨迹、权限与回流 |
| 以上同时存在 | 分层组合，而不是换一个“全能神器” | 先定 1–3 个真场景，再按层补齐 |

再补四条落地原则，足够写进内部 proposal：

1. **先场景，后品牌。**  
   门店洞察、订单协同、工程交付、运维巡检——场景比 logo 重要。

2. **先个人 ROI，后全员铺开。**  
   昨天引用 Anthropic 一线观察时说过：先看一个人快了多少。今天同样适用。

3. **先边界，后自动化。**  
   哪些数据能碰、哪些动作必须人批、失败如何回滚——边界比“全自动”优先。

4. **先轨迹入口，后工具扩容。**  
   工具会换。  
   若轨迹进不了 Token Hub，扩容只是把账单和碎片同步放大。

## 七、几个容易踩的坑

### 坑 1：把 Copilot 当成通用 Agent Runtime

结果通常是：办公场景很亮眼，跨系统场景靠人工复制粘贴硬扛。  
演示很好看，岗位交付不稳定。

### 坑 2：把 OpenClaw 当“第二个 Copilot”推给全员

Gateway 的价值在接入与调度，不在提供完整办公套件体验。  
全员入口如果本来就在 M365，不必为了“统一”把所有人赶进另一个壳。

### 坑 3：只上 Runtime，不管渠道与治理

执行引擎很强，但请求从哪进、权限谁批、成本谁看、失败谁接，全是散的。  
最后变成技术团队的私人军火库，进不了组织能力。

### 坑 4：给所有人发最强执行器

Claude Code / Codex 很强，不等于每个岗位都需要同等深度的工程 Agent。  
错配会造成两件事：预算飙，以及“会用的人更强、不会用的人更乱”。

### 坑 5：层齐了，心脏空着

这是昨天的核心。  
今天补一句：  
**层越齐，没有 Token Hub 时浪费越大。**  
因为每多一层，就多一处账单、一处日志、一处不可迁移的个人经验。

## 写在最后

企业端 AI 讨论，很容易被拉进品牌对打：

Copilot 够不够强？OpenClaw 火不火？Hermes 会不会学？Claude Code 能不能取代一切？

这些都能聊。  
但对企业落地，更有用的判断只有分层这几个字。

**M365 Copilot 是办公协作层。**  
**OpenClaw 是 Agent Gateway。**  
**Hermes 是 Agent Runtime。**  
**Claude Code / Codex 是专业执行器。**  
**Token Hub 是心脏。**

所以，企业已经有了 M365 Copilot，还要不要 OpenClaw、Hermes 和客户端 Agent？

答案不是简单的“要”或“不要”，而是：

- 如果你的工作几乎都在 M365 内闭环，先把 Copilot 用深、用出可验收的岗位结果；  
- 如果你的请求跨渠道、跨系统、跨长时间、跨执行器，那就不是“还要不要再买一个助手”，而是 **该把缺的层补上**；  
- 无论补哪一层，轨迹、成本、权限与沉淀，尽量回到同一颗 Token Hub。

**三者职责不同，组合使用比互相替代更合理。**  
这不是折中，是架构常识。

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，核心就是让能力进入真实交付链路，而不是停在聊天窗口。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)  
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)  
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)  
- [gift.junxinzhang.com](https://gift.junxinzhang.com)  
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。重点仍是那句土话：

**前台可以分层，心脏不能空；工具会换，层级职责别混。**

---

参考与延伸：

- [Microsoft 365 Copilot for enterprise](https://www.microsoft.com/en-us/microsoft-365-copilot/enterprise)  
- [OpenClaw](https://openclaw.ai) · [OpenClaw Docs](https://docs.openclaw.ai)  
- [Hermes Agent（Nous Research）](https://hermes-agent.nousresearch.com) · [GitHub: nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)  
- 公开对比参考：[Hermes vs OpenClaw](https://userorbit.com/blog/hermes-agent-vs-openclaw) · [Technical deep dive](https://trilogyai.substack.com/p/technical-deep-dive-hermes-vs-openclaw)  
- 站内相关：  
  - [企业端 Agent 怎么建、怎么选：工具可以分部门，心脏只能有一颗](/enterprise-agent-build-choose-token-hub)  
  - [企业落地数字员工，真正要买的是岗位交付](/enterprise-digital-employee-department)  
  - [把数据交给 AI 巨头，简直是疯了：主权 AI](/enterprise-ai-sovereignty-karp-nadella)  
  - [智能体经济：一个人，就是一家世界级公司](/one-person-agent-world-class-company)  
  - [会学习的不是模型，是模型外面那圈壳](/harness-continuous-learning-self-iteration)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，一个自己一个人做 AI 产品的创业者。企业端 AI 最容易浪费预算的方式，不是买错某一个工具，而是把不同层级的东西当成同一货架上的替代品。如果你正在做 M365 与 Agent 基建的叠加设计，欢迎聊聊你现在卡在办公入口、渠道接入、Runtime，还是轨迹治理。*
