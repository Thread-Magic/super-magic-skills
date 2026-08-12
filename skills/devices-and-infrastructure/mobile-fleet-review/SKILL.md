---
name: Mobile Fleet Review
description: Review phones and tablets under MDM — enrollment, OS version spread, compliance flags, and readiness to lock or wipe a lost or stolen device.
category: Devices & Infrastructure
tools: [liongard_launchpoint, liongard_query, liongard_metric, search_ninjaone_devices, search_itglue, search_hudu, add_ticket_note, create_ticket, send_approval]
connectors: [Liongard, NinjaOne, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Mobile Fleet Review

**When to use:** "Review <client>'s mobile fleet" / "are their phones and tablets compliant?", before enforcing a new mobile policy, or a lost/stolen phone ticket.

**Run it:** across a client's mobile fleet, on demand (not a Flow — it's a posture review, not a per-ticket event).

## Prompt

```
Posture review of a client's managed phones and tablets: who is enrolled, what OS versions are in the field, which are non-compliant or stale, and whether the desk could actually execute a remote lock/wipe if a device were reported lost today.

1. Establish the MDM source of truth. Mobile devices rarely live in the RMM: read enrollment data from the environment's posture in Liongard when enabled — verify the M365/Intune inspector exists and last ran successfully before trusting it, then read the enrollment data, stating dataprint age; check the RMM only to catch stragglers with a mobile agent; otherwise ask the requester for an MDM export. State which source you used and its as-of time.
2. Enrollment state: bucket into enrolled-and-compliant, enrolled-but-noncompliant, enrolled-but-stale (no check-in ~30+ days), and known-but-unenrolled (in docs or a user assignment list but absent from MDM). Stale devices are the silent risk — they will not receive a wipe command promptly.
3. OS version spread: tabulate iOS/iPadOS and Android versions. Flag versions no longer receiving vendor security updates — verify current support windows against vendor documentation rather than asserting from memory (Android support varies heavily by manufacturer).
4. Ownership model: note corporate-owned vs BYOD where the MDM or documentation distinguishes them. Wipe expectations differ — full wipe for corporate, account/container wipe for BYOD. Never assume BYOD devices can be fully wiped.
5. Lost-device readiness: for a sample (or the specific device in a lost-phone ticket), verify preconditions for remote lock/wipe — enrolled, recently checked in, supervised/corporate where full wipe is expected. Report readiness honestly: "a wipe command would reach N of M devices within an hour based on check-in recency."
6. Output: fleet summary table, non-compliance and staleness lists with recommended actions, and lost-device readiness verdict. Remote lock/wipe is not executable through these tools — hand off to the MDM console, and for an actual lost device recommend the desk get written client authorization first (route it for approval). Offer to open a ticket per remediation stream or leave a plain-text note (no markdown/emojis).

Guardrails: never present the fleet as complete unless it came from the MDM (via Liongard or export) — documentation-only device lists are candidates, not inventory. Wipe/lock/retire actions are never executed by this skill — they are MDM console actions requiring authorization, especially on BYOD where a full wipe may destroy personal data and create liability. For a lost/stolen device, confirm the reporter's identity through normal desk verification before recommending any destructive action; when in doubt, lock rather than wipe. If no MDM data source is available, say the mobile fleet cannot be verified — do not infer it from phone numbers in contact records.
```
