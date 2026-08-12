---
name: Liongard FortiGate Read
description: Interrogate a client's FortiGate via the Liongard Fortinet inspector: FortiOS firmware, policy changes, VPN tunnels, admin accounts, license state.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard FortiGate Read

**When to use:** "What FortiOS version is <client> running?" against a PSIRT advisory, VPN tunnel/peer inventory before diving into logs, "who has admin / is admin access open to the WAN?", "did their firewall policies change?", or a FortiGuard/support expiry check.

**Run it:** on one client — name the client and the FortiGate question.

## Prompt

```
Read FortiGate configuration posture for CLIENT_NAME from the Liongard Fortinet FortiGate inspector. Read-only — policy or firmware changes are human-owned through change control.

1. Resolve the client's environment, then find the FortiGate inspector(s) and confirm each ran recently — carry "as of <timestamp>" on every answer. HA pairs or multiple sites mean multiple inspectors — enumerate and answer per device.
2. Read the values from the latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Firmware: the FortiOS version string — report it verbatim and let the tech map it to advisories; do NOT label a version "vulnerable" from memory — recommend verifying against Fortinet's current PSIRT advisories.
   - Policies: policy count, and policies where action == accept with source/destination "all" — the overly-broad-rule flag.
   - VPN: tunnel list with name, remote peer, status — the inventory for a VPN incident.
   - Admins: admin accounts with trusted-host settings — empty trusted-host on a WAN-reachable interface is the finding.
   - Licensing: subscription/support expiry — flag anything within 90 days.
3. "What changed?" → check what changed on the FortiGate: policy adds/edits, admin changes, firmware upgrades. Policy-change detections around an outage window are the highest-value correlation — label it time-adjacency, not proven cause. A data read hours old can miss the change that caused the incident; state age and say "config may have changed since last inspection" on active incidents.
4. Never reproduce PSKs, certificates, or credential material from the dataprint in notes. Output: facts table, source + data age, flags (firmware stated as "verify against Fortinet PSIRT", broad policies, unrestricted admin access, expiring subscriptions, unexplained policy changes). Offer to leave a plain-text note. Degradation: inspector absent/failing → documentation → ticket history → "verify on device"; repeated inspector auth failures on a firewall are themselves worth a ticket.
```
