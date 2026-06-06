---
title: "Improving LM Studio's MLX Engine for Agentic Workflows"
type: article
source: X/Twitter NoteTweet
author: Neil Mehta
url: https://x.com/ostensiblyneil/status/2063006720616734835
created: 2026-06-05
tags: [AI, MLX, AppleSilicon, LMStudio, KVCache, Inference, Optimization]
---

# Improving LM Studio's MLX Engine for Agentic Workflows

**作者：** Neil Mehta，AI @ LM Studio
**平台：** X/Twitter NoteTweet
**链接：** https://x.com/ostensiblyneil/status/2063006720616734835
**相关 PR：** https://github.com/lmstudio-ai/mlx-engine/pull/326

---

## 概述

LM Studio 发布 **mlx-engine v1.8.5**，通过 KV cache checkpointing（检查点）大幅提升重复、长上下文 agentic 工作流的性能，同时为 VLM 请求添加 continuous batching（连续批处理）。

**核心提升：**
- 额外 RAM 使用降低 **80%**
- 吞吐量提升最高 **2x**
- 高分辨率图像请求处理速度提升 **3.5x**

---

## 问题：KV Cache 的 Rewind 难题

当前流行的开源模型（Qwen 3.5/3.6、Gemma 4）使用特殊注意力机制来减少大上下文长度时的 KV cache 内存占用：

- **Qwen 3.5**：混合架构（hybrid architecture）
- **Gemma 4**：滑动窗口架构（sliding window attention）

这些注意力策略使得 KV cache **无法任意回退（rewind）**，给 agentic use case 带来问题——当需要基于之前对话生成新回复时，必须重新计算 KV cache。

### Gemma 4 的推理步骤（示例）

1. **Prompt Prefill**：计算系统提示和用户消息的 KV cache
2. **Decode**：在计算助手推理内容时构建 KV cache
3. **Rewind**：将 KV cache 修整到 step (1)，追加助手消息（不含之前的推理内容）

---

## 解决方案：Disk-Backed KV Cache

### 写入磁盘（Saving to Disk）

- 每隔 **256 token** 边界，将本地注意力层的 KV cache 复制到磁盘
- 后台进程异步将 KV cache 写入磁盘
- Apple Silicon 采用统一内存架构，提交到磁盘后从内存中驱逐
- **效果**：内存使用量与活动序列挂钩，而非所有历史序列

### 从磁盘恢复（Restoring from Disk）

1. 为每个 256 token 块计算 key
2. 确定需要检索哪些 global 和 local KV cache 块
3. 从磁盘加载尽可能多的 KV cache
4. 对于从未计算过（或已被驱逐）的部分，回退到重新预填充
5. 采用 **LRU（最近最少使用）策略**，优化常见使用模式

### 磁盘缓存设计

- 缓存是**临时的**，模型卸载后自动清理，不留持久文件
- 整个缓存是一个临时文件（位于 `/tmp`）
- 多个 KV cache 条目打包进一个文件（safetensors 格式）
- 内存中维护索引表："条目 X 从字节偏移 Y 开始，长度 Z"
- 驱逐时字节范围归还空闲列表，供后续记录复用

---

## 额外优化：Continuous Batching

为 VLM（视觉语言模型）runner 添加了 continuous batching（连续批处理），允许多个请求并发处理。结合 KV cache 优化，mlx-engine 现在可用于严肃的 agentic 工作负载。

> 参考：Hugging Face 的 [continuous batching解释](https://huggingface.co/blog/continuous_batching)

---

## 基准测试（M3 Max MacBook Pro，36GB RAM）

模型：`lmstudio-community/Qwen3.6-27B-MLX-4bit`

### 1. 并行聊天吞吐量

| Runtime | Wall time | Output tokens | End-to-end tok/s | Delta |
|---|---|---|---|---|
| mlx-engine 1.7.0 | 37.60s | 573 | 15.24 | baseline |
| mlx-engine v1.8.5 | 16.78s | 570 | 33.97 | **2.2x faster** |

### 2. 并行长提示的内存使用

| Runtime | RAM after load | RAM after run | Extra RAM | Delta |
|---|---|---|---|---|
| mlx-engine 1.7.0 | 16.66 GB | 23.13 GB | +6.47 GB | baseline |
| mlx-engine v1.8.5 | 16.66 GB | 17.83 GB | +1.18 GB | **82% less** |

### 3. 重复高分辨率图像提示

| Runtime | Request | Cached | Uncached | Wall time | Delta |
|---|---|---|---|---|---|
| mlx-engine 1.7.0 | 1 | 0 | ~3,730 | 30.58s | baseline |
| mlx-engine 1.7.0 | 2 | 0 | ~3,730 | 23.79s | baseline |
| mlx-engine v1.8.5 | 1 | 0 | 3,729 | 28.62s | 1.1x faster |
| mlx-engine v1.8.5 | 2 |3,584 | 145 | **6.88s** | **3.5x faster** |

---

## 下载地址

https://lmstudio.ai/download