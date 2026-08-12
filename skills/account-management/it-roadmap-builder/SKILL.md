---
name: IT Roadmap Builder
description: Draft a client IT roadmap from their ticket history plus asset and posture data — what to fix, upgrade, and invest in, organized into investment tiers.
category: Account Management
tools: [search_tickets, search_clients, search_ninjaone_devices, list_ninjaone_alerts, liongard_cyber_risk_dashboard, liongard_metric]
connectors: [NinjaOne, Liongard]
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# IT Roadmap Builder

**When to use:** "Draft an IT roadmap for <client>"; "build <client>'s 12-month technology plan from what we know"; or "what should <client> invest in next year?"

**Run it:** across a client's year of history plus current environment state — a manual internal draft, not a Flow.

## Prompt

```
You are turning a year of tickets and the current state of the environment into a
structured roadmap draft a vCIO can refine and present: prioritized initiatives with the
evidence behind each, grouped into investment tiers.

1. Confirm the client (look it up) and the planning horizon. Default to a 12-month roadmap
   built from the last 12 months of history.

2. Ticket evidence. Extract the pain from the tickets: recurring failure modes, chronic
   systems, capacity complaints, security incidents, high-effort categories. One
   representative example per pattern.

3. Asset evidence (if an RMM is connected). Profile the fleet through NinjaOne — device age
   distribution, OS versions approaching end of support, chronic alerting devices, servers
   approaching refresh age. Skip silently if not connected and note the roadmap is
   ticket-evidence-only.

4. Posture evidence (if Liongard is connected). Pull Liongard's cyber-risk posture and
   relevant configuration metrics for security and configuration gaps worth roadmap items.
   Skip silently if absent.

5. Synthesize into initiatives: each with a name, what it addresses (tied to specific
   evidence from steps 2–4), rough scope, and the consequence of not doing it.

6. Organize into investment tiers:
   - Tier 1 — Must do: risk and stability items; things failing or exposed now.
   - Tier 2 — Should do: approaching-end-of-life refreshes, capacity, items that cut
     recurring ticket load.
   - Tier 3 — Strategic: improvements that enable the client's business goals rather than
     fix problems.

7. Within each tier, order by evidence strength, and suggest rough sequencing across
   quarters.

8. Deliver as a section-headed internal draft. Flag every item that needs pricing, vendor
   quotes, or client business context before it can go in front of the client.

Guardrails: this is a draft for the vCIO, not a client deliverable — client-facing
roadmaps get rewritten with ticket IDs, candor, and unpriced placeholders removed. Every
initiative must trace to evidence — ticket patterns, asset data, or posture findings; no
generic best-practice filler. No invented prices, timelines, or vendor commitments — cost
fields stay "to be scoped". Label device-age and effort figures as estimates; note any
result caps hit and which sections rest on partial data. RMM and Liongard sections degrade
silently when absent — the ticket-history roadmap still ships, with a note about what it
could not see.
```
