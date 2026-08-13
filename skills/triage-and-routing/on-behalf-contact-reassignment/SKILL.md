---
name: Reassign Contact Submitted On Behalf Of
description: Catch tickets one person opened for a colleague ("submitting this on behalf of Jane") and move the ticket's contact to the person the request is actually for — so it's attributed, notified, and reported against the right end user.
category: Triage & Routing
tools: [search_tickets, search_contacts, assign_contact, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise]
---

# Reassign Contact Submitted On Behalf Of

**When to use:** An office manager or team lead opens tickets for other staff; a ticket says "I'm submitting this for Jane" or "my colleague can't log in"; or a sweep to fix attribution so the real end user gets the updates and the reporting is right.

**Run it:** on one ticket · across recent tickets on a board · or as a Flow (when a ticket is created).

## Prompt

```
Detect when a ticket was opened by one person on behalf of a different colleague at the same
company, and move the ticket's contact to the person the request is actually for. If there's no
clear proxy submission, do nothing.

1. Read the ticket title and description. Look for explicit language that the submitter is acting
   for someone else, for example: "submitting this on behalf of <name>", "opening this for
   <name>", "this is for <name>, not me", "my colleague <name> is having an issue", "<name> asked
   me to submit this", "please help <name> with...".

   The intent must be explicit. A passing mention of another person ("I talked to <name> in
   accounting") is NOT a proxy submission. If nothing clearly indicates the ticket is for someone
   else, stop and make no change — do not touch the ticket.

2. When a proxy submission is clear, pull out the intended user: their name, and their email if the
   ticket gives one. This is the person the ticket should belong to.

3. Find that person as a contact at the SAME company the ticket is already on — search contacts
   scoped to the ticket's current company. Never move the ticket to a different company; this skill
   only changes the contact within the one company.
   - Confident match (email matches, or a full-name match within this company) → use it.
   - No confident match, or only a weak/partial name match → do not reassign. Leave a plain-text
     internal note naming the intended user and that a matching contact couldn't be found for a
     human to handle. Never attach to a lookalike.
   - If the intended user and the current submitter resolve to the same person, do nothing.

4. Reassign the ticket's contact to the intended user. Keep the original submitter visible in your
   note so the thread history stays clear — the submitter often still needs to be kept in the loop.

5. Leave a plain-text internal note: who opened it, who it's actually for, the exact phrase that
   signalled the proxy submission, and that the contact was moved. Notes bound for the PSA are
   plain text — no markdown, no emojis.

Only act on a clear, explicit proxy submission. When in doubt, do nothing and leave the ticket as
it is. Do not invent contacts or email addresses.

Running as a Flow: act only on an explicit on-behalf phrase with a confident contact match at the
same company; on anything weaker, make no change and leave one plain-text internal note. Your
entire reply is the internal note — no narration, no questions. One reassignment per ticket per
run; if the ticket already carries this skill's note, stop.
```
