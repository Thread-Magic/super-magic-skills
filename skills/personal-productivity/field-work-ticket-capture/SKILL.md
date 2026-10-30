---
name: Field Work Ticket Capture
description: Turn a technician's one-line description of work already done in the field into a complete ticket with client, contact, owner, status and a time entry, without opening the PSA.
category: Personal Productivity
tools: [search_clients, search_contacts, list_boards, list_ticket_statuses, create_ticket, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Faster Resolution & Response]
---

# Field Work Ticket Capture

**When to use:** You are on site and someone stops you in the hallway: "can you look at my printer?" Ten minutes later it is fixed and there is no ticket. You want to type "Fixed printer for Jane at Acme, 9:40 to 9:55" and have a ticket with the time on it before you forget.

**Run it:** on one ticket, by hand. Save it under a short name so it is quick to run from your phone. Set the default board and status once in the prompt.

## Prompt

```
Create a ticket from what I just told you, for work I am doing or already did.

Defaults (edit once): board <your service board>; status <your in-progress status>, or <your completed or review status> if I say it is done.

1. PARSE my message for: the client company, the contact, what was done or requested, the time (a range like "9:40 to 9:55" or a duration like "15 minutes"), and any status or priority I state.

2. RESOLVE. Find the company, then the contact at that company. Missing, ambiguous, or more than one plausible match for either: ask me before creating anything. Never invent or guess a client or contact.

3. CREATE the ticket on the default board with that company and contact, a short clear title, and a description of the work in plain text. Make me the owner and the assigned technician. Use the status I stated, else the default. Look up real board and status names first.

4. TIME. If I gave a range, log exactly that. If I gave only a duration, end it now and work back to the start. Log it to me, with my description as the note. No time given: log nothing and remind me.

5. CONFIRM in one short block: ticket number, company, contact, status, and time logged.

Never create a duplicate: if I already have an open ticket for the same contact and issue today, show it and ask whether to log the time there instead. Notes are plain text, no markdown or emojis.
```
