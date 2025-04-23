# HTML页面集成指南

本目录用于存放HTML页面，这些页面将在网站首页显示。

## 如何添加新的HTML页面

1. 将HTML文件复制到此目录 (`_html_pages/`)
2. 在 `_data/html_pages.yml` 文件中添加页面信息，格式如下：

```yaml
- title: 页面标题
  path: 文件名.html
  description: 页面简短描述
  date: YYYY-MM-DD
```

3. 重新构建网站（如果需要）

## 注意事项

- HTML文件应该是完整的独立页面，包含所有必要的CSS和JavaScript
- 页面将在新标签页中打开，保持原有样式
- 如果需要添加缩略图，可以在 `_data/html_pages.yml` 中添加 `image` 字段，并将图片放在 `assets/images/html_thumbnails/` 目录下
