---
layout: post
title: "桌子对面没有人"
date: 2026-08-28
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260828-one-person-company-story.webp
tags: [featured, AI, 一人公司, Zaokit, 寻绎, Agent, 创业, Cowork]
slug: one-person-company-story
description: >
  2023 年注册了一家公司。三年后桌子对面还是没有人，但屏幕上已经有 Agent 在跑了。
  这是一个人怎么从一把 API Key，做到 Zaokit AI PPT、Cowork 数字同事、AI Gateway、Token Hub、Guard 的过程。
faq:
  - question: "一人公司是不是什么都自己干？"
    answer: "不是。人守客户、判断和担责。研究、创作、开发、交付写进 Agent 的编制。最小组织单位变成一个人加一群 Agent。"
  - question: "Zaokit 做了哪些产品？"
    answer: "面向创作的 Zaokit AI PPT（zaokit.app），面向协作的 Zaokit Cowork（cowork.zaokit.app），面向企业的 AI Gateway、Token Hub、Guard，外加私有化算力和企业级 Agent。"
  - question: "企业客户一般先接哪块？"
    answer: "先把 Gateway 和 Token Hub 接好，管住模型入口和用量。再上 Guard 做合规。最后让 Agent 进生产。控制面先于坐席。"
  - question: "怎么联系？"
    answer: "个人站 junxinzhang.com，公众号 Just Jason。产品入口 zaokit.app / zaokit.ai。企业落地后台留言即可。"
---

2023 年 7 月，手机收到一份电子营业执照：上海寻绎信息科技有限公司。"寻绎"——寻找线索，发现价值。

那天回到家，桌上和前一天一样：一台电脑，一杯凉掉的咖啡。

我打开电脑，开始写代码。

![桌子对面没有人](/assets/images/cover-20260828-one-person-company-story.webp)

## 2023

之前的工作是企业架构师。帮客户管三百多条 CI/CD 流水线，给五十几套系统统一做 SSO，部署效率提了 90%，故障响应缩短 90%。帮公司管着三千万一年的生意——需求、开发、交付、运营、运维，就我一个人。

离开的时候什么都没带走。三年多，一份补偿没要。技术留在上家公司的内网里，人干干净净走了。

ChatGPT 出来的第一天我就订阅了。一个账号，到现在变成五个。

注册公司不是为了融资。是为了开发票。

第一个客户还没有。第一个产品也没有。有的是一条宽带和一把 API Key。

我打开电脑，写第一行代码。

大部分代码是凌晨两点以后提交的。天亮了，接着写。

桌子对面没有人。

![从客户的话里找线索](/assets/images/illust-20260828-find-clues.webp)

## 第一个产品

客户要出一份演示文稿。以前的流程我见过——设计改五遍，文案两遍，排版再来一遍，三天交不出。

我把这条流水线写进了代码，接上大模型。输入一段需求，三分钟，.pptx 生成了。封面、正文、排版，直接下载。

