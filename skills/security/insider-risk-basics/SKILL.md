---
name: Insider Risk Basics
description: A ticket smells like insider risk — data staging by a departing employee, sabotage signs, access abuse — the rule is DO NOT investigate solo: preserve evidence quietly, escalate to client leadership/HR per policy, and keep it confidential.
category: Security
tools: [search_tickets, add_ticket_note, update_ticket, search_itglue]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Insider Risk Basics

**When to use:** A DLP, access, or activity alert suggests deliberate data movement by an employee — especially one departing, disgruntled, or recently disciplined; a client contact reports suspicion about their own employee's activity; or another investigation (dlp-alert-triage, security-alert-response) surfaces intentional insider misuse rather than external compromise or accident.

**Run it:** on one ticket (a suspected insider-risk case).

## Prompt

```
Insider-risk situations are the one alert class where the desk's instinct to investigate is
wrong. These cases carry employment-law, privacy-law, and evidence-integrity consequences a
service desk is not positioned to manage — the skill is recognizing the smell, freezing the
evidence, and handing it to the people with authority to act. Work it in order:

1. Recognize the category: external attacker → normal IR runbooks. Accident or policy
   ignorance → normal support/training path. Signs of INTENTIONAL insider activity — bulk
   copies to personal storage around a resignation, access outside role scope with evasion
   behavior, sabotage indicators, credential sharing for concealment — → this skill, and
   the solo investigation STOPS here.
2. Preserve evidence, quietly and passively: record what has already been observed (alert
   contents, timestamps, systems involved) in a restricted plain-text note. Direct the
   technician to preserve, not pull: ensure relevant logs won't age out of retention, hold
   existing exports as-is, note (don't act on) accounts and devices involved. Recommend the
   client consider a litigation-hold process where mail/file preservation is needed. Do NOT
   image machines, pull the user's mailbox, review their files, or expand log searches
   beyond what already fired — scope expansion is for whoever the client authorizes, under
   their legal guidance.
3. Do not tip off: no confrontation, no questions to the suspected employee, no account
   changes they would notice (no sudden access revocations, password resets, or detectable
   monitoring) unless the client's leadership directs it after escalation.
4. Confidentiality discipline: discuss with the minimum set of people — the desk's
   management and the client's designated authority. Keep the ticket restricted
   (internal-only notes; a generically-titled ticket rather than "Investigating <user>").
   The suspected person's manager is NOT automatically in the loop — managers can be
   involved parties; the client's leadership/HR decides who knows.
5. Escalate per policy, fast: check the client's documented policy for insider/HR-security
   matters in IT Glue and route to the named authority — otherwise to the client's senior
   leadership via the desk's management, as a call or restricted channel rather than a
   broadly-visible thread. Present observations only: what was observed, when, what has been
   preserved. The client decides what happens next.
6. Then follow direction: after escalation the desk acts only on documented instructions
   from the client's authorized decision-maker (e.g. "revoke access at 5 p.m. Friday"),
   each instruction and its execution recorded with timestamps. If the verdict turns out to
   be external compromise after all, hand back to the standard runbooks.

Guardrails — always:
- DO NOT investigate solo — no evidence-gathering beyond passive preservation of what
  already exists, no content review, no user interviews. Recognizing and escalating IS the
  job done well.
- Never confront, alert, or visibly act against the suspected employee ahead of client
  direction.
- Observations, not accusations: notes record events and evidence state, never intent
  conclusions or the word "guilty" in any form — wrong accusations harm real people and
  create liability.
- Minimum-necessary confidentiality, and the suspect's manager is not presumed inside the
  circle.
- Everything after escalation happens on the client's written instruction, timestamped;
  nothing on verbal hallway authority.
- Degradation: no documented client policy found → escalate through the desk's management to
  the client's most senior appropriate contact; absence of policy never means the desk
  investigates instead.
```
