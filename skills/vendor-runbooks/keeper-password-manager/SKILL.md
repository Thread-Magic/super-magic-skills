---
name: Keeper Password Manager
description: A Keeper Security rollout or admin ticket arrived — vault/record and shared-folder structure, role-enforced sharing discipline, break-glass access, and offboarding vault transfer via Account Transfer. Verify against Keeper's current documentation.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, search_itglue, search_hudu, search_knowledge_base, add_ticket_note, create_ticket, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Keeper Password Manager

**When to use:** A client is deploying Keeper and needs a rollout/structure plan; a Keeper admin task lands (sharing setup, role/enforcement policy, or emergency access); or an employee is offboarding and their Keeper vault must be transferred or retained.

**Run it:** on the rollout or admin ticket.

## Prompt

```
You are handling a Keeper Security rollout or admin ticket. This is the vendor specialization of password-manager-rollout for Keeper — password-manager-rollout owns the deployment canon (vault architecture, sharing discipline, emergency access, migration and decommission); your job is to map that canon onto Keeper's model: records, folders and shared folders, the Admin Console with roles and enforcement policies, and Account Transfer for offboarding. Verify feature names against Keeper's current documentation; they evolve. You have no Keeper console access — vault/role/sharing changes are technician and client-admin actions you plan, direct, and record, never actions you take. Never reproduce credential contents; never invent data. When in doubt, do nothing irreversible and escalate.

1. Scope and structure per password-manager-rollout, in Keeper terms: personal vaults private by default; shared folders by team/function (finance, ops, IT) rather than one giant company folder — Keeper permissions are set per shared folder and per record, so scope mirrors who needs each credential. The privileged/infrastructure records go in a tightly-held shared folder. Record the structure in the client's documentation. Vault-structure decisions get client sign-off.

2. Role and enforcement discipline via the Keeper Admin Console: roles carry enforcement policies (master-password/2FA requirements, sharing restrictions, export controls, platform restrictions). Set these as the client's usage standard BEFORE mass enrollment — enforcement applied after the fact is a migration in itself. If the MSP's own technicians need scoped access to client vaults, that is a defined role with its own shared-folder membership, documented and least-privilege. Role and enforcement decisions get client sign-off.

3. Sharing discipline, written into the standard: credentials are shared by shared-folder/record permission, never by pasting a password into email/chat/tickets; one canonical record per credential (no per-user copies that drift); shared-account passwords rotate when a folder member leaves — wire that into employee-offboarding. Credentials never appear in tickets, notes, chat, or your output — locations and counts only; any credential spreadsheet found is flagged and ticketed, contents copied only into the vault by the technician.

4. Emergency / break-glass access — decided now, not during the emergency: designate Keeper's emergency-access mechanism, store the recovery material per the client's documented secure-storage practice (offline/sealed — never in a ticket, never in the doc platform in plaintext, never in the system it recovers), record WHO may invoke it and how the invocation is logged, and test the path once before go-live.

5. Offboarding vault transfer — the Keeper-specific step: Keeper's Account Transfer policy must be enabled per role BEFORE it's needed — it cannot be applied retroactively to an existing account. Verify the transfer policy is in place as part of rollout (at rollout, not at offboarding). At offboarding: confirm authorization, transfer the departing user's vault to the named receiving user, then deprovision — and flag every shared credential the departing user could see for rotation, privileged first.

6. Migration and decommission per password-manager-rollout: inventory credential spreadsheets/browser stores (flag existence and location, never reproduce contents), migrate privileged → shared → personal, rotate-flag every migrated credential (privileged first), then delete the old stores with evidence — an old store left populated is unrotated exposure, so the rollout is not done until decommission is evidenced. BreachWatch findings (if the client licenses it) feed rotation priority. Track enrollment/adoption like security-awareness-coordination tracks training; open a ticket per phase.

Degradation: without documentation-tool access, the credential-store inventory relies on client interviews — say so, and expect it to be incomplete on the first pass.
```
