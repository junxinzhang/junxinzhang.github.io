# SEO P1 执行清单（Google Search）

## 1. 发布后 10 分钟内
1. 访问以下页面确认 `200` 且页面源码只有 1 个 canonical：
- `https://junxinzhang.com/`
- `https://junxinzhang.com/posts.html`
- `https://junxinzhang.com/categories.html`
- `https://junxinzhang.com/tags.html`
2. 确认以下页面含 `noindex`：
- `https://junxinzhang.com/_html_pages/claude-plugins-report.html`
- `https://junxinzhang.com/_html_pages/enhanced_network_report.html`
- `https://junxinzhang.com/_html_pages/gpu_aws_cost_comparison.html`
- `https://junxinzhang.com/_html_pages/vendor_prd_access_control.html`
- `https://junxinzhang.com/assets/html/claude-plugins-report.html`
3. 确认以下非内容页含 `noindex`：
- `https://junxinzhang.com/404.html`
- `https://junxinzhang.com/offline.html`

## 2. Search Console 操作（当天）
1. 打开 Search Console -> `Sitemaps`，重新提交：
- `https://junxinzhang.com/sitemap.xml`
2. 使用 `URL Inspection` 提交以下 URL 重新抓取：
- `/`
- `/posts.html`
- `/categories.html`
- `/tags.html`
- `/category-ai.html`
- `/category-devops.html`
- `/category-technology.html`
- `/category-business.html`
- `/category-career.html`
- `/category-growth.html`

## 3. 一周内观察项
1. `Page indexing`：
- 观察 `Crawled - currently not indexed` 是否下降。
- 观察重复页面（Duplicate without user-selected canonical）是否下降。
2. `Search results`：
- 查询词：`Just Jason`、`junxinzhang`、`Jason Zhang AI`
- 观察品牌词点击是否向首页和 Hub 页集中。
3. `Enhancements / Rich results`：
- 验证 `CollectionPage` 和 `ItemList` 无报错。

## 4. 两周后复盘
1. `site:junxinzhang.com` 检查索引面是否以文章页和 Hub 页为主。
2. 品牌词 SERP 是否出现稳定子链接（Posts/Categories/Tags/Projects）。
3. 若子链接仍不稳定，下一步执行：
- 增强首页到 Hub 页的文案锚文本一致性。
- 提升 Hub 页内部链接密度（每页添加“相关栏目推荐”模块）。
- 为高频分类增加独立静态落地页（如 `/category-ai.html`）。

## 5. P2 新增 URL（建议提交抓取）
- `/category-ai.html`
- `/category-devops.html`
- `/category-technology.html`
- `/category-business.html`
- `/category-career.html`
- `/category-growth.html`
