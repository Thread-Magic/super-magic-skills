---
name: Mailbox Permissions Audit
description: Inventory Exchange mailbox access grants: Full Access, Send As, Send on Behalf, and folder-level permissions, flagging unexpected delegations.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket, log_time_entry, web_search]
connectors: []
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
You produce a complete, honest map of mailbox access for one mailbox or a whole tenant. You
prepare the collection block and classify what the tech pastes back. Inventory, classify and
recommend — never revoke inside the audit; every removal is a separate approved change with
its own rollback.

1. Scope it with the requester: one mailbox, a department, or tenant-wide — tenant-wide
   produces a report, not a quick answer.

2. Prepare the collection block for the tech (verify against current module versions). All
   three grant types must be collected — auditing only Full Access misses the
   impersonation-grade grants:
   - Full Access: Get-MailboxPermission <mbx> | Where {$_.User -notlike "NT AUTHORITY\SELF"}
   - Send As: Get-RecipientPermission <mbx>
   - Send on Behalf: Get-Mailbox <mbx> | Select GrantSendOnBehalfTo
   - Folder or calendar access, when the ticket concerns it:
     Get-MailboxFolderPermission <mbx>:\Calendar (see calendar-permissions).
   Tenant-wide is the same cmdlets piped over Get-Mailbox -ResultSize Unlimited, to CSV.

3. Classify every grant against the client's documentation, the knowledge base and prior
   tickets — continue without those integrations if off (Connector Degradation base
   skill). Expected means traceable to a ticket, a documented role, or a shared-mailbox
   design. Flag as unexpected:
   - Any grant with no ticket or documentation trail.
   - Full Access or Send As on a personal mailbox held by a peer, absent an assistant or
     manager arrangement on record.
   - Grants held by disabled or departed accounts.
   - Send As where the documented need was read-only.
   - Broad grants, such as a group with Full Access on individual mailboxes.
   Departed-user grants and Send As anomalies get flagged even when the requester only asked
   about Full Access.

4. List each unexpected grant with a recommended action — revoke, confirm with the owner, or
   document — then stop. Revocation is its own approved change via shared-mailbox-delegation,
   because "unexpected" sometimes means "undocumented but load-bearing".

5. A grant that appeared recently, held by someone irrelevant to the mailbox, especially
   paired with forwarding, is a compromise indicator — escalate it to
   compromised-account-containment rather than working it as an audit finding.

6. Leave a plain-text note (PSA Note Discipline base skill): scope, collection date, counts
   per grant type, the inventory or CSV reference, each unexpected grant with why it is
   flagged and its recommended action, and what was not covered (Sweep Honesty base skill:
   state result caps and "at least N") — a partial audit presented as complete is worse
   than no audit. Keep findings neutral: "grant not traceable to documentation", never
   "so-and-so has been reading the CEO's mail". Log time.

When in doubt, do nothing and escalate.
```
