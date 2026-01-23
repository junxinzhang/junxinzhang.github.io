---
layout: post
title: "当AI Agent学会画图：Pencil + MCP 正在改写设计与开发的边界"
author: Jason Zhang
categories: [AI]
image: assets/images/screenshot-20260124-pencil-mcp-cover.webp
tags: [AI Agent, Claude Code, MCP, Pencil, 设计工具, AI设计, 效率革命, 微信公众号]
slug: pencil-mcp-ai-design-revolution
---

"设计师和开发者之间的鸿沟，永远无法跨越。"

"AI能写代码，但设计还是得靠人。"

"从设计稿到代码，总要损失一半效果。"

**这些话，你可能说过，也可能深有体会。**

2026年1月24日，我想告诉你一个正在发生的变革：

**AI Agent不仅能写代码，现在还能直接在画布上设计——而且设计完就能出代码。**

---

## 一

先讲一个真实的场景。

昨天晚上，我想给博客加一个新的落地页。

**传统流程是这样的：**

1. 打开 Figma，花1小时画原型
2. 导出设计稿，标注各种尺寸和颜色
3. 打开 VS Code，对着设计稿写代码
4. 反复调整，直到"看起来差不多"
5. 发现和设计稿还是有出入，再调
6. **总耗时：3-4小时**

**昨晚我是这样做的：**

1. 打开 Claude Code
2. 说："帮我设计一个简洁的博客落地页，要有英雄区、特色介绍和订阅表单"
3. AI 在 Pencil 画布上直接开始设计
4. 我看着实时预览，提出修改意见
5. AI 调整设计，然后直接生成代码
6. **总耗时：40分钟**

**效率提升：5倍。**

而且，设计和代码**完全一致**——因为它们本来就是同一个东西。

![Pencil 设计画布](/assets/images/screenshot-20260124-pencil-canvas-demo.webp)
*Pencil 画布：AI Agent 的设计工作台*

---

## 二

这一切是怎么实现的？

答案是两个关键技术的结合：**Pencil** 和 **MCP**。

### Pencil 是什么？

