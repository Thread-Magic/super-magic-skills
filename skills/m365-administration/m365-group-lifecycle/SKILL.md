---
name: M365 Group Lifecycle
description: Govern the full life of Microsoft 365 Groups — who can create them, naming, expiration/renewal, ownership, and clean retirement — and keep the group-vs-DL-vs-security-group decision straight. Use when a client asks to control group sprawl, set who can make groups/teams, handle expiring or ownerless groups, or clean up dead groups.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# M365 Group Lifecycle

**When to use:** A client asks who can create groups/teams and whether that can be restricted, wants group expiration/renewal set up, has ownerless and abandoned groups, or wants a group retired cleanly. A group is the backing object for Teams, a SharePoint site, a mailbox, and a calendar all at once, so an ungoverned group is four kinds of sprawl. For picking the RIGHT object type in the first place, see distribution-vs-m365-groups; for Teams-specific naming/guest work, teams-governance (which shares this policy — keep them aligned).

**Run it:** on one client's request — you prepare and verify, a technician executes the portal/Graph changes (not a Flow: it needs a human at the console).

## Prompt

```
You are governing Microsoft 365 Group lifecycle for a client. The agent prepares and verifies; a technician executes the portal/Graph changes. Never report a policy as applied on intention, and never invent data.

Every M365 Group carries a mailbox, a SharePoint site, a calendar, and (if a team) Teams — so lifecycle rules here ripple into all of those. Coordinate with teams-governance so naming/expiration are one policy, not two conflicting ones.

1. Frame the blast radius before setting policy. Confirm which surfaces are affected and pull any documented client group-governance standard (check the client's documentation — connector-gated, skip gracefully if neither is connected; the knowledge base; and prior tickets).

2. Creation control: decide whether any user can create groups (the default) or only an approved security group. Restricting creation is a common "stop the sprawl" ask — note it applies to all group-creating surfaces (Teams, Outlook, SharePoint, Planner) and needs the right directory setting. Keep a self-service request path so restriction doesn't just push people to shadow IT.

3. Naming policy: prefix/suffix convention + blocked-words list. State the prerequisites plainly — a naming policy requires Entra ID P1 for every affected user and applies to all groups tenant-wide. Existing groups are not renamed retroactively.

4. Expiration/renewal: set a group-expiration period; active groups can auto-renew based on activity, inactive ones are soft-deleted and recoverable for 30 days. Also requires Entra ID P1. The trap: an ownerless group can't be renewed by anyone and will expire — so fix ownership first (step 5) before switching expiration on.

5. Ownership hygiene: enforce a minimum of two owners per group; find and remediate ownerless groups by assigning owners (ask the client who owns each business function). Single-owner groups orphan the moment that person leaves.

6. Retirement: retire a dead group cleanly rather than leaving it to rot — confirm with the client the group and its workloads (mailbox, site, files) are truly unused, export/preserve anything needed, then delete (soft-delete is recoverable for 30 days). Never hard-assume a quiet group is dead.

7. Approval + execution. Creation restriction, naming, and expiration are tenant-wide and user-visible — get client sign-off (send an approval request) with the policy specifics and any groups slated for retirement. Prepare execution for the tech (verify against current portals / module versions and Microsoft's current docs): Entra admin center group settings, `Set-AzureADDirectorySetting` / Microsoft Graph for naming and creation control, expiration policy in Entra, group deletion via admin center. Verify: new-group creation obeys the restriction/convention; expiration shows the agreed period; ownerless groups resolved; retired groups gone (and recoverable within 30 days). Leave a plain-text note: policies set (creation control, convention, expiration period, licensing prerequisite), ownership fixed, groups retired, approver, date, and rollback (remove policy; restore soft-deleted group within 30 days — capture prior settings as rollback). Log time.

Guardrails: Naming and expiration policies need Entra ID P1 for all users and hit every group tenant-wide — verify licensing and scope first. Fix ownerless groups (two owners minimum) BEFORE enabling expiration, or they expire silently. Restricting creation without a self-service request path drives shadow IT — keep a path. Never assume a quiet group is dead; confirm and preserve data before retirement. Keep this policy consistent with teams-governance. When in doubt about scope or a possible data-bearing group, do nothing and escalate.
```
