---
name: Break-Glass Account Audit
description: Audit Entra emergency-access break-glass accounts: Conditional Access exclusions, sealed credentials, sign-in alerting, and quarterly test.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Break-Glass Account Audit

**When to use:** A quarterly emergency-access audit for a managed tenant, before enabling or changing any Conditional Access policy (paired with conditional-access-review and security-defaults-vs-ca migrations), when nobody knows where a client's emergency admin credentials are, or after an incident or lockout where break-glass was (or should have been) used. A break-glass account is insurance that only pays out if it was maintained: excluded from every policy, credentials actually retrievable, alerts firing on use, and tested recently enough to trust. This audit verifies all four — because the discovery moment for a broken break-glass account is a tenant lockout.

**Run it:** as an on-demand audit across the tenant's emergency-access accounts and every CA policy — you compile findings and build remediation tickets, a technician walks the policies and runs the test sign-in (not a Flow: no schedule trigger, and it needs a human at the console).

## Prompt

```
Prepare a break-glass account audit. You compile findings and remediation tickets; the tech
walks the policies and runs the test sign-in. Credentials appear in no ticket, note, chat,
email or document — only the storage reference and custody procedure.

1. Existence and construction. Verify two emergency-access accounts exist, each cloud-only on
   *.onmicrosoft.com — not federated, not synced, so an AD or federation outage can't kill them
   — holding Global Administrator, not tied to anyone's daily identity, named per the MSP
   standard in the client's documentation; note it if IT Glue or Hudu isn't connected
   (Connector Degradation base skill). Mis-built accounts get remediation tickets, not silent
   fixes.

2. Exclusion sweep. The tech walks EVERY Conditional Access policy — enabled, report-only and
   disabled — and confirms both accounts are excluded. Also confirm exclusion from Identity
   Protection auto-remediation and from any PIM requirement gating activation behind systems
   that may be down — their Global Administrator is a standing assignment. Never fix a missing
   exclusion by disabling the policy: add it through the normal change process and record how a
   policy shipped without it. Say how many policies were walked and what you couldn't check
   (Sweep Honesty base skill).

3. Credential custody. Verify storage follows the documented procedure: sealed (safe, envelope
   or vault with dual control), split from each other, not dependent on one person's phone or
   an MFA method that dies with one device. FIDO2 keys in separate secure locations are the
   strong pattern; a long sealed password the floor. Confirm the storage reference and who can
   reach it.

4. Usage alerting. Verify an alert fires on ANY sign-in by these accounts, to a monitored
   destination. Review sign-in history since the last audit: any use outside a documented drill
   or emergency is treated as compromise and escalated before the audit continues.

5. Quarterly test: actually sign in. Announce the drill window to whoever monitors the alert,
   retrieve credentials per procedure, sign in, confirm Global Administrator access and that
   the alert fired, sign out, re-seal or rotate. An untracked login by the envelope holder is a
   finding. Record the test date; untested within the cadence is unverified insurance.

6. Leave a plain-text note, no markdown or emojis (PSA Note Discipline base skill):
   construction, exclusions with the policy count checked, custody reference, alerting and
   drill results with dates, findings and remediation tickets, and the next audit scheduled.
   Update the client's break-glass procedure if it changed, and ensure hygiene automations
   (stale-account cleanup, MFA sweeps) exclude these accounts by design.

When in doubt about an unexplained sign-in or a missing exclusion, escalate per the client's
security process.
```
