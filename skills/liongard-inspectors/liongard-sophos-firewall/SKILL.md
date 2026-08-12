---
name: Liongard Sophos Firewall Read
description: Interrogate a client's Sophos Firewall (XG/SFOS) through the Liongard Sophos Firewall inspector — firmware, firewall rules, port-forwards/NAT, VPN config, interfaces, admin access. Use for "what's their Sophos firewall config?", rule/exposure review during triage, or firmware-currency checks.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Sophos Firewall Read

**When to use:** "What firewall rules / port-forwards are configured at <client>?", a connectivity or exposure ticket, "what firmware is their Sophos firewall on?", a VPN troubleshooting read, or "did a rule or NAT entry change?".

**Run it:** on one client — name the client and the Sophos firewall question.

## Prompt

```
Read Sophos Firewall (SFOS / XG) config for CLIENT_NAME from the Liongard Sophos Firewall inspector. Read-only — firewall changes go through the partner's change process.

1. Resolve the client's environment, then find the Sophos Firewall inspector and confirm it ran recently — carry "as of <timestamp>." A client may have multiple firewalls — enumerate them.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Rules: firewall rule list with action, source/dest zones, service — flag any-any allows.
   - Port-forwards/NAT: inbound NAT entries with external port to internal host — flag exposure of RDP/3389, SMB/445.
   - Firmware: current SFOS version — report verbatim, compare against vendor's current release.
   - VPN: IPsec/SSL tunnel list with peers and status.
   - Admins: local/remote admin accounts and access methods.
3. "What changed?" → check what changed on the firewall: rule adds/edits, NAT changes, firmware upgrades, admin adds — ordered against the incident window (time-adjacency, not proven cause).
4. Sanity-check surprising zeros (zero rules) — usually a wrong field angle or partial inspection; re-probe broadly. Never paste PSKs, VPN pre-shared keys, or credentials into notes — reference "PSK on file in <doc platform>." Exposure findings are risk inputs, not confirmed breaches — "external RDP NAT present, verify need" phrasing.
5. Output: a compact table, source + data age line, flags (risky inbound NAT, any-any rules, outdated firmware, unexpected admins). Offer to leave a plain-text note. Degradation: no Sophos Firewall inspector → documentation → ticket history → "verify on appliance."
```
