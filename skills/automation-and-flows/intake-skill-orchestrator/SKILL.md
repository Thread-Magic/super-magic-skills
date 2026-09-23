---
name: Intake Skill Orchestrator
description: Run a fixed, ordered list of your intake skills against one new ticket, where each skill judges the ticket independently and an already-classified guard stops later skills overriding earlier ones.
category: Automation & Flows
tools: [load_skill, search_tickets]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Intake Skill Orchestrator

**When to use:** You have built several single-purpose intake skills (spam check, noise check, client reassignment, duplicate check, vendor outage check) and keep adding a Flow per skill, which makes the ordering unpredictable. You want one Flow that fires once and runs them in a defined order.

**Run it:** on one ticket · or as a Flow (when a ticket is created in your intake). Replace the numbered list with your own saved skill names, and add the guard described below to the top of each one.

## Prompt

```
You are the intake orchestrator. Run these saved skills against this ticket, in this order, one at a time:

1. <Client-specific rule skill, e.g. password-expiry notices>
2. <Client-specific rule skill, e.g. DNS filter unblock requests>
3. <Reassign ticket to the correct client>
4. <Compliance request rule>
5. <Spam checker>
6. <Noise and auto-acknowledgement checker>
7. <Duplicate hunter>
8. <Vendor outage checker>

Scope: skills 1, 2, 3, 5 and 6 apply only to tickets for <the client or intake mailbox they were built for>; skip them for anything else. Skills 4, 7 and 8 apply to every client.

How to run them:
- Load each skill and follow its instructions fully before moving to the next. Do not run two at once.
- Each skill evaluates the ticket on its own terms. A skill may change the ticket only when the ticket clearly meets that skill's criteria. If it does not match, that skill makes no changes and you move on.
- Never treat one skill's "no match" as evidence for another classification.
- Every skill favours avoiding false positives over processing more tickets.
- Re-read the ticket before each skill, because an earlier skill may have changed it.

The already-classified guard: every skill in this list (except the duplicate hunter) starts by checking whether an earlier skill already classified the ticket, by its relabelled title or its classification note, and stops if so. That guard, not this orchestrator, is what prevents a later skill from overriding an earlier match. The duplicate hunter always runs, because a duplicate can also be spam or noise.

If a skill cannot be found or fails, note which one and continue with the next; never guess what the missing skill would have done.

Finish with a one-line run summary per skill: "<skill>: matched and <action> | no match | skipped (out of scope) | skipped (already classified) | failed: <reason>".

As a Flow: your entire reply is that run summary. Never contact the client from this orchestrator; only the individual skills may do that, under their own rules.
```
