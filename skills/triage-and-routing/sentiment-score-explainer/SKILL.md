---
name: Sentiment Score Explainer
description: Explain why a ticket thread received its sentiment score by citing the exact messages that drove it — no hand-waving, no re-scoring.
category: Triage & Routing
tools: [search_tickets, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Technician, Service & Ops Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Sentiment Score Explainer

**When to use:** "Why did this thread receive this sentiment score?" — a flow fires when sentiment drops and needs an evidence note for the tech, or a lead reviewing flagged-negative tickets wants the driver messages, not a summary.

**Run it:** on one ticket · across all flagged-negative tickets · or as a Flow (when a ticket's sentiment drops).

## Prompt

```
Trace a thread's sentiment score back to the specific messages and phrases that plausibly drove
it, quoted verbatim.

1. Read the full thread — every message, in order, with authors and timestamps — plus the
   current sentiment score.

2. Identify the client-authored messages carrying sentiment signal: frustration, urgency,
   satisfaction, escalation language, repeated follow-ups, or sarcasm. Where useful, use a
   sentiment read to cross-check your own. Only client-authored messages drive client sentiment
   — never attribute a tech's tone to the client.

3. For each driver, quote the exact phrase verbatim with its message position (author +
   timestamp). Distinguish frustration at the situation from frustration at the desk — the score
   usually reflects both, but techs need to know which.

4. Note counter-signals too: positive or neutral messages that pulled the other way, and whether
   the negative signal is recent or early-thread (recency usually dominates).

5. Output (or leave as a plain-text note, if asked): the score, 2-4 quoted driver messages with
   one-line readings, counter-signals, and one line on whether the score looks consistent with
   the evidence.

Cite exact messages, quoted verbatim — never summarize a feeling into existence; every claimed
driver must be traceable to a quote. Explain the score; do not change it or overwrite it with
your own re-score. If the evidence contradicts the score, say "the score does not appear
consistent with the thread" and leave it to a human. Sentiment phrasing varies by language and
culture; read messages in their own language before judging tone, and say so when the thread is
non-English. Read-only except for the optional note.

Running as a Flow: your entire reply is posted verbatim as the internal note — plain text, no
markdown. Format: "SENTIMENT <score>: driven by: [1] "<quote>" (<author>, <when>) - <one-line
reading>. [2] ... Counter-signals: <one line or "none">. Consistency: <one line>." If the thread
has no client messages or the score is unavailable, output exactly: "SENTIMENT EXPLAINER:
insufficient thread content to explain score." Never modify the ticket; the note is the only
write.
```
