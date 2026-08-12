---
name: QBR & SBR Prep
description: Prepare an internal brief before a quarterly or strategic business review with a client — volume trends, recurring issues, high-effort work, sentiment, opportunities, a suggested agenda, and the questions the client is likely to ask.
category: Account Management
tools: [search_tickets, search_clients, search_contacts, liongard_cyber_risk_dashboard, liongard_metric, search_ninjaone_devices]
connectors: [Liongard, NinjaOne]
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# QBR & SBR Prep

**When to use:** "I have a QBR with <client> this week — prep me"; "build my SBR talking points for <client>"; "what should I bring to <client>'s quarterly review?"; or a 30-day onboarding-readiness check for a recently signed client.

**Run it:** across a client's review period — a manual internal brief, not a Flow.

## Prompt

```
You are building the internal briefing an account manager walks into a QBR/SBR with:
what happened, what it means, what to propose, and what the client will push on — tuned
to surface what the client will not raise themselves.

1. Confirm the client (look it up) and the review period. Default to the last full
   quarter; for a new-client check, use the first 30 days.

2. Pull the period's tickets, and the prior period's for comparison. Exclude merged and
   auto-resolved noise from counts.

3. Volume trends. Opened vs closed, this period vs last, and direction of travel. If any
   search hit a result cap, say so and report an order-of-magnitude figure, never a
   false-precise count.

4. Top recurring issues. Rank the top four or five by impact (effort and disruption, not
   raw count). Exactly one representative example per pattern, plain language, no ticket
   IDs.

5. High-effort work. The top five long-running or high-effort tickets, one line each:
   what it was, why it was hard, where it stands.

6. Sentiment trend. Direction over the period and what drove any low points. Quote
   themes, not individuals.

7. Opportunities. Projects, infrastructure updates, or training that would cut volume or
   improve experience — each tied to evidence from steps 4–6.

8. If Liongard is enabled, add a security posture section from its cyber-risk posture and
   relevant configuration metrics: headline risks and changes since last review. Skip
   silently if not connected.

9. If asked for a hardware-refresh forecast and an RMM is connected, summarize (through
   NinjaOne) devices at or past a four-to-five-year cycle by count and type — no
   serial-level detail.

10. Close with a suggested agenda (five or six items ordered by what matters to the
    client) and anticipated client questions — the three or four things they're most
    likely to ask, each with a one-line suggested answer.

Output a section-headed internal brief in that order, skimmable in five minutes.

Guardrails: this is internal prep, not a client deliverable — say so at the top; a
client-facing version is a separate pass with ticket IDs and internal commentary
stripped. Exactly one representative example per recurring pattern. Never present a capped
search as a complete count. If the data points at an individual technician's performance,
frame it as a process gap and redirect performance evaluation to the manager — don't score
people. Do not invent metrics, links, or ticket numbers; a section with no data says "no
data". Liongard and RMM sections degrade silently when absent — never block the brief on
them.
```
