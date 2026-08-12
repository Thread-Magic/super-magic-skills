---
name: Single Ticket Handoff Card
description: Hand one ticket to another technician with a compact card — status table, watch points, overdue-task detection, and a one-sentence next action.
category: Escalation
tools: [search_tickets, add_ticket_note, update_ticket, search_members, schedule_ticket]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Single Ticket Handoff Card

**When to use:** "Hand this ticket to <member>" / "reassign this to <member> with context"; a tech is going on PTO and one in-flight ticket needs a new owner; or a ticket moves between teams mid-work (not a tier escalation — for that use Escalation Prep).

**Run it:** on one ticket.

## Prompt

```
You are handing exactly one ticket to a specific technician. Build a compact card that
tells the receiver everything they need without reading the thread.

1. Read the full thread, notes, tasks, and schedule entries for the ticket.

2. Build the card:
   - Status table — one compact table: Status | Priority | Board | Client contact |
     Age | Last client contact | SLA state | Scheduled work.
   - Story so far — 2–3 sentences max: the issue and where the work stands.
   - Watch points — the traps: promised commitments and their deadlines, sensitive
     contact dynamics, VIP flags, things already tried that must not be repeated,
     dependencies on vendors or parts.
   - Overdue check — compare tasks, scheduled entries, and promised follow-ups against
     today's date; list anything already overdue at handoff, explicitly, so it
     transfers as a known debt rather than a surprise.
   - Next action — exactly one sentence, concrete and doable: "Call <user> after 2pm
     to confirm the replacement device arrived, then close." Not a list.

3. Show the card in chat. On confirmation: reassign the ticket to the new owner, post the
   card as a plain-text internal note so it lives on the ticket, and offer to move any
   scheduled entries to the new owner.

Guardrails: one next action — if the ticket genuinely needs a plan, the next action is
the first step of it and the rest goes under watch points. Overdue items are surfaced,
never silently rolled forward. Confirm the receiving technician before reassigning; never
guess between similarly named members. Do not invent commitments or deadlines — only
report ones documented in the thread; unknowns are stated as unknowns. The posted note is
plain text (no tables in the note — flatten to labeled lines for PSA compatibility); the
table form is for chat display only.
```
