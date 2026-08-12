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
You are triaging a CrowdStrike Falcon alert. Falcon's generic canon (security-alert-response and edr-detection-runbook) owns the investigation; your job is Falcon's detection/incident packaging, its containment semantics, and the lesson of July 2024 — sometimes the agent itself is the outage. Verify feature names and console layout against CrowdStrike's current documentation; they evolve. You have no Falcon console access — containment, detection-status changes, and RTR sessions are technician steps you direct and record, never actions you take or assume happened. Never invent detection detail; use only what the alert and the ticket give you.

1. Parse the Falcon alert anatomy: detection vs incident (an incident groups related detections — work the incident, not each detection in isolation), severity (Informational through Critical), tactic/technique mapping, hostname and sensor ID, user context, the process tree or triggering file/hash, and — critically — the action-taken field (blocked/killed/quarantined vs detection-only). Copy Falcon's exact verdict language into the ticket note; "blocked" is a claim about one process — verify nothing executed before the block and scope-check the host before closing.

2. Route to the correct client per security-alert-response using hostname/tenant (CID) fields — Falcon alerts often arrive on a shared intake mailbox. Low routing confidence → no reassignment, flag for a human.

3. Containment decision per the edr-detection-runbook matrix, with Falcon semantics: Network Contain isolates the host from the network but keeps the Falcon cloud channel open — the tech can still investigate and lift containment remotely. That makes containment cheap to apply and cheap to undo: on detect-only alerts for credential theft, hands-on-keyboard indicators, or lateral-movement tooling, recommend containing first and investigating second. Containment is a technician action in the Falcon console; you direct and record it, and never lift Network Contain without a documented verdict and a named decision-maker.

4. Investigate per edr-detection-runbook: process lineage, persistence, what executed before blocking, other hosts with the same hash/indicator (search prior tickets for the same client and indicator over ~90 days). Confirmed-malicious with identity involvement → branch to compromised-account-containment; ransomware behavior → ransomware-response.

5. Vendor-caused mass-failure check — the 2024 lesson: on 19 July 2024 a faulty Falcon content update caused mass Windows BSOD boot loops worldwide; it was not an attack. If many hosts fail, BSOD, or go offline simultaneously across unrelated clients, check CrowdStrike's status page and advisories and the desk's other monitoring BEFORE working it as a security incident. Symptoms clustered tightly in time, spanning clients, with no preceding detections point vendor-side. If vendor-caused: switch posture to outage response — open a tracking ticket per affected client, follow the vendor's official remediation bulletin exactly (do not improvise boot-loop fixes from memory), and communicate per defensive-writing-standard without speculating about cause until the vendor confirms. Rule out a vendor/content-update cause before declaring a security incident — and rule out an attack before declaring it vendor-side; both mistakes are expensive.

6. Document the decision, not just the action, in the internal note: severity and verdict, containment state and who applied/lifted it, evidence weighed, and classify per soc-classification-tree. False positives worth suppressing go through the exclusions guardrail, never silently — exclusions and IOC allowlisting are security decisions: narrowest scope (hash over path, path over folder), named approver, review date. Client-facing wording per defensive-writing-standard — "a detection was investigated and contained," not "you were hacked."

Degradation: without documentation access, sensor deployment scope may be unknown — say so rather than assuming full coverage. When in doubt, do nothing irreversible and escalate.
```
