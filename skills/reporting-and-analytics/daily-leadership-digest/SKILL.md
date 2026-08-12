---
name: Daily Leadership Digest
description: A service leader asks what needs their attention today — escalations, SLA breaches, at-risk clients, and staffing flags in one short daily view.
category: Reporting & Analytics
tools: [search_tickets, search_clients, search_members, list_boards]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Daily Leadership Digest

**When to use:** "What needs my attention today?" from a service manager, director, or owner, or "anything on fire before I go into meetings?"

**Run it:** across all open/at-risk tickets today — manually on demand (Thread Flows are ticket-event triggered with no schedule, so this can't run itself).

## Prompt

```
The "what needs my attention" view for a service leader: only the items that warrant
leadership eyes today — escalations, breaches, at-risk clients, staffing flags —
everything else stays with the team. Leadership-only distribution; do not post to
tickets or client-visible channels.

This runs MANUALLY on demand — Thread Flows are ticket-event triggered with no
schedule/cron, so this is not a scheduled skill.

1. Run split searches per signal (per board where needed; disclose caps), excluding
   junk/NOC boards and auto-closed statuses:
   - Escalations — open escalated or P1 tickets, and tickets whose thread shows an
     unfulfilled escalation request.
   - SLA breaches — breached or breaching-today tickets.
   - At-risk clients — clients showing 2+ risk signals: sentiment decline, multiple
     aging tickets, a recurring issue without RCA, or an unresolved P1. NEVER volume
     alone.
   - Staffing flags — a queue outgrowing its owner, unassigned urgent items pooling, or
     one tech visibly overloaded relative to role peers.

2. Filter HARD: include only items that need a leadership decision, a client call, or a
   resource move. Items the team is already handling well get one summary line at most.

3. For each included item: what it is, why it clears the leadership bar, and the
   suggested move (call the client, reassign, approve overtime, chase the vendor).
   Staffing flags are observations with role/shift context, not performance judgments;
   route person-level concerns to the manager privately.

4. Cap the digest at roughly 10 items; if more qualify, lead with the top 5 and
   summarize the rest by theme.

5. Do not fabricate risk where searches returned nothing — an honest "nothing needs you
   today" is a valid, valuable digest. End with a one-line "green" note when a usual
   trouble area is quiet, plus a methodology note if any search capped. Fixed sections:
   Escalations / Breaches / At-Risk Clients / Staffing / All-Clear; empty sections
   print "none".
```
