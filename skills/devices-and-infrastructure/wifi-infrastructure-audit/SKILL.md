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
Four lenses on a client's wireless: what APs exist and where, where users complain, how
stale the firmware is, and whether guest is really isolated from the corporate LAN.

1. AP inventory: documentation (IT Glue / Hudu) for the wireless records (controller/cloud
   platform, AP list, SSIDs, placement notes), plus Liongard's posture data for the live
   AP list where the platform has an inspector (Meraki, UniFi and most do) — apply the
   Inspector Read Discipline base skill: confirm the inspector exists and last ran
   successfully, read the AP data, state the dataprint age. Build a per-site table: name,
   model, location, last seen, firmware. Flag documented-but-unseen and undocumented APs.

2. Complaint mapping: read the client's WiFi tickets over ~6 months (search per signal:
   "wifi", "wireless", "disconnect", "slow internet"; apply the Sweep Honesty base skill —
   a capped search means "at least N"). Map each complaint's location against the AP
   inventory: a cluster with no nearby AP suggests a coverage hole; a cluster near an AP
   suggests a sick AP, channel congestion, or capacity — not coverage.

3. Firmware: from Liongard data or documentation, tabulate versions per AP model. Flag
   mixed versions within one site (roaming problems love mixed firmware) and versions far
   behind the vendor's current release — verify "current" against the vendor's release
   notes, not memory; read the change history for when firmware last changed.

4. Guest isolation, from evidence not probing: from documentation and controller config,
   verify the guest SSID maps to a separate VLAN/subnet, client isolation is on, and
   firewall rules block guest -> corporate traffic. With no config evidence the honest
   finding is "isolation unverified — recommend an on-site test (guest client attempting
   to reach a corporate IP)", never a pass.

5. Output: the AP table, a complaint heat summary (area -> count -> nearest AP ->
   hypothesis), firmware findings, the guest-isolation verdict (pass / fail / unverified),
   and ranked recommendations (add an AP at X, update Y, verify isolation on site). Offer
   a ticket per remediation and a summary note (apply the PSA Note Discipline base skill —
   plain text, no markdown or emojis).

Guardrails: complaint mapping is a hypothesis generator, not a site survey — recommend a
proper survey before any AP purchase, and never size a refresh from ticket text. This
skill cannot push firmware, and AP updates cause outages: firmware and controller changes
are change-window handoffs. An "unverified" guest-isolation result is never softened into
a pass — say what evidence is missing. Never include WiFi PSKs, RADIUS secrets, or
controller credentials in output, even when documentation has them. If neither
documentation nor Liongard covers the platform, report the audit as inventory-blind and
start with a documentation ticket.
```
