---
name: Flow Bulk Editor
description: List the desk's flows, present the target set, then bulk enable / disable / rename them in one confirmed pass — no editing each flow by hand. Answers the "turn these flows off / rename this batch" workflow; runs manually on demand.
category: Automation & Flows
tools: [list_flows, get_flow, update_flow]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Flow Bulk Editor

**When to use:** "Disable all the flows for <client>" / "rename this batch of flows to the new naming scheme" / "bulk enable/disable the flows matching <pattern>" / prepping for a maintenance window or client change that touches many flows.

**Run it:** across a batch of flows — manually on demand (bulk flow edits stay human-confirmed, so there's no Flow trigger for this one).

## Prompt

```
Flip a batch of flows on or off, or rename a group to a new convention, in one confirmed
pass. Member-invoked only; no unattended variant (a flow bulk-editing flows is not a
supported trigger, and this should stay human-confirmed).

1. List all flows. Identify the target set from the member's criteria
   (client, name pattern, current state) and open each for detail where needed to confirm
   each is the right one. Never act on a vague "all the X flows" without showing the
   resolved list first — act only on flows that actually exist in the list.

2. Present the target set as a table: flow name, current state (enabled/disabled), and the
   proposed change (enable / disable / rename -> new name). This is the review gate. Flag
   high-impact toggles (disabling a flow that handles P1 routing or SLA escalation) so the
   member knows what goes quiet.

3. For renames, show current -> proposed name per flow and check the new names don't collide.

4. Wait for explicit confirmation. Let the member drop individual flows from the batch
   first — bulk-toggling automation can silence real alerting or unleash it.

5. On confirm, apply the change flow by flow, tracking each result.

6. Report a summary: which flows changed, which were skipped, and any failures. Never
   report the batch as done if one didn't take.
```
