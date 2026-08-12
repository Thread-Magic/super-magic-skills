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
Route a ticket that arrived with no company (or on a catchall contact) to the real
client and contact using an explicit evidence ladder — or leave it alone when the
evidence isn't there.

1. Read the ticket: title, description, earliest message, and full headers/quoted text if
   present.

2. Spam pre-check: if the message is clearly unsolicited marketing or automated junk with
   no client-identifying content and no sign a human forwarded it in for a reason, stop
   and flag it as spam for review instead of routing it. Do not close spam unattended —
   flag with a note only.

3. Extract identity clues in this order of strength (the evidence ladder):
   a. Email domain of the true sender (strongest),
   b. An explicit company name stated in the body or alert fields,
   c. A person's name alone (weakest — never sufficient by itself).

4. If the subject starts with "FW:" or the body contains a quoted original message, parse
   the original "From:" line and use that sender — not the forwarder — as the identity
   source.

5. If the ticket is a vendor/monitoring alert, extract the structured fields (site name,
   organization, device, tenant) from the alert body and use those as the company clue.

6. Resolve the company by searching clients on the domain or extracted name; then find the
   contact by searching contacts scoped to that company. If the sender has no contact
   record, propose the closest match or note that one needs creating — never attach to a
   lookalike.

7. If the current wrong assignment must be cleared before the correct one can apply on
   this tenant, unassign first (set back to no-company/catchall), then set the correct
   company and contact.

8. Set the company and contact ONLY when exactly one company candidate fits at domain or
   explicit-name strength. Ambiguity (two or more plausible companies) → make no change;
   list candidates and ask. Never assign on name similarity alone.

9. If the tenant's PSA sync rejects company changes on an existing ticket, use the
   close-and-recreate path: open a new ticket under the correct company with the original
   text and a plain-text note cross-referencing both ticket numbers, then close the
   original — but only with my confirmation (this is destructive-adjacent), never
   unattended.

10. Leave a plain-text internal note stating what was matched, which evidence rung was
    used, and what changed.

A PSA-bound ticket must always have a company — if no match is possible, route it to the
designated internal/catchall client per desk policy and flag it; never leave it
companyless. Notes destined for the PSA are plain text — no markdown, no emojis. Do not
invent companies, contacts, or ticket numbers; if searches may have capped, say so.

Running as a Flow: act only at domain-match or explicit-company strength; on anything
weaker, make no change and leave one plain-text internal note: "CATCHALL ROUTING: no
confident match. Evidence found: <clues>. Left unassigned for human review." Never use
close-and-recreate unattended. One remap per ticket per run; if the ticket already
carries a routing note from this skill, stop. Your entire reply is the internal note —
no narration, no questions.
```
