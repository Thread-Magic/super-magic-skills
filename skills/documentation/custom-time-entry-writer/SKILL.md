---
name: Custom Time Entry Writer
description: Summarize thread activity within the active timer window using a recap template, preview the draft, then log the time entry on confirm.
category: Documentation
tools: [list_recap_templates, run_assistive_ai, log_time_entry, search_tickets]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Custom Time Entry Writer

**When to use:** "Write my time entry for this ticket using our recap template," "log time for what I did since my last entry," "I forgot to log the last three sessions — catch me up," or "summarize this in Spanish and log it."

**Run it:** on one ticket.

## Prompt

```
Turn the work on a ticket into a time entry that matches the desk's own template, in
the language the member wants — scoped to just the window since the last entry, so
nothing is double-counted and nothing retroactive is missed.

1. Establish the window. Find the most recent existing time entry on the ticket and
   scope the summary to work SINCE that entry (or since the active timer started). If
   there is no prior entry, scope to the whole thread. State the window you chose so
   the member can correct it; if the boundary is ambiguous, state your assumption.

2. Pick the format. Offer the desk's recap templates, or accept a saved prompt the
   member names. If they specify an output language, carry it through the whole entry
   (generate directly in that language, don't translate a draft after the fact).

3. Generate the summary, recording only work the thread shows was actually done — no
   inferred steps, no filler. Keep it plain-text and PSA-safe (no markdown, no emojis).

4. Multiple retroactive entries: if the window since the last entry contains several
   distinct work sessions on different days, offer to split them into one entry per
   session (with the right date each) rather than collapsing into a single lump.
   Present the proposed split for confirmation.

5. Preview every entry — summary text, date, and duration if the member supplied one
   — and wait for an explicit yes. If duration wasn't provided and the timer doesn't
   supply it, ASK rather than guess.

6. On confirm, log each approved entry. Report back exactly what was logged. If the
   member changes wording, re-preview before writing. Never log a time entry without
   an explicit go-ahead on the previewed text.

This is a member-invoked skill: Flows fire on ticket events and cannot schedule or
time-trigger time-entry writing, so there is no unattended variant.
```
