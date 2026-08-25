---
name: Credential Stuffing Response
description: Investigate password spraying and credential stuffing patterns: scope the attack across tenants, lock down accounts, and rotate the ones that fell.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Credential Stuffing Response

**When to use:** A spike of failed sign-ins spread across many accounts or repeated logins from unfamiliar IPs; an "unusual sign-in volume," "password spray," or "credential stuffing" alert; or a known breach dump prompts a check for replayed reused passwords.

**Run it:** on one ticket (managed as a single campaign/incident, not one ticket per account).

## Prompt

```
The signature here is breadth, not depth: many accounts hit, often one or few attempts each
(spraying), or a flood of logins using credentials leaked elsewhere (stuffing). Scope the
campaign, harden the front door, and rotate the accounts that actually succumbed — without
drowning the desk in per-account tickets. Work it in order:

1. Scope the campaign before touching individual accounts: how many accounts targeted, over
   what window, from which IPs/ranges/geographies, and — the pivotal split — which attempts
   FAILED versus which SUCCEEDED. A thousand failures is noise-to-harden; one success is a
   takeover to contain; the response diverges completely from there.
2. For any account where a login SUCCEEDED: treat it as compromised and contain per
   account-takeover-runbook (rotate password, revoke sessions and tokens, sweep rules and
   consents). Successful stuffing means that password was valid and is now known.
3. For the targeted-but-failed population: the passwords weren't guessed, but the accounts
   are now known targets. Prioritize MFA coverage on any that lack it and flag legacy-auth
   and non-MFA sign-in paths, which spraying hunts for.
4. Harden the front door at the tenant level: enforce MFA on all accounts, disable
   legacy/basic authentication, enable smart lockout and anomalous-sign-in protection, and
   consider conditional-access blocks on the attacking IP ranges and geographies. This is the
   fix that turns the campaign into noise.
5. Address exposed and reused credentials: if the source is a known breach dump of reused
   passwords, drive rotation for affected users (branch to breached-credential-response) and
   reinforce that reused passwords are the fuel.
6. Correlate, don't spam: manage the campaign as ONE incident with a scoped account list,
   not one ticket per failed login. Search related tickets to fold in related alerts.
7. Document the decision, not just the action: attack scope (accounts, IPs, window), the
   success/fail split, which accounts were contained, the hardening recommendations with
   their owner, and residual risk. Classify per soc-classification-tree.

Lockout policy, MFA enforcement, legacy-auth disablement and conditional-access changes are
tenant-wide admin actions owned by the client — recommend and drive them, never flip tenant
auth settings yourself. Watch for over-aggressive lockout as a self-inflicted denial of
service: a spray can be designed to lock real users out, so tune thresholds with them.
Never soft-close a successful stuffing login as "just one of many attempts" — it is a
compromised account and gets full containment. Write defensively: "a login attack targeting
multiple accounts was detected", not "you were breached", and call only accounts with a
confirmed successful sign-in compromised. Never invent data. When in doubt, harden MFA and
contain the confirmed successes.
```
