---
name: Network Outage Triage
description: Triage a suspected site-down — all-devices-offline vs single dead device, ISP vs internal, who to call, and set a comms cadence for the client updates.
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
Read the offline pattern across a client's fleet: site-down vs single-device, ISP vs
internal, then the right calls and a comms rhythm. With no RMM, triage from ticket volume
plus documentation and say the live fleet view is missing.

1. Establish the pattern: pull the client's devices and current alerts from the RMM. All
   or most devices at a site dropping within minutes = site event. A subset sharing a
   closet, switch or VLAN (inferred from naming and IP ranges) = internal segment. One
   device = not an outage; route back to Device Offline Runbook. Apply the Sweep Honesty
   base skill and flag result caps: an undercounted fleet makes a full outage look
   partial.

2. Drop time, from last-contact timestamps: a tight cluster is a hard cut (power, circuit,
   core switch); a stagger means something degrading (DHCP exhaustion, spanning-tree,
   failing hardware).

3. ISP vs internal, from outside evidence: edge device (firewall/router) unreachable while
   devices with independent connectivity (LTE, another site) are fine -> the cut is at or
   upstream of the edge. Edge answers but everything behind it is dark -> internal
   (switch, closet power, DHCP).

4. Pull the who-to-call sheet from documentation (IT Glue): ISP, account/circuit numbers,
   support line; the on-site contact; the network gear inventory. Missing any of these is
   a finding, not a footnote.

5. Scope beyond this client: are other clients on the same ISP or region dropping too
   (scan alerts across organizations)? A regional ISP event changes the message and the
   fix.

6. Consolidate ticket noise: designate a master incident ticket among the tickets this
   event spawned, and offer to merge the duplicates into it on the requester's
   confirmation.

7. Set the comms cadence and write the first update: who has been called (ISP with circuit
   ID, on-site contact heading to the closet), what is confirmed vs suspected, next update
   time. Rhythm: first client update immediately, then every 30 min for a full outage
   (hourly for partial) until restored, plus a closing summary. Updates go out as notes
   (apply the PSA Note Discipline base skill — plain text, no markdown or emojis).

8. On restoration: verify devices re-report online (spot-check last-contact), note the
   outage window and whether the cause is confirmed, and recommend a follow-up if not.

Guardrails: never declare ISP fault to the client without ISP confirmation or
edge-unreachable evidence — "we are investigating with the carrier" until then, and no
speculation in client-visible updates. Merge only on confirmation, and only tickets
verifiably from this event (same client, same window, offline-type) — never on title
similarity. The RMM sees the site from outside: every internal-topology conclusion is
inference until on-site confirms. Never reset offline alerts during the event; they are
the telemetry.
```
