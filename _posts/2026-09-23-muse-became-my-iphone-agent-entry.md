---
layout: post
title: "我把所有行程交给了 Muse，它住在我的 iPhone 里"
date: 2026-09-23
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260923-muse-agent-iphone.webp
tags: [featured, AI, Meta, Muse, Agent, iPhone, Zaokit]
slug: muse-became-my-iphone-agent-entry
description: >
  9 月 8 日 Meta 发布 Muse，9 月 21 日 iPhone 上装好。
  两周之后，我的日历、邮件、会议纪要全在它手上。
  一个代理接管了我手机里十几个 App 的活。
faq:
  - question: "Muse 是什么？"
    answer: "Meta 2026 年 9 月 8 日发布的个人 AI 代理。跑在云端虚拟机 Muse Secure VM 里，有自己的浏览器。能发邮件、订行程、填表、购物，付款前停下来等你点头。iOS、Android 和 muse.ai 可用，目前只在美国放量。"
  - question: "把行程交给代理安全吗？"
    answer: "Muse 有一个独立的 Sentinel 代理在系统层拦截所有外发请求。密码和支付信息存在加密容器里，Muse 用得了但看不见。年底会上线 Confidential VM，数据用用户自己的密钥加密，Meta 也读不到。"
  - question: "国内能用吗？"
    answer: "现在不行。Muse 只在美国的 iOS、Android 和 muse.ai 上线。国内用户如果想体验类似的代理入口整合，可以试 Zaokit 系列产品。"
  - question: "Muse 跟 Siri 有什么不同？"
    answer: "Siri 执行单条指令——设闹钟、发消息。Muse 接手的是一段任务链：你说一句话，它拆成多步去执行，中间碰到要花钱或发信的节点停下来等你确认。关掉 App 它还在跑，有进展了再回来找你。"
---

昨天傍晚，783 路公交到浦东南路东昌路站的时候，手机弹了一条推送。

不是微信。不是邮件。是 Muse。

「收到，这是徐汇区"千帆计划"高成长企业……」——它在替我处理一封邮件，同时往日历里塞了一条日程。屏幕下面弹出系统弹窗：「允许 Muse 访问日历？」我点了「允许完全访问」。

这个动作花了两秒。如果我自己来，至少六步：打开邮件、读内容、打开日历、新建事件、填时间地点、保存。六步和两秒。差距在这里。

![783 路公交上，Muse 正在创建日历事件，系统弹出日历权限请求](/assets/images/screenshot-20260923-muse-calendar-permission.webp)

![我把行程交给了 Muse](/assets/images/cover-20260923-muse-agent-iphone.webp)

<!--more-->

---

