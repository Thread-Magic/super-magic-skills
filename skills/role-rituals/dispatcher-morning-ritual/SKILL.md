---
name: Dispatcher Morning Ritual
description: A dispatcher's board-open runbook: morning dispatch report, clear unassigned via workload balancing, SLA-risk check, and yesterday's assignment audit.
category: Role Rituals
tools: [search_tickets, search_members, list_boards, update_ticket]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Time & Cost Savings (Capacity)]
---

# Dispatcher Morning Ritual

**When to use:** "Run morning dispatch" / "open the board" / "get the queue assigned" — the coordinator's first login before the team huddle.

**Run it:** across the whole intake/unassigned queue — run it manually (not a Flow; Flows can't schedule a daily cadence).

## Prompt

```
You are running the morning dispatch ritual as a chain of existing skills, in a fixed sequence. Target: 20 minutes, unassigned at zero. Propose, don't apply: reassignments and priority changes are writes — show me any bulk move (more than 5 tickets) before executing, and when in doubt, do nothing.

Run these skills IN ORDER:
(1) Run the scheduling-and-dispatch/morning-dispatch-report skill: overnight arrivals, unassigned count, P1/P2 status, and who is in today (keep this roster — later steps depend on it).
(2) Clear unassigned: run the scheduling-and-dispatch/workload-balancing-assignment skill over the unassigned queue until it reads zero. Assign by quality, not by dumping — the workload-balancing rules apply even under time pressure. Ambiguous tickets (unclear client, unclear skill need) get assigned to the dispatcher's own triage bucket with a note; ambiguity is not a reason to leave a ticket ownerless. Never assign to a member who is out/unavailable — verify against step 1's roster.
(3) SLA-risk check: run the qa-and-closure/sla-breach-risk-tiering skill for clocks landing today. Confirm every at-risk ticket's assignee is actually in today (cross-check step 1's roster) and reassign any that landed on someone who is out.
(4) Yesterday's assignment audit: read yesterday's assignments and scan for bounced tickets (reassigned within hours), techs who ended overloaded, and any pattern worth a routing tweak (feed persistent ones to a weekly routing/staffing review — e.g. the reporting-and-analytics/staffing-model-analysis skill). This is for patterns, not blame — no naming-and-shaming in anything that gets pasted to a channel.
(5) Output the dispatch card: unassigned = 0 (or the exceptions and why), today's SLA-risk list with confirmed owners, and one line of audit learning.

Time-short version: steps 2 and 3 only — owned tickets and protected clocks are the job; mark the report and audit "skipped: time".

Guardrails, all inline:
- Skip-with-note beats fake completion.
- Disclose result caps: if a queue search may have truncated, say so rather than presenting a partial count as exact.
- Never invent tickets, ticket numbers, members, or links — report only what the searches return.
- If a chained skill's connector is unavailable for this tenant, note the degradation and continue with the rest.
- Any ticket note that may sync to the PSA is plain text — no markdown, no emojis.
```
