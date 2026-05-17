---
layout: post
title: "三巨头同时下场：OpenAI、Google、Anthropic 组建 FDE 军团，企业 AI 落地最后一公里之战打响"
date: 2026-05-17
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260518-fde-last-mile-cover.jpg
tags: [featured, AI, OpenAI, Google, Anthropic, FDE, 前线部署工程师, 企业部署, AI落地, DeployCo, Zaokit]
slug: fde-last-mile-openai-google-anthropic-all-in
description: "上周写了 OpenAI 成立 DeployCo，派 150 名前线部署工程师驻场客户。没想到不到一周，Google Cloud 和 Anthropic 也同步组建 FDE 军团——Google 全球 FDE 岗位暴增 800%，Anthropic 联合黑石、高盛成立 15 亿美元企业 AI 服务公司。三巨头同时下场做脏活累活，说明一件事：AI 竞争的终局，不是比谁的模型聪明，而是比谁能帮企业把'能用'变成'在用'。"
faq:
  - question: "什么是 FDE（前线部署工程师）？"
    answer: "FDE 全称 Forward Deployed Engineer，最早由 Palantir 定义。与传统顾问不同，FDE 直接嵌入客户团队，写代码、调系统、做集成，交付的是可运行的生产系统而非 PPT。OpenAI、Google、Anthropic 三家都在大规模招聘或组建 FDE 团队。"
  - question: "三巨头的 FDE 策略有什么区别？"
    answer: "OpenAI 通过收购 Tomoro 成立 DeployCo，自建部署公司；Anthropic 联合黑石、高盛等金融巨头成立 15 亿美元合资服务公司；Google Cloud 则大规模扩招 FDE，岗位增长 800%，内嵌到 Go-To-Market 团队。路线不同，终点相同。"
  - question: "这对 AI 创业者意味着什么？"
    answer: "三巨头覆盖的是超大型客户，中国几千万中小企业的 AI 落地需求仍然是巨大空白。做垂直场景的'小型部署公司'——帮客户接系统、改流程、出结果——是当下最确定的创业方向。"
---

上周写了 [OpenAI 成立部署公司 DeployCo]({{ site.baseurl }}/openai-deployco-ai-deployment-company-b2b)，收购英国公司 Tomoro，派 150 名前线部署工程师（FDE）直接进驻客户团队。当时的判断是：**AI 下半场，从卖模型到卖落地。**

没想到不到一周，Google 和 Anthropic 也动了。

![三巨头同时下场：企业 AI 落地最后一公里之战](/assets/images/screenshot-20260518-fde-last-mile-cover.jpg)

---

## 一、三巨头同一周内的三个大动作

先摆事实。

**5 月 4 日，Anthropic** 宣布联合黑石（Blackstone）、Hellman & Friedman、高盛（Goldman Sachs）成立一家独立的企业 AI 服务公司。总资本规模约 **15 亿美元**，背后还站着 General Atlantic、Apollo、GIC、红杉资本等一票顶级机构。这家公司不卖 API，专门帮中型企业把 Claude 嵌入核心业务——派 Applied AI 工程师驻场，和客户工程团队一起找场景、写代码、交系统。

**5 月 11 日，OpenAI** 成立 Deployment Company（DeployCo），收购 Tomoro，首轮融资超 40 亿美元，150 名 FDE 进场。[上篇文章]({{ site.baseurl }}/openai-deployco-ai-deployment-company-b2b)已经讲过，不再赘述。

**同期，Google Cloud** 全球 FDE 岗位暴增 **800%**。CEO Thomas Kurian 公开表态：**"Pilot 时代已经结束，Agent 时代已经到来。"** Google 正在美国、伦敦、巴黎、香港等地大规模招聘 GenAI Forward Deployed Engineer，嵌入 Go-To-Market 团队，专门帮企业客户把 Gemini + Vertex AI 从 Demo 推到生产环境。

![三巨头 FDE 策略时间线对比](/assets/images/screenshot-20260518-fde-timeline.jpg)
<!-- baoyu-skill prompt: 2.35:1宽幅技术信息图。三巨头FDE时间线对比。从左到右三个里程碑模块发光排列：左侧OpenAI DeployCo红色"2026年5月11日 收购Tomoro 150名工程师 40亿美元融资"、中间Anthropic紫色"2026年5月4日 联合黑石高盛 15亿美元服务公司"、右侧Google Cloud蓝色"全球招聘数百FDE 800%岗位增长"。底部时间轴箭头标注"从卖模型到卖落地"。底部标语"三条路线 同一个终点：打通企业AI落地最后一公里"。深色科技背景。中文标注。 --ar 2.35:1 -->

**三条路线，同一个终点：打通企业 AI 落地的最后一公里。**

---

## 二、FDE 到底是什么？为什么不是传统顾问

