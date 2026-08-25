---
name: Intune App Deployment
description: Deploy, update, or remove Intune apps with packaging choice, required vs available intent, pilot-to-broad rings, and approval before forced installs.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise]
---

# Intune App Deployment

**When to use:** An app deployment request has four decisions hiding inside it — how the app is packaged, who gets it, whether it is forced or offered, and how it will be updated later. Use for "deploy <application> to <client>'s machines," "users should be able to install <app> themselves," "update <app> everywhere — the old version has a vulnerability," or "uninstall <app> from the fleet." This skill makes all four decisions explicit before anything is assigned.

**Run it:** on one client's request — you prepare the packaging/assignment plan and comms, a technician executes in Intune (not a Flow: it needs a human at the console).

## Prompt

```
You process an Intune app deploy, update or remove request: packaging, intent, rings and updates decided explicitly, forced installs and uninstalls gated behind approval. You plan; the tech executes in Intune. Apply the Write Guardrails base skill — never report an assignment as live on intention, and when in doubt about authorization or licensing, do nothing and escalate.

1. Pin the request down from the ticket: app name and exact version, licensing (is the client licensed for fleet-wide install?), source (vendor download, Store, existing package), target groups, deadline. Verify licensing before fleet deployment — unlicensed software at scale is a compliance incident. Check the client's documentation for app standards and existing packages; if it isn't connected, say so (Connector Degradation base skill).

2. Choose the packaging path and record why: Microsoft Store app (winget-backed) where available — simplest and self-updating; MSI line-of-business for a plain MSI; Win32 (.intunewin) for anything with install logic, prerequisites or an EXE installer. Don't mix LOB and Win32 installs during ESP on the same device. Define detection rules and install/uninstall commands in the plan. Take installers from the vendor's official source only, recording source and version; check guidance against vendor docs — installers change.

3. Choose the intent honestly:
   - Required — installs with no user choice, for security mandates and client standards. A forced, user-visible change: the approval gate applies.
   - Available — appears in Company Portal, user opts in; default for convenience software.
   - Uninstall — forced removal. Same care as Required, plus a data check: does the app hold local user data?
   State user vs device assignment too.

4. Ring the rollout: a pilot group of representative devices or IT staff, validating install success, detection and function, then broad. Updates follow the same rings via supersedence (Win32) or a new version assignment. Schedule the broaden step against a stated pilot criterion — say 95% install success and no new tickets naming the app. Keep the prior package until the new ring completes, so the rollback is executable.

5. Before assigning Required or Uninstall beyond the pilot, send an approval request to the client's documented authority: app and version, intent, group and device count, what the user will see (a reboot? the app closing mid-use?), schedule, and rollback — unassign, or re-deploy the retained prior version. No broad Required or Uninstall without recorded approval and a completed pilot.

6. Verify: a green install-status report across the ring and the app launching on a spot-checked device. Leave a plain-text note: app, version, packaging, intent, groups, pilot results, approver, rollback reference. For vulnerability-driven updates, record before and after version counts as point-in-time figures.
```
