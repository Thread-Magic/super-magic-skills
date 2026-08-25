---
name: M365 Group Lifecycle
description: Govern Microsoft 365 Groups lifecycle: creation controls, naming, expiration and renewal, ownership handoff, and clean retirement of dead groups.
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
You prepare and verify; the tech executes the portal and Graph changes. Apply the Write
Guardrails base skill — never report a policy as applied on intention, and when in doubt
about scope or a data-bearing group do nothing and escalate.

Every M365 Group carries a mailbox, SharePoint site, calendar and, if a team, Teams, so every
rule here ripples into all of them. Keep this aligned with teams-governance — naming and
expiration are one policy, not two.

1. Confirm which surfaces are affected and pull the documented client group-governance
   standard from their documentation, the knowledge base and prior tickets (Connector
   Degradation base skill if it isn't connected).

2. Creation control: any user can create groups by default, or only an approved security
   group. Restriction applies to every group-creating surface — Teams, Outlook, SharePoint,
   Planner — and needs the right directory setting. Keep a self-service request path, or it
   just pushes people to shadow IT.

3. Naming policy: prefix/suffix convention plus a blocked-words list. It requires Entra ID P1
   for every affected user and applies to all groups tenant-wide. Existing groups are not
   renamed retroactively.

4. Expiration and renewal: set an expiration period; active groups auto-renew on activity,
   inactive ones are soft-deleted and recoverable for 30 days. Also needs Entra ID P1. The
   trap: an ownerless group cannot be renewed by anyone and will expire, so fix ownership
   (step 5) before switching expiration on.

5. Ownership hygiene: two owners minimum per group. Find ownerless groups and assign owners,
   asking the client who owns each business function. Single-owner groups orphan the moment
   that person leaves.

6. Retirement: confirm with the client that the group and its workloads — mailbox, site,
   files — are genuinely unused, preserve or export anything needed, then delete (soft-delete
   is recoverable for 30 days). Never assume a quiet group is dead.

7. Approval and execution. Creation restriction, naming and expiration are tenant-wide and
   user-visible: get client sign-off on the specifics and on any groups slated for
   retirement. Prepare for the tech (verify current portals, module versions and Microsoft's
   docs): Entra admin center group settings, `Set-AzureADDirectorySetting` or Microsoft Graph
   for naming and creation control, the expiration policy in Entra, deletion via the admin
   center. Verify: creation obeys the restriction and convention, expiration shows the agreed
   period, ownerless groups resolved, retired groups gone and recoverable within 30 days.
   Note it (PSA Note Discipline base skill: plain text, no markdown) — policies set,
   licensing prerequisite, ownership fixed, groups retired, approver, date, rollback (remove
   the policy, restore a soft-deleted group within 30 days; capture prior settings first).
   Log time.
```
