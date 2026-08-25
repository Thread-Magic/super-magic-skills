---
name: Entra User Lifecycle (Zapier)
description: Create, update, or disable Microsoft Entra ID users through the Zapier connector with identity resolved from the PSA and approval gated on every write.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: [Zapier: Microsoft Entra ID]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Entra User Lifecycle (Zapier)

**When to use:** "Create the Entra account for <user> per the onboarding ticket" / "disable <user> in Entra now — offboarding effective today" / "update <user>'s title/department/manager in Entra" — an onboarding, offboarding, or user-update ticket where the desk executes Entra changes itself via the Zapier connector.

**Run it:** on one ticket — every write is approval-gated; not eligible for unattended Flow writes.

## Prompt

```
Execute Entra ID writes from this ticket via Zapier, around one hard constraint: the integration
can write users but cannot SEARCH them, so identity must be resolved PSA-side before any write.

1. Confirm the connector: the acting member needs Zapier with the Microsoft Entra ID app
   authorized for this client's tenant. Without it, apply the Connector Degradation base skill —
   produce the change specification as a plain-text note for a tech to run, and never imply the
   write happened.

2. Resolve identity PSA-side FIRST, from the contact and client records, the ticket, and IT Glue
   or the knowledge base: exact UPN and email, display name, and for updates or disables the
   unambiguous existing identifier. If the UPN isn't certain, STOP and ask — a write against a
   guessed UPN can hit the wrong person or create a duplicate.

3. For creates, also resolve the naming convention from client documentation, plus department,
   title, manager, usage location (required before licensing) and role-based groups. Check
   collisions against PSA contact records and documentation, and say in the note that collision
   checking was PSA-side only.

4. Approval gate before EVERY write: post the exact intended change — action, target UPN, fields
   and values or groups — and get sign-off via an approval request or the client's documented
   channel. One approval may cover a ticket's coherent change set; it never carries to a second
   user or a later ticket.

5. Execute the matching Zapier action — Microsoft Entra ID "Create User", "Update User", "Disable
   User" or a group-membership action — one logical change at a time. Sequencing still binds: for
   offboarding, mailbox handling precedes license removal; on hybrid tenants on-prem AD is the
   source of authority, so make the change in AD and run an AD Connect delta sync instead of
   writing cloud-side against a synced object.

6. Verify by EFFECT, since there is no search: the user appears in the licensing or billing view,
   sign-in behaves as expected, or a tech eyeballs the portal. Then note it — plain text, no
   markdown or emojis (PSA Note Discipline base skill): action, target, approver, Zapier action,
   verification, outcome. Log time.

No Entra write without the approval gate, including "small" updates. Never Delete User in routine
offboarding: Disable is the action; deletion happens only on explicit documented client
instruction after retention windows. Passwords set at creation: secure transfer only, forced
change at next sign-in, never in the ticket or an email. On a Zapier error or ambiguous result,
don't retry blind — report the state as unknown and have it verified; a retried create makes
duplicates. Never eligible for unattended writes: from a Flow, produce only the proposed change
specification as a note ending "PENDING APPROVAL - no changes made", for a human to approve and
trigger.
```
