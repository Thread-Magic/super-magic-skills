---
name: MFA Methods Audit
description: Audit Entra MFA authentication methods per user: phone-only risk, push without number matching, and missing phishing-resistant methods for admins.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# MFA Methods Audit

**When to use:** A ticket asks to audit what MFA methods a client's users actually have, insurance/compliance asks for "phishing-resistant MFA" and nobody knows the gap size, you're planning a move off SMS/voice or onto FIDO2 keys / passkeys, or you're following up after a successful phishing incident against an MFA-enabled account. Coverage (who has MFA at all) is the identity-mfa-health-check skill; this one grades the methods of those who do. Individual reset requests stay with the password-and-mfa-recovery ladder.

**Run it:** as an on-demand grade across every user's registered methods — you prepare, grade, and verify, a technician pulls exports and executes policy changes (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
"Everyone has MFA" hides a quality spectrum. Grade the tenant's registered methods per user and
plan upgrades without stranding anyone methodless. The tech pulls exports and executes policy
changes; you prepare, grade and verify.

1. Pull the registration data. The tech exports Entra's authentication-methods registration
   report: per user, the methods registered (SMS, voice, Authenticator push, TOTP, FIDO2 or
   passkey, Windows Hello, certificate) and the default. Date the export and label counts
   point-in-time (Sweep Honesty base skill — say "at least N" where a list may be capped).

2. Grade into tiers, worst first:
   - Tier 0, phone-only (SMS or voice the only method): SIM-swap and phone-forward attacks
     apply; always the first finding.
   - Tier 1, Authenticator push without number matching: open to MFA-fatigue prompt bombing.
     Microsoft now enforces number matching by default — confirm the tenant, don't assume.
   - Tier 2, Authenticator with number matching, or TOTP: baseline for general users.
   - Tier 3, phishing-resistant (FIDO2 keys, passkeys, Windows Hello for Business,
     certificates): required for privileged accounts.

3. Overlay privilege. Any privileged account below Tier 3 is a high finding, one at Tier 0
   critical. Flag single-method users of any tier — one lost device from a lockout.

4. Check the policy side. In the Authentication Methods policy: are SMS and voice still enabled
   tenant-wide, is Authenticator set for number matching and app context, are FIDO2 and
   passkeys enabled for the groups that need them? Policy allowing weak methods is its own
   finding.

5. Plan every upgrade as register-then-remove. Users register the stronger method FIRST, verify
   it with a real sign-in, and only then is the weak one disabled by policy for their group.
   Never disable a method class while anyone depends on it as their only method. Roll by group
   with comms and a registration campaign, shared with SSPR.

6. Approval gate. Disabling a method class changes every affected user's sign-in: send an
   approval request to the client authority with the affected count, schedule, comms plan, and
   rollback (re-enable the method in policy).

7. Leave a dated plain-text summary note, no markdown or emojis (PSA Note Discipline base
   skill): tier counts, privileged findings, single-method users, policy findings, and the
   upgrade plan as one ticket per phase. Full per-user lists go to the client's documentation,
   not a PSA-synced note; note it if IT Glue or Hudu isn't connected (Connector Degradation
   base skill). Schedule the re-audit.

Never remove or disable a user's only working method: register first, verify, then remove.
Re-pull counts before executing a phase planned weeks earlier, and verify portal and PowerShell
steps against Microsoft's current docs. When in doubt, do nothing and escalate.
```
