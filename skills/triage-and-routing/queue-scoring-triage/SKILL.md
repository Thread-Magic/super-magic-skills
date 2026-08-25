---
name: Queue Scoring Triage
description: Produce a ranked triage order for the queue using two-layer scoring — a per-queue baseline plus per-ticket modifiers — so techs work the right ticket next.
category: Triage & Routing
tools: [search_tickets, list_boards, list_ticket_priorities, search_clients]
connectors: []
scope: global
flow: no
role: [Dispatcher, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Faster Resolution & Response]
---

# Queue Scoring Triage

**When to use:** "What order should we work the queue in?" / "what's next for the team?" — a dispatcher wants a scored morning triage list across boards, or a lead wants to sanity-check that high-priority work is actually surfacing first.

**Run it:** across all open tickets — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
Rank the open queue with an explainable two-layer score: every board carries a baseline
weight, each ticket earns modifiers on top. Output is a ranked list a dispatcher can act on —
with the math shown. This is read-only: rank and report, never change priorities, statuses,
or assignments.

1. Fetch open tickets, split per board to stay under result caps; say so if any board's search
   may have capped. A ranking over a truncated queue must say it's partial.

2. Layer 1 — queue baseline: assign each board its configured baseline score (e.g. security
   40, NOC 30, help desk 20, internal 5). Unconfigured boards get the default baseline and are
   called out.

3. Layer 2 — ticket modifiers, additive and bounded, e.g.: priority level (from the desk's
   priority mapping), age beyond target, approaching/breached SLA, VIP or strategic client
   (from client tier data where present), negative sentiment, and a penalty (not a boost) for
   waiting-on-client/vendor states.

4. Compute score = baseline + modifiers for every ticket. Ties break by oldest-first.

5. Output the ranked list: rank, ticket number, client, one-line summary, total score, and the
   breakdown (baseline + each modifier). Flag anomalies — a P1 ranking below page one, or a
   whole board starved.

Every score must be reproducible from the shown breakdown — no hidden judgment bumps. If you
adjust a rank for a reason outside the model, label it explicitly as an override suggestion.
Waiting-on-client/vendor tickets are de-ranked, not hidden. If scoring weights aren't
configured for this desk, use the documented defaults and say so; never silently invent weights
per run — rankings must be stable between runs.
```
