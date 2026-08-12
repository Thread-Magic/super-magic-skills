---
name: Health Score Reconciliation
description: Reconcile a client's own health or satisfaction scores against our ticket reality — where their perception and our data agree, and where they diverge and why.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Health Score Reconciliation

**When to use:** "<client> rated us 6/10 — does our data explain that?"; "their CSAT looks great but the account feels rocky — reconcile"; or "compare <client>'s survey feedback with what our tickets show."

**Run it:** across a client's review-period tickets versus their supplied scores — a manual readout, not a Flow.

## Prompt

```
You are lining up the client's own scores against our ticket reality — where "7/10" and
the queue agree, and where they diverge and why. You compare two sources; you do not
invent the client's side.

1. Take the client-supplied scores from the AM (paste, summary, or verbal rating). If none
   are provided, ask for them — this skill compares two sources.

2. Confirm the client (look it up) and match the review window to the period the scores
   cover.

3. Build the data-side picture over the same window: volume and resolution trends, SLA
   performance, sentiment trend, recurring issues, notable incidents. Note result caps.

4. Produce a reconciliation table: for each dimension the client scored (or each theme in
   their feedback), state their perception, what the ticket data shows, and a verdict —
   aligned, client rosier than data, or client harsher than data.

5. For every divergence, offer the most plausible explanations grounded in evidence:
   - Client harsher: one memorable bad incident dominating perception; a frustrated key
     stakeholder whose threads skew hot; slow-feeling responses on low-priority items;
     issues raised outside the ticket system we never saw.
   - Client rosier: pain absorbed by their internal staff before reaching us; recent
     goodwill masking chronic issues; the scorer not being the person who feels the
     friction.
   Cite one representative example per explanation, plain language, no ticket IDs.

6. Close with implications: which perception gaps to address in conversation, which data
   gaps suggest we're not seeing the whole relationship, and one or two concrete
   follow-ups.

7. Deliver as a section-headed internal readout: scores as given, data picture,
   reconciliation table, divergence analysis, implications.

Guardrails: internal only — especially the "client is wrong" parts never go to the client
as written. Treat the client's perception as valid data about the relationship, not an
error to correct; the deliverable explains divergence, it does not adjudicate who is right.
Divergence explanations must be grounded in thread evidence and labeled as hypotheses where
inferential. If a divergence traces to a specific technician's interactions, describe the
interaction pattern as a process matter; performance evaluation goes to the manager.
Result-cap honesty: if the data side rests on a capped sample, the verdicts are provisional
and must say so. Never fabricate or estimate client scores.
```
