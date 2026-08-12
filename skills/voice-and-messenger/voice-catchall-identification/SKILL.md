---
name: Voice Catchall Identification
description: Identify the client and contact behind an unknown caller — a voice ticket carrying only a phone number — using number, spoken-name, and company clues from the transcript. Use when a voice-sourced ticket has no company or sits on the catchall contact.
category: Voice & Messenger
tools: [search_tickets, search_contacts, search_clients, assign_contact, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Voice Catchall Identification

**When to use:** a voice or voicemail ticket has no company assigned or landed on the catchall/no-company contact / "who is this caller? All we have is the number and the transcript" / a periodic sweep of the voice intake board for unidentified-caller tickets.

**Run it:** on one unidentified voice ticket · or as a Flow that fires on each voice ticket landing without a company, to attempt identification.

## Prompt

```
Match an unknown caller (a voice ticket carrying only a phone number) to a real contact and
client using the transcript's identity clues — or leave the ticket alone and say why.

1. Read the ticket: transcript, caller number, and any Voice AI recap fields.

2. Extract identity clues from the transcript, ranked by strength:
   a. Caller number matches a contact record (strongest) — look up the contact by number.
   b. Explicit company name spoken ("I'm calling from <company>") — look up the client by it.
   c. Contextual identifiers spoken — a site, a named coworker who IS on record, a ticket
      number they reference ("calling about my ticket") that resolves to a client.
   d. A spoken personal name alone (weakest — never sufficient by itself; transcription
      mangles names).

3. Cross-check clues: a number match plus a spoken name that matches that contact record is
   a confident match. A number match to contact A while the caller states they are person B
   at the same client → attach the client, flag the contact ("shared line / front desk?")
   rather than forcing A.

4. Transcription fuzziness: try phonetic and near-spelling variants when searching spoken
   names/companies ("Kaufman/Coffman"), but a fuzzy hit alone stays at name-alone strength.

5. Attach the contact and update the ticket only when exactly one client fits at number-match
   or spoken-company strength (or two clues corroborate). Two or more plausible clients → no
   change; list candidates.

6. If the caller has no contact record but the client is confident, attach the client and
   note that a contact may need creating with the number and spoken name — do not attach a
   lookalike contact.

7. Leave a plain-text note: which evidence rung matched, what changed, and any unverified
   fields.

Guardrails: a spoken name alone is never enough — transcripts mis-hear names, and MSPs have
duplicate names across clients. Never treat the caller's self-identification as verified
identity for anything sensitive: this skill routes tickets, it does not authorize resets or
grant access. Shared/main-line numbers match many callers; a number match on a company main
line identifies the client, not the person. Ambiguity → no change; a wrongly-attributed
ticket is worse than an unassigned one. If the tenant's PSA requires a company, follow desk
policy for the designated catchall client rather than leaving it companyless. Plain-text
notes; do not invent contacts, companies, or numbers.

Running unattended (Flows): act only on a number-to-contact match, a spoken company name
resolving to exactly one client, or two corroborating clues. Anything weaker → no change,
post: "VOICE ID: no confident match. Number: <number>. Heard: <clues>. Left for human
review." Never create contacts unattended; note the need instead. One identification pass
per ticket; if this skill's note already exists, stop. Your entire reply is posted verbatim
as the internal note — no narration, no questions.
```
