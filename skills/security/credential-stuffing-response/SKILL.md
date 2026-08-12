---
name: Credential Stuffing Response
description: A pattern of failed/anomalous logins across many accounts points to password spraying or credential stuffing — scope the attack, lock down, and rotate the accounts that actually fell.
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
The signature here is breadth, not depth: many accounts hit, often one or few attempts
each (spraying), or a flood of logins using credentials leaked elsewhere (stuffing). Scope
the campaign, harden the front door, and rotate the accounts that actually succumbed —
without drowning the desk in per-account tickets. Work it in order:

1. Scope the campaign before touching individual accounts: how many accounts targeted,
   over what window, from which IPs/ranges/geographies, and — the pivotal split — which
   attempts FAILED versus which SUCCEEDED. A thousand failures is noise-to-harden; one
   success is a takeover to contain.
2. For any account where a login SUCCEEDED: treat as compromised — contain per
   account-takeover-runbook (rotate password, revoke sessions/tokens, sweep
   rules/consents). Successful stuffing means that password was valid and is now known.
3. For the targeted-but-failed population: the passwords weren't guessed, but the accounts
   are now known targets. Prioritize MFA coverage on any that lack it and flag
   legacy-auth / non-MFA sign-in paths, which spraying specifically hunts for.
4. Harden the front door at the tenant level (client admin-owned, recommend and drive):
   enforce MFA on all accounts, disable legacy/basic authentication, enable smart lockout /
   anomalous-sign-in protection, and consider conditional-access blocks on the attacking IP
   ranges/geographies. This is the fix that turns the campaign into noise.
5. Address exposed/reused credentials: if the source is a known breach dump of reused
   passwords, drive rotation for affected users (branch to breached-credential-response)
   and reinforce that reused passwords are the fuel.
6. Correlate, don't spam: manage the campaign as ONE incident with a scoped account list,
   not one ticket per failed login. Search related tickets to fold in related alerts.
7. Document the decision, not just the action: attack scope (accounts, IPs, window), the
   success/fail split, which accounts were contained, the hardening recommendations with
   their owner, and residual risk. Classify per soc-classification-tree.

Guardrails — always:
- Separate failures from successes on the first pass — the response diverges completely.
  Contain the successes; harden around the failures.
- Lockout policy, MFA enforcement, legacy-auth disablement, and conditional-access changes
  are tenant-wide admin actions owned by the client — recommend and drive; never flip
  tenant auth settings yourself.
- Beware over-aggressive lockout as a self-inflicted denial of service — a spray can be
  designed to lock out real users; tune with the client.
- A successful stuffing login = compromised account = full containment; never soft-close it
  as "just one of many attempts."
- Defensive writing: "a login attack targeting multiple accounts was detected," not "you
  were breached"; only accounts with a confirmed successful sign-in are described as
  compromised. Plain text only; never invent data. When in doubt, harden MFA and contain
  the confirmed successes.
```
