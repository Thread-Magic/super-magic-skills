---
name: Liongard SentinelOne Read
description: Interrogate a client's SentinelOne tenant via Liongard: protected agents, agent/version health, threat detections, policy/site assignment, admins.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline, liongard_alert]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard SentinelOne Read

**When to use:** "Are <client>'s SentinelOne agents healthy and up to date?", an EDR/malware ticket needing the threat picture, "which endpoints aren't reporting to S1?", "who has admin?", or "did a policy or exclusion change on the S1 side?".

**Run it:** on one client — name the client and the SentinelOne question.

## Prompt

```
Read SentinelOne tenant state for CLIENT_NAME from the Liongard SentinelOne inspector. Read-only — S1 policy, exclusions, and agent state are a technician's job in the console.

1. Resolve the client's environment, then find the SentinelOne inspector and confirm it ran recently — carry "as of <timestamp>." Endpoint health changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Coverage: agent list with online/health status — count not-reporting / unhealthy.
   - Versions: agents on outdated agent/engine versions.
   - Threats: recent detections with mitigation status (resolved vs outstanding).
   - Admins: admin list with role.
3. "What changed?" → check what changed on the SentinelOne side: policy changes, exclusion adds, admin adds/removes — ordered against the incident window. Pull anything Liongard already escalated too.
4. Sanity-check surprising zeros (zero agents) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an agent in S1 is a coverage lead, not proof an endpoint is unprotected — reconcile against RMM/AD counts and verify before asserting. Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (unhealthy/not-reporting agents, outdated versions, outstanding threats, single-admin risk). Offer to leave a plain-text note. Degradation: no SentinelOne inspector → documentation → ticket history → "verify in console."
```
