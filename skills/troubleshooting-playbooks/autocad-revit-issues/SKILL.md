---
name: AutoCAD / Revit Issues
description: Troubleshoot Autodesk AutoCAD and Revit — FlexNet network license checkout failures, drawing corruption, and BIM central-model worksharing sync.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# AutoCAD / Revit Issues

**When to use:** "No license available" / AutoCAD or Revit won't check out a network license or licensing dropped for a site; a .dwg or .rvt won't open, crashes on open, or shows corruption; Revit "Synchronize with Central" fails, hangs, or throws conflicts; or very large drawings/models are slow or worksharing/central-file access broke.

**Run it:** on the one ticket you're working — a tech drives this hands-on with the user and the BIM manager, not unattended.

## Prompt

```
Autodesk tickets cluster in three areas: network license checkout, file corruption, Revit
worksharing. Treat the central model as sacred — a wrong move there loses a team's day.

Climb the Troubleshooting Ladder base skill first, pinning two facts. Product and year
version: Revit central files are version-specific and forward-only, so opening one in a
newer year upgrades it irreversibly and locks out the team. Licensing model: named-user
sign-in, or network licensing through Autodesk's Network License Manager. Documentation
gives where the license server and central models live (local or BIM 360/ACC); a Liongard
Windows inspector corroborates license-server state — note its dataprint age.

Get the error first: the Network License Manager status and debug log for licensing, the
open error and AutoCAD's Audit result for files, and for Revit the sync error text and
whether it is a lock rather than corruption.

1. Network license checkout failure — check the license service and adskflex daemon are
   running, the license file hasn't expired, the seats aren't all genuinely in use (a
   crashed client can hold a stale checkout, reclaimable in the manager), and clients can
   reach the server (port, firewall, the right server name in their config). Restarting
   the license service drops every active seat, so coordinate it with the site. Escalate
   an expired or wrong license file: that is an Autodesk account action.

2. Damaged .dwg — run AutoCAD's AUDIT and RECOVER, and RECOVERALL for xrefs, on a copy. If
   those fail, restore from the .bak or the file server's backup (pair with
   backup-restore-request). Never hand-edit a drawing file.

3. Damaged .rvt — open with Audit checked, on a copy; for a broken local file, Create New
   Local from central. Central-model corruption is serious: work from a backup or
   Autodesk's eTransmit and detach-to-recreate-central path, with the BIM manager involved
   before any recreate-central.

4. Synchronize with Central fails or hangs — usually network or storage under the central
   path, a lock held by another user or a stale local file, or too many pending changes.
   Confirm the path is reachable and nobody holds an editing lock; a sync interrupted
   mid-write is why central-model backups exist. Escalate a service-side failure on BIM
   360 or ACC as Autodesk's platform.

Always work on copies, and never delete or recreate a central model without the BIM
manager's sign-off and a verified backup. License files and serials are entitlement data:
keep them out of PSA notes and route license changes through the Autodesk account owner.

Success: a client checks out a license and opens the app, the recovered file audits clean,
or a test Synchronize with Central completes. Note it (apply the PSA Note Discipline base
skill): product and year, licensing model, evidence, branch, action, verification,
dataprint age.
```
