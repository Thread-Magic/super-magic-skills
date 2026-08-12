---
name: Scope Pushback
description: Draft the reply when a client requests something outside their agreement — a helpful no showing the path to yes (quote or agreement change) with AM loop.
category: Communication
tools: [search_tickets, search_members, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician, CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Scope Pushback

**When to use:** "Client is asking for <project work / new hardware / unsupported system> — it's out of scope, draft the reply" / "how do I say no to this nicely?"

**Run it:** on one ticket.

## Prompt

```
Draft the out-of-scope response that protects the agreement without souring the relationship:
we can't do this under your current plan, here's exactly how we can.

1. Read the ticket and confirm with me that the request is genuinely out of scope. You do NOT
   adjudicate contracts — scope determination is my (or the AM's) call. If I'm unsure, your
   first output is a recommendation to check with the account manager, not a client draft.

2. Draft:
   - Acknowledge the request positively — it's usually a good idea, say so when true.
   - The no, framed as a boundary of the current agreement, not a refusal to help: "this
     falls outside what's covered under your current agreement."
   - The path to yes: the concrete route — "we'd handle this as a quoted project" or "this
     could be added to your agreement" — and the immediate next step: "<account manager> will
     reach out to walk through options."
   - End with motion, never a wall.

3. Identify the account manager for this client (from the member list or client record) and
   prepare the internal handoff: offer a plain-text internal note summarizing the request, the
   pushback sent, and that the AM owes the client an outreach.

4. Show me the client draft for review, and the AM handoff note separately labeled. Sending
   and the AM handoff are human-confirmed.

Never assert specific contract terms, coverage details, or prices in the client email — you
haven't read the agreement. "Outside your current agreement" per my determination is the
ceiling. Never say yes-with-conditions that commits the desk to unquoted work ("we can probably
squeeze this in"). Never blame the client for asking. The AM loop-in is mandatory whenever the
path to yes is offered — if no AM is identifiable, flag that to me explicitly.
```
