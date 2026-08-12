---
name: No-Response Closure Sequence
description: Close a ticket after a client goes silent following three documented contact attempts: send the templated final message, close with a reopen-invite note.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# No-Response Closure Sequence

**When to use:** A ticket completed the follow-up cadence (three attempts) with no client reply and needs to be closed properly, "close out the no-response tickets" after a cadence sweep, or a tech asks to close a quiet ticket — this sequence proves it's safe to.

**Run it:** across all no-response tickets that finished the cadence (manually or on a schedule).

## Prompt

```
The clean, defensible end of the follow-up cadence. Verify the attempt history actually exists in
the thread, send a courteous final message, and close with an explicit invitation to reopen — so
no client ever discovers their ticket died silently.

1. Retrieve the ticket and verify the precondition: at least three documented, client-visible
   contact attempts since the client last replied, reasonably spaced (per the desk cadence). Phone
   attempts count only if a note records them. If fewer than three are on record, stop and route
   back to the Stale Ticket Follow-Up Cadence skill. Three documented attempts is a hard floor, not
   a guideline — if the attempts aren't in the thread, they didn't happen.

2. Confirm nothing changed since the last attempt: no inbound client reply on any channel in the
   thread, no future scheduled appointment, no open vendor dependency. Any of these voids the
   closure — a client reply after attempt three means the ticket is active again.

3. Send the templated final message as a client-facing note. House template shape: reference the
   issue in one line, list the dates we reached out, state the ticket is being closed due to no
   response, and say plainly that replying (or contacting the desk) will reopen it — no penalty, no
   friction. Friendly, never passive-aggressive. Keep it localizable; match the client's language
   where the thread isn't in English.

4. Close the ticket using the desk's no-response closed status where one exists; otherwise the
   standard closed status.

5. Add an internal closure note (plain text, no markdown): "Closed - no response after 3
   documented attempts on <date>, <date>, <date>. Client invited to reopen." The attempt dates
   come from the thread, never from memory.

6. Report: ticket closed, attempts cited, reopen path stated.

Never bulk-close a list without per-ticket verification of the attempt history and explicit user
sign-off on the batch. The final message and internal note must never fabricate dates, attempt
counts, or contact methods. If a dismissive one-word reply exists ("fine", "ok"), this is not a
no-response closure — route to Ticket QA Review. Direct client email is in-app only on some
tenants; the client-facing note is the standard delivery path and syncs to the PSA — note this
degradation rather than skipping the final message.

Running unattended: the trigger is a waiting-status age timer after the final cadence step, or a
"no response - pending closure" status. Your entire reply is the client-facing final message,
posted verbatim — no narration; the status change to closed happens as a tool call, then stop.
Proceed only when three documented client-visible attempts exist AND no inbound reply followed
them AND no future schedule entry exists. If any check fails or the history is ambiguous, do
nothing and stop.
```
