---
name: Disk Space Remediation
description: Work a disk-pressure alert or full-drive ticket — identify likely consumers from RMM signals and give the tech a safe cleanup sequence with a device link.
category: Devices & Infrastructure
tools: [get_ninjaone_device, search_ninjaone_devices, list_ninjaone_alerts, get_ninjaone_device_activities, get_ninjaone_device_link, search_knowledge_base, add_ticket_note]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Disk Space Remediation

**When to use:** A disk-space alert lands, "<user>'s C: drive is full", or "server <device> is at 98% on D:".

**Run it:** on one device/disk ticket · or as a Flow triggered when a disk-space alert lands on the ticket.

## Prompt

```
Turn a low-disk alert into a brief: severity, likely consumers, a safe-cleanup order, and
a deep link. With no RMM connected, degrade to generic guidance plus ticket history and
say the live disk view is unavailable.

1. Resolve the device in the RMM (organization first, ranking by org match then
   last-contact; don't stop to ask mid-lookup) and read its details for volume numbers.
   Severity: under 5% or under 5 GB free on a system volume is act-now (services and
   updates start failing); under 15% is soon.

2. Read evidence without touching the machine: which volume is full (system vs data
   changes the playbook), alerts for how long pressure has built (creep vs spike), recent
   activity for correlating events (failed patch run, backup writing locally, recent app
   install). Check whether another tech is already on the device.

3. Infer likely consumers by device role — hypotheses ranked by evidence, not findings.
   Workstations: user profiles, downloads, OneDrive cache bloat, shadow copies, Windows
   Update leftovers. Servers: log growth (IIS/SQL/app), backup staging, WSUS and update
   caches, database files, shadow copies. A sudden spike: runaway log or dump file.

4. Safe-cleanup sequence, decreasing safety: (a) empty recycle bins and temp/update caches
   via Disk Cleanup or Storage Sense; (b) clear stale user profiles per policy; (c) prune
   or archive app logs after confirming nothing needs them; (d) shrink shadow-copy
   allocation only with the restore-point impact understood; (e) anything touching
   databases, backup chains, or app data is change-controlled, not cleanup. Never delete a
   file you cannot identify — moving data beats deleting it.

5. Link any client- or device-specific cleanup SOP from the knowledge base, and hand the
   tech a deep link into the device in the RMM; remediation is hands-on. Offer the brief
   as a note (apply the PSA Note Discipline base skill — plain text, no markdown or
   emojis).

6. After the tech confirms cleanup, re-read the details and report before/after free
   space. Pressure returning within days is a root-cause/capacity ticket, not a repeat
   cleanup.

Guardrails: no script execution, no automated deletion — every destructive step is the
tech's, by hand. Consumers are inferred, not observed (the RMM does not expose per-folder
usage): say so. On servers, anything beyond temp and log hygiene needs a maintenance
window and user-impact confirmation. Never present the third cleanup as a fix.

As a Flow: your entire reply is the brief, posted verbatim — severity, hypotheses labelled
as such, safe-cleanup sequence, deep link. Device unresolvable or volume data unreadable
-> output nothing. Another tech recently active -> lead with "TECH ALREADY ENGAGED -
coordinate before acting". The note is the only permitted write: no script execution, no
deletion, no device actions.
```
