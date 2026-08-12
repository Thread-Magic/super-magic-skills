---
name: New Client 30-Day Review
description: Friction check on a client's first 30 days — early recurring issues, expectation mismatches, and onboarding gaps — so problems get fixed while the relationship is still forming.
category: Account Management
tools: [search_tickets, search_clients, search_contacts]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# New Client 30-Day Review

**When to use:** "<client> has been with us a month — how's it going?"; "run a 30-day review on our new client"; or "any early warning signs from <client>'s onboarding?"

**Run it:** across a new client's first month of history — a manual internal review, not a Flow.

## Prompt

```
You are reading every early signal from a client's first month — ticket patterns, tone,
confusion — and reporting where the onboarding is leaking before it hardens into
resentment. The first month sets the tone for the whole engagement.

1. Confirm the client (look it up) and their start date; review from go-live to now
   (roughly the first 30 days).

2. Pull all tickets in the window. Early volume is small, so read broadly — tone and
   phrasing matter as much as counts here.

3. Early recurring issues. Anything that has already happened more than once: an unstable
   system, a misconfigured integration, a site with chronic problems. One representative
   example per pattern.

4. Expectation mismatches. Threads where the client expected something different from what
   they got — response times, scope ("I thought this was covered"), channels ("I emailed
   the old address"), or who does what. Quote the mismatch in plain language.

5. Onboarding gaps. Signals that setup is incomplete: contacts not in the system
   (cross-check requesters against the contact roster), tickets landing on the wrong board,
   missing documentation forcing techs to ask the client basics, devices or users not yet
   under management, monitoring not yet reporting.

6. Tone read. Are the early interactions warm, neutral, or already strained? One or two
   lines with what drove it.

7. Close with a fix list: the three to five concrete actions, ordered by urgency, that
   would close the gaps — each traceable to a finding above.

Guardrails: internal only — this informs the 30-day check-in call, it is not the check-in;
anything shared with the client is rewritten separately, without ticket IDs. Small-sample
honesty: 30 days supports observations, not verdicts — phrase findings as early signals,
never as conclusions about the client. Never flag on volume alone — new clients
legitimately generate a burst of setup tickets; the pattern and tone carry the signal. If
early friction traces to a specific technician's handling, describe the process gap;
performance evaluation goes to the manager. Do not invent onboarding checklist items that
were never promised — mismatches must come from thread evidence.
```
