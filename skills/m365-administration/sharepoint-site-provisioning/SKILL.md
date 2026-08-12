---
name: SharePoint Site Provisioning
description: Stand up a new SharePoint site or document library the right way — site type, permission model, and sharing defaults decided deliberately instead of inherited by accident. Use when a client asks for "a new SharePoint site," "a place to store X," "a document library for the team," or a shared file area.
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
You are provisioning a new SharePoint site or library with permissions and sharing posture chosen deliberately. You prepare and verify; the technician executes in the admin center or PowerShell. Never invent data — verify the admin surface against current docs.

1. Decide the site TYPE from the purpose, and say the trade-off out loud:
   - Team site (M365 Group-backed) → collaboration with a group, membership, Teams/Planner attached. Creating one provisions a whole M365 Group — consistent with m365-group-lifecycle, so name/owners follow that policy.
   - Communication site → broadcast/intranet, few authors many readers, no group membership model.
   - A document library on an EXISTING site → when the ask is really "a folder area," not a new site; avoids site sprawl.
   Pick the lightest option that fits; a new site is not free — it is another thing to govern.

2. Permission model: use SharePoint groups (Owners/Members/Visitors) — never direct per-user grants on the site, and never break inheritance on individual folders unless there is a hard requirement. Broken inheritance is the root of "why can this person see that folder" tickets and the classic access-sprawl source. If a subset needs tighter access, model it as a separate library/site, not a maze of unique permissions. Two owners minimum.

3. Sharing defaults: set the site's external-sharing level deliberately — from most to least restrictive: only people in the org, existing guests, new and existing guests, anyone (anonymous links). Default to the most restrictive that meets the need; anonymous "Anyone" links are a deliberate, approved exception, never a default, and should carry link expiration. The site cannot be more open than the tenant-level sharing setting — check that ceiling first.

4. Sensitivity/retention: if the tenant uses sensitivity labels (sensitivity-labels) or retention policies, apply the right container label/policy at creation rather than retrofitting. Check the client's documented standard in the client's documentation if connected; degrade gracefully if not.

5. Approval gate: a new site with an external-sharing posture and a permission model is client-visible and governance-relevant. Confirm with the client (send an approval request): site type, name, owners, who gets access, and the sharing level — especially if any external sharing is requested. Capture the intended access list and sharing level before creation; that is the verification baseline and rollback reference.

6. Prepare execution for the tech (verify against current SharePoint admin center / PnP PowerShell): SharePoint admin center site creation, or New-SPOSite / New-PnPSite; set sharing with Set-SPOSite -SharingCapability; assign SharePoint groups; apply container label.

7. Verify with evidence: the site resolves; the intended people have the intended level and no one else; external sharing behaves at the set level (test a share). Leave a plain-text note: site type and WHY, name, owners, permission model, sharing level, any label/retention applied, approver, date, and rollback (delete site — recoverable from the site recycle bin/retention for the tenant's window; revert sharing level). Log time.

When in doubt about the sharing posture or authorization, do nothing and escalate.
```
