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
Work a Datto BCDR ticket (SIRIS/ALTO appliances plus cloud replication) — the vendor
specialization of backup-failure-triage, which owns the classify-recur-decide loop. Keep
three states separate: taken locally, replicated off-site, verified bootable — the client is
only as protected as the weakest. Appliance checks and test virtualizations are technician
actions you direct and record; verify feature names against Datto's docs.

1. Establish the recovery position first: last successful local point, last off-site sync,
   last passed screenshot verification.

2. Screenshot-verification failure → "won't boot" or "couldn't check"? A hung boot screen,
   blue screen, or OS error in the screenshot points at bootability: pending updates
   mid-boot, boot-volume driver changes, corrupt system state. A timeout or resource failure
   on the appliance points at the check, not the backup. Corroborate with recent patches or
   disk changes (RMM activity timeline) and prior alert history. Boot-level
   evidence → "restore in doubt": escalate for a manual test virtualization in an isolated
   network, not the next automatic check; never close a server on a later
   automatic pass alone. A one-off appliance timeout with a successful next run is
   note-and-monitor.

3. Local versus cloud lag is the site-loss question: only synced off-site points survive
   fire, theft, or ransomware reaching the appliance. Never say the client can recover from
   site loss without checking the off-site position. Quantify the lag ("cloud is N hours
   behind local") and classify the cause per backup-failure-triage: bandwidth saturation,
   large change rate, appliance storage pressure, or a service-side issue. Persistent lag
   growth is a design problem — problem ticket, not serial closes.

4. Screenshot checks are shallow. Check the client's documented DR expectations and the last
   full test virtualization; nothing within the expected cadence → flag it with
   dates to service leadership and account management. Never schedule a client-facing DR
   test unilaterally.

5. End every note with those three dates, explicitly. "Backup succeeded" never implies
   "backup boots" — bootability needs a passed verification or a manual test, and the note
   says which. Plain text, no markdown or emojis (apply the PSA Note Discipline base skill).
   As a Flow, apply that note and priority directly and flag boot-failure or DR-cadence
   findings for a human.

Handle here or escalate per backup-failure-triage; the Datto support package is appliance
serial and model, agent and OS versions, the screenshot or error, sync statistics, and what
was ruled out. Never recommend deleting recovery points as cleanup; retention changes
follow the client's documented design. Generic guardrails hold: no data-safety claims,
alerts are the evidence trail, recurring failures get problem tickets.
```
