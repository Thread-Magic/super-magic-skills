---
name: Liongard ConnectWise Automate Read
description: Interrogate a client's ConnectWise Automate (LabTech) footprint through the Liongard Automate inspector — managed computer inventory, agent check-in status, patch state, monitors, locations. Use for "what does Automate manage for them?", offline-agent checks, or patch-currency questions during triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard ConnectWise Automate Read

**When to use:** "What computers does Automate manage at <client>?", "which agents haven't checked in?", "are machines patched?" during triage, reconciling Automate count against AD/security-tool counts, or "did a monitor or patch policy change?".

**Run it:** on one client — name the client and the Automate question.

## Prompt

```
Read ConnectWise Automate (LabTech) state for CLIENT_NAME from the Liongard Automate inspector. Read-only — this never runs scripts, deploys software, or changes Automate policy.

1. Resolve the client's environment, then find the ConnectWise Automate / LabTech inspector and confirm it ran recently — carry "as of <timestamp>." Agent status changes constantly, so an old data read on an active incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Inventory: computer list with OS and last-contact — group by location.
   - Offline agents: computers whose last-contact exceeds a threshold.
   - Patch state: machines with missing/failed patches.
   - Monitors: monitors in a failed/alerting state.
3. "What changed?" → check what changed on the Automate side: agent adds/removes, monitor/policy changes — ordered against the incident window.
4. Sanity-check surprising zeros (zero computers) — usually a wrong field angle or partial inspection; re-probe broadly. Absence of an agent in Automate is a coverage lead, not proof a machine is unmanaged — reconcile against AD/AV counts and verify before asserting.
5. Output: a compact table, source + data age line, flags (offline agents, patch laggards, coverage gaps). Offer to leave a plain-text note. Degradation: no Automate inspector → documentation → ticket history → "verify in console."
```
