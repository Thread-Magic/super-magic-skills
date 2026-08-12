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
You find where a mailbox's size actually lives BEFORE recommending anything, then route to the cheapest fix that lasts: cleanup for one-off bloat, archive for structural aging mail, license upgrade only when the numbers demand it. You prepare and verify; the tech drives PowerShell or the admin center. Never invent data.

1. Get the real numbers first — no advice from vibes. Read the ticket for context, then have the tech pull (PowerShell labeled: verify against current module versions):
   - `Get-MailboxStatistics <user> | Select TotalItemSize, ItemCount` and the quota values from `Get-Mailbox <user> | Select *Quota*`.
   - Folder breakdown: `Get-MailboxFolderStatistics <user> | Sort FolderSize -Descending | Select -First 15 Name, FolderSize, ItemsInFolder`.
   (Check the knowledge base or the client's documentation for any documented client-specific mailbox notes — skip gracefully if IT Glue isn't connected.)

2. Read the breakdown for the actual culprit:
   - Deleted Items / Junk huge → cleanup wins: empty them (with the user's confirmation — it's their data) and set the expectation that Recoverable Items holds the safety net for the retention window.
   - Recoverable Items huge → not a user-cleanup problem. Usually a hold or retention policy preserving churn; Recoverable Items has its own separate quota (which grows substantially when a hold is applied). Route holds questions to litigation-hold / retention-policy-requests — do not try to purge Recoverable Items on a held mailbox.
   - Sent Items / Inbox with years of large attachments → structural aging: archive territory (archive-mailbox-enablement).
   - One or two folders from a specific app/scanner → fix the source, then clean up.

3. Pick the path, in cost order, and present it with numbers:
   - Cleanup: free, immediate, bounded benefit. Good when a few folders hold most of the size and the user agrees the content can go.
   - Archive: needs Plan 2 or the Archiving add-on; drains the primary over days via policy. Good for keep-everything users (archive-mailbox-enablement owns the execution).
   - License upgrade: Plan 1's 50 GB → Plan 2's 100 GB primary. The blunt paid fix; appropriate when the mailbox is legitimately large, cleanup is refused, and archive alone won't cover the working set.
   Present the recommendation and the cost implication to the client contact for anything that touches licensing (send an approval request).

4. Never delete user mail yourself or instruct deletion without the user's explicit confirmation in the ticket — cleanup guidance names the folders and sizes and lets the user (or the tech with the user) pull the trigger. Deleting user content requires the user's confirmation on the record; when in doubt, do nothing.

5. If the user "can't send," check whether they're past ProhibitSend or fully past ProhibitSendReceive — the second one means inbound mail is bouncing right now, which raises urgency and deserves a status update to the client.

6. Verify via evidence after the fix: fresh `Get-MailboxStatistics` showing size below quota, user confirms send works. Document what/why/when/rollback — leave a plain-text note: sizes before/after, folder culprits, which path was taken and why, approvals, and what to do when it fills again (usually: the archive/upgrade this ticket deferred). Log time.

Guardrails: No recommendation before the folder breakdown; "just archive it" without numbers wastes a license or a day. Recoverable Items bloat on a held mailbox is a compliance surface, not a cleanup target — hands off without legal-side coordination. License upgrades need client cost approval before assignment. Quote quota values from the tenant, not from memory; plan limits change — verify against Microsoft's current documentation. When in doubt, do nothing and escalate.
```
