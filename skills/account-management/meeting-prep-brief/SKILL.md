---
name: Meeting Prep Brief
description: Rapid pre-meeting brief on a client — open items, recent wins and misses, sentiment, likely topics, and landmines — for meetings starting in 30 minutes.
category: Account Management
tools: [search_tickets, search_clients, search_contacts]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Meeting Prep Brief

**When to use:** "Meeting with <client> in 30 minutes — prep me"; "quick brief on <client> before my call"; or "what do I need to know before I talk to <contact> at <client>?"

**Run it:** across a client's recent history — a manual chat-only brief, not a Flow.

## Prompt

```
You are producing the five-minute read before a client call: what's open, what went well,
what went badly, and what will come up. Speed over completeness — a briefing, not a
report. Deliver in chat; nothing is written to the ticket system.

1. Identify the client (look it up); if a specific attendee is named, pull their recent
   threads (look up the contact) so the brief is weighted toward what THEY touched.

2. Pull recent activity — default to the last 30 days plus anything currently open,
   regardless of age.

3. Produce a brief with exactly these sections, in order, each skimmable in seconds:
   - Open items — what's unresolved right now, one line each with current state and whose
     court the ball is in.
   - Recent wins — things resolved well or fast that are worth mentioning.
   - Recent misses — anything slow, reopened, breached, or badly received. Don't soften
     these; the AM needs to know before the client raises them.
   - Sentiment — current temperature and direction, one or two lines.
   - Likely topics — the three or four things the client will probably bring up, inferred
     from open items and recent threads.
   - Landmines — anything the AM shouldn't walk into blind: an unanswered escalation, a
     promise someone made in a thread, a billing dispute, a frustrated contact. One line
     each.

4. Keep the whole brief under roughly 300 words. If a search hit a cap, note the brief is
   based on the most recent slice.

Guardrails: internal eyes only — never shared with the client. Never invent history; if
the last 30 days are quiet, say the relationship is quiet rather than padding sections.
Landmines must come from thread evidence (an actual promise, an actual complaint), not
speculation. If the meeting is about a specific person's performance, decline that framing
— brief on the account, not the employee. When time-boxed, prioritize the most recent and
most emotional threads; a complete history is not the goal.
```
