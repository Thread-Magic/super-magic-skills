---
name: EDR Detection Runbook
description: An EDR suspicious-process or malware detection alert landed — pull device context from the RMM, check what the EDR already contained, confirm with the device user, and escalate or close with evidence.
category: Security
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# EDR Detection Runbook

**When to use:** An EDR/AV detection ticket arrives (suspicious process, malware quarantined, exploit behavior blocked); a tech asks "is this EDR alert real or noise?"; or a detection storm needs per-device working.

**Run it:** on one ticket (an EDR detection).

## Prompt

```
Turn an EDR detection alert into a defensible verdict: device and user context first, the
EDR's own containment state second, human corroboration third — then close with an evidence
pack or escalate with the same. You cannot run scripts or deploy software through the RMM;
remediation beyond service/reboot actions is a technician handoff via the device deep link.
Work it in order:

1. Parse the detection: process name and path, file hash, command line if present, the
   EDR's own action (blocked, quarantined, or allowed/detected-only), device name, and
   logged-in user. "Allowed" and "blocked" are different emergencies.
2. Pull device context from the RMM: the device's role (server vs workstation — a server
   detection is automatically higher stakes), assigned user, online state, and recent
   activity around the detection time.
3. Read the quarantine state honestly: if the EDR blocked or quarantined the item, the
   immediate threat is likely contained but persistence and siblings are not ruled out. If
   the EDR only detected and the process ran, treat it as live until proven otherwise.
4. Contact the device user via a verified channel: "what were you doing on <device> at
   <time>?" Legitimate admin tools, installers, and IT scripts trigger a large share of
   detections — corroboration from the user or change/ticket history (search for
   maintenance on that device) is the difference between noise and signal.
5. Prior-context check: same detection, same client, last 90 days. A repeatedly-benign
   detection with the same explanation is a candidate for security-noise-tuning — but each
   occurrence still gets verified before closing.
6. Verdict:
   - Benign/expected (known tool, corroborated activity, EDR action consistent) → close
     with an evidence pack in the note: process, hash, device, user corroboration, EDR
     action, and reasoning.
   - Malicious or uncertain — especially anything that executed — → escalate: isolate the
     device in the EDR console, and hand the technician the device deep link for hands-on
     remediation. If credentials may have been exposed on the device, branch to
     compromised-account-containment for the signed-in user.
7. Document the decision, not just the action, and classify per soc-classification-tree.

Guardrails — always:
- "Blocked" is not "done" — check for sibling detections and persistence before closing;
  one blocked payload often has friends.
- Never close on assumption: an unrecognized process with no corroboration stays open even
  if the EDR blocked it. When in doubt, escalate — a false escalation is cheap, a missed
  compromise isn't.
- You cannot run scripts or deploy software through the RMM; remediation beyond
  service/reboot is a technician handoff via the device deep link.
- Degradation: no RMM connected → work from the alert body, ticket history, and user
  contact alone, and state the reduced device visibility in the note.
- Defensive writing for anything client-facing: "a detection was investigated and
  contained," never impact claims ahead of evidence. Never invent hashes or timestamps.
```
