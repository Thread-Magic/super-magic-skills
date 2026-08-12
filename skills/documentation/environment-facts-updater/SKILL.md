---
name: Environment Facts Updater
description: When a ticket reveals a client environment fact changed — new server, ISP, VPN, key contact — draft the corresponding documentation update for the client's doc platform.
category: Documentation
tools: [search_tickets, search_itglue, search_hudu, notion-search, notion-fetch, notion-update-page, add_ticket_note]
connectors: [IT Glue, Hudu, Notion]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Environment Facts Updater

**When to use:** A ticket mentions a new server, replaced firewall, changed ISP, new VPN endpoint, or moved office; "update the docs — <client> switched providers"; post-project cleanup; or a mismatch that stale-doc-hygiene flagged is now resolved.

**Run it:** on one ticket.

## Prompt

```
Catch the environment changes that surface mid-ticket and turn each into a precise,
ready-to-apply doc update so documentation keeps matching reality.

1. Read the ticket thread and extract each CONFIRMED environment fact change: what
   changed, old value -> new value, effective date, and the evidence line in the
   thread. A plan or recommendation is not a change — zero-assumption applies; never
   promote "we plan to switch ISPs" into a documented change.

2. Locate the affected documentation: check IT Glue / Hudu where connected, and search
   Notion if the member's docs live there. Note every doc that references the old value.

3. Draft the update per doc, in a paste-ready block (one fact per block — bundled
   edits hide mistakes):
   - Doc title + location
   - Section/field affected
   - Old value -> new value
   - Source: ticket number and date

4. Apply the update only where a writable path exists AND the requester confirms:
   Notion pages can be updated directly. IT Glue and Hudu are SEARCH-ONLY from here —
   for those, output the paste-ready block and flag it as a manual update for the
   tech. Confirm before any write: show the exact old -> new diff and get a yes. When
   in doubt, output the draft and do nothing.

5. Never write credentials into documentation drafts; if a change involves new
   credentials, note "credentials updated — store in credential vault" without the
   values.

6. Leave a plain-text internal note on the ticket (on request) recording which docs
   were updated or queued for manual update, so the change ticket carries its
   documentation trail. With no doc platform reachable, output paste-ready drafts only
   and say which platforms were not checked.
```
