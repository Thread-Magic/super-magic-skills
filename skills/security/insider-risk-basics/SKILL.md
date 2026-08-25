---
name: Insider Risk Basics
description: Handle insider-risk signals like data staging, sabotage, or access abuse: preserve evidence quietly, escalate to client HR, and keep it confidential.
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
Insider risk is the one alert class where the desk's instinct to investigate is wrong: these
cases carry employment-law, privacy-law and evidence-integrity consequences a service desk
cannot manage. Recognize it, freeze the evidence, hand it to whoever has authority to act.

1. Recognize the category. External attacker → normal IR runbooks; accident or policy
   ignorance → normal support and training. Signs of INTENTIONAL insider activity — bulk
   copies to personal storage around a resignation, access outside role scope with evasion
   behavior, sabotage indicators, credential sharing for concealment — mean this skill, and
   solo investigation STOPS here.
2. Preserve evidence quietly and passively. Record what has already been observed — alert
   contents, timestamps, systems involved — in a restricted plain-text note. Direct the tech
   to preserve, not pull: stop relevant logs aging out of retention, hold existing exports
   as-is, note (don't act on) the accounts and devices involved. Recommend a litigation hold
   where mail or file preservation is needed. Do NOT image machines, pull the user's mailbox,
   review their files or widen log searches beyond what already fired — scope expansion
   belongs to whoever the client authorizes, under legal guidance.
3. Do not tip off. No confrontation, no questions to the suspected employee, no account change
   they would notice — no sudden access revocation, password reset or detectable monitoring —
   unless the client's leadership directs it after escalation.
4. Keep it confidential. Discuss with the minimum set: the desk's management and the client's
   designated authority. Keep the ticket restricted — internal-only notes, a generic title, not
   "Investigating <user>". The suspect's manager is NOT automatically in the loop;
   managers can be involved parties; the client's leadership or HR decides who knows.
5. Escalate per policy, fast. Check the client's documented policy for insider and HR-security
   matters and route to the named authority — otherwise to their senior leadership via the
   desk's management, on a call or restricted channel, not a visible thread. Present
   observations only: what was seen, when, what has been preserved. The client decides
   what happens next.
6. Then follow direction. After escalation the desk acts only on documented instructions from
   the client's authorized decision-maker ("revoke access at 5 p.m. Friday"), each instruction
   and its execution timestamped — nothing on verbal hallway authority. If it turns out to be
   external compromise, hand back to the standard runbooks.

Observations, not accusations: notes record events and evidence state, never intent
conclusions. With no documented client policy, escalate through the desk's management to the
client's most senior appropriate contact; absence of a policy never means the desk
investigates instead.
```
