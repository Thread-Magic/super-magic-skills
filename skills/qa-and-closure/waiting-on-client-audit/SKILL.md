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

**When to use:** "Audit the waiting-on-client bucket" / "what's actually waiting on clients vs just parked?" — a weekly review before waiting statuses distort aging and XLA numbers, or suspicions that techs park tickets in waiting to stop the clock.

**Run it:** across all tickets in waiting statuses — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
"Waiting on client" is where tickets go to hide. Separate tickets legitimately waiting —
follow-up sent, ball in the client's court — from tickets merely labelled waiting, where nobody
ever asked the client for anything.

1. Map the board's waiting statuses (waiting on client, pending customer, on-hold) and pull every
   open ticket in them, split per status per board. Sweep Honesty base skill: disclose caps as
   "at least N".

2. For each ticket establish three facts from the thread. Wait duration: time since it entered
   the waiting status, or since the last client-facing message, whichever is truer. Was a
   follow-up actually sent: a client-visible message asking for the specific thing we're waiting
   on, at or after the status change — a status flip with no outbound message is a false wait,
   and internal notes don't count. What are we waiting for: one line from the thread, or UNKNOWN,
   itself a defect. 3. Classify each ticket. Legitimate wait: ask sent, within cadence, reason
   known — note when the next nudge falls due. Overdue wait: ask sent, client silent past the
   cadence window — route to Stale Ticket Follow-Up Cadence, or No-Response Closure Sequence once
   attempts are exhausted. False wait: no ask was ever sent — an MSP-owned stall, mislabelled;
   recommend unparking. Stale-reason wait: waiting on something the thread shows already arrived.

4. Recommend one action per ticket: draft the missing ask, nudge per cadence, unpark to a working
   status, set a follow-up date, or route to closure.

5. Apply actions only on approval, posting any ask or unpark note as an internal note — plain
   text, no markdown or emojis (PSA Note Discipline base skill). Never bulk-unpark or bulk-send
   without sign-off — unparking changes XLA clocks and workloads.

6. Output a table grouped by classification, longest wait first: ticket, client, days waiting,
   ask-sent yes or no, waiting-for, next action. Headline the false-wait count — the audit's most
   important number.

The status label is a claim; only a client-visible ask makes a wait real. When the last message
is inbound from the client, the ticket is never "waiting on client", whatever the status says.
Where the waiting reason is UNKNOWN, recommend the tech document it. If write tools are off,
deliver the audit and drafts in chat.

This is a sweep, not a Flow: run it on demand, or from an external scheduler. Run unattended, the
reply is the artifact — the plain-text audit table, false-wait count first, no narration.
Statuses not supplied are not guessed. No writes: unparking, scheduling and posting asks change
XLA clocks or reach clients, so they stay attended. If you can't tell whether an ask was sent,
classify the ticket UNVERIFIED, never "false wait" — an accusation of parking needs certainty.
Zero tickets in waiting statuses, reply exactly "NO TICKETS IN WAITING STATUSES."
```
