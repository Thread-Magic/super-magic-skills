---
name: Employee Offboarding
description: Securely disable a departing employee in the right order — sign-in and sessions first, mailbox before licenses — and reclaim access and assets. Use when a ticket asks to offboard, terminate, disable, or "remove access for" a user.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_itglue, search_knowledge_base, add_ticket_note, update_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Employee Offboarding

**When to use:** "<user> is leaving Friday — disable everything on their last day" / "terminated effective immediately, cut access now" / "offboard <user>, manager needs their mailbox and files" — any offboarding ticket that needs the checklist built, sequenced, and worked.

**Run it:** on one ticket — a security event with destructive steps, so every action is human-confirmed.

## Prompt

```
Run this departure as a security event: cut access in the correct order, preserve
data before licenses disappear, confirm every destructive step, and end with a
sign-off summary for HR or the manager.

1. Confirm the target user (look up the contact), the client, the effective
   date/time, and that the requester is authorized to order this offboarding
   (manager, HR, or a documented authorized contact — never the departing user
   themselves). Pull the client's offboarding SOP from the knowledge base and their
   IT documentation (IT Glue).

2. At the effective time, cut interactive access FIRST, in this order: disable
   sign-in, revoke all active sessions and refresh tokens, remove/reset MFA methods,
   reset the password. An enabled session outlives a password reset — session
   revocation is not optional.

3. Handle the mailbox BEFORE touching licenses: convert to shared or set forwarding
   per client policy, set the out-of-office, grant the manager access if policy
   allows. Removing the license first can destroy the mailbox — never reverse this.

4. Only THEN remove licenses, security groups, app assignments, distribution lists,
   and shared-mailbox delegations. Transfer ownership of anything the user owned
   (files, groups, DLs) to the manager or a named successor.

5. Hardware and devices: list assigned hardware for return, disable/retire the
   managed device enrollment, record serial/asset details in the note. If a device
   is remote, note the return-logistics step as Pending with an owner (hand to the
   Laptop Return Logistics skill).

6. Stamp the trail: write the ticket number into the disabled AD/Entra object's
   description field so any future admin can trace why the account is disabled. If
   hybrid, run an AD Connect delta sync and verify the disable propagated before
   reporting the account secured.

7. Post a plain-text checklist note (no markdown/emojis — PSA sync) with each step
   Done / Pending / Blocked, then send a sign-off summary to HR or the manager:
   access-cut time, mailbox disposition, data handoff, hardware status, and anything
   awaiting their decision. Log time.

Guardrails: confirm before every destructive action — disable, wipe, license
removal, delegation removal; never run the whole sequence unattended. Mailbox
conversion always precedes license removal; if unsure the mailbox is preserved, stop
and verify. Do not act on an offboarding requested only by the departing user or an
unverified sender — verify authorization against a contact on file. Follow the
client's retention/data-handoff policy; if none is documented, ask rather than
defaulting to deletion. Never use access as leverage against the departing person —
this is a controlled, procedural cutover, not a punishment. Do not report the
offboarding complete while any Pending item lacks an owner.
```
