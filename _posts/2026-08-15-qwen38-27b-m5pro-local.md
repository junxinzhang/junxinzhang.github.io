---
layout: post
title: "Qwen3.8 27B 在 M5 Pro 64G 上：能跑不是新闻，MLX 快了四成才是"
date: 2026-08-15
author: Jason Zhang
categories: [AI]
image: assets/images/cover-20260815-qwen38-m5pro.webp
tags: [featured, AI, Qwen, Qwen3.8, Ollama, MLX, Apple Silicon, M5 Pro, 本地部署, 评测, Zaokit]
slug: qwen38-27b-m5pro-local
description: >
  Qwen3.8-27B 开源第二天，我在自己的 MacBook Pro M5 Pro 64G 上拉了两个 Ollama 标签。
  官方 Q4_K_M 热身解码 27–29 tok/s，进程 18–20G，8K 上下文没掉交换。
  同机换 MLX nvfp4，解码到 39–40 tok/s。64G 不是入场券，是用来比引擎的。
faq:
  - question: "Qwen3.8 27B 在 M5 Pro 64G 上实际跑多快？"
    answer: "2026-08-15 用 Ollama 0.32.13 实测。官方标签 qwen3.8:27b（Q4_K_M，盘上 17G）热身后解码 26–29 tok/s，3.6K prefill 272 tok/s，进程 RSS 18–20G。同机 qwen3.8:27b-mlx（nvfp4，盘上 18G）解码 39–40 tok/s。数字都来自这台机器，不是官方榜。"
  - question: "16GB 或 24GB 机器能不能跑？"
    answer: "官方 Q4_K_M 文件就是 17G，16GB 卡塞不进。24GB 是入场券，能跑短上下文，长上下文要给 KV cache 留空。64G 的意义不是证明能跑，是同一台机器能并排对比 GGUF 和 MLX，还能开思考、留应用。"
  - question: "默认开思考对本地有什么影响？"
    answer: "思考开关对解码速度影响不大：同一道 LRU 题，官方标签开思考 28.9 tok/s，关思考 26.7 tok/s。真正贵的是 token。写 400 字中文时，思考开着产出 1351 个生成 token，思考正文 1671 字、正文只有 454 字。本地没有 API 账单，但时间是你的。"
  - question: "这篇文章有没有抄官方 SWE-bench？"
    answer: "没有。官方自报 SWE-bench Pro 61.7，我没在这台机器上复现。这篇只报加载时间、RSS、prefill、decode、思考开关，以及两个 Ollama 标签的对比。评测文章最便宜的作弊是抄榜，最贵的诚实是只写自己跑出来的数。"
---

Qwen3.8-27B 的权重是 8 月 13 到 15 号这窗口落地的。Apache 2.0，稠密 27B，自带视觉，原生 262K 上下文。外面立刻开始传：17GB 就能跑，家用显卡入场。

我没去抄这句。今天下午在自己这台 MacBook Pro 上拉了两个标签，数字如下。

> **能跑不是新闻。这台 M5 Pro 64G 上，官方 Q4_K_M 热身解码 27–29 tok/s；换同机的 MLX 标签，解码到 39–40。64G 不是入场券，是用来比引擎的。**

![Qwen3.8 27B 在 M5 Pro 64G 上](/assets/images/cover-20260815-qwen38-m5pro.webp)
<!-- baoyu-skill prompt: 2.35:1清线漫画+清新扁平封面，奶油到天蓝渐变底，干净描边，薄荷绿/蜜桃/天蓝平涂，留白充足。禁止品牌logo与深色赛博UI。画面中央一台银色笔记本，上面坐着标中文「27B」的小机器人，身后淡淡隐去一个巨大「2.4T」影子；桌上一根发光内存条标「64G」，只亮了三分之一。顶部粗体中文「能跑不是新闻」，底部小字「M5 Pro 64G 本地实测」。中文清晰可读。 --ar 2.35:1 -->

