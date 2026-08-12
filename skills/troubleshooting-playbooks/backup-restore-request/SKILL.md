---
name: Backup Restore Request
description: Intake backup restore requests — deleted files, prior versions, mailboxes, servers — pinning down what, when, RPO limits, and verifying with requester.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, send_approval, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Backup Restore Request

**When to use:** "<user> deleted a file/folder — can we get it back?"; "we need <share/mailbox/site> as it was last Tuesday"; a ransomware/corruption recovery-point request (pair with security response); or any request naming a backup product, snapshot, or "previous version."

**Run it:** on the one restore ticket in front of you — an intake-and-execute workflow a tech drives with the requester, not unattended.

## Prompt

```
You are intaking and working a restore request. A restore done from a vague request restores the wrong thing to the wrong place — sometimes over the right thing. Make the intake precise (what, as-of-when, restored to where), set honest recovery-point expectations before work starts, and end with the requester verifying the data, not the tech assuming it.

History first. Search this data/user's past tickets — a related deletion or migration ticket pins the loss time better than memory, and a recent identical restore documents the working procedure.

Docs second. Check the client's documentation and knowledge base for what protects this data: the backup product and scope (is this share/mailbox/VM actually in a job?), schedule/retention, and any restore runbook. Also check the cheap paths first-class: recycle bins, M365 retention/deleted-item recovery, VSS previous versions — many "restores" never need the backup product. Documentation coverage varies per tenant — note what you could not check.

Intake — pin all three axes before touching anything:
- What: exact path/mailbox/object, and whether it's the item, a folder, or a whole system. Ambiguity here is where wrong restores come from — confirm the precise path with the requester.
- When: the as-of moment — "before it was deleted/changed", with the best-known timestamp. The restore point chosen is the newest point before that moment.
- Where: restore to original location (risks overwriting current data) or to a side location for the requester to pick from (the safe default). Never restore over the original location without explicit acknowledgment of what gets overwritten — side-restore is the default; when in doubt, side-restore.

RPO honesty — before promising anything. Read the actual available restore points from the job history, not the schedule: the promise is the last successful backup before the loss, and if last night's job failed, the honest answer may be 48+ hours of loss. State plainly: anything created or changed between that restore point and the loss is not recoverable from backup. Never imply backup can produce data from between points or from outside job scope. If the data was never in a job's scope, say that immediately and check the secondary paths (recycle bin, sync client versions, email copies) rather than raising false hope.

Verify authority. Restores expose data as-of a past date and can overwrite the present. Confirm the requester is entitled to this data (owner, their manager, or documented authorized contact); anything restoring one user's data at another's request, or company-wide data, goes out as an approval request to the authorized client contact. Requests to delete backups are out of scope entirely — escalate them. Ransomware-context restores also confirm with the security lead that the environment is clean before restoring into it — restoring into an infected environment loses the restore too.

Execute per the product's procedure. The tech performs the restore per the vendor's documented procedure (from the client runbook or the vendor's current docs on the web) — there is no remote execution from here; this playbook supplies sequence, gates, and expectations. Default to side-restore; original-location overwrites require explicit requester acknowledgment of what current data gets replaced. Large restores: give the realistic duration and set the expectation now, not at hour three.

Restore verification — the requester closes it, not the tech. The requester opens the actual restored data and confirms it is the right version and complete (files open, mailbox items present, application data consistent). "The job said success" is never verification and never closes a restore ticket. Only then clean up any side-restore staging.

Note and aftermath. Leave a plain-text internal note (raw URLs, not markdown): what/when/where as intaken, restore point used and why, RPO gap communicated, approvals, verification by whom, and what you couldn't check. If the job history showed failures or the data wasn't protected, open the follow-up ticket to fix coverage — that finding must not die with this ticket; silently fixing nothing is the worst outcome.
```
