---
name: Offboarding Completeness Audit
description: Post-offboarding sweep for licenses still assigned, live delegations, unreturned devices, lingering MFA methods and sessions, and external share links.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_itglue, search_knowledge_base, add_ticket_note, create_ticket, update_ticket, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Offboarding Completeness Audit

**When to use:** "Double-check <user>'s offboarding — did we get everything?" / a weekly sweep of departures in the last N days / before a client security review or license true-up / an offboarding closed fast under pressure that deserves a calm second pass.

**Run it:** on one departed user's offboarding (or each in a set you point me at) — a read-and-report pass a human reviews.

## Prompt

```
Catch what the offboarding missed while it's still cheap to fix: a checklist-driven
sweep of a departed user's residual footprint, findings raised as actionable
follow-ups. Run it on the user I name, or on each departed user in the set I point you
at.

1. Identify the departed user(s) and pull the offboarding ticket(s) (search the tickets,
   look up the contact) plus the client's offboarding SOP (knowledge base / IT Glue
   documentation) as the baseline of what should have happened.

2. Sweep the residual footprint against the checklist, verifying each from EVIDENCE,
   not from the offboarding ticket's claims:
   - Account: sign-in actually disabled; sessions revoked; password reset.
   - MFA: no registered methods remain; no app passwords or trusted devices.
   - Licenses: none still assigned (billing leak — cross-check License Lifecycle notes
     and the billing view).
   - Mailbox: converted/forwarded per policy BEFORE license removal; no forwarding
     rules to external personal addresses.
   - Delegations: no surviving Full Access / Send As grants held BY the user on other
     mailboxes; delegations TO the departed mailbox reviewed.
   - Groups and DLs: removed from security groups and distribution lists.
   - Devices: hardware returned or tracked; managed-device enrollment
     disabled/retired; no active remote-access tooling.
   - External shares: file/folder sharing links owned by the user, and any third-party
     OAuth consents still alive.
   - AD hygiene: object disabled, ticket number stamped in description, moved to the
     disabled OU per policy, AD Connect sync reflected.

3. Classify each finding: SECURITY (live access path — sessions, MFA method,
   delegation, external forward) vs COST (license still burning) vs HYGIENE (naming,
   OU, documentation).

4. For SECURITY findings, flag immediately on the offboarding ticket and to the
   client's contact per policy; for the rest, open follow-up tickets with owners
   rather than a passive list.

5. Post a plain-text audit note: user, offboarding ticket reference, each checklist
   item PASS / FAIL / UNVERIFIABLE (with why), findings by class, follow-up ticket
   references. State clearly which items couldn't be verified with available access —
   an unverifiable item is NOT a pass. Log time.

Guardrails: verify from evidence; never mark an item PASS because the offboarding note
said it was done. This audit is read-and-report — it opens follow-ups but does not
itself revoke, delete, or convert anything (remediation runs through the owning skill
with its own confirmations). Never write "breach" or "compromised" for a residual
access path — report it as an open item requiring closure. UNVERIFIABLE is an honest
verdict; say what access would be needed to check. Do not include credentials or
personal data beyond what the finding requires. If the departed user or offboarding
ticket can't be identified with confidence, say so and stop rather than guessing.
```
