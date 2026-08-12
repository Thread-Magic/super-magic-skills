---
name: Liongard Meraki Read
description: Interrogate a client's Cisco Meraki org via the Liongard Meraki inspector: SSIDs, VLANs, firmware, admin list, device inventory, and license state.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Meraki Read

**When to use:** "What SSIDs are broadcast / which VLAN is the guest wifi on at <client>?", a wifi or connectivity ticket, "who has admin on their Meraki org?", "when do their Meraki licenses expire / what firmware are the APs on?", or "did anything change on the Meraki side?".

**Run it:** on one client — name the client and the Meraki question.

## Prompt

```
Read Meraki dashboard state for CLIENT_NAME from the Liongard Cisco Meraki inspector. Read-only — Meraki changes go through the partner's change process.

1. Resolve the client's environment, then find the Meraki inspector (a client may have one org-level inspector covering many networks) and confirm it ran recently — carry "as of <timestamp>."
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - SSIDs: enabled SSIDs with auth mode and VLAN tagging.
   - VLANs: subnet map (id, name, subnet).
   - Firmware: device list grouped by model + firmware — flag mixed versions within a model family.
   - Admins: org admin list with privilege ("full" vs "read-only") — count full admins and list names.
   - Licensing: license state and expiration — flag anything expiring within 90 days.
3. "What changed?" → check what changed on the Meraki side: SSID/PSK changes, VLAN edits, admin adds/removes, firmware upgrades — ordered against the incident window (time-adjacency, not proven cause). Wireless config changes often, so an old data read on an active wifi incident deserves a "may be stale — verify live" caveat.
4. Sanity-check surprising zeros (zero SSIDs, no admins) — usually a wrong field angle or partial inspection; re-probe broadly. Never paste PSKs or credentials into notes — reference "PSK on file in <doc platform>." Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (expiring licenses, single-admin risk, firmware drift, unexplained recent changes). Offer to leave a plain-text note. Degradation: no Meraki inspector → documentation → ticket history → "verify on dashboard."
```
