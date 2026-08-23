---
layout: post
title: "企业级 Harness Agent 落地实践指南——先接控制面，再谈内核"
date: 2026-08-23
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260823-enterprise-harness.webp
tags: [featured, AI, Harness, DeerFlow, Authing, Zaokit, Agent]
slug: enterprise-harness-agent-practice-guide
description: >
  企业落地的第一件事不是换更强的循环，而是把身份、用量、数据边界接到已经能干活的 Agent 上。
  一次 deerflow.zaokit.app 的实装：Authing SSO、算力中心按邮箱绑 KEY、会话隔离。先接控制面，再谈内核。
faq:
  - question: "Harness 和企业控制面是一回事吗？"
    answer: "不是。Harness 管工具循环、沙箱、会话日志；企业控制面管 SSO、按人用量、审计、配额。办事 Agent、编码 Harness、企业控制面是三层，别混买。"
  - question: "配了 Authing OIDC，用户就会走 SSO 吗？"
    answer: "不一定。我们这周踩过：落地页仍是邮箱登录，Authing 在次入口。企业站要把 / 和干净的 /login 指到 IdP，只有 ?error=sso_failed 才回邮箱页。"
  - question: "上了登录，是不是每人一台机器？"
    answer: "不是。DeerFlow 现在有的是会话、文件、记忆按 user_id 隔离；执行仍是 LocalSandboxProvider + 宿主机 bash。看见的隔离，不等于跑着的隔离。"
  - question: "该不该在 DeerFlow 后台给每人开一把模型 KEY？"
    answer: "不该。模型 KEY 在全局 config.yaml，设置页没有这功能。正确做法是算力中心按人建 Token，运行时按 SSO 邮箱覆盖 api_key；映射放服务器 0600 文件，不进 git、不进聊天。"
---

这周把 deerflow.zaokit.app 的 Authing、按邮箱绑 KEY、会话隔离走通了一遍。不是评测文。是一条能复用的路径。

> **企业落地的第一件事不是换更强的循环，而是把身份、用量、数据边界接到已经能干活的 Agent 上。Model + Harness = Agent；企业还要再加 Identity、Metering、Isolation。**

