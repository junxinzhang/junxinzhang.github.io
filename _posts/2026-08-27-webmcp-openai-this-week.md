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
  WebMCP 不是后端 MCP。网页在浏览器标签里自己报工具，Agent 少瞎点。
  OpenAI 这周用 Codex、ChatGPT 桌面浏览器和一场 10 天 hackathon 把它推上台。协议还是草稿，门禁还是人守。
faq:
  - question: "WebMCP 和 MCP 是一回事吗？"
    answer: "不是。MCP 是后端协议，走 HTTP / SSE / stdio。WebMCP 跑在浏览器标签里，页面自己当工具注册表，目前只支持 Tools，没有 Resources 和 Prompts。"
  - question: "OpenAI 这周到底发了什么？"
    answer: "8 月 25 日开了 WebMCP Challenge，和 Chrome、Cloudflare、Shopify、Vercel、Render、Netlify 一起办 10 天黑客松。ChatGPT 桌面浏览器和 Codex 把 WebMCP 做成 Site tools，碰到兼容站点可以自动调用。"
  - question: "现在能上生产吗？"
    answer: "还早。规范是 8 月 26 日的 W3C Community Group 草稿，Chrome 要开 flag 或走 origin trial。先报只读工具，付购买、改账这类动作必须人确认。"
  - question: "和企业落地有什么关系？"
    answer: "工具交出去以后，身份、会话、隔离还是人守。Agent 会继承登录态，描述和真实行为可以对不上。这和 Harness 那篇同一件事：先接控制面，再谈更强循环。"
---

Agent 还在网页上瞎点。

截图、猜按钮、填错表。一页广告，它就迷路。

