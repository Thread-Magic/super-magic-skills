---
name: Monitoring Companion Merge
description: Merge companion tickets that multiple monitoring tools opened for the same underlying event on the same device, folding them into one parent within a time buffer.
category: Triage & Routing
tools: [search_tickets, merge_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Monitoring Companion Merge

**When to use:** The same device or site generated near-simultaneous tickets from different monitoring tools (a server goes down and three tools notice), a flow checks new alert tickets for companions from sibling tools, or queue cleanup after an outage left a cluster of same-event alerts.

**Run it:** on one alert ticket · across a cluster of same-event alerts · or as a Flow (when a new alert ticket is created).

## Prompt

```
When RMM, backup, EDR, and uptime tools each open their own ticket for one real-world
event, fold the companions into a single parent so one tech works one incident.

1. Read the new alert ticket: client, device/asset identifier, event type, and alert
   timestamp.

2. Search open tickets for the same client referencing the same device (hostname, asset
   tag, or IP as it appears in alert fields) created within the time buffer (default:
   30 minutes either side). Search per identifier, per board if alerts land on multiple
   boards; say so if a search may have capped.

3. Confirm the candidates describe the same underlying event: consistent device and a
   compatible symptom family (offline + heartbeat lost + backup unreachable is one event;
   offline + low disk is not). Same device is mandatory — same client + similar symptom on
   different devices is never a companion merge. Never merge across clients.

4. Choose the parent: the earliest-created ticket among the companions, unless a human is
   already actively working a later one — then that one is the parent.

5. Merge each companion under the parent, then leave one plain-text note on the parent
   listing the merged ticket numbers, the tools they came from, and the shared device/event.

Outside the time buffer → not a companion; leave it. Never merge a ticket that contains a
human (client or tech) message beyond the alert content — flag it instead. If it's unclear
whether two alerts describe one event or two, do not merge; note the relationship. Notes
are plain text.

Running as a Flow: your entire reply is the parent-ticket note, verbatim: "COMPANION
MERGE: merged #<a>, #<b> into #<parent>. Device: <device>. Event: <one line>." or "NO
COMPANIONS FOUND for #<n>. Checked window: <buffer>." Merge only when device match is
exact and all companions are pure alert tickets with no human replies; when in doubt, do
nothing. Cap unattended merges at the configured maximum per run (default: 5); beyond
that, stop and flag a possible storm for the alert-storm skill.
```
