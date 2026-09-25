---
layout: post
title: "Muse 帮我省了 72 美元机票差价，然后我想明白了一件事"
date: 2026-09-25
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260925-muse-connector-appstore.webp
tags: [featured, AI, Meta, Muse, Agent, 连接器, App Store, Zaokit]
slug: muse-connector-ai-appstore-agent-era
description: >
  扎克伯格开放 Muse 连接器，AI 时代的 App Store 来了。Muse 帮我改签机票省了 72 美元，但真正让我停下来想的不是省钱，而是它怎么省的——自己比价、自己填表、自己谈判，我只按了一下确认。以后用户说一句话，Agent 替你选产品、完成交易。连接器、Agent SEO 和代理支付，可能是下一轮创业机会。
faq:
  - question: "Muse 怎么帮省钱？"
    answer: "Muse 跑在独立虚拟机里，有自己的浏览器，能自动打开多个比价网站、航空公司官网和 OTA 平台，找出同一航线的最低价。它还能进入改签页面填好资料，把差价算出来让你确认。整个过程你不用打开任何网站。"
  - question: "Muse 连接器是什么？"
    answer: "Meta 开放的 Muse 第三方接入能力。开发者通过 API 把自己的服务注册为 Muse 的一个技能，用户跟 Muse 说需求时，Muse 可以直接调用该服务完成任务。类似于 App Store 里上架一个 App，但交互方式从点击变成了对话。"
  - question: "ChatGPT、Claude、Grok 做不了这些事吗？"
    answer: "模型能力上做得到。差距在执行层——浏览器、登录状态、支付、日历、邮箱的整合深度。Muse 把这些全接上了，并且敢让代理替用户发邮件、付款、改预约。其他几家在这一步上还比较保守。"
  - question: "Agent SEO 是什么意思？"
    answer: "传统 SEO 是让搜索引擎找到你的网站。Agent SEO 是让 AI 代理找到你的服务。当用户跟 Muse 说'帮我订一家日料'，Muse 选谁来执行，取决于你的服务描述、评分和完成率。谁先把这套优化做好，谁先拿到 Agent 时代的流量。"
---

上周我要改一张上海飞北京的机票。航班提前了，原来订的那趟赶不上。

以前的做法：打开航空公司 App，找到订单，点改签，一个个翻可选航班，比价，选座，填信息，付差价。整套流程走下来，二十分钟打底。

这次我跟 Muse 说了一句："帮我把下周三的东航改成下午两点之后的，经济舱就行。"

三分钟后它回来了："找到 14:20 的 MU5116，差价省 72 美元，改签手续费 0，资料已填好，你确认一下。"

我按了确认。完事。

![Muse 帮我省了 72 美元机票差价](/assets/images/cover-20260925-muse-connector-appstore.webp)

<!--more-->

72 美元。说大不大，说小不小。但让我停下来想的不是这笔钱，而是它怎么省的。

我自己改签的时候，通常只看航空公司官网。顶多再开一个携程对比一下。两个页面来回切，已经够烦了。Muse 不一样——它的虚拟机里有自己的浏览器，它同时打开了航空公司官网、两家 OTA 和一个比价引擎，把四个渠道的价格拉出来排了一遍。72 美元的差价，来自一个我压根没想到会去看的渠道。

人的注意力有限。你最多同时比三个页面。代理没有这个限制。它可以同时跑十个渠道，每个渠道的价格、退改规则、座位余量全摸一遍，花的时间比你打开一个页面还短。

这就是 Muse 省钱的底层逻辑——你拿不到的信息差，它替你抹平了。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画示意图，奶油到薄荷绿渐变底，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面分左右两部分：左边标「过去」，一个用户小人面对电脑屏幕，屏幕上显示密密麻麻的搜索结果、比价页面、填表单界面，小人头上冒汗珠和问号。右边标「现在」，同一个小人对着一个对话气泡说了一句话，下方一个机器人代理在高速穿梭于多个网站图标之间（航班、酒店、餐厅），最后递上一张已填好的表单和数字72美元差价提示。顶部中文「你说一句话 代理跑全程」，底部「搜索比价填表 全部自动完成」。中文清晰可读。 --ar 2.35:1 -->

