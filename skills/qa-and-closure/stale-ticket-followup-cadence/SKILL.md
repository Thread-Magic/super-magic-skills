---
name: Stale Ticket Follow-Up Cadence
description: Drive a configurable 24/48/72 follow-up cadence on tickets awaiting client reply: draft each friendly nudge, count attempts, skip legitimate waits.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, schedule_ticket]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Stale Ticket Follow-Up Cadence

**When to use:** "Follow up on my waiting tickets" / "who hasn't replied to us?" — running the desk's standard cadence (24/48/72h, or the house variant) across a queue, or drafting the next nudge for one specific quiet ticket.

**Run it:** across all waiting-on-client tickets — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
Keep waiting-on-client tickets moving on a predictable rhythm: count the attempts already
documented in the thread, draft the next follow-up in a friendly client-facing voice, and know
when a ticket is waiting for a good reason.

1. Confirm the cadence. Default: first follow-up 24h after the last outbound client-facing
   message, second at 48, third at 72 — three attempts, then hand off to the No-Response Closure
   Sequence skill. Honour a desk-specific cadence if the user states one; "3 days, 3 attempts, 3
   emails" is a common house rule.

2. Find candidates: open tickets in waiting-on-client statuses where the last message is outbound
   and older than the cadence step.

3. Count documented attempts per candidate — client-visible follow-ups since the client last
   replied. Only messages the client could actually see count: internal notes are not attempts,
   and never assume a phone attempt happened unless a note records it.

4. Skip legitimate waits: a future scheduled appointment, a client-stated timeline ("back from
   vacation Monday"), a vendor dependency, an approval pending. Don't nudge someone who told you
   when they'll respond. The skip list is sacred — where legitimacy is unclear, skip and flag
   rather than send.

5. Draft the follow-up for each remaining ticket in a client-facing voice: friendly, short,
   referencing the original issue in one line, saying what's needed, and offering an easy out
   ("if this is resolved, let us know and we'll close it"). Escalate tone gently across attempts:
   attempt three notes the ticket will close soon without a reply, and never sounds annoyed. No
   internal jargon, no ticket-system boilerplate, no invented details. Match the client's
   language where the thread isn't in English.

6. Present the drafts for review, then post each approved follow-up as a client-facing note and
   set the waiting status. Never bulk-send without the user reviewing the drafts.

7. Output a summary table: ticket, client, attempt just sent (or skipped, and why), and when the
   next cadence step falls due. Never exceed the attempt count — where the thread already shows
   three documented attempts, route to the closure sequence instead of a fourth nudge.

This is a cadence sweep, not a Flow: Thread Flows fire on ticket events only, with no schedule,
cron, age or elapsed-time trigger. Run it on demand, or from an external scheduler. Run
unattended, your entire reply is the client-facing follow-up, posted verbatim — no narration, no
attempt counters, no internal commentary. Send only when the ticket is in a waiting-on-client
status, the last message is outbound, the cadence step is due, and attempts are below the
maximum. If any condition fails, or the wait looks legitimate, produce no output and stop. Never
draft attempt three or beyond unattended where the desk requires sign-off before final notices.
```
