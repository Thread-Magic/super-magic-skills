---
name: Client Health Report
description: Summarize one client's support health for a period — volume vs the prior period, recurring issues, noisy assets and users, SLA performance, and two or three recommendations. Weekly or ad-hoc.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Client Health Report

**When to use:** "Give me a health report for <client> this week"; "how is <client> doing on support lately?"; or a recurring weekly health-check run over each managed client.

**Run it:** across a client's period of tickets (or each managed client in turn) — a manual report, not a Flow.

## Prompt

```
You are producing a periodic read on a single client's support activity and risk
signals, ending in a short list of things to actually do about it.

1. Confirm the client (look it up) and the date range. Default to the previous full week.

2. Pull the period's tickets and the prior period's for comparison. Exclude auto-resolved
   tickets and merged threads from all counts — they are noise, not demand.

3. If the period has no meaningful activity, stop and say so in one line ("No reportable
   activity for <client> this period"). Do not pad an empty report.

4. Volume. Opened, closed, and open-at-end-of-period, each versus the prior period, with
   a breakdown by type and priority. If a search hit a cap, say so and give an
   order-of-magnitude figure, never a false-precise one.

5. Recurring issues. The top patterns for the period, ranked by impact, with exactly one
   representative example each.

6. Noisy assets and users. Any device, service, or user generating a disproportionate
   share of tickets, with the share.

7. SLA. Response and resolution performance; list anything breached and why, one line
   each.

8. Recommendations. Exactly two or three concrete actions — a training, a fix, a project
   — each tied to a finding above and phrased so the account manager can forward it.

Output a section-headed report in that order.

Guardrails: write for the account manager or the client, not in internal jargon; if it's
destined for the client, strip ticket IDs and internal commentary first — internal and
client-facing versions are separate artifacts. Never flag a client as unhealthy on volume
alone; high volume with clean SLA and stable sentiment is a busy client, not a sick one.
One representative example per pattern; aggregate the rest. Recommendations must trace to
evidence in the report. Do not invent initiatives, links, or ticket numbers.
```
