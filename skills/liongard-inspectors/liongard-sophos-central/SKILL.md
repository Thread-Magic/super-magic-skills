---
name: Liongard Sophos Central Read
description: Interrogate a client's Sophos Central tenant via Liongard: protected endpoints, threat/health status, tamper protection, policy, and admin list.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline, liongard_alert]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Sophos Central Read

**When to use:** "Is <client> fully protected in Sophos?", an endpoint-security ticket needing the health/threat picture, "is tamper protection on across their fleet?", "who has admin on their Sophos Central?", or "did a policy or exclusion change?".

**Run it:** on one client — name the client and the Sophos Central question.

## Prompt

```
Read Sophos Central tenant state for CLIENT_NAME from the Liongard Sophos Central inspector. Read-only — Sophos policy, exclusions, and enrollment are a technician's job in the console.

1. Resolve the client's environment, then find the Sophos Central inspector and confirm it ran recently — carry "as of <timestamp>." Endpoint health changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Coverage: endpoint list with protection status — count unprotected / not-reporting.
   - Health: devices where health/compliance != good — list for follow-up.
   - Tamper protection: devices with tamper protection disabled — hardening gap.
   - Threats: recent threat/alert entries with status (cleaned vs outstanding).
   - Admins: admin list with role.
3. "What changed?" → check what changed on the Sophos side: policy changes, exclusion adds, admin adds/removes, agent-version shifts — ordered against the incident window. Pull anything already escalated too.
4. Sanity-check surprising zeros (zero endpoints, no admins) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an endpoint in Sophos is a coverage lead, not proof a machine is unprotected — a device may report to a different tenant; reconcile against RMM/AD counts and verify. Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (unprotected devices, tamper-off, outstanding threats, single-admin risk). Offer to leave a plain-text note. Degradation: no Sophos Central inspector → documentation → ticket history → "verify in console."
```
