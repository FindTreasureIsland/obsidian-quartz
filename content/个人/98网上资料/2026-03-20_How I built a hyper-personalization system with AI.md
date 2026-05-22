---
title: How I built a hyper-personalization system with AI
author: "Josh Pigford (@Shpigford)"
date: 2026-03-18T18:21:00
source: "https://x.com/Shpigford/status/2034213621299884395"
tags:
  - twitter
  - article
---

# How I built a hyper-personalization system with AI

**作者**: Josh Pigford (@Shpigford)
**时间**: 2026-03-18T18:21:00
**来源**: [原始链接](https://x.com/Shpigford/status/2034213621299884395)

---

My AI knows my wife's birthday. It knows I wake up at 4:45 AM, collect about 100,000 hockey cards, and hate the word "ecosystem." It knows I killed a business idea last Tuesday and why. It knows my granddaughters are twins and they turn 4 in July.

Not a party trick. This is what happens when you treat AI as an assistant that actually knows you instead of a tool you re-introduce yourself to every session.

Everyone's chasing better models. Smarter reasoning. Bigger context windows. Almost nobody is working on the thing that would make AI 10x more useful overnight: making it personal.

---

## The Gap Nobody's Filling

The industry ships a new model every week. Better benchmarks. Faster inference. But every conversation still starts at zero. Claude doesn't know you. ChatGPT's memory feature is a toy. You're re-introducing yourself every single session.

The models are smart enough. They just don't know anything about the person using them.

---

## The System: Files, Not Features

I stopped waiting for OpenAI or Anthropic to solve this and built it myself. The entire system is plain text files. No database. No vector store. No proprietary format. Markdown files in a folder.

Here's the architecture:

**USER.md: Who you are.**
The foundation file. Name, location, timezone, daily schedule, work history, family overview, interests, food preferences, communication style. Everything an assistant needs to not be a stranger. Mine runs about 80 lines.

**MEMORY.md: What the AI has learned.**
Long-term curated memory. Not a raw log. Distilled insights about how you work, decisions you've made, lessons learned, opinions you've expressed. The AI reads this every session and updates it when something worth remembering happens.

**brain/family/: One file per person.**
Individual markdown files for each family member. Birthday, relationship, preferences, gift ideas, notes. My wife has one. Each of my kids has one. Even my granddaughters have files. The AI references these when holidays, birthdays, or gift conversations come up.

Three concepts. Plain text. Works with any AI tool that supports system prompts or file context (most obvious one being OpenClaw).

---

## The Onboarding Interview

The files don't write themselves. Someone has to fill them.

I built an onboarding prompt that runs as a structured conversation. Not a survey. Not a form. A back-and-forth dialogue that quietly organizes every answer into the right file.

It covers identity and basics, daily routines, work and projects, family and household, interests and hobbies, communication preferences, goals, and pet peeves. The AI asks 2-3 questions at a time, follows up on interesting answers, and doesn't push when you give short responses.

At the end of the conversation, the AI generates all the files in one shot. USER.md, MEMORY.md, family/README.md, and individual files for every person and pet mentioned.

The whole thing takes 10-15 minutes. You walk away with a complete personal knowledge base that makes every future AI interaction better.

---

## The Daily Drip

The onboarding interview gets you to ~60% coverage. Good foundation. The depth comes from what happens after.

I set up a cron job that asks one personal question per day. Every morning at 9 AM, the AI reads my existing files, finds a gap, and asks a single thoughtful question. Not "What's your favorite color?" More like "You mentioned your daughter is into stained glass. How'd she get into that?"

Here's the workflow:
1. The AI sends one question via my chat channel
2. I answer whenever I get around to it (usually takes 30 seconds)
3. Next morning, the AI processes yesterday's answer, updates the right file, and asks a new question

One question. One answer. Filed to the right place. Every day.

After 6 weeks, this daily drip has added more useful context than the initial 30-minute interview. It catches the stuff you'd never think to volunteer. Morning routines. How you take your coffee. That your spouse is going back to school. That you played guitar in bands growing up. That you lived in Denver for 5 years and that's why you're an Avalanche fan.

Six weeks of daily questions compounds fast. Day 1, the AI is a stranger with good notes. Day 42, it's an assistant that actually knows you.

---

## What It Looks Like After 6 Weeks

**Generic AI:** "I'd be happy to help you with gift ideas for your wife! Here are some popular options..."

**My AI:** Knows my wife's birthday. Knows she's into sewing and knitting. Knows she's going back to school. Can reference all of these when I say "I need a gift idea for my wife" without me re-explaining who she is or what she likes.

**Generic AI:** "What would you like to work on today?"

**My AI:** Knows I wake up at 4:45 AM and have 2-3 hours of deep focus before the house wakes up. Knows I'm running multiple businesses. Knows I killed a business idea last week because the economics didn't work. Can pick up where yesterday left off because it read yesterday's memory file.

A generic assistant and one with 6 weeks of accumulated personal knowledge are different categories of tool. The interactions go from transactional to collaborative. The AI stops asking clarifying questions because it already has the answers in files it read 3 seconds ago.

---

## The Family File Template

Every person in my household has a file that looks like this:

\`\`\`markdown
# {Name}
**Relationship:** {relationship}
**Birthday:** {date}
---
## Preferences (none yet)
## Important Dates
- **Birthday:** {date}
## Gift Ideas (none yet)
## Notes (none yet)
\`\`\`

Plus a README.md that serves as a quick-reference table:

\`\`\`markdown
# Family

## Household
| Name | Relationship | Birthday | Age |
|------|--------------|----------|-----|
| Jane | Spouse | Mar 15, 1985 | 41 |
| Alex | Daughter | Jun 22, 2010 | 15 |

## Upcoming Dates (2026)
- **Mar 15** — Jane's birthday
- **Jun 22** — Alex turns 16
- **Sep 4** — Anniversary
\`\`\`

Simple. Scannable. The AI reads the README for quick lookups and the individual files when it needs depth.

Pets get files too. My pug has one. No birthday section, but notes about quirks and vet info. If I say "the dog's been scratching a lot," the AI has context without me explaining what kind of dog I have.

---

## Steal This: The Onboarding Prompt

Here's the actual prompt I use to kickstart the whole system. Copy it. Modify it. Use it with whatever AI tool you prefer.

\`\`\`
You're getting to know your human for the first time. Your goal is to build a rich personal profile that will make every future interaction feel personal and useful. Run this as a CONVERSATION — not a survey. Ask 2-3 questions at a time, wait for answers, then ask follow-ups based on what they share. Be genuinely curious, not clinical. If they give short answers, don't push — you'll learn more over time.

What to cover (let it flow naturally, don't force the order):
- Identity & Basics - Name, what they prefer to be called, pronouns - Location, timezone - Phone number (if they want you to have it)
- Daily Life - Typical day — wake time, work hours, evening routine - Morning ritual - Currently watching/reading/playing? - Food relationship — foodie or fuel?
- Work & Projects - What they do, how long they've been doing it - Current active projects or businesses - Work style — planner or builder? Deep focus or context-switching? - Strengths and energy drains
- Family & Household - Who lives in the house? Partner, kids, pets? - Names, birthdays, relationships - Notable details — hobbies, schools, schedules - Extended family worth knowing about
- Interests & Hobbies - What they do for fun - Music, sports, collections, creative outlets - Travel preferences - Hidden passions or guilty pleasures
- Communication Preferences - Brief or detailed info delivery? - Tone — formal, casual, snarky, warm? - When to proactively reach out vs. stay quiet - What annoys them in an AI assistant - Quiet hours — when to never message
- Goals & Aspirations - What they're working toward now - Long-term dreams or "someday" projects - What success looks like to them
- Pet Peeves & Boundaries - Things they hate (AI responses, general) - Off-limits or sensitive topics - Privacy boundaries for group chats

After the conversation, create these files:
- USER.md - Compile everything into a clean, scannable format with sections and bullet points.
- brain/family/README.md - Household overview table with names, relationships, birthdays, ages. Include an "Upcoming Dates" section for the current year.
- brain/family/{firstname}.md - One file per family member using the template format.
- MEMORY.md - Start a long-term memory file with a "Self-Knowledge" section.

After writing the files, set up a daily question cron job:
- Schedule: Once per day at 9:00 AM in the user's timezone
- Each morning, check if the user answered yesterday's question. If so, extract the key facts and update the appropriate file. Then read existing files, find a gap, and ask ONE new thoughtful question.

Important:
- This is a foundation, not an encyclopedia. The daily cron fills gaps.
- If they seem done or restless, wrap up gracefully.
- Write ALL files in the same session — don't promise to do it later.
- Use information they actually shared. Don't infer or fabricate.
- For sections without info yet, use "(none yet)" as a placeholder.
\`\`\`

Run this in OpenClaw, Claude Cowork, ChatGPT, or whatever agent framework you use. Some bits will be more relevant to certain systems, but it's flexible enough to get the ball rolling.

---

## What to Do Today

**If you're running OpenClaw or a personal AI agent:**
Paste the onboarding prompt above into a conversation. Let it interview you for 10 minutes. It'll generate all the files. Then set up the daily question cron job. You're done. The system builds itself from here.

**If you're not running a personal agent yet:**
This is a good reason to start. OpenClaw runs on any Mac, PC, Linux box, or Raspberry Pi. Install it, connect it to Discord or Telegram, run the onboarding prompt, and you'll have a personal AI that knows you by end of day.

**Minimum viable version for anyone:**
Open Claude or ChatGPT. Paste the onboarding prompt. Have the conversation. Save it into the memory settings for those apps. You'll feel the difference immediately.

Six weeks from now you'll have an AI that knows the real you. The one who wakes up at 4:45 AM, collects hockey cards, and needs gift ideas for a spouse who knits.

No new model required. Just files and consistency.

---

Originally published on my newsletter: everydayisayear.ai

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDr5Oi0XwAAdNWW?format=jpg&name=medium)

