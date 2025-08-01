---
layout: post
title: "一个人两个月开发计量轮换管理系统"
author: Jason Zhang
categories: [项目实战, 系统开发, 电力行业, 数字化改造]
image: assets/images/screenshot-20250724-meterinfoapp.jpg
tags: [计量轮换, 管理系统, React Native, Spring Boot, MongoDB, 离线作业]
---

这两个月，发小找到我，说他们电力公司最近换电表快被材料整疯了，照片堆成山、数据对不上、人手也不够……我听完也挺上头的，直接说一句：

> "要不我给你整套系统？"

于是就开始了这趟旅程——**一个人、两个月、从零开始开发**，做了一套完整的"计量轮换管理系统"，Web + App 都有，已经部署上线，**真正在用，~_~真正在救命**。

---

## 🧩 为什么要做这个系统？

我老家电力公司每年都要大批量换电表，覆盖城区、小区、农牧区，换表流程全靠**人工+微信群+Excel**，过程堪称灾难：

- 工人现场拍照后手抄数据，回来还得录入 Excel
- 所有照片靠微信群传，文件一多全乱套
- 管理员一个个核对照片和表单，哪个表是谁的全靠猜
- 数据错了还得返工，有时候来回 100 多公里

我当时就一个念头：**都 2025 年了，这种事不应该靠人脑记，应该靠系统管。**

---

## 🚧 怎么做的？

用的就是晚上 + 周末的时间，纯 vibe coding 模式。  
从架构设计 → 接口实现 → 页面写 UI → MongoDB 索引 → 图片压缩 → OCR → 离线缓存 → Docker 部署，一步步撸出来的。

两个多月，**没有产品经理，没有测试，没有 UI 设计，全靠自己扛。**

---

## ✨ 系统长什么样？

### 🖥 Web 管理后台

- 三类表单统一管理（公台 / 专台 / 用户）
- 电表照片自动识别（用了 LLM 多模态模型）
- 权限分级（施工队只能录入，管理员能导出统计）
- 图片自动压缩 + 本地存储优化
- 数据统计图表一应俱全，支持导出 Excel 报表

### 📱 移动端 App （ React Native ）

- **支持离线作业**，无网环境下也能录入保存
- 拍完表计照片一键上传，啥照片都支持（条码、倍率、CT 比值）
- 草稿自动保存，操作中断不丢数据
- 一有网就自动同步，后台悄悄传上去
- 一个 App 兼容 iOS 和安卓（ Expo 开发是真的省事）

---

## 🔧 技术栈怎么选的？

| 模块       | 技术方案                      |
|------------|-------------------------------|
| 后端       | Spring Boot 3.4.5 + Java 17   |
| 数据库     | MongoDB （文档结构更灵活）    |
| App 开发   | React Native + Expo           |
| 部署       | Docker + Docker Compose       |
| 架构风格   | 前后端分离 + 容器化部署       |

---

## 📸 系统实拍图（ App 页面）

![系统截图]( https://i.imgur.com/WksnYSG.jpeg)

---

## 💼 已经跑起来了 ✅

- ✅ 使用单位：**供电公司下属施工队、材料员、档案员**
- ✅ 使用人群：施工队、材料员、档案管理员等
- ✅ 平均每天提交超 **600+ 条表单**
- ✅ 30+ 一线员工已经在用，系统稳定，几乎不用管

---

## 🤝 如果你是……

- 电力行业从业者，做计量/运维/工程/设备的
- 想给县、旗、区级单位做"数字化改造"的人
- 对 OCR 、多模态识别、离线系统开发感兴趣的开发者

d2lubmllbG92ZTIwMjA= 都欢迎聊聊！这个系统是**可以推广复用的**，我也愿意继续打磨、扩展，甚至一起搞点事情。

---

> **技术不是为了炫技，而是为了让人少跑路、少返工、少出错。**
>  
> 愿所有基层数字化系统都能接地气、真好用。