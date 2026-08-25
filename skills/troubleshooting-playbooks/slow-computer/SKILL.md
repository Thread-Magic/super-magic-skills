---
name: Slow Computer
description: Triage a slow-computer ticket via resource hogs, disk health, startup load, and profile weight, ending with reimage or replace decision criteria.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Slow Computer

**When to use:** A "<user>'s computer is slow" or "everything takes forever" ticket; slowness only at boot/login or only in one app; a device with recurring slowness complaints; or a call on whether a machine is worth more tuning versus reimage/replacement.

**Run it:** on the one device ticket you're working — a tech measures and works it hands-on; not unattended.

## Prompt

```
"Slow" is a measurement problem before it is a fix problem. Turn the complaint into
numbers, climb the causes cheapest-first, and be honest when the answer is reimage or
replace.

Climb the Troubleshooting Ladder base skill first: this device's and user's past tickets
— a third slowness ticket on the same machine goes straight to the exit criteria below,
not another lap of the ladder. Then the documented spec and age; if the RMM is
connected, read the device record for spec, OS, disk, and health, and its recent
activity for alerts, patches, or installs that line up with onset. Otherwise have the
tech gather it manually and note the gap.

Pin the shape of "slow" — never accept the adjective. When did it start? Always, or at
boot and login, or in one app, or on certain actions (slow only on files from a share
means the network, not the PC)? Get numbers: Task Manager CPU, memory, and disk
percentages during the slowness, plus the OS build and the app's version — a known-slow
release beats any endpoint tuning.

Then the rungs:
- Resource hogs. Task Manager sorted by CPU, memory, disk during the pain. One process
  pinned high names the fix: a runaway process, an AV scan schedule, 60 browser tabs, a
  sync client re-indexing. Two security agents scanning each other is a classic — check
  for double-installed AV/EDR.
- Disk health and pressure are two checks. Health: SMART status, and whether the system
  disk is a spinning HDD — on a modern OS that is itself the diagnosis, and the fix is
  an SSD, not tuning. SMART pre-failure means stop tuning and start the
  backup-and-replace path immediately, and say why. Pressure: a near-full system drive
  degrades everything.
- Startup load, for slow boot or login: startup apps, autostart services, and login-time
  policy, script, and drive-mapping delays — a timeout to a dead server stalls everyone.
- Profile weight: an oversized local profile, a desktop or Documents full of sync churn,
  a bloated browser profile.

The exit: recommend a reimage when no single cause survives the ladder, or there's
malware history or OS-corruption symptoms, and reimage effort with data preservation is
below cumulative tuning effort — by ticket three it always is. Recommend replacement
when the hardware floor is the cause (HDD, too little RAM for the standard workload, an
aged CPU) or the device is past the client's documented refresh age. Quantify it: "third
ticket, N hours spent" is the business case.

Never bulk-disable services or apply "optimizer" tools; target the measured cause only.
Before recommending anything be deleted, temp cleanup included, name exactly what goes.

Verify by re-measuring the original pain point — boot time, app-open time; a number, not
a vibe. Note it (apply the PSA Note Discipline base skill): shape of slow, rung
findings, action, before-and-after numbers, and any reimage or replace recommendation.
```
