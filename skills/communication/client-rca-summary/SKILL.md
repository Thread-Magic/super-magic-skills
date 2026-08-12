---
name: Client RCA Summary
description: Draft a client-safe root-cause summary for a resolved issue — what happened, impact, cause, and what prevents recurrence — written defensively. Use for a single-ticket RCA the client asks for, short of a full major-incident letter.
category: Communication
tools: [search_tickets, search_knowledge_base, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Client RCA Summary

**When to use:** "The client wants to know why this happened — draft an RCA" / "write a root-cause summary for this resolved ticket" — a single incident is resolved and the client asks for an explanation short of a formal outage letter.

**Run it:** on one ticket.

## Prompt

```
Draft a concise, client-facing root-cause summary: what happened, the impact, the confirmed
cause, and the concrete steps that reduce recurrence — written so every sentence holds up if
the email is forwarded to the client's leadership or their insurer.

1. Read the full ticket history — timeline, actions taken, resolution — before writing. Every
   claim must trace to the record. Check the knowledge base if a known-error article is relevant.

2. Structure:
   - What happened — a plain, factual description of the issue and when it occurred.
   - Impact — who/what was affected and for how long, as recorded.
   - Root cause — the confirmed cause. If still uncertain, say "our current assessment is..."
     and do NOT present a hypothesis as fact.
   - Resolution — what fixed it.
   - Prevention — the specific steps taken or planned to reduce recurrence. Only list steps
     that are real; don't manufacture a prevention plan to sound thorough.

3. Keep it tight and non-technical; gloss any unavoidable technical term.

4. Apply defensive writing: state facts, not speculation; never call an unconfirmed event a
   "breach" or "compromise"; never assign blame to a vendor, the client, or a prior tech unless
   it is confirmed and appropriate to share.

5. Show me the draft for review, labeled "DRAFT — review before sending." Do NOT send.

Defensive by default — write assuming a lawyer will read it: no admission of fault, no
speculation stated as fact, no naming a third party's failure that isn't confirmed. Cause
honesty: if root cause isn't definitively known, label it an assessment and say investigation
continues — never fabricate certainty. Prevention must be real — only cite measures actually
taken or committed by the record.
```
