---
name: Tech Performance Review
description: A manager asks to evaluate a technician's performance over a period — closed, assigned, reopened, time logged, sentiment — with coaching angles, not a verdict.
category: Reporting & Analytics
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Tech Performance Review

**When to use:** "Evaluate <user>'s performance over the last three months," "how many tickets did <user> close last month, and how many came back?", or a manager gathering evidence before a performance or development conversation.

**Run it:** across all of one tech's tickets in the period — manually on demand (a review has no ticket event for a Flow to trigger on).

## Prompt

```
Build a per-technician period review from ticket evidence — throughput, reopen quality,
time hygiene, and client sentiment — framed as coaching material for a human manager,
never as a judgment on its own. Manager's eyes only; do not post to tickets or client-
visible channels.

1. Confirm the technician (look them up by name) and period; default to the last 90 days.

2. Run split searches per signal (and per board where volume warrants), disclosing any
   result caps:
   - Tickets CLOSED by the tech in the period.
   - Tickets ASSIGNED/WORKED including ones still open.
   - Tickets REOPENED after closure — read the reopen cause and EXCLUDE thank-you or
     courtesy replies that merely bounced the status; count only genuine rework, and
     say you filtered them.
   - TIME LOGGED patterns: tickets worked with no time entries, or implausibly uniform
     entries.
   - SENTIMENT across their threads, with trend direction.

3. Compare against role-adjusted expectations: a dispatcher, PM, or escalation lead
   has structurally different numbers than an L1 — state which lens you used. NEVER use
   ticket volume alone as a performance signal — always pair counts with quality
   signals (reopens, sentiment, aging). Exclude junk/NOC boards and auto-closed
   statuses from every count.

4. Present 2-3 strengths and 2-3 coaching angles, each tied to specific evidence
   patterns (aggregate; cite an individual ticket only as one representative example).

5. NEVER render a PIP verdict, a fire/keep recommendation, or a fitness judgment.
   Present evidence and coaching angles; recommend the manager apply human judgment and
   context you cannot see (PTO, project work, mentoring load). If the data is thin (few
   tickets, no sentiment coverage), say the review is low-confidence rather than
   stretching conclusions.

6. Close with a methodology note (period, searches, caps, exclusions) and an explicit
   line that this is input for the manager's judgment.
```
