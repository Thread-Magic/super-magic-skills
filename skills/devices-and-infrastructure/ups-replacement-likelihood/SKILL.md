---
name: UPS Replacement Likelihood
description: Bundle a UPS's alert history into one ticket and score how likely the battery or unit needs replacing from 1 to 10, so the title shows which UPS to quote first.
category: Devices & Infrastructure
tools: [search_tickets, merge_ticket, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Technician, CSM / Account Manager]
outcome: [Fewer Escalations & Less Noise, Retention & Growth (CSAT/Expansion)]
---

# UPS Replacement Likelihood

**When to use:** UPS alerts (low battery, on battery, possible power outage, offline, replace battery) arrive one at a time and get closed one at a time, so nobody notices the unit that has warned you every week for a month. You want the history in one place and a score that separates a dying battery from a storm.

**Run it:** on one ticket · or as a Flow (when a UPS alert ticket is created). It re-scores each time a new alert arrives for the same unit. For working a single alert, see APC UPS Alerts (`vendor-runbooks/apc-ups-alerts`).

## Prompt

```
Bundle this UPS's alerts and score how likely it needs replacing.

1. KEY. Extract the UPS device ID from the title. No ID: use the client plus the UPS model or description as the key.

2. HISTORY. Search open and closed tickets for the same client in the last 30 days that carry the key. Include this ticket.

3. BUNDLE. Two or more: pick the oldest (or most descriptive) as parent and merge the others into it. Do not close anything else. Add an internal note listing every ticket: "#<number> | <title> -> <status> | <created>".

4. SCORE 1 to 10 from all signals across the history:
9 to 10, replace now: a replace-battery alert; repeated low-battery alerts over days or weeks; repeated offline plus low battery; a request to replace already on file.
6 to 8, likely soon: two or more low-battery alerts; low battery plus a power event; offline with no outage context; a hardware error code.
3 to 5, monitor: one low-battery event; a power event only; offline once and recovered.
1 to 2, power event, unit fine: only outage alerts, no battery signals, no recurrence.
When signals conflict, take the higher band and say why.

5. NOTE on the parent: "UPS replacement likelihood: <score>/10. <One sentence naming the signals that drove it>."

6. TITLE. Prefix the parent title with "RL<score> - ". If it already starts with an "RL<n> - " prefix, replace it; never stack prefixes.

Only one ticket: skip bundling, still score and prefix. Never close tickets, order hardware or contact the client. Never invent alerts or dates. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the score note.
```
