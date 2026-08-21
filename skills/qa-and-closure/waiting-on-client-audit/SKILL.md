---
name: Waiting-on-Client Audit
description: Audit every ticket parked in a waiting status: how long, whether a follow-up was sent, and the correct next action — nudge, reschedule, unpark, close.
category: QA & Closure
tools: [search_tickets, list_ticket_statuses, add_ticket_note, update_ticket, schedule_ticket]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Waiting-on-Client Audit

**When to use:** "Audit the waiting-on-client bucket" / "what's actually waiting on clients vs just parked?" — a weekly review before waiting statuses distort aging and SLA numbers, or suspicions that techs park tickets in waiting to stop the clock.

**Run it:** across all tickets in waiting statuses — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
"Waiting on client" is where tickets go to hide. Separate tickets legitimately waiting (follow-up
sent, ball demonstrably in the client's court) from tickets merely labeled waiting — where the
status was set but no one ever actually asked the client for anything.

1. Map the board's waiting statuses (waiting on client, pending customer, on hold variants), then
   pull every open ticket in them, split per status per board. Disclose result caps.

2. For each ticket, establish three facts from the thread:
   - Wait duration — time since it entered the waiting status (or since the last client-facing
     message, whichever tells the truer story).
   - Was a follow-up actually sent? — a client-visible message exists asking the client for the
     specific thing we're waiting on, sent at or after the status change. A status flip with no
     outbound message is a false wait. Internal notes don't count.
   - What are we waiting for? — extractable from the thread in one line, or UNKNOWN (itself a
     defect).

3. Classify each ticket:
   - Legitimate wait — ask sent, wait within cadence, reason known. Note when the next cadence
     nudge is due.
   - Overdue wait — ask sent but client silent past the cadence window → route to Stale Ticket
     Follow-Up Cadence (or No-Response Closure Sequence if attempts are exhausted).
   - False wait — status says waiting but no ask was ever sent, or the last message is FROM the
     client (we owe them) → an MSP-owned stall mislabeled; recommend unparking.
   - Stale-reason wait — waiting on something the thread shows already arrived or was resolved.

4. Recommend one next action per ticket: draft-and-send the missing ask (false wait), nudge per
   cadence (overdue), unpark to a working status (false/stale), set a follow-up date (legitimate
   wait with no touchpoint), or route to closure sequence.

5. Apply actions only on approval. Any posted ask or unpark note goes as an internal plain-text
   note. Never bulk-unpark or bulk-send without sign-off — unparking changes SLA clocks and
   workloads.

6. Output a table grouped by classification, longest wait first: ticket, client, days waiting,
   ask-sent yes/no, waiting-for, next action. Headline the false-wait count — it's the audit's
   most important number.

The status label is a claim; only a client-visible ask in the thread makes a wait real. When the
last message is inbound from the client, the ticket is never "waiting on client," whatever the
status says. If the waiting reason is UNKNOWN, say so and recommend the tech document it. If write
tools are disabled, deliver the audit and drafts in chat only.

This is a sweep, not a Flow — run it manually on demand, or from an external scheduler that
invokes Super Magic. Running unattended: the entire reply is the artifact — the plain-text audit
table (classification, ticket, client, days waiting, ask-sent yes/no, waiting-for, recommended
action), with the false-wait count as the first line. No narration. Statuses not supplied are not
guessed. Permitted writes: none — unparking, scheduling, and posting asks all change SLA clocks or
reach clients, so they stay attended. If it can't be determined whether an ask was sent, classify
the ticket UNVERIFIED, never "false wait" — an accusation of parking needs certainty. Capped
searches labeled "at least N". Zero tickets in waiting statuses → reply exactly "NO TICKETS IN
WAITING STATUSES."
```
