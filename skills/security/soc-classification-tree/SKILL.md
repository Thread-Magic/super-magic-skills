---
name: SOC Classification Tree
description: Classify a security-board ticket down the Incident/Request/Problem tree and set type, subtype, and item consistently — use whenever a security ticket needs classification or a tech asks how to categorize an alert.
category: Security
tools: [list_boards, list_ticket_statuses, search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: no
role: [Dispatcher, Security & Compliance Owner]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# SOC Classification Tree

**When to use:** A new security-board ticket needs its classification set; a tech asks whether an alert is an Incident or a Request; or a classification cleanup pass across recently opened security tickets.

**Run it:** on one ticket · or across recently opened security tickets (a classification cleanup pass).

## Prompt

```
Walk a deterministic decision tree that turns "what kind of ticket is this?" into a
consistent Incident/Request/Problem classification with type, subtype, and item — so
reporting, SLAs, and escalation paths stay trustworthy. Work this ticket, or each ticket in
the set I point you at, in order:

1. Walk the top of the tree:
   - Incident — something happened that shouldn't have: an alert fired, suspicious activity
     was detected or reported, a control failed. All SOC alerts, phishing reports, and
     detections start here.
   - Request — someone is asking for an action: release a quarantined message, allowlist a
     sender, adjust a rule, grant an exception.
   - Problem — a recurring root cause spanning multiple incidents (the same benign alert
     firing weekly, the same misconfiguration resurfacing). Link the member incidents to it.
2. Select type/subtype/item from the board's configured values (look them up from the board's
   own field options — never invent values). Map common patterns: sign-in anomaly →
   Identity; reported email → Email Security / Phishing; EDR detection → Endpoint; credential
   exposure → Identity / Credential Exposure; lookalike domain → Email Security /
   Impersonation.
3. When two branches both fit, classify by the response the ticket needs, not the tool that
   sent it — a quarantine-release ask arriving from the mail filter is still a Request.
4. Apply the classification and record a one-line plain-text note stating the branch taken
   and why, so the next person can follow the decision.
5. Set a working status only. If the ticket is finished, move it to the desk's pre-closure
   status (for example "Ready to Close") — final closure statuses on security boards are
   restricted to management.

Guardrails — always:
- Never set a final closed status on a security-board ticket; closure is a management action.
  Move to the pre-closure status and stop.
- Never invent type/subtype/item values — only use values that exist on the board's own
  configuration.
- Ambiguous after walking the tree → classify at the safest broader level and flag for a
  human rather than guessing a leaf value.
- Reclassifying an existing ticket wipes reporting history context — note the previous
  classification when changing one.
- Document the decision, not just the action: the note states why the branch was chosen.
```