![先接控制面，再谈内核](/assets/images/cover-20260823-enterprise-harness.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平封面，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。机器人手持「身份」「用量」「隔离」三块牌，身后「更强循环」齿轮打叉。顶部粗体中文「先接控制面」，底部小字「再谈内核」。中文清晰可读。 --ar 2.35:1 -->

## 先分清三层，别买错东西

写成三层，别写成厂商清单。

| 层 | 解决什么 | 成熟代表 | 我们现在 |
|---|---|---|---|
| 办事 Agent | 调研、长任务、工作区、会话 | DeerFlow / Suna | deerflow.zaokit.app 已上 |
| 编码 Harness | 工具循环、沙箱、会话日志、改仓库 | Claude Code / Codex / OpenHands | 未上，下一期再选 |
| 企业控制面 | SSO、按人用量、审计、配额 | Authing + cc.zaokit.ai | SSO 已通，KEY 映射已埋 |

DeepSeek Harness 属于编码层。2026-08-13 开源，官方写的是 developer preview。插件化方向对，还不能当企业底座。LangGraph、AutoGen 是编排框架，别和 Harness 混写。

![先分清三层](/assets/images/illust-20260823-three-layers.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。三层架子：办事 Agent、编码 Harness、企业控制面，机器人指着底层。顶部粗体中文「先分清三层」，底部小字「别拿框架当底座」。中文清晰可读。 --ar 2.35:1 -->

## 选型：先用已经能跑的办事层

我们这周的判断很死：不自研一套 Grok Bot，不把 Suna 并进现网，不把 DeerFlow 先包进 RFC Work。

线上已经有 deerflow.zaokit.app。模型已经走 cc.zaokit.ai，GPT-5.5 和 Claude Sonnet 4.6 都在。缺的是 Authing 和按人记账，不是再写一套循环。

原则只有三条：一个生产入口，一个身份源，一个算力入口。第四套内核不进本期。

## 身份：企业站必须默认走 IdP

配了 OIDC，不等于用户会走 SSO。这是这周踩过的第一坑。

落地页仍是邮箱登录，Authing 藏在次入口。企业站要把 `/` 和干净的 `/login` 指到 IdP。只有 `?error=sso_failed` 才回邮箱页，否则死循环。

第二坑在验签，不在授权码。Token 换到了，回调照样挂。Authing 默认 HS256，DeerFlow 上游只认 RS/ES。我们和 RFC Work 共用用户池，IdP 改成 **RS256** 比改业务代码干净。RFC Work 两边算法都认。

第三件：SSO 用户自动建号，角色是 `user`，进来是空工作区。别默认把历史 thread 挂到新邮箱上。

![企业站默认走 IdP](/assets/images/illust-20260823-sso-entry.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。大门「IdP / SSO」，小门「邮箱登录」挂牌「sso_failed」，机器人指路。顶部粗体中文「企业站默认走 IdP」，底部小字「配了 OIDC 不等于会走」。中文清晰可读。 --ar 2.35:1 -->

## 隔离：先写「看见的」，再写「跑着的」

上了登录，不等于每人一台机器。必须拆开写，否则读者会把能力写进合同。

**已经有的：** 会话 `threads_meta.user_id`；文件 `.deer-flow/users/{user_id}/...`；记忆 `strict_user_scope`。别人的 thread 是 404。

**还没有的：** 沙箱仍是 `LocalSandboxProvider` + 宿主机 bash。UI 互不可见，执行环境共用一台机。角色只有 admin / user，没有部门、项目 RBAC。

这些写进能力边界，别写成已交付。

![看见的不等于跑着的](/assets/images/illust-20260823-isolation.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。两侧玻璃房「看见的隔离」，中间机房「执行仍共用」。顶部粗体中文「看见的，不等于跑着的」，底部小字「会话隔离 ≠ 机器隔离」。中文清晰可读。 --ar 2.35:1 -->

## 用量：KEY 不进产品后台

这章最有实践含量。

DeerFlow 设置页不能给每人开通模型 KEY。KEY 在全局 `config.yaml`。

正确做法：算力中心按人建 Token；运行时按 **SSO 邮箱** 覆盖 `api_key`。映射放服务器 `0600` 文件，不进 git，不进聊天。

未绑定的人，试运行阶段可以暂时回落共用 KEY。企业正式启用后，应改成未绑定就拒绝。

业务用户不要自己到产品里粘贴 KEY。

![KEY 不进产品后台](/assets/images/illust-20260823-metering.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。算力中心金库按邮箱发个人令牌，产品后台「粘贴 KEY」打叉。顶部粗体中文「KEY 不进产品后台」，底部小字「按邮箱覆盖用量」。中文清晰可读。 --ar 2.35:1 -->

## 部署：tryout 可以在宿主机，隔离必须进容器

写动机，别写「Docker 更好」这种空话。

本周是 systemd tryout：`/opt/tryout/deer-flow`，网关 `127.0.0.1:18001`，前端 `13000`，和 RFC Work 同机，盘已经紧。

网关进容器，解决不了「每人一台执行环境」。该容器化的是 sandbox，不是先把 Next / uvicorn 塞进镜像。

原则：控制面可以留在宿主机；执行面要 Docker / K8s，才算企业隔离。

## 编码层什么时候补

点到为止。

| 产品 | 状态 | 企业怎么用 |
|---|---|---|
| Claude Code | 最成熟闭源循环 | 复杂改仓库；绑 Anthropic |
| OpenAI Codex | CLI + 云沙箱 + 开源 runtime | 和现有算力中心最好接 |
| OpenHands | 开源自托管里最成熟 | 要 Docker 沙箱、VPC 时优先 |
| DeepSeek Harness | 2026-08-13 开发者预览 | 可跟，不当本期底座 |

要复杂改仓库：Claude Code。要接现有算力、要可审计循环：Codex 开源 runtime。要自托管加 Docker 沙箱：OpenHands。本期不叠第四套。

## 反模式，和下一期只留三件

容易写成错的句子：

- DeepSeek Harness 已经是企业级底座
- DeerFlow 后台可以给每人开通 KEY
- 上了 SSO 就有机器级隔离
- 应该再并一套 Suna / 自研第四内核
- 让业务用户自己去产品里粘贴 API Key

下一期只写三件，避免指南散成路线图：

1. 算力中心按人 Token 写完映射，未绑定可选择拒绝
2. 执行隔离换 Docker / K8s sandbox；网关可以继续留在宿主机
3. 若要编码循环，在 Codex 开源 runtime 和 OpenHands 里二选一

## 写在最后

压成五句：

1. **先接控制面**——Identity、Metering、Isolation 接到已经能干活的 Agent 上，再谈更强循环
2. **三层别混买**——办事 Agent、编码 Harness、企业控制面；DeepSeek Harness 是预览，不是底座
3. **身份默认走 IdP**——`/` 指到 SSO；HS256 改 RS256；新用户空工作区
4. **看见的隔离 ≠ 机器隔离**——thread/文件/记忆按人；bash 仍是宿主机
5. **KEY 留在算力中心**——按邮箱覆盖；产品不存 KEY；下一期只补三件

土话一句：

**先把门锁好、电表装上、房间分清，再谈要不要换发动机。**

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

延伸：[Grok Bot 接手了创意策略师和 Marketing](/grok-bot-takes-creative-marketing) · [Grok Bot 被严重低估了——我把股票实盘交给了它](/grok-bot-stock-trading-agent) · [Grok Bot：一人公司第一次被做成了产品](/grok-bot-one-person-company)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。企业 Agent 先接控制面——门锁、电表、房间，比发动机更贵。*
