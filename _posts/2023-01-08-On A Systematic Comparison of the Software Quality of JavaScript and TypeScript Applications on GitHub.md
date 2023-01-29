---
layout: post
title:  "一分钟读论文：《要不要上 TypeScript？GitHub 上 JS 和 TS 应用软件质量的系统比较》"
author: unbug
categories: [ TypeScript, JS ]
image: assets/images/screenshot-20230109-113530.jpeg
tags: [featured]
---
你的团队是否还在纠结要不要将项目改成 TypeScript 呢？改成 TypeScript 应用的 bug 能得到收敛吗？德国斯图加特大学软件工程研究所的这篇新论文[《To Type or Not to Type? A Systematic Comparison of the Software Quality of JavaScript and TypeScript Applications on GitHub》][paper1-url]能给你答案。

论文作者基于 604 个 GitHub 项目（299 个用于 JS，305 个用于 TS）进行了挖掘，`这些项目的代码行数（LoC）超过 1600 万`。 通过 SonarQube 和 GitHub API 分析了软件质量的几个方面：
- a) 代码质量（每个 LoC 的代码味道数）；
- b) 代码可理解性（每个 LoC 的认知复杂度）；
- c) bug 倾向性（bug 提交率）；
- d) bug 解决时间（平均 bug issue commit 的时间）;
- 对于 TS，还通过 ESLint 收集了每个项目忽略 any 类型安全的频率。

**论文研究问题和假说的结论：**
1. TypeScript 应用的代码味道（code smells）比 JavaScript 应用少得多，即`代码质量更好`。
2. TypeScript 应用的认知复杂性明显低于 JavaScript 应用，即`更好的代码可理解性`。
3. TypeScript 应用比 JavaScript 应用具有`更高的 bug 提交率`，即更容易或同样容易出现 bug。
4. TypeScript 应用比 JavaScript 应用`花费更多`或相等的时间来解决 bug。
5. 使用 any 类型的频率与 TypeScript 应用中的代码异味数量`呈正相关`但微弱相关 (𝜌 = 0.26)。
6. 使用 any 类型的频率与 TypeScript 应用中的认知复杂性`呈正相关`但微弱相关 (𝜌 = 0.19)。
7. 在 TypeScript 应用中，使用 any 类型的频率与 bug 修复率之间`没有显著相关性`。
8. 使用 any 类型的频率与 TypeScript 应用中的 bug解决时间`呈正相关`但微弱相关 (𝜌 = 0.17)。

![summary]({{ site.baseurl }}/assets/images/screenshot-20230109-114345.jpeg)

## References
- [SonarQube][links-1]


[paper1-url]: https://arxiv.org/pdf/2203.11115.pdf
[links-1]: https://en.wikipedia.org/wiki/SonarQube