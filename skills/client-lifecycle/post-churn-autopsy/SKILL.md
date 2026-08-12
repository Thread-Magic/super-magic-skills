---
name: Post-Churn Autopsy
description: After a client terminates — reconstruct the causes from ticket evidence, extract the lessons, and identify the early-warning signals we missed so the next departure is caught in time.
category: Client Lifecycle
tools: [search_tickets, search_clients]
connectors: []
scope: single
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Post-Churn Autopsy

**When to use:** "<client> churned — run the autopsy"; "what can we learn from losing <client>?"; or "which signals did we miss before <former client> left?"

**Run it:** on one churned client's full history — a manual blameless post-mortem, not a Flow.

## Prompt

```
The client is gone; the lessons don't have to be. Run a blameless post-mortem on the
relationship: what actually drove the departure, when it became visible in the data, and
what to instrument so the pattern is caught earlier next time.

1. Confirm the departed client (look it up) and establish the timeline: relationship start,
   termination notice date, final date. Review the full history, working backward from the
   end; state which portion the analysis fully covers if searches cap.

2. Reconstruct the cause chain from evidence:
   - The proximate trigger, if visible (a final incident, a renewal dispute, a stakeholder
     change).
   - The underlying conditions: chronic recurring issues without root-cause fixes, SLA
     erosion, declining sentiment arc, dropped commitments, relationship concentration in
     one departing contact.
   - External factors the tickets hint at (competitor mention, internal-IT hire, business
     downturn) — labeled hypothesis where inferred.
   Present as a dated narrative: what happened, in what order, one representative example per
   pattern.

3. Mark the point of no return as best the data shows — the moment after which no thread
   suggests the client was still persuadable — and what distinguished before from after.

4. Extract lessons, each phrased as a process change, not a regret ("recurring issues at
   this frequency need a forced RCA", "a single point of contact going quiet for 60 days
   should trigger AM outreach").

5. Build the missed-signals list: each early warning visible in the data with its date, how
   many months before termination it appeared, and the detection rule that would catch it
   (frequency threshold, sentiment drop, silence window). Where a rule maps onto Client Risk
   Scan or Sentiment Decline Watch signals, say so — the autopsy should feed the scanners.

6. Close with two or three recommended changes — monitoring rules, process fixes,
   account-coverage changes — each traceable to a lesson.

Guardrails: blameless and internal — the autopsy names process failures, never people; if an
individual's handling contributed, describe the missing guardrail or escalation path, and
performance evaluation goes to the manager. Evidence discipline: every cause claim cites
thread evidence (one representative example, plain language, no ticket IDs); external-factor
speculation is clearly labeled hypothesis. Do not rewrite history to a tidy single cause —
churn is usually plural; report the chain as the evidence shows it, including genuine
unknowns. The former client is still owed professionalism: no disparaging commentary, and
nothing here is ever shared externally or reused in marketing. Result-cap honesty on every
historical claim ("based on the final 18 months of history").
```
