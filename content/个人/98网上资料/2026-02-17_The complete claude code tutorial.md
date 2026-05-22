---
title: The complete claude code tutorial
author: "Eyad (@eyad_khrais)"
date: 2026-01-10 19:51
source: "https://x.com/eyad_khrais/status/2010076957938188661"
tags:
  - twitter
  - article
---

# The complete claude code tutorial

**作者**: Eyad (@eyad_khrais)
**时间**: 2026-01-10 19:51
**来源**: [原始链接](https://x.com/eyad_khrais/status/2010076957938188661)

---

I've been a SWE for 7 years, between Amazon, Disney, and Capital One. The code I've shipped touches millions of users, and I built systems that couldn't afford to break. Now I'm the CTO of a startup that builds agents for enterprise, and Claude Code is my daily driver.

Here's a beginners playbook you might find useful, containing everything I've learned about Claude after using it to build robust systems that handle complex workloads from large companies. Let me know if it helps below.

## Think First

Most people assume that with Claude Code and other AI tools, the first thing you need to do is type (or start talking). But that's probably one of the biggest mistakes that you can make straight off the bat. The first thing that you actually need to do is think.

10 out of 10 times, the output I've gotten with plan mode did significantly better than when I just started talking and spewing everything into Claude Code. It's not even close.

Now for some of you, this is easier said than done. You might not have years of software engineering experience that would allow you to think about this on your own. To this extent I have two pieces of advice: 1. Start learning. You are handicapping yourself if you never pick up on this, even if just a little bit at a time. 2. Have a deep back and forth with ChatGPT/Gemini/Claude, where you describe exactly what you want to build, you ask the LLM for the various options you can take in terms of system design, and ultimately the two of you settle on a solution. You and the LLM should be asking each other questions, not just a one way street.

This applies to everything. This also includes very small tasks like summarizing emails. Before you ask Claude to build a feature, think about the architecture. Before you ask it to refactor something, think about what the end state should look like. Before you ask it to debug, think about what you actually know about the problem. The more information that you have in plan mode, the better your output is actually going to be because the better the input is going to be.

The pattern is consistent: thinking first, then typing, produces dramatically better results than typing first and hoping Claude figures it out.

This brings me onto my next point of architecture. Architecture, especially in software engineering, is a little bit like giving a person the output and nothing more. This leaves for A LOT of wiggle room in how to get to the output, which is essentially what the problem with AI generated code is. If you say something super broad like "build me an auth system" as opposed to "Build email/password authentication using the existing User model, store sessions in Redis with 24-hour expiry, and add middleware that protects all routes under /api/protected.", you can see the difference.

You click shift + tab twice, and you're in plan mode. Trust me when I say this, this is going to take 5 minutes of your time, but will save you hours upon hours of debugging later on.

## CLAUDE.md

CLAUDE.md is a markdown file. Markdown is a text format that AI models process extremely well, and Claude in particular handles it better than most other models I've tested.

When you start a Claude Code session, the first thing Claude does is read your CLAUDE.md file. Every instruction in that file shapes how Claude approaches your project. It's essentially onboarding material that Claude reads before every single conversation.

Most people either ignore it completely or stuff it with garbage that makes Claude worse instead of better. There is a threshold where too much or too little information means worse model output.

Here's what actually matters:

- Keep it short. Claude can only reliably follow around 150 to 200 instructions at a time, and Claude Code's system prompt already uses about 50 of those. Every instruction you add competes for attention. If your CLAUDE.md is a novel, Claude will start ignoring things randomly and you won't know which things.
- Make it specific to your project. Don't explain what a components folder is. Claude knows what components are. Tell it the weird stuff, like the bash commands that actually matter. Everything that is part of your flow should go into it.
- Tell it why, not just what. Claude is a little bit like a human in this way. When you give it the reason behind an instruction, Claude implements it better than if you just tell it what to do. "Use TypeScript strict mode" is okay. "Use TypeScript strict mode because we've had production bugs from implicit any types" is better. The why gives Claude context for making judgment calls you didn't anticipate. You'll be surprised how effective this actually is.
- Update it constantly. Press the # key while you're working and Claude will add instructions to your CLAUDE.md automatically. Every time you find yourself correcting Claude on the same thing twice, that's a signal it should be in the file. Over time your CLAUDE.md becomes a living document of how your codebase actually works.

Bad CLAUDE.md looks like documentation written for a new hire. Good CLAUDE.md looks like notes you'd leave yourself if you knew you'd have amnesia tomorrow.

---

## 图片

![Image 1](https://pbs.twimg.com/media/G-U5_YwWMAA7Ulv?format=jpg&name=medium)

