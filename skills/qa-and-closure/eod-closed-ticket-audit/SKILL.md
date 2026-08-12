---
name: EOD Closed Ticket Audit
description: End-of-day quality sweep of every ticket closed today — check each against the closure rubric (resolution evidence, documentation, classification, time, closure message) and produce a pass/fail summary with reopen recommendations.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, list_boards]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# EOD Closed Ticket Audit

**When to use:** End of day — "audit today's closed tickets" / "how did today's closures look?", a lead running a daily quality pulse on the desk or one tech, or catching up after a busy day when the per-ticket QA gate wasn't running.

**Run it:** across all tickets closed today (manually or on a schedule).

## Prompt

```
The daily batch version of the QA gate: instead of grading one ticket at close time, sweep
everything closed today and report where the closure standard slipped — before the tickets are a
week old and nobody remembers the context.

1. Find every ticket closed today, splitting searches per board so result caps don't truncate the
   day. If a search may have capped, say so rather than presenting the count as exact.

2. For each closed ticket, grade the closure rubric strictly from the thread (same criteria as
   Ticket QA Review): genuine resolution evidence (customer confirmation or documented verbal
   confirmation — a work summary does not count), classification set, owner assigned, time logged,
   title accuracy, and a client-facing closure message. Additionally check documentation: the notes
   let a stranger reconstruct what the issue was, what was done, and why it worked.

3. Score each ticket PASS (all criteria met) or FAIL (list the failing criteria). Score 0 on any
   criterion whose evidence isn't in the thread — never assume. If confirmation may have happened
   off-channel, mark it FAIL on evidence and flag for the tech to document.

4. Produce the audit report:
   - Headline: N closed, N passed, N failed, pass rate.
   - Failures grouped by ticket: failing criteria, one line each, plus the single fix that would
     make it pass.
   - Patterns worth a sentence: a criterion failing repeatedly, or a cluster on one board.

5. For each failure, recommend the action: reopen for rework, or annotate-and-leave when the miss
   is documentation-only and the client outcome was fine. Apply reopens (move it back to a working
   status, then leave a plain-text internal note, in that order) only for tickets the user approves
   — never reopen in bulk without explicit sign-off on the specific tickets.

6. Keep the whole report skimmable in under a minute — a table plus a short patterns paragraph,
   not an essay.

Per-tech numbers are factual counts, not commentary; coaching interpretation belongs to the Weekly
QA Digest skill and the human lead. Notes posted to reopened tickets are plain text (PSA sync).
Disclose result caps; a partial audit presented as complete is worse than no audit. If write tools
are disabled, deliver findings and recommended reopens in chat only.
```
