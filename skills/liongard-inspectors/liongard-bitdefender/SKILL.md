---
name: Liongard Bitdefender Read
description: Interrogate a client's Bitdefender GravityZone tenant through the Liongard Bitdefender inspector — protected endpoints, agent/module status, threat detections, policy assignment, admins. Use for "are their Bitdefender endpoints protected?", coverage-gap checks, or AV/EDR posture questions during triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline, liongard_alert]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Bitdefender Read

**When to use:** "Are <client>'s Bitdefender endpoints protected and reporting?", a malware/AV ticket needing the health picture, "which endpoints have protection modules disabled?", "who has admin on their GravityZone?", or "did a policy or exclusion change?".

**Run it:** on one client — name the client and the Bitdefender question.

## Prompt

```
Read Bitdefender GravityZone state for CLIENT_NAME from the Liongard Bitdefender inspector. Read-only — Bitdefender policy, exclusions, and enrollment are a technician's job in the console.

1. Resolve the client's environment, then find the Bitdefender / GravityZone inspector and confirm it ran recently — carry "as of <timestamp>" on every answer. Endpoint health changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Coverage: endpoint list with protection status — count unprotected / not-reporting.
   - Modules: endpoints with a protection module disabled.
   - Threats: recent detections with status (resolved vs outstanding).
   - Admins: admin list with role.
3. "What changed?" → check what changed on the Bitdefender side: policy changes, exclusion adds, admin adds/removes — ordered against the incident window. Pull anything already escalated too.
4. Sanity-check surprising zeros (zero endpoints) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an endpoint in Bitdefender is a coverage lead, not proof a machine is unprotected — reconcile against RMM/AD counts and verify before asserting. Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (unprotected endpoints, disabled modules, outstanding threats, single-admin risk). Offer to leave a plain-text note. Degradation: no Bitdefender inspector → documentation → ticket history → "verify in console."
```
