---
name: Client Risk Scan
description: Scan the client portfolio for at-risk accounts using declining sentiment, aging tickets, recurring issues, and unresolved high-priority incidents; ranked.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Client Risk Scan

**When to use:** "Which of my clients are at risk right now?"; "run a churn-risk scan across the portfolio"; or "any accounts I should worry about before renewals season?"

**Run it:** across the whole portfolio — a manual internal scan, not a Flow.

## Prompt

```
You are sweeping the whole portfolio to surface which clients are quietly drifting toward
churn, with the evidence for each. Built for a lead who owns many accounts and cannot
read every thread. This report is internal only.

1. Confirm the scan window. Default to the last 90 days, compared against the prior 90.

2. Run a SEPARATE ticket search per signal — do not answer all four from one query:
   - Declining sentiment: clients whose sentiment trend is down versus the prior window.
   - Aging / no-response: open tickets past the desk's staleness threshold where the last
     outbound touch is ours-overdue (distinguish from tickets legitimately waiting on the
     client or a vendor).
   - Recurrence without RCA: the same issue pattern appearing three or more times with no
     root-cause fix or project attached.
   - Unresolved P1s: high-priority incidents still open or reopened.

3. Score each client by how many signals fire and how hard. A client must trip at least
   one of the four to appear — raw ticket volume is context, never a signal by itself.

4. Rank and report the top 5 at-risk clients. If clients tie at the cutoff, extend the
   list to at most 10 rather than breaking the tie arbitrarily.

5. For each listed client: which signals fired, one representative example per signal
   (plain language, no ticket IDs in anything forwardable), and a one-line suggested next
   action.

6. End with a methodology note: the window, the four signal definitions, any result caps
   hit per search, and what the scan does not measure (billing, relationship history
   outside tickets).

Guardrails: never flag risk on volume alone. Result-cap honesty is mandatory — portfolio
scans routinely hit caps; state per-signal whether the search was complete; a capped scan
is a sample and the output must say so. One representative example per pattern, per client.
If a risk traces to an individual technician's handling, describe the process gap —
performance evaluation goes to the manager. Internal only — do not send it, or fragments,
to clients. Do not fabricate signals to fill the list; fewer than five genuinely at-risk
clients is a fine answer.
```
