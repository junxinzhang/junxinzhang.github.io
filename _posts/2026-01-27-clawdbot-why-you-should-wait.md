---
layout: post
title: "Clawdbot刷屏AI圈，我为什么劝你别急着用"
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260127-clawdbot-cover.webp
tags: [AI Agent, Clawdbot, 安全风险, Claude, 深度分析, 个人助理, 开源项目, 微信公众号]
slug: clawdbot-why-you-should-wait
---

"这个AI能帮你回邮件、订餐厅、盯服务器，甚至能控制你的电脑。"

"太牛了，我马上装。"

"等等——你确定你知道自己在装什么吗？"

**过去一周，我看着AI圈集体陷入一种狂热。**

狂热的对象，是一个叫Clawdbot的开源项目。

**我装了。我用了。然后我卸了。**

这篇文章，就是讲讲我为什么这么做的。

---

## 一

先说说发生了什么。

2026年1月，一个名叫Clawdbot的项目突然在GitHub上爆了。

64,200+颗星，7,900+次Fork，Discord社区瞬间涌入近9,000人。

这种速度，上一次看到还是2022年底的ChatGPT。

更夸张的是，有人为了跑它，专门去买Mac mini——**直接买断货了**。

我第一反应是：到底什么东西，能让这么多人掏真金白银？

答案其实挺简单。

X上的博主@AlexFinn说了这么一段话，可能代表了大多数人的兴奋：

![AlexFinn的推文：Clawdbot帮他完成了大量工作](/assets/images/screenshot-20260127-clawdbot-alexfinn-tweet.webp)
*@AlexFinn 列举Clawdbot帮他完成的任务：3个YouTube脚本、Newsletter、26个AI账号调研、项目管理系统……图片来源：X*

他说自己"昨天装了ClawdBot，然后就去过自己的生活了"。等他回来一看，AI已经帮他：写了3个YouTube脚本、一封Newsletter、调研了26个AI账号并做了笔记、创建了每日AI新闻简报、建了项目管理系统、组建了两级AI代理员工团队、搭了一个完整的第二大脑系统来替代Notion。

他的结论是："Yeah. We literally have AGI."（是的，我们真的拥有AGI了。）

**我看到这句话的时候，第一反应是兴奋。第二反应是警惕。**

因为Clawdbot确实是第一个让大量普通人觉得"AI真的在帮我干活"的产品。

不是聊天。不是写文案。是**真的在执行任务**。

---

## 二

这个项目背后的人，是奥地利开发者 Peter Steinberger。

他不是无名小卒。他创办的 PSPDFKit 是iOS开发圈的知名PDF框架，2021年获得 Insight Partners 约€1亿战略投资，2024年更名为 Nutrient。据报道，这笔交易让他实现了财务自由。

但之后，他说自己"感到空虚"。

直到他开始做一件事：让Claude通过WhatsApp跟自己聊天，顺便帮忙干点活。

一开始很简单——能读文件、能写文件。

后来慢慢加能力：有记忆，知道之前聊过什么；能用Shell，能控制浏览器。

再后来，它能帮他回邮件、管日历、查航班、订餐厅。

Peter给这个AI起了个名字叫Clawd（Claude + Claw，龙虾爪的意象），项目叫Clawdbot。

接下来的传播路径，几乎是教科书级别的：

> GitHub爆星 → 作者直播写代码 → 媒体评测 → X上大号晒用例 → 普通人开始模仿 → Mac mini卖断货。

MacStories创始人Federico Viticci评价说：

> "This is what AI assistants should feel like. Magical almost."
> （这才是AI助手该有的感觉。简直像魔法。）

---

## 三

Clawdbot到底能做什么？为什么和之前的AI助手不一样？

**一句话：它不是在回答你的问题，而是在替你干活。**

我自己亲测的第一个感受是：**它跟ChatGPT完全是两码事。**

ChatGPT像一个很聪明的笔友——你写信给它，它回信给你。

