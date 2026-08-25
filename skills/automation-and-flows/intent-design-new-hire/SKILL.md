---
name: New Hire Intent Design
description: Design the new-hire onboarding intake intent: collect the full checklist up front so the ticket arrives complete and routes into the onboarding workflow.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# New Hire Intent Design

**When to use:** "Build an intent for new employee onboarding requests" / "new-user tickets always come in half-filled — fix the intake" / Intent Mining flagged new user / new hire as a top-volume request.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a new-hire intent whose whole job is complete intake: gather every checklist field in one
conversation so the onboarding ticket arrives dispatch-ready and never bounces back with "what's
their start date?". It does NOT deflect. Building intents is admin-only; if you can't, output the
complete written spec for an admin to apply.

Follow automation-and-flows/intent-builder: check the existing intents and prefer updating a
new-user intent over a duplicate; mine recent new-hire tickets for users' phrasing and for the
follow-up questions techs had to ask, which become arguments; show the full spec plus a test plan
(5 should-match, 3-5 should-not, including an access-request near-miss), write only on explicit
confirmation, then report and recommend activation once the tests pass. Do NOT activate.

Spec:
- Triggers: "new hire starting", "new employee", "onboard a new user", "set up a new user", "new
  starter", "we hired someone", "need accounts for a new person", "new team member starting
  Monday", "add a user", "employee starting next week". Near-miss watch: "add a user to
  <distribution list>" belongs to the access-request intent.
- Arguments, the checklist: full name plus a personal or manager contact for credential delivery;
  start date (urgency and licensing timing); job title, department and manager (group memberships
  and mirroring); "model after" an existing user where the client works that way (<user>);
  equipment needed and work location; applications and licenses beyond the standard stack; who
  approved the hire, the authorization anchor.
- Reply flow: collect the arguments, confirm the full summary back to the requester, create the
  ticket with every field in a structured plain-text block, route it to the client's onboarding
  board or workflow, and reply with what happens next — the assigned technician confirms timelines;
  never promise a completion date.
- Handoff rule: account creation, licensing and hardware are always human or workflow actions; the
  intent only does intake. Asked for credentials in the conversation, it states they will be
  delivered through the client's secure method.
- Variations per client: extra checklist fields (badge access, LOB app seats), standard hardware
  bundles, whether "model after user" is allowed, the receiving board or flow.
- Success metric: first-touch completeness — new-hire tickets reaching a technician with zero
  follow-up questions. Deflection is not the goal.

Guardrails: never design replies that deliver credentials in the conversation. Do not invent the
client's standard hardware, license stack or onboarding turnaround — placeholder anything unknown
and flag it before activation. Every argument adds friction: keep the checklist to what the
workflow genuinely consumes. Field block in plain text, no markdown or emojis (apply the PSA Note
Discipline base skill).
```
