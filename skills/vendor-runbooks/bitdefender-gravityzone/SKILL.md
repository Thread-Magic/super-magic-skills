---
name: Bitdefender GravityZone
description: Triage Bitdefender GravityZone alerts: identify the detection layer (AV, ATC, HyperDetect, EDR) and use Risk Analytics, quarantine, and rollback safely.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Bitdefender GravityZone

**When to use:** A GravityZone detection, EDR incident, or ransomware-mitigation alert arrives as a ticket; a tech asks what an ATC or HyperDetect event means, or whether to restore a quarantined file; or a Risk Analytics report or risk-score item needs turning into desk work.

**Run it:** on the alert ticket.

## Prompt

```
Triage a Bitdefender GravityZone alert in the MSP multi-tenant console — the vendor
specialization of security-alert-response and edr-detection-runbook. Which layer fired changes
the triage; isolation, quarantine and policy changes are technician steps you direct and record.

1. Identify the layer — it sets the confidence baseline: on-access/on-demand antimalware
   (signature or cloud verdict, high confidence, usually auto-remediated); Advanced Threat
   Control (behavioral, mid-confidence, false-positive-prone on niche apps); HyperDetect
   (tunable pre-execution ML — sensitivity is a policy choice, so an aggressive-setting hit is
   weaker evidence than a signature hit); Network Attack Defense (exploit or lateral movement
   over the wire); EDR incidents (correlated graphs — work as incidents, not single alerts).

2. Parse the anatomy per security-vendor-generic: endpoint, user, detection name, file path and
   hash, and the action taken — disinfected, quarantined, blocked or reported-only. Report-only
   modes make the console look like it acted when it didn't — always read the action field.
   Route per security-alert-response — the console mixes tenants, so confirm the company/site
   field.

3. Contain per edr-detection-runbook: auto-remediated and verifiable → verify in the console,
   then scope calmly. Reported-only or detection mode (common during policy rollout) → treat as
   live and contain first. GravityZone endpoint isolation, where licensed, is the containment
   tool.

4. Quarantine restore is for confirmed false positives only, at the evidence bar of dismissing
   an alert, plus a proper exclusion decision: narrowest scope, named approver, review date.
   Never restore on user say-so — "we need that file" is a business fact, not a benign verdict.
   Ransomware Mitigation's file restore (tamper-proof copies taken at attack time) aids
   remediation after a confirmed ransomware verdict — branch to ransomware-response first;
   rollback does not replace scoping the intrusion.

5. Risk Analytics items — misconfigurations, vulnerable apps, risky behaviors — are posture
   findings, not incidents: batch them into a remediation ticket per client with risk score and
   affected endpoints. Recurring noise feeds security-noise-tuning; a HyperDetect or ATC hit
   dismissed as false positive still needs its exclusion recorded and reviewed — silent
   exceptions rot.

6. Note the layer, verdict, evidence weighed, and containment or restore decisions with
   approver; classify per soc-classification-tree. "Disinfected" covers the file, not the
   incident — scope persistence, siblings by hash and identity exposure before closing.
   Client-facing wording per defensive-writing-standard.

Without documentation, policy sensitivity is unknown — say HyperDetect confidence can't be
calibrated. When in doubt do nothing irreversible and escalate.
```
