---
name: Premature Confirmation Detector
description: Catch tickets closed on assumption without customer confirmation — work summaries treated as sign-off, closes minutes after last change — then reopen.
category: QA & Closure
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Premature Confirmation Detector

**When to use:** "Check today's closures for premature confirmations" / "did anyone close on assumption?" — focused follow-up after Reopen Forensics shows premature closure as the leading failure mode, verifying one closure a client complained about, or a narrow confirmation-only Flow gate on close.

**Run it:** on one ticket · across a window of closed tickets · or as a Flow (when a ticket is closed).

## Prompt

```
The single biggest reopen cause: closing because the tech believes it's fixed, not because the
customer said so. Hunt the telltale closure patterns, check the thread for actual confirmation,
and reopen the ones closed on hope.

1. Scope: one ticket, or a window of closed tickets (split per board, and say so if a search may
   have capped).

2. For each ticket, locate the confirmation evidence, if any. Valid confirmation is exactly one
   of: an inbound client-visible message after the fix confirming the issue is resolved; OR a tech
   note documenting a verbal confirmation — who confirmed, when, and how ("spoke with <user> at
   <time>, confirmed login working").

3. Flag the premature-closure tells when no valid confirmation exists:
   - Closure note says "should be fine / should be working / believe this is resolved."
   - The last thread event before close is the tech's own work summary — work performed is not
     outcome confirmed.
   - Closed within minutes of the last change with no client interaction in between.
   - The client's last actual message reports the problem still occurring, unaddressed.
   - Dismissive client reply ("fine", "whatever") treated as confirmation — it isn't; it's a
     sentiment flag.

4. Verdict per ticket: CONFIRMED (valid evidence, cite the note/message and date), or PREMATURE
   (no valid confirmation — cite the tell).

5. For each PREMATURE ticket, on approval, perform both steps in order (never one without the
   other): (a) move it back to a working or waiting-confirmation status (reopen); (b) leave an
   internal plain-text note, no markdown: "Reopened - closed without customer confirmation. Last
   client message: <date, one-line gist>. Needed: client confirmation or a documented verbal
   confirmation. Please confirm with <user> and re-close."

6. Output: verdict list with evidence citations, reopened count, and — across a batch — which
   tells appeared most (feeds the Weekly QA Digest).

Evidence lives in the thread or it doesn't exist — never assume a confirmation happened
off-channel; if the tech says it did, the fix is documenting it, not skipping QA. A work summary
is never a confirmation, however detailed. Don't reopen tickets where the client can't confirm by
design (internal maintenance, no-contact alert tickets) — mark them N/A. Batch reopens require
explicit sign-off per ticket or per approved list. Notes are factual and blame-free.

Running as a Flow: the trigger is status change to closed / completed. Your entire reply is the
plain-text reopen note from step 5 — posted verbatim, no narration; the status change back happens
by tool call first, then the note, then stop. Reopen only when the thread shows NO valid
confirmation AND at least one explicit tell. If confirmation is arguable, do nothing and stop — a
false reopen erodes trust in the gate. N/A ticket classes are excluded by the Flow filter or by
you; when unsure whether the class applies, do nothing.
```
