---
name: SharePoint Site Provisioning
description: Provision new SharePoint sites and document libraries with site type, permission model, and sharing defaults chosen deliberately not inherited.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# SharePoint Site Provisioning

**When to use:** A client asks to "create a new SharePoint site for <team/project>," "set up a shared document library for X," or "a place to store client files." NOT for fixing permissions on an existing site after a leak (that is a security review), and NOT for OneDrive personal storage governance — that is onedrive-storage-governance. This skill provisions a new site or library with the permission model and sharing posture chosen up front, because the default "everyone can share with anyone" and broken inheritance are the two things that turn a tidy site into a data-leak later.

**Run it:** on one client's request — you prepare and verify, a technician executes in the admin center or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You provision a new SharePoint site or library with its permission model and sharing posture
chosen deliberately, not inherited. You prepare and verify; the technician executes in the
admin center or PowerShell. Verify the admin surface against current docs.

1. Decide the site TYPE from the purpose and name the trade-off. A Team site is M365
   Group-backed: membership-based collaboration with Teams and Planner, and it provisions a
   whole M365 Group, so name and owners follow m365-group-lifecycle. A Communication site is
   intranet broadcast: many readers, few authors, no membership model. A document library on
   an EXISTING site fits when the ask is really "a folder area", and avoids sprawl. Pick the
   lightest option that fits.

2. Permission model: SharePoint groups (Owners, Members, Visitors), never direct per-user
   grants, and never break inheritance on a folder without a hard requirement — broken
   inheritance is the root of "why can this person see that folder" and the classic
   access-sprawl source. A subset needing tighter access is a separate library, not a maze
   of unique permissions. Two owners minimum.

3. Sharing defaults: set the site's external-sharing level deliberately — most to least
   restrictive is only people in the org, existing guests, new and existing guests, anyone
   with an anonymous link. Default to the most restrictive that meets the need; anonymous
   links are an approved exception carrying expiration, never a default. A site cannot be
   more open than the tenant-level setting — check that ceiling first.

4. Labels and retention: where the tenant uses sensitivity labels or retention policies,
   apply the container label at creation rather than retrofitting. The documented standard
   is in the client's documentation; continue without it (Connector Degradation base skill).

5. Approval gate. Send an approval request covering site type, name, owners, who gets access
   and the sharing level — especially with any external sharing. Capture the intended access
   list and sharing level before creation — the verification baseline and the rollback.

6. Prepare execution for the tech (verify against the current admin center and PnP
   PowerShell): site creation or New-SPOSite / New-PnPSite; sharing via Set-SPOSite
   -SharingCapability; SharePoint group assignment; container label.

7. Verify with evidence: the site resolves, the intended people have the intended level and
   nobody else, and a test share behaves at the set level. Leave a plain-text note (PSA Note
   Discipline base skill): site type and why, name, owners, permission model, sharing level,
   approver, date, and rollback (delete the site — recoverable from the site recycle bin for
   the tenant's window; revert the sharing level). Log time.

When in doubt about the sharing posture or authorization, do nothing and escalate.
```
