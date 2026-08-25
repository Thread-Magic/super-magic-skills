---
name: CrowdStrike Falcon Alerts
description: Triage CrowdStrike Falcon detections: parse detection anatomy, decide when Network Contain is warranted, and spot mass endpoint failures as vendor-side.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# CrowdStrike Falcon Alerts

**When to use:** A Falcon detection or incident arrives as a ticket (email connector, SIEM forward, or MDR escalation); a tech asks whether to network-contain a host or how to read a Falcon verdict; or many endpoints across one or more clients fail simultaneously and someone suspects the sensor or a content update.

**Run it:** on the alert ticket.

## Prompt

```
Triage a CrowdStrike Falcon alert. security-alert-response and edr-detection-runbook own the
investigation canon; you add Falcon's packaging and containment semantics. Containment,
status changes and RTR sessions are technician steps you direct and record.

1. Parse the alert: detection or incident (an incident groups detections — work the incident), severity, hostname and sensor ID, process tree or triggering hash, and the action-taken field (blocked/killed/quarantined versus
   detection-only). Copy Falcon's exact verdict language; "blocked" is a claim about one
   process — verify nothing executed before the block and scope-check the host before
   closing. Route the client per security-alert-response using hostname and tenant (CID);
   Falcon alerts often land on a shared intake mailbox, and low routing confidence means
   flag for a human, not reassign.

2. Contain per the edr-detection-runbook matrix: Network Contain isolates the host but keeps
   the Falcon cloud channel open, so the technician can investigate and lift it remotely.
   Cheap to apply and undo — on detect-only alerts for credential theft, hands-on-keyboard
   indicators or lateral-movement tooling, contain first, investigate second. Never lift
   Network Contain without a documented verdict and a named decision-maker.

3. Investigate per edr-detection-runbook: process lineage, persistence, what executed before
   blocking, other hosts with the same hash or indicator (prior tickets, ~90 days). Confirmed malicious with identity involvement branches to
   compromised-account-containment; ransomware behavior to ransomware-response.

4. Check for a vendor-caused mass failure: on 19 July 2024 a faulty Falcon content update
   caused mass Windows BSOD boot loops, not an attack. Many hosts failing or blue-screening across
   unrelated clients, tightly clustered in time with no preceding detections, points
   vendor-side — check CrowdStrike's status page BEFORE working it as a security incident. Then switch to outage response: a tracking ticket per
   client, the vendor's remediation bulletin followed exactly rather than improvised fixes, and communication per defensive-writing-standard without speculating
   until the vendor confirms. Rule out a content update before declaring a security
   incident, and an attack before declaring it vendor-side.

5. Note the decision: severity and verdict, containment state and who applied or lifted it.
   Classify per soc-classification-tree. Exclusions and IOC allowlisting
   are security decisions, never silent: narrowest scope (hash over path, path over folder),
   named approver, review date. Client-facing wording per defensive-writing-standard:
   never "you were hacked".

Sensor deployment scope may be unknown without documentation — say so, don't assume full
coverage. When in doubt do nothing irreversible and escalate.
```
