---
name: Huntress EDR Incident
description: Work Huntress EDR incident reports: foothold, persistence, or active endpoint threats. Read what Huntress isolated, finish remediation, and verify closure.
category: Vendor Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Huntress EDR Incident

**When to use:** A Huntress incident report lands as a ticket (foothold, persistence mechanism, malicious process, ransomware canary); a Huntress-isolated host needs follow-up and release; or a tech asks what to do with the "assisted remediation" steps in a Huntress report.

**Run it:** on the incident ticket.

## Prompt

```
You are working a Huntress managed-EDR incident — a vendor specialization of edr-detection-runbook. Huntress is analyst-reviewed: an incident report means a human SOC analyst already judged it real, which changes the default posture from "is this noise?" to "what remains to be done?" You cannot run scripts, deploy software, or push through the RMM — portal actions (approve remediation, release isolation, close incident) are technician steps you direct, record, and never assume happened without confirmation; hand the tech a deep link into the device in the RMM for hands-on work. Never invent data; verify report structure and portal actions against Huntress's current documentation.

1. Parse the incident report anatomy: severity (Low/High/Critical), affected hostname, the finding class — footholds/persistence (autoruns, scheduled tasks, services, registry run keys) are Huntress's signature detection — indicators (paths, hashes, command lines), and the two action sections: what Huntress already executed (automated remediation, host isolation if enabled for the org) and the remediation steps awaiting the technician (approve-to-run remediations and fully manual steps).

2. Trust the verdict, verify the scope: because a Huntress analyst reviewed it, do not burn time re-litigating "is it real?" — spend it on scope instead. Read the device's live state and its recent activity timeline in the RMM for role (server detections are higher stakes), assigned user, and activity around the detection time.

3. Isolation status check: the report states whether the host was isolated. If isolated → the immediate spread risk is handled; plan remediation before release. If NOT isolated on a High/Critical incident → isolating it is the first technician action, before investigation continues. Never release host isolation to stop user complaints — the inconvenience is the containment working.

4. Execute the remainder: approve pending Huntress remediations in the portal (technician action), then work the manual steps in order. Hand the technician a deep link into the device in the RMM for hands-on work — the agent cannot run scripts or deploy software through the RMM. Never close on the automated actions alone when manual steps remain unchecked in the report.

5. Credential blast-radius: if the finding class implies credential access (infostealer, credential-dumping tooling, RDP foothold), branch to compromised-account-containment for the signed-in user(s) — Huntress's endpoint remediation does not reset identities.

6. Verify before release/close: "Huntress remediated" covers the listed items only — footholds come in sets, so confirm the report's full checklist is complete. Remediation steps marked complete in the Huntress portal, no new detections on the host, persistence locations rechecked. Release isolation only after that verification, and record who released it and when.

7. Anything suggesting lateral movement or multiple hosts → escalate to the incident path, not per-ticket working; check for sibling reports on other devices at the same client (search prior tickets).

8. Document the decision, not just the action, in the internal note — Huntress actions vs technician actions, timestamps, verification evidence — and classify per soc-classification-tree. Client-facing wording follows the defensive-writing-standard.

Degradation: no RMM connected → work from the report body and ticket history; state the reduced device visibility in the note. When in doubt, do nothing irreversible and escalate.
```
