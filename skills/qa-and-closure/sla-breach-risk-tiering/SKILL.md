---
name: SLA Breach Risk Tiering
description: Tier every open ticket by SLA exposure — Breached, Critical, High, Watch — from remaining time to target with escalation factors and a next move.
category: QA & Closure
tools: [search_tickets, list_boards, list_ticket_priorities, add_ticket_note, update_ticket]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# SLA Breach Risk Tiering

**When to use:** "What's at risk of breaching?" / "tier the queue by SLA risk" / "anything breached overnight?" — the dispatcher's morning and pre-EOD passes, or feeding an escalation huddle a defensible priority order.

**Run it:** across all open tickets — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
Turn "what's about to breach?" into a four-tier board: already breached, breaching within hours,
breaching today/tomorrow, and worth watching. Remaining time sets the base tier; what the thread
shows moves tickets up or down.

1. Establish the SLA scheme: per-priority response/resolution targets from the desk's config as
   the user states them, or the priority mapping from the available levels with the desk's default
   targets. If no targets are known, ask — never invent an SLA.

2. Pull open tickets, split per board and per priority; disclose result caps — a missed board in an
   SLA sweep is exactly the ticket that breaches.

3. For each ticket, compute remaining time to the nearest applicable SLA target (first response
   for unanswered tickets, resolution otherwise), respecting SLA clock pauses where waiting
   statuses legitimately pause the clock — but verify the wait is real (a client-visible ask
   exists), not just a parked status. State time math in business hours with the assumption shown;
   when the business calendar is unknown, say so.

4. Assign the base tier by remaining time: Breached (target passed) / Critical (breaches within
   the current shift, default < 4 business hours) / High (breaches within the next business day) /
   Watch (breaches within the tier horizon, default 3 business days).

5. Adjust one tier up or down for factors read from the thread, citing which factor moved it —
   no vibes-based bumps. Escalating: visible client frustration or executive contact, repeat issue,
   ticket unassigned, prior breach on the same ticket, contractual/VIP flags the user defined.
   Mitigating: fix delivered and pending client confirmation, client agreed to a new timeline in
   writing, scheduled appointment before the target. Breached never adjusts down — a breach is a
   fact.

6. Recommend one move per ticket: assign now, escalate to <role>, respond now (first-response
   saves are cheapest), request an SLA pause with documented client agreement, or
   accept-and-communicate for unavoidable breaches.

7. Output the tier board: Breached first with age-past-target, then Critical / High / Watch each
   sorted by remaining time; per line: ticket, client, priority, remaining/overdue time,
   adjustment factor if any, recommended move. On request, leave a plain-text risk-flag note or
   assign/escalate the ticket — with confirmation, never in bulk.

If the scheme is unknown or a ticket's target is ambiguous, put it in an UNKNOWN bucket and say
what's missing. Breached tickets are reported without spin: age past target, not "slightly over."
Read-mostly: notes, assignments, and escalations happen only on explicit approval.

Running unattended (from a scheduler): the entire reply is the artifact — a plain-text tier
digest, no narration, no questions. Deterministic inputs: board list, per-priority SLA targets,
tier horizons, business calendar — none ever inferred; if SLA targets aren't supplied, reply
exactly "SLA TARGETS NOT CONFIGURED - NO REPORT." Format: Breached / Critical / High / Watch
sections, one line per ticket. Ambiguous-target tickets go in an UNKNOWN section, never guessed
into a tier. Capped searches labeled "at least N". Factor adjustments (step 5) do NOT run in this
variant — thread-evidence bumps are judgment and stay attended; base tiers by remaining time only.
Permitted writes: none. Zero open tickets in scope → reply exactly "NO TICKETS AT RISK."
```
