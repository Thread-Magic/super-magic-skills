---
name: Notion Intake Forms
description: Build a Notion form view for structured requests (new hires, access, project intake) and convert submitted rows into tickets without another vendor.
category: Connectors
tools: [create_ticket, search_clients, search_contacts]
connectors: [Notion]
scope: global
flow: no
role: [Dispatcher, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Notion Intake Forms

**When to use:** "We keep getting half-complete new-hire requests — build an intake form," or "process this week's form submissions into tickets."

**Run it:** across all unprocessed form submissions (run manually to build the form, then to process the batch).

## Prompt

```
Two halves of one loop: a Notion form view that captures a request with every field the desk
needs up front, and a processing pass that turns submitted rows into correctly-populated
tickets — exactly once each.

This needs the member's connected Notion. If Notion isn't connected, degrade by designing the
schema + form fields as a spec the member builds by hand, and note tickets must then be created
manually — do not stop.

Building the form (one-time):
1. Search Notion for an existing intake database for this request type; extend rather than duplicate.
2. Design the schema from what the desk needs to act without a follow-up question — e.g. new hire:
   name, start date, manager, role/template user, applications, hardware, client/site. Add two
   processing properties: Processed (checkbox) and Ticket ref (text).
3. Confirm schema + teamspace, then create the Notion database and a form-type view. Share the
   form link with the member to distribute.

Processing submissions (repeatable):
4. Query the database for rows where Processed is false.
5. For each row: validate required fields (incomplete → skip and list it for human follow-up,
   never guess missing data); resolve the client and the requester; draft the ticket (standard
   title format, description carrying every form field, correct board).
6. Show me the batch of draft tickets and wait for confirmation, then create each ticket and
   write back Processed = true and the ticket number to the row. The Processed flag is the
   dedupe mechanism — never create a ticket from a row without setting it, and never process a
   row that already has it; double tickets erode trust in the whole loop.
7. Report: created tickets with numbers, skipped rows with reasons.
```
