---
name: WiFi Infrastructure Audit
description: Audit a wireless estate — AP inventory per site, coverage complaints from ticket history, firmware posture, and a guest-network isolation check per client.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, liongard_launchpoint, liongard_device, liongard_metric, liongard_timeline, search_tickets, search_ninjaone_devices, add_ticket_note, create_ticket]
connectors: [IT Glue, Hudu, Liongard, NinjaOne]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# WiFi Infrastructure Audit

**When to use:** "Audit <client>'s WiFi" / "why do they keep complaining about wireless?", recurring coverage/roaming complaints from one area, or a security review asking whether guest WiFi is segregated.

**Run it:** across a client's wireless estate, on demand (not a Flow — it's an audit pass, not a per-ticket event).

## Prompt

```
Four-lens review of a client's wireless network: what APs exist and where, where users actually complain, how stale the firmware is, and whether the guest network is genuinely isolated from the corporate LAN.

1. AP inventory: check the documentation (IT Glue / Hudu) for the wireless documentation (controller/cloud platform, AP list, SSIDs, placement notes), and read the environment's posture in Liongard for the live AP list where the wireless platform has an inspector (Meraki, UniFi, and most major platforms do) — filter by system type to confirm the inspector exists and last ran successfully, then read the AP data, stating the dataprint age. Build a per-site table: AP name, model, location note, last seen, firmware. Flag documented-but-unseen and seen-but-undocumented APs.
2. Coverage-complaint mapping: read the client's WiFi tickets over ~6 months (search per signal — "wifi", "wireless", "disconnect", "slow internet" — and note capped searches mean "at least N"). Extract the location in each complaint and map complaints against the AP inventory: clusters in one area with no nearby AP suggest a coverage hole; clusters near an AP suggest a sick AP, channel congestion, or capacity, not coverage.
3. Firmware posture: from the Liongard data or documentation, tabulate firmware versions per AP model. Flag mixed versions within one site (roaming problems love mixed firmware) and versions far behind the vendor's current release — verify "current" against the vendor's release notes rather than memory, and read the change history for when firmware last changed.
4. Guest isolation check (evidence-based, not intrusive): from documentation and controller config data, verify the guest SSID maps to a separate VLAN/subnet, client isolation is enabled, and firewall rules block guest->corporate traffic. If config evidence is unavailable, the honest finding is "isolation unverified — recommend an on-site test (guest client attempting to reach a corporate IP)", not a pass.
5. Output: per-site AP table, complaint heat summary (area -> complaint count -> nearest AP -> hypothesis), firmware findings, guest-isolation verdict (pass / fail / unverified), and a ranked recommendation list (add AP at X, replace/update Y, verify isolation on site). Offer to open a ticket per remediation and a plain-text summary note (no markdown/emojis).

Guardrails: complaint mapping is a hypothesis generator, not a site survey — recommend a proper wireless survey before any AP purchase; never size a refresh from ticket text alone. Firmware updates and controller changes are handoffs — this skill cannot push firmware, and AP updates cause outages, so they belong in a change window. An "unverified" guest-isolation result must never be softened into a pass — say what evidence is missing. Never include WiFi PSKs, RADIUS secrets, or controller credentials in output, even when documentation contains them. If neither documentation nor Liongard covers the wireless platform, report the audit as inventory-blind and start with a documentation ticket.
```
