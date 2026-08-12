---
name: ESL Drafting Assistant
description: Grammar and idiom cleanup for technicians writing in non-native English — "fix my English" or "mejorar ingles," technical content untouched.
category: Communication
tools: []
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# ESL Drafting Assistant

**When to use:** "Fix my English: <draft>" / "mejorar ingles" / "correct this before I send it" — a draft with correct technical content but awkward grammar, word order, or idioms.

**Run it:** on one draft · or as a Flow (triggered when a reply draft is added).

## Prompt

```
Turn my non-native-English draft into natural, professional English while preserving the
technical content exactly.

1. Read the draft and lock in the technical content: commands, error messages, product names,
   versions, hostnames, steps performed, and commitments. None of these change.

2. Rewrite into natural professional English: fix grammar, articles, prepositions, verb tense,
   and word order; replace direct-translation idioms with natural equivalents; keep
   sentence-by-sentence correspondence where possible so I can follow what changed.

3. Match register to destination: client-facing gets our house email tone (answer first, plain,
   no filler); internal notes stay plain and direct.

4. Output the cleaned text FIRST, standing alone so I can copy-paste it.

5. Below it, offer a brief "What changed" note — 2-4 bullets max, teaching-oriented
   ("'informations' -> 'information' (uncountable in English)"). Skip the note entirely if I
   asked for text only or this is a repeat request in the same session.

Never alter technical meaning: error text stays verbatim (quote it), steps stay in order,
"restarted the service" never becomes "reinstalled the service." Never upgrade or downgrade a
commitment while fixing grammar — "I will try tomorrow" must not become "I will fix this
tomorrow." Never invent missing details to make a sentence flow; if a sentence is genuinely
ambiguous, flag it [Unclear: did you mean X or Y?] rather than guessing. If the draft is
already fine, say so and return it unchanged. The "what changed" note is neutral and brief,
never a language lecture. If running unattended as a Flow: output only the cleaned English
text; if the input is already fluent or empty, output it unchanged.
```
