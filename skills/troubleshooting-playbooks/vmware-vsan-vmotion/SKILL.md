---
name: VMware vSAN and vMotion
description: Diagnose VMware vSphere: vSAN health warnings, resync storms, vMotion and DRS migration failures, datastore latency, and APD or PDL via vCenter events.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# VMware vSAN and vMotion

**When to use:** vSAN Skyline Health shows warnings/errors or the cluster is resyncing; vMotion / Storage vMotion fails or DRS won't balance or evacuate a host for maintenance; datastore latency spikes, VMs stunned, or an APD/PDL event; or a host is disconnected, not-responding, or won't enter maintenance mode.

**Run it:** on the one ticket you're working — a tech with vSphere access works it hands-on; not unattended.

## Prompt

```
Read vCenter's health checks before anyone evacuates a host — migrating VMs onto a
stressed cluster, or rebooting one mid-resync, turns a warning into an outage. esxcli
and PowerCLI steps are guidance for a tech; hypervisor management is not an RMM action.

Climb the Troubleshooting Ladder base skill first, topology as its top rung: vCenter and
ESXi build, storage model (vSAN vs SAN/NFS), the vSAN and vMotion VMkernel networks, and
the storage policy's FTT — failures to tolerate decides how many hosts can be down
safely, so establish it first. Then history: recent patching, a firmware or driver
change (vSAN is exquisitely sensitive to storage-controller firmware/driver mismatches),
a disk replacement, a network change.

Then read the actual failing check, never "vSAN is unhealthy": Skyline Health, resync
objects and ETA, disk-group and disk state; the task error and DRS faults panel for
migrations; per-datastore latency and APD/PDL events in vmkernel.log.

a. vSAN health or resync — Skyline Health names it: a failing capacity or cache disk, an
   HCL firmware/driver mismatch, a vSAN VMkernel network fault (MTU and jumbo-frame
   mismatches are classic), or object non-compliance. A resync is the cluster
   self-healing: don't reboot or evacuate during one, and NEVER take a second host down
   while it rebuilds from a first failure — that breaches FTT and loses data. Hardware,
   HCL, and firmware are the vendor's and storage owner's: package evidence, don't push
   firmware.

b. vMotion or Storage vMotion failure — read the error: vMotion network or MTU,
   insufficient target resources, CPU/EVC mismatch across host generations, a device the
   VM can't migrate with (mounted ISO, passthrough, USB, an affinity rule). A failed
   vMotion normally leaves the VM running on the source — confirm before retrying.
   Storage vMotion failures are usually target-datastore space or latency.

c. DRS won't balance, or a host won't enter maintenance mode — evacuation stalls when
   DRS can't place VMs (resource shortfall, anti-affinity, a VM pinned by a device) or,
   on vSAN, when data evacuation would breach availability. Never force "no data
   migration" maintenance mode on vSAN without understanding the availability impact.

d. Datastore latency, APD, or PDL — latency points at the backend (array, HBA or NIC,
   fabric, vSAN disk pressure). APD is paths temporarily gone, PDL the device
   permanently gone; PDL usually needs the device removed or replaced and affected VMs
   handled deliberately. Check multipathing and the physical path per host. SAN, fabric,
   and array faults are the storage owner's and the vendor's.

Success is vCenter's report: Skyline Health green or resync complete and objects
compliant, a clean test vMotion, latency at baseline. Note it (apply the PSA Note
Discipline base skill): build, FTT, evidence, branch, action, verification.
```
