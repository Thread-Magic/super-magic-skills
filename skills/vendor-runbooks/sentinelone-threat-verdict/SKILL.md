---
name: SentinelOne Threat Verdict
description: Triage SentinelOne threat detections: read static vs behavioral engine verdicts, direct kill, quarantine, rollback, and hold on exclusion requests.
category: Vendor Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# SentinelOne Threat Verdict

**When to use:** A SentinelOne threat alert lands as a ticket (malicious/suspicious verdict, mitigation report); a tech asks whether to kill, quarantine, roll back, or disconnect a device in the S1 console; or a user or tech requests an exclusion because "S1 keeps blocking our app."

**Run it:** on the alert ticket.

## Prompt

```
Triage a SentinelOne threat detection. edr-detection-runbook owns the canon — verdict,
containment, scope; you add S1's engines, mitigation states, rollback, and exclusion discipline.
You have no S1 access: kill, quarantine, rollback, disconnect, and verdict changes are technician
actions you recommend and record with timestamps, never take or invent.

1. Parse the alert: threat name, path and hash; the engine — static AI (pre-execution, file-based)
   versus behavioral AI, meaning it ran; confidence (malicious or suspicious); the mitigation
   policy already applied — auto kill and quarantine under protect, alert-only under detect — and
   its status per action. A behavioral detection on an executed process is a different emergency
   from a static hit on a dormant file.

2. Get context: live device state in the RMM for role and assigned user, the activity timeline
   around the detection, and user corroboration on a verified channel — admin tools and installers
   are a large share of "suspicious" verdicts.

3. Read the mitigation honestly: kill or quarantine reported complete stops execution but rules
   out neither persistence nor siblings — check the storyline for what the process touched before
   it died. Detect-only or partial mitigation is live.

4. Direct the console actions:
   - Kill and quarantine — the default for a malicious verdict not yet fully mitigated.
   - Disconnect from network — for behavioral detections showing spread, C2, or hands-on-keyboard
     activity, before deep investigation.
   - Rollback (Windows, VSS-based) — for confirmed ransomware or file damage. It restores files,
     not credentials or persistence outside the storyline, and needs intact Volume Shadow Copies.
     Not absolution: the initial access vector and any persistence still need remediating, or the
     encryption comes back.
   - A deep link into the device in the RMM for hands-on work.

5. A false-positive verdict in the console is a closure decision needing the same corroboration as
   closing the ticket; never mark false positive to silence noise — that trains the desk to miss
   the real one. Credential-touching tooling in the storyline branches to
   compromised-account-containment for the signed-in user.

6. Exclusions get their own gate: an exclusion is a permanent blind spot, not a convenience.
   Require confirmed false-positive evidence; narrowest scope — hash or signed certificate over
   path, path over folder, never a whole drive or wildcard; a named approver, security lead or
   management rather than the requesting tech; and a review date. "It's annoying" is not a
   justification.

7. Note the decision, not just the action; classify per soc-classification-tree, client-facing
   wording factual (defensive-writing-standard). With no RMM, say device context was reduced. When
   in doubt, do nothing irreversible and escalate.
```
