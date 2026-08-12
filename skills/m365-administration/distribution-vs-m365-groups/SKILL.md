---
name: Distribution vs M365 Groups
description: Pick between distribution lists, Microsoft 365 Groups, mail-enabled security groups, and dynamic groups, and handle DL-to-M365-Group upgrades.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise]
---

# Distribution vs M365 Groups

**When to use:** A ticket maps a vague "we need a group" request onto the group type that actually fits — "create a group email for the sales team," "should this be a distribution list or a Team?", "upgrade our old distribution lists to Microsoft 365 Groups," or "we need a group we can also use for permissions." The point is preventing the two classic mistakes: creating a full M365 Group (with a SharePoint site and Planner) when the client wanted an email alias, and trying to "upgrade" a DL that can't be upgraded. NOT for adding/removing members of an existing list — that is distribution-list-management.

**Run it:** on one client's request — you choose the right type and plan any upgrade, a technician executes in Exchange/Entra or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You are choosing the correct group type for a request and, where asked, planning a DL-to-M365-Group upgrade with the hard blockers checked first. You prepare and verify; the technician executes in Exchange/Entra or PowerShell. Never report creation as done on intention — never invent data.

1. Ask what the group is FOR, not what it should be called (read the ticket for context):
   - Just an address that fans out email → Distribution List. Lightest footprint, supports nesting, no extra workloads created.
   - Email plus a shared workspace (files, shared calendar, Teams, Planner) → M365 Group. Creating one provisions a mailbox, SharePoint site, and calendar — say that out loud; clients asking for "a group email" are often surprised by the workspace sprawl. Never create an M365 Group when the stated need is only an email alias.
   - Granting permissions to resources AND receiving email → Mail-enabled security group.
   - Permissions only, no email → plain security group (Entra, not Exchange).
   - Membership by attribute (all users in department X) → dynamic membership, which requires Entra ID P1 licensing — verify licensing before promising it.

2. Ask the external-mail question for anything that receives email: should outside senders be able to mail it? DLs and M365 Groups both default to internal-only (RequireSenderAuthenticationEnabled $true); a support@ or sales@ that clients email needs that flipped deliberately — and that makes it spoofing/phishing surface worth noting. External-mail enablement is an explicit, approved decision, never a default.

3. If the group receives email people must WORK from (reply, triage, own), steer to a shared mailbox instead (shared-mailbox-creation) — a DL that fans out to five inboxes creates five uncoordinated copies; that's the root of "two people answered the same customer" tickets.

4. For DL → M365 Group upgrade requests, check the hard blockers before promising anything. A DL cannot be upgraded if it is: synced from on-premises AD, nested (contains groups or is a member of one), a mail-enabled security group, has send-on-behalf settings, is moderated, or is hidden from the GAL. Have the tech verify against the current eligibility list in Microsoft's current docs — the list shifts. Ineligible DLs get recreated-and-cutover instead, which changes membership management and needs a comms plan. Tell the client the DL is consumed by the upgrade; do not promise reversibility.

5. Approval and naming: group creation is user-visible (GAL entry, possible Teams/SharePoint provisioning) — confirm name, address, owners (at least two — single-owner groups orphan), and privacy (public/private for M365 Groups) with the client via an approval request. Check the tenant's group-naming policy and creation restrictions (check the client's documentation for documented standards; skip gracefully if not connected) before the tech hits create.

6. Prepare execution for the tech (PowerShell labeled: verify against current module versions): New-DistributionGroup (add -Type Security for mail-enabled security), New-UnifiedGroup for M365 Groups, or the admin-center flow. For upgrades: the EAC upgrade action or Upgrade-DistributionGroup.

7. Verify via evidence: mail to the address fans out / lands; for M365 Groups the workspace provisioned; owners can manage membership. Document what/why/when/rollback in a plain-text note: group type chosen and WHY (the decision from step 1), name/address, owners, external-mail setting, privacy, approver, date, and rollback (remove group; for upgrades note the DL is deleted by the upgrade and rollback means recreating it). Log time.

When in doubt about the right type or a possible collision, do nothing and escalate.
```
