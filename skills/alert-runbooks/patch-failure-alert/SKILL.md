---
name: Patch Failure Alert
description: Triage a patch-failure alert — separate a one-off from a repeat offender, detect reboot-pending as the usual culprit, correlate against the patch window.
category: Alert Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Patch Failure Alert

**When to use:** A "patch failed / update installation failed" alert opens a ticket; or a tech asks "why does <device> keep failing updates?"

**Run it:** on the alert ticket · or as a Flow that fires on the patch-failure alert ticket event.

## Prompt

```
Triage a patch-failure alert. Most fix themselves next cycle; a minority are the same patch
failing for the third month while the device drifts out of compliance.

1. Parse the alert: device, patch or KB identifier, error code, when the attempt ran. Keep the
   error code VERBATIM — it is the most diagnostic token here.

2. Check recurrence for this device over 30-90 days. The SAME patch failing repeatedly is a stuck
   patch — corrupt update cache, insufficient space, incompatibility. DIFFERENT patches failing
   each cycle is a systemic device problem: disk, component store, agent. A first failure is
   likely one-off. Sweep Honesty base skill: "at least N" if the search capped.

3. Check for a pending reboot, the most common cause: a pending-reboot flag, an
   installed-awaiting-restart event, or long uptime with recent patch activity. A device that
   hasn't rebooted since the last patch run often can't take the next. On a workstation the fix
   is a restart; on a server it needs a maintenance window.

4. Correlate with the patch window, then check self-heal. An attempt outside the designated
   window that failed because a user was active or the device slept mid-install is scheduling
   noise; look for that shutdown or sleep event. A later successful install of the same KB means
   self-healed.

5. Classify, then note it — plain text, no markdown or emojis (PSA Note Discipline base skill):
   verdict, error code, recurrence class, reboot-pending status, window correlation, route.
   Self-healed: close naming the successful install. Needs-tech (repeat same-patch failure,
   systemic multi-patch failure, disk-space or component errors): route with the error code,
   recurrence history and the RMM deep link; remediation is hands-on. Needs-client (client
   declined the reboot or excluded the device per the docs): account owner. Noise (shutdown or
   sleep outside the window, no repeat): close as a scheduling artifact; recommend a window
   review if it recurs.

Never call a device patched from an absence of alerts — report only install evidence. Don't
trigger reboots here; that goes through the reboot and maintenance workflows with their
confirmations. A security-critical patch failing repeatedly is an exposure: name the KB and how
long the device has been unpatched. If the patch engine runs outside the RMM, apply the Connector
Degradation base skill — say the view is partial and name the console to check.

As a Flow: your entire reply is the note. Close ONLY on evidence of a later successful install of
the same patch. Reboot-pending workstation: reboot-request queue. Reboot-pending server:
patch-window queue. Same patch with 2+ prior failures, or 3+ mixed failures in 90 days: tech
queue as stuck or systemic. Everything else: route as a one-off for next-cycle watch, do not
close. Unverifiable state or a capped search: route to a human, cap noted.
```
