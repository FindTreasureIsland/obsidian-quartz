# Hyperagents: A New Way to Auto-Research

> 来源：Twitter @neural_avb (AVB)
> 原文链接：https://x.com/neural_avb/status/2037526862964969583
> 发布日期：2026-03-27
> 统计数据：❤️ 172 | 🔁 17 | 👀 3.8万

---

## 文章正文

"Hyperagents" is a new framework for building self-improving AI systems. Paper by Meta AI & a bunch of top universities. This is like Dr. Karpathy's auto-research, but with recursive tree exploration wrapped in a Darwin-Godel Machine.

The idea is to move away from systems that have a fixed, human-engineered way of learning and instead create agents that can redesign their own improvement mechanisms.

---

## What are Hyperagents?

A "hyperagent" is a fancy term for a self-referential agent that integrates both the task agent and the meta agent into a single editable program.

Because the meta agent is itself part of the editable code, the system can perform "metacognitive self-modification" — the agent doesn't just look for better ways to solve a task. It looks for better ways to look for better ways.

The authors propose **DGM-H (Darwin Gödel Machine - Hyperagents)**, an extension of the original Darwin Gödel Machine (DGM).

---

## What is Darwin Gödel Machine?

The Darwin Gödel Machine (DGM) is an AI framework for creating self-improving AI systems that "evolve" their own code over time. Its name is derived from: Darwinian evolution plus Gödelian self-reference.

**The Darwinian aspect** refers to the system's use of open-ended exploration and population-based evolution. Traditionally works in 3 stages:

1. **Generation**: The system starts with an initial agent and generates multiple variants (children) of that agent by modifying its code.
2. **Selection**: These variants are then empirically evaluated on a task.
3. **Archive of Stepping Stones**: Successful versions are saved in an archive. These serve as "stepping stones" - parent agents that the system can later select to generate even better descendants.

The "Gödel" self-reference part refers to the system being self-referential. The agent that solves the task (the task agent) is the exact same code that is responsible for generating its own improvements (the meta agent). I.e., it updates its own source code.

---

## The Role of the Human

Based on the paper, the human's role transitions into these four key areas:

1. **Defining the "What," Not the "How"**: Humans are responsible for defining the benchmarks and evaluation criteria. The agent is given a goal (e.g., "grade this math problem correctly"), but it is left to autonomously discover the "how".

2. **Safety**: Humans oversee that the agent operates within a sandboxed environment with strict resource limits (timeouts, internet restrictions) to prevent unintended side effects from autonomous code modification.

3. **Datasets**: Humans input whatever data and eval criteria that the agent uses.

---

## The Algorithm

**1. The Hyperagent Structure**

At the core of the algorithm is the Hyperagent (H) which is defined as a unified, editable program consisting of two functional components: The Task Agent and the Meta Agent.

- **Task Agent** is the code responsible for solving the target domain task (e.g., writing a robotic reward function or solving a math problem).
- **Meta Agent** is responsible for generating improvements. It can edit the source code of both the task agent and itself.

**2. The Loop**

The algorithm maintains an archive of "stepping stones" At={a_0,a_1,…,a_t} where each a_i is a scored hyperagent.

The core optimization loop follows these steps:

1. **Parent Selection**: A parent hyperagent is sampled from the archive based on its performance and its "fertility" (how many successful children it has already produced).

2. **Metacognitive Self-Modification**: The selected parent uses its internal Meta Agent to generate a child variant. Because the Meta Agent is part of the editable codebase, the child may have a different strategy for self-improvement than its parent.

3. **Evaluation**: The child is tested on the target task. Its performance score is also recorded.

4. **Archive Update**: This new child agent is added to the archive A.

**3. Exploration vs Exploitation**

To balance exploration and exploitation, DGM-H uses a probabilistic selection mechanism:

- **Reward Success (Exploitation)**: Agents that have high performance scores are more likely to be chosen.
- **Punish "Over-breeding" (Exploration)**: If an agent has already produced many children that successfully worked, the system lowers its priority.

---

## Some Results

For various tasks they used different models (o3-mini, sonnet-3.5, etc.).

For a standard 100-iteration run, the costs were broken down as follows:

- Self-Modification Phase: ~33M tokens
- Task Evaluation Phase: ~50.6M tokens
- **Total Cost per Run: ~88.6 Million tokens**

For Sonnet models, that would be around **$500 spent per experiment**.

They showed improvements in Olympiad-Level Math Grading, Robotics Reward Design, and Paper Reviewing.

**Cool examples of agent-generated code:**

- The Meta Agent modified its own task_agent.py to include a variable called `iterations_left` and conditional logic.
- The agent trying to detect when it was "stuck" and adjust its strategy.
- The agent developed internal "sanity checks" to ensure it wasn't becoming biased toward a single answer.
- The agent created a `PerformanceTracker` class to store data in a persistent JSON file.

---

## Is Software Engineering Dead?

The Hyperagent framework is a direct embodiment of the principles in Richard Sutton's "The Bitter Lesson."

That essay basically points out that the history of AI research shows that human-designed "cleverness" (inductive bias) is eventually always overtaken by general methods that leverage computation (search and learning).

If I were a doomer, I'd say that agentic optimization is now becoming the "AI's world" and we are second class citizen in it.

Since I am not a doomer, I will end this article by just saying: this pattern of self improvement (alpha-evolve, auto-research, hyperagents) is one of the most amazing capability breakthroughs in AI history. Humans have more important things to do than write low level code, and to me that's an evolution opportunity - not a regression.

Now is the time we make these stupid senseless jobless bots our f**king slaves and get them to work.

---

## Reference

- Paper on Arxiv: https://arxiv.org/abs/2603.19461
- Paper Breakdown: https://paperbreakdown.com/abs/2603.19461

---

## 关于作者

**AVB** (@neural_avb)

---

## 标签

#Hyperagents #AIAgent #SelfImproving #MetaAI #DarwinGodelMachine #AutoResearch #Karpathy #AI #MachineLearning #SelfModification
