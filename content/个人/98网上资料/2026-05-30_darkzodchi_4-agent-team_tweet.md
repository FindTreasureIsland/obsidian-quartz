---
title: "How to build a 4-agent team, that ships a feature while you sleep (Exact Setup Inside)"
author: darkzodchi
source: https://x.com/zodchiii/status/2060674246880149900
created: 2026-05-30
tags: [X, twitter, AI, agents, Claude, workflow]
description: Four AI agents (Planner → Coder → Tester → Reviewer) chained with handoff files can ship a complete feature overnight. Here's the exact setup.
stats:
  likes: 657
  retweets: 74
  views: 946902
---

Four AI agents can ship a feature while you sleep. Most people never wire them up.

They fire a reviewer here, a test generator there, by hand, one at a time, each forgetting what the last one did. You're still the bottleneck.

The fix: Planner → Coder → Tester → Reviewer, chained to hand off automatically. One trigger, four stages, a finished feature by morning.

Here's the full pipeline, with copy-paste code 👇

Before we dive in, I share daily notes on AI & vibe coding in my Telegram channel: https://t.me/zodchixquant 🧠

---

## Why a pipeline beats a pile of agents

One agent doing everything fills its context window with planning, code, tests, and review notes until quality drops.

Four specialists each stay in a clean, narrow context.

The trick is the handoff file. Each agent writes its output where the next one can read it: Planner drops a spec at .pipeline/spec.md, Coder reads it and writes .pipeline/changes.md, and so on.

The orchestrator running them in order is a single slash command. That's the whole thing: four subagents, one command, a shared folder for handoffs.

## Agent 1: The Planner (subagent, opus)

The Planner never writes code. It turns a vague feature request into a concrete spec the Coder can follow without guessing.

Create .claude/agents/planner.md:

Planning runs on opus because this stage sets the quality ceiling for everything after it. A vague spec produces vague code no matter how good the Coder is.

## Agent 2: The Coder (subagent, sonnet)

The Coder reads the spec and writes the implementation. It doesn't plan and it doesn't review its own work, it just builds what the spec says.

Create .claude/agents/coder.md:

Sonnet is the right call here: implementation against a clear spec is exactly the balanced cost-quality work Sonnet handles best.

The handoff note at .pipeline/changes.md is what lets the Tester target the right surface instead of testing blind.

## Agent 3: The Tester (subagent, sonnet)

The Tester reads what changed and writes tests that prove the feature works, then runs them.

Create .claude/agents/tester.md:

## Agent 4: The Reviewer (subagent, opus)

The last gate. The Reviewer reads everything the pipeline produced and gives a verdict before any of it reaches your main branch.

Create .claude/agents/reviewer.md:

Read-only tools mean the Reviewer can't paper over problems by editing, it can only judge.

## The orchestrator: one command to run all four

Now the piece that turns four separate agents into a pipeline. A slash command that invokes them in order, each one picking up the handoff file the last one wrote.

Create .claude/commands/ship.md:

Then a single line kicks off the whole chain: /ship add rate limiting to the login endpoint.

## Where I run the overnight version

That's what I use Teamly for: managed cloud hosting built specifically for AI agents.

You hire a team, it runs 24/7 on dedicated infrastructure, and you never touch a server.

The reason @Teamly fits this article specifically: the handoff problem is already solved for you.

Everything we built by hand above (the spec file, the changes file, the orchestrator chaining one agent to the next) Teamly does with a Coordinator.

It routes work between agents, passes context from one to the next, and keeps a shared brief they all read from.

The same Planner-to-Coder-to-Tester flow, except you don't wire the handoffs yourself.

The difference is that @Teamly isn't code-only. The exact same orchestration runs a marketing team, a research team, or a support team.

Your Claude Code pipeline ships features overnight; a Teamly marketing team ships content the same way, with the same hand-off logic underneath.

## Build the exact team you need

New feature, that team just rolled out: My Team

Now you can build your team with just 3 questions.

You also can control: voice rules, forbidden phrases, integrations, team style (Strict / Casual / Creative), and team size (2-4 agents).

@Teamly returns a team with a real rationale for why each specialist is there, not boilerplate. Swap any agent with one click. Edit the brief if it's off.

The point is a structured brief that forces clarity, then composes a team you can audit before hiring.

Same handoff architecture as the pre-built teams, fitted to your specific problem.

## Try it free first

You can test the whole thing free for 3 days on Teamly 5, no charge until day 4.

If you stay, pricing is $29/mo for 5 agents.

Cheap enough that one shipped feature pays for the month.

## The bottom line

The difference between a pile of agents and a pipeline is the handoff.

Four specialists writing to shared files, one orchestrator running them in order, each stage building on the last instead of starting from scratch.

Build the Planner and Coder first and run them as a two-stage chain. Once that flow feels solid, add the Tester and Reviewer.

By the time all four are wired up, you'll kick off a feature before bed and read a verdict with your coffee.

For daily notes on AI agents, vibe coding and Claude Code setups: https://t.me/zodchixquant 🧠