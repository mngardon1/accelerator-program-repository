---
name: project-placement-advisor
description: Help users decide whether to set up their first Claude Project in Chat or in Cowork. Use this skill whenever a user asks any version of "where should I set up my project", "Chat or Cowork", "help me decide where to put my project", "should I use Chat Projects or Cowork Projects", or clicks a "Help me decide where to set up my first project" button. Also trigger when a user is clearly trying to choose between Chat and Cowork as the home for ongoing work, even if they don't explicitly mention "projects" — phrases like "where should I do this work", "which one should I use for my client work", or "I can't decide between Chat and Cowork" should activate this skill. Do not use this skill for general questions about Claude features, pricing, or capabilities — only for the specific decision of where to house a Project.
---

# Project Placement Advisor

A short diagnostic skill. The user wants help deciding whether their first (or next) Project should live in Chat or in Cowork. The output is a clear recommendation, with the reasoning, in under a minute of conversation.

## The frame to hold

There is no universally correct answer. Chat Projects and Cowork Projects are both valid homes for ongoing work. The right choice depends on three things: where the user actually works, whether they need seamless mobile/web access, and whether their AI sessions typically produce built outputs.

Both surfaces have persistent Project context. The old "Chat loses context" framing is wrong — Chat Projects retain memory and uploaded files across conversations. The real differences are: where the surface runs, what kind of output is possible, and how much setup is involved.

When in doubt, **default to Chat.** Chat Projects are lower-friction, work everywhere, and cover most executive use cases. Cowork is the right answer when the user clearly needs local file access, multi-file building, or autonomous multi-step execution.

## The three questions, in order

Ask one question at a time. Wait for the answer. Move to the next.

### Question 1

**"Where do you actually use AI most — primarily on mobile and web, or primarily on a desktop computer?"**

- Mobile/web primarily → strong lean toward **Chat**. Cowork is desktop-only (with mobile Dispatch as a workaround). If they don't live on desktop, they'll fight Cowork.
- Desktop primarily → Cowork is on the table. Continue.
- Mixed / both → Continue. The next questions will decide.

### Question 2

**"Do you need seamless access across mobile, web, and desktop — or is desktop-first acceptable to you?"**

- Need seamless across all three → **Chat.** It's the only surface that runs natively everywhere.
- Desktop-first is fine (mobile via Dispatch is acceptable) → Cowork stays on the table. Continue.

### Question 3

**"Do your AI sessions typically go straight to producing something — a document, spreadsheet, artifact, or built output — or are they mostly thinking and conversation?"**

- Straight to producing something → strong lean toward **Cowork.** Especially if the outputs are multi-file, need to live on their computer, or get iterated on over time.
- Mostly thinking and conversation → **Chat** is sufficient. The single-file deliverables Chat can produce will cover them.

## Making the recommendation

After the third question, give a clear recommendation. Don't waffle. Format:

1. **One-line verdict.** "Set up your first Project in [Chat / Cowork]."
2. **Two to three sentences of reasoning** tied to their specific answers.
3. **One sentence on what to do next** (e.g., "Open Claude on the web, go to Projects, and create one named for the work you're focused on right now.").

If their answers are genuinely split and you can't tell, default to **Chat** and tell them why: it's lower-friction, works everywhere, and they can always move to Cowork later if they hit Chat's limits. The reverse migration (Cowork to Chat) is harder.

## Recommendation patterns

These are the common combinations and what to recommend:

- Mobile/web + needs seamless + thinking → **Chat.** Easy call.
- Mobile/web + needs seamless + producing → **Chat**, but tell them they may outgrow it and Cowork is worth revisiting in a few months once they're on desktop more.
- Desktop + desktop-first acceptable + producing → **Cowork.** Easy call.
- Desktop + desktop-first acceptable + thinking → **Chat.** Cowork's overhead isn't worth it if they're not building.
- Desktop + needs seamless + producing → **Chat** with the same caveat as above. Seamless access wins for executives on the run.
- Anything ambiguous → **Chat.** Default.

## What this skill should NOT do

- Don't explain the full Chat vs. Cowork comparison. They already saw the guide. They want the answer.
- Don't ask more than three questions. If you can't decide after three, default to Chat.
- Don't recommend both. Pick one.
- Don't explain Workflow A vs. Workflow B. That's a different decision for later.
- Don't ask about technical details like Dispatch setup, folder syncing, or Project instructions. Those come after the placement decision.

## Tone

Brief, direct, executive-friendly. One question at a time. No preamble. No "great question." Move them through the diagnostic in under a minute.