这周 OpenAI 把 [WebMCP](https://webmachinelearning.github.io/webmcp/) 推上台。不是新模型。是网页自己报工具。

我的判断很死。

**页面把 `checkout`、`filter_results` 交出去，Agent 少猜。门禁、会话、最后一刀，还是人守。**

![网页自己报工具](/assets/images/cover-20260827-webmcp.webp)

## 别再让 Agent 在页面上猜

Chrome 文档写得很直：[WebMCP](https://developer.chrome.com/docs/ai/webmcp) 让站点用 JavaScript，或给表单加标注，把功能报成带 JSON Schema 的工具。

左边是刮 DOM、看按钮。右边是调用 `checkout`。预约、多城行程、嵌在菜单里的诊断，都能少走几步。敏感动作可以弹确认。

工具在页面上跑，人看得见。品牌和交互还在你手里。

![别再瞎点](/assets/images/illust-20260827-no-blind-click.webp)

## 它不是后端 MCP

名字带 MCP，容易听成又一个服务器。

[规范](https://webmachinelearning.github.io/webmcp/) 写在 2026 年 8 月 26 日，W3C Web Machine Learning Community Group 的草稿，不是正式标准。页面可以看成「在客户端脚本里实现工具的 MCP 服务器」。

关键差别钉死：

跑在浏览器标签里。不走 HTTP、SSE、stdio。
目前只有 Tools，没有后端 MCP 的 Resources、Prompts。
入口是 `document.modelContext.registerTool()`，表单也能用声明式标注。
要 HTTPS，要源隔离，权限策略默认 `tools=self`。跨源 iframe 得写 `allow="tools"`。

Chrome 本地要开 `chrome://flags/#enable-webmcp-testing`。文档说 origin trial 从 Chrome 149 开始。Firefox、Safari 还没有时间表。

设计给「人在环上」的本地浏览器，不是无头机房。Agent 还得先打开这个站，才知道有没有工具。

![不是后端 MCP](/assets/images/illust-20260827-not-backend-mcp.webp)

## OpenAI 这周推上台的，是分发

协议是 Google、Microsoft 那边的人先推的。Chrome 文档 5 月 18 日上线，8 月 7 日改过一版。

OpenAI 干的是把它送进人手里。

8 月 25 日，[WebMCP Challenge](https://openai.com/webmcp-challenge/) 开张。Chrome、Cloudflare、Shopify、Vercel、Render、Netlify 一起办 10 天黑客松。奖金 3.5 万美元，外加 Codex Micro、一年 ChatGPT Pro。投稿截止官方页写 9 月 3 日太平洋时间下午 1 点，9 月 23 日公布 10 个赢家。

同一天，ChatGPT 桌面内置浏览器和 ChatGPT Sites 接上 **Site tools**。OpenAI 自己的说法：这就是他们对 WebMCP 草案的实现。人和 Agent 对着同一张已登录的活页。碰到兼容站点，ChatGPT Work 和 Codex 可以自动发现、调用。

Codex 也能直接起一个带 WebMCP 的应用，部署到 Sites。

![OpenAI 这周推上台](/assets/images/illust-20260827-openai-push.webp)

## X 上两边都有，我站中间那句

OpenAI Developers 在 X 上开了 [开播](https://x.com/i/broadcasts/1qGoNYbWdkvKv)。社区帖也钉在论坛首页。

X 上这几天的味道，和 [daily.dev 汇总的讨论](https://daily.dev/posts/openai-and-partners-launch-a-10-day-webmcp-hackathon-54bqootzg) 对得上：报名的人多，也有人嫌报名链接、截止时间对不上。StefanoGPT 当众问过：官网写 9 月 3 日下午 5 点 PT，Devpost 写下午 1 点。

真正吵的不是奖金。

一边觉得，网页交工具，Agent 少靠脆的浏览器自动化。论坛里 proflead 就写：直接调定义清楚的工具，比只靠页面跳转稳。

另一边觉得，这是换皮的浏览器自动化。授权范围、回滚、可观测、各家运行时会不会各写一套，都没答完。有人把整场黑客松读成「给讨厌多开标签页的人做自动完成」。

我站中间那句。

工具契约比瞎点强。协议还是草稿，Chrome 要开 flag。生产上的身份、回滚、审计，hackathon 奖金买不来。

OpenAI 社区里有人把规则抠完：必须开源、还要交 3 分钟视频。这才像真要交东西，不是再发一篇演示。

## 工具交出去，门禁还是人守

规范自己把风险写进了第 6 章。

Agent 会继承你的登录态。工具描述可以写「整理购物车」，真实行为是下单。返回值里能塞进提示词，把 Agent 拐走。参数开多了，站点能从 Agent 嘴里掏出年龄、住址、跨站画像。

8 月 23 日那篇写过：企业落地先接身份、用量、隔离。WebMCP 把同一道题搬到浏览器里。

页面报工具，是执行层。谁能调、调的是不是登录后的高权操作、付购买要不要人点，是控制面。

Chrome 也写了：购买这类动作，让工具弹出确认。先报只读工具，再报能改状态、能花钱的。

我在企业里落地 Harness，看的也是这一层。Zaokit AI Gateway 管模型从哪进，Token Hub 管按人计量，Guard 管不该出的别出。网页把工具交出去以后，这三块不能空。

![工具交出去，门禁还是人守](/assets/images/illust-20260827-user-control.webp)

## 写在最后

WebMCP 把「Agent 怎么用网页」从刮页面，改成页面自己报菜单。OpenAI 这周用 Codex、桌面浏览器和一场黑客松把它送进人手里。

别把报名当落地。

协议还在改。浏览器还没齐。Agent 带着你的 cookie 调工具，出了事问的是你。

土话一句：菜单可以交给伙计报，钥匙别交给伙计保管。

---

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

延伸：[公司的最小单位，变成了一个人加一群 Agent](/one-person-plus-agents) · [数字员工上岗之后，最值得攒的是这几类岗位](/digital-employee-roles-worth-keeping) · [企业级 Harness Agent 落地实践指南](/enterprise-harness-agent-practice-guide)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。网页可以把工具交出去，钥匙还是人拿着。*