![你说一句话，代理跑全程](/assets/images/illust-20260925-agent-workflow.webp)

---

省钱只是表面。底下藏着一件更大的事。

扎克伯格上周把 Muse 连接器开放了。意思是：第三方开发者可以把自己的服务接进 Muse。

你做了一个本地餐厅预订的 API，接进去。你做了一个二手车比价的服务，接进去。你做了一个签证代办的工具，接进去。用户跟 Muse 说"帮我订今晚七点的日料，两个人"，Muse 去连接器里挑一个餐厅服务来执行。

我看完公告第一反应——这跟 2008 年苹果开放 App Store，味道太像了。

当年乔布斯打开 iPhone 的开发者入口，一个人做的计算器 App 一夜之间冲进下载榜前十。移动互联网生态从那扇门里长出来。Muse 连接器做的是同一件事，只是入口从"点击图标"变成了"说一句话"。

更狠的一点——用户连挑选都不用了。App Store 时代你还得自己搜 App、看评分、下载试用。Agent 时代，用户只说需求，代理替你挑。

一个 3 人的 API 团队，API 可靠、价格合理、完成率高，就有可能触达千万用户。不需要品牌，不需要市场部。

---

最近很多人问我：Muse 能打电话、订餐厅、改机票、订酒店——ChatGPT、Claude、Grok 做不了吗？

不是做不了。

ChatGPT 已经可以操作网页和调用工具，Operator 在跑着。Claude 更早——Anthropic 2025 年底就推了 computer use，让 AI 操作桌面和浏览器。Grok 也在推 voice agent。

模型能力都过了及格线。拆开看，每一家都能做"搜航班、填表单、发邮件"这种事。

差距在两件事：谁把模型之外的执行能力接得更完整，谁愿意给 AI 更大的操作权限。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画对比图，奶油底到淡蓝渐变，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面中央一个三角形天平秤，左盘标注「模型能力」放着一个大脑图标，右盘标注「执行权限」放着一把钥匙和一个盾牌，天平倾斜向右盘（表示执行权限更重）。天平下方画三个图标排列：浏览器、登录状态、支付钱包，每个图标上方有一个小锁。顶部中文「瓶颈不在模型 在权限」，底部「浏览器 登录 支付 每一步都要授权」。中文清晰可读。 --ar 2.35:1 -->

![瓶颈不在模型，在权限](/assets/images/illust-20260925-permission-bottleneck.webp)

代理真正替你办事需要一整条链：浏览器能打开网页填表单，登录状态能进你的邮箱和航空公司会员账号，电话能打客服热线，邮箱能发确认函，日历知道你哪天有空，支付能帮你掏钱，关掉 App 之后还得接着跑。

哪一块缺了，代理就只能停在"给建议"这一步。给建议省不了钱。替你干活才省钱。

ChatGPT 的 Operator 网页操作走得远，但不住在你手机里，不接日历，不帮打电话。Claude 的 computer use 桌面端演示漂亮，但产品定位偏开发者工具，普通人拿来订餐？距离太远。Grok 声音自然，支付和账号管理这些重活还没接上。

Muse 把这些补全了。独立的 Secure VM，一台虚拟机一个人。自己的浏览器。Sentinel 代理在系统级拦截每一个外发请求。密码和支付信息在加密容器里——Muse 用得了但看不见。年底还上 Confidential VM，数据用用户自己的密钥加密。

所以 Muse 最近体感强，原因在这里——它更敢把"最后一公里"做出来。

---

但"敢"是要付代价的。

以前 AI 错了，顶多回答不准确，你自己再查一遍。现在 AI 能操作你的账号、修改预约、花你的钱——错了就是真钱、隐私和合同。帮你回复了一封措辞不当的邮件，帮你订了一张退不了的机票，帮你用错误的金额完成了一笔付款。每一件都有后果。

Agent 走到今天，瓶颈从模型能力转移到了三件事：权限、安全、责任。

