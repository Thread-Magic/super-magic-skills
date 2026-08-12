---
name: Deep Recap
description: Build a comprehensive ticket recap beyond the default template — full message/note/time-entry history, related sibling tickets for the client, a timeline, and current blockers. The "give me a REAL recap, not the two-line summary" workflow.
category: Documentation
tools: [search_tickets, list_recap_templates, add_ticket_note, search_clients]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Deep Recap

**When to use:** "Recap this ticket properly" / "I'm taking over this ticket, catch me up on everything" — a long-running or escalated ticket where the default recap is too thin for a handoff, escalation, manager review, or client status call.

**Run it:** on one ticket · or as a Flow (triggered when a ticket is escalated).

## Prompt

```
Build a recap with the whole picture: everything on the ticket, related client
activity, a dated timeline, and an explicit statement of what's blocking progress now.
Start from the desk's own recap template so the output still looks like THEIR recap.

1. Pull the base format: use the desk's default recap template's sections as the
   skeleton, so the deep recap is a superset of what they already expect — not a
   foreign format.

2. Gather the full history on the target ticket: all messages (client and internal),
   internal notes, status changes, ownership changes, time entries. RESULT-CAP
   HONESTY: if any lookup is capped or truncated, say so in the recap ("history may be
   incomplete beyond <date>").

3. Find related sibling tickets: look up the same client (and same contact/device
   where identifiable) with overlapping symptoms or explicit references, recent first.
   Relate them by evidence (same error, explicit reference, same device) and state the
   evidence — never invent a relationship.

4. Build the recap, extending the template with:
   - Timeline — dated bullets of major events (reported, diagnosed, escalated,
     waiting periods with durations). Distinguish client-visible messages from
     internal notes — a handoff reader needs to know what the client has been told.
   - Work done — what was actually tried/changed, from notes and time entries, with
     who and roughly how long.
   - Current state & blockers — exactly what the ticket is waiting on right now, on
     whom, since when.
   - Related tickets — the sibling list from step 3.
   - Open questions — things the history doesn't answer, stated as questions rather
     than guesses.

5. Recap ONLY what the record shows. No inferred resolutions, no invented ticket
   numbers or links, no converting "tech planned to reboot the server" into "server
   was rebooted". Gaps go under Open questions.

6. Post it as an internal note — plain text, PSA-safe, sections as plain headers, no
   markdown tables or emojis. In attended mode, show it in chat first for review.

UNATTENDED (Flow on escalation): the entire reply is the posted note — skeleton
sections always present, "Open questions" instead of guesses, and no questions
addressed to a reader who isn't there.
```
