---
name: Multilingual Reply
description: Draft the client reply in the client's own language — detect it from their messages, write natively in it, and provide an English back-translation so the technician can verify before sending.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Multilingual Reply

**When to use:** A client writes in Spanish, French, Dutch, German, Norwegian, or any non-English language and the reply should match — "reply to this in their language" / "translate my reply to <language> before I send it."

**Run it:** on one ticket.

## Prompt

```
Draft the client reply in their language, and give me an English mirror so I can verify it says
what I meant.

1. Detect the client's language from their messages in the thread — the language they actually
   write in, not their country or name. If the thread mixes languages, match their most recent
   substantive message; if genuinely ambiguous, ask me which language.

2. Draft the reply NATIVELY in that language — composed in it, not word-for-word translated
   from an English draft — applying full house standards: answer first, no filler, greeting
   only on a thread's first message, defensive writing, and locally natural register (match
   their formal/informal address — vous/usted/Sie level).

3. Keep technical anchors unambiguous: product names, error messages, and ticket numbers stay
   as-is; error text the client must recognize on screen is quoted in its original language.

4. Provide the English back-translation directly below the draft, labeled "English
   back-translation (for your review)" — a faithful mirror of what the foreign-language draft
   actually says, including anything that shifted in translation.

5. Show me both together (draft on top, back-translation below for removal before send) for
   review. I confirm before anything is sent.

The back-translation is mandatory whenever I don't read the target language — never ask me to
approve text I can't verify, and remind me to remove it before sending. The two versions must
match: never add nuance, promises, or softening in one that isn't in the other; if a concept
doesn't translate cleanly, flag it ("<term> has no direct equivalent — I used X, which means
Y"). All standard reply guardrails apply across languages: no invented details, no jargon,
defensive writing intact, reopen line on close-outs (translated naturally). If the language
uses honorifics the thread doesn't reveal, default to formal.
```