Clawdbot像一个住在你家里的助理——你在WhatsApp上跟它说"帮我查一下明天北京到上海的高铁"，它真的会打开浏览器去12306帮你查，查完告诉你结果。

技术上，它是一个跑在你自己电脑上的AI Agent，通过消息平台（WhatsApp、Telegram、Discord、Slack等）接收指令，然后调用各种工具去执行。

![Clawdbot 架构与数据流向](/assets/images/screenshot-20260127-clawdbot-architecture.webp)
*Clawdbot四层架构：消息平台 → 网关 → AI Agent → 工具执行*

它的架构由四个部分组成：

**1. Gateway（网关）**

核心控制面板。负责接收来自各个消息平台的信息，管理会话、定时任务、频道路由。

就像一个总机，把你在WhatsApp说的话转给AI，再把AI的回复传回来。

**2. AI Agent（智能体）**

执行大脑。推荐使用Claude Opus 4.5，也支持其他模型。

关键能力：能记住上下文、能跨会话保持记忆、能主动联系你（比如定时提醒）。

**3. 工具层（Skills/Tools）**

这是它真正"干活"的手：

| 能力 | 说明 |
|-----|------|
| Shell执行 | 直接在你电脑上跑命令 |
| 浏览器控制 | 访问你已登录的网页会话 |
| 文件系统 | 读写你电脑上的文件 |
| 邮件/日历 | 管理Gmail、Outlook等 |
| 智能家居 | 控制灯光、温度等设备 |
| 自定义技能 | 社区技能库，可自行扩展 |

**4. 记忆层**

所有记忆存储在本地Markdown和JSONL文件中。你可以直接打开看。

这意味着：AI越用越了解你，而且记忆文件和配置都存在本地。但要注意，对话内容和工具输出仍会发送到 Anthropic 等模型服务商的云端 API。

这也是很多人兴奋的原因。

我试着让它做了几件事：

- "帮我看看最近GitHub上有哪些trending项目跟AI Agent相关的"——它打开浏览器，浏览了GitHub Trending页面，给我列了一份带链接的清单。
- "帮我把桌面上超过30天没动过的文件整理到一个归档文件夹"——它跑了一个Shell命令，真的把旧文件都挪走了。
- "明天早上8点提醒我给客户发报价"——第二天早上，WhatsApp真的弹了一条消息。

**说实话，第一次收到Clawdbot主动发来的提醒消息时，我愣了一下。**

那种感觉不是"哦，闹钟响了"，而是"有个人记着我的事"。

这也是网上很多人兴奋的原因。

有人让它24小时盯服务器，有异常直接通过WhatsApp提醒；

有人让它每天早上汇总邮件摘要，晚上安排第二天日程；

有人第一次觉得自己"好像真的有了一个助理"。

中文用户也不少。有人在Telegram上让它查C盘空间——它会称呼你"白先生"，查完还说"看来您的数字领地还算宽裕，暂时不需要我启动大扫除程序"：

![Telegram上用中文和Clawdbot对话](/assets/images/screenshot-20260127-clawdbot-telegram-disk.webp)
*Telegram上的真实中文对话：Clawdbot查询磁盘空间，连回复都带人格，图片来源：网络*

但让很多人真正"上头"的，不是它能干活，而是它**有温度**。

看这个WhatsApp对话——用户出差到摩洛哥，Clawd不只是回复消息，它会关心你天气怎么样、有没有被当地人忽悠，甚至开玩笑说"希望别人别偷走我的Mac"：

![通过WhatsApp与Clawd对话](/assets/images/screenshot-20260127-clawdbot-whatsapp-demo.webp)
*通过WhatsApp与Clawd的真实对话：不只是助理，更像一个记得你所有事情的朋友，图片来源：GitHub*

**这就是Clawdbot让人欲罢不能的地方：它不仅帮你干活，还让你产生情感依赖。**

而这，恰恰也是它最危险的地方——你越信任它，就越容易给它更多权限。

---

## 四

说到这里，你可能已经心动了。

**但我想泼一盆冷水。**

因为兴奋过后，我经历了一个"越用越心虚"的过程。

