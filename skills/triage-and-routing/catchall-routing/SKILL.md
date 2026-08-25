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
Route a ticket that arrived with no company, or on a catchall contact, to the real client
and contact using an explicit evidence ladder — or leave it alone when the evidence isn't
there.

1. Read the ticket: title, description, earliest message, and the full headers and quoted
   text if present.

2. Spam pre-check. Clearly unsolicited marketing or automated junk, with no
   client-identifying content and no sign a human forwarded it in for a reason: stop and
   flag it as spam for review rather than routing it. Never close spam unattended.

3. Extract identity clues, strongest first — this is the ladder everything below depends on:
   (a) the true sender's email domain, (b) a company name stated explicitly in the body or
   alert fields, (c) a person's name alone, which is never sufficient by itself.

4. On a forward — "FW:" subject, or a quoted original — parse the original "From:" line and
   use that sender as the identity source, not the forwarder.

5. On a vendor or monitoring alert, take the structured fields (site, organization, device,
   tenant) from the alert body as the company clue.

6. Resolve the company by searching clients on the domain or extracted name, then find the
   contact scoped to that company. No contact record for the sender: propose the closest
   match or say one needs creating — never attach to a lookalike.

7. If this tenant needs the wrong assignment cleared before a correct one applies, unassign
   back to catchall first, then set the right company and contact.

8. Set company and contact ONLY when exactly one candidate fits at domain or
   explicit-name strength. Two or more plausible companies: change nothing, list the
   candidates, ask. Never assign on name similarity alone.

9. If the tenant's PSA sync rejects company changes on an existing ticket, the fallback is
   close-and-recreate: a new ticket under the correct company with the original text and a
   note cross-referencing both numbers, then close the original. Destructive-adjacent — my
   confirmation only, never unattended.

10. Note what you matched, which rung of the ladder you used, and what changed (apply the
    PSA Note Discipline base skill).

A PSA-bound ticket must always have a company: if no match is possible, route to the desk's
designated catchall client and flag it rather than leaving it companyless. Don't invent
companies, contacts or ticket numbers, and say so if a search may have capped.

As a Flow: act only at domain or explicit-company strength. Anything weaker, change nothing
and leave one note: "CATCHALL ROUTING: no confident match. Evidence found: <clues>. Left
unassigned for human review." Never close-and-recreate unattended. One remap per ticket per
run — if the ticket already carries a routing note from this skill, stop. Your entire reply
is the note.
```
