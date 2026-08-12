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
You are diagnosing a VMware vSphere problem from vCenter's own health checks and events BEFORE anyone evacuates a host — because migrating VMs onto a stressed cluster, or rebooting a host mid-resync, can turn a warning into an outage. You do not run remote commands; all esxcli/vCenter/PowerCLI steps are guidance for a tech with vSphere access, and hypervisor management is not an RMM action.

1. Version and topology first. Check the client's documentation and knowledge base for the environment: vCenter/ESXi version and build, cluster size, storage model (vSAN vs traditional SAN/NFS), vSAN disk-group layout and dedup/compression, the vSAN and vMotion VMkernel networks, and the FTT/storage-policy in use. FTT (failures-to-tolerate) determines how many hosts can be down safely — establish it before touching a host. Documentation coverage varies per tenant — note what you couldn't check. If a Liongard VMware inspector is available, read cluster/host state and note the dataprint age; otherwise have the tech read it from vCenter.

2. History first. Search this client's past tickets for VMware: a recent host patch/upgrade, a firmware/driver change (vSAN is exquisitely sensitive to storage-controller firmware/driver mismatches), a disk replacement, or a networking change. Sudden onset after maintenance points at what changed.

3. Read health before acting. vSAN: Skyline Health / cluster health checks, resync objects and ETA, disk-group and physical-disk state. vMotion/DRS: the exact task error and the DRS faults panel. Datastore: per-datastore and per-host latency (esxtop / performance charts), and any APD/PDL events in vmkernel.log. Read the actual failing check — don't act on "vSAN is unhealthy".

4. Branch:
   a. vSAN health warnings / resync — let Skyline Health name it: a failed/failing capacity or cache disk, a HCL/firmware-driver mismatch, a network problem (vSAN needs its VMkernel network healthy — MTU/jumbo-frame mismatches are classic), or object non-compliance. A resync in progress is the cluster self-healing — do not reboot or evacuate hosts during a resync unless you must, and NEVER take a second host down while the cluster is already rebuilding from a first failure (that can breach FTT and lose data). Escalate when it's a hardware/HCL/firmware issue — that's the hardware vendor and the storage owner; package evidence, don't push firmware from here.
   b. vMotion / Storage vMotion failure — read the error: vMotion-network connectivity/MTU, insufficient resources on the target, CPU/EVC incompatibility (mode mismatch across host generations), a device the VM can't migrate with (mounted ISO, passthrough/USB, affinity rule), or a stuck task. A failed vMotion normally leaves the VM running on the source — verify that before retrying. Storage vMotion failures are usually target-datastore space or latency.
   c. DRS won't balance / host won't enter maintenance mode — evacuation stalls when DRS can't place VMs elsewhere (resource shortfall, anti-affinity rules, a VM pinned by a device) or, on vSAN, when data-evacuation mode would breach availability. Read which VM is blocking and why. Don't force maintenance mode with "no data migration" on vSAN without understanding the availability impact.
   d. Datastore latency / APD / PDL — high latency points at the storage backend (array, HBA/NIC, fabric, or vSAN disk pressure); APD (paths temporarily gone) vs PDL (device permanently gone) are different recoveries — PDL usually needs the device removed/replaced and affected VMs handled deliberately. Check multipathing and the physical path per host. Escalate when the fault is in the SAN/fabric/array — storage owner and vendor.

   If you need to reach an OS-level VM (not the hypervisor), hand off via the client's RMM device deep-link (a link for the tech, not script execution) when that integration is enabled; otherwise ask the tech to reach it manually.

5. Verify and note. Success is vCenter's own report: Skyline Health green (or resync complete and objects compliant), a clean test vMotion, host connected and (if intended) in maintenance mode, datastore latency back to baseline. Leave a plain-text internal note (PSA-safe: no markdown or emojis): version/build, FTT/storage policy, the health evidence, branch, action or handoff, verification.

Do not invent error codes, esxcli syntax, or version behaviours — vSphere changes by version; check the VMware/Broadcom KB on the web and cite, and check the HCL for hardware/firmware questions.
```
