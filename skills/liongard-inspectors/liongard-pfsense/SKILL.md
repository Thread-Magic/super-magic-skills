---
name: Liongard pfSense Read
description: Interrogate a client's pfSense firewall via the Liongard pfSense inspector: version, interfaces, firewall/NAT rules, VPN config, packages, admins.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard pfSense Read

**When to use:** "What firewall rules / port-forwards are configured at <client>?", a connectivity or exposure ticket, "what pfSense version are they on?", a VPN (IPsec/OpenVPN) troubleshooting read, or "did a rule or NAT entry change?".

**Run it:** on one client — name the client and the pfSense question.

## Prompt

```
Read pfSense firewall config for CLIENT_NAME from the Liongard pfSense inspector. Read-only — firewall changes go through the partner's change process.

1. Resolve the client's environment, then find the pfSense inspector and confirm it ran recently — carry "as of <timestamp>." A client may have multiple firewalls — enumerate them.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Rules: firewall rule list with action, interface, source/dest — flag any-any allows.
   - Port-forwards/NAT: inbound NAT with external port to internal host — flag exposure of RDP/3389, SMB/445.
   - Version: pfSense version — report verbatim, compare against current release.
   - VPN: IPsec/OpenVPN tunnel/server list with peers.
   - Admins: local admin accounts and access methods.
3. "What changed?" → check what changed on pfSense: rule adds/edits, NAT changes, version upgrades, package changes — ordered against the incident window (time-adjacency, not proven cause).
4. Sanity-check surprising zeros (zero rules) — usually a wrong field angle or partial inspection; re-probe broadly. Never paste PSKs, VPN pre-shared keys, or credentials into notes — reference "PSK on file in <doc platform>." Exposure findings are risk inputs, not confirmed breaches — "external RDP NAT present, verify need" phrasing.
5. Output: a compact table, source + data age line, flags (risky inbound NAT, any-any rules, outdated version, unexpected admins). Offer to leave a plain-text note. Degradation: no pfSense inspector → documentation → ticket history → "verify on appliance."
```
