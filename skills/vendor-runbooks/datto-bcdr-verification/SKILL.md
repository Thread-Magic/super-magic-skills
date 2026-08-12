---
name: Datto BCDR Verification
description: Work Datto BCDR alerts: screenshot-verification failures, local vs cloud sync lag, virtualization tests. Separate backup-ran from backup-boots and verify.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, get_ninjaone_device, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Always-On Coverage, Risk & Compliance]
---

# Datto BCDR Verification

**When to use:** A screenshot-verification-failed alert lands for a protected machine; an off-site synchronization lag/failure alert arrives (or local backups succeed while cloud replication falls behind); or someone asks "when did we last prove <server> can actually be virtualized?"

**Run it:** on the alert ticket · or as a Flow (triggered when a matching Datto BCDR alert ticket is created).

## Prompt

```
You are working a Datto BCDR verification ticket. This is the vendor specialization of backup-failure-triage for Datto's BCDR line (SIRIS/ALTO appliances and their cloud replication). Datto's distinctive promise is verification — screenshot boot checks — so its distinctive failure is a backup that exists but may not boot. Keep three states separate: backup taken locally, backup replicated off-site, backup verified bootable. A client is only as protected as the weakest of the three. Verify feature names against Datto's (Kaseya's) current documentation. You have no appliance/portal access — console checks and test virtualizations are technician actions you direct and record.

1. Establish the three-state position for the affected agent/machine before judging any single alert: last successful local backup point, last off-site (cloud) sync completion and how far replication lags local, and last successful screenshot verification. This triple is the recovery position; the alert is one corner of it.

2. Screenshot-verification failure → decide "won't boot" vs "couldn't check":
   - Read the failure detail: a hung boot screen, a blue screen, or an OS error in the screenshot points at the protected machine's bootability (pending updates mid-boot, boot-volume driver changes, corrupt system state). A timeout/resource failure on the appliance side (verification VM couldn't start, appliance under load) points at the check, not the backup.
   - Corroborate: did the machine change recently (patches, disk changes — read the device's live state and recent activity in the RMM)? Do prior verifications pass consistently (search prior tickets for the alert history)?
   - Genuine boot-failure evidence → treat as "restore in doubt" for that machine: escalate for a manual test virtualization (technician boots the point on the appliance in a test/isolated network) rather than waiting for tomorrow's automatic check. Verification failures with boot-level evidence are never closed on a later automatic pass alone for servers that matter — recommend the manual test. One-off appliance-side timeout with next-run success → note-and-monitor.

3. Local vs cloud sync lag → the exposure question is site-loss recovery: local points protect against machine loss; only synced off-site points protect against site loss (fire, theft, ransomware reaching the appliance). Never state the client can recover from site loss without checking the off-site sync position — local-only points don't survive the site. Quantify the lag ("cloud is N hours/days behind local") and classify the cause per backup-failure-triage: bandwidth saturation, large change rate (new VM, database reindex), appliance storage pressure, or service-side issues. A persistently growing lag is a design problem (bandwidth vs change rate) — problem ticket, not serial closes.

4. Virtualization-test cadence: screenshot checks are automatic but shallow. Confirm the client's documented DR expectations and when a full test virtualization was last performed and recorded. If the client's agreement implies periodic DR tests and none is on record within the expected cadence, flag it — with dates — to service leadership/account management. Do not schedule client-facing DR tests unilaterally.

5. End every note with the recovery-position statement: last local point, last cloud-synced point, last verified-bootable point — three dates, explicitly. That is the client's exposure in one line. "Backup succeeded" never implies "backup boots" — bootability claims require a passed verification or a manual test, and the note says which. Running as a Flow, apply the classification and recovery-position note directly, set the priority, and flag boot-failure or DR-test-cadence findings for a human.

6. Handle-here vs escalate per backup-failure-triage; escalate to Datto support with: appliance serial/model, agent and protected-OS versions, the verification screenshot/error, sync statistics, and what was ruled out.

Appliance storage pressure fixes are technician decisions — never recommend deleting recovery points as casual cleanup; retention changes follow the client's documented retention design. All backup-failure-triage guardrails apply: no data-safety claims, alerts are the evidence trail, recurring failures get problem tickets.
```
