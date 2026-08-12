---
name: Liongard N-central Read
description: Interrogate a client's N-able N-central footprint via Liongard: managed device inventory, agent/probe status, patch state, monitored services, sites.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard N-central Read

**When to use:** "What devices does N-central manage at <client>?", "which agents or probes are offline?", "are machines patched?" during triage, reconciling N-central count against AD/security-tool counts, or "did a monitoring service or patch policy change?".

**Run it:** on one client — name the client and the N-central question.

## Prompt

```
Read N-able N-central state for CLIENT_NAME from the Liongard N-central inspector. Read-only — this never runs scripts, deploys software, or changes N-central policy.

1. Resolve the client's environment, then find the N-central inspector and confirm it ran recently — carry "as of <timestamp>." Agent status changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Inventory: device list with OS and last-seen — group by customer/site.
   - Offline agents: devices whose last-check-in exceeds a threshold.
   - Patch state: machines with missing/failed patches.
   - Services: monitored services in a failed/warning state.
3. "What changed?" → check what changed on the N-central side: device adds/removes, service/policy changes — ordered against the incident window.
4. Sanity-check surprising zeros (zero devices) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of a device in N-central is a coverage lead, not proof it is unmanaged — reconcile against AD/AV counts and verify before asserting.
5. Output: a compact table, source + data age line, flags (offline agents, patch laggards, coverage gaps). Offer to leave a plain-text note. Degradation: no N-central inspector → documentation → ticket history → "verify in console."
```
