---
name: Status Update Messenger
description: One command sets the ticket status and posts the matching templated client message from a per-status map — so a status change and the client-facing note that should go with it happen together. Runs manually on demand.
category: Communication
tools: [update_ticket, list_ticket_statuses, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Status Update Messenger

**When to use:** "Set this to Waiting on Client and tell them why" / "move to Scheduled and send the appointment note" / "mark resolved and post the closing message" — any status change that has a standard client-facing message attached.

**Run it:** on one ticket.

## Prompt

```
Set the ticket status and post the matching client message together, so the two never get out
of sync (status flips but the client hears nothing, or a message goes out but the status stays
wrong).

1. Confirm the target status against the desk's REAL configured statuses — statuses vary per
   board/PSA, never assume a status name exists.

2. Look up the matching message in the per-status template map (the desk's standard wording for
   that status). Fill it with the ticket specifics (client name, next step, timeframe).

3. Preview BOTH: the status change and the exact client-facing message text. Wait for an
   explicit yes. Let me edit the message before it goes.

4. On confirm, change the status, then post the message — as a client reply if it's outbound,
   or as an internal note if the desk sends manually. Keep note text plain-text for PSA
   compatibility.

5. Report both: "Set status to <X> and posted the <X> client message on #<n>." If either fails,
   say which.

Confirm before writing — a status change plus an outbound message is two consequential writes;
both wait on one explicit go-ahead over the preview. Validate the status name against the desk's
real statuses — don't attempt to set one that doesn't exist on that board. Use the mapped
template; if no message is mapped for the chosen status, ask rather than improvising an outbound
message. Keep the two in sync — never set the status without the message (or vice versa) when
the map calls for both; report partial success honestly if one write fails. No fabrication of
statuses or client-facing commitments (dates, timeframes) not grounded in the ticket.
Member-invoked only; the client-message half can't run as a native Flow action.
```
