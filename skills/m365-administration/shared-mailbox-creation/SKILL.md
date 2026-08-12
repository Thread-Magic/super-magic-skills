---
name: Shared Mailbox Creation
description: Create Exchange Online shared mailboxes: naming, licensing at the 50GB threshold, initial delegation, and documentation for team inboxes.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Shared Mailbox Creation

**When to use:** A ticket asks for a new shared mailbox / team inbox / group address people work out of (support@, invoices@, hr@), or an ex-employee's mailbox is being converted to shared during offboarding. NOT for adding people to an existing shared mailbox — that is shared-mailbox-delegation.

**Run it:** on one client's request — you prepare and verify, a technician drives the admin center or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You are preparing a shared-mailbox creation for a technician to execute in one pass. You prepare and verify; the tech drives the admin center or PowerShell. Never report creation as done on intention — never invent data.

1. Pin down the request from the ticket (read the ticket for context): display name, SMTP address, purpose, and the initial delegate list with the permission each person needs (Full Access vs Send As vs Send on Behalf — see shared-mailbox-delegation for the distinctions). Confirm the address isn't already in use as an alias, DL, or M365 group — ask the tech to check, or check the client's documentation for documented addresses (skip gracefully if IT Glue isn't connected).

2. Answer the license question BEFORE creation, not after: a shared mailbox is free up to 50 GB with no license; over 50 GB, or if it needs an online archive or a litigation hold, it requires Exchange Online Plan 2 (or Plan 1 + Archiving add-on). If expected volume is high (shared support queues grow fast), say so in the ticket and flag the future license cost to the client contact.

3. Approval gate: a new sendable identity on the client's domain is user-visible and impersonation-adjacent — get the client's documented approver to sign off on the address and the initial delegate list via an approval request before anything is created.

4. Prepare the execution block for the tech (PowerShell labeled: verify against current module versions):
   - New-Mailbox -Shared -Name "<display name>" -PrimarySmtpAddress <address>
   - Delegations per shared-mailbox-delegation — minimum permission per person; do NOT pre-grant Send As to everyone "to be safe".
   - Sign-in on the underlying account stays blocked (disabled by default — keep it that way; nobody logs in "as" the mailbox). If someone asks for "the password to the shared mailbox," redirect to delegation.

5. After the tech executes, verify via ticket evidence: a delegate confirms they can open the mailbox and, if granted, send from it; a test mail to the new address arrives. Allow up to an hour for permission propagation before calling it broken.

6. Document what/why/when/rollback: leave a plain-text note with mailbox name and address, purpose, delegates and exact permission types, approver, creation date, license status (unlicensed under 50GB / Plan 2 attached), and rollback (disable delegations, convert or remove mailbox). Log time.

When in doubt about authorization or a possible address collision, do nothing and escalate.
```
