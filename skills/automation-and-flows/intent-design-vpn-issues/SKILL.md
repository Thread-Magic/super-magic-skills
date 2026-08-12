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
Build a VPN intent that rules out the cheap causes (local internet, stale client, simple
reconnect) and captures the environment — VPN client, user location, exact error — so the
ticket a tech receives is immediately diagnosable. Building intents is admin-only; if you
can't, output the complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "VPN not working", "can't connect to VPN",
  "vpn wont connect", "VPN keeps disconnecting", "VPN error", "can't reach the server from
  home", "remote access not working", "VPN stuck on connecting", "vpn down", "can't get on
  the VPN". Near-miss watch: "can't reach <website>" without VPN context is general
  connectivity; "need VPN access" (never had it) is an access request, not a fault.
- Arguments (environment capture): which VPN client/app (<application>, pin per client in
  variations); where they are (home / travel / office / public wifi — office + VPN is its own
  smell); exact error/behavior (stuck connecting, authenticates then drops, connects but can't
  reach resources); does regular internet work right now (rules out the ISP); when it last
  worked and what changed (new laptop, password change, new router).
- Reply flow (self-help ladder): (1) confirm local internet works — open any external site;
  if not, it's their connection/ISP: give "restart router, contact ISP" guidance and stop;
  (2) full reconnect — quit the VPN client completely, relaunch, reconnect; complete any MFA
  prompt fresh; (3) reboot the computer — clears stuck adapters/tunnels, retry once. After
  each rung: "connected now?" — stop and close as deflected on success. (4) if the ladder
  fails, or the error is authentication-related after a recent password change, or several
  users report it -> create a ticket carrying the full environment capture and rungs
  attempted. Multiple users affected = probable concentrator/tunnel issue, skip self-help.
- Handoff rule: never walk a user through changing VPN client settings, certificates, or
  credentials in self-help. Authentication failures route to the human path (may need the
  password-reset intent's verified flow — never resolve credentials in chat).
- Variation hooks (per client): VPN product name and reconnect steps, whether MFA is in the
  path, known-good status page/head-end to mention, office-network exceptions.
- Success metric: deflection rate on VPN conversations plus diagnostics completeness (client +
  location + error text on escalated tickets).

Steps:
1. List the existing intents — check for an existing VPN/remote-access intent; prefer updating.
2. Search recent VPN tickets; confirm from resolution notes which rungs actually
   resolve on this desk, and harvest real error strings for the capture prompts.
3. Search the knowledge base for VPN setup/troubleshooting articles; link where they exist.
4. Draft the full spec (triggers, environment-capture arguments, ladder with stop conditions,
   escalation block, variations) plus a test plan (5 should-match, 3–5 should-not: new-access
   request and generic-internet near-misses). Show before any write.
5. On explicit confirmation: create the intent, then set its variations.
6. Report what was created, restate the test plan, recommend activation after tests pass. Do
   NOT activate.

Guardrails: no credential, certificate, or client-settings changes in self-help —
authentication problems hand off to the verified human path. Multiple users affected always
escalates immediately; do not loop a probable outage through self-help. Do not invent the
client's VPN product, status page, or MFA setup; placeholder and flag before activation.
Confirm before any write; environment capture in plain text on the ticket.
```
