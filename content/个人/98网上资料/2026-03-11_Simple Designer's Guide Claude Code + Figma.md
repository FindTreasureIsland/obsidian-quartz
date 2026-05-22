---
title: "Simple Designer's Guide: Claude Code + Figma"
author: "rico (@_heyrico)"
date: 2026-03-09 08:20
source: "https://x.com/_heyrico/status/2030921707251486822"
tags:
  - twitter
  - article
---

# Simple Designer's Guide: Claude Code + Figma

**作者**: rico (@_heyrico)
**时间**: 2026-03-09 08:20
**来源**: [原始链接](https://x.com/_heyrico/status/2030921707251486822)

---

For a long time, the design-to-code handoff only moved in one direction.

You designed in Figma. A developer built it in code. You reviewed it, marked up changes, and repeated. The canvas and the codebase were two separate worlds. Getting ideas from one to the other took time, and something always got lost.

In February 2026, Anthropic and Figma changed that direction. The integration is called Code to Canvas. It lets you build a UI in Claude Code and send it directly into Figma as editable layers. Code becomes canvas. The workflow now runs both ways.

This is not a small update. It changes how you can work, if you know how to use it.

## What Code to Canvas Actually Does

The basic idea is straightforward.

You write a prompt in Claude Code. Claude generates working HTML and CSS. A rendered version of that UI appears in your browser. Then, with the Figma MCP installed, you type a single instruction: send this to Figma. Claude translates the rendered browser state into a fully editable Figma frame.

What arrives in Figma is not a screenshot. It is a real frame with layers. You can select elements, change colors, adjust spacing, update typography. It behaves like something you built in Figma from scratch.

From there, you can also go back. Share the updated Figma design with Claude Code via MCP, then prompt it to rewrite the code to match what you changed. It is not a single button. It is a prompt. But the round-trip works, and that is what matters.

## How to Set It Up

You need two things: Claude Code and the Figma MCP.

If you are new to Claude Code, start with the Claude desktop app. You get the same workflow without touching the terminal. Connect a project folder and you are ready.

Remote MCP server:
This works whether you use Figma in the browser or the desktop app. Open your terminal and run:

claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp

Restart Claude Code. Then type /mcp inside Claude to see your connected servers. If Figma shows as disconnected, hit Enter to log in and click Allow access. Type /mcp again to confirm it shows as connected.

## Where It Breaks Down

It is worth being honest about this.

The output quality depends heavily on the prompt. Vague prompts produce vague results.

Instead of writing: "Build a dashboard."

Write something like: "Build a SaaS analytics dashboard. Show a sidebar on the left with navigation, a top bar with a user avatar, and a main area with 3 metric cards at the top and a line chart below. Use a white background with neutral gray text. Keep it minimal."

The more context you give, the less Claude has to guess. If you leave things vague, Claude fills the gaps. Those gaps are usually what you spend time fixing in Figma.

The same rule applies to components. Instead of: "Build a pricing card."

Try: "Build a pricing card with a plan name, monthly price, a list of 4 features, and a CTA button at the bottom. Rounded corners, white background, subtle border."

Specificity is the difference between a result you can use and a result you have to redo.

The integration also works best on isolated screens or components. Complex multi-screen flows with transitions and states are harder to hand off this way. You will get a static frame, not a prototype.

And if your Figma design system uses custom components with specific tokens and variants, Claude will not always match them perfectly on the first pass. It reads what is there, but it does not know your conventions unless you explain them. A quick note in your prompt like "use 8px border radius and neutral gray 100 for card backgrounds" gets you much closer on the first try.

## When To Use It

Code to Canvas is most useful in three situations.

The first is early exploration.
You have an idea but no clear visual direction. Instead of starting from a blank Figma frame, you describe the interface in plain language and get something to react to. It is faster than starting from scratch and more concrete than a sketch.

The second is quick iteration.
You have a design and want to test a different layout or interaction pattern quickly. Build a variation in Claude Code, send it to Figma, compare the two side by side.

The third is communication.
Sometimes it is easier to show a working UI than to describe it. Generate something in Claude Code, bring it into Figma, and share it as a reference point for your team.

It is not a replacement for a proper design process. It is a shortcut for specific moments in that process.

## The Takeaway

The handoff used to mean: design it, then build it.

Code to Canvas means that is no longer the only path. You can build it first, then bring it into your design tool and shape it from there. The direction you move depends on what the moment calls for.

That flexibility is the point. Designers who understand both ends of this workflow will move faster and work with more confidence than those who stay on one side.

The tool is available now. The only thing left is learning how to use it well.

The goal is not to just become a designer

The goal is to become someone who thinks in design, builds with AI, and ships products that feel right.

That is what I write about. Design and AI. Not as separate topics. As one discipline that helps you build better things, faster, and beautifully.

Follow if that is what you are building toward.

---

## 图片

![Image 1](https://pbs.twimg.com/media/HC8SNvXbQAEpZXH?format=jpg&name=medium)

