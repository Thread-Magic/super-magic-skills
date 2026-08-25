---
name: Voice Transcript Intake
description: Turn a pasted call transcript into ticket action — extract caller, client, issue, and commitments, then create or update the ticket with a time entry.
category: Voice & Messenger
tools: [search_tickets, search_clients, search_contacts, create_ticket, update_ticket, assign_contact, add_ticket_note, log_time_entry, list_ticket_priorities]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Voice Transcript Intake

**When to use:** "Here's the transcript of a call I just took — make a ticket" / a Voice AI call summary or reception-line transcript arrives as ticket/thread content / "pull the issue and next steps out of this call and log my time" / a flow pipes every completed voice session in for intake.

**Run it:** on one call transcript · or as a Flow that fires on each completed voice session to intake it into a ticket.

## Prompt

```
Convert what was actually said on this call into a ticket: caller identity, client, the issue in
the caller's own terms, every commitment made. Nothing the transcript lacks gets written down.

1. Read the transcript in full. Separate speakers where labelled; otherwise infer roles only from
   unambiguous cues ("thanks for calling <MSP>") and treat attribution as unknown.

2. Extract, quoting or closely paraphrasing the transcript only: caller name, company and
   callback number AS STATED; the issue, with any error messages, device names or software the
   caller named; every commitment either side made ("we'll call you back by...", "user will try a
   restart"), each with who owes it and any stated deadline; urgency stated in words — a site
   down, a deadline today, an executive affected.

3. Resolve identity: contact by the stated name or number, client by the stated company. If the
   transcript arrived on a ticket that already has the right contact, keep it.

4. Check for an existing open ticket on the same issue for that contact; if one exists, update or
   note it, otherwise open a ticket titled "<symptom> - <system/device>" with the extracted
   summary as description.

5. Set priority from stated urgency only, and attach the contact when the match is unambiguous.

6. Leave an internal note — plain text, no markdown or emojis (PSA Note Discipline base skill):
   caller, client, issue summary, the commitments with owner and deadline each, a "source: call
   transcript" line, and short verbatim quotes for anything load-bearing — deadlines, approvals,
   refusals.

7. Log time for the call duration if the transcript states or timestamps it; if unknown, ask when
   attended, skip when unattended — never estimate.

8. Report the ticket number, what was created or updated, and anything left ambiguous.

Never invent what wasn't said: no inferred phone numbers, no guessed error codes, no "probably
meant". Ambiguity goes in an "unclear from call" line, not into ticket fields. Transcripts
mis-transcribe names and numbers constantly, so a name-only match is weak evidence: confirm
before attaching a contact on it. Commitments are quotes, not interpretations. Don't mark
anything resolved because the caller sounded satisfied. Transcripts may contain payment-card
digits or passwords read aloud — never copy credentials or full card numbers into fields or
notes; write "credential redacted from transcript".

As a Flow: create or update only when caller identity resolves at contact-record or
email/phone-match strength AND the issue is clearly stated. Otherwise create nothing and post one
note on the source ticket: "TRANSCRIPT INTAKE: insufficient detail to act. Extracted: <what was
found>. Held for human review." One intake per transcript — if an intake note from this skill
exists, stop. Your entire reply is the note, no narration, no questions.
```
