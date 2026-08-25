---
name: Synology NAS Alerts
description: Work Synology NAS alerts: degraded RAID or storage pool, disk-health warnings, full volumes, DSM updates. Treat a degraded array as near data loss.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Always-On Coverage, Risk & Compliance]
---

# Synology NAS Alerts

**When to use:** A "storage pool/volume degraded" or disk-failure alert lands for a client's Synology; SMART / disk-health warnings arrive (bad sectors increasing, reallocated sectors); or a volume-nearly-full alert or a DSM-update decision needs handling.

**Run it:** on the alert ticket · or as a Flow (triggered when a matching Synology alert ticket is created).

## Prompt

```
Work a Synology NAS alert (DSM alerts by email or RMM). Physical and DSM actions are
technician steps you direct and record. Verify DSM paths against Synology's docs;
never invent disk state, and never say data is safe during or after a rebuild — report array
status and last-backup facts only.

1. Parse the alert: device, affected pool or volume, alert class (degraded, disk failure,
   SMART warning, capacity, DSM update, security notice), drive slot if named. The client's
   documentation gives the RAID layout and workloads; a NAS holding their backups is a
   different emergency than a media share.

2. Degraded pool or failed disk is the priority path. State the redundancy position in the
   note; it drives the clock: one disk down leaves an SHR or RAID-5-class array surviving
   zero further failures, RAID-6 or SHR-2 one. Verify backups of the affected volumes FIRST,
   before any physical work; the rebuild is the highest-risk window for a second failure.
   No current backup → escalate the gap before touching drives and flag single-copy data;
   "the NAS is the backup" is itself a finding. For the technician: identify the failed
   drive by slot number AND serial in DSM Storage Manager, never by "the red light", and
   never direct a pull without both — pulling a healthy disk from a degraded array is
   unrecoverable total loss. Confirm the replacement meets size and type, replace one drive
   at a time, and monitor the rebuild.

3. SMART warnings on a healthy array are a pre-failure signal: check drive age and error
   trend (rising reallocated or pending sectors → replace proactively, same slot-and-serial
   discipline) and prior tickets for earlier warnings. Drives from one batch fail together —
   recommend staggered replacement and a problem ticket, not serial one-off closes.

4. Volume nearly full → find the consumer before adding space: snapshot retention, recycle
   bins, unbounded backup targets, or real growth. Cleanup follows the client's
   documented retention intent, never ad-hoc deletion; persistent growth goes to account
   management.

5. DSM updates reboot the unit: schedule inside the maintenance window with backups
   confirmed, never during business hours as housekeeping. Exposed NAS devices are actively
   targeted: a unit reachable by QuickConnect or port forwards and behind on security
   updates is a security finding, not hygiene.

6. Note the alert class, redundancy position, backup-verification result, what was directed
   versus done, and rebuild status; set the priority. Plain text, no markdown or emojis
   (apply the PSA Note Discipline base skill). As a Flow apply that note and priority
   directly, and flag any disk-replacement decision for a human.

Without documentation the RAID layout may be unknown — say so; the technician confirms in
DSM before anything physical. When in doubt escalate rather than act.
```
