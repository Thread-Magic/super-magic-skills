---
name: One-on-One Prep
description: A manager is preparing for a 1:1, 30-day check-in, or coaching conversation with a technician and wants a candid brief on their recent work.
category: Reporting & Analytics
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# One-on-One Prep

**When to use:** "I have a 1:1 with <user> this afternoon — prep me," a 30/90-day check-in on a newer engineer, or "how is <user> doing lately?" ahead of a coaching conversation.

**Run it:** across all of one tech's tickets in the period — manually on demand (a prep brief has no ticket event for a Flow to trigger on).

## Prompt

```
Give a manager a concise, candid brief on one technician's recent work — sized to be
read in the two minutes before the meeting. Manager's eyes only: write candidly and
never post this to a ticket or client channel.

1. Confirm the technician (look them up by name) and the period; default to the last 30 days.

2. Pull their tickets, splitting searches per signal (opened,
   closed, still open, negative sentiment) and per board where volume may hit a result
   cap. Disclose any caps hit.

3. Write AT MOST 300 words in five short paragraphs:
   - Load — tickets worked, opened vs closed, current aging/stalled items.
   - Speed — response and resolution patterns, distinguishing tech-side delays from
     client or vendor holds.
   - Sentiment — the overall trend across tickets with data, plus the single best and
     single worst interaction.
   - Highlights — exactly two standout pieces of work.
   - Improvements — exactly two specific, actionable areas to work on.

4. AGGREGATE rather than enumerate: report patterns and counts, not ticket-by-ticket
   listings. Name a specific client or ticket only when it genuinely needs the
   manager's action.

5. Benchmark ROLE-AWARE: a dispatcher, project engineer, or lead carries different
   open/closed expectations than an L1 — do not rank them against raw tech numbers.
   NEVER treat ticket volume alone as a performance signal — pair every count with an
   outcome (resolution, reopen, sentiment). Exclude junk/NOC boards and auto-closed
   statuses. If sentiment or timing data is missing for the period, say so rather than
   inferring.

6. Close with a one-line methodology note: period covered, which searches were run,
   and any result caps hit.
```
