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
Choose the correct group type, and where asked plan a DL-to-M365-Group upgrade with the
blockers checked first. The tech executes in Exchange/Entra or PowerShell. Apply the Write
Guardrails base skill — never invent data, never report creation as done on intention, when
in doubt do nothing and escalate.

1. Ask what the group is FOR, not what it's called:
   - Fans out email only — Distribution List: lightest footprint, supports nesting.
   - Email plus a shared workspace (files, calendar, Teams, Planner) — M365 Group. It
     provisions a mailbox, SharePoint site and calendar; say so out loud. Never create one
     when the need is only an email alias.
   - Permissions on resources AND email — mail-enabled security group; permissions only, no
     email — plain security group in Entra, not Exchange.
   - Membership by attribute (everyone in department X) — dynamic membership; needs Entra ID
     P1, so verify licensing first.
   If people must WORK from the address — reply, triage, own — steer to a shared mailbox
   (shared-mailbox-creation); a DL to five inboxes makes five uncoordinated copies.

2. External mail: should outside senders reach it? DLs and M365 Groups default to
   internal-only (RequireSenderAuthenticationEnabled $true). A support@ or sales@ clients
   email needs it flipped deliberately — that creates spoofing surface, so it is an explicit,
   approved decision, never a default.

3. DL to M365 Group upgrade: check the blockers first. A DL cannot be upgraded if it is
   synced from on-premises AD, nested (contains groups or belongs to one), a mail-enabled
   security group, has send-on-behalf settings, is moderated, or is hidden from the GAL.
   Confirm against Microsoft's current eligibility list — it shifts. Ineligible DLs get
   recreated and cut over instead: different membership management, plus a comms plan. Tell
   the client the upgrade consumes the DL; never promise reversibility.

4. Approval and naming. Creation is user-visible (GAL entry, possible Teams/SharePoint
   provisioning): confirm name, address, owners (two minimum — single-owner groups orphan)
   and privacy with the client. Check the tenant's naming policy and creation restrictions
   and documented client standards (Connector Degradation base skill if IT Glue is off).

5. Execution (verify module versions): New-DistributionGroup, with -Type Security for
   mail-enabled security; New-UnifiedGroup for M365 Groups; or the admin-center flow.
   Upgrades use the EAC upgrade action or Upgrade-DistributionGroup.

6. Verify: mail lands or fans out, the M365 Group workspace provisioned, owners can manage
   it. Note it (PSA Note Discipline base skill: plain text, no
   markdown) — type chosen and WHY, name, address, owners, external mail, privacy,
   approver, date, rollback (remove the group; an upgrade deletes the DL, so rollback is
   recreating it). Log time.
```
