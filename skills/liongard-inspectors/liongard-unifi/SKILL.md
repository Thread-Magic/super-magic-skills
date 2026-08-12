---
name: Liongard UniFi Read
description: Interrogate a client's Ubiquiti UniFi controller through the Liongard inspector — device inventory, adoption state, firmware drift, WLAN/network config. Use for "what UniFi gear do they have", wifi triage context, or firmware-currency checks.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard UniFi Read

**When to use:** "What UniFi devices does <client> have?" for triage or a refresh quote, a wifi ticket (which APs, what WLANs, what auth), "are their UniFi devices on current firmware?", "is anything disconnected/not adopted?", or change correlation after a controller upgrade.

**Run it:** on one client — name the client and the UniFi question.

## Prompt

```
Read UniFi controller state for CLIENT_NAME from the Liongard Ubiquiti UniFi inspector. Read-only — adoption, upgrades, and WLAN changes are tech-owned.

1. Resolve the client's environment, then find the UniFi inspector and confirm it ran recently — carry "as of <timestamp>." Multi-site controllers: identify which site maps to this client before answering.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Inventory: devices grouped by type/model with name, IP, firmware — the "what's there" table.
   - Firmware drift: group devices by model, compare firmware within each model — same-model boxes on different firmware is the drift finding.
   - Connection state: devices where state != connected/adopted — offline or orphaned gear. A device the controller lost may still be powered and forwarding — phrase as "controller reports disconnected," not "device is down."
   - WLANs: enabled WLANs with SSID, security mode (flag open or WEP/WPA1), and network binding.
3. "What changed?" → check what changed: device adds/removals, firmware upgrades, WLAN edits around the incident window (time-adjacency, not proven cause).
4. Never expose wifi PSKs in notes — point to the documentation platform. Output: inventory/config table, source + data age, flags (offline devices, firmware drift, weak WLAN security, single-AP-per-site SPOFs). Offer to leave a plain-text note. Degradation: inspector absent → documentation → ticket history → "verify on controller."
```
