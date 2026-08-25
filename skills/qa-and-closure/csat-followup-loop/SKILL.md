---
name: CSAT Follow-Up Loop
description: Close the CSAT loop after ticket closure: confirm the survey went out, pull the response into the ticket as a note, and flag detractors to a lead.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, search_members]
connectors: [Zapier: Typeform, Zapier: Microsoft Teams, Zapier: Outlook]
scope: global
flow: no
role: [Service & Ops Manager, CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# CSAT Follow-Up Loop

**When to use:** "Did the CSAT go out on this ticket?" / "send the satisfaction survey for these closures", pulling survey responses back onto their tickets, "any detractors this week?", or the delivery step after Ticket QA Review passes a ticket to close.

**Run it:** across all recently closed tickets — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
CSAT dies in two places: the survey never goes out, or the response never reaches anyone who acts
on it. Close both gaps — verify the ask, record the answer on the ticket, and make sure a bad
score becomes a same-day conversation instead of a quarterly statistic.

1. Retrieve the closed ticket(s) and check whether a CSAT ask already exists: the desk's native
   CSAT survey fires on close where configured (verify the closure used the triggering status),
   or a survey link was in the client-facing closure message. Never send a second ask when one is
   on record — one ask per closure, ever.

2. If no ask went out and the desk uses the native survey: recommend re-driving the close through
   the triggering status (with confirmation), so the platform sends its survey.

3. If the desk runs its survey on a form tool instead: draft the short client-facing CSAT message
   (thanks, one-line recap, the survey link with the ticket reference). Where the member has
   connected Zapier, the Typeform "Create Form" variants manage the form, and delivery goes by
   client-facing note (or Outlook "Send Email"). Present the draft for approval before anything is
   sent.

4. Pull responses back: check the thread for a native survey result note; for form-based desks,
   use Typeform "Find Response" filtered by the ticket reference. Match responses to tickets only
   on an explicit reference (ticket number, hidden field, or the respondent's email on that
   ticket) — never by timing coincidence.

5. Record each response on its ticket as an internal plain-text note: score, verbatim comment
   (quoted exactly, never paraphrased into something nicer), response date, and source (native
   survey / form).

6. Flag detractors (bottom-tier score or negative comment): identify the lead or account owner and
   surface a same-day alert — an internal @mention note on the ticket, and where the desk prefers,
   a Teams "Send Channel Message" to the service channel. Include score, comment, client, tech, and
   the ticket reference. Do NOT draft an apology to the client unattended — the detractor
   conversation is a human's.

7. Output: per-ticket status table (ask sent / response recorded / no response yet / detractor
   flagged) and the response rate for the batch.

Match responses to tickets on explicit references only — a mismatched detractor note on the wrong
client's ticket is a serious error. Detractor handling is escalation, not automation: no automated
client-facing damage control, no auto-reopening. Scores and comments are never fabricated or
estimated for tickets without a response. Zapier steps require the member to have connected the
Zapier MCP; without it, use the native survey path and client-facing notes, and note the
limitation. Notes are plain text, no markdown/emojis; survey messages stay short, friendly, and
localizable.
```