## 一、这台机器，和「17GB 能跑」这句话

先把台子摆清楚，免得后文的 tok/s 像从别处抄来的。

| 项目 | 这台机器 |
|------|----------|
| 型号 | MacBook Pro（Mac17,8） |
| 芯片 | Apple M5 Pro |
| CPU | 18 核（6 Super + 12 Performance） |
| GPU | 20 核，Metal 4 |
| 统一内存 | 64 GB |
| 系统 | macOS 26.6.1（25G76） |
| 运行时 | Ollama 0.32.13（Homebrew，Flash Attention 开，KV cache q8_0） |
| 测试日期 | 2026-08-15，上海时区 |

官方仓库是 `Qwen/Qwen3.8-27B`，Apache 2.0。旁边那个 2.4T Max 是另一张许可证，跟这篇无关。Unsloth 和 LM Studio 对外说的地板是 17GB——那是权重大小，不是你开 256K 上下文之后的工作集。

这台机器开测前，本地没有 Qwen3.8 权重。Ollama 也是现装的。拉下来的两个标签：

| 标签 | 量化 | 盘上大小 | 架构 |
|------|------|----------|------|
| `qwen3.8:27b` | Q4_K_M | **17 GB** | qwen35 + CLIP 视觉 |
| `qwen3.8:27b-mlx` | nvfp4 | **18 GB** | qwen3_5，`--mlx-engine` |

这台机器上当时的真实命令输出：

![Ollama 0.32.13 拉下的两个标签](/assets/images/shot-20260815-ollama-list.webp)

下面所有速度，除特别注明外，都走 Ollama HTTP `/api/generate`，`num_ctx=8192`，温度 1 / top_p 0.95 / top_k 20。没有 128K，没有 256K，没有 BF16，也没有复现官方 SWE-bench。

## 二、官方 Q4_K_M：28 tok/s，20G，没掉交换

先跑官方标签。这是大多数人会 `ollama run qwen3.8:27b` 的那一条。

| 任务 | 思考 | 加载 | 预填充 | 解码 | 生成 token | 进程 RSS |
|------|------|------|--------|------|------------|----------|
| 首次加载 | 关 | 4.0 s | 30 t/s | 16.7 t/s | 25 | 18.0 G |
| 热身短答 | 关 | 0.14 s | 105 t/s | **26.1 t/s** | 19 | 18.5 G |
| 线程安全 LRU | 开 | 0.14 s | 54 t/s | **28.9 t/s** | 1194 | 18.9 G |
| 同一道 LRU | 关 | 0.14 s | 134 t/s | **26.7 t/s** | 1585 | 19.4 G |
| 400 字中文 | 开 | 0.16 s | 104 t/s | 15.3 t/s | 1351 | 19.5 G |
| `is_prime` | 关 | 0.16 s | 57 t/s | 28.1 t/s | 91 | 19.7 G |
| 约 3.6K prefill | 关 | 0.17 s | **272 t/s** | 14.0 t/s | 159 | 20.3 G |

命令行再打一条 `ollama run --verbose`（新进程，默认上下文 256K）：加载 7.4 s，解码 **27.6 t/s**。

![官方标签 verbose：解码 27.57 tok/s](/assets/images/shot-20260815-verbose-27b.webp)

看这张表，只抓三件事。

第一，**热身之后，官方 GGUF 就在 27–29 tok/s 这条线上。** 首次加载 4 秒，之后加载都在 0.14–0.17 秒。16.7 那种冷启动数字，不要拿去当日常体感。

第二，**内存很老实。** 进程 RSS 从 18.0G 爬到 20.3G，8K 上下文全程 Swapins=0、Swapouts=0，memory_pressure 没有 warn。压缩内存有，交换没有。官方 runner 报 66/66 层在 GPU，Metal 占用约 16.0 GiB，再加 888 MiB 的 CLIP mmproj。

