---
name: Hypervisor Alert Triage
description: Triage Hyper-V and VMware host alerts — datastore capacity, snapshot sprawl, CPU/memory pressure — deciding if the issue is host-level or VM-level first.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, get_ninjaone_device_activities, get_ninjaone_device_link, reset_ninjaone_alert, search_itglue, search_hudu, search_tickets, add_ticket_note, create_ticket, update_ticket]
connectors: [NinjaOne, IT Glue, Hudu]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Hypervisor Alert Triage

**When to use:** A Hyper-V/VMware host raises a capacity/resource/health alert, several VMs on one client degrade at once, or a datastore is filling.

**Run it:** on one host/alert ticket · or as a Flow triggered when a hypervisor/host alert lands on the ticket.

## Prompt

```
Separate host-level causes from VM-level ones and hand over an ordered remediation.

1. Confirm it is a host from device details plus documentation (IT Glue / Hudu);
   HV/ESX/VMH prefixes and class filters are hints, not evidence. Not RMM-managed (common
   for ESXi) -> visibility is docs plus guest symptoms; route to the hypervisor console.
   Map its guests and storage (local, SAN/NAS, cluster shared volume) — the blast radius.

2. Read the alert family from active alerts and activity, then split host vs VM. Most
   guests affected, or host metrics elevated (CPU ready/queueing, memory pressure,
   datastore latency) -> host-level. One guest sick while the host is comfortable ->
   VM-level: route it as a normal server ticket (device-health-check), host exonerated.

3. Datastore capacity — find the consumer, in order: snapshot/checkpoint sprawl (grows
   unbounded; top emergency cause), orphaned disks from deleted VMs, thin-provisioned
   disks growing into overcommitted space, ISOs or backups parked there. Guests crash at
   zero free: a datastore at real risk of filling is an emergency — raise the priority.
   Inventory snapshots by age and size in the hypervisor console (hand off with a deep
   link into the device in the RMM): consolidating a large old snapshot drives heavy I/O
   for hours — window work, unless the datastore is critically full and the trade flips;
   spell that out. A stuck backup snapshot points at the backup chain
   (backup-failure-triage), not manual cleanup.

4. Host pressure: check activity and ticket history for guests recently added or resized,
   and name the noisy neighbour where metrics allow. Ladder: rebalance or migrate guests,
   right-size overallocated VMs, then hardware.

5. Output: verdict, ranked cause, ordered remediation with window requirements, and a note
   of what was found and done (apply the PSA Note Discipline base skill — plain text, no
   markdown or emojis). Reset the alert only after a real action or verified change;
   without one it reads "reset, unresolved, recurrence expected". A chronic alert gets a
   root-cause ticket, not a weekly reset.

Guardrails: never recommend deleting snapshots, disks, or files without saying what they
are and confirming the backup product is not mid-chain — deleting its working snapshot
corrupts the chain. Host reboots and storage migrations are change-window work needing the
full guest map and every guest handled gracefully; this integration cannot orchestrate
them — hands-on handoff only.

As a Flow: your entire reply posts verbatim as the note. Rank from tool evidence alone;
where it does not distinguish, state both and stop. Never reset alerts, never change
priority beyond board rules, never recommend deletions — findings and a next assignment
only. If the device is not confirmed a hypervisor host, output that line alone.
```
