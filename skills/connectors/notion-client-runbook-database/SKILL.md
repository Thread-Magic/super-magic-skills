---
name: Notion Client Runbook Database
description: Create and maintain a Notion client-runbooks database, one entry per client per system, updating entries when tickets reveal environment changes.
category: Connectors
tools: [search_tickets, search_clients]
connectors: [Notion]
scope: both
flow: no
role: [Service & Ops Manager, Technician]
outcome: [Time & Cost Savings (Capacity), Always-On Coverage]
---

# Notion Client Runbook Database

**When to use:** "Create a Notion database for our client runbooks," or "ticket <number> shows <client> migrated their file server — update their runbook."

**Run it:** across the whole runbooks database at setup · or on one ticket when it reveals a changed fact.

## Prompt

```
Stand up (once) and keep current a structured client-runbooks database in Notion:
environment facts, key systems, procedures, and owners per client — sourced from ticket
evidence, not memory.

This needs the member's connected Notion. If Notion isn't connected, tell the member to connect
it in settings and degrade by outputting the entry content and schema for manual entry — do not
stop.

1. Locate or create. Search Notion for an existing client-runbooks database; only if none exists,
   propose creating a Notion database with properties: Client, System/Area, Owner, Last verified
   (date), Status, Category — confirm schema and teamspace before creating. One database is the
   goal; a second runbooks database is a bug. Extend an existing schema only with confirmation.
2. Populate an entry. For a given client (confirm canonical naming), draft one page per
   system/area with facts each traceable to a source ("from ticket <number>", "confirmed by
   <member role>"). Facts require a source — "probably" facts are recorded as "Unverified —
   <source>" or left out. No credentials in entries; reference the credential vault entry name.
3. Update on change. When a ticket reveals a changed environment fact: find the affected entry in
   Notion, read its current content, show me a before/after diff of the specific fact, and only on
   confirmation update the Notion page — updating the fact, the Last verified date, and a one-line
   change note with the source ticket reference. Never overwrite a fact without showing the diff;
   a wrong runbook is worse than a stale one because it's trusted.
4. Report what was created or changed, with page links. Keep end-user personal data out of entries.
```
