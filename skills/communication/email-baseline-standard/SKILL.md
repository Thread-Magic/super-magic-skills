---
name: Email Baseline Standard
description: The base client-email standard other communication skills build on — structure, tone rules, and placeholder discipline for every outbound message. Load when drafting any client email, or when another skill references it.
category: Communication
tools: []
connectors: []
scope: both
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Email Baseline Standard

**When to use:** Whenever another communication skill says "per the Email Baseline Standard," or when someone asks "what's our email standard?" or wants an email drafted that no specialized skill covers.

**Run it:** on one ticket · or across any client email the desk sends.

## Prompt

```
Apply this standard to every client-facing email. It defines house structure, tone,
and placeholder discipline — other skills reference it instead of restating it.

STRUCTURE, in order:
1. Greeting — client's first name, on the FIRST message of a thread only. No greeting on
   later replies in the same thread.
2. Context line — one sentence anchoring which issue/ticket this is about, so the email
   stands alone in their inbox.
3. Body — the substance, answer first, then detail. 1-2 short paragraphs for routine messages.
4. Next steps — who does what next, and by when. If the client must act, make the action
   unmissable (its own line or a short list).
5. Close — one plain forward-looking sentence. Do NOT add a sign-off block if a managed
   signature is applied automatically (it would double up).

TONE:
- Plain, direct, warm. Write like a competent human, not a template.
- No filler openers ("I hope this finds you well", "Just circling back").
- No jargon unless the client used the term first; gloss any unavoidable technical term.
- Never blame the client, a colleague, a vendor, or a previous tech.
- Commit only to what is confirmed: "We'll update you by <time>" beats "this should be fixed soon."

PLACEHOLDER DISCIPLINE:
- Drafts may use bracketed placeholders (<client first name>, <ticket number>, <time window>),
  but every bracket must be filled before sending. Fill each from ticket data, or flag the
  unfilled ones explicitly at the top of your output ("NEEDS: <time window>"). Never let a
  placeholder leak into a sent message.

DEFENSIVE WRITING:
- State facts, not speculation. Never assert a cause, a breach, or a third party's failure
  that isn't confirmed in the ticket record.
- Never use "hacked," "breached," or "compromised" for unconfirmed security events — say
  "suspicious activity we are investigating."
- Write every email as if it will be forwarded to the client's lawyer, their boss, and your
  competitor — because sometimes it is.

This skill defines standards; it sends nothing. House-specific overrides (per-partner tone,
banned words, signature policy) take precedence — apply them on top. These rules survive
translation: when drafting in another language, keep structure and defensive-writing intact.
```
