---
title: "A Guide to Agent-native Product Management"
author: "Marcus Moretti"
source: "every.to"
url: "https://every.to/guides/ai-product-management-guide"
date: "2026-04-27"
saved: "2026-05-02"
tags:
---

# A Guide to Agent-native Product Management

*By Marcus Moretti · 2026-04-27*

The discipline of product management 

 "Product management" was born in the 1930s within the consumer goods giant Procter & Gamble. As the company expanded its product offering, leaders realized their products would be more successful if they ceded control to direct managers of the products. Someone needed to be in charge of each product, and they called that person the "Brand Man." The raison d'etre of product management—ownership and accountability—survives to this day. In the intervening years, however, the product management job description has been rewritten several times over. In the 1940s and 1950s, Hewlett-Packard's product managers became the middlemen between customers and engineers. Toward the end of the century, internet startup PMs added user experience design, agile development, and A/B testing to their toolkits. Now, PMs need to be good at everything: design and diplomacy, sales and statistics. Thousands of startups have raised billions of dollars to help PMs across these disciplines. But that introduced a new problem: The average company today has over 100 software subscriptions , an overload that impacts PMs more than other functions given how many other roles and disciplines they interact with. No wonder many people I know in product management feel burnt out. Now, much of the interdisciplinary work that goes into product management can be done by an LLM in minutes, sometimes seconds. What used to be a three-hour-long analytics investigation is now a simple back-and-forth with Claude. A product review that used to be a fortnightly chore emerges from a single typo-ridden chat message. This has been my recent experience, at least. I no longer struggle with semicolons in SQL queries or even write tickets. All of my product management work happens in conversation with, in my case, Claude Code. The conversation is the work. The following guide is a point-in-time snapshot of how I'm doing product management with agents. New AI tools launch every day, and my workflow changes at least weekly. I've tried to capture here the main pillars of my workflow that likely won't change for months. It's hard to see ahead farther than that these days. 

 The main PM loop 

 Plan → ship → review → repeat This is a familiar software development lifecycle (SDLC) loop. Product management happens mainly at the "plan" and "review" stages. For more on the "ship" stage, check out my colleague Kieran Klaassen 's guide to compound engineering . 
 Plan : This starts with a product strategy. What is the problem we're solving, and how do we solve it? Who is our product for? How do we measure success? What are the main tracks of work to realize our solution? This strategy then informs feature ideas, prioritization, and feature specs. 
 Ship : Build the thing. Make sure it works. Deploy it. 
 Review : Gather the learnings from building the thing. Save those for later. Once the feature has been live for some time, check the metrics. This will be covered below in the new "product-pulse" skill that's part of compound engineering. It's important to pick the right metrics, measure them effectively, and regularly review them. 
 Everything that ships is an experiment. You never know for sure how users are going to react to something new. The more you ship, the more you learn—and those learnings reinforce themselves over time, allowing you to serve customers better. Once enough learnings accumulate, it's time to revisit the strategy. Is this still the winning approach, in light of what we now know? The answer may be yes, but if it's no, change it and get back to shipping. But everything starts with… 

 The strategy document 

 As Kieran says, software development has shifted from 20 percent planning and 80 percent execution to 80 percent planning and 20 percent execution. The foundation of all software planning is the strategy. The new compound engineering command /ce-strategy takes its structure from the book Good Strategy Bad Strategy by management professor Richard Rumelt . As the title suggests, he surveys lots of real examples, from companies and governments, and classifies them as good strategies or bad strategies. The first time you run /ce-strategy in an agent environment (Claude Code, Codex, etc.), you'll be asked a series of questions and ultimately get a strategy.md file. The components of strategy.md are: 

 Target problem. What is the current pain that people feel, which will encourage them to entertain your pitch? Ideally, this is a recurring, expensive problem. 

 Approach. One or two sentences describing the guiding policy for the product. If you said these sentences to a person experiencing the target problem, they should be unmistakably intrigued. The approach is not a goal or a generic positive description ("better tools for X"), and it's not a feature. The approach is a description of your product's specific angle of solving the target problem. 

 Who it's for. This section describes the one or more personas that will use your product. Good personas answer: What are their jobs to be done? What are their pain points? What are they currently paying for the problem, in money or time? 

 Success metrics. How will you know if the product is working? These should be measurable, ideally tied to revenue or some other north star metric. Your goals are first-order outcomes (revenue, retention, activation), not vanity metrics (page views, sign-ups). 

 Main work tracks. What are the big buckets of work required to ship this product? These can be UX, backend, ML, data, or growth tracks. 

 Risks. What's the riskiest part of the plan? What assumptions are you making that could be wrong? What technical or product risks exist? 

 The product-pulse skill 

 After strategy, the other key skill is product-pulse. This compound engineering command sets up an automated weekly (or daily) metrics review. The goal is to have a regular, systematic process for reviewing product metrics and generating insights. It solves two problems: 

 First, most people don't review metrics regularly. The "review" step of the plan → ship → review loop rarely happens consistently. Automated monitoring helps. Second, when people do review metrics, they don't know what to look for. You need a framework for interpreting data. The product-pulse skill gives you that framework. 

 What to measure 

 The first question is what metrics to track. In compound engineering's product-pulse skill, you configure the following metrics for weekly review: 

 North star metric. The single metric that best captures the value your product delivers to customers. For Slack, it's daily active users connected to coworkers. For Superhuman, it's emails processed per hour. 

 Lead indicators. These are metrics that are likely to change before the north star metric changes. They give you early warning signs. If your lead indicators are trending in the wrong direction, you can course-correct before it shows up in your north star. 

 Lag indicators. These are the metrics that tell you if you've already won or lost—revenue, churn, NPS. 

 Why this setup? 

 With lead and lag indicators, you can answer questions like: "Our north star is up 10 percent this month, but our lead indicators are trending down. What does that mean?" The answer might be that a recent change had a short-term positive effect but will eventually hurt. Or it could be seasonal noise. Either way, you're in a better position to investigate. 

 Weekly review cadence 

 The weekly review should be a standing meeting on your calendar. It should be 30 minutes, no longer. The goal is to spot anomalies, not to deep dive. If something looks interesting, schedule a separate investigation. To run the weekly review, you go into whatever channel you've set up for your product-pulse (Slack, email, Linear, Notion), and you ask: "What are we learning this week?" The agent will generate a report based on the data. 

 The agent knows what your metrics are, where the data lives, and what a reasonable baseline is. It will flag anomalies and offer hypotheses about what might be causing them. 

 This is the compound engineering approach to product review: not a manual, tedious process, but an automated, ongoing conversation about what's working and what isn't. 

 When to delegate 

 There are two main modes for working with an agent on product work: delegation and collaboration. 

 Delegation is when you hand a task to an agent and let it run. This is great for well-defined, bounded tasks: a research spike, a data analysis job, a spec review. 

 Collaboration is when you work with an agent in a back-and-forth conversation. This is better for ambiguous, evolving tasks: brainstorming, strategy development, metric interpretation. 

 In my experience, most product work benefits from collaboration. But delegation is useful for repetitive, well-defined tasks that don't require judgment. 

 Putting it together 

 The compound engineering approach to product management has three main pillars: 

 Strategy: Define what you're building and why, using /ce-strategy. 
 Ship: Build it using compound engineering's agent commands. 
 Review: Monitor your metrics using /ce-product-pulse and review weekly. 

 These three steps create a feedback loop that helps you build the right thing, measure whether it's working, and iterate based on what you learn. 

 The more you ship, the more you learn. The more you learn, the better your strategy. The better your strategy, the more confident you can be in what you ship. This virtuous cycle is the foundation of good product management in the age of agents.

---

Source: [A Guide to Agent-native Product Management](https://every.to/guides/ai-product-management-guide)
