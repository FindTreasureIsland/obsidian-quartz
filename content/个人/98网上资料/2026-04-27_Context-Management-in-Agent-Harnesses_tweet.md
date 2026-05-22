---
title: Context Management in Agent Harnesses
author: 
source: X.com
tags: [AI, Agent, Context Management, OpenClaw, Claude Code]
date: 2026-04-27
stats:
  likes: 35
  retweets: 7
  views: 10498
---

# Context Management in Agent Harnesses

**来源**：https://x.com/i/status/2048492731929149929

---

## 核心观点

Every agent harness runs into the same limit: the context window is too small for everything the model might want to remember.

As sessions grow, file reads expand, subagent calls multiply, and tool outputs pile up, the harness has to decide what stays in the working set, what gets compressed, and what gets retrieved later.

**The important question is no longer just what goes into the prompt. It is how the harness manages context over time.**

The best systems do not treat the context window like a passive transcript buffer. They manage it actively.

---

## 四大Agent Harness的上下文管理策略

### Pi (pi-mono)

**File Reads:**
- Hard cap: 2,000 lines or 50KB, whichever hits first
- Content is head-truncated
- Appends explicit continuation nudge: `[Showing lines 1-2000 of 50000. Use offset=2001 to continue.]`

**Compaction:**
- Trigger: Estimated context tokens exceed `contextWindow - reserveTokens` (default reserve: 16,384 tokens)
- Walks backward through conversation, keeping most recent ~20,000 tokens
- Everything older gets summarized by LLM
- Summary becomes synthetic user message prepended to kept tail
- Never cuts at orphaned tool result

### OpenClaw

**File Reads:**
- Inherits Pi's 2K line / 50KB truncation
- Additional caps for bootstrap files: 12,000 chars per file, 60,000 chars total
- Uses 75% head / 25% tail split when bootstrap file exceeds budget

**Tool Results:**
- 16,000 chars or 30% of context window, whichever is smaller
- Switches to head+tail mode when tail looks "important" (errors, JSON close braces, summary keywords)

**Compaction (two distinct mechanisms):**
- Trigger: History exceeds 50% of context window
- History split into equal-mass token chunks; oldest chunk dropped
- Dropped content goes through staged multi-pass LLM summarization
- **Pre-compaction flush**: Silent agentic turn lets agent persist state to memory files before history disappears

### Claude Code

**File Reads (two-layer defense):**
- First gate: 256KB byte cap checked via stat call before file is opened
- Second gate: Token-counted against 25,000 token budget after read
- Both limits are remotely tunable via GrowthBook feature flags
- Tool defaults to returning 2,000 lines from beginning
- **File dedup system**: Re-reads at same range return stub instead of full content

**Compaction:**
- Trigger: Estimated tokens exceed effective context window minus 13,000-token buffer
- Full conversation sent to model with structured 9-section prompt
- Summary becomes user message telling model session is being continued
- Post-compact: Up to 5 recently-read files re-attached within token budget
- **Pre-query optimization**: Every API call runs pipeline managing tool results

**Tool Result Offloading:**
- Oversized tool results persisted to disk, replaced with 2KB previews
- Per-tool cap: 50,000 characters
- Per-message aggregate cap: 200,000 characters

### Letta

**File Reads (fundamentally different approach):**
- Every uploaded file is parsed, chunked, and embedded into a vector store
- Three file tools: `open_files` (raw text), `grep_files` (exact pattern), `semantic_search_files` (meaning-based)
- Visible content truncated to per-file character limit scaling with context window:
  - 5,000 chars for 8K context
  - 15,000 for 32K
  - 25,000 for 128K
  - 40,000 for 200K+
- LRU policy evicts least-recently-accessed files

**Compaction:**
- Trigger: Context usage exceeds 90% of context window
- Sliding window eviction starts at 30% of messages
- **Self-compact mode**: Uses agent's own model to summarize
- Two-stage fallback: clamp tool returns to 5,000 chars, then middle-truncate

---

## Sub-agent Context Management

| Harness | Sub-agent Approach |
|---------|-------------------|
| Pi | New process per task, task string as only user message, no parent history |
| OpenClaw | Fresh isolated sessions by default; fork mode copies parent's transcript |
| Claude Code | Default: blank conversation; fork path: full parent message history |
| Letta | No fork; tools run within main agent loop, accessed through search tools |

---

## 设计的收敛点

The most striking finding is not how different they are. It is how much they agree.

**All four harnesses:**
- Hard-cap file reads
- Support offset/limit pagination
- Cap tool result sizes
- Isolate sub-agent sessions
- Run LLM-powered compaction triggered by token threshold
- Estimate context usage and detect pressure

**Specific design choices that rhyme:**
- Pi and OpenClaw both head-truncate file reads and append continuation nudge
- Claude Code and OpenClaw both persist oversized tool results to disk
- Pi, OpenClaw, and Claude Code all enforce tool-call/result boundary safety during compaction

---

## 核心洞察

> 50 years of computing taught us that the best memory management is the kind the program never thinks about. Registers, cache lines, page tables, swap. Each layer managed by the system, each invisible to the layer above. The program just runs.

**Agent harnesses are moving in the same direction.**

The goal is not to show the model everything. It is to give it the right working set at the right time and allow it to dynamically make decisions to manage its own context.

---

**原文链接**：https://x.com/i/status/2048492731929149929
