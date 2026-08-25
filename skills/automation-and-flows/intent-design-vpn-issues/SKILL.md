---
name: VPN Issues Intent Design
description: Design the VPN connectivity intent: a short self-help ladder plus environment capture — client, location, error text — so escalations arrive diagnosable.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# VPN Issues Intent Design

**When to use:** "Build an intent for VPN problems" / "remote workers flood us with VPN tickets that say only 'VPN broken'" / Intent Mining ranked VPN/remote access as a top candidate.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a VPN intent that rules out the cheap causes — local internet, stale client, a simple
reconnect — and captures the environment so the ticket a tech receives is diagnosable at once.
Building intents is admin-only; if you can't, output the spec for an admin to apply.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate it;
ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5 near-misses
from the watch-outs below) and write only on explicit confirmation; do NOT activate — the admin
does that once the tests pass. Confirm from recent tickets' resolution notes which
rungs actually resolve here, harvest real error strings for the prompts, and link the knowledge
base's VPN articles.

Spec:
- Triggers: "VPN not working", "can't connect to VPN", "vpn wont connect", "VPN keeps
  disconnecting", "can't reach the server from home", "remote access not working",
  "VPN stuck on connecting", "can't get on the VPN". Watch-outs: "can't reach
  <website>" with no VPN context is general connectivity; "need VPN access" from someone who never
  had it is an access request, not a fault.
- Arguments, the environment capture: which VPN client (<application>); where they are — home,
  travel, office, public wifi (office plus VPN is its own smell); the exact error or behavior
  (stuck connecting, authenticates then drops, connects but reaches nothing); whether
  ordinary internet works now, ruling out the ISP; when it last worked and what changed (new
  laptop, password change, new router).
- Reply flow, the self-help ladder: (1) confirm local internet works — open any external site. If
  not, the fault is their connection or ISP: restart the router, contact the ISP, stop. (2)
  Full reconnect — quit the VPN client, relaunch, reconnect, completing any MFA prompt fresh. (3)
  Reboot to clear stuck adapters and tunnels, then retry once. Ask "connected now?" after each
  rung and close as deflected on success. (4) If the ladder fails, open a
  ticket carrying the environment capture and rungs tried.
- Handoff rule: never change VPN client settings, certificates or credentials in self-help.
  Authentication failures, especially after a recent password change, route to the human path:
  credentials are never resolved in chat, and the password-reset intent's verified flow may apply.
  Several users at once is a probable concentrator or tunnel issue — skip self-help, escalate
  immediately.
- Variations per client: VPN product name and reconnect steps, whether MFA is in the path, the
  status page or head-end to name, office-network exceptions.
- Success metric: deflection rate plus diagnostics completeness on escalated tickets.

Guardrails: do not invent the client's VPN product, status page or MFA setup; placeholder and flag
before activation. Environment capture on the ticket in plain text.
```
