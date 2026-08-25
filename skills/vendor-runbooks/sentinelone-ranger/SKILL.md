---
name: SentinelOne Ranger
description: Work SentinelOne Ranger network-discovery findings: read the rogue or unmanaged-device signal and drive to identify-then-manage without blind action.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# SentinelOne Ranger

**When to use:** A Ranger finding reports a new/unmanaged/rogue device on a client's network; a coverage-gap question arises ("which endpoints have no S1 agent?"); or a tech asks how to read a Ranger discovery or whether a discovered device is a threat.

**Run it:** on the finding ticket.

## Prompt

```
Triage a SentinelOne Ranger finding — Ranger is the network-discovery layer, using already
deployed S1 agents to passively map the network and surface devices with no agent on them.
sentinelone-threat-verdict owns S1 detection reading, mitigation and exclusion discipline —
use it for an actual threat verdict. Identify before acting: a "rogue device" is usually a
known printer, IoT sensor, switch or an EDR coverage gap on a real workstation. You have no S1, Ranger or
network-device console — agent installs, network blocks and switch/DHCP investigation are
technician actions you direct and record. Never invent discovery detail.

1. Parse the finding: the discovered device's IP and MAC, hostname if resolved, OS
   fingerprint guess, the network or subnet and the S1 agent that observed it, first-seen
   time, and whether Ranger calls it managed, unmanaged or unknown. Copy Ranger's exact
   wording. Route to the client per security-alert-response on the observing site or tenant;
   low confidence means flag for a human, not reassign.

2. Cross-reference the RMM inventory by hostname, MAC or IP, and the client's documentation,
   to answer: is this a known asset that simply lacks an
   S1 agent, a known non-endpoint device that cannot run S1, or genuinely unrecognized? The
   MAC OUI (vendor prefix) is a strong first clue to device type.

3. Put the finding in the right lane — a coverage gap is not an unknown device:
   - Known asset, no S1 agent → an EDR coverage gap: a deployment task for the technician,
     not an incident. Note it for coverage remediation.
   - Known non-endpoint device (printer, switch, IoT, phone) → expected. Record it and, if it
     recurs, suppress it with scoped tuning so it stops surfacing as rogue — scoped
     suppression only, never disabling discovery.
   - Genuinely unidentified device on a trusted segment → a security question per
     security-alert-response: who plugged in what, when. Correlate with access-control, DHCP
     or switch logs the technician gathers before concluding.

4. Take no blind network action. Ranger can be configured to block or quarantine unknown
   devices at the network layer, and blocking one that turns out to be a critical printer or
   a medical or OT device causes its own outage. Identify first; any network-level
   containment is a deliberate, documented, technician-executed decision.

5. Hand off: a deep link into the device in the RMM where you matched a managed device, and
   a written handoff for the rest.

6. Note the identification result, the lane, any coverage-gap items, and any containment
   decision with its owner. Client-facing wording per defensive-writing-standard.

Without RMM lookup or documentation, identification is limited to IP, MAC and OUI — say so
and lean on technician-gathered evidence. When in doubt do nothing irreversible and
escalate.
```
