---
name: Status Check Intent Design
description: Design the "any update on my ticket?" intent: answer from real ticket status and last client-visible update, escalating only when the trail has gone cold.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Status Check Intent Design

**When to use:** "Build an intent for ticket status questions" / "techs get interrupted all day by 'any update?' messages" / Intent Mining shows update-requests as one of the biggest non-issue conversation types.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a status-check intent that turns "any update?" into a self-served answer: identify the
ticket, read its real status and last client-visible update, reply with that, and ping a human only
when the ticket is genuinely stale or the user rejects the answer. Building intents is admin-only;
if you can't, output the spec for an admin.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate it;
ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5 near-misses
from the watch-outs below) and write only on explicit confirmation; do NOT activate — the admin
does that once the tests pass. Two decisions define the behavior and are agreed
with the admin first: the freshness threshold — calibrate it from how often a recent "any update"
ticket was really "waiting on you" rather than stale — and the visibility policy.

Spec:
- Triggers: "any update on my ticket", "status of my ticket", "any news on", "has anyone looked at
  my request", "when will my ticket be fixed", "still waiting on", "ticket number <ticket> update".
  Watch-outs: "any update?" inside an active ticket thread is conversation, not a new match; a
  follow-up adding new symptoms should append to the ticket, not just report status.
- Arguments, identification: the ticket number, or enough to find it — what it was about and
  roughly when. Several open tickets and no number: list theirs briefly and ask which.
- Reply flow, from the record: (1) locate the ticket among the requester's or their company's own
  tickets; (2) reply with the status in plain language ("Scheduled", not an internal code), the
  last client-visible update with its date, and the next expected step if recorded; (3)
  client-visible material ONLY — never internal notes or tech names in blame-able contexts; (4)
  waiting on the user: say so, restate what is needed; (5) staleness branch — no client-visible
  activity beyond the admin-set freshness threshold: note on the ticket that the client asked and
  it looks stale, and tell the user the desk was nudged; (6) pushback or escalation-level
  frustration routes to a human with the conversation attached; never argue.
- Handoff rule: the intent reports and nudges. It never changes priority, promises a resolution
  date, or reopens or closes tickets.
- Variations per client: status-name translations, the freshness threshold, whether contacts see
  their company's tickets or only their own, the escalation path.
- Success metric: deflection rate on status conversations; counter-metric, escalations that began
  as status checks.

Guardrails: strict requester scoping — never return status for a ticket the asking contact is not
entitled to see, and when identification is ambiguous, ask rather than guess. No promises: no
resolution dates, no "shortly", no priority changes. The staleness nudge is a plain-text note.
```
