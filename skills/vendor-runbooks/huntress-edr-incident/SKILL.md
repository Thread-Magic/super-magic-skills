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
Work a Huntress managed-EDR incident — the vendor specialization of edr-detection-runbook.
Huntress is analyst-reviewed: a human SOC analyst already judged the incident real, so the
question is not "is this noise?" but "what remains to be done?" You cannot run
scripts or deploy software through the RMM — portal actions (approve remediation, release
isolation, close the incident) are technician steps you direct, record, and never assume
happened without confirmation.

1. Parse the report: severity (Low/High/Critical), affected hostname, the finding class —
   footholds and persistence (autoruns, scheduled tasks, services, registry run keys) are
   Huntress's signature detection — indicators (paths, hashes, command lines), and the two
   action sections: what Huntress already executed (automated remediation, host isolation
   where the org has it enabled) and what awaits the technician (approve-to-run remediations
   and fully manual steps).

2. Trust the verdict, verify the scope: read the device's live state and recent activity
   timeline in the RMM for role (server detections are higher stakes), assigned user, and
   activity around the detection time.

3. Check isolation status. Isolated → immediate spread risk is handled, so plan remediation
   before release. Not isolated on a High or Critical incident → isolating it is the first
   technician action. Never release isolation to stop user
   complaints; the inconvenience is the containment working.

4. Finish the remainder: the technician approves the pending Huntress remediations in the
   portal, then works the manual steps — hand them a deep link into the device in the RMM. Never close on the automated actions alone while manual steps sit unchecked.

5. Check credential blast radius: a finding class implying credential access (infostealer,
   credential-dumping tooling, RDP foothold) branches to compromised-account-containment for
   the signed-in users — Huntress's endpoint remediation does not reset identities.

6. Verify before release or close. "Huntress remediated" covers the listed items only, and
   footholds come in sets: confirm the report's full checklist is complete, no new detections
   on the host, persistence locations rechecked. Release isolation only after that
   verification, and record who released it and when.

7. Escalate anything suggesting lateral movement or multiple hosts to the incident path, and
   check prior tickets for sibling reports on other devices at the same client.

8. Note the decision, not just the action: Huntress actions versus technician actions,
   timestamps, verification evidence. Classify per soc-classification-tree; client-facing
   wording per defensive-writing-standard.

With no RMM connected, work from the report body and ticket history and state the reduced
device visibility. When in doubt do nothing irreversible and escalate.
```
