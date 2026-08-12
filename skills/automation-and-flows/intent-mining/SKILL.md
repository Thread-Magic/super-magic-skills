---
name: Intent Mining
description: Analyze recent tickets to find top customer-facing intents worth building, ranked by volume and automatability, with draft trigger phrases for each pick.
category: Automation & Flows
tools: [search_tickets, list_intents, list_boards, get_intent]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Intent Mining

**When to use:** "Analyze the last 30 days and tell me what intents to build" / "what are our most common requests Magic could deflect?" / a partner wants a data-backed intent roadmap to grow zero-touch resolution.

**Run it:** across all tickets in the window — manually on demand (an analysis pass has no ticket event for a Flow to trigger on).

## Prompt

```
Mine a window of real tickets for repeated end-user requests that could become customer-
facing intents. This is READ-ONLY: never build an intent here — mining and building are
separate confirmations.

1. Confirm the analysis window (default: last 30 days) and which boards to include.
   Exclude alert/monitoring boards — machine-generated tickets are not intents.

2. List the existing intents FIRST and note every one and its trigger phrases.
   Anything already covered is excluded from recommendations, not re-proposed — list it
   under "already covered" instead.

3. Search tickets per board and per signal (password reset, new user, access request,
   printer, VPN, license…) rather than one giant query. If a search hits its result cap,
   say so and report that count as "at least N", never as exact — capped counts are
   floors, not totals.

4. Cluster tickets into candidate intents by the request the end user actually made, not
   by internal category.

5. Score each candidate: volume (tickets in window) x automatability (deterministic answer
   or scripted info-gathering = high; judgment, hands-on, or approval-heavy = low). Rank
   by the product.

6. For each top candidate, draft 8–12 varied trigger phrases mirroring how end users
   actually wrote them. Sanitize every example: use <user>, <client>, <application>
   placeholders — no names, clients, or systems specific to one tenant.

7. Do NOT propose intents for security-sensitive requests (password disclosure, MFA
   bypass) as self-service answers — flag them as identity-verification workflows instead.

Output a ranked table: candidate intent, ticket count (with cap caveats), automatability
rating and why, draft trigger phrases, and what the intent should collect or answer. Close
by offering to hand the top pick to the Intent Builder skill.
```
