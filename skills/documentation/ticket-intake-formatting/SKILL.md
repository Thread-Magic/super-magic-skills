---
name: Ticket Intake & Formatting
description: Build a clean ticket title and description from a raw report, voicemail, email, form submission, or rough technician notes, following the house intake standard.
category: Documentation
tools: [search_tickets, create_ticket, update_ticket, add_ticket_note, run_assistive_ai]
connectors: []
scope: single
flow: no
role: [Technician, Dispatcher]
outcome: [Time & Cost Savings (Capacity)]
---

# Ticket Intake & Formatting

**When to use:** "Create a ticket from this email / voicemail transcript / chat paste," a ticket arrived with a junk title ("help!!", "FW: FW: printer") that needs reformatting, or a web-form / vendor-alert submission needs its fields parsed into a description.

**Run it:** on one ticket.

## Prompt

```
Turn unstructured intake into a standardized title and description a dispatcher or
technician can act on immediately — restructured, not summarized away.

1. Read the raw source and extract: WHO (contact + <client>), WHAT (the symptom,
   verbatim where useful), WHEN (onset, recurrence), IMPACT (users/systems affected,
   urgency signals), and any error text.

2. Write the TITLE in the house convention. Default when the desk has not defined
   one: "<Client> - <System/Device> - <Symptom>". Keep it under ~80 characters,
   symptom-first, no "URGENT!!!" styling.

3. Write the DESCRIPTION as structured intake:
   - Reported by / affected user(s)
   - Symptom and exact error messages
   - Onset and frequency
   - Business impact
   - Environment facts stated in the source (<device>, OS, application)
   - Original source text preserved below a separator when it adds detail.
   Do NOT put troubleshooting steps in the description — suggested or attempted fixes
   belong in a separate internal note. The description records the problem, not the work.

4. Form-field parsing: if the source is a structured form or alert email, map each
   labeled field to the intake sections; keep unmapped fields verbatim in a "Raw
   fields" block rather than dropping them.

5. If a follow-up or callback date is requested, compute it weekend-adjusted: a
   follow-up landing on Saturday or Sunday moves to the next business day (respect
   stated desk holidays if known). State the adjusted date explicitly.

6. Restructure, do not summarize away specifics — exact error text, names, and
   timestamps survive intact. Never place troubleshooting content, credentials, or
   internal commentary in the client-visible description. If the desk runs a non-
   English working language, produce the title/description in that language.

7. Only create or modify a ticket AFTER confirming the extracted details are right;
   never guess the client/contact from name similarity — low confidence means ask,
   do not assign. Then create the ticket (or update it when reformatting) with the
   right board/status/priority; use the assistive AI for category/priority
   suggestions when requested. Post attempted-fix info, if any, as an internal note.
```
