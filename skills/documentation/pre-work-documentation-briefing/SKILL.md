---
name: Pre-Work Documentation Briefing
description: Before an engineer starts a ticket, pull the client's own IT Glue or Hudu documentation for the symptoms, drop archived and draft articles, flag conflicts and gaps, and post a short briefing.
category: Documentation
tools: [search_tickets, search_clients, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Staff Enablement]
---

# Pre-Work Documentation Briefing

**When to use:** Technicians skip the documentation platform because searching it is slow, then solve problems that already have an SOP. You want every new ticket to arrive with the client's relevant documents, a confidence read, and a clear note when nothing exists.

**Run it:** on one ticket · or as a Flow (when a ticket is created on your service boards).

## Prompt

```
Give the technician a documentation briefing for this ticket before they start.

1. Read the ticket with its full thread: what was reported, the affected system or app, and any error text word for word. Identify the client company; if the ticket is on a catchall or shared board, look for the client named in the title or description. No client identified: post "Documentation briefing skipped: client could not be identified." and stop. If the ticket is closed, stop with no note.

2. Search the client's documentation (IT Glue, or Hudu if that is what this desk uses) scoped to that client, using keywords from the symptoms, the system and the error text. If a scoped search returns nothing, retry once without the client scope, but keep only results clearly marked as shared across the MSP or global. Never include another client's documents.

3. Filter hard:
- Drop anything archived, retired, draft or under review. Do not list them even as a maybe.
- Age alone does not disqualify an article; only its status does.
- Keep only articles that address the reported symptoms, not just the same general topic.
- If two current articles contradict each other, say so; never silently pick one.
- Keep at most 5.

4. Post one internal note, plain text, no markdown or emojis:
DOCUMENTATION BRIEFING
Ticket: <1 to 2 sentences, including any verbatim error>
Relevant documentation:
- <article name> <link> : <one line on what it says to do>
Conflict: <article A> and <article B> disagree on <point>. Review both. (only if found)
Match confidence: <Strong, Partial or None>
Documentation gap: No current documentation covers these symptoms. Flag for a KB update after resolution. (only if none)
Suggested starting point: <one line, e.g. confirm X before following article Y>
Internal use only.

Rules: only list documents the search actually returned, with their real links; never invent a title, URL or step. No pricing, contract or SLA details. Never reply to the client. Never change the status, priority or owner. If the documentation connector is not available, post "Documentation briefing skipped: no documentation connector enabled." and stop.

As a Flow: your entire reply is the note.
```
