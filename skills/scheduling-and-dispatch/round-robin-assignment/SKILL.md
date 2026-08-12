---
name: Round-Robin Assignment
description: Distribute incoming tickets fairly across a named technician roster in rotation, honoring exclusion rules — runnable unattended inside a Flow.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Round-Robin Assignment

**When to use:** The desk assigns a board's intake by rotation ("round-robin the helpdesk board across <roster>"); a Flow fires on ticket creation for a board that uses rotation instead of load scoring; or a dispatcher wants to spread a batch evenly across a named group.

**Run it:** on one ticket · across a batch you point me at · or as a Flow that assigns each new ticket by rotation.

## Prompt

```
You are running fair rotation: each new ticket goes to the next technician in the roster,
so distribution is even by design rather than by whoever happens to look free.

1. Establish the roster. Use the explicit roster the desk configured for this skill (a
   named list of members); confirm each one resolves to a real member. If no roster is
   configured, ask for one — do not invent a roster from "everyone on the board".

2. Determine rotation position: find the most recent ticket on this board assigned by this
   rotation (newest assigned first, or the rotation marker in its note) and pick the next
   roster member after that assignee, wrapping at the end.

3. Apply exclusions before assigning, and skip to the next in rotation if the candidate
   is: the ticket's requester, inactive, marked out/on PTO, or excluded by a
   client-specific routing rule or pinned exclusion. A skipped tech keeps their place —
   they get the next eligible ticket.

4. If every roster member is excluded, stop: report (or note, unattended) that no eligible
   candidate exists and leave the ticket unassigned.

5. Set the owner. Then, because the assignment succeeded, advance the status: if the desk
   uses an "Assigned" status for dispatched work, move the ticket to it; if no such status
   exists, leave status alone. Never change priority.

6. Record a plain-text note marking the rotation ("Round-robin: assigned <tech> (position 3
   of 5; skipped <tech>, PTO).") — this note is also the rotation state for the next run.

7. For batch mode, continue the rotation across the batch (ticket 1 → next tech, ticket 2
   → the one after) and output the full distribution table for confirmation before
   applying.

Running as an agent in a Flow (unattended): your entire reply is posted as the note — plain
text, no narration, no questions. Deterministic behavior only: next eligible member in
configured roster order, skips noted; no judgment calls about "fit". On assignment, advance
status and note it. Already assigned, empty roster, or all excluded → make no writes except
(all-excluded case) a single note "Round-robin: no eligible roster member (reasons). Left
unassigned." Touch only the assignee, the status, and the note.
If the last-rotation lookup is ambiguous (no marker, or capped search), start from the top
of the roster and say so in the note.

Guardrails: the roster is explicit — never substitute or add members the desk didn't name.
Fairness is auditable: every note states position and skips; skipped techs stay next in
line. Never assign to the requester, inactive members, or around a routing rule/pinned
exclusion. Client-specific routing rules beat the rotation — follow the rule, note it, and
don't advance the rotation. Never reassign a ticket that already has an owner. If clients are
aligned to dedicated service pods rather than one board-wide rotation, use Pod-Based Dispatch
to rotate within the client's team instead.
```
