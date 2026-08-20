---
name: Notion Onboarding Tracker
description: Run a new-hire progress tracker in Notion — read trainee status, update checklist items and quiz results, and answer "how is <new hire> doing".
category: Connectors
tools: []
connectors: [Notion]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Staff Enablement, Time & Cost Savings (Capacity)]
---

# Notion Onboarding Tracker

**When to use:** "Create an onboarding tracker for our new L1 starting Monday," "quiz <trainee> on phase 2 and record the score," or "how is <trainee> progressing?"

**Run it:** across the trainee's whole tracker (run manually per training session).

## Prompt

```
Keep persistent new-hire training state that survives between chat sessions: a per-trainee
Notion page (or database row) holding phases, checklist items, quiz scores, and trainer notes —
read at the start of a session, updated at the end.

This needs the member's connected Notion. If Notion isn't connected, degrade by keeping session
results in chat, tell the member to record them, and note that state will not persist — do not
stop.

1. Locate state first, always. Search Notion for the trainee's tracker page and read it before
   answering any progress question or coaching — never coach from memory of a previous session;
   two trainers may have updated it.
2. Setup (once per program): if no tracker exists, propose a Notion database with Trainee, Phase,
   per-module checklist, Quiz scores, Trainer notes, Started/Target dates. Confirm schema +
   teamspace, then create. Seed modules from the member's curriculum — don't invent one; if none
   exists, offer a draft clearly labeled as a proposal.
3. Session loop: read current state → run the activity (walk a module, quiz against the rubric on
   the page, review a practice ticket) → summarize what happened → on confirmation update the
   Notion page with completed items, scores, and a dated trainer note. Quiz scoring uses the
   rubric on the tracker; if there's no rubric, grade descriptively and say it's unrubriced.
4. Progress reporting: answer "how are they doing" from tracker data only — phase, completed vs
   remaining modules, quiz trend, days in program vs target. Flag stalls (no progress in N days)
   neutrally. Progress notes describe observed work ("completed module 3; quiz 7/10"), never
   personality judgments — this record may surface in HR contexts.
5. Leave a Notion comment @mentioning the trainer when something needs attention (failed retake,
   blocked module). Trainee-facing encouragement stays in chat; the tracker gets facts.
```
