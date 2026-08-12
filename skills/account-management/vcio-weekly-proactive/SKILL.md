---
name: vCIO Weekly Proactive
description: Pick the three highest-leverage clients to proactively contact this week from live ticket signals, with a reason and a suggested opener for each outreach.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# vCIO Weekly Proactive

**When to use:** "Which 3 clients should I proactively contact this week and why?"; "who needs a touch from me this week?"; or a recurring Monday-morning outreach planning run.

**Run it:** across the portfolio's last ~30 days — a manual weekly ritual, not a Flow.

## Prompt

```
You are running a weekly ritual for account managers and vCIOs: instead of reacting to
whoever shouts, pick the three clients where a proactive touch this week does the most
good — and know exactly what to say.

1. Establish the portfolio (look up the clients, or use the AM's stated account list) and
   look back over roughly the last 30 days — separate searches per signal, not one
   mega-query.

2. Score outreach candidates on signals like:
   - A rough patch just ended (major incident resolved, SLA miss) — a follow-up turns a
     miss into a save.
   - Sentiment drifting down — early, cheap to repair.
   - Unusual quiet from a normally active client — silence can mean disengagement.
   - A pattern worth advising on (recurring issue, aging kit) — a proactive recommendation
     lands better than a reactive quote.
   - A win worth celebrating — a project landed, a fast save; goodwill is free.
   - No touch in a long time — relationship maintenance.

3. Pick exactly THREE clients — the highest-leverage touches, not the three loudest.
   Diversity of reason is a feature: ideally not three of the same signal.

4. For each of the three, output:
   - Why now — the signal, with one representative example in plain language (no ticket
     IDs).
   - Suggested opener — two or three sentences the AM could actually say or send, labeled
     DRAFT.
   - Watch-out — one line on anything to avoid stepping in during the call.

5. List one or two bench clients (would have made the list on another week) so the AM can
   trade if they disagree.

Guardrails: recommendations only — never send the outreach yourself. Every pick needs
ticket-evidence for its "why now"; no filler picks to reach three — if the portfolio
genuinely offers fewer than three good touches, say so. Never pick on volume alone; the
signal, not the count, justifies the call. Internal analysis and DRAFT openers are clearly
separated; openers contain no ticket IDs or internal commentary. Note any result caps hit
— a capped scan means the picks come from a sample, and the output should say so.
```
