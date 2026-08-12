---
name: RMM Cross-Tool Reconciliation
description: Reconcile device lists across RMM, EDR, backup, and documentation — find missing agents, single-tool orphans, and count mismatches that distort billing.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, connectwise_rmm_search_devices, liongard_device, liongard_metric, search_immybot_computers, search_itglue, search_hudu, add_ticket_note]
connectors: [NinjaOne, ConnectWise RMM, Liongard, ImmyBot, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# RMM Cross-Tool Reconciliation

**When to use:** "How many devices does <client> actually have? The tools disagree.", an agent-coverage audit ("is every RMM device also covered by EDR/backup?"), or a pre-billing-run true-up.

**Run it:** across a client's device inventories in every connected tool, on demand (not a Flow — it's a reconciliation pass, not a per-ticket event).

## Prompt

```
Cross-reference every device inventory the tenant has connected and produce the three lists that matter: devices missing an agent somewhere, orphans that exist in only one tool, and the count deltas per tool — because per-device billing rides on these numbers. This skill changes nothing.

1. Enumerate which inventory sources this tenant actually has enabled, and say which ones the reconciliation will cover: NinjaOne, ConnectWise RMM, Liongard device inventories (its inspectors often carry EDR, backup, and AD/M365 device views that stand in for tools without direct integrations — read the environment's posture for the details), ImmyBot, and documented asset lists in IT Glue / Hudu.
2. Pull the client's device list from each source. Flag any list that may have capped — a truncated list makes every downstream delta wrong, so reconcile per-segment (servers, then workstations, per location) if needed for full coverage.
3. Normalize before matching: hostnames casefolded, domain suffixes stripped, obvious duplicates within a single tool collapsed (same serial, same hostname re-enrolled). Match across tools on hostname first, serial number where available as the tiebreaker.
4. Build the three outputs:
   - Coverage gaps: devices in the RMM but absent from EDR/backup/docs views — unprotected or undocumented machines.
   - Orphans: devices in exactly one tool — stale records (retired, never removed) or rogue installs. Use last-contact/last-seen to split "stale, propose cleanup" from "active but unenrolled elsewhere, propose enrollment".
   - Count matrix: per-tool totals side by side, with deltas and the named devices behind each delta. Call out the billing angle explicitly: which count each tool would bill on, and which direction the MSP is likely over- or under-billing.
5. Sanity checks: devices offline 30+ days in every tool are probably retired — bucket as decommission candidates, not gaps. Devices matched on hostname but with different serials are re-used names, not the same machine.
6. Output the reconciliation with per-source caveats (cap hits, integration absences), the three lists, and recommended actions (enroll, remove stale record, verify with client, adjust billing count). Offer a plain-text summary note (no markdown/emojis).

Guardrails: never present a delta as billing truth without the caveats attached — a capped or stale source invalidates the comparison, and billing disputes are exactly where this report gets used. This skill changes nothing: no removals, no enrollments, no approval actions — cleanup is ticketed work. Hostname matching is heuristic — surface low-confidence matches separately. Name every integration that is NOT enabled so the reader knows which columns are missing, and never infer a tool's inventory from another tool's data.
```
