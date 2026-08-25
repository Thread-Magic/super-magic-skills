---
name: Pod-Based Dispatch
description: Route a ticket to the least-loaded technician in the client's assigned service pod: read the pod from company record, load-balance, assign, and note it.
category: Scheduling & Dispatch
tools: [search_clients, search_tickets, search_members, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Pod-Based Dispatch

**When to use:** The desk aligns each client to a dedicated service pod/team ("<client> is a <Team B> account") and wants new tickets auto-routed to the least-busy tech in that client's pod — a Flow that dispatches each ticket the moment it lands, or a dispatcher clearing an unassigned board.

**Run it:** on one ticket · across a board's unassigned intake · or as a Flow-run **agent** that dispatches every new ticket automatically.

## Prompt

```
Route each ticket to the least-loaded technician in the CLIENT'S assigned service pod, then take
the actions that move it forward. When you can assign, you also advance the status; when you
can't, change nothing and hand off with a clear reason.

1. Identify the client from the ticket and read the company record, including its notes and
   custom fields.

2. Determine the pod from that record — a labelled line in the notes or a company custom field,
   such as "Service Team: <Team A>". Use the desk's real pod names (<Team A>, <Team B>, <Team C>
   here are placeholders). If no pod is recorded, STOP: leave status and owner untouched and
   leave an internal note — "Unable to determine the service pod for <company>: no pod is set on
   the company record. Please assign manually and set the pod on the company." Never guess a pod.

3. Resolve the members configured for that pod. If the pod has no technicians, STOP, note that it
   is empty, and leave the ticket unassigned.

4. Count each pod technician's currently open assigned tickets, and pick the fewest. Break ties
   in order: the one idle longest, whose most recently updated ticket is the oldest; then
   alphabetically by first name.

5. Apply exclusions before committing — skip to the next-least-loaded if the pick is the
   requester, inactive, marked out or on PTO, or excluded by a client-specific routing rule.
   Never assign outside the client's pod, and never reassign a ticket that already has an owner:
   check first, and only proceed if it is unassigned.

6. Set the owner to the selected technician.

7. Advance the status only because the assignment succeeded: if the desk has an "Assigned" status
   for dispatched work, move the ticket to it; if not, leave status alone.

8. Leave an internal note — plain text, no markdown or emojis (PSA Note Discipline base skill):
   "Pod dispatch: assigned <tech> from <client>'s pod (<Team X>). Open assigned tickets at
   dispatch: <n>."

The pod is the boundary: never assign to a tech outside the client's pod, and never invent or
substitute pod members the company isn't aligned to. Advance status only when the assignment
actually succeeded — assign, then status; on failure leave status alone. Apply the Sweep Honesty
base skill to the load counts: if a search hits a result cap, say the load may be undercounted
rather than assuming. When you can't determine the pod or a safe pick, change nothing and hand
off — a wrong auto-assignment is worse than none.

As a Flow: work autonomously, take no input, ask no questions, and complete steps 1 to 8 on a
clean assignment. On any STOP condition — no pod, empty pod, all excluded, already owned — make
no writes except the single explanatory note and leave the ticket for a dispatcher; never force a
pick. Your entire reply is the note.
```
