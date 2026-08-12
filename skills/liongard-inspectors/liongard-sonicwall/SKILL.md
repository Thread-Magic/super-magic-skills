---
name: Liongard SonicWall Read
description: Interrogate a client's SonicWall through the Liongard inspector — SonicOS firmware, security-services licensing and expiry, access rules, VPN policies, admin accounts. Use for firewall triage context, the classic "security services just expired" check, or posture review.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard SonicWall Read

**When to use:** "Are <client>'s SonicWall security services current?" (or a content-filtering/AV ticket that smells like an expired subscription), a SonicOS firmware-currency check, VPN policy inventory, "who can log into their SonicWall?", or "did the firewall rules change before this outage?".

**Run it:** on one client — name the client and the SonicWall question.

## Prompt

```
Read SonicWall configuration and licensing state for CLIENT_NAME from the Liongard SonicWall inspector. Read-only — renewals, rule changes, and upgrades are human-owned.

1. Resolve the client's environment, then find the SonicWall inspector(s) and confirm each ran recently — carry "as of <timestamp>." Multiple appliances (HA, branch units) → enumerate and answer per device.
2. Read the values from the latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Licensing (the priority read): per-service license status + expiry (Gateway AV, Anti-Spyware, IPS, Content Filtering, support) — flag anything expired or expiring within 90 days and state the impact in plain terms ("content filtering will stop enforcing"). Get expiry dates verbatim, never estimated, and carry the data age (an expiry read from a week-old data read may already have been renewed).
   - Firmware: SonicOS version string; report as-is and recommend verifying against SonicWall's current advisories rather than asserting vulnerability from memory.
   - Rules: access-rule count, and any-any allow rules or rules with logging disabled.
   - VPN: policy list with peer gateways and enabled state.
   - Admins: accounts; flag default "admin" still enabled alongside named accounts, or management exposed on WAN zones if visible.
3. "What changed?" → check what changed: rule changes, admin changes, firmware upgrades, license-state transitions. A license expiring is a change worth catching before the tickets arrive — label incident correlations time-adjacency, not proven cause.
4. Never reproduce shared secrets or credentials from VPN policy data in notes. Output: facts + a dedicated license table (service / status / expiry), source + data age, flags, and follow-ups (renewal quote, firmware review). Offer to leave a plain-text note. Degradation: inspector absent → documentation → ticket history → "verify on device"; a SonicWall inspector failing auth repeatedly is its own finding.
```
