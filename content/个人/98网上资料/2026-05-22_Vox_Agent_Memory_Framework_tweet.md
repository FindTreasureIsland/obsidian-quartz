---
title: "A Framework for Agent Memory: Remember, Cite, Forget"
author: Vox
source: https://x.com/Voxyz_ai/status/2057862044783628508
created: 2026-05-22
tags: [X, twitter, agent, memory, AI, framework]
stats:
  likes: 108
  retweets: 9
  views: 31955
---

When people add memory to an agent, the first instinct is usually "what else can I store in there?" But more storage doesn't mean the agent will actually use it.

For example: I run X Manager, the kind of agent that fires lots of cron jobs throughout the day. After running it for a while, I'm convinced of one thing. Agent memory has to do three jobs at once to be reliable. Remember what should be remembered. Cite what should be trusted. Forget what should expire. Break these three apart and you have a framework you can apply to any agent.

## Remember: agent memory comes in layers

In practice, the memory an agent uses comes in roughly 6 layers. Each one has a different lifespan, a different scope of authority, and a different way of failing.

**Hot session (working memory for the current task)**

Holds the in-progress context: what the user just said, the last tool output, intermediate conclusions from this round. Should be cleared at task end. Common failure: the user said "no emoji today" two turns ago, the agent compressed the context on turn three, dropped that line, and added emoji again.

To soften this kind of loss, look at how lossless-claw handles it: raw messages land in SQLite, summaries only do compression, and the agent can grep the originals when needed.

