---
name: Intune vs RMM Reconciliation
description: Reconcile an Intune-enrolled device list against RMM agent inventory — find machines missing an RMM agent, missing Intune, or double-managed conflicts.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, list_ninjaone_organizations, get_ninjaone_device, connectwise_rmm_search_devices, connectwise_rmm_list_companies, liongard_launchpoint, liongard_query, liongard_metric, search_itglue, search_hudu, add_ticket_note, create_ticket]
connectors: [NinjaOne, ConnectWise RMM, Liongard, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Intune vs RMM Reconciliation

**When to use:** "Do all of <client>'s Intune devices have the RMM agent?", a machine in Intune but invisible to monitoring (or vice versa), or before rolling out a policy that assumes one tool covers the whole fleet.

**Run it:** across a client's whole fleet, on demand (not a Flow — it's a reconciliation pass, not a per-ticket event).

## Prompt

```
Cross-check the Intune enrollment list against the RMM agent inventory for one client and produce three actionable buckets: missing RMM agent, missing Intune enrollment, and double-managed conflict candidates. Read-only.

1. Resolve the client organization in the RMM and pull its full device list (whichever RMM is connected — NinjaOne or ConnectWise RMM). If a listing may have capped, report the count as "at least N".
2. Get the Intune side. There is no direct Intune tool: read Intune device data from the environment's posture in Liongard when enabled — first verify the M365/Azure/Intune inspector exists and last ran successfully, then read the device list, stating the dataprint age. If the inspector is absent or its last run failed, ask the requester to export the Intune device list (Devices -> All devices -> Export) and paste/attach it. Never guess the Intune population.
3. Normalize before matching: lowercase hostnames, strip domain suffixes, match on serial number where both sides expose it — hostname alone misses renamed machines. Flag rows matched on hostname only as lower confidence.
4. Bucket results: (a) in Intune, not in RMM -> missing agent (agent-deployment candidate); (b) in RMM, not in Intune -> enrollment gap (MDM-enrollment candidate, or a server/appliance where Intune is not expected — separate those out); (c) in both -> check for double-management conflicts (both tools owning patching or pushing conflicting policies). Note which tool is intended source of truth per function if the documentation (IT Glue / Hudu) says.
5. Age-filter noise: a device last seen by either side >~30 days ago is likely retired, not a gap. List stale devices separately as "verify then retire".
6. Output a reconciliation table per bucket (device, last seen in each tool, match confidence, recommended action). Deploying agents or enrolling devices is not something this skill can do — hand off with the exact device list and, for RMM-side work, the device's RMM context. Offer to open a remediation ticket per bucket or leave a plain-text summary note (no markdown/emojis).

Guardrails: never claim the Intune list is complete unless it came from Liongard or a user-supplied export; say which source you used and its as-of time. Serial-number matches are authoritative; hostname-only matches are stated as probable, never certain. Do not recommend removing either management agent from a double-managed device without the client's documented management model — flag the conflict, do not resolve it unilaterally. Read-only — no agent installs, enrollments, or policy pushes (this integration cannot run scripts or deploy software). If neither Liongard nor an export is available, stop after the RMM inventory and say the Intune side could not be verified.
```
