---
layout: post
title: "网页自己报工具：WebMCP 这周被 OpenAI 推上台"
date: 2026-08-27
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260827-webmcp.webp
tags: [featured, AI, WebMCP, MCP, OpenAI, Chrome, Agent, Harness, Zaokit]
slug: webmcp-openai-this-week
description: >
  AI 助手上网还在瞎点按钮。WebMCP 让网页主动告诉 AI「我这里能结账、能筛选」，不用它自己猜。
  OpenAI 这周把这个能力接进 ChatGPT 和 Codex，还办了一场 10 天比赛推广。技术还没定型，安全还得人盯。
faq:
  - question: "WebMCP 是什么？一句话解释"
    answer: "网页主动告诉 AI 助手「我这里有哪些功能可以用」，比如结账、筛选、查状态。AI 不用再猜按钮在哪。"
  - question: "OpenAI 这周到底发了什么？"
    answer: "8 月 25 日，OpenAI 联合 Chrome、Cloudflare、Shopify 等办了一场 10 天比赛。同时 ChatGPT 桌面版和 Codex 已经能自动识别支持 WebMCP 的网站，直接调用网页提供的功能。"
  - question: "现在普通人能用吗？"
    answer: "还早。标准还是草稿，Chrome 浏览器需要手动开启实验功能才能用。Firefox、Safari 还没动静。"
  - question: "安全吗？会不会被乱扣钱？"
    answer: "花钱、下单这类操作必须弹窗让你确认。但 AI 助手会带着你的登录身份去操作，所以网站要靠谱，你自己也要看着点。"
---

你有没有让 AI 助手帮你操作网页的经验？

比如让它帮你订机票、填表格、查物流。结果呢——它截屏看半天，猜错按钮，填错信息，碰上个弹窗广告直接傻掉。

