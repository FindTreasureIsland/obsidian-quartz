---
title: "Chain-of-Agents (CoA), a framework for long text tasks"
source: "https://www.linkedin.com/pulse/chain-of-agents-coa-framework-long-text-tasks-theturingpost-harnf"
author:
  - "[[TuringPost]]"
published: 2025-01-26
created: 2025-03-05
description: "Google Cloud AI Research and Penn State University proposed a Chain-of-Agents (CoA) framework that uses multiple AI agents working together to reason through long texts. It outperforms RAG and full-context processing by up to 10%! Here's how CoA works: 1."
tags:
  - "clippings"
---
[Google Cloud](https://www.linkedin.com/showcase/google-cloud/?trk=article-ssr-frontend-pulse_little-mention) AI Research and [美国宾夕法尼亚州立大学](https://www.linkedin.com/school/penn-state-university/?trk=article-ssr-frontend-pulse_little-mention) proposed a Chain-of-Agents (CoA) framework that uses multiple AI agents working together to reason through long texts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

It outperforms RAG and full-context processing by up to 10%!            

Here's how CoA works:            

1\. Worker agents:            

Each worker agent processes different parts of the text (smaller chunks), combines it with the previous agent’s findings, and passes the result, called a "communication unit", to the next worker.            

• For question answering, the workers extract evidence from their chunks.            

• For summarization, they summarize their assigned chunks of the text.            

• For code completion, they create summaries of the code, including function or class details.            

If one worker can’t fully answer a question based on its chunk, the next worker builds on their findings. Workers only pass useful information forward, avoiding irrelevant details.            

![](https://media.licdn.com/dms/image/v2/D4D12AQFyqyfvQm-rjQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1737895494667?e=2147483647&v=beta&t=_rrpnCccQ_FovvEQrRWK4SKKT-X0ZOrGI4mLNgWRM0A)

Image credit: The original paper            

2\. Manager agent:            

Once all worker agents have processed their chunks and passed on their findings, the manager agent steps in. Its job is focused on synthesizing and presenting the final result, allowing worker agents to focus only on their chunks.            

---

Advantages of CoA:                                                                                        

\- No training needed: It works with existing models without requiring additional fine-tuning.          

\- Task flexibility: It can handle many types of tasks, like summarization, answering complex questions, and code completion.          

## 领英推荐

\- Cost efficiency: CoA processes text faster by focusing on smaller chunks, reducing computational complexity.          

---

Results of CoA:          

• It outperformed RAG and other models in question answering, summarization, code completion, and long context tasks, even with a smaller window.          

• CoA’s performance improved as input length increased.          

• 57% faster runtime on average due to parallel processing.          

• Minimal information loss (1-4%) during communication between agents.          

Image credit: The original paper          

---

Why CoA is better than other methods?                                                                                

\- Unlike input reduction, CoA doesn’t skip important details because it processes everything step by step.        

\- Unlike window extension, CoA doesn’t overwhelm the model with too much information at once.        

Thanks to collaboration and communication between agents it handles long texts more naturally.        

Image credit: The original paper                                                                                                                                                                                                                                                                                                        

---