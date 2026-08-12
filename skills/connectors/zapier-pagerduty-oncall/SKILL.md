---
name: Zapier PagerDuty On-Call
description: Page the on-call engineer for a P1 via PagerDuty, tell the requester who's on call and that they've been paged, and mirror the ack/resolve loop back to the ticket. Use for "page on-call", "who is on call right now", or wiring P1 paging into an after-hours flow.
category: Connectors
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: [Zapier: PagerDuty]
scope: single
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Zapier PagerDuty On-Call

**When to use:** "Server down at <client> — page on-call," "who's on call tonight?" (lookup only), or an after-hours flow that needs a paging action for P1s outside coverage.

**Run it:** on one ticket · or as a Flow (triggered when a P1 lands outside coverage hours).

## Prompt

```
Close the after-hours gap: for a genuine P1, look up who's on call in PagerDuty, trigger the page,
tell the requester a named human is engaged, and keep the ticket in lockstep with the incident's
ack/resolve state.

This runs only if the member has connected Zapier with the tenant's PagerDuty. If it's absent,
degrade to the tenant's manual on-call procedure (documented phone tree) and say clearly that no
page was sent — do not stop. Each Zapier call = 2 Zapier tasks; a page cycle is ~2–3 calls, so
check on the escalation window, don't poll incident state in a tight loop.

1. Qualify the P1 against the tenant's paging criteria (site down, server down, security incident,
   VIP-defined). Not qualifying → do not page; route to the normal queue and say why. Paging for
   non-P1s is how paging gets ignored.
2. Dedupe before paging: check the ticket and recent siblings for an existing page on the same
   incident. Already paged → add context to the existing incident rather than re-triggering. Use a
   deterministic dedup key (ticket number or alert correlation id) when triggering so PagerDuty
   folds repeats into one incident. Double-paging one incident at 3am costs goodwill the desk can't
   buy back.
3. Look up who is on call for the relevant escalation policy/schedule.
4. Confirm with me (attended) or proceed per the flow's approved criteria (unattended), then
   trigger the page with client, one-line symptom, ticket reference, callback path, and the dedup
   key.
5. Tell the requester: "<MSP>: we've paged our on-call engineer (<first name>) — you'll hear from us
   within <SLA window>." Name only what the tenant shares (first name/role); commit only to the SLA
   the desk actually has. Never tell a requester someone was paged unless the page actually fired.
6. Mirror to the ticket: leave a note (plain text) for paged/acknowledged/resolved transitions;
   set the ticket status per the desk's incident choreography. On follow-up, check the incident → if
   unacknowledged past the escalation window, escalate per policy (next tier/manager), don't silently
   wait. PagerDuty resolution is not ticket resolution — the ticket still closes through normal QA.
```
