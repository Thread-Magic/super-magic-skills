---
name: Zapier OneDrive User Files
description: Work a user's OneDrive during troubleshooting and data-recovery tickets — fetch the specific file in question, run KQL search to locate "lost" documents, and mint sharing links with hygiene. Use for "the user says the file is gone", "find <document> in their OneDrive", or "get me a safe link to that file".
category: Connectors
tools: [search_tickets, search_contacts, add_ticket_note]
connectors: [Zapier: OneDrive]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Zapier OneDrive User Files

**When to use:** "<user> says the Q3 proposal vanished — find it," "pull the file that won't open so we can check it," or "send <user> a link to the recovered file."

**Run it:** on one ticket.

## Prompt

```
"My file disappeared" is a top-ten ticket, and the answer is usually findable: locate the document
with a OneDrive KQL search, fetch the specific file the ticket is about, and when something must be
shared, create the narrowest link that works. Touch exactly the files the ticket names — a user's
OneDrive is their working life, not a browsing ground.

This runs only if the member has connected Zapier with a Microsoft account whose permissions actually
reach the user's OneDrive (often via admin/delegated access). If the connected account can't see the
drive, say so rather than concluding the file doesn't exist. If Zapier is absent, degrade by giving
the user self-serve search/recycle-bin steps — do not stop. Each Zapier call = 2 Zapier tasks — one
well-formed KQL search beats five vague ones.

1. Anchor to the ticket: the exact file name/description, the user, and why access is needed. No
   ticket-relevant reason, no file access — every access is ticket-justified and noted.
2. Locating ("it's gone"): run a KQL search scoped to the user's drive — filename fragments,
   filetype:, modified-date ranges. Files are usually misplaced, renamed, or auto-saved elsewhere.
   Report candidates as name + path + modified date only — enough for the user to say "that's it"
   without the desk reading anything.
3. Not found in scope → report the searched terms and scope honestly and hand off to the tenant's
   recovery process (recycle bin, retention/restore). This skill searches; it doesn't promise
   restoration, and never concludes "the file never existed" or "it was deleted by <user>".
4. Fetching (troubleshooting): retrieve the named file only when inspecting it is the ticket's actual
   task (corrupt file, version check). Content beyond the ticket's need stays unread and unquoted.
5. Sharing-link hygiene: narrowest scope that works — specific-people link over org-wide, org-wide
   over anyone-with-link; view unless editing is the purpose; expiration where the tenant supports it.
   "Anyone with the link" requires my explicit okay; never widen an existing link's scope to save a
   step.
6. Leave a note (plain text): what was searched/accessed, what was found (name/path, not contents),
   any link created and its scope/audience. The access trail is part of the deliverable.
```
