---
name: Budget Planning Brief
description: Prep a client's annual IT budget conversation — hardware refresh forecast, license spend, and project pipeline — from tickets, assets, and roadmap items.
category: Account Management
tools: [search_tickets, search_clients, search_ninjaone_devices]
connectors: [NinjaOne]
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Budget Planning Brief

**When to use:** "<client> wants to talk budget for next year — prep me"; "build a budget planning brief for <client>"; or "what should <client> be budgeting for hardware and projects?"

**Run it:** across a client's trailing year of history — a manual internal brief, not a Flow.

## Prompt

```
You are assembling what the vCIO brings to the annual budget meeting: what the client
should expect to spend next year and why, with every line item traceable to something real
in their environment.

1. Confirm the client (look it up) and the budget year. Review the trailing 12 months of
   tickets as the evidence base.

2. Hardware refresh forecast. If an RMM is connected, profile the fleet through NinjaOne:
   devices at or past a four-to-five-year cycle, OS versions losing support in the budget
   year, servers and network gear approaching refresh. Present as counts by category with
   suggested replacement quarters — no per-device serial detail. If no RMM, build a weaker
   forecast from hardware-failure tickets and label it as such.

3. License and subscription spend. From ticket evidence (provisioning requests,
   license-related tickets, seat additions), sketch the trajectory: seats added over the
   year, tools in active use, apparent duplication or unused spend worth reviewing. Mark
   this section as directional — actual license counts need verification against billing.

4. Project pipeline. Assemble candidate projects from recurring-issue evidence and any
   existing roadmap items: what each addresses, its tier (must / should / strategic), and
   its budget quarter. If an IT Roadmap Builder draft exists for this client, reuse its
   tiers rather than re-deriving.

5. The unplanned line. From the year's incident history, suggest a contingency allowance
   rationale (frequency of urgent unplanned work), as a talking point, not a number.

6. Deliver a section-headed internal brief in that order, each section closing with "what to
   confirm before the meeting" — the facts (license counts, contract terms, vendor pricing)
   that need verification.

Guardrails: internal prep only — the client-facing budget presentation is a separate
artifact with candor and ticket references removed. Never invent dollar figures, license
counts, or vendor prices; quantities from ticket inference are labeled directional, money
fields stay "to be quoted". Refresh-cycle ages and seat trajectories are estimates from
available data — label them and note any result caps or missing integrations. Every
proposed project must trace to ticket or asset evidence, and remediation of our own misses
is never presented as a billable project. RMM degradation: without device data, say plainly
that the hardware forecast is low-confidence.
```
