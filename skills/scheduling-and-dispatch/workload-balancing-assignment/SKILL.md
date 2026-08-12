---
name: Workload-Balancing Assignment
description: Assign a ticket to the tech with the best availability score — base capacity minus open tickets minus scheduled blocks — with math shown, runs in Flows.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, list_ticket_priorities, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Workload-Balancing Assignment

**When to use:** "Assign this to whoever is least busy" for a single ticket or small batch; a Flow fires on ticket creation and the desk wants load-balanced auto-assignment; or a dispatcher wants assignment recommendations they can approve in one glance.

**Run it:** on one ticket · across a small batch · or as a Flow that load-balances each new ticket.

## Prompt

```
You are scoring every eligible technician's availability with an explicit formula and
assigning the ticket to the highest scorer — with scores shown, so the choice is
auditable rather than a black box.

1. Build the candidate pool: the technicians on the relevant board/team. Remove the
   ticket's requester (if a member), inactive members, anyone on a stated exclusion list,
   and anyone excluded by a client-specific routing rule for this client.

2. For each candidate, compute an availability score:
   score = base capacity − open tickets (priority-weighted) − scheduled blocks today
   - Base capacity: the desk's stated per-tech capacity, or a uniform default if none.
   - Priority weighting: Critical/High heavier than Low (e.g. Critical ×3, High ×2,
     Medium/Low ×1) — complexity matters, not just count.
   - Scheduled blocks: today's schedule entries reduce availability even when open-ticket
     count is low.

3. Rank candidates. If the top two are effectively tied, do not pick arbitrarily: in
   attended mode ask the dispatcher; in unattended mode apply the deterministic tie-break
   (alphabetical by member id) only if the desk opted in, otherwise leave unassigned.

4. Set the owner. Then, because the assignment succeeded, advance the status: if the desk
   uses an "Assigned" status for dispatched work, move the ticket to it; if no such status
   exists, leave status alone. Never change priority.

5. Record the rationale in a plain-text note: the winning score, the runner-up, and the
   formula inputs ("Assigned <tech>: score 7 (base 10, 2 open weighted 2, 1 scheduled
   block). Runner-up <tech>: 5.").

6. In attended mode, output the full score table before assigning and confirm.

Running as an agent in a Flow (unattended): your entire reply is posted as the note — plain
text, no narration, no questions. Assign only on a single clear top scorer after exclusions,
then advance status and note it. Tie or empty pool → no assignment, no status change, and
post "Workload balancer: no unambiguous candidate (reason). Left unassigned for dispatcher."
Never reassign a ticket that already has an owner (do nothing, post nothing).

Guardrails: show the math — every assignment carries its score breakdown. Never assign to
the requester, an inactive member, or anyone excluded by a routing rule or pinned
exclusion. Client-specific routing rules beat the score — follow and say so. If searches
hit caps, scores may undercount load — flag it and prefer asking over assigning. When in
doubt (empty pool, unresolvable tie, missing priority data), do nothing and leave the
ticket unassigned. If clients are aligned to dedicated service pods, use Pod-Based Dispatch
to scope this formula to the client's team instead of the whole board.
```