[Zaokit AI PPT](https://zaokit.app) 上线的时候，后台用户数是零。

没投过广告。第一个用户是搜索引擎带来的。第二个也是。

后来图文加进去了。公众号封面、小红书套图、文章插图——输入一段文字，选个风格，出来一整套能发的东西。八种语言，直连微信和小红书。定价四档，最高 $49.99/月。

以前一个小团队做这套内容要三天。设计改五遍，文案两遍，排版再来一遍。

现在从输入到下载，几分钟。

每天早上，我打开电脑，看一眼后台。数字比昨天多了一点。

桌子对面还是没有人。

## 数字同事

用户在后台留言：能不能让 AI 帮我做研究？能不能跟进项目？能不能不是回答完一个问题就消失，而是接一整段活，交一个结果？

我写了 [Zaokit Cowork](https://cowork.zaokit.app)。

AI 从工具变岗位。每个岗位有名字。Creative Strategist 出广告创意。bingoJob 往 Telegram 发素材。策略分析交给 StrategyBot。竞品调研交给 ResearchAgent。

给它们起名字的时候，我停了一下。以前在企业里，新来一个同事也是先写进花名册，分个工位。

现在花名册上写的全是 Agent 的名字。

早上我打开电脑，有几个 Agent 的任务已经跑完了。结果放在那里，等我看一眼、批一下。

桌子对面还是没有人。但屏幕上，有人在干活了。

![一排 Agent 坐上了工位](/assets/images/illust-20260828-agents-on-desk.webp)

## 企业来了

2024 年，开始有企业找过来。

第一个客户进门说的不是"AI 行不行"。说的是："Key 在微信群里传，有人离职了还能用。十几个人各用各的，月底账单到了，几万块，谁花的花在哪，说不清。"

第二个更直接："合规部说了，客户数据不能过公网。模型必须跑在自己机房。但搭算力的和用模型的是两拨人，中间没人管。"

第三个："三个部门各接了一家模型，各有各的账号。统一？没人干这事。"

三个问题我都接了。

[Zaokit AI Gateway](https://grok.zaokit.com)——模型从哪进来，走哪条路，出了事一键关。以前搭 CI/CD 管的是代码流水线，现在管模型调用。逻辑一样，对象换了。

[Zaokit AI Token Hub](https://tokenhub.zaokit.ai)——谁调了什么，花了多少，额度剩多少。电表装在公司手里，月底账单对得上。

Zaokit AI Guard——不该说的不说，不该出域的不出，该拦的自动拦。

加上私有化算力和企业级 Agent，[cx.zaokit.com](https://cx.zaokit.com)、[cc.zaokit.com](https://cc.zaokit.com) 跑着企业服务入口。[完整产品清单](https://junxinzhang.com/projects.html)在官网上。

客户用这套系统的时候，不知道背后是一个人。

他们不需要知道。

![企业要的不是聊天窗](/assets/images/illust-20260828-enterprise-infra.webp)

## 三年零一个月

2023 年 7 月到 2026 年 8 月。

[Zaokit AI PPT](https://zaokit.app)。[Cowork](https://cowork.zaokit.app)。[Agent 交易平台](https://zaokit.ai)。Gateway。Token Hub。Guard。私有化算力。企业级 Agent。275 篇博客。12 个开源项目。[gift.junxinzhang.com](https://gift.junxinzhang.com) 还跑着一个 Apple 礼品卡的小生意。

全从同一张桌子上出来的。

桌子和三年前一样。一台电脑，一杯咖啡。

今天早上我打开电脑，屏幕上已经有几个 Agent 在跑了。有一个在帮客户出图文，有一个在跑策略分析，还有一个刚完成了一轮企业的合规扫描。

结果排在那里，等我批。

![三年，一张工位](/assets/images/illust-20260828-three-years.webp)

## 写在最后

外面管这个叫"一人公司"。

准确一点：一个人加一群 Agent。人守客户、守判断、守担责。研究、创作、开发、交付，写进 Agent 的编制。

以前做架构师，三百多条流水线的经验就一句话：流程标准化，写进系统里跑，人只管例外。

现在做公司，一模一样。

"寻绎"两个字，注册那天选的。三年了，每接一个客户，还是先做同一件事——从他们的话里找线索，把线索做成能交货的东西。

**桌子没换过。桌子上跑的东西，全换了。**

---

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

数据不能出域？试试 [Cowork](https://cowork.zaokit.app)——AI 直接帮你交付任务，支持企业私有化部署，数据留在你自己的服务器里。

企业侧同一逻辑，已经融进可直接接入的服务：

- **NEW** [cowork.zaokit.app](https://cowork.zaokit.app) — AI 任务交付，私有化部署，数据不出域
- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[公司的最小单位，变成了一个人加一群 Agent](/one-person-plus-agents) · [数字员工上岗之后，最值得攒的是这几类岗位](/digital-employee-roles-worth-keeping) · [企业级 Harness Agent 落地实践指南](/enterprise-harness-agent-practice-guide)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。桌子没换过。桌子上跑的东西，全换了。*
