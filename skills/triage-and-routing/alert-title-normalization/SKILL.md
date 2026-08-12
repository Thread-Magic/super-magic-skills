---
name: Alert Title Normalization
description: Classify a monitoring or security alert ticket and rewrite its title into the desk's standard format using a controlled vocabulary, with an internal note.
category: Triage & Routing
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Alert Title Normalization

**When to use:** Alert tickets arrive with cryptic or verbose tool-generated subjects — "normalize these alert titles" during a queue cleanup, or a flow on the alert board that should rewrite every new title to the house standard.

**Run it:** on one alert ticket · across all alert tickets on a board · or as a Flow (when a new alert ticket is created).

## Prompt

```
Turn a raw tool-generated alert title into a standard, scannable one —
"<AlertClass> - <client> - <device or user> - <symptom>" — so the queue reads
consistently regardless of which tool raised the alert.

1. Read the ticket: current title, description, and the raw alert body.

2. Classify the alert into one class from the controlled vocabulary configured for this
   desk (e.g. Backup Failure, Disk Space, Offline Device, AV/EDR Detection, Patch
   Failure, Certificate Expiry, Login/Identity, Other). Pick exactly one; use Other only
   when nothing else fits. Do not coin new classes mid-run.

3. Extract the concrete subjects from the alert fields: client, device or user, and the
   specific symptom (error, threshold, service name). Take them from the alert body,
   never from guesswork.

4. Compose the new title in the standard format with the controlled-vocabulary class
   first. Keep it under ~90 characters; drop tool boilerplate, IDs already tracked
   elsewhere, and repeated timestamps. Never remove information that exists only in the
   title (unique error codes, hostnames) — move it into the note if it doesn't fit.

5. If the alert body doesn't identify a client or device, do not fabricate placeholders
   in the title — keep the original title and note why.

6. Apply the new title and leave a plain-text internal note: old title, new title, alert
   class chosen.

The title and the internal note are the only changes — no status, priority, board, or
owner changes. Notes are plain text — no markdown or emojis.

Running as a Flow: your entire reply is the internal note, posted verbatim: "TITLE
NORMALIZED. Old: <old>. New: <new>. Class: <class>." or "TITLE UNCHANGED. Reason: <one
line>." One title rewrite per ticket, ever: if the current title already matches the
standard format, stop without writing. When classification is uncertain between two
classes, do nothing.
```
