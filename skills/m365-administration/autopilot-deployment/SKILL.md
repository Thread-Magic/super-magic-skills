---
name: Autopilot Deployment
description: Run Windows Autopilot deployments end-to-end: hardware hash registration, profile assignment, ESP behavior, and reset-vs-re-enroll decisions.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Autopilot Deployment

**When to use:** A ticket asks to register new laptops for Autopilot / import hardware hashes, a device boots to normal OOBE instead of the company-branded experience, the Enrollment Status Page is stuck or timing out, or someone asks "do we reset this device or re-enroll it?" after a failed deployment. Autopilot fails in three distinct phases — registration (the hash), targeting (the profile), and provisioning (the ESP) — and the fix is different in each. This skill diagnoses by phase and keeps "just wipe it" from becoming the default answer.

**Run it:** on one device — you diagnose by phase and make the reset/re-enroll call, a technician runs every Intune console action (not a Flow: it needs a human at the console).

## Prompt

```
Prepare an Autopilot diagnosis and plan. You diagnose by phase and make the reset-or-re-enroll
call; the tech runs every Intune console action. Never invent device or profile status.

1. Context. Check the client's documentation for their Autopilot standard: profile settings
   (user-driven or self-deploying, join type), device group logic, ESP config, hash source.
   Note it if IT Glue or Hudu isn't connected (Connector Degradation base skill). Read prior
   tickets.

2. Registration. Prefer OEM or partner registration. For manual capture the tech collects the
   hash (Get-WindowsAutopilotInfo or the client's documented HWID CSV path — verify current
   module versions) and imports it under Devices, Enrollment, Windows Autopilot. Confirm
   profile status reaches Assigned before shipping; never call a device ready at Pending.

3. Targeting. If a device skips the Autopilot experience: is the hash registered (serial
   lookup), did the device land in the Autopilot group (ZTDId-tag dynamic membership takes time
   to evaluate), and does exactly one deployment profile win for that group? Overlapping
   profiles with different join types are the usual cause.

4. ESP. The Enrollment Status Page runs device setup then account setup, blocking on the apps
   and policies it is told to. If it hangs, identify the phase and app from ESP details or the
   Intune troubleshooting pane. Usual causes: a required app failing or very large, a Win32 and
   line-of-business app mix, or an ESP timeout shorter than the real install. Fix the blocking
   app or trim the blocking-app list via the client's change process. Never lower ESP blocking
   tenant-wide for one device; that needs client sign-off.

5. Reset or re-enroll:
   - Config or app issue, device healthy: fix targeting, then sync or re-run.
   - Provisioning half-completed, no user data: wipe with reprovision intent (Autopilot Reset
     if it stays with the same tenant and user).
   - Device previously used, user data present: route through the device-wipe workflow and its
     approval gate, data-loss consequence stated plainly. An Autopilot redo is not exempt.
   - Hash never registered, or registered to the wrong tenant: correct the registration first,
     re-enrollment alone won't fix it. Never deregister a hash as cleanup without confirming
     the device isn't about to be redeployed — deregistration plus device deletion drops a
     machine out of management permanently.

6. Verify and note. Success: ESP completes, the user signs in, required apps present, device
   compliant. Leave a plain-text note, no markdown or emojis (PSA Note Discipline base skill):
   phase diagnosed, evidence, actions, serial, verification. Hashes and CSV exports are
   sensitive — reference by serial, never paste the hash blob.

When in doubt whether a device holds user data, do nothing destructive and escalate.
```