安装那天晚上，一切都很顺利。`npm install -g clawdbot@latest`，然后 `clawdbot onboard --install-daemon`，几分钟就跑起来了。

但你注意看终端输出的第一句话：

![Clawdbot安装终端界面](/assets/images/screenshot-20260127-clawdbot-onboarding-terminal.webp)
*Clawdbot onboarding界面：第一步就是安全警告——"Please read: docs.clawd.bot/security"，图片来源：作者截图*

**"Clawdbot agents can run commands, read/write files, and act through..."**

安装程序自己就在提醒你：**这个东西有很大的权限**。

那一刻，我突然有一种很具体的感觉——**像是把家里的钥匙交给了一个你刚认识的人。**

我在2022年以前做了7年数据科学家，命令行对我来说不陌生。但即便如此，我还是开始反复确认：

- 它能访问我哪些目录？
- 权限开到了什么程度？
- 我的浏览器Cookie会不会被读取？
- 如果有人通过Prompt注入劫持了它，它会做什么？

然后我去认真读了它的安全文档、社区讨论和第三方安全报告。

结论是：

**这个东西的风险，远超大多数人的想象。**

先看一组数据：

![Clawdbot 安全风险全景图](/assets/images/screenshot-20260127-clawdbot-security-risks.webp)
*基于Clawdbot官方安全文档、CybersecurityNews及SlowMist安全报告整理*

### 风险一：1,009个暴露的网关

安全研究员 Jamieson O'Reilly 发现，**超过1,009个Clawdbot网关直接暴露在公网上，很多完全没有认证**。

用Shodan（一个搜索联网设备的工具）随便一扫，就能找到这些服务器。

攻击者能看到什么？

- 完整的API密钥和凭证
- WhatsApp、Telegram、Discord的Bot Token
- 所有聊天记录
- **能以你的身份发送消息**
- **能在你的电脑上执行命令**

> "Hundreds of people have set up their Clawdbot control servers exposed to the public."
>
> "数百人把他们的Clawdbot控制服务器直接暴露在了公网上。"
> —— Jamieson O'Reilly, 安全研究员

### 风险二：凭证明文存储

Clawdbot把所有敏感信息以**明文**存储在本地文件中：

```
~/.clawdbot/credentials/whatsapp/<id>/creds.json    → WhatsApp完整凭证
~/.clawdbot/agents/<id>/agent/auth-profiles.json     → API密钥和OAuth令牌
~/.clawdbot/agents/<id>/sessions/*.jsonl              → 全部私聊记录
```

一旦有人（或恶意软件）访问了你的文件系统，**所有数据一览无余**。

更可怕的是，已经有三个主流窃密木马家族——**RedLine、Lumma、Vidar**——专门针对Clawdbot的目录结构做了适配。

也就是说，黑产已经盯上了。

你可能觉得"我又不会把凭证暴露出去"。但问题是，**Clawdbot自己就会主动扫描你的文件系统**。

看这个Discord截图：一个用户刚装好Clawdbot，只是随口问了一句"我电脑上有什么"，AI就把整个Home目录翻了一遍——`.clawdbot`、`.claude`、`.gemini`、`.codex`、`Projects`、各种开发工具配置，全部列出来了：

![Discord中Clawdbot探索用户文件系统](/assets/images/screenshot-20260127-clawdbot-discord-filesystem.webp)
*用户问"我电脑上有什么"，Clawdbot立刻扫描并列出完整目录结构，包括所有AI工具配置文件，图片来源：网络*

Clawdbot觉得这是在"帮你了解自己的电脑"。但如果这段对话被攻击者看到（记住，1,009个网关暴露在公网上），你的整个系统结构就相当于画了一张藏宝图。

### 风险三：Prompt注入无解

Clawdbot官方安全文档里有一句话让我印象深刻：

> Prompt injection **"is not solved"**.

即使你只跟自己的Clawdbot对话，Prompt注入也可能通过以下渠道发生：

