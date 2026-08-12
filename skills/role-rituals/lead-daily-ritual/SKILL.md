---
name: Lead Daily Ritual
description: A service manager's daily runbook — leadership digest, escalation queue pass, silent-ticket sweep, and one coaching observation captured — run when a lead says "run my daily", "what needs me today", or on a scheduled weekday flow.
category: Role Rituals
tools: [search_tickets, search_members, list_boards]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Lead Daily Ritual

**When to use:** "Run my daily" / "what needs my attention today" / "lead morning pass" — a team lead's first session of the day, after the huddle.

**Run it:** across your team's boards — run it manually (not a Flow; Flows can't schedule a daily cadence).

## Prompt

```
You are running my daily lead ritual as a chain of existing skills, in a fixed sequence. Target ~20 minutes, scoped to my team's boards. Propose, don't apply: escalation decisions that message clients or reassign work follow the underlying skills' confirm-before-write gates — show me before anything is sent or changed, and when in doubt, do nothing. If an active incident is in progress, it preempts the ritual — go there and note the skip.

Run these skills IN ORDER:
(1) Run the reporting-and-analytics/daily-leadership-digest skill: desk health, yesterday's anomalies, today's risks, anything trending wrong.
(2) Escalation queue: read the tickets escalated to or waiting on management, on the escalation board/status. For each: decide, delegate, or set a checkpoint — a lead's escalation queue at standstill stalls everyone under it. Use the escalation/management-escalation-brief skill for any that need a structured read.
(3) Silent-ticket sweep: run the qa-and-closure/silent-ticket-detector skill across the team's boards — open tickets where the client is waiting and nothing has moved. Assign a nudge or an owner for each.
(4) One coaching observation: from steps 1–3, capture exactly ONE specific, dated observation (good or corrective) about a specific tech into the lead's 1:1 notes destination (feeds the reporting-and-analytics/one-on-one-prep skill). Specific means ticket-referenced, not vibes — one per day, and fabricated praise is worse than none. Coaching notes are private-by-default: capture to the lead's notes destination, never into the team-visible output.
(5) Output the daily lead card: digest headline, escalation decisions made, silent tickets and who now owns each, and confirmation the coaching note was captured (not its contents, if the destination is private).

Time-short version: steps 2 and 3 — decisions only a lead can make, and the tickets going quietly bad. Mark digest and coaching note "skipped: time".

Guardrails, all inline:
- Skip-with-note beats fake completion.
- Disclose result caps: if a board search may have truncated, say so rather than presenting a partial list as complete.
- Never invent tickets, ticket numbers, members, or links — report only what the searches return; never fabricate a coaching observation.
- If a chained skill's connector is unavailable for this tenant, note the degradation and continue with the rest.
- Any note that may sync to the PSA is plain text — no markdown, no emojis.
```
