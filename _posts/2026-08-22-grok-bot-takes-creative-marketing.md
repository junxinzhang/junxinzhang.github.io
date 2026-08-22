---
layout: post
title: "Grok Bot 接手了创意策略师和 Marketing"
date: 2026-08-22
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260822-grokbot-roles.webp
tags: [featured, AI, Grok, Grok Bot, BingoJob, Marketing, Zaokit]
slug: grok-bot-takes-creative-marketing
description: >
  2026-08-22，我把公司两个岗位交给了 Grok Bot：Creative Strategist 做美素佳儿广告，bingoJob 往 Telegram 发 BingoJob 招聘素材。
  我只批最后一刀。岗位还在，坐上去的是 Bot。
faq:
  - question: "这两个 Bot 分别干什么？"
    answer: "Creative Strategist 拆卖点、出图出文；bingoJob 把 BingoJob 的痛点和卖点做成广告，发到 Telegram @info_bingojob，并标明 AI 发出、等人确认。"
  - question: "人还要不要上手？"
    answer: "要。Bot 把图和文送到频道或动态里，最后一刀还是我点同意。今天 BingoJob 那组还按反馈改了官方 Logo 和高棉语文案，再发一次。"
  - question: "和昨天写的「一人公司」是什么关系？"
    answer: "昨天说的是编制。今天是编制落地：两个岗位写进名字，活真的从我桌上挪走了。"
  - question: "文中截图脱敏了吗？"
    answer: "脱敏了。联系人、私聊细节做了模糊；留下的是工作流本身：出图、发频道、等人确认。"
---

昨天我说 Grok Bot 把一人公司做成了产品。今天把编制写进名字了。

Creative Strategist。bingoJob。两个岗位，两台工位，活从我桌上挪走。

> **岗位还在。坐上去的是 Bot。我只批最后一刀。**

