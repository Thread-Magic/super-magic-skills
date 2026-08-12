---
name: IT Glue Asset & Contact Lookup
description: On demand, pull IT Glue contacts, credentials, and flex-asset configs into a plain-text ticket summary, degrading to KB or ticket history if unavailable.
category: Devices & Infrastructure
tools: [search_itglue, search_knowledge_base, search_tickets, add_ticket_note]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# IT Glue Asset & Contact Lookup

**When to use:** "Pull <client>'s IT Glue contacts for this ticket", "where are the credentials for <system>?", or "get the flex-asset config for <asset> and post it here".

**Run it:** on one ticket, member-invoked (not a Flow — credential-adjacent lookups stay human-initiated).

## Prompt

```
Pull the client-facing facts a tech needs mid-ticket — key contacts, where credentials live, the config of a documented asset — and drop a clean, plain-text summary with deep links onto the ticket.

1. Connection check first. This needs IT Glue enabled. If the documentation isn't reachable, say so and go to the degrade path (step 5) instead of implying a search happened.
2. Identify the client and what's being asked (contacts, credential locations, or a specific flex-asset/configuration). Search the documentation scoped to that client and asset type.
3. Assemble a plain-text summary suitable for a PSA-synced note (no markdown, no emojis):
   - Contacts — name, role, and how to reach them, for the key people only.
   - Credentials — the LABEL and DEEP LINK to the IT Glue password entry, never the secret value itself.
   - Configs / flex assets — the fields the ticket needs (make/model, IP, versions, notes) with a deep link to the full record.
4. Include the IT Glue deep link for each item so the tech can open the authoritative record in one click.
5. Degrade path: if IT Glue is absent or has nothing, fall back to the knowledge base, then prior tickets on the same client/asset that captured the facts. State clearly which source the info came from; if none has it, say so.
6. Preview the summary; on confirm, leave it as a note on the ticket. If the member only wanted to read it, skip the note.

Guardrails: never surface actual secrets — post the credential's label and deep link only; the value stays in IT Glue behind its own access control. Confirm before writing the note; posting waits on an explicit go-ahead. Cite real IT Glue deep links only; never fabricate a record, contact, or URL — if a field is missing, leave it out rather than inventing it. Verify freshness where the data shows a last-updated date, and flag anything stale. Member-invoked only; no unattended variant (credential-adjacent lookups stay human-initiated).
```