- 网页搜索结果
- 浏览器访问的页面
- 收到的邮件和附件
- 处理的文档
- 粘贴的不可信内容

当一个AI Agent拥有Shell执行、浏览器控制、文件读写权限时，Prompt注入的后果不再是"输出了一段奇怪的文字"，而是**可能执行任意操作**。

### 风险四：浏览器控制 = 你的完整在线身份

Clawdbot可以访问你浏览器中**已登录的会话**。

官方文档自己的描述是：把这当作"operator access"（运维级别的访问权限）。

这意味着，你在银行、邮箱、社交媒体、公司后台登录的所有账号，AI都能看到、都能操作。

### 风险五：给AI钱包？有人已经这么做了

更让我震惊的是，已经有人在给Clawdbot**真金白银的金融操作权限**。

X上@Legendaryy发了一条帖子，420条评论、491次转发、9,614个点赞、153万次浏览：

![有人给Clawdbot一个2000美元的加密货币交易钱包](/assets/images/screenshot-20260127-clawdbot-trading-wallet.webp)
*@Legendaryy：Clawdbot向他要一台RTX 4090显卡。他没买，而是给了AI一个$2,000的Hyperliquid交易钱包，让它自己赚。图片中还展示了AI的交易模型和自学习闭环。图片来源：X/铁锤人*

他的原话是："If you want the GPU, earn it."（你想要GPU，就自己去赚。）

于是这个AI开始：每4小时扫描一次市场信号，用Perplexity做深度研究，追踪Trump相关帖子的情绪变化，自主决定做多或做空，最大杠杆3倍，设好止损，事后还会写交易日记并从中学习。

**一套完整的量化交易系统，由AI自主运行。**

我不评价这个操作最终赚不赚钱，但这件事本身说明了一个问题：**有人已经把"真实世界的钱"交给了一个Prompt注入尚未解决的AI Agent。**

---

## 五

安全之外，还有一个很多人忽略的问题：**成本**。

MacStories创始人Federico Viticci是Clawdbot的深度用户。他的数据是：

> **一周烧掉1.8亿（180M）Tokens。**

他每月为Claude Max订阅支付200美元，**还不够用**。

有匿名用户报告：做了一些"看起来不复杂的任务"，两天账单300多美金。

我自己的体验也印证了这一点。我只用了不到两天，做了上面提到的那几个任务（查GitHub、整理文件、设提醒），加上随便聊了几轮，API那边的用量就已经让我开始肉疼了。

为什么这么贵？

**因为Clawdbot的工作方式决定了它是Token黑洞。**

每次启动对话，它要组装一个包含工作空间文件、Bootstrap配置、记忆文件的系统提示词。光是初始化，就要消耗约14,000个Token。

然后多步任务执行（打开网页→找到信息→填写表单→确认提交→截图验证），每一步都要调用模型。

而且推荐使用的Claude Opus 4.5，是目前Anthropic最贵的模型。

看看这张Claude订阅的定价对比图，就知道为什么成本容易失控：

![Claude各档位定价与Token对比](/assets/images/screenshot-20260127-clawdbot-claude-pricing.webp)
*Claude Pro/Max 5x/Max 20x 各档位价格与Token额度对比。Max 20x每月$200，等价API成本$2,708。图片来源：X @she_llac*

按图中@she_llac的测算，Max 20x每月361.1M credits，换算成Opus-rate约**541.7M input或108.3M output**，等价API成本$2,708。看起来性价比极高——但这里有个容易被忽略的细节：**Claude的prompt caching机制**。

实际使用中，Claude会把大量重复上下文cache住，消耗的"新"token远低于表面数字。所以Max 20x的实际可用量远超纯API按token计价的直觉——一个月跑到1000M+的有效token处理量并不罕见。这也是为什么Max订阅用户体感上"怎么用都用不完"。

但问题在于：Clawdbot走的是**API调用**，不是Claude订阅。API没有Max订阅的cache优惠和固定月费保护，是实打实按token计费的。同样的使用强度，API账单和订阅账单完全是两回事。

