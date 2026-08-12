---
name: Liongard Cisco Network Read
description: Interrogate a client's Cisco switches/routers (IOS/IOS-XE) through Liongard — IOS versions across the fleet, running-config change detections, port/interface inventory, VLAN layout. Use for "what changed on the switch", IOS-currency sweeps, or port/VLAN facts during connectivity triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Cisco Network Read

**When to use:** "Did the switch config change before this VLAN broke?", an IOS-currency sweep before an upgrade project, "what VLAN is that port on?", a free-port count before a desk move, or a documented-vs-actual VLAN check. (Meraki gear is a different inspector.)

**Run it:** on one client — name the client and the switch/router question (one device or the whole fleet).

## Prompt

```
Read Cisco switch/router state (IOS/IOS-XE) for CLIENT_NAME from the Liongard inspector. Read-only — config changes go through change control.

1. Resolve the client's environment, then find the Cisco IOS switch/router inspectors and confirm each ran recently. Expect one inspector per device; a fleet question means iterating them all — say how many you covered, and flag devices whose inspector hasn't run recently as "stale — excluded/qualified" rather than mixing ages silently.
2. Read the values from each device's latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - IOS sweep: version string per device, grouped — the drift table (same model, different IOS = upgrade-planning input). Report versions verbatim; EOL/vulnerability mapping needs verification against Cisco notices, not memory.
   - VLANs: VLAN id/name list per switch; compare across switches for VLANs defined on one side of a trunk only.
   - Ports: interface list with description, access VLAN, status — free-port counts come from unconfigured/administratively-down interfaces, clearly labeled as an approximation (a port can be unconfigured and physically in use). Interface up/down state is a snapshot, not monitoring — never present it as current link state during an incident.
3. Config changes → check what changed per device: running-config change detections are the core value. Order against the incident window (time-adjacency, bounded by inspector cadence).
4. Never reproduce enable secrets, SNMP strings, or key material from config-derived data. Output: table (device / fact / as-of), change list where relevant, flags (IOS drift, EOL-looking versions labeled "verify against Cisco EOL notices", VLAN mismatches, stale inspectors). Offer to leave a plain-text note. Degradation: devices lacking inspectors → documentation → ticket history; partial fleet coverage must be stated ("6 of 9 documented switches have inspectors").
```
