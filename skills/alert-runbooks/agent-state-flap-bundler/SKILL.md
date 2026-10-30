---
name: Agent State Flap Bundler
description: Bundle repeated endpoint agent enabled and disabled alerts for one machine into the oldest ticket, then set that parent's title, subtype and status from the newest state so only a still-disabled agent stays open.
category: Alert Runbooks
tools: [search_tickets, merge_ticket, update_ticket, add_ticket_note, list_ticket_statuses, set_ticket_classification]
connectors: []
scope: single
flow: yes
role: [Security & Compliance Owner, Dispatcher]
outcome: [Fewer Escalations & Less Noise, Always-On Coverage]
---

# Agent State Flap Bundler

**When to use:** Your EDR or RMM opens a ticket every time an endpoint agent changes state ("Agent Disabled", then "Agent Enabled" ten minutes later after a reboot or update). The pairs flood the security board, and the only question that matters is whether the agent is still off.

**Run it:** on one ticket · or as a Flow (when an agent status alert ticket is created). Pair it with Alert Threshold Problem Ticket (`alert-runbooks/alert-threshold-problem-ticket`) when a machine keeps flapping for days.

## Prompt

```
Bundle agent on/off alerts for one machine and leave one ticket that tells the truth about its current state.

1. EXTRACT. From this ticket's title, extract the machine name and the state (enabled or disabled). Expected shape: "<Tool> - Agent <State> - Machine <Name>". If either is missing, make no changes, add the internal note "Could not extract machine name or agent state from the title. Manual review needed." and stop.

2. FIND. Search open and closed tickets on the same board with the same alert type whose titles contain the machine name, updated in the last 6 hours. Always include this ticket even if search has not indexed it yet. Fewer than two: add the internal note "Only one agent status ticket for <machine>. No bundling needed." and stop.

3. ORDER. Sort by created date. The oldest is the parent; the others are children.

4. STATE. Read the newest ticket's title and messages and decide the current state:
- Enabled signals: agent enabled, protection active, agent running, re-enabled.
- Disabled signals: agent disabled, protection off, agent stopped, tampered, uninstalled.
Unclear: add the internal note "Agent state unclear. Manual review needed." and stop. Never guess on a security control.

5. BUNDLE. Merge each child into the parent. Add an internal note on the parent: "Bundled <ticket numbers>. Current agent state: <Enabled/Disabled>."

6. UPDATE THE PARENT (look up the real status names on that board first):
- Enabled: subtype "Agent Enabled", title "Enabled - <Tool> Agent Enabled - Machine <Name>", status your auto-closed or resolved status.
- Disabled: subtype "Agent Disabled", title "Disabled - Action Required - <Tool> Agent Disabled - Machine <Name>", status your action-required status.
If a subtype does not exist on the board, leave the subtype and say so in the note.

7. NOTE. On the parent, add an internal note: tickets matched, what was bundled, the state detected and the evidence, and the title, subtype and status changes made.

A disabled agent must never be auto-closed. Never invent ticket numbers. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the final note.
```
