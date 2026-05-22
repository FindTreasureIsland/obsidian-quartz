---
title: "Agentic Engineering Patterns - Simon Willison"
author: "Simon Willison"
date: 2026-02-23 17:43
source: "https://simonwillison.net/guides/agentic-engineering-patterns/"
tags:
  - agentic-engineering
  - coding-agents
  - simon-willison
---

# Agentic Engineering Patterns

**作者**: Simon Willison
**时间**: 2026-02-23 17:43
**来源**: [原始链接](https://simonwillison.net/guides/agentic-engineering-patterns/)

---

## 引言：关于 Agentic Engineering Patterns

23rd February 2026

I've started a new project to collect and document **Agentic Engineering Patterns**—coding practices and patterns to help get the best results out of this new era of coding agent development we find ourselves entering.

I'm using **Agentic Engineering** to refer to building software using coding agents—tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and *execute* code—allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor.

I think of **vibe coding** using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code.

Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise.

---

## 第一章：Writing code is cheap now

The biggest challenge in adopting agentic engineering practices is getting comfortable with the consequences of the fact that *writing code is cheap now*.

Code has always been expensive. Producing a few hundred lines of clean, tested code takes most software developers a full day or more. Many of our engineering habits, at both the macro and micro level, are built around this core constraint.

At the macro level we spend a great deal of time designing, estimating and planning out projects, to ensure that our expensive coding time is spent as efficiently as possible. Product feature ideas are evaluated in terms of how much value they can provide *in exchange for that time* - a feature needs to earn its development costs many times over to be worthwhile!

At the micro level we make hundreds of decisions a day predicated on available time and anticipated tradeoffs. Should I refactor that function to be slightly more elegant if it adds an extra hour of coding time? How about writing documentation? Is it worth adding a test for this edge case? Can I justify building a debug interface for this?

Coding agents dramatically drop the cost of typing code into the computer, which disrupts *so many* of our existing personal and organizational intuitions about which trade-offs make sense.

The ability to run parallel agents makes this even harder to evaluate, since one human engineer can now be implementing, refactoring, testing and documenting code in multiple places at the same time.

### Good code still has a cost

Delivering new code has dropped in price to almost free... but delivering *good* code remains significantly more expensive than that.

Here's what I mean by "good code":

- The code works. It does what it's meant to do, without bugs.
- We *know the code works*. We've taken steps to confirm to ourselves and to others that the code is fit for purpose.
- It solves the right problem.
- It handles error cases gracefully and predictably: it doesn't just consider the happy path. Errors should provide enough information to help future maintainers understand what went wrong.
- It's simple and minimal - it does only what's needed, in a way that both humans and machines can understand now and maintain in the future.
- It's protected by tests. The tests show that it works now and act as a regression suite to avoid it quietly breaking in the future.
- It's documented at an appropriate level, and that documentation reflects the current state of the system - if the code changes an existing behavior the existing documentation needs to be updated to match.
- The design affords future changes. It's important to maintain YAGNI - code with added complexity to anticipate future changes that may never come is often bad code - but it's also important not to write code that makes future changes much harder than they should be.
- All of the other relevant "ilities" - accessibility, testability, reliability, security, maintainability, observability, scalability, usability - the non-functional quality measures that are appropriate for the particular class of software being developed.

Coding agent tools can help with most of this, but there is still a substantial burden on the developer driving those tools to ensure that the produced code is good code for the subset of good that's needed for the current project.

### We need to build new habits

The challenge is to develop new personal and organizational habits that respond to the affordances and opportunities of agentic engineering.

These best practices are still being figured out across our industry. I'm still figuring them out myself.

For now I think the best we can do is to second guess ourselves: any time our instinct says "don't build that, it's not worth the time" fire off a prompt anyway, in an asynchronous agent session where the worst that can happen is you check ten minutes later and find that it wasn't worth the tokens.

---

## 第二章：Red/green TDD

"**Use red/green TDD**" is a pleasingly succinct way to get better results out of a coding agent.

TDD stands for Test Driven Development. It's a programming style where you ensure every piece of code you write is accompanied by automated tests that demonstrate the code works.

The most disciplined form of TDD is test-first development. You write the automated tests first, confirm that they fail, then iterate on the implementation until the tests pass.

This turns out to be a *fantastic* fit for coding agents. A significant risk with coding agents is that they might write code that doesn't work, or build code that is unnecessary and never gets used, or both.

Test-first development helps protect against both of these common mistakes, and also ensures a robust automated test suite that protects against future regressions. As projects grow the chance that a new change might break an existing feature grows with them. A comprehensive test suite is by far the most effective way to keep those features working.

It's important to confirm that the tests fail before implementing the code to make them pass. If you skip that step you risk building a test that passes already, hence failing to exercise and confirm your new implementation.

That's what "red/green" means: the red phase watches the tests fail, then the green phase confirms that they now pass.

Every good model understands "red/green TDD" as a shorthand for the much longer "use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass".

Example prompt:

> Build a Python function to extract headers from a markdown string. Use red/green TDD.

---

## 目录

1. **Principles**
   - Writing code is cheap now
   - Hoard things you know how to do
2. **Testing and QA**
   - Red/green TDD
   - First run the tests
3. **Understanding code**
   - Interactive explanations
   - Linear walkthroughs
4. **Appendix**
   - Prompts I use

---

*更多章节陆续更新中...*
