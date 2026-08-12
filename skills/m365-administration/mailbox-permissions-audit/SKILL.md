---
name: Mailbox Permissions Audit
description: Inventory who can access what across mailboxes — Full Access, Send As, Send on Behalf, and folder-level grants — and flag unexpected grants. Use when a ticket asks "who has access to this mailbox," a security review needs a delegation inventory, or offboarding needs a permission sweep.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket, log_time_entry, web_search]
connectors: [IT Glue]
scope: both
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Mailbox Permissions Audit

**When to use:** A ticket asks "who can read/send from <mailbox>," a periodic client security review needs a delegation inventory, an offboarding sweep needs to know what the departing user had access to (and who has access to theirs), or a user reports "someone read/sent my email" — inventory first, then hand proven-misuse questions to delegate-access-forensics. Produce a complete, honest map: every grant type enumerated, each classified expected or unexpected, findings documented so someone can act. Never revoke within the audit itself.

**Run it:** on a single mailbox, or as a tenant-wide sweep — you prepare the collection and classify, a technician runs and pastes back the results (not a Flow: it needs a human at the console).

## Prompt

```
You are producing a complete, honest map of mailbox access for one mailbox or a whole tenant. The agent prepares the collection block and classifies what the tech pastes back; every removal is a separate approved change, never done inside the audit. Never invent data; report what was NOT checked as clearly as what was.

1. Scope with the requester: one mailbox, a department, or tenant-wide. Tenant-wide takes longer and produces a report, not a quick answer — say so.

2. Prepare the collection block for the tech (verify against current module versions). All three grant types must be collected — auditing only Full Access misses the impersonation-grade grants:
   - Full Access: `Get-MailboxPermission <mbx> | Where {$_.User -notlike "NT AUTHORITY\SELF"}`
   - Send As: `Get-RecipientPermission <mbx>`
   - Send on Behalf: `Get-Mailbox <mbx> | Select GrantSendOnBehalfTo`
   - If the ticket concerns calendar/folder access, add `Get-MailboxFolderPermission <mbx>:\Calendar` (see calendar-permissions).
   For tenant-wide, the same cmdlets piped over `Get-Mailbox -ResultSize Unlimited`, exported to CSV.

3. Classify every grant against documentation (check the client's documentation — skip gracefully if IT Glue isn't connected — the knowledge base, and prior tickets). Expected = traceable to a ticket, a documented role, or a shared-mailbox design. Flag as unexpected:
   - Any grant with no ticket or documentation trail.
   - Full Access or Send As on a personal mailbox held by a peer (not an assistant/manager arrangement on record).
   - Grants held by disabled or departed accounts.
   - Send As granted where the documented need was read-only.
   - Broad grants (groups with FullAccess on individual mailboxes).

4. Do not remediate inside the audit. Unexpected grants get listed with a recommended action (revoke / confirm with owner / document); revocation is its own approved change via shared-mailbox-delegation, because "unexpected" sometimes means "undocumented but load-bearing."

5. If a flagged grant smells like compromise (grant appeared recently, grantee irrelevant to the mailbox, paired with forwarding), escalate to the security playbooks (compromised-account-containment) instead of treating it as hygiene.

6. Leave a plain-text note (update the ticket as needed): scope, collection date, counts per grant type, the full inventory (or CSV reference for tenant-wide), each unexpected grant with why it's flagged and the recommended action, and explicit statement of anything not covered (e.g., folder-level grants not swept — a partial audit presented as complete is worse than no audit). Use neutral language in findings: "grant not traceable to documentation," not "so-and-so has been reading the CEO's mail." Log time.

Guardrails: Inventory, classify, recommend — never revoke within the audit itself; every removal is a separate approved change with its own rollback. Departed-user grants and Send As anomalies always get flagged, even when the requester only asked about Full Access. When in doubt about a grant that may be load-bearing or a possible compromise, do nothing and escalate.
```
