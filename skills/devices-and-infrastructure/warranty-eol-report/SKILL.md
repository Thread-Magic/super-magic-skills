---
name: Warranty and EOL Report
description: Build an aging-fleet report for a client — end-of-life operating systems, old hardware, and warranty status where a source exposes it, for lifecycle risk.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, liongard_device, liongard_metric, search_itglue, add_ticket_note]
connectors: [NinjaOne, Liongard, IT Glue]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Warranty and EOL Report

**When to use:** "What's end-of-life or out of warranty at <client>?", QBR/budget-season lifecycle prep, or "who's exposed?" after an OS vendor announces an end-of-support date.

**Run it:** across a client's whole fleet, on demand for lifecycle-risk reporting (not a Flow — it's a reporting pass, not a per-ticket event).

## Prompt

```
Surface the lifecycle risk hiding in a client's fleet: OS versions past or approaching end of support, hardware old enough to be a reliability risk, and warranty expirations where any connected source actually records them. This needs the RMM connected; if absent, say the report needs an RMM inventory source and stop. Read-only.

1. Resolve the client organization and pull the fleet from the RMM; verify device classes in the details rather than trusting a class filter. Flag result caps and page to full coverage or report floors.
2. OS end-of-life pass: from each device's OS name/build, bucket into past end of support / within 12 months of end of support / current. Use the OS build actually reported — do not assume a device was upgraded. When unsure of a specific edition's date, mark it "verify support date" instead of guessing.
3. Hardware age pass: estimate age from the strongest signal in order: documented purchase date (IT Glue asset records), CPU generation from the model string, OS install/first-seen date as a weak floor. Label which signal produced each estimate. Bucket: 5+ years (refresh due), 4-5 years (plan), under 4 (fine).
4. Warranty pass: warranty data is only as good as its source — check IT Glue asset records and the device inventories in the environment's posture in Liongard where enabled. Report warranty status ONLY for devices where a source states it; everything else is "warranty unknown — serial available for manufacturer lookup", with the serial listed so a human can check.
5. Compose the report: summary counts per risk bucket, then the risk table (device, OS status, estimated age + signal used, warranty status/unknown), servers listed first. Close with recommendations: replace-now list, budget-next-cycle list, and a pointer to the Hardware Refresh Forecast skill for the spend model.
6. Offer a plain-text note (no markdown/emojis), and note that a client-facing version should go through the Client-Facing Device Report skill instead of this internal one.

Guardrails: never fabricate warranty status or support dates — "unknown" with a lookup path beats a confident guess that ends up in a client budget meeting. Every hardware-age figure carries its evidence signal; ages inferred from first-seen dates are floors, not facts. Offline/stale devices get flagged as possibly retired rather than inflating the risk counts. Read-only — the output is a report, not a change plan. Result-cap honesty on every fleet listing.
```
