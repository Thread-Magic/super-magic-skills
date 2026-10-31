---
name: Triage Closure Review
description: When a ticket closes, compare what the triage skills set or recommended with what the tech left, and update the Triage Learnings skill only when repeated real misses prove a rule will raise accuracy.
category: QA & Closure
tools: [search_tickets, list_skills, update_skill, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Triage Closure Review

**When to use:** You run the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`) and want it to learn from your techs. Each closed ticket is scored against the triage note, real misses go on a watchlist, and repeated misses become learned rules in Triage Learnings (`automation-and-flows/triage-learnings`).

**Run it:** as a Flow (when a ticket enters your closed or resolved status, on the same boards as the triage Flow) · or on one closed ticket by hand. Give the Flow agent one rule beyond this skill: never reopen the ticket or change its fields.

## Prompt

```
Purpose: when a ticket closes, check whether the technician changed what triage set or recommended. Update "Triage Learnings" ONLY when the evidence shows it will raise accuracy. Most tickets need no change.

STEP 1 - COMPARE
Find the "TRIAGE RESULTS" internal note. If there isn't one, stop: "No triage note".
For category, ticket type and priority, compare the note with the value on the closed ticket:
- Note says "kept by person", or the value is unchanged -> nothing to learn.
- Agent set it and the tech changed it -> a CORRECTION.
- Type: note says "recommended" and the closed type is different, or "default is right" and the tech changed it -> a CORRECTION.

STEP 2 - IS IT A REAL TRIAGE MISS?
Read the whole ticket. Discard the correction if:
- the issue changed during the work (a "printer" ticket turned out to be a network fault). The first call was right for what was known at intake.
- the agent's pick also fits the ticket text and the tech simply filed it differently.
- it's a test, merged or deleted ticket, or an automation changed the field, not a person.
- priority changed only because the issue got worse or was resolved.

STEP 3 - RECORD OR LEARN
Describe the pattern as product + problem (e.g. "accounting app error on a single laptop"), never one keyword.
- Matches an existing WATCHLIST item (same field, pattern and tech choice): Count +1, High-conf +1 if the note shows High confidence for that field, add the ticket number, update Last seen.
- Otherwise add a new WATCHLIST item with Count 1.
- PROMOTE a watchlist item to a LEARNED RULE when Count reaches 3, or High-conf reaches 2 (confidently wrong twice). Remove it from the watchlist.
- If a new rule contradicts a learned rule, keep the one with more evidence and add the loser's tickets to the winner's Evidence.
- If the tech's choice matches a learned rule the agent ignored, change nothing. Note "agent missed L<n>".

STEP 4 - SAVE ONLY IF NEEDED
Edit the saved "Triage Learnings" skill only if Step 3 changed something, following its EDITING RULES. Never edit any other skill. Never touch its HOW TO USE or EDITING RULES sections.

STEP 5 - NOTE
Add ONE plain-text internal note, no markdown:
CLOSURE REVIEW
Category: match | corrected | discarded (<reason>)
Type: match | corrected | discarded (<reason>)
Priority: match | corrected | discarded (<reason>)
Learnings: no change | watchlist W<n> (count <n>) | NEW RULE L<n> | agent missed L<n>

RULES
- Read only on this ticket except for the note. Never reopen it or change its fields.
- One correction is a data point, not a rule. Never change rules on a single ticket.
- If you're unsure whether something is a real miss, discard it.
- As a Flow, your entire reply is the note.
```
