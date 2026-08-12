---
name: Delay Apology
description: Draft an honest acknowledgment that a ticket has taken too long or a commitment slipped — apology without excuses, new commitment only if confirmed.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Delay Apology

**When to use:** "This ticket sat for a week — draft an apology to the client" / "we missed the date we promised, help me write the update" — a thread shows a long silent gap or a blown commitment. For a bigger failure with a make-good, use Apology With Remedy.

**Run it:** on one ticket.

## Prompt

```
Draft the message that repairs a slipped timeline: honest about the delay, silent on excuses,
and careful not to replace one broken promise with another.

1. Read the thread and establish the shape of the delay: what was promised (or reasonably
   expected), when, and how long the gap actually is. Get the facts right — apologizing for the
   wrong thing makes it worse.

2. Draft:
   - Open by naming the delay plainly: "This has taken longer than it should have, and I'm
     sorry for the silence since <day>." No filler before it.
   - No excuses. One neutral sentence of context is allowed only if it helps the client (e.g.,
     "we've been waiting on the vendor" when true and documented) — never workload, staffing,
     or "things have been busy."
   - State where the issue actually stands right now.
   - New commitment — ONLY if confirmed. Before including any new date or promise, ask me what
     I can actually commit to. If I haven't confirmed one, close with the honest alternative:
     "I'll update you by <end of next business day> with a firm plan" — a communication
     commitment, not a fix commitment.

3. Keep it to one short paragraph plus the commitment line. Over-apologizing reads as insincere.

4. Show me the draft for review, labeled "DRAFT — confirm the commitment line before sending."

Never invent or infer a new ETA — an unconfirmed date in an apology email is how the desk ends
up writing the next apology; if none is confirmed, carry the update-by line only. Apologize for
what the record shows — don't accept blame for delays caused by the client or a documented
vendor wait (state those neutrally, without finger-pointing). One apology per message. No
compensation offers — that's a management decision; flag it separately if the delay is severe.
```
