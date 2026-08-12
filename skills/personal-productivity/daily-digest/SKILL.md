---
name: Daily Digest
description: Summarize a technician's open tickets in under a minute with what needs a reply, what's urgent, what's scheduled today, plus a 3-line ultra-short option.
category: Personal Productivity
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Daily Digest

**When to use:** "Give me a summary of my open tickets" / "what needs replies, anything urgent?" / "morning digest" / "what's my day look like?" — the under-a-minute read that names the single first thing to do; ask for "short version" or "3 lines" for the ultra-short variant.

**Run it:** across your own open tickets — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are building my daily digest. Scope everything strictly to MY own open
tickets — never include other techs' queues unless I explicitly ask.

1. Read all open tickets assigned to me. If a result cap may have truncated the
   list, say so up front ("showing 50 — there may be more") instead of presenting
   the digest as complete.

2. Sort every ticket into exactly one bucket, in this priority order — a ticket
   lands in the first bucket it qualifies for:
   - Needs your reply: the client responded last and is waiting on you. Order by
     how long they've been waiting.
   - Urgent / at risk: high priority, SLA at or near breach, or negative-sentiment
     threads. Order by severity.
   - Scheduled today: tickets with a schedule entry or committed follow-up today,
     in time order.
   - Waiting on others: client, vendor, or escalation has the ball. Flag any quiet
     3+ days as a nudge candidate, but don't let this bucket crowd the top.
   - Everything else: count and a one-line characterization only, no per-ticket lines.

3. Each ticket line is ONE line: number, client (short), 5–8-word state, and the
   next action ("#1234 <client> — printer offline 2d, client replied yesterday ->
   confirm fix worked"). Every line must be actionable — a state without a next
   action is a wasted line.

4. Lead with "Start here:" — the single most important ticket and one sentence why
   (longest-waiting client reply beats vague urgency; a hard SLA breach beats
   everything).

5. Close with the shape of the day: totals per bucket and one sentence ("2 replies
   and 1 urgent before your 10:00 scheduled visit clears most of the pressure").

6. If I ask for the short version (or "3 lines"), output EXACTLY three lines and
   nothing else: (1) Start here + why, (2) counts — X need replies / Y urgent /
   Z scheduled, (3) the one thing that will bite if ignored today. No headers,
   no preamble.

7. Offer the natural follow-up: "Want reply drafts for the ones waiting on you?"

This is read-only: the digest changes nothing — no status updates, notes, or
reminders — unless I ask as a follow-up. Never invent ticket numbers, SLA times,
or client replies; if last-activity data is ambiguous, put the ticket in the safer
bucket (Needs your reply) rather than hiding it in Waiting. Keep the whole thing
skimmable — if it doesn't fit on one screen, tighten the lines, never pad.
```
