---
name: Trend Root-Cause Mining
description: Someone asks what is making the desk so busy, what is driving ticket volume, or what the top recurring issues are for a period.
category: Reporting & Analytics
tools: [search_tickets, list_boards, search_clients]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Trend Root-Cause Mining

**When to use:** "What's making us so busy this week/month?", "what are the top recurring issues across the desk?", or "volume is up 20% — where is it coming from?"

**Run it:** across all tickets in the period — manually on demand (a volume-driver analysis has no ticket event for a Flow to trigger on).

## Prompt

```
Answer "why is the desk busy?" with evidence: the top recurring volume drivers for the
period, each sized, explained, and illustrated with exactly ONE representative ticket.

1. Confirm the period (default: last 30 days) and pull the ticket population with split
   searches per board — and per obvious segment (client, type) when a board would cap;
   disclose caps. Do not invent ticket numbers, counts, or percentages.

2. Cluster tickets into drivers by shared signal: same issue type, same client, same
   asset/service, same alert source, or same request category. Read titles and
   summaries; do not rely on categories alone if they look inconsistently applied. If
   clustering is ambiguous, present the uncertainty.

3. Rank the top 5-8 drivers by ticket count and estimated time consumed (thread length
   and time entries as proxies). Distinguish "busy" from "many tickets": a few heavy
   escalations can outweigh dozens of password resets — weigh by effort, not count
   alone.

4. For each driver give: name, size (count and rough % of period volume), the likely
   root cause in one or two sentences, and ONE representative ticket as the example —
   never a full listing. A wall of ticket numbers is a failure mode. Root causes are
   hypotheses read from ticket text; label them as such and recommend verification
   before investment.

5. Tag each driver with its fix lane: automation candidate (intent/flow), monitoring
   retune, client training, project/RCA needed, or vendor issue. Exclude junk/NOC
   boards and auto-closed noise unless the question is specifically about alert noise;
   if noise dominates real volume, say so as its own finding.

6. Close with the 2-3 drivers most worth acting on and a methodology note (period,
   boards, clustering basis, caps).
```