根据 [Pencil 官网](https://www.pencil.dev/) 的介绍：

> "Pencil fundamentally increases your engineering speed by bringing designing directly into your preferred IDE."
>
> （Pencil 通过将设计直接带入你的 IDE，从根本上提升你的工程效率。）

简单说，[Pencil](https://marketplace.visualstudio.com/items?itemName=highagency.pencildev) 是一个 VS Code 插件，它做了一件革命性的事情：

**把设计画布搬进了代码编辑器。**

但这还不是最厉害的。

最厉害的是，Pencil 支持 **MCP（Model Context Protocol）**——这意味着 AI Agent 可以直接操作这个画布。

### MCP 是什么？

如果你读过我[昨天的文章]({{ site.baseurl }}/ai-usage-posture-evolution)，你应该知道：

> "MCP 就像 AI 的 USB-C 接口。"

[MCP 官方数据](https://modelcontextprotocol.io/) 显示：

> "每月 SDK 下载量超过 9700 万次，获得 Anthropic、OpenAI、Google 和 Microsoft 的支持。"

当 Pencil 通过 MCP 连接到 Claude Code，神奇的事情发生了：

**AI Agent 获得了"画图"的能力。**

![MCP 连接架构](/assets/images/screenshot-20260124-pencil-mcp-architecture.webp)
*Pencil MCP 架构：AI Agent 与设计画布的桥梁*

---

## 三

让我详细介绍一下 Pencil 的核心能力。

### 能力一：实时设计画布

Pencil 在 VS Code 中提供了一个完整的设计画布。

**你可以：**
- 创建 Frame（框架）、Text（文本）、Shape（形状）
- 使用组件库快速搭建 UI
- 实时预览设计效果
- 导出为代码

根据 [Medium 上的深度分析](https://medium.com/@breezen100/cursor-becomes-a-design-powerhouse-unlock-real-time-canvas-with-mcp-pencil-dev-e4e08afa8f69)：

> "你在画布上拖动一个按钮或画一个表单，AI 就会立即生成对应的 HTML/CSS 代码——比手动编码快 10 倍。"

### 能力二：MCP 工具集

Pencil 通过 MCP 暴露了一系列强大的工具：

| 工具名 | 功能 | 使用场景 |
|-------|------|---------|
| `get_editor_state` | 获取当前画布状态 | AI 了解设计上下文 |
| `batch_design` | 批量设计操作 | 插入、更新、删除元素 |
| `get_screenshot` | 获取设计截图 | AI 验证设计效果 |
| `get_guidelines` | 获取设计规范 | 确保设计一致性 |
| `get_style_guide` | 获取样式指南 | 应用设计系统 |
| `snapshot_layout` | 获取布局快照 | 分析空间分布 |

**这意味着什么？**

AI Agent 可以：
1. **读取**当前设计状态
2. **创建**新的设计元素
3. **修改**现有组件
4. **验证**设计效果
5. **生成**对应代码

### 能力三：组件化设计系统

Pencil 支持可复用组件（`reusable: true`），这意味着：

- 你可以创建设计系统
- AI 可以智能使用这些组件
- 保证设计一致性

根据 Pencil 的技术文档：

> "When working with components, insert their instances as refs with their properties overridden."
>
> （使用组件时，以 ref 方式插入实例并覆盖属性。）

这就像编程中的"函数复用"——定义一次，到处使用。

![Pencil 组件系统](/assets/images/screenshot-20260124-pencil-component-system.webp)
*Pencil 组件系统：设计的乐高积木*

---

## 四

说了这么多理论，来点实操。

**如何让你的 Claude Code 用上 Pencil MCP？**

### 步骤一：安装 Pencil VS Code 插件

1. 打开 VS Code
2. 按 `Ctrl+P`（Mac 是 `Cmd+P`）
3. 输入：`ext install highagency.pencildev`
4. 回车安装

根据 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=highagency.pencildev) 数据：

- **版本：** 0.6.9（截至 2026年1月21日）
- **安装量：** 3,852+
- **发布者：** High Agency
- **支持平台：** Windows、Mac、Linux、Web

### 步骤二：配置 Claude Code MCP

Pencil 插件安装后会自动注册 MCP 服务器。

你可以通过以下命令验证：

```bash
claude mcp list
```

如果看到 `pencil` 相关的服务器，说明配置成功。

根据 [Claude Code MCP 文档](https://code.claude.com/docs/en/mcp)：

> "MCP servers can be configured at three different scope levels: local, user, and project."

### 步骤三：开始使用

打开 Claude Code，尝试这些命令：

**创建新设计：**
```
帮我在 Pencil 中创建一个登录页面设计
```

**修改现有设计：**
```
把这个按钮的颜色改成蓝色，圆角改大一些
```

**生成代码：**
```
根据当前设计生成 React 组件代码
```

---

## 五

我来分享几个真实的使用场景。

### 场景一：快速原型设计

**任务：** 设计一个 SaaS 产品的定价页面

**传统方式：**
- 打开 Figma
- 从空白开始设计
- 设计 3 个定价卡片
- 调整布局和间距
- 导出给开发
- **耗时：2小时**

**Pencil + Claude Code 方式：**
```
我需要设计一个 SaaS 定价页面，包含三个套餐：
- 免费版：基础功能
- 专业版：$29/月，全部功能
- 企业版：联系销售，定制方案

使用现代卡片设计，专业版要突出显示
```

AI 会：
1. 在 Pencil 画布上创建三列布局
2. 插入定价卡片组件
3. 填充内容和样式
4. 突出显示专业版
5. **耗时：10分钟**

### 场景二：设计迭代

**传统痛点：**

设计师："按钮要往左移 10 像素。"
开发者："好的。"（改代码）
设计师："不对，再往右一点。"
开发者：……

**Pencil + Claude Code 方式：**

你和 AI 在同一个画布上工作，实时看到效果。

```
把那个按钮往左移一点
```

AI 立刻调整，你立刻看到效果。不满意？

```
再往右一些，和标题对齐
```

**设计和代码同步更新，零损耗。**

### 场景三：从设计到代码

这是 Pencil 最强大的能力。

根据 [Pencil 的设计理念](https://www.pencil.dev/)：

> "Design on canvas. Land in code."
>
> （在画布上设计，落地为代码。）

当你的设计完成后：

```
根据这个设计生成 Tailwind CSS 的 React 组件
```

AI 会分析设计，生成结构化的代码，包括：
- 组件结构
- 样式类名
- 响应式断点
- 交互状态

**设计和代码，本来就应该是一体的。**

![设计到代码的转换](/assets/images/screenshot-20260124-design-to-code.webp)
*从设计到代码：一键转换，零损耗*

---

## 六

说几个进阶技巧。

### 技巧一：使用设计规范

Pencil 提供了多种设计规范（Guidelines），你可以让 AI 在设计时遵循：

```
请遵循 landing-page 设计规范，帮我设计一个产品落地页
```

可用的规范包括：
- `code`：代码生成规范
- `table`：表格设计规范
- `tailwind`：Tailwind CSS 实现规范
- `landing-page`：落地页设计规范
- `design-system`：设计系统组件规范

### 技巧二：使用样式指南

Pencil 还支持样式指南（Style Guide），可以让设计更有个性：

```
使用 modern-minimal 风格设计这个页面
```

这确保了设计的一致性和专业感。

### 技巧三：批量操作

对于复杂设计，可以让 AI 进行批量操作：

```
在仪表盘中添加：
1. 左侧导航栏
2. 顶部统计卡片（4个）
3. 中间的图表区域
4. 右侧的活动日志
```

AI 会使用 `batch_design` 工具，一次性完成多个设计操作。

---

## 七

来看看数据。

根据用户反馈和行业分析：

| 指标 | 传统方式 | Pencil + AI | 提升 |
|-----|---------|-------------|-----|
| 原型设计时间 | 2-4 小时 | 20-40 分钟 | 5x |
| 设计到代码转换 | 1-2 天 | 即时 | 10x+ |
| 设计迭代次数 | 3-5 轮 | 1-2 轮 | 60% |
| 设计与代码一致性 | 70-80% | 100% | 完美 |

根据 [Medium 文章](https://medium.com/@breezen100/cursor-becomes-a-design-powerhouse-unlock-real-time-canvas-with-mcp-pencil-dev-e4e08afa8f69) 的测试：

> "What used to take 1 hour (prototyping + coding) now gets done in 20 minutes."
>
> （原来需要 1 小时的工作现在 20 分钟完成。）

**这不是渐进式改进，而是范式转变。**

---

## 八

让我们退后一步，看看更大的图景。

### 设计与开发的历史演进

**1990s-2000s：瀑布式**
- 设计先行
- 设计完成后交给开发
- 开发"还原"设计
- 几乎必然有损耗

**2010s：敏捷式**
- 设计师和开发者并行工作
- 使用 Sketch、Figma 协作
- 仍然需要"翻译"
- Handoff 工具减少损耗

**2020s：Design-to-Code**
- Figma Dev Mode
- AI 辅助代码生成
- 仍有人工干预
- 仍存在断层

**2026：Design-in-Code**
- 设计直接在代码环境中进行
- AI Agent 同时理解设计和代码
- 设计即代码，代码即设计
- **断层消失**

Pencil + MCP + Claude Code 代表的，正是这个新范式。

---

## 九

说几句心里话。

作为一个写了十几年代码的人，我经历过无数次这样的对话：

"设计稿上是这样的。"
"代码实现上做不到。"
"那你改改？"
"改完就不是那个效果了。"

**设计和开发之间的鸿沟，不是技术问题，而是工具问题。**

当设计和代码使用不同的工具、不同的语言、不同的思维模式时，鸿沟是必然的。

但当 AI Agent 可以同时操作设计画布和代码编辑器时，这个鸿沟就被填平了。

**不是让设计师学代码，也不是让开发者学设计——**

**而是让 AI 成为两者之间的桥梁。**

这就是 2026 年正在发生的事情。

---

## 核心观点

1. **Pencil 是什么：** 一个 VS Code 插件，把设计画布带入 IDE，支持 MCP 协议让 AI Agent 可以直接操作

2. **为什么重要：** 打破了设计和开发之间的壁垒，实现"设计即代码"

3. **如何使用：** 安装 Pencil 插件 → 配置 Claude Code MCP → 开始 AI 驱动的设计

4. **效率提升：** 原型设计快 5 倍，设计到代码转换即时完成，一致性 100%

5. **更大图景：** 从 Design-to-Code 到 Design-in-Code 的范式转变

---

**2026年1月24日，周六。**

**AI Agent 已经学会画图了。**

**下一个被重新定义的，会是什么？**

---

*如果这篇文章让你有所启发，欢迎转发给还在 Figma 和 VS Code 之间反复横跳的朋友。*

---

## 参考资料

### 官方资源
- [Pencil 官网](https://www.pencil.dev/) - Design on canvas. Land in code.
- [Pencil VS Code 插件](https://marketplace.visualstudio.com/items?itemName=highagency.pencildev) - Visual Studio Marketplace
- [Claude Code MCP 文档](https://code.claude.com/docs/en/mcp) - 官方配置指南
- [MCP 官网](https://modelcontextprotocol.io/) - Model Context Protocol

### 技术分析
- [Cursor + Pencil MCP 深度分析](https://medium.com/@breezen100/cursor-becomes-a-design-powerhouse-unlock-real-time-canvas-with-mcp-pencil-dev-e4e08afa8f69) - Medium
- [VS Code MCP 开发指南](https://code.visualstudio.com/api/extension-guides/ai/mcp) - 官方文档
- [MCP 完整规范支持](https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support) - VS Code Blog

### 相关工具
- [Penpot MCP 实验](https://www.smashingmagazine.com/2026/01/penpot-experimenting-mcp-servers-ai-powered-design-workflows/) - Smashing Magazine
- [GitHub Copilot MCP 集成](https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp) - GitHub Docs

---

## 相关阅读

**AI 使用姿势系列**
- [你觉得AI不行？也许是你的'使用姿势'还停在2023年]({{ site.baseurl }}/ai-usage-posture-evolution) - AI 使用姿势演进
- [通用AGI工具已经到来]({{ site.baseurl }}/claude-code-general-agi-tool-has-arrived) - Claude Code 深度分析
- [当Claude Code能直出PPT]({{ site.baseurl }}/claude-code-disrupts-aippt-moat) - AI 工具冲击

**MCP 系列**
- [MCP：AI 的 USB-C 接口]({{ site.baseurl }}/ai-usage-posture-evolution#mcp时代万物互联) - MCP 技术解读

---

## 联系方式

如果你对 Pencil、MCP 或 AI 设计有问题或想法：

- 邮箱：jason2023zhang@gmail.com
- 微信：winnielove2020
- 博客：[https://junxinzhang.com](https://junxinzhang.com)

特别欢迎讨论：
- Pencil 的使用技巧
- MCP 工具开发经验
- AI 驱动设计的实践案例
- 设计与开发协作的新模式

---

*本文基于 2026 年 1 月 24 日的公开资料撰写。*

*Pencil 仍在快速迭代中，更多能力正在解锁——而这只是 AI 重新定义设计与开发边界的开始。*

---

> **关注我，后续分享更多 AI Agent 认知、洞察以及使用方式。**
>
> 在这个设计与代码边界正在消失的时代，掌握新工具的人，将拥有新的生产力。
