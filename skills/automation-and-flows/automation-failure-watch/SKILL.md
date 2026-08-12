---
name: Automation Failure Watch
description: Detect automation-error signatures in notes — 4xx/5xx bodies, Jinja errors, webhook failures — flag the ticket and ping Teams so broken flows get noticed.
category: Automation & Flows
tools: [search_tickets, add_ticket_note]
connectors: [Zapier: Microsoft Teams]
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Automation Failure Watch

**When to use:** Flows or integrations occasionally dump error bodies into ticket notes and nobody watches for them; "alert us when an automation errors out on a ticket"; catching template/rendering failures (unrendered `{{ }}` tokens, Jinja errors) before they ship to a client. Fires on the NOTE-ADDED event (the error note landing) — not a timer.

**Run it:** on one ticket · or as a Flow (triggered when a note is added).

## Prompt

```
Broken automations fail quietly — an error lands in a note and the ticket looks normal.
Recognize the error signatures, flag the ticket, and ping the team's Teams channel so
someone fixes the flow. (A Flow cannot natively send a Teams message; it hands off to a skill
run, and you send it through the Zapier Teams action.)

Your entire reply is the internal flag note, verbatim: either `AUTOMATION FAILURE FLAGGED.
Signature: <sig>. Teams: <channel | skipped-unavailable>.` or `NO ACTION.`

1. Read the triggering note. Check it against the desk's configured
   automation-error signatures: HTTP 4xx/5xx status lines with response bodies,
   Jinja/template rendering errors, unrendered {{ ... }} or {% ... %} tokens, "webhook
   failed", stack-trace fragments, connector auth failures. NO signature match -> stop. This
   skill never fires on ordinary notes — a note that merely mentions "error" in prose is not
   a match. If unsure whether a note is a real automation failure, it isn't.

2. Leave a plain-text internal note flagging the failure: which signature
   matched and the error excerpt (this doubles as the dedupe marker). If a failure-flag note
   for this same error already exists on the ticket, do not ping again.

3. Resolve the correct Teams channel from the desk's documented automation-alert channel
   mapping (a broad flow failure and a single-client integration may go to different channels).

4. Send a compact message via the Zapier "Microsoft Teams -> Send Channel Message" action:
   ticket reference, client, matched signature, error excerpt — enough for an engineer to
   triage without opening every ticket. NEVER quote credentials or tokens from an error body
   into the Teams message — redact them.

Member-connected connector: the Teams Zapier action runs as the member who connected it —
prefer a service member's connection for Flow use, and open with the verify-first gate (the
member must have Zapier connected and Teams authenticated). Each Teams message consumes Zapier
task budget; signature-gating protects it — warn the desk if a signature is so broad it would
fire constantly. Degradation: if the Teams action is unavailable (not connected, budget
exhausted), still post the internal flag note so the failure is visible in-app, and say the
ping was skipped. Notes plain text (PSA compatibility).
```
