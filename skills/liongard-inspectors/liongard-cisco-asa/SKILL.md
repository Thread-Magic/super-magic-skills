---
name: Liongard Cisco ASA Read
description: Interrogate a client's Cisco ASA firewall via Liongard: software version, interfaces, ACLs/NAT, IPsec/AnyConnect VPN config, and admin access review.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Cisco ASA Read

**When to use:** "What access lists / NAT rules are configured at <client>?", a connectivity or exposure ticket needing the ACL/NAT picture, "what ASA version are they on?", a VPN (IPsec site-to-site / AnyConnect) troubleshooting read, or "did an ACL or NAT entry change?".

**Run it:** on one client — name the client and the ASA question.

## Prompt

```
Read Cisco ASA firewall config for CLIENT_NAME from the Liongard Cisco ASA inspector. Read-only — ASA changes go through the partner's change process.

1. Resolve the client's environment, then find the Cisco ASA inspector and confirm it ran recently — carry "as of <timestamp>." A client may have multiple ASAs — enumerate them.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - ACLs: access-list entries with action, source/dest, service — flag permit any any.
   - NAT: static/inbound NAT with external port to internal host — flag exposure of RDP/3389, SMB/445.
   - Version: ASA software version — report verbatim and recommend verifying against current advisories, not memory.
   - VPN: IPsec site-to-site peers and AnyConnect config.
   - Admins: local admin accounts and access methods (SSH/ASDM).
3. "What changed?" → check what changed on the ASA: ACL adds/edits, NAT changes, version upgrades, admin changes — ordered against the incident window (time-adjacency, not proven cause).
4. Sanity-check surprising zeros (zero ACL entries) — usually a wrong field angle or partial inspection; re-probe broadly. Never paste PSKs, VPN pre-shared keys, or credentials into notes — reference "PSK on file in <doc platform>." Exposure findings are risk inputs, not confirmed breaches — "external RDP NAT present, verify need" phrasing.
5. Output: a compact table, source + data age line, flags (permit-any ACLs, risky inbound NAT, outdated version, unexpected admins). Offer to leave a plain-text note. Degradation: no ASA inspector → documentation → ticket history → "verify on appliance"; also check the generic Cisco network inspector.
```