**Day-state (today's operating whiteboard)**

What the agent has done today, where it is in its sequence, what's next. A whiteboard is meant to be overwritten. One direct instruction with a newer timestamp should retire the previous state. Common failure: you said in the morning "work on article A first," then switched to B in the afternoon, but the cron agent is still pulling research for A.

**Project memory (long-running lessons)**

What this project has tripped over before, which patterns worked, which decisions have been settled. Longer-lived than the whiteboard, but still gets overwritten by newer lessons. Common failure: a three-month-old note that says "user prefers markdown" still shapes today's formatting choice, even though the user switched preferences last month.

To do this layer well, write lessons into a cross-session structured knowledge base like GBrain, or your own notes / wiki system.

**Retrieval / Index (surfaces candidates, doesn't decide)**

Vector stores, RAG, GBrain search, graph search all live here. Their job is to surface material that might be relevant. The index gives you candidates. The final call still depends on source, time, authority, and freshness. Common failure: a vector search pulls up an old plan from six months ago, and it gets treated as the current best answer.

**Canonical policy (the long-term rule layer)**

Project rule files (things like AGENTS.md, SOUL.md), team policy, product boundaries. These are more like the agent's "constitution": long-lived, stable, and you only change them by editing the file by hand.

**Direct instruction (the immediate task command)**

What the user just said. High priority for the current task, but not necessarily durable. It has to keep its original source attached. A summary paraphrase doesn't carry the same weight. Common failure: AGENTS.md says "public actions require manual confirmation," the hot-session summary says "user has authorized batch sending," and the agent quietly follows the summary. The only thing that can override canonical is a traceable original confirmation. "The user seemed to authorize this" from a summary doesn't count.

These 6 layers weren't invented in a vacuum. Mainstream frameworks like LangGraph and Mem0 also split memory into layers. Different names, same principle. This version is a builder's-eye take on the same idea.

Layering alone isn't enough. Every layer has to answer one question: what gives this memory the right to influence the decision? That's where the second job comes in.

## Cite: don't make the agent guess who's authoritative

In practice, memory work takes at least two steps.

**Step 1: Figure out which source the current query should hit.** GBrain's source resolver is a good reference: it uses a CLI flag, an env variable, a dotfile, longest-prefix path match, a default config, and a fallback to decide the current source. What this step prevents: querying the wrong source.

**Step 2: When the lookup turns up conflicting facts, an authority order decides who wins.** The application defines this part for itself. Here's an order you can copy:

1. Original direct instruction
2. Canonical policy
3. Most recent project decision
4. Long-term memory with source attribution
5. Retrieval summary
6. Compressed summary

Higher levels overrule lower ones.

What does this look like without that machinery in production? The 2024 Air Canada chatbot case is the classic source-authority example. The bot told a customer he could apply for a retroactive bereavement-fare refund, but the official policy page said the opposite. The tribunal ordered Air Canada to pay C$650.88 in fare difference plus interest. The judge's words: "It makes no difference whether the information comes from a static page or a chatbot."

What this case shows: once AI speaks for the company, it can't disagree with the canonical policy page. Users shouldn't have to guess which one is more accurate. The company has to define the authority chain itself.

Citations themselves go stale. Before the 2026 Scottish election, Demos tested AI tools on 75 election questions and found misinformation in 34% of the answers. ChatGPT's citations were "at least a year out of date" 44% of the time. For agents, judging a source means asking whether the link is still current.

Even the most authoritative fact has to step aside when it goes stale. On to the third job.

## Forget: expiring old memories is reliability engineering

The most underrated agent memory capability is letting old memories expire. Most teams treat forget as a GDPR compliance task, but for agents this is a reliability problem: a memory that's gone stale still looks usable, even though the agent doesn't know it's already quietly wrong. That's more dangerous than "no memory at all."

This risk has already shown up in real content systems. In 2026, the UK's Department for Business and Trade described a GOV.UK example: the main page was up to date, but the GenAI bot, on narrower queries, was pulling answers from an unmaintained old GOV.UK page. The DBT audit found 150 pages on the first pass that all met three criteria at once: not updated in 5 years, fewer than 11 visits in 5 years, and no owner.

The old information hasn't gone anywhere. It's just unread. Once the agent pulls it back, it sounds as confident as today's answer.

Three implementation routes are out there. They can coexist.

**Hard expiry.** valid_from / valid_until columns. When a new fact arrives, the old fact gets an expiry timestamp written to it. The old record is retained but flagged as no longer usable. Example: GBrain typed facts / trajectory. Use for policy, pricing, regulations.

**Bitemporal.** Four timestamps created_at / valid_at / invalid_at / expired_at distinguish "when it was true in reality" from "when the system learned it was no longer valid." Example: Zep. Use for facts that change over time.

**Soft decay.** Retrieval ranking demotes long-unused memories, down to a 0.3× floor. The docs say "Nothing gets deleted or hidden." It's a search-time recency rerank. Example: Mem0. Use for preferences, habits, background knowledge.

When you design agent memory, define the expiry mechanism alongside the storage mechanism.

## 3 questions to ask before any memory enters the decision loop

Now translate the three jobs into a quick audit. Before any memory enters the decision loop, ask:

1. **What level of decision can this affect?** Hint only? Citable evidence? Or can it make the final call?
2. **Where did it come from?** Which canonical file, which day's notes, which message? Or is it just a derivative of another memory?
3. **Is it still valid?** What kind of new information would make this memory step aside?

An example. The agent is about to reply to an email and pulls a three-month-old preference from project memory: the user once said "don't use markdown for replies, plain text is fine."

- Decision level: hint only, can't override an explicit instruction from today.
- Source: must be able to point to which message and who said it.
- Still valid: three months untouched, so confirm with the user once before using.

If all three questions are answerable, the memory can enter the decision path. If not, it can only stay as background context. Don't let a memory with no source, no validity window, and no authority boundary make calls for the agent.

## A pocket card you can save

Remember by layer. Cite by source. Forget by expiry. Stick this somewhere visible. Run through it before adding any new memory to your agent.

- **Hot session.** Carries the current task. Steps aside when the task ends.
- **Day-state.** Coordinates today. Steps aside when a newer direct decision arrives.
- **Project memory.** Long-running lessons. Steps aside when the lesson gets overwritten.
- **Retrieval / Index.** Surfaces candidates, doesn't decide. Steps aside when the source updates, the index rebuilds, or a candidate fact expires.
- **Canonical policy.** Long-term rules and boundaries. Steps aside when a new policy version is manually committed.
- **Direct instruction.** Immediate call for the current task. Steps aside when the task ends, or a new instruction arrives.

Drop it into your agent project's AGENTS.md or README, and run through it before any memory change review.

Designing agent memory is the same shape as company governance. Remember through layering. Cite through provenance. Forget through expiry. Bundle these three into one trust contract you write into the agent, and its calls start being reliable.

The point where an agent actually becomes trustworthy is when all three are working at once.

*Everything I'm writing as I build: voxyz.ai/insights.*

## Tools you can try

**GBrain:** cross-session structured knowledge base, bitemporal facts, 6-tier source resolver. github.com/garrytan/gbrain

**lossless-claw:** lossless session recording (OpenClaw plugin). github.com/Martian-Engineering/lossless-claw

**LangGraph:** short-term + long-term layers (semantic / episodic / procedural). docs.langchain.com/oss/python/concepts/memory

**Mem0:** conversation / session / user / org layers + soft decay. docs.mem0.ai

**Zep:** bitemporal facts (four timestamps). help.getzep.com/facts
