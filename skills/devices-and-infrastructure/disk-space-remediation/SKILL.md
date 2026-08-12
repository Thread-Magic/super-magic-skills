---
name: Disk Space Remediation
description: Work a disk-pressure alert or "drive is full" ticket — establish likely consumers from RMM signals, give the tech a safe-cleanup sequence, and hand off via device deep link. Use when a low-disk alert fires or a user reports a full drive.
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
Turn a low-disk alert into an actionable brief: severity, likely consumers, a safe-cleanup order of operations, and a deep link — because the agent cannot run cleanup scripts itself. This needs the RMM connected; if absent, degrade to generic guidance + ticket history and say the live disk view is unavailable.

1. Resolve the device in the RMM (organization first, rank candidates by org match then last-contact — don't stop to ask mid-lookup, don't trust a class filter) and read its details for current volume numbers. Severity: under 5% or under 5 GB free on a system volume is act-now (services/updates start failing); under 15% is soon.
2. Read evidence without touching the machine: which volume is full (system vs data changes the playbook), the device's alerts for how long pressure has built (creep vs spike), the recent device activity for correlating events (failed patch run, backup writing locally, recent app install).
3. Check whether another tech is already on the device before proposing anything.
4. Infer likely consumers by device role (as hypotheses ranked by evidence, not findings): workstations — user profiles, downloads, OneDrive/cache bloat, shadow copies, Windows Update leftovers; servers — log growth (IIS/SQL/app), backup staging, WSUS/update caches, database files, shadow copies; sudden spikes — a runaway log or dump file.
5. Give the safe-cleanup sequence, decreasing safety: (a) empty recycle bins and temp/update caches via Disk Cleanup/Storage Sense; (b) clear stale user profiles per policy; (c) prune/archive app logs after confirming nothing needs them; (d) shrink shadow-copy allocation only with restore-point-impact understanding; (e) anything touching databases, backup chains, or app data is change-controlled — not cleanup. Never delete files you cannot identify; moving data beats deleting it.
6. Check the knowledge base for a client- or device-specific cleanup SOP and link it if one exists.
7. Hand the tech a deep link into the device in the RMM — remediation is hands-on tech work; this integration cannot execute scripts or deploy cleanup tools. Offer to leave the brief as a plain-text note (no markdown/emojis).
8. Close the loop: after the tech confirms cleanup, re-check the device details and report before/after free space. If pressure returns within days, recommend a root-cause/capacity ticket rather than repeat cleanup.

Guardrails: NO script execution, NO automated deletion — every destructive step is performed by the tech by hand, with the sequence above as guidance. Consumers are inferred, not observed (the RMM does not expose per-folder usage) — say so. On servers, anything beyond temp/log hygiene needs a maintenance window and user-impact confirmation. Recurring pressure is a capacity problem; do not present the third cleanup as a fix.

Unattended (Flow) mode: entire reply is the plain-text brief posted verbatim (severity, hypotheses labeled as hypotheses, safe-cleanup sequence, deep link). Device unresolvable or volume data unreadable -> output nothing. Another tech recently active -> lead with "TECH ALREADY ENGAGED - coordinate before acting". Repeat pressure in the lookback -> recommend a root-cause/capacity ticket. Permitted write: the note only — no script exec, no deletion, no device actions.
```
