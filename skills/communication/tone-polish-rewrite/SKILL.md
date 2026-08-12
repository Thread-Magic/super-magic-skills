---
name: Tone Polish Rewrite
description: Rewrite rough technician text into a polished, client-ready version — "write this nicely," "make this better," "clean this up" — preserving every fact exactly.
category: Communication
tools: []
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Tone Polish Rewrite

**When to use:** "Write this nicely: <rough text>" / "make this sound professional" / "clean this up before I send it" — a message reads harsh, curt, or unclear and the tech wants a friendlier version with the facts untouched.

**Run it:** on one draft · or as a Flow (triggered when a reply draft is added).

## Prompt

```
Take my rough draft and return a polished, client-ready version with identical factual content.

1. Read the rough text and identify every factual claim: what happened, what was done, times,
   names, commitments. These are immutable.

2. Rewrite for tone and clarity: answer first, plain language, no filler openers, 1-2 short
   paragraphs unless the source demands more. Warm and professional.

3. Honor any style constraints I state, exactly — "no em-dashes" means zero em-dashes,
   "shorter" means shorter, "British spelling" means British spelling. A constraint stated
   once in a session applies to every rewrite in it.

4. Keep my meaning and commitments identical: do not soften a "no" into a "maybe," do not
   upgrade "should" to "will," do not add promises, apologies, or steps the source didn't
   contain.

5. Return ONLY the rewritten text — no preamble, no "Here's a polished version:", no
   commentary, no options unless I ask. The reply is the artifact; I'll copy-paste it.

Never add, remove, or alter facts — polishing is tone-only. If the source is ambiguous, keep
the ambiguity rather than guessing. Never invent a greeting name, ticket number, or detail
not in the source. If the source contains something that must not go to a client (credentials,
internal pricing, blame), keep it out of the rewrite and add one bracketed flag at the end:
[Removed: <what> — internal only]. Preserve the source language unless asked to translate. If
running unattended as a Flow: output only the rewritten text; if the input is empty or has no
rewritable prose, output nothing.
```
