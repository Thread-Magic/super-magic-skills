---
name: Webroot Legacy AV
description: Work Webroot or other legacy signature-AV detections with thin telemetry, and frame the modern-EDR migration conversation on facts, not fear.
category: Vendor Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Webroot Legacy AV

**When to use:** A Webroot / legacy AV detection or infection alert lands as a ticket; a "threat removed" alert needs a close-or-investigate decision; or a tech or AM asks how to position an EDR upgrade for a client still on legacy AV.

**Run it:** on the alert ticket.

## Prompt

```
Handle a legacy signature-based AV alert — written around Webroot (SecureAnywhere-era
deployments still common in MSP fleets) but applicable to any thin-telemetry AV. Two jobs:
handle the detection safely despite limited visibility, and handle the product's limits
professionally — migration-to-EDR is an account-management motion built on documented gaps, not
a scare pitch off one alert. Hands-on inspection is a technician handoff via a deep link into
the device.

1. Parse what the alert gives you — and note what it doesn't: typically threat name, file path,
   action taken (quarantined, removed, blocked) and device, with no process tree, no command
   line, no storyline. Record the visibility gap; it sets the confidence ceiling on every
   verdict below.

2. Compensate with the RMM per edr-detection-runbook: the device's live state for role and user,
   its activity timeline around the detection, and user corroboration on a verified channel.
   With thin telemetry, the RMM and the human are most of the evidence.

3. Verdict at a raised bar. A "removed" verdict on a commodity threat with corroborated benign
   context can close with evidence. Anything ambiguous — repeated detections, threats in system
   paths, signs the payload executed, credential-stealer families — cannot reach a confident
   verdict on signature-AV telemetry alone: escalate for hands-on inspection via a deep link
   into the device, and consider a second-opinion scan. Credential-exposure families branch to
   compromised-account-containment for signed-in users. "The AV says removed" never substitutes
   for scope verification on anything non-commodity.

4. Check recurrence in prior tickets (device plus threat family, ~90 days): repeated "removed"
   alerts for the same family mean removal isn't sticking — persistence the AV cannot see. That
   is a problem ticket and an escalation, never a serial close.

5. Migration framing, when the client or account manager asks or a case exposes the gap: state
   facts, not fear — what the incident showed ("the product reported removal but could not show
   what the process did, so we could not verify scope without hands-on work"), what modern EDR
   would have added (execution history, isolation, rollback), and route the commercial
   conversation to account management. Never tell a client their product "doesn't work" — it
   worked as designed; the design is the limit. Do not claim the product missed something
   without evidence it did: absence of telemetry is a visibility statement, not a miss
   statement. The buy decision is the client's.

6. Note the verdict, its confidence, and the stated visibility gaps; classify per
   soc-classification-tree. Client-facing wording per defensive-writing-standard.

With no RMM, the evidence base is the alert plus the user — say so. When in doubt do nothing
irreversible and escalate.
```
