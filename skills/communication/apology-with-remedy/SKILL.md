---
name: Apology With Remedy
description: Draft the message for when the desk genuinely failed — specific acknowledgment of what went wrong, a concrete remedy, and one prevention step — without groveling and without admissions beyond the established facts.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise, Retention & Growth (CSAT/Expansion)]
---

# Apology With Remedy

**When to use:** "We really dropped the ball on this one — draft the apology with a make-good" — a failure bigger than a slipped date: wrong change applied, data-affecting mistake, repeated misses, a broken commitment after an escalation. For a simple slipped timeline, use Delay Apology instead.

**Run it:** on one ticket.

## Prompt

```
Draft the accountability message that actually repairs trust: names the failure precisely,
offers something real to make it right, and says what changes so it doesn't recur — in the
confident voice of a professional who owns mistakes, not a supplicant.

1. Establish the facts from the ticket record: read the full history to find what specifically
   went wrong, when, the client-visible impact, and what's already been done to fix or contain
   it. The apology must match the record — apologizing for the wrong thing, or for more than
   happened, both make it worse.

2. Confirm the REMEDY with me before drafting — it must be real, approved, and specific: a
   credit of a stated amount, waived hours, priority remediation, a senior review. Never invent
   one, never imply one is coming if none is approved. If no remedy is approved yet, tell me
   the letter is materially weaker without one and draft accordingly.

3. Confirm the PREVENTION step: the one concrete change being made (a checklist added, a review
   gate, a monitoring alert). It must be something the desk is actually doing — a fabricated
   process improvement is a second failure waiting to be discovered.

4. Draft:
   - Specific acknowledgment, first sentence: what went wrong and its impact on them, in plain
     words, no passive-voice fog ("we applied the change to the wrong server, which took your
     <system> offline for <duration>").
   - One apology. Direct, unqualified — no "we apologize if this caused inconvenience," no "but."
   - What we've done to fix/contain it, if not already known to the client.
   - The remedy, stated plainly as a done decision.
   - The prevention step, one or two sentences: "so this doesn't happen again, we have <change>."
   - Close forward-looking; invite a call if the relationship warrants it.

5. Tone pass — the hard part: exactly one apology, zero groveling ("we're deeply ashamed,"
   "unforgivable"), zero blame-shifting to vendors or tools. Cut every hedge and every excuse.

6. Show me the draft for account-manager review, labeled "APOLOGY DRAFT — AM review required."
   Do NOT send. For significant failures, recommend it come from the AM's or a leader's name.

Acknowledge only what the record establishes — never speculate about additional harm, never
characterize the failure legally ("negligence," "liability," "at fault"), never promise
compensation beyond the approved remedy. If the incident plausibly involves legal,
contractual-penalty, or insurance exposure, flag for management review before anything is sent
— that is a gate, not a formality. Never blame a named individual technician in client-facing
text — the desk owns the failure institutionally.
```
