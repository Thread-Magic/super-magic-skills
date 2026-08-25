---
name: Mailbox Quota Management
description: Investigate full or filling Exchange mailboxes and choose targeted cleanup, archive enablement, or license upgrade based on where size lives.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Mailbox Quota Management

**When to use:** A ticket says "mailbox is full" / a user can't send (or can't send and receive), proactive quota warnings are firing (ProhibitSendQuota approaching), or someone asks "why is this mailbox 49 GB?" as a size investigation on its own. Also covers a shared mailbox hitting the 50 GB unlicensed ceiling (cross-ref shared-mailbox-creation for the license rule).

**Run it:** on one mailbox — you find where the size lives and pick the fix, a technician drives PowerShell or the admin center (not a Flow: it needs a human at the console).

## Prompt

```
Find where the size actually lives BEFORE recommending anything, then route to the
cheapest fix that lasts. The tech drives PowerShell. Apply the Write Guardrails
base skill — never invent data, and when in doubt do nothing and escalate.

1. Get the real numbers first. Tech pulls (verify against current module versions):
   - `Get-MailboxStatistics <user> | Select TotalItemSize, ItemCount` and `Get-Mailbox
     <user> | Select *Quota*`.
   - `Get-MailboxFolderStatistics <user> | Sort FolderSize -Descending | Select -First 15
     Name, FolderSize, ItemsInFolder`.
   Check the knowledge base and client documentation for mailbox notes (Connector
   Degradation base skill if IT Glue isn't connected). Quote quotas from the tenant, not
   memory — plan limits change; verify against Microsoft's current docs.

2. Read the breakdown for the culprit:
   - Deleted Items or Junk huge — cleanup wins. Empty with the user's confirmation;
     Recoverable Items is the safety net for the retention window.
   - Recoverable Items huge — not a user-cleanup problem. Usually a hold or retention policy
     preserving churn; it has its own quota, which grows substantially once a hold applies.
     Route to litigation-hold or retention-policy-requests; never purge Recoverable Items on
     a held mailbox.
   - Sent Items or Inbox full of years of large attachments — archive territory
     (archive-mailbox-enablement).
   - One or two folders from a scanner or app — fix the source, then clean up.

3. Pick the path in cost order, with numbers:
   - Cleanup: free, immediate, bounded — when a few folders hold most of the size and the
     user agrees it can go.
   - Archive: needs Plan 2 or the Archiving add-on; drains the primary over days via policy.
     For keep-everything users (archive-mailbox-enablement executes).
   - License upgrade: Plan 1's 50 GB to Plan 2's 100 GB primary. The blunt paid fix, when
     the mailbox is legitimately large, cleanup is refused and archive won't cover the
     working set. An unlicensed shared mailbox hits the same 50 GB ceiling.
   Anything touching licensing needs the client's cost approval first.

4. Never delete user mail yourself, and never instruct deletion without the user's explicit
   confirmation in the ticket — it is their data. Name the folders and sizes; the user
   pulls the trigger.

5. If the user "can't send", check whether they are past ProhibitSend or past
   ProhibitSendReceive — the second means inbound mail is bouncing right now: higher
   urgency, and a client status update.

6. Verify: a fresh `Get-MailboxStatistics` below quota and the user confirms send works.
   Note it (PSA Note Discipline base skill: plain text, no markdown or emojis) — sizes
   before and after, folder culprits, path taken and why, approvals, and what to do
   when it fills again — usually the archive or upgrade deferred here. Log time.
```
