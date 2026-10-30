---
name: Triage Category
description: Set the category on a new ticket whose category is empty, using learned rules first, then how techs filed similar tickets, then your desk's own category rules.
category: Triage & Routing
tools: [list_board_classifications, update_ticket]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Triage Category

**When to use:** New tickets land with no category and built-in categorization keeps picking the wrong branch. You want the pick to follow your techs' corrections and your own written rules. Run by the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`), after Triage Learnings and Triage Similar Tickets.

**Run it:** on one ticket · or inside a triage Flow. Replace the example rules with the lines your techs actually argue about.

## Prompt

```
Purpose: set the category on a new ticket. Only run when the category was empty in the orchestrator's snapshot. Never overwrite a category a person chose.

HOW TO DECIDE
1. Read the ticket text, the "Triage Learnings" LEARNED RULES and the "Triage Similar Tickets" result.
2. If a learned rule matches, use it. It overrides everything below.
3. Else if the category agreement is Strong, use that category, even over the rules below. Say so.
4. Otherwise apply the rules below. Pick the most specific level on the ticket's board (e.g. Server > Patch Management, not Server). Only pick from the board's live category list. Never invent a value.

DESK RULES (replace these examples with your own)
- Server > Patch Management: patching, failed updates, reboot scheduling, and vendor security advisories that need a patch, even for backup or remote-access products. Not cloud tenant security.
- Server > Software: services, roles and self-hosted apps ON A SERVER. Not patches, not new builds.
- Server > Hardware: disk or storage expansion, hardware faults, new servers or VMs. Not backups or snapshots.
- Backup/Restore > <product>: only that product's backup jobs, failures and restores. Not its RMM agent, monitoring or patches.
- Cloud App > Security: SaaS tenant security only: suspicious sign-ins, conditional access, tenant alerts, compromised accounts. Never vendor advisories.
- Cloud App > Config: M365 or Google admin tasks: mailboxes, groups, license assignment, Teams settings, sharing.
- Firewall > Troubleshooting: can't reach the office or internal resources over firewall, VPN or SASE. ISP only if the circuit is down.
- Desktop/Laptop > Software: an app problem on ONE user's machine, new PC or Mac setup, software on a single machine.
- All email down with no on-prem Exchange mentioned: the cloud email category, not Server.
- License, pricing or quote questions: Sales, not Technical.

IF IT'S CLOSE
If two categories fit, use the one the similar tickets favour. If they don't settle it, pick the more specific one and mark confidence Low.

OUTPUT
Write the category to the ticket. Report back to the orchestrator (no note of your own):
Category: <value> | Reason: <one line, naming any learned rule used> | Confidence: High/Medium/Low
```
