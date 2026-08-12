---
name: Liongard Webroot Read
description: Interrogate a client's Webroot GSM console via the Liongard Webroot inspector: protected endpoints, agent status, threat state, policy, and sites.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline, liongard_alert]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Webroot Read

**When to use:** "Are <client>'s Webroot endpoints protected and reporting?", a malware/AV ticket needing the infection picture, "which endpoints are flagged infected or needing attention?", "which sites/policies is a device assigned to?", or "did a policy assignment change?".

**Run it:** on one client — name the client and the Webroot question.

## Prompt

```
Read Webroot (Global Site Manager) state for CLIENT_NAME from the Liongard Webroot inspector. Read-only — Webroot policy and enrollment are a technician's job in the console.

1. Resolve the client's environment, then find the Webroot inspector and confirm it ran recently — carry "as of <timestamp>." Endpoint state changes, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Coverage: endpoint list with protection status — count unprotected / not-reporting.
   - Infections: endpoints flagged infected or needing attention.
   - Policy: policy/site assignment per device.
   - Versions: agents on outdated versions.
3. "What changed?" → check what changed on the Webroot side: policy changes, endpoint adds/removes — ordered against the incident window. Pull anything already escalated too.
4. Sanity-check surprising zeros (zero endpoints) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an endpoint in Webroot is a coverage lead, not proof a machine is unprotected — reconcile against RMM/AD counts and verify before asserting.
5. Output: a compact table, source + data age line, flags (unprotected endpoints, infected devices, coverage gaps). Offer to leave a plain-text note. Degradation: no Webroot inspector → documentation → ticket history → "verify in console."
```