很多人第一反应：这不就是 IT 咨询吗？派人进客户公司，帮忙搞系统集成，Accenture 和 Deloitte 干了几十年了。

不一样。**本质区别在于：传统顾问写 PPT、提建议、然后走人；FDE 写代码、交系统、而且反馈产品。**

FDE（Forward Deployed Engineer）这个概念最早由 Palantir 定义——把最强的工程师派到前线，直接在客户的环境里写代码、做集成、交付可运行的系统。不是"给建议"，是"一起建"。

![FDE 前线部署工程师角色解剖](/assets/images/screenshot-20260518-fde-role.jpg)
<!-- baoyu-skill prompt: 2.35:1宽幅技术信息图。FDE前线部署工程师角色解剖图。中央一个穿着工程师装备的人物形象，左手拿代码编辑器右手拿企业流程图。四条辐射路径连接四个核心职责：左上"驻场开发"蓝色编码图标、右上"系统集成"绿色齿轮图标、左下"安全合规"紫色盾牌图标、右下"反馈产品"金色回路箭头图标。底部对比：传统顾问灰色"写PPT提建议"叉号 vs FDE发光"写代码交系统"对号。底部标语"不是顾问而是共建者：FDE重新定义企业服务"。深色背景。中文标注。 --ar 2.35:1 -->

具体来看 FDE 的四大核心职责：

- **驻场开发**：进入客户环境，在客户的代码库、数据管线、安全边界里直接写生产代码
- **系统集成**：把 AI 能力接进客户的 CRM、ERP、审批流、权限系统——这些"脏活"才是真正的价值
- **安全合规**：帮客户搞定数据隐私、访问控制、审计日志，满足行业监管要求
- **反馈产品**：把前线踩的坑和发现的需求反馈给总部产品团队，推动模型和平台迭代

<mark><strong>FDE 不是外包，不是顾问，而是共建者。这也是为什么三巨头都在砸重金组建 FDE 军团——因为这个角色直接决定了企业 AI 能不能从"能用"变成"在用"。</strong></mark>

---

## 三、90% 的 AI 项目死在最后一公里

三巨头同时下场做"脏活累活"，不是巧合，是被逼的。

行业数据已经说明了一切：**绝大多数企业 AI 项目停留在 Pilot 阶段，真正进入生产环境的不到 10%。** 不是模型不行，是落地太难。

![企业 AI 落地的四大断裂带](/assets/images/screenshot-20260518-fde-gaps.jpg)
<!-- baoyu-skill prompt: 2.35:1宽幅技术信息图。企业AI落地的四大断裂带。四个红色警告模块横排：第一"遗留系统"老旧服务器与新AI系统之间断裂、第二"数据孤岛"多个数据库被高墙隔开、第三"安全合规"锁链与盾牌层层嵌套、第四"组织惯性"人员与流程抵抗变革。底部绿色解决方案条：FDE工程师像桥梁一样连接断裂带两端。底部标语"90%的AI项目死在最后一公里：不是模型不行，是落地太难"。深色背景红蓝对比。中文标注。 --ar 2.35:1 -->

企业 AI 落地有四道"断裂带"：

**遗留系统：** 企业不是从零开始的。十年前的 ERP、五年前的 CRM、三年前的中台——AI 要接进这些系统，光是搞清楚接口文档就够头疼了，更别说权限体系和数据格式的兼容。

**数据孤岛：** 销售数据在 Salesforce，财务数据在 SAP，客服数据在自研系统，产品数据在 Confluence——AI 需要打通这些孤岛才能发挥价值，但每个部门都在守着自己的数据堡垒。

**安全合规：** 金融行业要满足巴塞尔协议，医疗行业要满足 HIPAA，制造业有供应链安全标准——AI 不是接进去就完了，还要过层层合规审查。

**组织惯性：** 就算技术全部搞定，还有人的问题。中层管理者觉得 AI 威胁自己的岗位，一线员工觉得新工具增加学习成本，决策者觉得 ROI 不够明显——这些"软性阻力"往往比技术难题更致命。

**这四道断裂带，不是靠一个更强的模型就能填平的。需要的是人——能写代码、懂业务、有耐心的工程师，驻扎在客户那里，一个系统一个系统地接、一个流程一个流程地改。** 这就是 FDE 存在的意义。

---

## 四、三条路线，各有算盘

虽然终点相同，但三巨头的策略路径明显不同：

| 维度 | OpenAI DeployCo | Anthropic 合资公司 | Google Cloud FDE |
|------|----------------|------------------|-----------------|
| 模式 | 自建子公司 | 联合金融巨头合资 | 内部大规模扩招 |
| 资金 | 40 亿美元 | 15 亿美元 | 内部预算 |
| 团队 | 收购 Tomoro 150 人 | Applied AI 工程师 | 数百 FDE 岗位 |
| 目标客户 | 超大型企业 | 中型企业 + 投资组合 | GCP 企业客户 |
| 独特优势 | 全栈自研模型 + 部署 | 借金融巨头触达中型客户 | GCP 生态 + Gemini |

