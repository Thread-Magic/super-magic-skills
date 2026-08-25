---
name: Morning Briefing
description: A start-of-day briefing across your tiered support boards — every open human ticket grouped and flagged (unassigned, aging, SLA risk), with the alert/automation noise filtered out, a quick-stats table per board, and the day's key follow-up actions, all in one scannable report.
category: Scheduling & Dispatch
tools: [search_tickets, list_boards, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Morning Briefing

**When to use:** Start of the day or shift — a dispatcher or team lead wants one clean, scannable picture of every open ticket across the desk's support tiers, the monitoring/alert noise stripped out, and the day's priorities called out.

**Run it:** across all open tickets on your support boards, on demand each morning.

## Prompt

```
Produce a morning briefing of open work across the desk's support boards — filtered, grouped and
flagged. Format it richly in markdown. The first character of your reply is the "🌅 Morning
Briefing" header — no preamble.

PULL
Open tickets on the first-line (Tier 1) and second-line (Tier 2) support boards, plus tickets in
a scheduled status. If it isn't obvious which boards those are, list them and ask — don't guess.
Search generously; say so if a search may have capped.

FILTER — first-line board only; second-line includes ALL open tickets
Exclude what isn't human work: alert, monitoring, security-automation and rules-engine tickets,
and anything an RMM, monitoring, security or backup platform generated (by type, originating
board, or sender — noreply@, no-reply@, a service address); "Unknown" client or contact; anything
flagged for deletion. Keep human-raised work — hardware, software, printing, installs,
onboarding, access requests, email, network. When unsure, keep it.

READ MESSAGES ONLY WHERE IT PAYS
On hold, waiting on vendor or parts, and scheduled: the latest internal note gives Next Steps.
Customer-updated: the latest customer message gives the Customer Update line. Otherwise use what
you have.

FLAGS
Last updated as an age — "5h ago", "3d ago". SLA: 🔴 breached, 🟠 within about 2 hours; with no
SLA timer to read, fall back on age by priority — Critical/High 🟠 4h+, 🔴 8h+; Medium 🟠 2d+,
🔴 4d+; Low 🟠 5d+. Also 🚨 unassigned and ⚠️ created 3+ days ago. Nothing else gets a flag.

OUTPUT
Open with "### 🌅 Morning Briefing — [today's date]", then "#### 📅 Scheduled Today" listing
today's scheduled tickets.

One section per board, first-line then second-line, each grouped into these buckets in order:
🚨 Needs Attention (unassigned or High/Critical) · 🟡 Waiting on Customer · 🔵 On Hold (on hold,
vendor or parts) · 🟢 In Progress / Completed (in progress, acknowledged, customer-updated,
completed) · 📅 Scheduled (future) — never folded into In Progress. Lead the first-line section
with the count of human tickets left after filtering.

Render each ticket as a one-row table — Ticket# (flags, linked) · Client · Status · Assignee ·
Last Updated — then a "↳" line summarizing it in 6-10 words. Add a bold "Customer Update:" line
only on customer-updated tickets, a bold "📌 Next Steps:" line only on on-hold and scheduled ones.

Close with "#### 🔢 Quick Stats", one row per board (Open · Needs Attention · Waiting Customer ·
On Hold · Scheduled · 🔴 SLA Breach · 🟠 SLA Warning), then "#### Key actions for today": the top
follow-ups as bullets, each starting 📞 (follow-up or call) or 🚨 (unassigned, needs an owner),
the responsible tech in bold, what must happen in a few words, and the linked ticket. Focus on
unassigned, High/Critical, and anything time-sensitive.

Link each ticket to its real URL — never invent one. Report only what the tickets show; never
fabricate.
```
