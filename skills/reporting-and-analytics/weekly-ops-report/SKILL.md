---
name: Weekly Ops Report
description: A service manager wants the weekly service-desk report — team volume, closures, sentiment, aging, and anything anomalous versus the prior week.
category: Reporting & Analytics
tools: [search_tickets, search_members, list_boards, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Weekly Ops Report

**When to use:** "Run the weekly ops report" / "how did the desk do last week?" — a recurring Monday-morning summary for a lead or director, or "compare last week to the week before, anything off?"

**Run it:** across all tickets in the period — manually on demand (Thread Flows are ticket-event triggered with no schedule, so this can't run itself).

## Prompt

```
Produce the weekly operations readout for the service desk: what came in, what got
closed, how clients felt, what is aging, and what looked unusual — a fast stats pass
first, then targeted deep dives only where something moved.

This runs MANUALLY on demand — Thread Flows are ticket-event triggered with no
schedule/cron, so this is not an unattended/scheduled skill; run it on request or from
an external scheduler that invokes Super Magic.

1. Confirm the period (default: last full week) and the boards in scope.
   Exclude junk/NOC and internal-noise boards up front.

2. FAST STATS PASS — run split searches per signal per board (opened, closed, still
   open, aged past threshold, negative sentiment) rather than one giant query. Record
   which searches hit a result cap; never present a capped result as an exact total —
   disclose caps and give order-of-magnitude estimates instead.

3. Report headline numbers vs the prior week: volume in, closures, net queue change,
   aging count, sentiment trend. Exclude auto-closed statuses from closure credit so
   automation noise doesn't inflate the numbers. Do not fabricate a prior-week
   baseline; if last week's data is unavailable, report this week standalone and say so.

4. ANOMALY SCAN — flag anything that moved sharply week over week: a volume spike on
   one board or client, a closure-rate drop, a sentiment dip, a growing aging bucket.

5. TARGETED DEEP DIVES — for each flagged anomaly only, pull a narrow follow-up search
   and explain the likely driver in one or two sentences (alert storm, one large client
   incident, a tech out sick per the queue pattern). AGGREGATE rather than enumerate —
   patterns and counts, not ticket lists; name a specific ticket only when it explains
   an anomaly. Per-tech numbers are context, not rankings — benchmark role-aware and
   never flag a person on volume alone.

6. End with 2-3 recommended actions and a methodology note: period, boards
   included/excluded, searches run, and any result caps hit. Use fixed sections
   (Headlines / Anomalies / Actions / Methodology). If a search fails or returns
   nothing, state "no data for <section>" rather than guessing.
```
