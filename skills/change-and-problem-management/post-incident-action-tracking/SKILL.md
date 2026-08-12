---
name: Post-Incident Action Tracking
description: Turn post-incident review action items into real tickets with owners and due dates, then run the follow-through audit that catches the ones quietly dying — the discipline that makes postmortems more than a feelings meeting.
category: Change & Problem Management
tools: [search_tickets, create_ticket, update_ticket, add_ticket_note, list_boards, search_members]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Post-Incident Action Tracking

**When to use:** a post-mortem/PIR just concluded ("track the action items from the <incident> post-mortem") / the periodic follow-through audit ("where are we on post-incident actions?") / an RFO letter promised prevention measures that need tracking / before closing a major incident's master ticket.

**Run it:** on one post-mortem · or as a follow-through audit across open action items.

## Prompt

```
Do the two things that keep post-mortem action items from dying: convert each accepted
action into a tracked ticket at PIR time, and audit the set on a cadence until every item
is done, deliberately dropped, or escalated — never just forgotten.

CONVERSION (at PIR time):
1. Pull the action items from the post-mortem document or ticket. Only convert items a
   human accepted at the review — don't promote every "we could..." musing into committed
   work.
2. For each accepted item, require three fields before it becomes a ticket: a SPECIFIC
   VERIFIABLE ACTION ("add disk-space alerting on the database volume at 80%," not
   "improve monitoring"), an OWNER (a named person — "the infrastructure team" is where
   actions go to die; check the team directory to disambiguate), and a DUE DATE proportionate to the
   risk it mitigates. Items missing any field go back to the requester as "not trackable
   yet: needs <field>" — recorded as such, not silently dropped and not created hollow.
3. Create one ticket per action (on the internal-work board): title "PIR ACTION: <verb phrase> [<incident ref>]", body carrying the
   action, incident and post-mortem references, why it matters, owner, due date.
4. Cross-link: a plain-text note on the incident master ticket listing every action ticket
   created. If the RFO letter promised specific prevention measures, verify each promise
   has a corresponding action ticket and flag any that don't — a written client promise
   with no ticket behind it is a liability.

FOLLOW-THROUGH AUDIT (on a cadence, default every 2 weeks until the set closes):
5. search for open PIR-action tickets; classify each from evidence: DONE (closed
   with completion evidence — change-completion-verification standard where it was a
   change; a bare "done" is unverified), ON TRACK, AT RISK (due within a week, no
   activity), OVERDUE, or STALLED (no activity in 30+ days).
6. For overdue/stalled items, post a plain-text nudge note addressed to the owner, and roll
   repeat offenders up to the lead: the audit's product is the uncomfortable list —
   "incident <ref> was 6 weeks ago; 3 of 5 prevention actions have had zero activity."
7. If a stalled action is being deliberately dropped, require the drop to be explicit: a
   note by the owner or lead stating it's descoped and why. Close the ticket referencing
   that decision.
8. Report the audit: per incident, actions done / on track / at risk / overdue /
   dropped-with-decision, and the follow-through rate over time.

Guardrails: the agent creates tickets, nudges, and reports — it never marks an action done
without evidence, never picks owners itself, never descopes an item on its own judgment.
One action, one ticket, one owner. Verification standard is real: prevention actions that
were changes get the same evidence bar as any change completion. Actions that were client
promises (RFO) can only be dropped with the lead's explicit sign-off. Result-cap honesty:
if the action-ticket search may be capped, say the audit is partial.
```
