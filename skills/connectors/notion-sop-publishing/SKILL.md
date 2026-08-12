---
name: Notion SOP Publishing
description: Turn a resolved ticket into an SOP page in the team's Notion runbooks teamspace, tagged by client, product, and category, with link back to ticket.
category: Connectors
tools: [search_tickets, add_ticket_note]
connectors: [Notion]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Notion SOP Publishing

**When to use:** "That was painful — write it up as an SOP so we never rediscover it," or "publish the resolution from ticket <number> to our Notion runbooks."

**Run it:** on one resolved ticket.

## Prompt

```
Publish a resolved ticket as a structured SOP in the team's Notion runbooks teamspace.

This needs the member's connected Notion. If Notion isn't connected, say so, tell them to connect
Notion in settings, and degrade by outputting the finished SOP text for manual paste — do not stop.

1. Read the full ticket thread (include messages and internal notes) and extract: symptom as the
   user reported it, environment (application, OS/version, relevant config), the diagnostic path,
   the fix that worked, and what was tried that did NOT work.
2. Search the runbooks teamspace in Notion for an existing SOP on the same issue. If one exists,
   propose updating it rather than creating a duplicate — search-before-create is mandatory;
   duplicate SOPs are how runbook trust dies.
3. Draft the SOP: title as "<Product> — <symptom>: <fix summary>"; sections for Symptoms,
   Environment, Resolution steps (numbered, imperative), What didn't work, Source ticket ref.
   Sanitize as you draft: no passwords, license keys, or shared secrets — reference the
   credential vault entry name instead ("credentials in the documentation vault under
   <entry>"); replace end-user personal details with <user>. Document only what the ticket
   evidence shows worked — never pad with plausible extra steps or invented KB links.
4. Show me the draft and the target teamspace/database, and wait for confirmation before writing.
5. On confirmation: create the Notion page in the runbooks location, setting the client, product,
   and category tags/properties the database defines. Confirm the target teamspace on first use
   and reuse it thereafter — never scatter SOPs into private pages.
6. Leave an internal note (plain text): "SOP published: <page title> — <link>".
```
