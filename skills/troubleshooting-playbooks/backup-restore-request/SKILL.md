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
A restore run from a vague request restores the wrong thing to the wrong place —
sometimes over the right thing.

Climb the Troubleshooting Ladder base skill first: past tickets for this data or user (a
related deletion or migration ticket pins the loss time better than memory), then the
documentation for what protects it — the backup product and scope (is this share,
mailbox, or VM actually in a job?), schedule, retention, any runbook. Check the cheap
paths first — recycle bins, Microsoft 365 retention and deleted-item recovery, VSS
previous versions; many "restores" never need the backup product.

Intake — pin three axes before touching anything:
- What: the exact path, mailbox, or object, and whether it's an item, a folder, or a
  whole system. Confirm it with the requester; ambiguity here is where wrong restores
  come from.
- When: the as-of moment, best-known timestamp. The restore point is the newest one
  before it.
- Where: a side location for the requester to pick from — the safe default — or the
  original, which risks overwriting current data. Never restore over the original
  without the requester explicitly acknowledging in the ticket what gets overwritten.

RPO honesty before promising anything: read the available restore points from the job
history, not the schedule. The promise is the last successful backup before the loss; if
last night's job failed, the honest answer may be 48+ hours of loss. State plainly that
anything created or changed between that restore point and the loss is not recoverable.
Never imply backup can produce data from between points or from outside a job's scope.
If the data was never in scope, say so immediately and work the secondary paths.

Verify authority: the requester must be entitled to this data — the owner, their
manager, or a documented authorized contact. Restoring one user's data at another's
request, or anything company-wide, goes out as an approval request to the authorized
client contact. Requests to delete backups are out of scope: escalate them. In a
ransomware context, confirm with the security lead that the environment is clean before
restoring into it — restoring into an infected environment loses the restore too.

The tech executes per the vendor's documented procedure. On a large restore, give the
realistic duration now, not at hour three.

The requester closes it, not the tech: they open the restored data and confirm it is the
right version and complete — files open, mailbox items present, app data consistent.
"The job said success" is never verification. Only then clean up side-restore staging.

Note it (apply the PSA Note Discipline base skill): what/when/where as intaken, the
restore point used, the RPO gap communicated, approvals, who verified. If the job
history showed failures or the data wasn't protected, open the follow-up ticket to fix
coverage; that finding must not die here.
```
