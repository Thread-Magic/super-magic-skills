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
You are preparing a calendar-permission change for a technician to execute. You translate the ask into the minimum folder role and capture consent; the tech runs the PowerShell or Outlook delegate flow. Never mark a grant as done on intention, and never invent the current permission state.

1. Translate the ask into a folder role before proposing anything (read the ticket for context), and confirm the minimum that satisfies it:
   - AvailabilityOnly — free/busy times only.
   - LimitedDetails — free/busy plus subject and location.
   - Reviewer — read full details.
   - Editor — read, create, and modify items.
   - Delegate (Editor + meeting-request handling) — the assistant scenario; meeting requests and responses route to the delegate.
   "Can they see my calendar?" is almost always LimitedDetails or Reviewer, not Editor. Minimum role always; Editor and delegate rights only when creating or managing items was explicitly requested and approved. Ask when ambiguous; do not default upward.

2. Consent: the calendar owner (or their manager per client policy) approves the grant — a calendar exposes travel, medical, and personnel meetings. Send an approval request or capture the owner's reply in the ticket. Owner consent on record before any grant; when the owner is unavailable and the request is urgent, escalate per client policy rather than granting.

3. Private items are a separate decision. By default a delegate does NOT see items marked private; the "delegate can see private items" flag is an explicit, owner-approved extra. Never bundle it silently.

4. Prepare execution for the tech (PowerShell labeled: verify against current module versions):
   - Grant: Add-MailboxFolderPermission -Identity "<owner>:\Calendar" -User <delegate> -AccessRights <Role>
   - Change existing: Set-MailboxFolderPermission (Add fails if a grant already exists — check first with Get-MailboxFolderPermission).
   - Full delegate flows (meeting forwarding, private items) are cleanest via Outlook's Delegate Access UI by the owner or the tech with the owner.
   Note: non-English mailboxes may name the folder differently — resolve the folder name from the mailbox, don't hardcode "Calendar".

5. Default-calendar exposure check: if the ask is "everyone can see details," that's the Default user's permission on the calendar — changing it affects the entire organization. Changing the Default permission is an org-wide change — restate that scope to the approver explicitly and get separate, explicit approval naming that scope before touching it.

6. Verify via evidence: the grantee opens the calendar and sees exactly the granted level (and cannot edit if Reviewer). Allow propagation time before retesting. Document what/why/when/rollback: leave a plain-text note with owner, grantee, exact role, private items yes/no, approver, date, expiry if temporary, and rollback (Remove-MailboxFolderPermission). Temporary coverage (leave, project) gets an expiry and a tracked revert. Log time.

When in doubt about scope, an unavailable owner, or an org-wide Default change, do nothing and escalate per client policy.
```
