# Homebrew软件包管理器从入门到精通

## 作者信息
- **作者**：AI少年 (@aehyok)
- **平台**：X (Twitter)
- **发布时间**：2026年4月10日 16:56
- **原始链接**：https://x.com/i/status/2042527221332508866
- **浏览量**：5.5万

## 核心内容

### 什么是Homebrew
macOS的包管理器，可以一条命令安装命令行工具和图形界面应用。

### 为什么推荐Homebrew
- 安装方便：一条命令就能装好
- 管理省心：更新、卸载都很方便
- 自动补齐：缺什么依赖，它会帮你一起装
- 卸载干净：不容易留下乱七八糟的文件
- 软件很多：常见开发工具基本都能装

### 安装步骤
1. 安装Xcode命令行工具：`xcode-select --install`
2. 安装Homebrew：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. 配置PATH环境变量
4. 验证：`brew --version`

### 常用命令
- 安装：`brew install <软件>` / `brew install --cask <应用>`
- 更新：`brew update` / `brew upgrade`
- 搜索：`brew search <关键词>` / `brew info <软件>`
- 清理：`brew doctor` / `brew cleanup`

### 重要原则
永远不要用 sudo brew 来安装软件。Homebrew设计就不需要管理员权限。

---

## 数据亮点
- 浏览量：5.5万
- 转发：19
- 评论：37
- 点赞：180
