---
name: Zapier SharePoint Ticket Filing
description: File ticket artifacts — reports, PIRs, signed docs, exports — into the client's SharePoint library with correct foldering and sharing-link hygiene (expiry, least privilege). Use for "put this in the client's SharePoint", "file the incident report to their site", or "share this document with the client safely".
category: Connectors
tools: [search_tickets, add_ticket_note]
connectors: [Zapier: SharePoint]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Time & Cost Savings (Capacity)]
---

# Zapier SharePoint Ticket Filing

**When to use:** "File the post-incident report to <client>'s SharePoint," or "upload the signed change authorization to their site and link it on the ticket."

**Run it:** on one ticket.

## Prompt

```
Ticket-born documents deserve a permanent, findable home: upload artifacts to the right client's
SharePoint library, in the agreed folder structure, and share them with links that expire instead
of links that leak.

This runs only if the member has connected Zapier with a Microsoft account that has rights to the
client's site. If it's absent, degrade by preparing the document + a filing instruction note for the
member to upload manually — do not stop. Each Zapier call = 2 Zapier tasks; a normal filing is 2–3
calls (find, upload, share).

1. Identify the artifact and its client. Resolve the destination: locate the client's library and
   target folder. On first use for a client, confirm the mapping with me and follow the tenant's
   folder convention (e.g. /Documentation/<year>/) rather than inventing one. Cross-tenant filing is
   the catastrophic failure — verify the site belongs to the artifact's client before upload; never
   resolve a site by name similarity between clients.
2. Name the file to the desk's convention: date-prefixed, client and subject in the name, no internal
   shorthand ("2026-07-15 <Client> Post-Incident Report — <system>").
3. Confirm destination + filename, then upload the file (replace an existing file only when the
   member explicitly wants a new version — replacing destroys the previous version for viewers).
4. Sharing-link hygiene, when a link is needed: scope to specific people or the client's existing site
   access — no "anyone with the link" unless the member explicitly overrides; set an expiry on
   external links (default 30 days, shorter for sensitive material); view-only unless editing is the
   point. When a temporary broad share was used, schedule the removal of that sharing permission after
   the window. No credentials or secret values inside filed shareable copies.
5. Leave a note (plain text): what was filed, where (site/folder/filename), the link if created,
   and its expiry. A link nobody remembers issuing is a standing exposure. For recurring/unattended
   filing, use a curated Zapier server with the site/library field locked per workflow.
```
