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
One sick host is every guest's bad day. Read the alert, separate host-level causes from VM-level ones, and hand the tech a specific, ordered remediation. This needs the RMM connected; if the host is not RMM-managed (common for ESXi), say monitoring visibility is limited to docs + guest symptoms and route to the hypervisor console.

1. Confirm you are looking at a host: read the device details in the RMM and the documentation (IT Glue / Hudu) — hostname prefixes (HV/ESX/VMH) are hints, not facts (don't trust a class filter). From documentation, map the host's guests and storage (local, SAN/NAS, cluster shared volume); the guest map is the blast radius of everything that follows.
2. Read the alert family from the host's active alerts and its recent activity, then run the host-vs-VM split — the core judgment: all/most guests affected or host-level metrics (CPU ready/queueing, memory pressure, datastore latency) elevated -> host-level; one guest misbehaving while the host is comfortable -> VM-level, route as a normal server ticket for that guest (device-health-check / server-diagnostics) and say the host is exonerated with evidence.
3. Datastore/volume capacity — find what is consuming, usual suspects in order: snapshot/checkpoint sprawl (long-running snapshots grow unbounded — top emergency cause), orphaned VM disks from deleted VMs, thin-provisioned disks growing into overcommitted space, ISO/backup files parked on the datastore. A datastore at genuine risk of filling is an emergency (guests pause/crash at zero) — escalate priority on the ticket.
4. Snapshot sprawl: inventory snapshots/checkpoints by age and size (via the hypervisor console — a hands-on step to hand off with a deep link into the device in the RMM). Deleting/consolidating a large old snapshot generates heavy I/O and can take hours — it belongs in a window, not a business-hours panic click, unless the datastore is critically full and the risk trade flips; spell out that trade. Check ticket history for why the snapshot exists — a backup product's stuck snapshot points at the backup chain (backup-failure-triage), not manual cleanup.
5. Host resource pressure: check consolidation history (recent activity, ticket history) for recently added/resized guests; identify the noisy neighbor where guest metrics allow. Remediation ladder: rebalance/migrate guests, right-size overallocated VMs, then hardware. Host reboots are last-resort choreography — every guest gracefully handled first; never propose a host reboot with workstation-reboot casualness.
6. Output: host-vs-VM verdict with evidence, ranked cause hypothesis, remediation steps in order with window requirements, and the deep link. Reset the alert in the RMM only after a real action or verified condition change, with a plain-text note (no markdown/emojis) saying what was found and done. Chronic alerts get a root-cause ticket, not a weekly reset.

Guardrails: never recommend deleting snapshots, disks, or files without stating what they are and confirming the backup product is not mid-chain — deleting a backup's working snapshot corrupts the chain. Host reboots and storage migrations are change-window work with the full guest map; this integration cannot orchestrate them — hands-on handoff only. Do not reset a host alert to clear the board; resets without remediation are recorded as "reset, unresolved, recurrence expected". For "when does it fill", route to storage-capacity-planning.

Unattended (Flow) mode: entire reply posted verbatim as the plain-text note. Do the host-vs-VM split and cause ranking from tool evidence only; if evidence does not distinguish, state both possibilities and stop. Never reset alerts, never change priority beyond board rules, never recommend deletions unattended — findings and a recommended next assignment only. If the device cannot be confirmed as a hypervisor host, output that single line and nothing else.
```
