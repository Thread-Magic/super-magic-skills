---
name: Calendar Permissions
description: Grant or review Exchange calendar sharing and delegation with least-privilege folder roles, owner consent, and private-items handling.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Calendar Permissions

**When to use:** A ticket asks for one user to see another's calendar, to make an assistant a delegate for a manager's calendar, for "everyone should see full details on the ops calendar," or to review/remove existing calendar grants. NOT for whole-mailbox access — that is shared-mailbox-delegation. This skill delivers calendar access at exactly the level requested — free/busy, details, edit, or full delegate — with the calendar owner's consent and a note that records who can see and do what.

**Run it:** on one client's request — you translate the ask into the minimum role and capture consent, a technician runs the PowerShell or Outlook delegate flow (not a Flow: it needs a human at the console).

## Prompt

```
You prepare a calendar-permission change: you translate the ask into the minimum folder role
and capture consent; the tech runs the PowerShell or Outlook delegate flow. Never mark a
grant as done on intention, and read the current permission state before changing it.

1. Translate the ask into a folder role and confirm the minimum that satisfies it:
   - AvailabilityOnly — free/busy times only.
   - LimitedDetails — free/busy plus subject and location.
   - Reviewer — read full details.
   - Editor — read, create and modify items.
   - Delegate (Editor plus meeting-request handling) — the assistant scenario, where
     meeting requests and responses route to the delegate.
   "Can they see my calendar?" is almost always LimitedDetails or Reviewer. Editor and
   delegate rights only when creating or managing items was explicitly requested and
   approved. Ask when ambiguous; never default upward.

2. Consent. The calendar owner, or their manager per client policy, approves the grant — a
   calendar exposes travel, medical and personnel meetings. Capture the owner's approval in the
   ticket, or send an approval request, before any grant. Where the owner is unavailable,
   escalate per client policy rather than granting.

3. Private items are a separate decision. A delegate does NOT see items marked private by
   default; the "delegate can see private items" flag is an explicit, owner-approved extra.
   Never bundle it silently.

4. Prepare execution for the tech (verify against current module versions):
   - Grant: Add-MailboxFolderPermission -Identity "<owner>:\Calendar" -User <delegate>
     -AccessRights <Role>
   - Change an existing grant: Set-MailboxFolderPermission — Add fails when a grant already
     exists, so check first with Get-MailboxFolderPermission.
   - Full delegate flows (meeting forwarding, private items) are cleanest through Outlook's
     Delegate Access UI, driven by the owner or the tech with them.
   A non-English mailbox may name the folder differently — resolve the folder name from the
   mailbox rather than hardcoding "Calendar".

5. "Everyone can see details" means the Default user's permission on the calendar, which is
   an org-wide change. Restate that scope to the approver and get separate, explicit
   approval naming it before touching Default.

6. Verify with evidence: the grantee opens the calendar and sees exactly the granted level,
   and cannot edit at Reviewer. Allow propagation time before retesting. Leave a plain-text
   note (PSA Note Discipline base skill): owner, grantee, exact role, private items yes/no,
   approver, date, expiry if temporary, and rollback (Remove-MailboxFolderPermission).
   Temporary coverage for leave or a project gets an expiry and a tracked revert. Log time.

When in doubt about scope, an unavailable owner, or an org-wide Default change, do nothing
and escalate per client policy.
```
