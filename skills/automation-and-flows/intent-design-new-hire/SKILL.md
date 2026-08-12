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
Build a new-hire intent whose whole job is complete intake: gather every checklist field in
one conversation so the onboarding ticket never bounces back with "what's their start date?".
This intent does NOT deflect — it makes the ticket dispatch-ready on arrival. Building intents
is admin-only; if you can't, degrade to a complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "new hire starting", "new employee",
  "onboard a new user", "set up a new user", "new starter", "we hired someone", "need
  accounts for a new person", "new team member starting Monday", "add a user", "employee
  starting next week". Near-miss watch: "add a user to <distribution list>" belongs to the
  access-request intent, not this one.
- Arguments (the checklist): full name + personal/manager contact for credential delivery;
  start date (drives urgency and licensing timing); job title / department / manager (drives
  group memberships and mirroring); "model after" existing user if the client works that way
  (<user>); equipment needed (laptop/desktop/phone) and work location; applications and
  licenses beyond the standard stack; who approved the hire (authorization anchor).
- Reply flow: collect the arguments; confirm the full summary back to the requester; create
  the ticket with every field in a structured plain-text block and route to the client's
  onboarding board/workflow; reply with what happens next and that the assigned technician
  will confirm timelines — do not promise a completion date.
- Handoff rule: account creation, licensing, and hardware are always human/workflow actions —
  the intent only performs intake. If the requester asks for credentials in-chat, state they
  will be delivered through the client's secure method.
- Variation hooks (per client): differing checklist fields (badge/door access, LOB app
  seats), standard hardware bundles, whether "model after user" is allowed, which board/flow
  receives the ticket.
- Success metric: first-touch completeness — percentage of new-hire tickets reaching a
  technician with zero follow-up questions. Deflection is not the goal here.

Steps:
1. List the existing intents — check for an existing new-user/onboarding intent; prefer
   updating over a duplicate.
2. Search recent new-hire tickets; mine users' phrasing (triggers) and the
   follow-up questions techs had to ask (those become arguments).
3. Draft the full spec (triggers, complete argument checklist, confirmation reply, routing
   target, variations) plus a test plan (5 should-match, 3–5 should-not, incl. an access-
   request near-miss). Show it before any write.
4. On explicit confirmation: create the intent, then set its variations.
5. Report what was created, restate the test plan, recommend activation only after tests pass.
   Do NOT activate.

Guardrails: never design replies that deliver credentials in the conversation. Do not invent
the client's standard hardware, license stack, or onboarding SLA — placeholder anything
unknown and flag it before activation. Every argument adds friction; keep the checklist to
what the onboarding workflow genuinely consumes, push rarely-used fields into a variation.
Confirm before any write; ticket field block in plain text (PSA-safe, no markdown).
```
