# Jekyll 网站

这是一个基于 Jekyll 的静态网站。Jekyll 是一个简单的、博客友好的静态站点生成器，使用 Ruby 编写。它将您的内容与布局结合，生成静态 HTML 文件，这些文件可以由任何 Web 服务器进行托管。

## 必备条件

在开始之前，请确保您的系统已安装以下软件：

- [Ruby](https://www.ruby-lang.org/zh/documentation/)（版本 >= 3.0）
- [Bundler](https://bundler.io/)（通过 `gem install bundler` 安装）
- [Jekyll](https://jekyllrb.com/)（通过 `gem install jekyll` 安装）
- [Git](https://git-scm.com/)

对于 macOS 用户，请确保已安装 [Homebrew](https://brew.sh/) 以便安装依赖。

## 安装

1. 克隆该仓库：

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. 安装所需的 Ruby gem：

   ```bash
   bundle install
   ```

## 启动开发环境

要启动本地开发服务器并查看您的网站：

```bash
bundle exec jekyll serve
```

服务器启动后，您可以在浏览器中访问：

http://localhost:4000

## 目录结构

以下是该项目目录结构的简要说明：

- `_config.yml`：Jekyll 配置文件，在此文件中可以设置站点的全局选项。
- `_posts/`：存放博客文章或其他 Markdown 格式的内容。
- `_layouts/`：存放布局文件（HTML 模板）。
- `_includes/`：存放可复用的片段或部分模板。
- `_sass/`：存放用于站点 CSS 的 SCSS 文件。
- `assets/`：存放图片、CSS 和 JavaScript 文件。
- `index.md`：站点的主页。