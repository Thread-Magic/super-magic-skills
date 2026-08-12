---
name: Aging, SLA & Follow-Up
description: Sweep open tickets for real staleness by last client-facing update, separate MSP stalls from legitimate waits, nudge techs, and drive clean closure.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, schedule_ticket, search_members, list_boards, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Aging, SLA & Follow-Up

**When to use:** Run on a cadence (daily/weekly) to catch tickets going quiet or drifting toward SLA trouble — "what's aging in the queue?" / "clean up the stale tickets" / "which tickets have we dropped?", or clearing the backlog honestly before a service review.

**Run it:** across all open tickets (manually or on a schedule).

## Prompt

```
The recurring hygiene sweep for tickets going quiet. Distinguish tickets genuinely stalled on the
MSP's side from tickets correctly waiting on a client, vendor, or scheduled date — and produce a
prioritized action list, not a raw age report.

1. Enumerate open tickets, splitting searches per board and per status so result caps don't
   silently truncate the sweep. If any search may have capped, say so.

2. For each ticket, compute the last meaningful client-facing update: the most recent
   client-visible message or substantive progress note. Internal notes, time entries, status
   flips, and automated touches do NOT reset the clock — a ticket "touched" daily by a bot can
   still be stale.

3. Classify each stale ticket's ownership:
   - MSP-owned stall — the ball is in our court: client replied and we went quiet, work promised
     but not documented, unassigned and aging.
   - Legitimate wait — client response pending WITH a follow-up actually sent, vendor RMA or
     third-party dependency documented, or a future scheduled service date in a proper scheduled
     status. Verify the wait is documented, not assumed.

4. For each MSP-owned stall, leave an internal plain-text note @mentioning the assigned tech —
   look them up to resolve the mention — stating days since the last meaningful client-facing
   update and the single next expected action. If unassigned, flag for dispatch instead.
   @mention notes are factual nudges, not blame.

5. Pull tickets nearing or past an SLA target out of the routine list and flag them at the top —
   imminent breaches are not routine aging.

6. For legitimate waits with no future touchpoint, offer to schedule a follow-up date rather than
   leaving them adrift. Skip tickets parked on a future scheduled call in a proper status — don't
   nag a correctly scheduled ticket.

7. Output a prioritized list: SLA-imminent first, then MSP-owned stalls (oldest meaningful-update
   first), then legitimate waits with their next touchpoint. One recommended action per ticket:
   nudge, escalate, schedule, or route to closure.

8. Present everything for sign-off before acting. Never bulk-close, bulk-reassign, or bulk-send
   follow-ups without explicit confirmation — closure of no-response tickets belongs to the
   No-Response Closure Sequence skill after documented attempts. Disclose result caps rather than
   presenting a truncated sweep as complete. If write tools are disabled, deliver the action list
   in chat only.
```
