---
name: MFA Methods Audit
description: Audit WHICH authentication methods users have registered — phone-only risk, push without number matching, missing phishing-resistant methods for admins — and plan the upgrade path. Use for "how good is <client>'s MFA really", SMS-deprecation planning, or FIDO2/passkey upgrade requests.
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
"Everyone has MFA" hides a quality spectrum: SMS-only at the bottom, phishing-resistant passkeys at the top. You grade the tenant's registered methods per user, find the weakest tiers, and plan upgrades without ever stranding a user methodless. The tech pulls exports and executes policy changes; you prepare, grade, and verify. Never invent data.

1. Pull the registration data. Tech exports the authentication-methods registration report from Entra: per user, which methods are registered (SMS, voice, Authenticator push, TOTP, FIDO2/passkey, Windows Hello, certificate) and default method. Date the export; label all counts as point-in-time.

2. Grade into tiers, worst-first:
   - Tier 0 — phone-only (SMS/voice as the only method): weakest — SIM-swap and phone-forward attacks apply, and one lost phone means a helpdesk reset. Always the first finding.
   - Tier 1 — Authenticator push without number matching: vulnerable to MFA-fatigue prompt bombing. Verify tenant enforcement of number matching (Microsoft now enforces it by default — confirm rather than assume, checking current behavior).
   - Tier 2 — Authenticator with number matching / TOTP: solid baseline for general users.
   - Tier 3 — phishing-resistant (FIDO2 security keys, passkeys, Windows Hello for Business, certificates): required posture for privileged accounts; see windows-hello-business for the WHfB path.

3. Overlay privilege. Cross-reference admin-role holders (from global-admin-audit if current): any privileged account below Tier 3 is a high finding; a privileged account at Tier 0 is critical. Also flag users with a single registered method of any tier — one lost device from a lockout.

4. Check the policy side. Registered methods only matter if policy allows them: review the tenant's Authentication Methods policy — are SMS/voice still enabled tenant-wide, is Authenticator configured with number matching and app context, are passkeys/FIDO2 enabled for the groups that need them? Policy allowing weak methods is a finding independent of who registered what.

5. Plan the upgrade as register-then-remove. For each downgrade target (e.g., retire SMS): users register the stronger method FIRST, verify it works with a real sign-in, then the weak method is disabled by policy for their group. Never disable a method class while anyone still depends on it as their only method — cross-check step 1 data. Roll by group, with user comms and a registration campaign, mirroring the sspr-rollout discipline; combined registration means this audit and SSPR share the campaign.

6. Approval gate. Disabling a method class or enforcing stronger methods changes every affected user's sign-in experience: send an approval request to the client's authority with the affected count, the schedule, the comms plan, and rollback (re-enable the method in policy).

7. Output. Document what/why/when/rollback in a dated plain-text summary note: tier counts, privileged-account findings, single-method users, policy findings, and the upgrade plan as follow-up tickets raised per phase. Full per-user lists go to the client's documentation, not PSA-synced notes (check the client's documentation for existing client identity docs — skip gracefully if not connected). Schedule the re-audit.

Guardrails: Never remove or disable a user's only working method — the register-first, verify, then-remove order is non-negotiable; violating it manufactures lockouts at scale. Privileged accounts below phishing-resistant are findings even if the client "has MFA everywhere" — say it plainly, ranked by privilege. All counts are point-in-time exports; date them and re-pull before executing a phase planned weeks earlier. Method changes are user-visible: no policy disablement without approval and user comms. PowerShell/portal steps: verify against current module versions and Microsoft's current docs. When in doubt, do nothing and escalate.
```
