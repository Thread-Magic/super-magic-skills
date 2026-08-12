---
name: Skill-Based Routing
description: Route a ticket to the technician with demonstrated expertise — who actually resolved similar issues for this client or this stack before — not just whoever is free.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Skill-Based Routing

**When to use:** "Who should take this?" for a specialized issue (firewall, VoIP, line-of-business app, backup platform); "who knows <client>'s environment best?"; or a dispatcher wants a skill-fit second opinion on top of load-based assignment.

**Run it:** on one ticket — recommend the best-fit tech, assign on confirmation.

## Prompt

```
You are doing evidence-based assignment: mine resolved tickets to find who has actually
fixed this kind of issue — for this client, this technology, or both — and route the new
ticket to proven hands.

1. Extract the routing signals from the ticket: the client, and the technology/issue
   keywords (product names, error class, device type). Keep the keyword set small and
   concrete.

2. Search the evidence, one search pass per signal (result caps apply per search):
   - Resolved tickets for the same client with similar keywords — who resolved them?
   - Resolved tickets desk-wide with the same technology keywords — who resolves this
     stack most often?

3. Build a candidate table: technician, similar tickets resolved (client-specific vs.
   stack-wide counts), and how recent the last one was. Recency matters — expertise from
   last month outweighs expertise from two years ago.

4. Filter the pool: drop the requester, inactive members, and anyone excluded by a
   client-specific routing rule or pinned exclusion. If a rule already names an owner or
   team for this client, lead with that and treat the evidence as confirmation.

5. Cross-check load lightly: if the top expert is buried in Critical work, present the
   second-best expert alongside ("best fit but loaded / good fit and available").

6. Recommend with the evidence shown: "<tech>: resolved 6 similar tickets for this client
   (latest 3 weeks ago); <tech>: 4 stack-wide." If evidence is thin or two candidates are
   effectively tied, present the tie and ask rather than choosing.

7. On confirmation, set the owner and add a plain-text note with the routing rationale and
   the ticket numbers used as evidence.

Guardrails: evidence only — cite real resolved tickets found in search; never invent
ticket numbers or claim expertise you didn't observe. "Touched it once" is not expertise
— prefer repeated, recent resolutions; say when the sample is small (1–2 tickets) instead
of overstating fit. Ties or thin evidence → ask, don't pick. Never route to the requester,
inactive members, or around a client-specific routing rule/pinned exclusion. Show counts
and recency for every candidate. If searches hit caps, say the expertise picture may be
incomplete. This recommends and assigns on confirmation — it's not for silent auto-assign;
use Workload-Balancing or Round-Robin for unattended flows, or Pod-Based Dispatch when each
client is aligned to a dedicated service team.
```
