---
name: Storage Capacity Planning
description: Turn repeated disk-space alerts into a trend-based capacity forecast per server or NAS — growth rate, projected full date, and expansion options to price.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, search_tickets, search_itglue, search_hudu, add_ticket_note, create_ticket]
connectors: [NinjaOne, IT Glue, Hudu]
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Storage Capacity Planning

**When to use:** The same server/NAS has alerted on disk more than once, "how long until <server>'s data drive is full?", or the account team wants an expansion recommendation.

**Run it:** on one server/NAS volume, on demand (not a Flow — it's a trend forecast and options brief, not a per-ticket event).

## Prompt

```
Stop treating the same disk alert as a new incident: reconstruct the growth trend, project
when the volume fills, and produce an options brief — clean up, expand, re-architect.
Needs the RMM for current state.

1. Current state: the device details for capacity and free space per volume; documentation
   (IT Glue / Hudu) for what the volume holds (file shares, databases, backup targets) —
   the workload drives growth character and expansion options. Resolve org -> device
   without stopping to ask; a class filter is not evidence.

2. Reconstruct the trend — the RMM exposes point-in-time readings only. Harvest dated
   points from the device's alerts and activity (each threshold alert is a dated reading)
   and from earlier disk tickets recording free-space figures. Three or more make a usable
   trend; fewer and the honest output is "insufficient history — start recording,
   re-forecast in N weeks", plus the current-state brief.

3. Compute growth honestly: rate per month from the points you have, a projected-full date
   at that rate, a sensitivity line ("at 1.5x the rate, full by <earlier date>"). Deduct
   known one-off events (a migration, a cleanup) rather than letting them distort the
   trend — say when you did. State the forecast as a range, never a date certain.

4. Separate reclaimable from organic growth: old user profiles, stale snapshots, log bloat
   and duplicate backup copies are reclaimable (quick wins go to disk-space-remediation);
   steady LOB data growth is organic, and cleanup only rents time against it. Quantify the
   runway cleanup buys against the growth rate.

5. Expansion options, matched to the platform from documentation: extend the volume or
   datastore (if the underlying storage has headroom), add disks or a shelf (check slots
   and warranty/EOL — expanding a dying unit is money misspent; see
   hardware-refresh-forecast), tier or archive cold data, or move the workload (larger
   NAS, SAN, cloud). For each: effort class, disruption (window needed?), and runway
   bought at the observed rate.

6. Output current state, the trend with its data points, the projected-full range, the
   reclaimable-vs-organic split and the options, as a note (apply the PSA Note Discipline
   base skill — plain text, no markdown or emojis). Open a ticket for the account team
   when the projected-full date is inside the client's procurement lead time.

Guardrails: a forecast from fewer than three dated readings is labelled low-confidence or
not issued — two points are not a trend. Cleanup recommendations name what the files are
believed to be and require verification before deletion; this skill deletes nothing. No
hardware model or price quotes from memory — sizing and pricing is the account team's.
Never forecast a backup-target volume as organic growth — retention settings drive it, not
users; say when growth is policy-driven.
```
