---
name: M365 SaaS Backup
description: Work M365 and Google Workspace SaaS backup tickets: point-in-time restores, license and seat reconciliation, and job failures with authorization checks.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: both
flow: no
role: [Technician]
outcome: [Always-On Coverage, Risk & Compliance]
---

# M365 SaaS Backup

**When to use:** Someone asks to restore a mailbox, OneDrive/Drive files, SharePoint site, or Teams data "as of <date>"; protected-seat counts need reconciling against the tenant's actual users (a billing or coverage audit); or a SaaS-backup job failure or "unprotected user" alert lands.

**Run it:** on one restore/failure ticket · or across a client's protected-seat inventory as a reconciliation sweep.

## Prompt

```
Work a SaaS-backup ticket for a product protecting a Microsoft 365 or Google Workspace
tenant. Restores, exports and seat changes are technician actions you scope, authorize and
record — you never run them. Verify per-product specifics against the vendor's docs.

1. Restore requests — authorization first. A restore of anyone else's mailbox or files, including a departed
   employee's, needs the client's authorized approver on file; it is the client's
   data-access decision, not the desk's. Urgency does not waive authorization, and the
   request channel is not proof of identity. Record who authorized it.

2. Scope precisely: which objects, the point-in-time date, and the destination — in-place
   overwrites or merges with current data; alternate location or export does not. Never run or recommend an in-place restore without stating that
   consequence first; default to alternate location or export. Confirm a restore point
   exists at the requested date before promising anything — retention windows and when
   protection started bound what is recoverable. If the loss traces to
   deletion, ransomware or compromise, branch to compromised-account-containment or
   phishing-triage first so the restore does not mask evidence.

3. License reconciliation — pull three numbers: seats licensed with the backup vendor, users
   configured for protection, and current active users in the tenant (the technician exports
   that list). Active users NOT protected is the dangerous gap, usually new hires when
   auto-add is off: unrecoverable data accruing daily, so flag it loudly, not in a billing
   note. Protected accounts that no longer exist are ghosts you pay for, but check the
   client's retention intent before removing them — removing protection often deletes the
   backups. Licensed but unassigned seats are billing slack. Recommend
   auto-add where supported, align seats at the next billing cycle, and document
   departed-user retention decisions with the client's approver: retention first, seat
   cleanup second. Commercial changes go to account management.

4. Job failures and unprotected-object alerts follow backup-failure-triage: classify (token
   or consent expiry against the tenant is the SaaS classic — reconsent or fix the service
   account; API throttling; object-type limits), check recurrence in prior tickets, and end
   with the exposure statement: last successful backup per affected object.

5. Note it plainly, no markdown or emojis (apply the PSA Note Discipline base skill): for a
   restore: requester, authorization, scope, point-in-time, destination, result. For a
   reconciliation: the three numbers, gaps by count not names, recommendations with dates,
   any result cap. "Microsoft or Google keeps our data" is not a backup; a client
   declining SaaS backup is a documented decision through account management, not a triage
   argument.
```