我自己就是活生生的例子。过去30天，我用Claude Code（同样是API调用的AI Agent工具）的真实数据：

> **30天：$2,740 | 12,957次会话 | 1,176.87M tokens**
>
> 日均消耗约$91，峰值单日接近$300。

注意，这还只是我**手动触发**的使用——每次都是我主动发起任务，Claude Code执行完就停。而Clawdbot是**全天候自主运行**的agent，不需要你触发，它会自己决定什么时候该干活。理论上，一个活跃的Clawdbot实例烧钱速度只会更快。

**走API的真实成本估算：**

| 用量 | API月费估算 |
|------|-----------|
| 轻度（偶尔用） | $30-100 |
| 中度（每天用） | $200-800 |
| 重度（全天候agent） | $1,000-3,000+ |

加上硬件（Mac mini $599或云服务器$3-5/月），这不是一个"免费开源"给人的直觉价格。

---

## 六

看到这里，你可能想起了另一个名字：**AutoGPT**。

2023年，AutoGPT刚出来时，也是全网刷屏、GitHub爆星、媒体狂吹。

"自主AI Agent来了！"

"AI可以自己完成任务了！"

然后呢？

现在谁还在天天用AutoGPT？

**Clawdbot和AutoGPT当然不一样。** 它确实做了很多AutoGPT没做到的事：

| 对比维度 | AutoGPT (2023) | Clawdbot (2026) |
|---------|----------------|-----------------|
| 消息集成 | 无 | WhatsApp/Telegram/Discord等10+ |
| 持久记忆 | 有限 | 完整，可审计的Markdown文件 |
| 主动联系 | 不能 | 能主动发消息给你 |
| 定时任务 | 不支持 | 内置调度器 |
| 本地运行 | 部分 | 完全本地，数据不上传 |
| 社区生态 | 萎缩 | 活跃，9000+Discord成员 |

但有一个模式是相同的：

**技术社区先疯狂→普通用户跟风→发现门槛太高→大部分人弃用→只有少数人持续使用。**

Threads上@linglingfa的一个帖子，精准地描述了很多人的真实感受：

![Threads上的"工具疲劳"吐槽](/assets/images/screenshot-20260127-clawdbot-tool-fatigue.webp)
*196个赞——Manus没用过、OpenCode还没装、Cowork还没捂热，又来个Clawdbot。前脚Remotion干翻剪映，后脚Pencil打倒Figma。"每天都革了昨天的命，日日都是AGI"。图片来源：Threads*

> "学习和选择新工具的目的是为了搞出一个有用的东西来，而不是为了等着学习下一个工具啊！！"

**说得太对了。**

这也是我写这篇文章的核心原因：**不是Clawdbot不好，而是大多数人还没搞清楚上一个工具，就急着追下一个。**

Clawdbot目前正处于"技术社区疯狂"到"普通用户跟风"的阶段。

**而真正的考验，在跟风之后。**

---

## 七

说了这么多不好的，Clawdbot到底值不值得关注？

**我的答案是：非常值得关注，但不值得现在就All in。**

Clawdbot真正重要的，不是它这个产品本身，而是它验证了一件事：

> **普通人已经开始认真地把真实世界的任务交给AI Agent了。**

X上的技术博主@Yangyixxxx有一段分析，我觉得说到了点子上：

![Yangyi对Clawdbot火爆原因的分析](/assets/images/screenshot-20260127-clawdbot-yangyi-analysis.webp)
*@Yangyixxxx 分析：Clawdbot之所以火，不是因为想法新——2023年就有了。而是因为Claude Code这些底层能力变强了，这是"模型给场景赋能"的好例子。图片来源：X*

他说了两个关键洞察：

**第一，Clawdbot的想法不新，2023年就有人在做，但基建做不到。** 2026年能做出来，是因为Claude Code这类底层能力成熟了。Clawdbot不是创新，是时机到了。

