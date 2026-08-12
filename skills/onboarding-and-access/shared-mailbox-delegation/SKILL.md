---
name: Shared Mailbox Delegation
description: Set up or change shared mailbox access (Full Access, Send As, Send on Behalf) with owner approval and an audit note recorded on the delegation ticket.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Shared Mailbox Delegation

**When to use:** "Add <user> to the support shared mailbox" / "<user> needs to send as accounting@<client-domain>" / "give the assistant access to the manager's mailbox" — setting up, changing, or reviewing a delegation.

**Run it:** on one ticket — approval-gated, so a human confirms the delegation.

## Prompt

```
Deliver this mailbox delegation with the right permission type, an approval on
record, and an audit note that says exactly who can now do what from which address.

1. Pin down the three variables: the delegate (look up the contact), the target
   mailbox, and the permission type — distinguish explicitly:
   - Full Access: read and manage the mailbox contents.
   - Send As: send mail that appears to come from the mailbox itself.
   - Send on Behalf: send with "on behalf of" visible to recipients.
   If the requester just says "access," ask which behavior they need — Send As is a
   bigger grant than most requesters realize.

2. Identify the mailbox owner or the client's documented approver (knowledge base / IT
   Glue documentation) and get approval before the change (send an approval request, or
   use the client's channel). A user's personal mailbox always requires that user's (or
   their manager's, per policy) consent.

3. Apply the minimum permission type that satisfies the need. Do not pair Full Access
   with Send As by default — grant Send As only when sending from the address was
   actually requested and approved.

4. If the delegation is temporary (leave coverage, project), set an expiry and create
   a tracked revert (follow-up note with date and owner, or a scheduled follow-up
   ticket).

5. Execute, allow for propagation delay before the user tests, and verify the delegate
   can do what was granted — and nothing more.

6. Post a plain-text audit note: delegate, mailbox, exact permission type, approver,
   business reason, grant date, and expiry/revert if temporary. Log time.

Guardrails: no delegation without approval from the mailbox owner or documented
approver. Never grant Send As when Send on Behalf or Full Access satisfies the need —
sending as another identity is impersonation-grade. The audit note is mandatory: a
delegation nobody can trace is a finding in the next security review. Temporary
delegations always carry an expiry and revert. When the requester, owner, or
permission type is ambiguous, ask; do not grant.
```
