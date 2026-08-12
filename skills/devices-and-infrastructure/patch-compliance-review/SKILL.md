---
name: Patch Compliance Review
description: Report patch status for a device or a client's whole fleet — missing, failed, and pending patches — using ConnectWise RMM patch reads or Liongard metrics when enabled, degrading to NinjaOne alerts and activities otherwise. Use for "are <client>'s machines patched" or a compliance evidence pull.
category: Devices & Infrastructure
tools: [connectwise_rmm_search_devices, connectwise_rmm_get_device, liongard_metric, search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, get_ninjaone_device_activities, add_ticket_note]
connectors: [ConnectWise RMM, Liongard, NinjaOne]
scope: both
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Patch Compliance Review

**When to use:** "Is <device> / <client>'s fleet up to date on patches?", compliance/cyber-insurance evidence, or "which machines are missing <update class>?" after a vulnerability announcement.

**Run it:** on one device · or across a client's whole fleet, on demand (not a Flow — it's a reporting/evidence pull, not a per-ticket event).

## Prompt

```
Per-device or per-fleet patch posture — what is missing, what failed, what is pending a reboot — sourced from the best patch integration the tenant actually has, with the data source named in the output.

1. Determine scope (one device or a fleet) and resolve the organization/device first — rank candidates by organization match then last-contact; don't pause mid-lookup to ask when ranking resolves it. Don't trust a class filter.
2. Pick the data source, best first, and NAME it in the output:
   - ConnectWise RMM enabled -> its per-device patch reads give patch status directly.
   - Liongard enabled -> its patch/OS-currency metrics give environment-level compliance numbers (state dataprint age).
   - Otherwise degrade to NinjaOne: read the device details for OS build and pending-reboot state, its alerts for patch-failure alerts, and its recent activity for patch install/failure events. Say explicitly that this is an inferred view, not a patch-management report.
3. For fleet scope, iterate the device list; if any listing hits a result cap, report the compliance figure over "at least N devices reviewed" and never as a percentage of an unknown total.
4. Classify each device: current / pending reboot to complete / failed patches / stale (no successful patch activity in 30+ days) / unknown (offline too long to assess). Offline devices are "unknown", not "compliant".
5. Roll up: counts per class, worst offenders (servers first), and repeated-failure devices needing hands-on attention.
6. Output the review with the data source and its limits stated, the per-class breakdown, and recommended next actions (reboot to complete, investigate repeat failures, verify decommissions). Offer to leave a plain-text summary note (no markdown/emojis).

Guardrails: never present the degraded RMM-inferred view as authoritative compliance data — compliance answers require a patch-management source, and the output must say which source produced it. No patch deployment from here: pushing patches, running scripts, and policy changes are not available through this integration — remediation is guidance plus a deep link for the tech. Result-cap honesty: truncated fleets produce floor counts, not percentages. Devices offline beyond the assessment window are "unknown" — counting them compliant fabricates evidence. If none of the patch-capable integrations are enabled, say so and stop rather than guessing.
```
