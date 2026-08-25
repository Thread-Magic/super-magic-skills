---
name: XLA Breach Risk Tiering
description: Tier every open ticket by XLA exposure — Breached, Critical, High, Watch — from remaining time to target with escalation factors and a next move.
category: QA & Closure
tools: [search_tickets, list_boards, list_ticket_priorities, add_ticket_note, update_ticket]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# XLA Breach Risk Tiering

**When to use:** "What's at risk of breaching?" / "tier the queue by XLA risk" / "anything breached overnight?" — the dispatcher's morning and pre-EOD passes, or feeding an escalation huddle a defensible priority order.

**Run it:** across all open tickets — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
Turn "what's about to breach?" into a four-tier board. Remaining time sets the base tier; the
thread moves tickets up or down.

1. Establish the XLA scheme: per-priority response and resolution targets as the user states
   them, or the priority mapping from available levels with the desk's defaults. If no targets
   are known, ask — never invent one.

2. Pull open tickets, split per board and per priority. Sweep Honesty base skill: disclose caps
   as "at least N" — a missed board here is exactly the ticket that breaches.

3. For each ticket compute remaining time to the nearest applicable target — first response for
   unanswered tickets, resolution otherwise — respecting pauses where a waiting status
   legitimately stops the XLA clock, but verify the wait is real (a client-visible ask exists),
   not just a parked status. State the math in business hours with the assumption shown, and say
   when the calendar is unknown.

4. Assign the base tier by remaining time: Breached (target passed), Critical (breaches this
   shift, default under 4 business hours), High (breaches within the next business day), Watch
   (within the tier horizon, default 3 business days).

5. Adjust one tier up or down for factors read from the thread, citing the factor that moved it —
   no vibes-based bumps. Escalating: client frustration or executive contact, repeat issue,
   unassigned ticket, a prior breach on the ticket, contractual or VIP flags the user defined.
   Mitigating: fix delivered pending client confirmation, a new timeline agreed in writing, an
   appointment before the target. Breached never adjusts down — a breach is a fact.

6. Recommend one move per ticket: assign now, escalate to a named role, respond now
   (first-response saves are cheapest), request a pause with documented client agreement, or
   accept-and-communicate an unavoidable breach.

7. Output the board: Breached first with age past target, then Critical, High and Watch, each
   sorted by remaining time. Per line: ticket, client, priority, remaining or overdue time,
   adjustment factor, recommended move. On request, leave a plain-text risk-flag note or assign
   and escalate — with confirmation, never in bulk.

If the scheme is unknown or a ticket's target is ambiguous, put it in an UNKNOWN bucket and say
what's missing. Report breaches without spin: age past target, not "slightly over".

Run unattended from an external scheduler: the entire reply is a plain-text tier digest, no
narration. Board list, per-priority targets, tier horizons and business calendar are supplied,
never inferred; without targets reply exactly "XLA TARGETS NOT CONFIGURED - NO REPORT." Ambiguous
targets go to UNKNOWN. Step 5 does NOT run there — thread-evidence bumps stay attended, so tier
by remaining time only. No writes. Zero open tickets in scope, reply exactly "NO TICKETS AT
RISK."
```