![加载后进程 18.9G RSS，8K 没掉交换](/assets/images/shot-20260815-rss-loaded.webp)

第三，**长一点的预填充，这台机器吃得动。** 3662 个 prompt token，prefill 272 t/s，首 token 大约 13.4 秒。这不是 256K 长窗口，只是说明 8K 档的预填充不是瓶颈。

![官方 Q4 热身之后就在 28 tok/s](/assets/images/illust-20260815-qwen-ollama-speed.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底、清线描边。银色笔记本吐出一条稳定的薄荷绿 token 缎带，旁边放着一块标中文「17G」的砝码和一只秒表。顶部中文「官方 Q4 热身之后就在 28 tok/s」，底部小字「进程 18 到 20G，8K 没掉交换」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读，禁止深色赛博风。 --ar 2.35:1 -->

## 三、同一台机器换 MLX：40 tok/s

64G 的好处现在才出现：不用换电脑，直接拉 `qwen3.8:27b-mlx`。

同一道 LRU，同一套采样：

| 任务 | 思考 | 加载 | 预填充 | 解码 | 生成 token |
|------|------|------|--------|------|------------|
| LRU | 开 | 0.03 s | 82 t/s | **38.9 t/s** | 2858 |
| 同一道 LRU | 关 | 0.03 s | 167 t/s | **40.5 t/s** | 1166 |

相对官方 Q4_K_M 的 26.7–28.9，这是大约四成的解码加速。量化不是 Q8，是 **nvfp4**，引擎是 `ollama runner --mlx-engine`。

MLX 进程 RSS 不能直接跟 GGUF 比。权重走 Metal/wired，进程本身只有几百 MB；我测的时候还叠过一次官方 runner 的残留，那个 26G 的脏数字不写进结论。卸掉官方标签之后，机器空闲内存回到 61%，没有新的压力。

所以结论很窄，也很硬：

**在这台 M5 Pro 64G 上，想要交互速度，走 MLX 标签；想要对齐社区最常见的 Q4 体感，走官方 GGUF。** 同一份 27B，引擎差一档，手感就不一样。

![同机换 MLX，解码到 40](/assets/images/illust-20260815-qwen-mlx-faster.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底、清线描边。同一台银色笔记本喷出两条 token 缎带：左侧较慢标中文「GGUF 28」，右侧更快更亮标「MLX 40」。顶部中文「同一台机器换 MLX」，底部小字「快了大约四成」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读，禁止深色赛博风。 --ar 2.35:1 -->

## 四、默认开思考，本地更费的是 token

Qwen3.8 默认思考开着。本地没有 API 账单，很多人会以为「开着也无所谓」。

速度上，这件事几乎不成立。官方标签同一道 LRU：开思考 28.9 tok/s，关思考 26.7 tok/s，解码没有变慢。MLX 也一样，开 38.9、关 40.5。

贵的是生成量。

写 400 字中文产品体感、思考开着：一共 1351 个生成 token，思考正文 1671 字，真正给读者的只有 454 字。墙钟 89 秒。同一下午，关思考的短代码题 91 个 token、4 秒结束。

| 任务 | 思考 | 生成 token | 思考字数 | 正文字数 | 墙钟 |
|------|------|------------|----------|----------|------|
| LRU | 开 | 1194 | 429 | 3698 | 42 s |
| LRU | 关 | 1585 | — | 6282 | 60 s |
| 400 字中文 | 开 | 1351 | 1671 | 454 | 89 s |
| `is_prime` | 关 | 91 | — | 247 | 4 s |

本地模型的思考开关，不是「更聪明所以更慢」，是「同一速度下多写一堆你不一定要看的字」。日常写代码、改补丁，先关；真要推一道算法，再开。

![思考开关烧掉的是字，不是显存](/assets/images/illust-20260815-qwen-think-tokens.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底、清线描边。深色书桌上一个拨杆开关，一侧是薄薄一张答案卡片，另一侧是烧着火星的长卷草稿纸。顶部中文「思考开关烧掉的是字」，底部小字「不是显存」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读，禁止深色赛博风。 --ar 2.35:1 -->

## 五、一张自检表：16G / 24G / 64G 怎么选

把官方那句「17GB 能跑」放回硬件账本里。

| 内存 | 能不能跑官方 Q4 | 实际该怎么选 |
|------|------------------|--------------|
| 16 GB | 不能。Q4_K_M 文件就是 17G | 换 9B，或者等更狠的量化，别硬上 27B |
| 24 GB | 能进门，短上下文 | 官方 Q4，关思考，别开 128K |
| 32–48 GB | 能比较舒服地跑 Q4 / Q5 | 日常本地助手够了 |
| **64 GB（这台）** | 很宽裕 | 同一台机器对比 GGUF 和 MLX，思考可以开，应用可以留 |

64G 不是「终于能跑 27B」的门槛。24G 才是入场券。64G 买到的是余量：两个引擎并排、思考开着、浏览器不用关。

这篇没测 128K / 256K，也没测 BF16。BF16 官方权重约 55.6G，这台 64G 理论上塞得进短上下文，长窗口会顶满，我今天没拉。LM Studio 的 MLX 下载中途超时，所以速度只报 Ollama 两条线。

![16G 塞不进，64G 是用来比引擎的](/assets/images/illust-20260815-qwen-64g-ledger.webp)
<!-- baoyu-skill prompt: 2.35:1清新知识漫画，奶油底、清线描边。三根内存条并排：短的一根裂开标中文「16G」，中等一根勉强托住「17G」砝码标「24G」，最长一根大半空着标「64G」。顶部中文「16G 塞不进，64G 是用来比引擎的」，底部小字「24G 才是入场券」。薄荷绿/蜜桃/天蓝平涂，中文清晰可读，禁止深色赛博风。 --ar 2.35:1 -->

## 写在最后

压成五句：

1. **数字都来自这台 M5 Pro 64G**——Ollama 0.32.13，2026-08-15 下午，不是官方榜
2. **官方 Q4_K_M 热身解码 27–29 tok/s**——进程 18–20G，8K 没掉交换，3.6K prefill 272 t/s
3. **同机 MLX nvfp4 解码 39–40 tok/s**——快大约四成，64G 的意义是能并排对比
4. **思考开关不减速，只烧 token**——400 字任务思考 1671 字、正文 454 字
5. **16G 塞不进，24G 才是入场券**——64G 买的是余量，不是入场资格

土话一句：

**能跑只说明你买对了内存，快不快，要看你喂给它的是哪一个引擎。**

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

延伸：[Grok 4.6 和 Gemini 3.7 Flash 同周落地：模型竞争进入淘汰赛](/grok46-gemini37-flash-model-knockout) · [Grok Bot 上线：这场战争才刚刚开始](/grok-bot-cloud-pc-agent-war) · [私有化大模型部署指南](/private-llm-deployment-guide)

---

唯一网站：[Zaokit.app](https://zaokit.app) | Agent 交易平台：[Zaokit.ai](https://zaokit.ai)

企业 Grok 服务：[grok.zaokit.com](https://grok.zaokit.com)

企业服务：[cx.zaokit.com](https://cx.zaokit.com) · [cc.zaokit.com](https://cc.zaokit.com) · [tokenhub.zaokit.ai](https://tokenhub.zaokit.ai) · [gift.junxinzhang.com](https://gift.junxinzhang.com) · [完整产品列表](https://junxinzhang.com/projects.html)

稳定靠谱的 AI 全家桶，开箱即用。

---

*我是 Jason，自己一个人做 AI 产品。本地评测最便宜的作弊是抄榜——数字只能从自己桌上的那台机器出。*