9 月 8 日 Meta [发布 Muse](https://about.fb.com/news/2026/09/introducing-muse/)，官网写得很直白：个人 AI 代理，跑在一台云端虚拟机里，有自己的浏览器，能替你发邮件、订行程、填表、购物。大部分免费，用量上去再订阅。

9 月 21 日我在 iPhone 上装好。

两周过去了。今天我回头看，手机里的使用习惯变了一圈。

过去早上醒来，我的动作链是：看微信消息 → 看邮件 → 看日历 → 查一下今天要出发去哪里 → 打开地图看路线。五个 App，五次点开，五次返回。

现在早上醒来，我跟 Muse 说一句：「今天行程。」它把日历里的安排列出来，附上每段路程的预估时间，如果有冲突会标红。我扫一眼，继续刷牙。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画示意图，奶油到薄荷绿渐变底，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画一个时间线对比：左侧标「过去」，一个小人面前摆着六个App图标（日历、邮件、地图、外卖、购物、航班），小人头上画问号和汗珠，表示要逐个打开；右侧标「现在」，同一个小人面前只有一个大大的对话气泡（写着Muse），Muse下方连线到同样的六个App图标，小人面带微笑喝咖啡。顶部中文「从六个App到一句话」，底部「入口变了 事还是那些事」。中文清晰可读。 --ar 2.35:1 -->

![从六个 App 到一句话——入口变了，事还是那些事](/assets/images/illust-20260923-before-after-muse.webp)

---

举几件这两周 Muse 替我干的事。

有一封供应商的对账邮件，我转发给 Muse，说「核一下数字，如果没问题回复确认」。十分钟后它推了条消息回来：金额一致，已拟好回复邮件，等我确认。我看了一眼内容，点「发送」。

有一场下周三的产品演示，我跟 Muse 说「帮我订会议室，10 人，下午两点到四点，要有投影」。它去翻我公司的日历系统，发了一封预约邮件，回来告诉我：8 楼 B 座会议室，确认函已发你邮箱。

有一天中午想吃上次那家黄焖鸡。我跟 Muse 说了一句。它打开浏览器去找上次的订单记录，问我「送到公司还是家里？」我说公司。它下单，付款弹窗出来让我按指纹确认。

三件事。过去每件都要我打开两到三个 App，切来切去。现在都在同一个对话窗口里。

---

这中间有一个门槛。

我第一次让 Muse 读邮件的时候，系统弹了权限窗口。日历权限、邮件权限、通讯录权限。每一个都要我点「允许」。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画流程图，奶油底、清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画一个手机屏幕，屏幕里是Muse代理的对话界面，上面有一条消息气泡写「收到，已创建日程」。手机旁边画日历弹出窗口，显示一个日程条目写着「徐汇区千帆计划会议」和时间。日历下方有一个盾牌图标，旁边写「需要你同意」。左侧一只手点击「允许」按钮。顶部中文「代理办事 你来点头」，底部「每一步都要你授权」。中文清晰可读。 --ar 2.35:1 -->

![代理办事，你来点头——每一步都要你授权](/assets/images/illust-20260923-permission-flow.webp)

说实话，手指按在「允许」上的时候犹豫了。邮件里有合同报价，日历里有客户行程，通讯录里有合伙人电话。交出去，代理看得到；不交，它帮不了你。

Meta 在这一层做了几道锁。官网技术文档写得很清楚：Muse 跑在独立的 Secure VM 里，一台虚拟机一个人，别人的代理进不来。虚拟机里有一个独立的 Sentinel 代理，系统级隔离，Muse 做的每一件事，发邮件、访问网站、填表单，都要过 Sentinel 这一关。密码和支付信息存在加密容器里——Muse 用得了但看不见。年底会上线 Confidential VM，数据用用户自己的密钥加密，Meta 也碰不到。

这些保障够不够？我不知道。但我算了一笔账：每天花在切 App、读通知、复制粘贴上的时间，大约 40 分钟。Muse 接手之后，这 40 分钟压到 10 分钟以内。省下来的 30 分钟，我用来想产品。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画对比图，奶油到薄荷绿渐变底，清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。画一个小人站在岔路口，左边路标写「自己动手」，路上画很多复杂的表单、按钮、搜索框；右边路标写「代理代劳」，路上画一条笔直的箭头通向终点旗帜。小人选择走右边的路。岔路口中间有一个标志牌写「信任」。顶部中文「信任是门槛 不是技术」，底部「交出控制权 换回时间」。中文清晰可读。 --ar 2.35:1 -->

![信任是门槛，不是技术——交出控制权，换回时间](/assets/images/illust-20260923-trust-threshold.webp)

30 分钟 × 365 天 = 182 小时。一年里多出来的 182 小时，我拿来做产品、见客户、写文章。这笔账算完，我把权限全开了。

---

用了两周之后，我发现一件事情在变。

Muse 变成了我 iPhone 里的 Agent 入口。我不再打开日历 App——我跟 Muse 说「帮我查明天几点有会」。我不再打开邮件 App——我跟 Muse 说「今天有没有需要回复的邮件」。我不再打开地图——我跟 Muse 说「从这里到虹桥机场最快多久」。

日历、邮件、地图、外卖、购物——这些 App 还在手机里。我没卸载。但我打开它们的次数，从每天几十次降到了个位数。它们从我的主屏退到了文件夹里。

这跟我昨天写的那篇文章讲的是同一件事。**代理站在前面，App 退到后面。**

微信面对的问题，我在自己手机上先碰到了。Muse 替我接管了一部分过去属于微信的事——查日程、发消息、看通知。微信还在，但我打开它的理由少了一个：不再需要去微信里翻群消息来确认行程，Muse 替我盯着了。

---

做自己的产品也碰到同样的逻辑。

我一个人做了七八个网站。图文创作在 [Zaokit.app](https://zaokit.app)，AI PPT 也在那里。数字分身在 [cowork.zaokit.app](https://cowork.zaokit.app)。Agent 交易平台在 [zaokit.ai](https://zaokit.ai)。模型服务有 [grok.zaokit.com](https://grok.zaokit.com)、[cx.zaokit.com](https://cx.zaokit.com)、[cc.zaokit.com](https://cc.zaokit.com)。Token 路由在 [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)。还有一个面向教育的 [edu.zaokit.app](https://edu.zaokit.app)——我每天拿它给我一年级的女儿用，她坐在桌前跟 AI 对话练拼音、做数学口算，眼睛盯着屏幕不肯走。一个七岁的孩子，不需要人教她怎么用，打开就说话。如果你家里有小朋友，推荐试试。

八九个域名。用户记得住哪个？

我已经在做一件事：把入口收到一个代理后面。用户进来，跟代理说话。「帮我做一页 PPT」——代理调 Zaokit.app 的绘图和排版。「帮我查上个月的消耗」——代理调 Token Hub 拉数据。「帮我生成一段营销文案」——代理调数字分身去写。

<!-- baoyu-skill prompt: 2.35:1清新知识漫画架构图，奶油底、清线描边，薄荷绿/蜜桃/天蓝/暖黄平涂，留白充足。禁止品牌logo与深色赛博UI。中央画一个人物小人，头顶有一个对话气泡连接到一个标着「AI代理」的圆形节点。这个圆形节点下方用线条连接到一排工具架子，架子上摆着：PPT图标、图文创作图标、数字分身图标、交易平台图标、模型服务图标。架子下方写着各个网址域名。顶部中文「一个入口 一排技能」，底部「用户记住代理 不记域名」。中文清晰可读。 --ar 2.35:1 -->

![一个入口，一排技能——用户记住代理，不记域名](/assets/images/illust-20260923-agent-skill-shelf.webp)

后面那些网站变成了代理的技能。用户记住的是那个对话框，不是 zaokit.app 还是 grok.zaokit.com。

Meta 在手机端做了一遍。我在产品端做了一遍。结论一样：**谁控制代理，谁控制入口。**

---

说回 Muse 这两周的使用感受，记几条真实碰到的问题。

它对中文的理解有偏差。我跟它说「帮我约下周三下午的会」，它偶尔会把「下周三」理解成下下周三。我学会了说具体日期：「帮我约 10 月 1 号下午的会。」

有一次它替我回邮件，措辞太客气。对方是长期合作的供应商，我平时邮件风格直来直去，Muse 写的回复像一个刚入职的实习生在跟领导汇报。我把模板调了一下，告诉它「我的邮件风格：短句、不用敬语、直接说事」。后面的回复正常了。

它在购物场景里容易踩坑。亚马逊在 9 月 21 日把 Muse 挡在门外了——未经授权的 AI 代理访问，直接拦截。国内的电商平台就更不用想了。它能帮你比价、做购物清单，但最后一步「下单」，很多网站走不通。

这些都是 V1 的问题。我不在意。在意的是另一件事：**它让我体验到了「代理优先」的日常是什么样子。**

我不再从 App 出发去找功能。我从一句话出发，让代理去调功能。

---

昨天的文章我写了一句：小程序的调用权交给谁，前门就在谁手里。

今天换个角度讲同一件事。手机里十几个 App 的入口交给谁，日常就在谁手里。

我把我的日历交给了 Muse。邮件交给了 Muse。会议纪要交给了 Muse。出差行程交给了 Muse。

手机里的 App 还在。但我每天第一个打开的，变成了 Muse。

这个习惯一旦养成，回不去了。

---

我一个人打造的 [Zaokit AI Agent 交易平台](https://zaokit.ai)，以及 AI PPT / 图文创作 [Zaokit.app](https://zaokit.app)、[你的数字分身](https://cowork.zaokit.app)，助力大家高效完成图文创作和 PPT 生成。唯一网站：[https://zaokit.app](https://zaokit.app)。

企业侧同一逻辑，已经融进可直接接入的服务：

- [grok.zaokit.com](https://grok.zaokit.com)
- [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com)
- [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai)
- [edu.zaokit.app](https://edu.zaokit.app)（AI 教育，推荐给有小朋友的家庭）
- [gift.junxinzhang.com](https://gift.junxinzhang.com)
- [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

如果你认可 Zaokit AI 的产品理念，欢迎后台留言加入社群。**我们不卖课、不割韭菜，只聚焦 ToB 企业场景的 AI 落地实战。**

---

延伸：[Meta 做了个代理，跟微信抢的不是用户，是前门](/agent-in-front-wechat-mini-program) · [Jev 到底是什么？小白版解释](/jev-for-beginners-pair-with-gpt-claude) · [Jev 刷屏三天，我把它跟决策树放一起拆开看](/jev-system-one-decision-model)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cowork.zaokit.app](https://cowork.zaokit.app) · [cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [edu.zaokit.app](https://edu.zaokit.app) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。Muse 住进我的 iPhone 两周了。日历、邮件、行程，全在它手上。我打开 App 的次数从每天几十次降到了个位数。代理站在前面，App 退到后面。这个方向回不去了。*
