---
name: Billable Scope Router
description: Decide at intake whether a request is covered by the managed agreement or billable project work, using your contract's own criteria, and route it to the matching board with the rule cited.
category: Triage & Routing
tools: [search_tickets, list_boards, update_ticket, add_ticket_note, set_ticket_classification]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Billable Scope Router

**When to use:** You run separate boards for work covered by the managed agreement and for billable work (installs, projects, out-of-scope devices, end-of-life gear), and dispatchers make that call by hand on every ticket. You want the decision made once, at intake, against your written contract terms, with the reason on the ticket for when the client asks.

**Run it:** on one ticket · or as a Flow (when a ticket lands on your triage board). A common setup runs a security keyword gate first (Board Routing Rules Engine (`triage-and-routing/board-routing-rules-engine`)) and sends everything else here. Replace the example criteria with your own agreement's.

## Prompt

```
Make one routing decision: is this request covered or billable? Read the title, description and every message.

STEP 1, BILLABLE (any match makes it billable). Edit these to match your agreement:
A. Damage from an external factor: storms, surges, extended outages.
B. Installs and projects: new workstations, servers, printers or network gear; re-imaging or data transfer; major upgrades (2+ hours); multi-user deployments; new backup devices; new internet service turn-up.
C. Implementation and configuration: procurement, physical install, advanced config, migration, new site or library creation.
D. Out of scope: unsupported A/V, printers, phone systems, database tuning, repair after a third party changed something.
E. End of life: hardware, software or OS without active vendor support; line-of-business apps without a support contract.
F. Security incident work beyond basic containment: recovery, forensics, formal reporting.
G. Residential requests or requests from people who are not client employees.

STEP 2, COVERED (only if nothing in Step 1 matched):
A. A standard break or fix with no external factor.
B. User management: new accounts, terminations, access changes, agent installs.
C. License purchase or renewal only, with no install or configuration.
D. Basic accessories with no complex setup: monitors, keyboards, docks, webcams.

STEP 3, ROUTE. Look up the real board names first.
Billable: move to <your billable board>.
Covered: move to <your covered board>.
Unclear: move to <your covered board>, set the type to <your general break/fix type>, and list the missing facts you need in the note. Default to covered when unsure; billing a client by mistake costs more than reviewing one ticket.

STEP 4, NOTE (internal, plain text, no markdown or emojis):
"Scope decision: <Billable/Covered/Unclear>. Rule: <letter and short name, for example Step 1B new hardware install>. Moved to: <board>. Caveats: <missing info or none>."

Never tell the client a ticket is billable from this skill; quoting and approval follow your normal process. Never invent contract terms.

As a Flow: your entire reply is the note.
```
