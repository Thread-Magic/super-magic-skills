---
name: Voicemail to Ticket
description: Convert a voicemail transcription into a ticket with a callback commitment — urgency read from what the caller actually said, not from tone guesses.
category: Voice & Messenger
tools: [search_contacts, search_clients, search_tickets, create_ticket, update_ticket, assign_contact, add_ticket_note, list_ticket_priorities]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Always-On Coverage]
---

# Voicemail to Ticket

**When to use:** a voicemail transcription arrives on the intake board or is pasted into chat / "left on the after-hours line: <transcription> — make a ticket" / a flow routes every voicemail-sourced ticket through structuring.

**Run it:** on one voicemail · or as a Flow that fires on each voicemail-sourced ticket to structure it and record the callback.

## Prompt

```
Turn this voicemail transcription into an actionable ticket: who called, what they need,
what number to call back, and a callback owed — with urgency set only from the words in the
message.

1. Read the full transcription. Extract only what is present: caller name, company,
   callback number as spoken, the request, and any stated time constraint ("before we open
   at 8", "I'm leaving at noon").

2. Transcribed phone numbers are error-prone: keep the number exactly as transcribed and
   flag it as unverified if it doesn't match the contact record found in step 3.

3. Resolve identity: look up the contact by stated name/number and the client by stated
   company. Check for an open ticket this voicemail continues ("calling about my ticket from
   yesterday") — update that ticket instead of creating a duplicate.

4. Set urgency from CONTENT only:
   - Stated business stoppage, safety issue, security concern, or "everyone is down" →
     high.
   - Stated deadline today → elevated.
   - Everything else → the desk's default intake priority.
   Never raise priority because the caller "sounded" angry or stressed — transcripts carry
   no reliable tone, and guessing writes fiction into the queue.

5. Open a ticket (or update the existing one): title "<request/symptom> — voicemail from
   <caller>", description = cleaned transcription plus extracted fields. Attach the contact
   only on an unambiguous match.

6. Record the callback commitment in a plain-text note: number to call, best-by time if the
   caller stated one, otherwise the desk's standard callback SLA. Keep the format
   consistent: "CALLBACK OWED: <number> by <time/SLA>".

7. Output: ticket number, priority + the stated words that justified it, callback line, and
   any unverified fields.

Guardrails: urgency evidence must be quotable — if you cannot point at the words that make
it urgent, it is not urgent. Never invent a callback number; if none was left and no contact
record supplies one, say so on the ticket (that changes the callback plan to email). Garbled
or partial transcriptions: capture what exists, mark gaps as "[inaudible in transcription]",
do not fill them. Voicemails sometimes contain credentials or card numbers read aloud —
redact them from fields and notes. Plain-text notes only for PSA-synced tickets.

Running unattended (Flows): create a ticket only when there is a resolvable client
(contact/company match, or the source line is dedicated to one client). Unresolvable → post
one plain-text note on the source: "VOICEMAIL INTAKE: caller/client unresolved. Heard:
<extracted fields>. Held for human review." and stop. Priority above default requires a
quoted urgency phrase in the note. Never mark the callback as made — this skill records the
debt, it does not pay it. One ticket per voicemail; if an intake note from this skill exists,
stop. Your entire reply is posted verbatim as the internal note — no narration.
```
