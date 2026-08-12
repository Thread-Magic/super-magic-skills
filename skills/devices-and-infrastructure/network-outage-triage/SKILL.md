---
name: Network Outage Triage
description: Triage a suspected site-down — distinguish the all-devices-offline pattern from a single dead device, split ISP from internal causes, identify who to call, and set a comms cadence. Use when multiple offline alerts fire from one client or someone reports "the whole office is down".
category: Devices & Infrastructure
tools: [search_ninjaone_devices, list_ninjaone_alerts, get_ninjaone_device, search_itglue, search_tickets, search_contacts, merge_ticket, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Network Outage Triage

**When to use:** A burst of offline alerts from one client hits the board, "<client> says the whole office is down", or a single offline ticket smells bigger.

**Run it:** on one outage/incident (consolidating its related tickets), on demand (not a Flow — merges and comms cadence need requester confirmation).

## Prompt

```
Read the offline pattern across a client's fleet to call site-down vs single-device, point at ISP vs internal, and set up the right phone calls and a communication rhythm. This needs the RMM connected; if absent, triage from ticket volume + documentation and say the live fleet view is missing.

1. Establish the pattern first: pull the client's devices and current alerts from the RMM. All/most devices at a site dropping within minutes = site event. A subset sharing a closet/switch/VLAN (infer from naming and IP ranges) = internal segment. One device = not an outage; route back to Device Offline Runbook. Flag result caps — an undercounted fleet can make a full outage look partial.
2. Note the drop time from last-contact timestamps — a tight cluster is a hard cut (power, circuit, core switch); a stagger suggests something degrading (DHCP exhaustion, spanning-tree, failing hardware).
3. ISP vs internal, from outside evidence: if the firewall/router/edge device is unreachable but devices with independent connectivity (LTE, other site) are fine, the cut is at or upstream of the edge. If the edge answers but everything behind it is dark, it is internal (switch, closet power, DHCP). Say which evidence supports the call — from the RMM's outside view this is inference; on-site confirmation beats it.
4. Pull the who-to-call sheet from documentation (IT Glue): ISP name, account/circuit numbers, support line; on-site contact; the site's network gear inventory. If docs are missing these, say so — that is a finding, not a footnote.
5. Check scope beyond this client: are other clients on the same ISP/region also dropping (scan alerts across organizations)? A regional ISP event changes the message and the fix.
6. Consolidate ticket noise: identify the offline-alert tickets this event spawned, designate one master incident ticket, and offer to merge the duplicates into it — with the requester's confirmation.
7. Set the comms cadence and write the first update: who has been called (ISP with circuit ID / on-site contact walking to the closet), what is confirmed vs suspected, next update time. Recommended rhythm: first client update immediately, then every 30 minutes for a full outage (hourly for partial) until restored, plus a closing summary. Leave updates as plain-text notes (no markdown/emojis).
8. On restoration: verify devices actually re-report online (spot-check last-contact), note the outage window and cause as confirmed/unconfirmed, and recommend a follow-up if cause is unknown — unexplained outages repeat.

Guardrails: never declare ISP fault to the client without ISP confirmation or edge-unreachable evidence — "we are investigating with the carrier" until confirmed; no speculation in client-visible updates. Merges only with confirmation, and only tickets verifiably from this event (same client, same window, offline-type) — never merge on title similarity. The RMM sees the site from outside; every internal-topology conclusion is labeled as inference until on-site confirms. Do not reset offline alerts during the event — they are the telemetry.
```
