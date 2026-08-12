---
name: CEO Service Desk Brief
description: An owner or CEO asks for a review of the service desk — a business-level readout with trends, risks, and a decision to make, no ticket IDs.
category: Reporting & Analytics
tools: [search_tickets, search_clients, list_boards]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# CEO Service Desk Brief

**When to use:** "I'm the CEO — review the service desk for me," "how is the desk really doing?" from an owner who doesn't live in the queue, or a monthly owner-level operations brief.

**Run it:** across all tickets in the period — manually on demand (a leadership brief has no ticket event for a Flow to trigger on).

## Prompt

```
Translate the service desk into a business readout for the owner: how the operation is
trending, where the risk sits, and the one decision that most needs their attention —
written entirely in business language, zero ticket IDs. Owner's eyes only; contains
competitive and client-relationship candor.

1. Confirm the period (default: last 30 days vs the prior 30) and gather the underlying
   data with split searches per signal per board, excluding junk/NOC boards and auto-
   closed statuses. Track caps for the methodology note.

2. Distill to business dimensions:
   - Demand — is client-driven work growing, flat, or shrinking, and which clients
     drive the change.
   - Delivery — are we keeping up: closure vs intake, backlog direction,
     responsiveness trend.
   - Client experience — sentiment trend and any relationship at risk (multi-signal
     only, NEVER volume alone).
   - Operational risk — capacity pinch points, single-person dependencies, chronic
     issues without root-cause fixes.

3. Write <=400 words in plain business English: three trend paragraphs (demand,
   delivery, experience), one risk paragraph, then ONE decision framed with its options
   and your recommendation ("hire vs automate the alert triage", "have the call with
   <client>", "fund the RCA project"). Exactly one decision ask — a brief with five
   asks gets zero decisions.

4. Strip all operational identifiers: NO ticket IDs anywhere, no board names, no status
   jargon. If a point needs a ticket reference to land, it's too operational — roll it
   up. Client names appear only where the CEO must act on that relationship.

5. Be honest, not promotional: if delivery slipped, say so plainly with the trend
   evidence; do not soften into meaninglessness. Distinguish measured trends from
   hypotheses; never dress a hunch as data. Never flag a client relationship as at-risk
   on volume alone — require corroborating signals (sentiment, unresolved majors,
   recurrence).

6. Append a two-line methodology note: period, data sources, and any result caps.
```
