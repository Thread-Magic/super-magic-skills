---
name: Bulk Onboarding Coordinator
description: Coordinate a multi-hire onboarding wave with one parent ticket, child ticket per hire, and a consolidated status table kept current through cutover.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, create_ticket, update_ticket, add_ticket_note, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Bulk Onboarding Coordinator

**When to use:** "We have 8 new starters on the 1st — here's the list" / an acquisition, new office, or seasonal class landing as one big request / "where are we on the <client> hiring wave?"

**Run it:** on one wave request — identity- and approval-gated per hire, so a human stays in the loop.

## Prompt

```
Keep this hiring wave from becoming ten interleaved messes: one parent ticket owns the
wave, each hire gets their own child ticket running the standard onboarding, and a
consolidated status table on the parent shows the whole wave at a glance.

1. Parse the wave request into a per-hire roster: name, start date, role, department,
   manager, location, hardware, special requests. Validate each row (missing fields =
   MISSING, never guessed). Confirm the roster back to me before creating anything —
   one wrong spreadsheet column becomes N wrong accounts.

2. Open the parent ticket for the wave: client, start date(s), hire count, requester,
   roster. This is the coordination/status surface, not a work ticket.

3. Open one child ticket per hire, titled to the client's convention, each referencing
   the parent ticket number and carrying that hire's Required / Conditional / Optional
   checklist per New Hire Onboarding. List every child ticket number on the parent.
   Each child runs the standard New Hire Onboarding skill — ALL its guardrails
   (role-based access, approvals for cost, secure credential handling, 48-hour priority
   bump) apply per hire, not once for the wave.

4. Batch what is honestly batchable, keep per-hire what is not: one license purchase
   approval may cover the wave's counted total (License Lifecycle note on the parent);
   hardware may ship as one order. Credentials, verification, and MFA enrollment are
   strictly per hire — never share a temporary password across hires or reuse a
   pattern-guessable sequence.

5. Maintain the consolidated status table as a plain-text note on the parent (re-post
   updated, plain text only for PSA sync; a fixed-width table reads fine): one row per
   hire — name, child ticket, account, licenses, groups, hardware, MFA, credential
   handoff — each cell Done / Pending / Blocked. Update on every meaningful child
   change or the requested cadence.

6. Escalate wave-level risks on the parent: hires within 48 hours of start with Blocked
   items; roster changes mid-wave (added/dropped hires get an explicit note, and a
   dropped hire's child ticket is closed with any created access rolled back per
   Employee Offboarding order).

7. When every child completes: final status table, wave summary to me with anything
   still pending (e.g. hardware in transit), and log time on the parent.

Guardrails: confirm the roster with me before creating child tickets — never provision
from an unconfirmed spreadsheet. Every per-hire guardrail from New Hire Onboarding holds
inside the wave; bulk is a coordination pattern, not a shortcut past approvals or secure
credential handoffs. Never reuse or sequence temporary passwords across the wave. The
status table reports child-ticket reality; do not mark a hire Done on the parent while
their child ticket has open items. If the wave exceeds what one table can track
reliably, split into batched parents by start date rather than letting one table go
stale.
```
