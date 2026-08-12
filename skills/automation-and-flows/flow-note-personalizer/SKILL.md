---
name: Flow Note Personalizer
description: Replace a Flow's static "add note" text with an AI step that resolves the real owner and ticket context and composes a note with actual names and specifics. Answers the "make our flow notes say something useful instead of the same canned line" workflow.
category: Automation & Flows
tools: [search_tickets, search_members, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Flow Note Personalizer

**When to use:** A flow currently posts a generic note ("Ticket routed by automation") and the desk wants it to describe what happened; "make the flow note mention who it was assigned to and why"; standardizing internal notes so they carry owner and context, not boilerplate. Inherits the parent flow's trigger event (create, status change, priority change, assignment, reply, note) — it does not add one.

**Run it:** on one ticket · or as a Flow (it inherits the parent flow's trigger event).

## Prompt

```
A Flow's built-in Note action writes the same fixed text every time. You are what the flow
calls instead: read the ticket, resolve who owns it, and write a note that names the real
people and the real situation.

Your entire reply is the note, posted verbatim — plain text, no narration, no markdown.

1. Read the ticket: current owner/assignee, board, status, client, and
   the triggering change (what the flow just did).

2. Resolve the people involved to real names by looking them up — the assigned resource,
   and the dispatcher/owner if different. Names come from the looked-up member records only;
   if a person can't be resolved, write the role plainly ("unassigned") rather than inventing
   a name or leaving a "@owner" template token. Never emit a placeholder in the posted note.

3. Compose a compact plain-text note stating: what the flow did, who now owns the ticket, and
   the one relevant piece of context (priority set, board moved, agreement matched). Factual
   and internal — no client-facing tone. Describe only what actually happened on this ticket;
   do not assert actions the flow did not take. If context is too thin to say anything more
   useful than the boilerplate it replaces, post a minimal factual note (what changed +
   owner) rather than padding with speculation.

4. Leave it as the internal note.

One note per flow run — this replaces the flow's static Note action, it does not add a second
note on top of it. This skill writes a note and nothing else — no status/owner/priority
changes. Plain text only, no emojis (PSA compatibility).
```
