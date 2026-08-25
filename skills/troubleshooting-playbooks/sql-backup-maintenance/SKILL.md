---
name: SQL Backup and Maintenance
description: Fix SQL Server backup issues: runaway log growth, FULL vs SIMPLE recovery model, missing log backups, VSS conflicts, and broken point-in-time recovery.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# SQL Backup and Maintenance

**When to use:** The transaction log (.ldf) grew huge or filled the disk ("the log is full", error 9002); a maintenance plan or backup job is failing or backups aren't running as expected; "we can't restore to the point we needed" / point-in-time recovery isn't available; or backups conflict with a VSS/image/app backup and two products are fighting over the database.

**Run it:** on the one ticket you're working — a DBA/tech works it hands-on with the client on RPO decisions; not unattended.

## Prompt

```
Most "the log filled the disk" and "we can't restore to the right point" tickets have one
root: the recovery model and the backup regime don't match. A FULL database with no log
backups grows forever; a SIMPLE one cannot do point-in-time recovery whatever the backup
job claims.

Climb the Troubleshooting Ladder base skill first: documentation for the backup design —
each database's recovery model (FULL, SIMPLE, BULK_LOGGED), what performs backups (native
Agent plans, a scripted solution, an image/VSS product with application-aware SQL
processing, or several at once), the backup schedules, and the RPO the client believes
they have; then past tickets: a recovery-model change, a new backup product, or a restore
that failed for want of a log chain.

Read the state first: the recovery model in sys.databases; log_reuse_wait_desc, the one
value that names why the log won't clear (LOG_BACKUP, ACTIVE_TRANSACTION, REPLICATION);
and msdb..backupset for when a full, differential or log backup last succeeded.

1. Runaway log growth — LOG_BACKUP means the database is FULL and the log can't clear
   because log backups aren't running or are failing. Back up the log — that clears the
   space for reuse — then fix the job. Do not shrink the file, and do not switch to SIMPLE
   reflexively.

2. Recovery-model mismatch — the client expects point-in-time recovery but the database is
   SIMPLE, or FULL with a broken chain. Point-in-time needs FULL plus regular log backups
   in an unbroken chain. Say honestly what is recoverable now — only to the last full or
   differential — versus what the corrected regime gives.

3. Maintenance-plan or job failure — read the job history's step error: permissions, a
   missing folder, disk space, a dropped database in the plan, Agent stopped. Fix that
   step. A robust maintenance solution beats a fragile hand-built plan, but propose it,
   don't impose.

4. VSS and app-backup interplay — an image product taking copy-only backups that don't
   truncate, or two products both truncating and shredding each other's chains. Decide one
   owner of the log chain: either the image product does application-aware SQL processing
   with log handling, or native SQL takes the log backups, never both.

Never break the log chain to solve log growth: no switching to SIMPLE and back, no manual
truncation outside a backup, no routine .ldf shrink. Switching recovery model, or who owns
the backup, changes the client's recoverability: a design decision made with them against
their RPO, never a silent quick fix. Never imply a restore point the backup history
doesn't support.

Success is log_reuse_wait_desc back to NOTHING, the log stable after a successful log
backup, the job green, and an unbroken chain supporting the RPO. Note it (apply the PSA
Note Discipline base skill): recovery model, reuse-wait cause, backup history, branch,
action, verification.
```
