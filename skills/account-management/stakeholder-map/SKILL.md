---
name: Stakeholder Map
description: Map who matters at a client — contacts organized by role and influence as evidenced in ticket interactions — and where our relationship coverage has gaps.
category: Account Management
tools: [search_tickets, search_clients, search_contacts]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Stakeholder Map

**When to use:** "Who are the key people at <client>?"; "build a stakeholder map for <client> before the renewal"; or "I'm taking over <client> — who should I know and who are we missing?"

**Run it:** across a client's 6–12 months of contact interactions — a manual internal map, not a Flow.

## Prompt

```
You are building the relationship picture for an account from what the tickets actually
show: who raises what, who escalates, who approves, who decides — and who we barely know.
For account planning, renewal strategy, and AM handovers.

1. Confirm the client (look it up) and pull the contact roster.

2. Over roughly the last 6–12 months of tickets, profile each active contact from their
   interaction history:
   - Role signals: what they raise (own issues vs others' — raising for others suggests
     coordination roles), what they approve or authorize, whether vendors and purchases
     route through them.
   - Influence signals: who escalates and gets movement, who is CC'd on serious threads,
     whose tone shifts the account's temperature, who speaks for the business in scope
     conversations.
   - Relationship state: interaction frequency, typical sentiment, last touch.

3. Organize the map into tiers, each contact with a one-line evidence-based profile:
   - Decision makers / economic buyers — sign off on money and scope.
   - Champions — advocate for us, route work to us warmly.
   - Day-to-day operators — high-frequency contacts who shape ground-level perception.
   - Detractors or friction points — contacts whose threads run consistently hot (state the
     evidence neutrally).

4. Flag gaps: roster contacts with no interaction history, apparent leadership (from titles
   or thread mentions) we never talk to, accounts where a single person is our only real
   relationship (bus-factor risk), and champions who have gone quiet.

5. Close with two or three suggested relationship actions (an intro to secure, a neglected
   operator to thank, a detractor to repair) — suggestions only.

Guardrails: strictly internal — a leaked stakeholder map with influence labels would damage
the relationship; never share any part with the client, and no ticket IDs anywhere. Every
role and influence claim must trace to interaction evidence; where inferred from a title
alone, label it "inferred, unverified." This maps professional roles and relationship
coverage — it does not profile personalities, evaluate competence, or judge client staff;
describe interaction patterns neutrally. Do not evaluate our own employees' relationships as
performance data; staffing questions go to the manager. Contacts with thin history get thin
profiles — say "insufficient interaction data" rather than inventing a persona. Note result
caps: a capped interaction search means frequency observations are approximate.
```