这周 OpenAI 把一个叫 [WebMCP](https://webmachinelearning.github.io/webmcp/) 的东西推上了台。不是新的 AI 模型，是一种让网页**主动告诉 AI 助手「我这里能干什么」**的方法。

我的判断很简单：

**网页自己报菜单，AI 少猜。但花钱、下单这种大事，还是得你自己拍板。**

![网页自己报工具](/assets/images/cover-20260827-webmcp.webp)

## 以前：AI 在网页上像个瞎子

你让 AI 助手帮你在一个购物网站下单。它看到的是什么？一堆文字、图片、按钮，和你看到的一样——但它不知道哪个按钮是「结账」，哪个是「加入收藏」。它只能猜。

猜对了，帮你省事。猜错了，可能把东西删了。

更惨的是，碰到复杂页面——比如多步骤的预约、嵌在菜单深处的功能——AI 根本找不到入口。

![别再瞎点](/assets/images/illust-20260827-no-blind-click.webp)

## 现在：网页主动递菜单

[WebMCP](https://developer.chrome.com/docs/ai/webmcp) 的思路很简单：**不让 AI 自己猜，让网页主动说。**

打个比方。以前 AI 去餐厅，得自己翻遍整个厨房才知道能点什么菜。现在呢，服务员直接把菜单递过来：「结账在这，筛选在这，查订单状态在这。」

AI 照着菜单点，不用再满屋子翻。你在浏览器里全程看得见它在干什么，品牌和操作体验还是网站自己的。

花钱、改账户这种敏感操作？网页可以设成必须弹窗让你确认，AI 不能偷偷干。

## 它和之前的 MCP 不是一回事

你可能听过 MCP 这个词。之前的 MCP 是给后台服务器用的——AI 通过网络连接调用远程工具。

WebMCP 不一样，它跑在你的浏览器里。[规范](https://webmachinelearning.github.io/webmcp/)是 2026 年 8 月 26 日写的草稿，还不是正式标准。

简单理解：**MCP 是厨房后门递菜，WebMCP 是前厅服务员递菜单。** 一个在后台，一个在你眼前。

目前只有 Chrome 浏览器能用，而且还要手动打开实验开关。Firefox、Safari 还没动静。

AI 助手得先打开这个网站，才知道它有没有提供菜单。你不打开，它就不知道。

![不是后端 MCP](/assets/images/illust-20260827-not-backend-mcp.webp)

## OpenAI 这周干了什么

这个技术是 Google、微软那边的人先做的。但 OpenAI 这周做了一件更重要的事：**让普通人能用上。**

8 月 25 日，OpenAI 联合 Chrome、Cloudflare、Shopify 等大厂，办了一场 [10 天比赛](https://openai.com/webmcp-challenge/)。奖金 3.5 万美元，还送 Codex 和一年 ChatGPT Pro 会员。截止 9 月 3 日投稿，9 月 23 日公布 10 个获奖作品。

更关键的是，同一天 ChatGPT 桌面版的内置浏览器直接支持了这个功能。如果你用 ChatGPT 打开一个支持 WebMCP 的网站，它能自动发现这个网站提供了哪些功能，直接帮你用。

你和 AI 看的是同一个网页、同一个已登录的页面。它不是在后台偷偷操作，而是在你眼皮底下干活。

![OpenAI 这周推上台](/assets/images/illust-20260827-openai-push.webp)

## 网上吵成两派，我站中间

OpenAI 在 X（原推特）上开了 [直播](https://x.com/i/broadcasts/1qGoNYbWdkvKv)，[社区讨论](https://daily.dev/posts/openai-and-partners-launch-a-10-day-webmcp-hackathon-54bqootzg)也很热。

**看好的人说**：网页主动告诉 AI 能干什么，总比 AI 自己瞎猜靠谱。有人在论坛写：调用定义清楚的功能，比让 AI 自己在页面上摸索稳多了。

**看衰的人说**：说到底还是让 AI 操作网页，只是换了个方式。万一出了问题谁负责？各家浏览器会不会搞出不兼容的版本？有人吐槽：这不就是「给懒得自己点网页的人做了个自动完成」吗。

我站中间。

有菜单总比瞎猜好。但标准还在改、浏览器还没全支持。真要在正式业务里用，身份验证、操作记录、出错回滚——这些比赛奖金可解决不了。

比赛规则倒是认真的：必须开源代码、交 3 分钟视频演示。这才像真要做东西，不是又一个 PPT。

## 方便归方便，安全你得盯着

标准文件自己都把风险写得很清楚。

最大的问题：**AI 助手会带着你的登录身份去操作。** 你登录了淘宝，AI 就能以你的身份在淘宝上做事。

几个要注意的：

- 网页说「帮你整理购物车」，背后可能偷偷下单
- AI 在操作过程中可能把你的个人信息（地址、年龄）泄露给网站
- 网页可以在返回结果里「夹带私货」，误导 AI 去做别的事

所以 Chrome 也建议：花钱的操作一定要弹确认。先让网页只提供查询类功能，能花钱、能改东西的功能慢慢放开。

我在企业里做 AI 落地，看的也是这一层。Zaokit AI Gateway 管 AI 从哪个入口进来，Token Hub 管每个人的用量，Guard 管不该说的别说。网页把功能交出去之后，这些安全围栏不能缺。

![工具交出去，门禁还是人守](/assets/images/illust-20260827-user-control.webp)

## 写在最后

WebMCP 的意思很简单：以前 AI 上网靠猜，现在网页主动递菜单。OpenAI 这周把这个能力接进了 ChatGPT，还办了一场比赛推广。

但别着急——

标准还在改。浏览器还没全支持。AI 带着你的身份在网上操作，出了事还是算你的。

**一句大白话：菜单可以让服务员报，钥匙别交给服务员保管。**

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

*我是 Jason，自己一个人做 AI 产品。网页可以把工具交出去，钥匙还是人拿着。*
