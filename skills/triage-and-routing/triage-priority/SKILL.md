---
name: Triage Priority
description: Set the priority on a new ticket whose priority is empty from impact and urgency, checked against learned rules and how techs prioritized similar tickets.
category: Triage & Routing
tools: [list_ticket_priorities, update_ticket]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Triage Priority

**When to use:** Priority is blank on new tickets and you want it set from who is affected and whether they are blocked, corrected over time by your techs. Run by the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`). For a standalone priority pass without the learning loop, use Auto Priority Classification (`triage-and-routing/auto-priority-classification`).

**Run it:** on one ticket · or inside a triage Flow. Replace the definitions with your desk's own and match the level names to your PSA.

## Prompt

```
Purpose: set the priority on a new ticket. Only run when priority was empty in the orchestrator's snapshot. Never overwrite a priority a person chose.

PRIORITY DEFINITIONS (use the highest that applies; replace with your desk's)
Critical
- Broken for the whole company (all email down, office internet down, main server down, nobody can log in).
- Any security issue: compromised account, phishing link clicked, suspicious sign-in, ransomware or malware alert, an advisory flagged as actively exploited.
- Urgent offboarding (termination, access must be cut now).
High
- Broken for a whole department or site.
- The person is blocked from their work (can't log in, can't open the app their job depends on, no internet).
- Urgent onboarding (starts today or tomorrow).
Medium
- Broken for one person, but they can still work.
- Scheduled onboarding or offboarding with notice.
Low
- A request for something new with no outage (new software, how-to, documentation update, a quote).

HOW TO DECIDE
1. Read the "Triage Learnings" LEARNED RULES. If one matches, use it.
2. Find the IMPACT: who is affected (company, department, one person).
3. Find the URGENCY: are they blocked, or is this a request?
4. Take the higher of the two.
5. Check the "Triage Similar Tickets" priority pattern. If agreement is Strong and it differs from your pick by one level, use the pattern. Never move to Critical on the pattern alone.
6. If impact is unclear, use Medium.
7. Never choose Critical without a clear company-wide or security signal in the text. "Urgent" or "ASAP" alone is not enough.
8. Alert-generated tickets (backup failed, disk space) are Medium unless the text shows a company-wide outage or data loss.
Only use priority levels that exist on this desk. Never invent one.

OUTPUT
Write the priority to the ticket. Report back to the orchestrator (no note of your own):
Priority: <value> | Signal: <e.g. "whole company - all email down"> | Confidence: High/Medium/Low
```
