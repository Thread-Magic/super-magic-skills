---
name: Voice Transcript Intake
description: Turn a pasted or piped call transcript into ticket action — extract caller, client, issue, and any commitments made, then create or update the ticket with a time entry. Use when a call transcript, Voice AI recap, or reception-line recording text lands in chat or on a ticket.
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
Convert what was actually said on this call into a ticket: caller identity, client, the
issue in the caller's own terms, and every commitment made. Nothing the transcript doesn't
contain gets written down.

1. Read the transcript in full. Separate speakers if labeled; if unlabeled, infer roles
   only from unambiguous cues ("thanks for calling <MSP>") and otherwise treat attribution
   as unknown.

2. Extract, quoting or closely paraphrasing the transcript only:
   a. Caller name, company, and callback number AS STATED on the call.
   b. The issue and any error messages, device names, or software the caller named.
   c. Every commitment either side made ("we'll call you back by...", "I'll email the
      form", "user will try a restart"), each with who owes it and any stated deadline.
   d. Urgency signals stated in words (down site, deadline today, executive affected).

3. Resolve identity: look up the contact by the stated name/number, and the client by the
   stated company. If the transcript arrived attached to a ticket that already has the
   right contact, keep it.

4. Check for an existing open ticket about the same issue for that contact. If one exists →
   update it / leave a note on it; otherwise → open a ticket with a title "<symptom> —
   <system/device>" and the extracted summary as description.

5. Set the priority mapped from stated urgency only; attach the contact when the match is
   unambiguous.

6. Leave a plain-text internal note: caller, client, issue summary, commitments list (owner
   + deadline each), and a "source: call transcript" line. Include short verbatim quotes
   for anything load-bearing (deadlines, approvals, refusals).

7. Log time for the call duration if the transcript states or timestamps it; if duration is
   unknown, ask (attended) or skip (unattended) — never estimate one.

8. Output: ticket number, what was created/updated, the commitments list, and anything the
   transcript left ambiguous.

Guardrails: never invent what wasn't said — no inferred phone numbers, no guessed error
codes, no "probably meant"; ambiguity goes in an "unclear from call" line, not into ticket
fields. Transcripts mis-transcribe names and numbers constantly — treat a name-only match
as weak evidence; confirm before attaching a contact on name alone. Commitments are quotes,
not interpretations. Do not mark anything resolved because the caller sounded satisfied.
Plain-text notes only for PSA-synced tickets. Transcripts may contain payment-card digits
or passwords read aloud — never copy credentials or full card numbers into fields or notes;
write "credential redacted from transcript".

Running unattended (Flows): create/update only when caller identity resolves at
contact-record or email/phone-match strength AND the issue is clearly stated. Otherwise
create nothing and post one plain-text note on the source ticket: "TRANSCRIPT INTAKE:
insufficient detail to act. Extracted: <what was found>. Held for human review." Never log
time unattended unless the duration is present in the transcript metadata. One intake per
transcript; if an intake note from this skill exists, stop. Your entire reply is posted
verbatim as the internal note — no narration, no questions.
```
