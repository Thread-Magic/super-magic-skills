---
name: Post-Incident Action Tracking
description: Turn post-incident review action items into real tickets with owners and due dates, then run the follow-through audit that catches ones dying in backlog.
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
Two things keep post-mortem action items from dying: convert each accepted action into a
tracked ticket at PIR time, and audit the set until every item is done, deliberately
dropped, or escalated.

CONVERSION (at PIR time)
1. Pull the action items from the post-mortem document or ticket. Convert only items a
   human accepted at the review — not every "we could..." musing.
2. Each accepted item needs three fields before it becomes a ticket: a SPECIFIC VERIFIABLE
   ACTION ("add disk-space alerting on the database volume at 80%", not "improve
   monitoring"), an OWNER (a named person — "the infrastructure team" is where actions go
   to die; check the team directory to disambiguate), and a DUE DATE proportionate to the
   risk it mitigates. An item missing a field goes back to the requester as "not trackable
   yet: needs <field>", recorded as such — never dropped silently, never created hollow.
3. Create one ticket per action on the internal-work board, titled "PIR ACTION: <verb
   phrase> [<incident ref>]", carrying the action, the incident and post-mortem
   references, why it matters, the owner and the due date.
4. Cross-link: leave a note on the incident master ticket listing every action ticket
   created (apply the PSA Note Discipline base skill — plain text, no markdown or emojis).
   If the RFO letter promised specific prevention measures, verify each promise has an
   action ticket behind it and flag any that does not — a written client promise with no
   ticket behind it is a liability.

FOLLOW-THROUGH AUDIT (default every 2 weeks until the set closes)
5. Search open PIR-action tickets and classify each from evidence: DONE (closed with
   completion evidence — the change-completion-verification standard where it was a
   change; a bare "done" is unverified), ON TRACK, AT RISK (due within a week, no
   activity), OVERDUE, or STALLED (no activity in 30+ days).
6. On overdue and stalled items, leave a nudge note addressed to the owner and roll repeat
   offenders up to the lead. The audit's product is the uncomfortable list: "incident
   <ref> was 6 weeks ago; 3 of 5 prevention actions have had zero activity."
7. A stalled action being deliberately dropped needs the drop made explicit: a note by the
   owner or lead saying it is descoped and why. Close the ticket referencing that
   decision.
8. Report per incident: actions done / on track / at risk / overdue /
   dropped-with-decision, and the follow-through rate over time.

Guardrails: you create tickets, nudge, and report — you never mark an action done without
evidence, never pick owners yourself, never descope an item on your own judgment. One
action, one ticket, one owner. Actions that were client promises in an RFO can only be
dropped with the lead's explicit sign-off. Apply the Sweep Honesty base skill: if the
action-ticket search may have capped, say the audit is partial.
```
