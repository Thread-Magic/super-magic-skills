---
name: Server Decommission Runbook
description: Safely retire a server — map dependencies, migrate data, clean up DNS, monitoring, backup, wipe, and update docs, with an approval gate before destruction.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, liongard_launchpoint, liongard_metric, liongard_timeline, search_itglue, search_knowledge_base, create_ticket, add_ticket_note, send_approval]
connectors: [NinjaOne, Liongard, IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Server Decommission Runbook

**When to use:** "Decommission <server> — it's being replaced", retiring a physical host / VM / legacy app server, or confirming a server is genuinely safe to power off.

**Run it:** on one server, on demand (not a Flow — the destructive phase routes through human approval).

## Prompt

```
Retire a server without breaking the services that quietly depend on it. Dependency-first, approval-gated: prove nothing still relies on the box before it is wiped, then clean up every record it touched. This skill plans, verifies, and documents only — the wipe/power-off/deletion are human actions behind approval.

1. Identify the server and its role: look it up in the RMM and read its details for OS, role hints, last contact, installed agents (don't trust a class filter). Pull the asset and its documented purpose from the documentation (IT Glue) and any decommission checklist from the knowledge base.
2. Map dependencies before proposing anything destructive. Check for: roles the box holds (DC/DNS/DHCP/CA/file/print/SQL/app), services other systems consume, scheduled tasks, shares and mapped drives, DNS records pointing at it, backup jobs, monitoring. Where the partner runs Liongard, read the environment's posture via the relevant inspectors (AD, DNS, DHCP, hypervisor, backup) to read current config and confirm what references this host. Verify each inspector last ran successfully and state dataprint age; where no inspector exists, fall back to documentation + RMM and say the dependency check is partial.
3. Check recent device activity for live sessions or users still hitting the box — active use is a stop condition until confirmed.
4. Produce a pre-decommission plan listing, per dependency: what must be migrated, repointed, or confirmed dead first (data migration, DNS/record changes, backup-job removal, monitoring removal, license reclamation). Nothing is marked done that you cannot verify.
5. Gate the destructive phase behind explicit sign-off: route the plan for approval so a human authorizes the wipe/power-off. Do not represent the shutdown or wipe as something this skill performs.
6. On approval, hand off execution: the actual power-off, disk wipe, and hypervisor/RMM removal are performed by the tech in-console (there is no script-exec or delete path through this skill). Track the record changes (DNS, backup, monitoring, licensing) as they are completed.
7. Close out documentation: mark the asset retired with date and reason, remove it from active inventory. Leave the runbook status as a plain-text note (no markdown/emojis), or open a ticket if none exists.

Guardrails: dependency mapping is mandatory before any destructive step — never propose a wipe/power-off until dependencies are accounted for and data is confirmed migrated. The wipe, power-off, and deletion are human actions behind approval; do not claim to have deleted or wiped anything. Trust Liongard/RMM data only after confirming the inspector/agent last ran; always state dataprint/last-contact age; degrade to docs when a source is absent and say the check is partial. Never remove backup jobs or retention until the retention policy for the retired system is confirmed — the data may be needed after the box is gone.
```
