---
title: Claude Subagents vs. Agent Teams, explained
author: "Akshay 🚀 (@)"
date: 2026-03-15 13:04
source: "https://x.com/akshay_pachaar/status/2033167408463069526"
tags:
  - twitter
  - article
---

# Claude Subagents vs. Agent Teams, explained

**作者**: Akshay 🚀 (@)
**时间**: 2026-03-15 13:04
**来源**: [原始链接](https://x.com/akshay_pachaar/status/2033167408463069526)

---

Most people reach for multi-agent systems the moment a task feels complex.

That's almost always the wrong instinct.

The right question isn't "should I use multiple agents?" It's "what kind of coordination does this task actually need?"

The answer to that determines everything about your architecture.

Claude gives you two distinct multi-agent paradigms: sub-agents and agent teams. They look similar on the surface. Architecturally, they solve completely different problems.

## Sub-Agents: Parallelism Through Isolation

A sub-agent is a specialized Claude instance that runs in its own isolated context window.

Here's the mental model: imagine you're a research lead. You don't read every primary source yourself. You delegate focused questions to researchers, they come back with distilled findings, and you synthesize everything into a coherent output.

That's exactly what sub-agents do.

Each sub-agent gets:
- Its own system prompt defining its specialty
- A specific set of tools it can access
- A clean, isolated context window
- One job to do

When it finishes, only the final result returns to the parent. Not the full reasoning chain. Not the intermediate steps. Just the compressed output.

The point of sub-agents isn't just parallelism, it's compression. You're distilling a vast amount of exploration into a clean signal, without polluting your parent agent's context with noise.

One hard constraint: sub-agents can't spawn other sub-agents, and they can't talk to each other. Every result flows back to the parent. The parent is the sole coordinator.

This constraint is a feature, not a limitation. It keeps the system predictable. You always know where information flows and where decisions get made.

## Agent Teams: Coordination Through Communication

Agent teams are a fundamentally different model.

Where sub-agents are short-lived workers that complete a task and disappear, agent teams are long-running instances that persist, communicate directly with each other, and coordinate through shared state.

Think of it like the difference between hiring contractors for isolated tasks vs. assembling a team that works together in the same room.

An agent team has three moving parts:
1. A team lead that coordinates work, assigns tasks, and synthesizes results
2. Teammates that are independent agent instances, each with their own context window, working in parallel
3. A shared task list that tracks what's pending, in progress, and done, along with dependencies between tasks

## The Core Distinction: Fire-and-Forget vs. Ongoing Coordination

**Sub-agents are fire-and-forget:**
- You give them a task, they complete it, they report back
- No conversation between agents
- No shared memory, no ongoing state
- Each sub-agent lives and dies within a single session

**Agent teams are collaborative:**
- Agents persist and accumulate context over time
- Mid-task discoveries surface to teammates immediately
- A frontend agent can tell a backend agent "the API response structure needs to change" and the backend agent adjusts without waiting for the lead to mediate

## The clearest way to choose between them:

- Use sub-agents when your work is embarrassingly parallel: independent research streams, codebase exploration, or lookups where the parent only needs the summary
- Use agent teams when your work requires ongoing negotiation: agents that need to reconcile their outputs before proceeding, or where a discovery in one thread changes what another thread should do

## How to Design Agent Systems From First Principles

Most multi-agent designs fail because people split work by role instead of by context.

The intuitive instinct is to split by role: planner, implementer, tester. It feels organized. But it creates a telephone game where information degrades at every handoff.

The right mental model is context-centric decomposition.

Ask: what context does this subtask actually need? If two subtasks need deeply overlapping information, they probably belong to the same agent. If they can operate with truly isolated information and clean interfaces between them, that's where you split.

A practical example: an agent implementing a feature should also write the tests for that feature. It already has the context. Splitting those two into separate agents creates a handoff problem that costs more than the parallelism saves. Only separate when context can be genuinely isolated.

## The Five Orchestration Patterns Worth Knowing

Regardless of which paradigm you use, these five patterns cover most real-world needs:

1. **Prompt chaining:** Sequential steps where each call processes the previous output. Use when order matters and steps are dependent.

2. **Routing:** A classifier decides which specialized handler gets the task. Easy questions go to cheaper, faster models. Hard questions go to more capable ones. This is how you keep costs from exploding.

3. **Parallelization:** Independent subtasks run simultaneously. Either the same task runs multiple times for diverse outputs (voting), or different subtasks run at the same time (sectioning).

4. **Orchestrator-worker:** A central agent breaks down the task, delegates to workers, and synthesizes results. This is the dominant architecture for both sub-agents and agent teams, and what most production systems actually use.

5. **Evaluator-optimizer:** One agent generates, another evaluates and provides feedback in a loop. Useful when quality matters more than speed and a single pass isn't reliable enough.

## When Not to Use Multi-Agent Systems at All

This is the part most articles skip.

Teams have spent months building elaborate multi-agent pipelines only to discover that better prompting on a single agent achieved equivalent results.

Start simple. Add complexity only when you can clearly measure that it's needed.

**Multi-agent systems earn their cost in three situations:**
- Context protection: A subtask generates information irrelevant to the main task. Keeping it in a sub-agent prevents context bloat.
- True parallelization: Independent research or search tasks that benefit from simultaneous coverage.
- Specialization: The task requires conflicting system prompts, or one agent is juggling so many tools that its performance degrades.

**They're the wrong call when:**
- Agents constantly need to share context with each other
- Inter-agent dependencies create more overhead than execution value
- The task is simple enough that one well-prompted agent handles it

One specific warning for coding: parallel agents writing code make incompatible assumptions. When you merge their work, those implicit decisions conflict in ways that are hard to debug. Sub-agents for coding should answer questions and explore, not write code simultaneously with the main agent.

## What Makes Multi-Agent Systems Actually Fail

Three failure modes show up constantly:

1. **Vague task descriptions cause agents to duplicate each other's work.**
Every agent needs a clear objective, an expected output format, guidance on what tools or sources to use, and explicit boundaries on what it should not cover. Without this, two agents will research the same thing and neither will notice.

2. **Verification agents declare victory without verifying.**
Explicit, concrete instructions are non-negotiable: run the full test suite, cover these specific cases, do not mark as complete until each one passes. Vague approval criteria produce false positives.

3. **Token costs compound faster than you expect.**
The solution is to tier your models intelligently: use your most capable model where it genuinely matters, route routine work to faster, cheaper models, and build in budget controls so costs can't run away unchecked.

## The One Design Principle That Actually Matters

Design around context boundaries, not around roles or org charts.

Start with a single agent. Push it until you find where it breaks. That failure point tells you exactly what to add next.

Add complexity only where it solves a real, measured problem.

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDcyYhSbwAELkEh?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HDclWiXaUAAtHmx?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HDclgDXbcAAAkIH?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HDcolYDbQAAthSB?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HDcscLeawAAmtxF?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HDcupB4bUAAQ7XB?format=jpg&name=medium)