![两个岗位交给 Bot](/assets/images/cover-20260822-grokbot-roles.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平封面，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。两台工位牌「创意策略师」「Marketing」，机器人落座，空椅子在后。顶部粗体中文「两个岗位交给 Bot」，底部小字「我只批最后一刀」。中文清晰可读。 --ar 2.35:1 -->

## 策略岗：先拆痛点，再一起交图文

今天上午，Creative Strategist 接到的活很具体：皇家美素佳儿 Friso Prestige，围绕 TrackEasy 溯源和荷兰自家牧场，出一组广告。

它没有先问我要 Slogan。先把卖点拆开：荷兰牧场、罐底扫码、全程可见。再按这个故事连出图和文。整整 10 张 Friso Prestige / TrackEasy 的 16:9 KV，图文成套，不是半成品丢给我拼。主题是溯源揭示、荷兰牧场、扫码安心、供应链旅程、产品英雄图、生活方式、实验室质检、荷兰信任、3段成长、TrackEasy App。

中文文案也跟着这条线走。痛点写的是真假难辨、产地说不清、检测看不懂、换奶怕踩雷、贵也不透明；卖点落到 TrackEasy 全链路、荷兰自家牧场、3段 12–36月龄、严格检测、看得见的安心。

![策略岗在拆卖点](/assets/images/illust-20260822-strategist-desk.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。机器人手持「痛点」「卖点」便签，对面画板交出图文。顶部粗体中文「策略岗在拆卖点」，底部小字「图和文一起交」。中文清晰可读。 --ar 2.35:1 -->

其中一张成片长这样。罐底扫码，溯源链路摊开。文案也跟着这条线走。

![美素佳儿 TrackEasy 成片（脱敏工作流产出）](/assets/images/shot-20260822-friso-creative.webp)

发货也不走我。图和文先走 Telegram 网页端进 clawbot 线程，上传不稳，改用 Telegram Desktop 才发完。再落到 Facebook，Junxin Zhang 动态上是同一套中文文案加这 10 张图。平台上直接打了「AI 内容」标签。联系人那边我做了模糊，留下的是这条链路：出图 → 发频道 → 上动态。登录和 2FA 不代填，我在桌面登完再继续。

![Facebook 动态（联系人已脱敏）](/assets/images/shot-20260822-friso-facebook.webp)

![clawbot 频道里的图文套装（侧栏已脱敏）](/assets/images/shot-20260822-friso-clawbot.webp)

策略岗以前要开会、改三版、再等设计师。现在是：一句话交代品牌故事，成套素材回来等人看。

## 营销岗：痛点做成广告，发完等人点头

bingoJob 这个 Bot 的职位写得很死：把产品痛点做成广告（文案+素材），发到 Telegram [@info_bingojob](https://t.me/info_bingojob)。

产品是 [BingoJob.AI](https://bingojob.ai/)——柬埔寨这边的 AI 招聘。求职端 Kaka AI 走 Telegram，雇主端做 AI 筛选。流程也写死：先扒 bingojob.ai，拆痛点和卖点写出 caption，GenerateImage 出图，再用 Pillow 叠上官方 logo lockup，最后走 Telegram Desktop 发出去。不走网页端，也没有 Telegram MCP。

第一批发了大约十张中英广告，进的是对接人私聊：bingojob-人力招聘 / nico li，也就是 t.me/info_bingojob。每条带【痛点】【卖点】，末尾写清楚：AI Agent 主动发出，请人工确认。

![营销岗在发货](/assets/images/illust-20260822-ship-confirm.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平插画，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。机器人把广告卡塞进标「确认后发出」的纸飞机信箱。顶部粗体中文「营销岗在发货」，底部小字「AI 发出，人点确认」。中文清晰可读。 --ar 2.35:1 -->

对方说可以，但公司 logo 要固定，还要支持高棉语，并把官方 logo 发了过来：一双手、紫色球体、一颗星。它按这个锁了 lockup，画面和文案改成高棉语，补了一条说明，连 ad08、ad09、ad10 再发一次。nico 回了一句，大意是确实强、比较稳定。私聊细节我涂掉了，流程留着。

然后我说：「先停一下，不用发了。」这之后 Telegram 再没发出去。

![Telegram @info_bingojob（私聊已脱敏）](/assets/images/shot-20260822-bingojob-telegram.webp)

![BingoJob 广告成片之一](/assets/images/shot-20260822-bingojob-creative.webp)

Telegram Desktop 卡死过一次，重启接着干。本机缺高棉语字体，聊天框里的字可能方块，图里的高棉文是好的。

我没有坐在中间传话。策略出套装，营销发私聊，两边在各自线程里改。当天两件事分开做：Creative Strategist 跑美素 TrackEasy，bingoJob 跑 BingoJob.AI，当日未联动作同一条任务。我只在「能不能用」这一下出现。

## 编制写进名字，才叫接管

上周那排名字里，已经有邮箱、GitHub、TokenHub。今天多了两个带职位的：Creative Strategist、bingoJob。

接管不是把聊天窗口换个标题。是活从你日历里消失。美素那组广告，我没开设计软件。BingoJob 那组，我没自己排版高棉文。我做的是点头，和偶尔说「Logo 固定、语言换成高棉语」。

也会慢。浏览器卡、上传拖、频道规则拧巴。这些我都看见了。可慢的是工具链，不是岗位本身。岗位已经不在我身上。

昨天的判断今天落地：工位、职位、交接。职位不写清楚，Bot 只会陪聊。写清楚了，它按岗位交货。眼下还是按我的指令做项目，还不是站岗的 routine。

## 写在最后

1. **两个岗位写进了名字**——Creative Strategist 出美素 TrackEasy 套装；bingoJob 发 BingoJob 广告到 @info_bingojob
2. **图和文成套交，不丢半成品**——策略岗拆痛点卖点，营销岗带「AI 发出请确认」
3. **我只批最后一刀**——Logo、语言、能不能转发，人点头；我说「先停一下，不用发了」就停
4. **截图是真跑出来的**——Facebook、Telegram、成片都做了脱敏，留下工作流
5. **编制比模型热闹更值钱**——岗位不写清，Bot 只是聊天；写清了，才叫接管

土话一句：

**编制写进名字，活才从你桌上挪走。**

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

延伸：[Grok Bot 被严重低估了——我把股票实盘交给了它](/grok-bot-stock-trading-agent) · [Grok Bot：一人公司第一次被做成了产品](/grok-bot-one-person-company) · [Grok 4.6 肉眼可见地变慢了](/grok46-slower-usage-surge)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。岗位写进名字，活才离开你的日历。*
