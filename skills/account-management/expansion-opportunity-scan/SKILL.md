---
name: Expansion Opportunity Scan
description: Mine a client's ticket history for expansion signals — recurring issues that justify a project or upsell, and training gaps that justify a service offering.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Expansion Opportunity Scan

**When to use:** "Any upsell opportunities at <client>?"; "what projects should we be proposing to <client> based on their tickets?"; or "scan my accounts for expansion candidates."

**Run it:** across one client's history or the whole portfolio — a manual internal scan, not a Flow.

## Prompt

```
You are finding the revenue hiding in the ticket queue: patterns a project would
eliminate, and user struggles a training or managed-service offering would address. The
output is a qualified internal opportunity list, not a pitch.

1. Confirm scope (one client or the portfolio) and window (look up the client). Default to
   the last 6 months.

2. Hunt two distinct signal families in the tickets — separate searches per family, per
   client:
   - Recurring issues → project/upsell: the same failure mode repeating (aging hardware,
     capacity limits, a flaky line-of-business app, an unmanaged system generating
     incidents). Each recurrence cluster is a candidate for a project, hardware refresh,
     license upgrade, or scope expansion.
   - Training gaps → service opportunity: clusters of how-do-I tickets, repeated user error
     on the same tool, or one team generating disproportionate basic requests. Candidates
     for training engagements or an expanded support tier.

3. For each opportunity, produce a qualified entry: the pattern with exactly one
   representative example (plain language, no ticket IDs); rough frequency and effort cost
   to the desk ("roughly monthly, ~2 hours each" — mark as estimate); the proposed
   offering, one line; why the client would care, in their business terms.

4. Rank opportunities by evidence strength times likely deal size, strongest first.

5. End with a note on anything that looks like an opportunity but is really a
   service-quality problem we should fix for free — do not disguise remediation as upsell.

Guardrails: internal only — this informs a proposal, it isn't client-facing. Every
opportunity must trace to ticket evidence; no generic MSP upsell boilerplate without
threads to back it. Never flag on volume alone — the pattern, not the count, makes the
case. Be honest about the free-fix line: if the recurring issue stems from something we
misconfigured or under-delivered, say so instead of proposing to charge for the cure.
Frequency and effort figures are estimates from ticket data — label them, and note any
result caps hit.
```
