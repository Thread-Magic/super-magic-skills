---
name: Security Incident Postmortem
description: Build a security incident postmortem: executive summary, timeline, impact, root cause, and action items drawn from ticket evidence in defensible language.
category: Security
tools: [search_tickets, search_knowledge_base, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# Security Incident Postmortem

**When to use:** "Write up the postmortem / PIR / incident report for <ticket>"; a client, insurer, or management asks for the formal record of a resolved incident; or a recurring incident needs its pattern documented for the problem record.

**Run it:** on one ticket (a resolved incident to write up).

## Prompt

```
Turn the ticket record of a security incident into a structured postmortem: what happened
and when, what was affected (and provably not), why it happened, and what changes — with
every claim traceable to timestamped evidence and every sentence written to the
defensive-writing-standard. Work it in order:

1. Gather the raw material: the incident ticket(s) and their notes (search for linked and
   sibling tickets), containment timestamps, and any related change tickets. The containment
   notes' timestamp lines are the spine of the timeline.
2. Build the timeline first: detection → triage → containment → eradication → recovery, each
   entry with a timestamp and its source note. Gaps in the timeline are findings, not
   embarrassments — record them.
3. Draft the document in this structure:
   - Executive summary: 3–5 sentences, defensive-writing-standard vocabulary, readable by a
     non-technical owner.
   - Timeline: the timestamped sequence.
   - Impact: what was affected, and what was NOT affected — negative claims ("no other
     accounts showed anomalous sign-ins") only where evidence supports them, with the
     evidence named.
   - Root cause: the confirmed cause, or "under investigation" / "most probable cause,
     unconfirmed" — labeled as such.
   - Actions taken: containment and remediation, from the record.
   - Follow-up actions: each with a suggested owner and a target date; recommendations, never
     reported as done.
4. Label every inference: facts carry timestamps and sources; anything reasoned-but-unproven
   is marked as assessment, not fact.
5. Apply the defensive-writing pass: "breach" only if the incident was a confirmed
   system-level event and management has used the word; never "hacked"; no absolute safety
   claims without log evidence; no attacker attribution.
6. Deliver the draft for human review and leave it as a note or KB draft on request — the
   postmortem is management's document to finalize and distribute.

Guardrails — always:
- No unverified impact claims in either direction — "no data was accessed" requires evidence,
  not absence of evidence.
- Root cause unknown → the document says so; a guessed root cause in a formal record is worse
  than an open question.
- Blameless by construction: name processes and controls, not individuals.
- Do not invent timeline entries, ticket references, or evidence; gaps stay gaps.
- Distribution (client, insurer, legal) is a management decision — you draft and stop.
```
