---
name: Project Conversion Inbox Cleanup
description: When a ticket is converted to a project or moved to a project board, set the attribute that removes it from live inbox and queue views so dispatch is tidy.
category: Automation & Flows
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Project Conversion Inbox Cleanup

**When to use:** Tickets converted to project work still appear in the front-line inbox/dispatch views; "when something becomes a project, get it out of our reactive queue"; a flow should tidy the inbox automatically on conversion. Fires on the BOARD-CHANGE or TYPE-CHANGE event — supported ticket events, not a timer.

**Run it:** on one ticket · or as a Flow (triggered when a ticket's board or type changes to project work).

## Prompt

```
A ticket that becomes project work shouldn't keep surfacing in the reactive queue. When a
ticket is converted to a project type/board, apply the desk's documented inbox-exclusion
attribute so project tickets live on the project board without polluting live dispatch views.

Your entire reply is the audit note, verbatim: either `PROJECT INBOX CLEANUP. Set
<attribute>. Removed from live views.` or `NO ACTION. Reason: <not project work | no
exclusion attribute configured>.`

1. Read the ticket and confirm the conversion actually happened: it is
   now a project type or sits on a project board. If it is not genuinely project work, stop —
   never pull an ordinary reactive ticket out of the inbox because it merely mentions a project.

2. Identify the desk's DOCUMENTED inbox-exclusion attribute — the specific field/value this
   desk uses to keep a ticket off live inbox/queue views (a queue/board reassignment, a view-
   scoping status, or a flag the desk's views filter on). This is configured alongside the
   skill. Do NOT invent the mechanism — if it isn't documented, stop and note that no
   exclusion attribute is configured rather than guessing at a field.

3. Apply that attribute to the ticket.

4. Leave a plain-text audit note: that the ticket was recognized as
   project work and which inbox-exclusion attribute was set.

The attribute change and audit note are the only writes — do not change status to something
that would hide the ticket from the project team too, and do not close it. One application
per conversion event. Notes plain text (PSA compatibility).
```
