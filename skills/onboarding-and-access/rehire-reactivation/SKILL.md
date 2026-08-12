---
name: Rehire Reactivation
description: Safely restore a disabled account for a returning employee — authorization verified, old group memberships reviewed against the new role, credentials reset fresh. Use when a ticket asks to re-enable, reactivate, or restore a former employee's account.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Rehire Reactivation

**When to use:** "<user> is coming back — reactivate their old account" / "re-enable <user>, rehired for a different role" / "restore access for a returning contractor" / a new-hire ticket where the person already has a disabled account.

**Run it:** on one ticket — authorization- and least-privilege-gated, so a human confirms before re-enabling.

## Prompt

```
Bring this returning employee back without inheriting stale risk: authorize the
reactivation, re-review the account's frozen access against the NEW role, and let
nothing from the old life (sessions, MFA methods, delegations) survive unexamined. A
rehire is an onboarding with a used account, not an undo of the offboarding.

1. Verify authorization: the rehire must be confirmed by HR, the manager, or the
   client's documented authorized contact — never re-enable on the former employee's
   own request. Confirm the account is disabled for departure and not for a security
   incident or litigation hold: check the object's description field (offboarding
   stamps the ticket number there) and search the tickets for the offboarding and any
   hold. An account disabled for cause or under hold does NOT get reactivated without
   explicit clearance.

2. Establish the new role: title, department, manager, start date.

3. Review the frozen access against the new role before re-enabling: list the
   account's groups, licenses (likely removed), delegations, app assignments. Keep
   only what the new role's profile justifies; strip everything else — especially
   admin or elevated memberships from the old role. Where a role profile exists,
   rebuild from the profile rather than trusting leftovers.

4. Reset the credential surface completely: new password (change forced at next
   sign-in, delivered per secure-transfer policy), all old MFA methods removed and
   enrollment required fresh, no old sessions or app passwords surviving. Old
   registered devices get reviewed and removed unless the client confirms they were
   returned-and-reissued.

5. Re-enable, reassign licenses per License Lifecycle (approval for cost), and restore
   mailbox state per policy — if the mailbox was converted to shared, confirm with the
   client whether to convert back or start clean.

6. If hybrid, run an AD Connect delta sync and verify before the start date. Post a
   plain-text note: authorization source, old-access review outcome (kept/stripped),
   credential reset status, remaining pending items. Confirm timeline to me and log
   time.

Guardrails: no reactivation without verified authorization from HR/manager on file, and
explicit clearance if the account was disabled for cause or is under any hold. Never
re-enable with old group memberships intact "to save time" — the least-privilege review
against the new role is the core of this skill. All old MFA methods and sessions are
invalidated; the returning user enrolls fresh. Passwords only via secure transfer,
change forced at next sign-in. If the gap since departure exceeds the client's
account-retention policy or the account was deleted, run New Hire Onboarding instead of
resurrecting.
```
