---
name: Catchall Routing
description: Identify the correct client and contact for a ticket that landed in a catchall or no-company mailbox, including forwarded mail and vendor alert routing.
category: Triage & Routing
tools: [search_tickets, search_clients, search_contacts, assign_contact, update_ticket, add_ticket_note, create_ticket]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Catchall Routing

**When to use:** A ticket has no company assigned or sits on a catchall/no-company contact; forwarded mail ("FW:") is attributed to the forwarder not the original sender; a vendor/monitoring alert landed in the catchall; or a periodic sweep of the intake board to remap misattributed tickets.

**Run it:** on one ticket · across all catchall/no-company tickets · or as a Flow (when a ticket is created with no company).

## Prompt

```
Route a ticket that arrived with no company, or on a catchall contact, to its real client and
contact — on evidence, or not at all.

1. Read the whole ticket: the earliest message, headers, quoted text and internal notes. On a
   phone-sourced ticket, a post-call note often names the caller and their company outright —
   treat it as high-confidence identity.

2. Spam pre-check: unsolicited marketing or automated junk with no client-identifying content,
   and no sign a human forwarded it in for a reason, gets a spam flag and a note — never a close.

3. Rank identity clues by strength (the evidence ladder): the true sender's email domain,
   strongest; then an explicit company name in the body or alert fields; then a person's name
   alone, never sufficient. On "FW:" or a quoted original, parse the original "From:" line
   and use that sender, not the forwarder. On a vendor or monitoring alert, use its structured
   fields — site, organization, device, tenant — as the company clue.

4. Search clients on the domain or extracted name to resolve the company, then contacts scoped to
   it. Take the first that fits: a confident contact match (email, or a full name at that
   company); else, only once the company itself is confidently resolved, its admin/primary
   contact — or any basic contact there if it has no admin — noting that a fallback was used so a
   human can correct it; else a company with no contacts at all: note that and leave it for
   manual handling. Never attach a lookalike contact at another company.

5. Commit company and contact ONLY when exactly one candidate fits at domain or explicit-name
   strength — never on name similarity alone. Two or more plausible: change nothing, list them
   and ask. If this tenant needs the wrong assignment cleared first, unassign to no-company, then
   set the correct pair.

6. If the PSA sync rejects a company change on an existing ticket, close-and-recreate: a new
   ticket under the correct company with the original text and a note cross-referencing both
   numbers, then close the original — only with my confirmation, never unattended.

7. Note it: plain text, no markdown or emojis — what matched, which evidence rung, what changed.

A PSA-bound ticket must always have a company: with no match possible, route it to the desk's
designated internal/catchall client and flag it, never leave it companyless. Never invent
companies, contacts, or ticket numbers; say if a search may have capped.

As a Flow: act only at domain-match or explicit-company strength; on anything weaker change
nothing and leave one plain-text note: "CATCHALL ROUTING: no confident match. Evidence found:
<clues>. Left unassigned for human review." Never close-and-recreate unattended. If the ticket
already carries a routing note from this skill, stop — one remap per ticket. Your entire reply is
the note: no narration, no questions.
```
