---
name: SOC Alert Intake and Correlation
description: Process an inbound SOC alert ticket unattended — correlate it to its case number, state the severity facts, set the priority the security protocol requires, and hand a human a documented incident decision.
category: Security
tools: [search_tickets, list_ticket_priorities, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Security & Compliance Owner]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# SOC Alert Intake and Correlation

**When to use:** SOC alerts land on a security board faster than anyone can tier them, and the same case arrives as several tickets. This is the unattended front door: it correlates the case, records the severity facts, applies the priority the protocol demands, and states whether the alert is an Incident — so the first human to open the ticket starts from a decision instead of a raw alert. Related: `security/soc-classification-tree` is the human walk that actually sets type, subtype, and item; this skill only recommends them.

**Run it:** on one ticket · or as a Flow (when a ticket is created on a SOC alert board).

## Prompt

```
Process an inbound SOC alert ticket: correlate it to its case, state the severity facts,
set the priority the desk's protocol requires, and hand a human a documented decision.
Changing priority and posting one internal note are the only writes.

1. READ the ticket: subject, body, the alert's own fields, and any technician notes.
Pull the SOC case number. If the alert carries none, say so in the note and skip step 2.

2. CORRELATE. Search open tickets for that case number. Report either the other active
ticket numbers carrying it, or that this is the only active ticket for the case. Never
merge, close, or link anything: correlation is a finding for a human, not an action.

3. EXTRACT the severity facts verbatim from the alert, inventing nothing: SOC severity
level, the provider's own classification, threat score if present, and one line on the
activity (who or what did what, to which host or account).

4. SET PRIORITY per the desk's severity map (fill yours in here; the row this was built
from is: SOC severity High requires the incident priority tier). Never lower a priority
— already at or above the mapped tier, leave it and record it as unchanged. State which
rule fired.

5. DECIDE INCIDENT, YES or NO, by that same protocol, and name the criterion met. High
SOC severity qualifies on its own: suspicious activity with no confirmed compromise is
still an incident at that severity, and the note should say exactly that when it applies.

6. RECOMMEND type > subtype > item using only values that exist on the board's own
configuration. Never invent one, and never write the classification yourself.

7. NAME THE NEXT STEP in one line: the human action this ticket now needs.

8. NOTE. Post one internal note in exactly this shape:

SECURITY AUTOMATION PROCESSING COMPLETE

SOC Case Correlation: [case number]
[other active tickets for this case, or "only active ticket for this case"]

SOC Severity Assessment: [level]
Classification: [the alert's own classification]
Threat Score: [score, or "not stated"]
Activity: [one line]

Priority Update: [tier set, or "unchanged, already at or above"]
Rationale: [the rule that fired]

Incident Classification: [YES or NO]
Criteria met: [the criterion]

Recommended Classification: [type] > [subtype] > [item]

Next Steps: [the action]

Guardrails:
- Never change status, board, assignee, type, subtype, or item; never merge or close a
ticket; never contact the client.
- Never invent a severity, score, or case number. A field the alert does not carry is
recorded as not stated.
- Unclear severity or a malformed alert: post the note with what you have, set no
priority, and say a human must tier it.
- Notes are plain text, no markdown or emojis (apply the PSA Note Discipline skill).
```
