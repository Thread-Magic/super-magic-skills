---
name: Liongard Datto RMM Read
description: Interrogate a client's Datto RMM footprint via Liongard: managed device inventory, agent online status, patch state, monitored alerts, and sites.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Datto RMM Read

**When to use:** "What devices does Datto RMM manage at <client>?", "which agents are offline / not checking in?", "are their machines patched?" during triage, reconciling RMM count against AD/security-tool counts, or "did monitoring or patch policy change?".

**Run it:** on one client — name the client and the Datto RMM question.

## Prompt

```
Read Datto RMM state for CLIENT_NAME from the Liongard Datto RMM inspector. Read-only — this never runs scripts, deploys software, or changes RMM policy.

1. Resolve the client's environment, then find the Datto RMM inspector and confirm it ran recently — carry "as of <timestamp>." Agent status changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Inventory: device list with OS and last-seen — group by site.
   - Offline agents: devices whose last-check-in exceeds a threshold.
   - Patch state: devices with missing/failed patches.
   - Alerts: open monitored alerts with severity.
3. "What changed?" → check what changed on the Datto RMM side: device adds/removes, monitor/policy changes, agent-version shifts — ordered against the incident window.
4. Sanity-check surprising zeros (zero devices) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of a device in RMM is a coverage lead, not proof it is unmanaged — reconcile against AD/AV counts and verify before asserting.
5. Output: a compact table, source + data age line, flags (offline agents, patch laggards, coverage gaps). Offer to leave a plain-text note. Degradation: no Datto RMM inspector → documentation → ticket history → "verify in console."
```
