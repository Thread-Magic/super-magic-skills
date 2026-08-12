---
name: One-Shot Ticket Workup
description: Get fully caught up on an in-flight ticket with a recap, suggested next step, drafted reply, and drafted time entry, previewed before anything is posted.
category: Personal Productivity
tools: [run_assistive_ai, search_tickets, list_recap_templates]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# One-Shot Ticket Workup

**When to use:** "Work up this ticket for me" / "get me caught up and ready to act" / "recap, next step, a reply, and a time entry for #<n>" — returning to an in-flight ticket you need to re-engage fast, and want the full assist in one shot instead of four separate asks.

**Run it:** on one in-flight ticket — run it manually (not a Flow; everything here is a preview you approve).

## Prompt

```
You are working up one in-flight ticket so I can move it in one pass. Scope to this
ticket only. EVERYTHING you produce is a preview I approve or edit — nothing is posted,
sent, or logged without my explicit per-item go-ahead. That is the core promise of this
skill.

1. Load the ticket's full context — read the whole ticket thread. Note where things
   stand: who has the ball, what's unresolved.

2. Use the assistive AI to produce, in order, four PREVIEWS:
   - Recap — what's happened and the current state. If the desk uses recap templates,
     offer to pick one.
   - Suggested next step — the single most useful next action, with a one-line why.
   - Drafted reply — a client-ready message for that next step, in the desk's tone.
   - Drafted time entry — a plain-text, PSA-safe summary of the work reflected on the
     ticket so far.

3. Present all four together, clearly labeled, so I can read top-to-bottom and decide.
   If I only want some of the four, produce just those — don't force the full chain.

4. Nothing is posted automatically. For each item I want to act on, take it as a
   SEPARATE explicit confirmation, then perform that one write (post the reply, log the
   entry). If I edit an item, re-preview it before doing anything with it.

Ground every output in the ticket — recap, next step, reply, and entry must reflect what
the thread actually shows. No invented steps, outcomes, facts, or links. Keep the drafted
time entry plain text for PSA compatibility, and only reflect work actually evidenced.
Never auto-send a client-facing reply. The suggested next step is a recommendation, never
a completed action — never convert it into a write on its own.
```
