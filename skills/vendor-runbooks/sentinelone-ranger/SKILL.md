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
You are triaging a SentinelOne Ranger finding — the network-discovery / device-inventory capability, as distinct from endpoint threat detection. Ranger uses already-deployed S1 agents to passively map the network and surface devices that have no S1 agent — rogue or unmanaged assets. The parent skill sentinelone-threat-verdict owns S1 detection-engine reading, mitigation, and exclusion discipline; read it first and do not duplicate its threat-verdict steps — for an actual endpoint threat verdict, use that skill; this one is the network-discovery layer. The triage discipline is identification before action: a "rogue device" is usually a known printer, IoT sensor, switch, or an EDR-coverage gap on a real workstation — not an intruder. Verify Ranger feature names against SentinelOne's current documentation. You have no S1/Ranger or network-device console access — agent installs, network-block decisions, and switch/DHCP investigation are technician actions you direct and record, never assume completion. Never invent discovery detail.

1. Parse the Ranger finding: discovered device's IP/MAC, hostname if resolved, OS/fingerprint guess, the network/subnet and the S1 agent that observed it, first-seen time, and whether Ranger classifies it managed/unmanaged/unknown. Copy Ranger's exact wording. Route to the client per security-alert-response using the observing site/tenant; low confidence → flag for a human.

2. Identify before alarming — most "rogue" devices are mundane. Cross-reference the RMM inventory (look up the device in the RMM by hostname/MAC/IP; read its details for a match) and documentation to answer: is this a known asset that simply lacks an S1 agent (coverage gap), a known non-endpoint device that can't run S1 (printer, switch, IoT, phone), or a genuinely unrecognized device? The MAC OUI (vendor prefix) is a strong first clue to device type.

3. Classify the finding into the right lane — don't collapse a coverage gap and an unknown device into one:
   - Known asset, no S1 agent → EDR coverage gap: an install/deployment task (technician action), not an incident. Note it for coverage remediation.
   - Known non-endpoint device → expected; record and, if recurring, suppress via scoped tuning so it stops surfacing as "rogue" — scoped suppression, never blanket disabling of discovery.
   - Genuinely unidentified device on a trusted segment → treat as a security question per security-alert-response: who plugged in what, when; correlate with any access-control/DHCP/switch logs (technician-gathered) before concluding.

4. Do not take blind network action: Ranger can, with configuration, help block/quarantine unknown devices at the network layer — but blocking an unidentified device that turns out to be a critical printer or medical/OT device causes its own outage. Identify first; any network-level containment is a deliberate, documented, technician-executed decision.

5. Hand off: agent installs, network-block decisions, and switch/DHCP investigation are technician actions — hand the tech a deep link into the device in the RMM for a matched managed device, and a clear handoff for the rest. Direct and record.

6. In the internal note, document the identification result, the lane, coverage-gap items, and any containment decision with its owner. Client-facing wording per defensive-writing-standard.

Degradation: without RMM lookup or documentation, identification is limited to IP/MAC/OUI — say so and lean on technician-gathered network evidence. When in doubt, do nothing irreversible and escalate.
```