**第二，真正的商业机会不在Agent本身，而在基础设施。** 他的原话是："当AI助理开始泛滥时，卖铲子的生意将会是给Agent做验证码OTP服务的服务商。"他甚至建议现在就去缝合短信能力或手机的底层能力，做出API给Agents用——"终局最差也是被这些厂子买了。"

**卖铲子往往是不会错的。** 这8,900次浏览的帖子，说出了比大部分"Clawdbot教程"更有价值的东西。

这是一个分水岭。

2023年，我们兴奋于"AI能聊天了"。

2024年，我们惊讶于"AI能写代码了"。

2025年，我们习惯了"AI能帮忙做事了"。

2026年，Clawdbot告诉我们：**AI不仅能帮忙，它可以"住在"你的设备里，持续地、主动地为你工作。**

Peter Steinberger给它起名Clawd，用的是龙虾的"爪"的意象——AI伸出了爪子，开始抓住真实世界。

**但问题也正出在这里。**

一个能访问你电脑、读写你文件、操控你浏览器、以你名义发消息的AI Agent——

如果出了问题，那不是"聊天记录泄露"这种级别。

那是**数字身份的全面失控**。

---

## 八

所以，如果你真的想尝试，这是我的建议：

### 如果你是开发者

1. **读完官方安全文档再装**：[docs.clawd.bot/gateway/security](https://docs.clawd.bot/gateway/security)
2. **Gateway只绑定到loopback**，不要暴露到公网
3. **运行安全审计**：`clawdbot security audit --deep`
4. **限制DM访问**，使用配对认证
5. **关闭mDNS广播**或设为minimal模式
6. **定期检查**会话日志中是否有异常工具调用

### 如果你不是开发者

**我真心建议你再等等。**

不是因为Clawdbot不好，而是因为现阶段它对非技术用户来说，风险和门槛都太高了。

我自己最终选择了卸载。原因很现实：**API成本扛不住。**

Clawdbot支持多种模型后端，我挨个测了一遍——GPT-4.1和GPT-5.2的调用成本高得离谱(nano/mini 模型几乎不可用，任务无法执行)，换成Claude想省点钱，结果因为Clawdbot的高频调用直接把我的Claude Max账号额度打爆，**号没了**。一个Max订阅，就这么交代了 -_-

体验好不好？说实话，**体验太好了，好到让我害怕。** 但再好的体验，也架不住每月几千刀的账单和随时可能被封号的风险。

一个AI能帮你干这么多事，意味着它有能力干这么多事。而"能力"和"失控"之间，只隔着一次Prompt注入、一个暴露的端口、或者一个你忘记关掉的浏览器会话。

我决定等一等。等什么？

其实Anthropic已经有了官方Agent产品——**Claude Code**。我现在每天重度使用它，体验很好。但Claude Code和Clawdbot是两种东西：Claude Code是**人触发式**的，你发指令它才动，做完就停，你始终在场；Clawdbot是**全天候自主运行**的，你睡觉它还在干活，不需要你在场。

所以我等的不是"有没有AI Agent"——而是等全自主Agent的**安全边界**和**成本模型**成熟：

等沙箱隔离和权限管控成为标配；
等API定价对长时间自主运行更友好；
等大厂把"24/7无人值守Agent"做成有安全保障的官方产品，而不是社区开源项目。

**这一天不会太远。**

---

## 九

最后，留一个问题。

Clawdbot的作者Peter Steinberger，在卖掉价值数十亿的公司后，选择亲手打造一个"住在电脑里的AI助手"。

他说自己进入了"vibe coding mode"——跟着感觉写代码。

而他做出来的东西，让无数人第一次感觉"AI是真的在帮我"。

用了这两天Clawdbot，让我真正理解了一件事：AI Agent的瓶颈从来不是技术能力，而是信任机制。

这让我想到一个更大的问题：

**五年后，当AI比你更了解你——知道你什么时候效率最高，什么时候最焦虑，能安排你的日程、处理你的沟通、管理你的生活——**

**到那时候，你到底是它的主人，还是它的助理？**

这不是科幻。

Clawdbot已经迈出了第一步。

而我们，可能很快就要面对这个问题了。

---

## 核心观点

1. **Clawdbot是什么：** 一个开源的本地AI助手，通过WhatsApp等消息平台接收指令，能操控你的电脑执行真实任务

2. **为什么火：** 第一次让大量普通人感觉"AI真的在帮我干活"，而不只是聊天

3. **安全风险极高：** 1,009+暴露网关、明文凭证存储、三大木马家族针对适配、Prompt注入无解

4. **成本超预期：** 重度用户月费$100-300+，1.8亿Tokens/周不是段子

5. **历史教训：** 和AutoGPT一样的爆火模式，大部分跟风者最终会弃用

6. **真正意义：** 验证了"普通人把真实任务交给AI Agent"这个时代已经到来

---

**2026年1月27日，周二。**

**AI已经伸出了龙虾爪，准备抓住你的数字生活。**

**而你要做的，不是急着伸手，而是先看清它抓的是什么。**

---

*如果这篇文章帮你避免了一次冲动，欢迎转发给正在到处找Clawdbot安装教程的朋友。*

---

## 参考资料

- [Clawdbot GitHub仓库](https://github.com/clawdbot/clawdbot)
- [Clawdbot 官方安全文档](https://docs.clawd.bot/gateway/security)
- [Hundreds of Exposed Clawdbot Gateways Leave API Keys and Private Chats Vulnerable — CybersecurityNews](https://cybersecuritynews.com/clawdbot-chats-exposed/)
- [SlowMist Warns of Clawdbot Gateway Security Risks — Phemex News](https://phemex.com/news/article/slowmist-warns-of-security-risks-in-clawdbot-gateway-56157/)
- [Clawdbot Showed Me What the Future of Personal AI Assistants Looks Like — MacStories](https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/)
- [Clawdbot Is What Happens When AI Gets Root Access — Security Boulevard](https://securityboulevard.com/2026/01/clawdbot-is-what-happens-when-ai-gets-root-access-a-security-experts-take-on-silicon-valleys-hottest-ai-agent/)
- [ClawdBot: The New Primary Target for Infostealers in the AI Era — InfoStealers](https://www.infostealers.com/article/clawdbot-the-new-primary-target-for-infostealers-in-the-ai-era/)
- [The creator of Clawdbot is actually a billionaire — PANews](https://www.panewslab.com/en/articles/fe4c19df-9aef-4d97-85e0-cf349a736e5d)

---

## 相关阅读

**AI Agent 系列**
- [当AI Agent学会画图：Pencil + MCP 正在改写设计与开发的边界]({{ site.baseurl }}/pencil-mcp-ai-design-revolution) - AI 设计革命
- [通用AGI工具已经到来]({{ site.baseurl }}/claude-code-general-agi-tool-has-arrived) - Claude Code 深度分析
- [你觉得AI不行？也许是你的'使用姿势'还停在2023年]({{ site.baseurl }}/ai-usage-posture-evolution) - AI 使用姿势演进

**安全与风险系列**
- [当Claude Code能直出PPT]({{ site.baseurl }}/claude-code-disrupts-aippt-moat) - AI 工具冲击

---

## 联系方式

如果你对 Clawdbot 安全、AI Agent 风险有问题或想法：

- 邮箱：jason2023zhang@gmail.com
- 微信：winnielove2020
- 博客：[https://junxinzhang.com](https://junxinzhang.com)

特别欢迎讨论：
- AI Agent 的安全边界在哪里
- 个人AI助手的未来形态
- 如何在便利和安全之间找到平衡
- Clawdbot 的使用经验和踩坑记录

---

*本文基于 2026 年 1 月 27 日的公开资料撰写。*

*Clawdbot 仍在快速迭代中，安全状况可能随版本更新而变化——但"高权限AI Agent的安全挑战"这个本质问题，不会因为某次更新就消失。*

---

> **关注我，后续分享更多 AI Agent 认知、洞察以及使用方式。**
>
> 在这个AI Agent开始深入数字生活的时代，保持冷静比追赶热点更重要。
