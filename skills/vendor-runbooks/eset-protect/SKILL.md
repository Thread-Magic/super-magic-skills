---
name: ESET PROTECT
description: Triage ESET PROTECT detections by engine, interpret LiveGuard sandbox verdicts, and recognize when a protection-disabled alert is really a policy conflict.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# ESET PROTECT

**When to use:** An ESET detection, firewall/HIPS event, or protection-status alert arrives as a ticket; a user reports a file or download "stuck" or blocked and LiveGuard analysis is suspected; or a "protection disabled / product not activated / policy not applied" alarm needs triage — on ESET PROTECT cloud or on-prem console.

**Run it:** on the alert ticket.

## Prompt

```
Triage an ESET PROTECT alert — the vendor specialization of security-alert-response and
edr-detection-runbook. Two ESET traits matter: sandbox verdicts that hold files in limbo, and
policy merge order producing protection-status alarms that are configuration artifacts, not
attacks. Console actions are technician steps you direct and record.

1. Identify the layer that fired — it sets confidence: real-time/on-demand antimalware
   (signature plus ML, high confidence); HIPS (behavioral, more false-positive-prone with
   line-of-business software); network/web protection (a blocked URL or exploit attempt —
   something tried to reach a bad destination); ESET Inspect EDR detections, worked as
   correlated incidents. Parse the anatomy per security-vendor-generic and route per
   security-alert-response on the console's company/group context — multi-tenant consoles mix
   clients, so never route on name similarity.

2. LiveGuard Advanced submits unknown files to a cloud sandbox and blocks execution until a
   verdict returns. Malicious → a live detection per edr-detection-runbook; it reached the
   endpoint, so scope where else it landed. Suspicious → do not release; escalate for technician
   review with the sandbox report. Clean-but-held → the complaint resolves itself; note the
   delay window. Never release or exclude a file awaiting a pending analysis to unblock a user —
   waiting minutes is cheaper than releasing a payload.

3. Protection-status alarms: check for a policy conflict before assuming compromise or agent
   failure. ESET merges policies in order, so a later policy overriding an earlier one — or a
   local setting flagged against an applied policy — commonly produces "protection disabled",
   "settings not applied" or paused protection. Have the technician read the applied-policies
   list and effective settings before reinstalling agents or declaring tampering. Genuine tamper
   indicators — service killed, self-defense triggered, uninstall attempted — escalate as
   security events instead.

4. Cleaned or quarantined detections get a verification pass: "cleaned" covers the object, not
   the incident. Confirm in the console, scope siblings by hash, check persistence; identity
   involvement branches to compromised-account-containment. Detect-only means live — contain
   first; isolation, where licensed, is a technician action.

5. Note the layer, verdict, any policy conflict and decisions with approvers; classify per
   soc-classification-tree. Exclusions are security decisions — narrowest scope, named approver,
   review date — HIPS exclusions especially, since they blind the behavioral layer. Recurring
   policy-drift alarms feed security-noise-tuning; client-facing wording per
   defensive-writing-standard.

Without documentation the policy hierarchy is unknown; say so. When in doubt do nothing
irreversible and escalate.
```
