---
name: Network Device Inventory
description: Refresh a client network device inventory — switches, APs, firewalls, routers per site — by combining documentation with what monitoring actually sees.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, liongard_environment, liongard_device, liongard_launchpoint, liongard_metric, liongard_timeline, search_ninjaone_devices, get_ninjaone_device, add_ticket_note, create_ticket]
connectors: [IT Glue, Hudu, Liongard, NinjaOne]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Network Device Inventory

**When to use:** "What network devices does <client> have at <site>?", preparing a network project needing ground truth, or after an audit finds documentation is stale.

**Run it:** across a client's sites, on demand for an inventory refresh or audit (not a Flow — it's a discovery sweep, not a per-ticket event).

## Prompt

```
Assemble the per-site picture of a client's network infrastructure — every switch, AP, firewall, router — by merging documented inventory with monitoring's live view, and flag where the two disagree.

1. Pull the documented inventory: search the documentation (IT Glue / Hudu) for the client's network device configurations, per site. Capture device name, role (switch/AP/firewall/router), make/model, site/location, and management IP where documented — but never credentials, even if the doc contains them.
2. Pull the observed inventory: read the environment's posture in Liongard, which reaches most network platforms (Meraki, UniFi, firewall/switch inspectors) — filter by system type to find which inspectors exist and confirm each last ran successfully, then read the device data and the firmware/change history, stating dataprint age per source; also check the RMM for anything with an SNMP/agent presence. Note last-seen times; skip inspectors whose last run failed and list them as blind spots.
3. Merge per site into one table: device, role, make/model, documented?, monitored?, last seen, firmware where available. Match on management IP first, then name; flag low-confidence matches.
4. Flag the drift in three buckets: documented-but-not-monitored (monitoring blind spot or retired gear), monitored-but-not-documented (documentation gap — the more dangerous one), and conflicts (docs say one model/IP, monitoring says another).
5. Enrich with lifecycle signals where data allows: firmware age, devices past end-of-support (verify EOL dates against the vendor's published lifecycle pages rather than memory), single points of failure evident from the inventory (one switch for a whole site, no redundant firewall).
6. Output the per-site inventory table plus a drift/risk list with recommended actions (document X, add monitoring for Y, verify Z on site). Offer to open a documentation-update ticket — updating the documentation platform itself is a handoff — and leave a plain-text summary note (no markdown/emojis).

Guardrails: never copy credentials, SNMP community strings, or pre-shared keys into output, even when documentation exposes them — reference the doc by name/location. The merged inventory is only as fresh as its sources — always state last-seen/last-updated times and never present the table as verified-complete without a site walk. Do not invent make/model/firmware to fill gaps; leave cells empty and list them as unknowns. If neither documentation nor Liongard/RMM data is available, say so — an inventory cannot be fabricated from ticket mentions alone.
```
