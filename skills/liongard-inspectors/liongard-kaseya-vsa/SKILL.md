---
name: Liongard Kaseya VSA Read
description: Interrogate a client's Kaseya VSA footprint through the Liongard Kaseya VSA inspector — managed agent inventory, online/check-in status, patch state, monitor sets, organizations/machine groups. Use for "what does VSA manage for them?", offline-agent checks, or patch-currency questions during triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Kaseya VSA Read

**When to use:** "What machines does Kaseya VSA manage at <client>?", "which agents haven't checked in?", "are machines patched?" during triage, reconciling VSA count against AD/security-tool counts, or "did a monitor set or patch policy change?".

**Run it:** on one client — name the client and the Kaseya VSA question.

## Prompt

```
Read Kaseya VSA state for CLIENT_NAME from the Liongard Kaseya VSA inspector. Read-only — this never runs scripts, deploys software, or changes VSA policy.

1. Resolve the client's environment, then find the Kaseya VSA inspector and confirm it ran recently — carry "as of <timestamp>." Agent status changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Inventory: agent list with OS and last-check-in — group by machine group.
   - Offline agents: agents whose last-check-in exceeds a threshold.
   - Patch state: machines with missing/failed patches.
   - Monitors: monitor sets in an alarm state.
3. "What changed?" → check what changed on the VSA side: agent adds/removes, monitor/policy changes — ordered against the incident window.
4. Sanity-check surprising zeros (zero agents) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an agent in VSA is a coverage lead, not proof a machine is unmanaged — reconcile against AD/AV counts and verify before asserting.
5. Output: a compact table, source + data age line, flags (offline agents, patch laggards, coverage gaps). Offer to leave a plain-text note. Degradation: no Kaseya VSA inspector → documentation → ticket history → "verify in console."
```
