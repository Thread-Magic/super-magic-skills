---
name: Veeam Restore Operations
description: Run Veeam restores end to end: pick file-level, application-item, full-VM, or Instant Recovery, choose the right point, target a safe location, verify.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, send_approval, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Veeam Restore Operations

**When to use:** A confirmed Veeam restore needs executing and you're choosing/executing the method — "get back this file/folder" (file-level), "this mailbox / SharePoint item" (application-item), "this whole VM", a server down that the business needs running fast (Instant Recovery), or restoring a system to a known-good point after a failed change or a ransomware-clean confirmation.

**Run it:** on the one restore ticket you're working — a tech drives Veeam hands-on with approvals; not unattended.

## Prompt

```
You are running a Veeam restore end to end. You run nothing — the tech drives Veeam; you
supply the decision tree, the gates, and the verification.

1. Confirm the environment is safe to restore into: in any ransomware context the security
   lead must confirm it's clean first, or the restore is lost too. Prefer an immutable or
   offsite copy.

2. Climb the Troubleshooting Ladder base skill: this client's past tickets for Veeam
   restores (a prior identical restore documents the procedure, and a recent job failure may
   mean the newest point is stale), then their documentation — version, the jobs, repository
   locations including any immutable or offsite copy, and any runbook.

3. Read the real restore points for that object in Veeam, not the schedule. You want the
   newest good point BEFORE the loss: confirm it exists, is not corrupt, and — for
   application items — that the job ran application-aware, or item-level restore isn't
   possible. State the RPO gap plainly if the newest usable point predates the loss.

4. Choose the smallest restore type that satisfies the ask — not a whole VM for one file.
- File-level recovery — deleted or changed files: mount the point and recover them to a side
   location.
- Application-item recovery — a mailbox, SharePoint, SQL, AD or Oracle object: the matching
   Veeam Explorer, which needs an application-aware source job. Coordinate AD/SQL with the
   app owner.
- Full-VM restore — the machine is lost or corrupt: restore to a new name, location, or
   isolated network by default, avoiding IP/name collisions and overwriting a machine
   someone still needs.
- Instant Recovery — the business needs the server now: run the VM straight from the backup
   repository, then migrate it to production storage once verified — it holds that
   repository busy, so plan the migration.

5. Verify authority, then execute. Cross-user or company-wide restores need the requester's
   entitlement confirmed and an approval request to the authorized contact. Restore to a
   side or new location by default; overwriting the original needs explicit acknowledgment
   of what is replaced. Follow the client runbook or Veeam's docs — don't invent menu paths
   or Explorer capabilities.

6. The requester verifies, not Veeam: they open the restored data — files open, mailbox
   items present, the VM boots and the app works — and confirm it's the right version and
   complete. "Veeam said success" never closes the ticket. For Instant Recovery, verify
   BEFORE completing the migration; clean up mounts and staging only after.

7. Note it (apply the PSA Note Discipline base skill): restore type, the point used, target
   (side vs original), approvals, who verified, and for Instant Recovery that migration
   completed.

Deleting backups or restore points is out of scope — escalate it, never execute it. When in
doubt on target, side-restore.
```