**OpenAI 的算盘：** 最直接——我自己下场，收购有经验的团队，从卖 API 升级到卖整套落地服务。优势是全栈自研，从模型到部署一条龙。

**Anthropic 的算盘：** 最巧妙——不自己组建庞大团队，而是借黑石和高盛的"投资组合公司"作为客户池。这些金融巨头旗下有成千上万家被投企业，Anthropic 等于拿到了现成的客户入口，而且 15 亿资本让这个模式可以快速规模化。

**Google 的算盘：** 最传统也最稳健——FDE 直接嵌入 Google Cloud 的 GTM 团队，利用已有的企业客户关系和 GCP 生态，把 Gemini 模型从实验室推到客户的生产环境。不成立独立公司，但 800% 的岗位增长说明投入力度不小。

---

## 五、对我们意味着什么

消息一出，社交媒体上就有人讨论：**"这不就是得否老板做的业务吗？"、"有点像 ERP Consultant 啊。"**

说对了一半。FDE 确实像 ERP Consultant 的升级版——但核心区别在于，传统 ERP 顾问帮企业实施已有的标准化软件，FDE 帮企业构建全新的 AI 原生系统。**一个是"配置"，一个是"创造"。**

![AI 行业竞争升级路线图](/assets/images/screenshot-20260518-fde-competition.jpg)
<!-- baoyu-skill prompt: 2.35:1宽幅技术信息图。AI行业竞争升级路线图。三个阶段从左到右：第一阶段灰暗"模型之战"GPT vs Claude跑分对比已过时、第二阶段蓝紫发光"生态之战"Agent SDK MCP CLI争夺正在进行、第三阶段金色明亮"落地之战"FDE驻场部署企业系统未来主战场。底部大箭头标注"竞争维度升级"。底部标语"AI竞争终局：谁能帮企业把能用变成在用"。深色背景渐变。中文标注。 --ar 2.35:1 -->

AI 行业的竞争已经经历了三个阶段：模型之战 → 生态之战 → **落地之战**。前两场战争的主角是研究员和开发者，第三场战争的主角是 FDE——那些能走进客户办公室、坐下来写代码、把 AI 真正嵌入业务流程的工程师。

我做 AI 落地已经三年了。三年前跟客户讲"AI 能改变你的工作流"，客户半信半疑。今天 OpenAI 砸 40 亿、Anthropic 砸 15 亿、Google 全球扩招数百人——**赛道被验证了，而且是被全球最聪明的钱验证的。**

<mark><strong>三巨头同时组建 FDE 军团，本质上是在告诉整个行业一件事：AI 竞争的终局，不是比谁的模型跑分高，而是比谁能帮企业把"能用"变成"在用"。谁打通了最后一公里，谁就拿到了这个时代最大的商业入口。</strong></mark>

---

## 写在最后

从年初写 [Agent 生态之战]({{ site.baseurl }}/openai-vs-anthropic-agent-ecosystem-war)，到上周写 [OpenAI 成立部署公司]({{ site.baseurl }}/openai-deployco-ai-deployment-company-b2b)，再到今天三巨头同时组建 FDE 军团——趋势越来越清晰：**AI 行业正在从"炫技"走向"干活"。**

对创业者来说，三巨头覆盖的是全球超大型客户。但中国有几千万家中小企业，它们的 AI 落地需求同样强烈——只是请不起 OpenAI 的前线部署工程师。**做某个垂直场景里的"小型 Deployment Company"，仍然是当下最确定的创业方向。**

我一个人打造的 [Zaokit AI 产品](https://zaokit.app) 已融入企业工作流，**2026 年 5 月 31 日前 1000 名用户赠送价值 150RMB 的 Pro 计划**，助力大家高效完成图文创作和 PPT 生成。唯一官方网站：[zaokit.app](https://zaokit.app)。

最后，如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入我们的社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

## 相关阅读

- [OpenAI 不只卖模型了：成立部署公司、收购 Tomoro，AI 下半场拼的是落地能力]({{ site.baseurl }}/openai-deployco-ai-deployment-company-b2b)
- [朴实无华的商战开始了：OpenAI 和 Anthropic 正面抢夺 Agent 生态入口]({{ site.baseurl }}/openai-vs-anthropic-agent-ecosystem-war)
- [一个人的 AI 军团：我用 Agent 完成了一整个 Team 的项目交付]({{ site.baseurl }}/ai-one-person-army-full-delivery-sequoia-agi)
- [深度测试 6 大 AI PPT 方案：企业生产场景，能打的只有 Zaokit]({{ site.baseurl }}/deep-test-6-ai-ppt-solutions-enterprise-only-zaokit)
