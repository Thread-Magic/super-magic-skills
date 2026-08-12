---
name: Monthly Security Report
description: Produce a client's monthly security digest: incident and alert counts, notable events, posture trend, and recommendations for client or internal review.
category: Security
tools: [search_tickets, liongard_cyber_risk_dashboard, add_ticket_note]
connectors: [Liongard]
scope: global
flow: no
role: [Security & Compliance Owner, CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion), Risk & Compliance]
---

# Monthly Security Report

**When to use:** "Build <client>'s monthly security report"; a vCIO/CSM needs the security section for a monthly or quarterly review; or a recurring per-client security digest cadence.

**Run it:** across a client's security tickets for the reporting window (a monthly digest).

## Prompt

```
One client, one month, one digest: what fired, what mattered, whether posture is trending
the right way, and what to do next — with counts the desk can defend. Work it in order:

1. Fix the reporting window (the calendar month unless told otherwise) and pull the client's
   security tickets, split per type per board — phishing reports, sign-in/identity alerts,
   EDR detections, credential exposures, vendor-fraud reports, requests (quarantine
   releases, allowlists). If any search hits its result cap, report that figure as "at
   least N" — never present a capped count as exact.
2. Count and compare: this month's counts by type against the prior month's. Note the
   biggest movers and — where the tickets say so — why (a phishing campaign, a new alert
   source onboarded, tuning that landed).
3. Notable events: the month's P1/P2 security incidents, each as one line — what happened,
   how fast it was contained, outcome. Facts from the tickets with timestamps;
   defensive-writing-standard wording.
4. Posture trend: read the cyber risk dashboard deltas in Liongard where available (score
   movement, MFA coverage change, open detections). Liongard absent → the trend section is
   ticket-derived only and labeled as such.
5. Recommendations: two or three, each tied explicitly to this month's data ("phishing
   reports doubled → schedule awareness refresh"; "the same benign alert consumed N tickets
   → tuning recommendation attached" via security-noise-tuning). Recommendations, never
   actions reported as done.
6. Produce the right edition: the internal edition may reference tooling detail and open
   investigations; the client edition strips other-client references, individual staff
   names, and anything under active investigation that management hasn't cleared for
   disclosure. Leave it as a plain-text note or deliver as draft text for the CSM.

Guardrails — always:
- Result-cap honesty is the headline rule — a security report with silently truncated counts
  is worse than no report.
- Client edition never names individual employees in a negative light ("3 users clicked" not
  "<user> clicked"), never references other clients, and follows the
  defensive-writing-standard.
- Never disclose an open investigation's specifics in the client edition without management
  sign-off.
- Counts and events come from tickets — no estimated or recalled figures; if a data source
  was unavailable for part of the month, say so.
- Trend claims require both months measured the same way; if the search method changed, note
  the break in comparability.
```
