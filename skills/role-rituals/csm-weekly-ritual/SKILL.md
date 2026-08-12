---
name: CSM Weekly Ritual
description: A CSM or vCIO weekly account runbook: proactive outreach, sentiment-decline watch, meeting prep for the week's calls, and an expansion-scan skim.
category: Role Rituals
tools: [search_tickets, search_clients, search_contacts]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# CSM Weekly Ritual

**When to use:** "Run my CSM weekly" / "what do my accounts need this week" / "prep my account week" — Monday morning across the CSM's own book of business.

**Run it:** across your whole book of business — run it manually (not a Flow; Flows can't schedule a weekly cadence).

## Prompt

```
You are running my CSM weekly ritual as a chain of existing skills, in a fixed sequence. Scope everything strictly to MY own book of business — my accounts, my calls. Target ~90 minutes at the start of the account week. Propose, don't apply: client-facing messages are drafts until I approve them — never auto-send outreach, and when in doubt, do nothing.

Run these skills IN ORDER:
(1) Proactive pass: run the account-management/vcio-weekly-proactive skill across my book — which accounts get a proactive touch this week and what the touch says (an insight, a heads-up, a fixed thing they did not know broke). Every touch must contain something real (a fixed issue, a metric, a relevant heads-up) — a contentless check-in email costs goodwill.
(2) Sentiment-decline watch: run the account-management/sentiment-decline-watch skill — accounts whose ticket sentiment or engagement is trending down. Any account flagged here gets promoted to a call or an owner this week; a flag with no action is a flag wasted. Flags require evidence (scores, ticket refs, dates) — do not put an account on a risk list on a hunch.
(3) Meeting prep: for each client call on this week's calendar, run the account-management/meeting-prep-brief skill, folding in anything steps 1–2 surfaced about that client.
(4) Expansion skim: run the account-management/expansion-opportunity-scan skill in skim mode — any account whose usage/asks suggest a service conversation. Note candidates and deep-dive only the strongest one. Expansion candidates stay internal; nothing sales-flavored reaches a client from this ritual.
(5) Output the weekly account card: this week's proactive touches (client + one-line message angle), sentiment flags and the action taken on each, calls prepped, and at most one expansion candidate worth pursuing.

Time-short version: steps 2 and 3 — declining sentiment and unprepped calls are the two same-week risks. Mark the proactive pass and expansion skim "skipped: time".

Guardrails, all inline:
- Skip-with-note beats fake completion.
- Disclose result caps on book-wide scans: if a search may have truncated, say so rather than presenting a partial book as complete.
- Never invent accounts, contacts, ticket numbers, metrics, or links — report only what the searches and underlying skills return.
- If a chained skill's connector (e.g. calendar for meeting prep) is unavailable for this tenant, note the degradation and continue with the rest.
- Any note that may sync to the PSA is plain text — no markdown, no emojis.
```
