---
name: Veeam Restore Operations
description: Run a Veeam restore request end-to-end — choosing the right restore type (file-level vs application-item vs full-VM vs Instant Recovery), picking the correct restore point, restoring to a safe location, and verifying the data — distinct from diagnosing why a backup failed (backup-failure-triage / backup-restore-request for intake).
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
You are running a Veeam restore end-to-end. The request is already intaken (what/when/where is settled) and the backups exist — your job is to pick the right restore type, the right restore point, a safe target, and verify the result. This is the counterpart to backup-failure-triage (which is about backups that didn't run); here someone needs data back.

1. Confirm intake and environment first. Ensure the what/when/where and the RPO honesty are settled, and confirm the environment is safe to restore into. For any ransomware context, the security lead must confirm the environment is clean before you restore — restoring into an infected environment loses the restore; prefer an immutable/offsite copy, and pair with the security response playbooks. Check the client's documentation and knowledge base for the Veeam setup: version/edition, the backup jobs and what they protect, repository locations (and whether an immutable/offsite copy exists), and any documented restore runbook. Documentation coverage varies per tenant — note what you couldn't check. If a Liongard Veeam inspector is available in this tenant, corroborate job/restore-point state and note the dataprint age; otherwise ask the tech to confirm from the Veeam console.

2. History first. Search this client's past tickets for Veeam/restore: a prior identical restore documents the working procedure and duration; a recent job-failure ticket may mean the newest restore point isn't what the requester assumes.

3. Read the actual restore points before promising. Have the tech read the real available restore points for the specific object in Veeam (not the schedule) — the chosen point is the newest good one BEFORE the loss moment. Confirm the point exists, is not corrupt, and (for application items) that application-aware processing was on for that job so item-level restore is even possible. State the RPO gap plainly if the newest usable point predates the loss — never invent a restore point or its contents.

4. Choose the right restore type — this is the core decision. Pick the smallest type that satisfies the ask; don't full-VM-restore for one file:
   - File-level recovery — deleted/changed files or folders: mount the restore point and recover the specific items to a SIDE location by default. Never overwrite the live path without explicit acknowledgment. Smallest, safest, most common.
   - Application-item recovery (Veeam Explorers) — a mailbox item, a SharePoint/OneDrive item, a SQL/AD/Oracle object: use the matching Explorer, which needs the source job to have been application-aware. Restore the specific item to a safe target; for AD/SQL objects, coordinate with the app owner.
   - Full-VM restore — the whole machine is lost/corrupt: restore the VM, by default to a NEW name/location or isolated network to avoid IP/name collisions and overwriting a machine that might still be needed. Overwriting the original is a deliberate, acknowledged choice.
   - Instant Recovery — the business needs the server NOW: run the VM directly from the backup repository for speed, then migrate it to production storage once verified. It trades performance for uptime and holds the repository busy — plan the follow-through (Storage vMotion / migrate) so it doesn't run indefinitely from backup, and know it loads that repository.

5. Verify authority, then execute per Veeam's procedure. For cross-user or company-wide restores, send an approval request to the authorized client contact and confirm the requester is entitled to this data. Execute per the vendor's documented procedure (the client runbook, or Veeam's current docs on the web — cite; do not invent Veeam menu paths, Explorer capabilities, or version behaviours). Default to side/new-location; original overwrites require explicit acknowledgment of what's replaced. Give realistic duration for large restores up front. You do not run remote commands — the tech drives Veeam; you supply the decision tree, gates, and verification.

6. Restore verification — the requester closes it. The requester opens the actual restored data (files open, mailbox items present, the VM boots and the app works) and confirms it's the right version and complete. "Veeam said success" is not verification and never closes the ticket on its own. For Instant Recovery, verify BEFORE completing the migration to production storage; only after migration completes do you clean up mounts/staging.

7. Note and aftermath. Leave a plain-text internal note (PSA-safe: no markdown or emojis, raw URLs not links): restore type and why, restore point used, target (side vs original), approvals, verification by whom, and (for Instant Recovery) that migration completed. If the restore points revealed a coverage/failure gap, open the follow-up per backup-failure-triage.

Deletion of backups or restore points is out of scope — escalate it, never execute it. When in doubt on target, side-restore.
```
