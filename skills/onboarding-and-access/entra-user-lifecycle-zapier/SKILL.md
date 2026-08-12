---
name: Entra User Lifecycle (Zapier)
description: Create, update, or disable Microsoft Entra ID users through the Zapier connector — identity resolved from the PSA/ticket first (Entra has no search), approval gated before every write. Use when an onboarding/offboarding/update ticket should execute directly against Entra via Zapier.
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
Execute Entra ID account writes from this ticket via Zapier — with the one hard
constraint designed in: Zapier's Entra integration can write users but cannot SEARCH
them, so identity must be fully resolved on the PSA/ticket side before any write.

1. Confirm the connector: the acting member must have the Zapier connector with the
   Microsoft Entra ID app authorized for this client's tenant. If unavailable, degrade
   to producing the exact change specification as a plain-text note for a tech to
   execute manually — never pretend the write happened.

2. Resolve identity from the PSA side FIRST. There is no user search in Entra via
   Zapier. Build the full identity by looking up the contact and client, reading the
   ticket, and checking client documentation (IT Glue / knowledge base): exact
   UPN/email, display name, and for updates/disables the unambiguous existing user
   identifier. If the UPN cannot be established with certainty, STOP and ask — a write
   against a guessed UPN can hit the wrong person or create a duplicate.

3. For creates, also resolve: naming convention (from client docs), department, title,
   manager, usage location (required before licensing), and the role-based groups per
   New Hire Onboarding. Check for collisions using PSA contact records and
   documentation (Entra can't be searched) — state in the note that collision checking
   was PSA-side only.

4. Approval gate before EVERY write, no exceptions: post the exact intended change
   (action, target UPN, fields/values or groups) and get sign-off (send an approval
   request, or use the client's documented channel). One approval may cover one
   ticket's coherent change set, but never carries over to a second user or a later
   ticket.

5. Execute via the corresponding Zapier action — `Zapier: Microsoft Entra ID
   "Create User"`, `"Update User"`, `"Disable User"`, or the group-membership actions —
   one logical change at a time. Sequencing rules from the sibling skills still bind:
   for offboarding, mailbox handling precedes license removal; for hybrid tenants,
   on-prem AD is the source of authority — do not write cloud-side against a synced
   object; make the change in AD and run an AD Connect delta sync instead.

6. Verify by EFFECT, not by search (there is none): confirm through an observable
   outcome — user appears in the licensing/billing view, sign-in behaves as expected,
   or a tech eyeballs the portal. Then post a plain-text note: action, target, approver,
   Zapier action used, verification method, outcome. Log time.

Guardrails: no Entra write without the approval gate — including "small" updates. Never
guess a UPN; unresolvable identity = no write. Never Delete User as part of routine
offboarding — Disable is the offboarding action; deletion only on explicit documented
client instruction after retention windows. Passwords set at creation follow the canon:
secure transfer only, change forced at next sign-in, never in the ticket or email. On
any Zapier error or ambiguous result, do not retry blind — report the exact state as
unknown and have it verified before a second attempt (a retried create makes
duplicates). Do not write cloud-side attributes on objects mastered in on-prem AD.
Never eligible for unattended writes: if this is somehow invoked from a Flow, produce
only the proposed change specification as a plain-text note ending "PENDING APPROVAL —
no changes made," and let a human approve and trigger execution.
```
