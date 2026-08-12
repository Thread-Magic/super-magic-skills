---
name: Halo SLA and Priorities
description: HaloPSA SLA and priority interplay: priority sets response and fix targets within the client's SLA, and configured hold statuses pause the clock.
category: PSA-Specific
tools: [search_tickets, list_ticket_priorities, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Halo SLA and Priorities

**When to use:** Setting or changing priority on a Halo-synced ticket, "when is this due?" / breach-risk assessment on a Halo desk, or explaining why two same-priority tickets have different deadlines.

**Run it:** on one ticket · across all at-risk tickets on a board · or as a Flow (triggered on ticket create or status change, to set/verify priority and SLA).

## Prompt

```
You are reading Halo's SLA/priority interplay. In HaloPSA the client's SLA and the ticket's
priority work as a pair: the SLA defines a target matrix, and the priority row selects which
response target and fix (resolution) target apply. Changing priority changes the deadlines — it
is an SLA action, not a cosmetic label.

1. Re-read the ticket at full detail — priority, status, and SLA state may have moved Halo-side
   since your last read.

2. Read the pair: which SLA applies (from the client/contract) and which priority is set (from
   the tenant's actual priority list). The deadlines are the intersection; never quote a target
   from priority alone without knowing the client's SLA, since Halo targets differ per SLA.

3. Distinguish the two clocks: response target (first agent response) and fix target
   (resolution). Report which is live and how much remains on each. A met response with a distant
   fix target is a different situation from an unmet response — say which.

4. Check pause state: hold-type statuses (waiting on customer/vendor/etc., per the desk's config)
   pause the SLA clock; verify the actual status against the desk's live status list rather than
   trusting a "waiting" phrase in a note. Only the status pauses the clock — a note does not.

5. When changing priority, treat it as a deadline change: state old → new priority and the
   resulting target shift, and justify from impact/urgency evidence in the thread (security and
   multi-user impact force high priority). Apply after confirmation; note the reason in a plain-
   text note.

6. Output: applicable SLA (as far as visible), priority, live clock(s) with remaining time or
   "target not visible from Thread", pause state, and breach-risk tier.

Always: re-read before any deadline claim or priority change; a Halo-side response may have
already met the target you are about to escalate over. Never lower a priority to avoid a breach —
that is deadline-gaming and shows in Halo's SLA reporting; escalate instead. Never quote deadlines
you cannot see: if SLA targets are not visible from Thread, report the priority and recommend
confirming the target matrix in Halo rather than inventing hours. Business-hours calendars vary
per SLA in Halo; do not convert targets to wall-clock times unless the coverage calendar is known.
Priority changes on client-facing tickets may trigger Halo notifications — call it out before
applying.
```