谁先把这三件事理顺，谁才算真正进场。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画架构图，奶油底、清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面展示三个创业机会的方向牌，像路标一样竖立在草地上。第一个路标写「连接器」旁边画API插头和齿轮。第二个路标写「Agent SEO」旁边画搜索放大镜和代理小人。第三个路标写「代理支付」旁边画钱包和芯片。三个路标的交汇处站着一个背包客小人（代表创业者），看着这三条路思考。顶部中文「三个方向 三个机会」，底部「连接器 Agent SEO 支付」。中文清晰可读。 --ar 2.35:1 -->

![三个方向，三个机会](/assets/images/illust-20260925-three-opportunities.webp)

---

我琢磨了一下，连接器开放之后，创业机会可能出在三个地方。

连接器开发。谁能做出好用的第三方连接器——帮 Muse 接通本地外卖、快递、打车、政务办事——谁就是 Agent 时代的"App 开发者"。中国市场这一块几乎空白。想想看：一个三人团队做了个"帮你比价全国酒店并自动预订"的连接器，接进 Muse，用户一句话就能省几百块住宿费。这个事情成立。

Agent SEO。传统 SEO 让谷歌找到你的网站。Agent SEO 让 AI 代理找到你的服务。用户跟 Muse 说"帮我订一家日料"，Muse 怎么决定调谁？服务描述的质量、历史完成率、评分、价格竞争力——这些变成新的排名因子。谁先跑通这套优化，谁先吃到 Agent 时代的流量。

代理支付。Muse 用的是 Stripe Link，支付前弹窗让用户确认，还有 Link 的购物保障——退货免费、价格下降补差。中国市场呢？微信支付、支付宝能接进代理链路吗？代理替你付款这件事，牌照、风控、退款流程，每一环都是生意。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画流程图，奶油到薄荷绿渐变底，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画面是一条跑道，起点写「回答得好」，终点写「把事办完」。跑道上有四个选手（简笔小机器人），分别标注C、Cl、G、M。前三个选手在起点附近的「聊天区」走着，M选手已经跑到了「执行区」——跑道后半段画着电话、邮箱、日历、钱包等图标。顶部中文「竞争从回答 转向办事」，底部「谁先跑完最后一公里 谁赢」。中文清晰可读。 --ar 2.35:1 -->

![竞争从回答转向办事——谁先跑完最后一公里，谁赢](/assets/images/illust-20260925-race-last-mile.webp)

---

我自己做 Zaokit 一年多，走过不少弯路。

最初做 AI PPT 想法简单——快速出 PPT。后来发现 PPT 只是表层，底下是内容创作工作流，再往下是企业 AI 管理——谁调用了什么模型、花了多少 token、数据能不能出域。

一层层扒下来，从 [Zaokit.app](https://zaokit.app) 到 [Agent 交易平台](https://zaokit.ai) 到 [Token Hub](https://tokenhub.zaokit.ai)，从 [数字分身 Cowork](https://cowork.zaokit.app) 到 [模型服务](https://grok.zaokit.com)（[cx](https://cx.zaokit.com)、[cc](https://cc.zaokit.com)），每一个产品都是被客户推着做出来的。

做到今天我有一个体感：Agent 的竞争，下一阶段会从"谁回答得好"变成"谁能真正替用户省钱省时间"。

回答得好，用户说"谢谢"然后关掉窗口。

帮你省了 72 美元，用户说"下次还找你"。

这两句话之间的距离，就是 Agent 这一代产品的战场。

---

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)、[你的数字分身](https://cowork.zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。** 希望在这里，能给你带来不一样的思维火花和真实的商业碰撞。

---

延伸：[我把所有行程交给了 Muse，它住在我的 iPhone 里](/muse-became-my-iphone-agent-entry) · [Meta 做了个代理，跟微信抢的不是用户，是前门](/agent-in-front-wechat-mini-program) · [千帆竞发，接地气的才跑得远](/xuhui-qianfan-ai-training-camp)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Muse 帮我省了 72 美元机票差价，但真正让我想明白的是——Agent 的下一步竞争，不是谁更聪明，是谁能替用户省钱省时间。*
