# Mac本地跑AI模型：Ollama安装指南

## 作者信息
- **作者**：Lonely__MH (@Lonely__MH)
- **平台**：X (Twitter)
- **发布时间**：2026年4月6日 13:38
- **原始链接**：https://x.com/Lonely__MH/status/2041027838531506625
- **浏览量**：19万

## 核心内容

### 第一步：安装 Homebrew
去 brew.sh 复制安装命令，在终端执行。

### 第二步：安装 Ollama
Ollama 负责模型的下载、加载和运行，还自带一个本地 API。

```bash
brew install --cask ollama
```

看到 "🍺 ollama-app was successfully installed!" 表示安装成功。

### 第三步：选模型下载

**推荐模型：**
- **Gemma 4** — 谷歌 DeepMind 2025年发布，支持多模态，上下文128K-256K
- **Qwen3.5** — 阿里通义，支持201种语言，内置"思考模式"

```bash
# 下载 Gemma 4
ollama run gemma4:26b

# 下载 Qwen3.5
ollama run qwen3.5:27b
```

### 第四步：验证跑起来了
输入测试：
```
>>> 你是谁？
```

### 第五步（可选）：图形界面
下载 Ollama 官方 app，有完整聊天界面，支持文件拖拽。
地址：ollama.com/download

### 进阶接入工具
- Open WebUI：网页版对话界面
- Cherry Studio：桌面客户端，支持多模型切换
- Claude Code：命令行编程助手

### 常见问题
1. brew 命令报错 → 检查 Homebrew 是否装好
2. 模型下载中断 → 重新执行 ollama run 模型名，支持断点续传
3. 速度特别慢 → 可能是内存不够，换更小的版本

---

## 数据亮点
- 浏览量：19万
- 转发：15
- 评论：98
- 点赞：326
