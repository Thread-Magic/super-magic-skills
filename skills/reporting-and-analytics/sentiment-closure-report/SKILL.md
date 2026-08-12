---
name: Sentiment Closure Report
description: Bucket closed tickets by sentiment score per client, tech, or period, with driver messages cited so a low score is explainable, not just a number.
category: Reporting & Analytics
tools: [search_tickets, search_clients, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Sentiment Closure Report

**When to use:** "Sentiment on everything we closed last month," "which clients / techs had the most negative closes?", "show closure sentiment by week for <client>," or prepping a QBR or coaching conversation with evidence, not vibes.

**Run it:** across all closed tickets in the range — manually on demand (Thread Flows are ticket-event triggered with no schedule, so this can't run itself).

## Prompt

```
How did clients actually feel about the tickets you closed? Take the closed tickets in
a range, bucket them by sentiment, break it down by client / tech / period, and —
crucially — cite the messages that drove the low (and high) scores so the report is
actionable, not just a gauge. Read-only; this changes nothing.

This runs MANUALLY on demand — Thread Flows are ticket-event triggered with no
schedule/cron, so this is not a scheduled skill; run it on request or from an external
scheduler.

1. Scope the population: closed tickets within the requested date range. Apply any
   client/tech filter asked for, looking up the client or tech names first.

2. Pull the tickets and read each ticket's sentiment score. Bucket
   them — Negative / Neutral / Positive (or the desk's score bands) — and count per
   bucket. Never invent a sentiment value or a message.

3. Break down by the axis requested: per client, per tech, or per period (week/month).
   Show counts and the share negative, not just an average that hides a bad tail — a
   handful of very negative closes matters more than the mean.

4. CITE DRIVERS. For the negative bucket (and a couple of strong positives), quote or
   paraphrase the specific message(s) that drove the score, with the ticket number — so
   a reader can see WHY. This is the point of the report.

5. RESPONSE/COVERAGE HONESTY: always show the scored-vs-total denominator — state how
   many closed tickets actually had a sentiment score. Never present sentiment on 12
   tickets as if it characterized 300 closes.

6. Attribute fairly — a negative sentiment isn't automatically the assigned tech's
   fault; present it as signal, not a verdict. Close with the one or two patterns worth
   acting on (a recurring complaint theme, a client trending down) and offer a
   drill-down.
```
