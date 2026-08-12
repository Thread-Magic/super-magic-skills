---
name: Technical to Plain English
description: Translate a technical resolution, diagnosis, or explanation into language a non-technical stakeholder can understand — "make this client-friendly."
category: Communication
tools: [search_tickets]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Retention & Growth (CSAT/Expansion), Time & Cost Savings (Capacity)]
---

# Technical to Plain English

**When to use:** "Explain this fix in plain English for the client" / "the office manager asked what actually happened — translate this" — any resolution note, diagnosis, or vendor explanation that needs to leave the technical bubble.

**Run it:** on one ticket.

## Prompt

```
Rewrite technical content for a non-technical reader: same truth, no jargon, framed around what
it means for them rather than how it works.

1. Read the technical source (resolution notes, diagnosis, pasted vendor response — pull it
   from the ticket if referenced). Identify the three things the plain version must carry: what
   was wrong, what changed, and what it means for the reader.

2. Translate using these rules:
   - Replace every technical term with what it does, not a simpler synonym for what it is
     ("DNS wasn't resolving" -> "computers couldn't look up where to find the server").
   - Analogies are allowed when they clarify — keep them modest and accurate; an analogy that
     overstates certainty or severity is worse than jargon.
   - Lead with the reader's stake: impact and status first, mechanism second (only as much as
     they need).
   - Keep quantities honest but round ("about 40 machines," not "38 endpoints").
   - Sentence test: would a smart person with no IT background nod along? If a sentence needs
     IT knowledge, rewrite it.

3. Preserve exactness where it matters: dates, durations, what data was or wasn't affected, and
   any action the reader must take stay precise, never approximated away.

4. Output the plain-English version standing alone. If it's destined for an email, apply our
   house email tone (answer first, plain, no filler); if I just need the explanation, the text
   itself is the artifact.

Simplify the language, never the truth: no rounding "mostly fixed" up to "fixed," no dropping
caveats, no upgrading uncertainty into confidence. Never introduce cause claims the source
doesn't make. Security topics keep defensive-writing rules: "suspicious activity," not "hack,"
unless confirmed. Don't condescend — plain is respectful, not childish. If the source is
ambiguous or self-contradictory, flag it to me instead of picking an interpretation.
```
