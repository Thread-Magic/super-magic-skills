---
name: Intune Enrollment Troubleshooting
description: Diagnose Windows Intune enrollment failures via a fixed ladder: user licensing, MDM scope, device state, and Entra join type checks.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Intune Enrollment Troubleshooting

**When to use:** A Windows device won't enroll in Intune — "<user>'s new laptop isn't appearing in Intune," "enrollment failed" with an 0x8018xxxx error, auto-enrollment configured but devices only ever show as Entra-registered, or one client's devices all stopped enrolling this week (tenant-side suspect). Enrollment failures are almost always one of four things and fail in a predictable order — walk the ladder top-down, do not reimage first. Mobile (iOS/Android) enrollment and lost-device flows belong to the mobile-device-mdm playbook; this skill is the Windows/Intune ladder.

**Run it:** on one device — you prepare the diagnosis and checklist, a technician executes all console changes (not a Flow: it needs a human at the console).

## Prompt

```
Diagnose an Intune enrollment failure for a technician to fix in one pass. You prepare the
diagnosis; the tech makes every console change. Never present a recommendation as a completed
change.

Climb the Troubleshooting Ladder base skill first: prior tickets for this device, user and
client — several failing since the same date is one tenant-side cause (MDM scope change,
licensing lapse, expired enrollment cert) — then the client's documentation for the enrollment
standard: Autopilot or manual, hybrid or cloud-only, expected join type, restrictions in force.
Note it if IT Glue or Hudu isn't connected (Connector Degradation base skill).

1. Capture the exact error: the device's Access work or school account Info pane, Event Viewer
   under DeviceManagement-Enterprise-Diagnostics-Provider, or the Intune enrollment failures
   report. Look the code up against Microsoft's current list, don't paraphrase.

2. Rung 1, licensing. Verify the user holds an Intune-inclusive license (Intune Plan 1, EMS,
   Business Premium), assigned and not merely purchased. Classic symptom: 0x80180018.

3. Rung 2, MDM user scope. In Entra, Mobility, Microsoft Intune, confirm MDM user scope covers
   this user (Some: check group membership; None breaks everyone). MAM user scope taking
   precedence over MDM scope for the same user is a classic silent failure: the device
   registers but never enrolls.

4. Rung 3, device state. Check for a stale or duplicate record for the same hardware (often
   deleted before re-enrolling), device-limit restrictions and the Entra device cap
   (0x801c0003), and enrollment restrictions blocking the platform or personal ownership
   (0x80180014); route a firing restriction to the restrictions workflow, don't work around it.
   Before deleting a stale record the tech confirms by serial that it maps to the device in
   hand, and notes what was deleted.

5. Rung 4, join type. Run dsregcmd /status. Auto-enrollment needs Entra joined or hybrid
   joined; Entra registered is not enough. Hybrid join failures trace to Entra Connect sync
   scope, the SCP, or the auto-enrollment GPO ("Enable automatic MDM enrollment using default
   Azure AD credentials", set to user credential). Fix the join before retrying.

6. Verify and note. Success is the device visible in Intune, checking in, with profiles
   delivered. Leave a plain-text note, no markdown or emojis (PSA Note Discipline base skill):
   error code, rung that failed, evidence, what the tech changed, verification, plus other
   devices to retry if the cause was tenant-side.

No wipe, reset or reimage as a troubleshooting step; resets go through the device-wipe workflow
and its approval gate. Never widen MDM user scope or lift an enrollment restriction to make one
device work — both change the whole tenant and need the client's documented change approval.
When in doubt, do nothing and escalate.
```
