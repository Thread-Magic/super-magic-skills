---
name: Mail Flow Reports
description: Produce a periodic mail flow health summary for a client — volume trends, spam/malware catch rates, top senders and recipients, connector health, and forwarding anomalies — with flags on what changed since last period. Use for monthly/quarterly email health reviews or "is our mail filtering actually working" asks.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, log_time_entry, web_search]
connectors: [IT Glue]
scope: global
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Mail Flow Reports

**When to use:** A scheduled monthly/quarterly email health review for a client, "how much spam are we actually catching," a baseline capture before/after a filtering change (anti-spam-policy-tuning's verification window), or feeding the email section of a broader review (monthly-security-report owns the security-wide report; this skill owns mail flow depth). Read-only — this skill never changes policy; findings route to the owning skill as recommendations.

**Run it:** as an on-demand summary across the tenant's whole mail flow — read-only; findings route to the owning skill as recommendations (not a Flow: no schedule trigger).

## Prompt

```
You are producing a periodic mail flow health summary for a client. Read-only exercise: this skill never changes policy — findings route to the owning skill (anti-spam-policy-tuning, mail-forwarding-audit, email-connector-setup) as recommendations. The agent frames what to pull and reads what the tech pastes back. Never invent numbers; every figure carries its source report and period.

1. Define period and comparison baseline (this month vs last, or vs the same period prior). A number without a baseline is decoration; pull the prior report from the ticket history or state that this run establishes the baseline. Pull documented client context from the client's documentation (skip gracefully if IT Glue isn't connected) and the knowledge base.

2. Have the tech pull from the EAC / Defender reporting pages (portal names and locations shift — verify current report names against Microsoft's current docs):
   - Mailflow status: total inbound/outbound volume, and the split across good mail / spam / malware / phishing verdicts.
   - Threat protection status: catch counts by detection technology.
   - Top senders and recipients (and top spam recipients — repeat targets are a finding).
   - Connector report: volume per connector, TLS status, delivery failures (feeds email-connector-setup if a connector looks sick).
   - Auto-forwarded messages report (feeds mail-forwarding-audit if new external forwards appeared).
   - Queues / delayed delivery if the period had delivery complaints.
   PowerShell equivalents (`Get-MailTrafficATPReport`, `Get-MailFlowStatusReport` etc.) where the tech prefers export — verify against current module versions; some historical reporting cmdlets have been retired.

3. Compute the readable metrics: total volume and week-over-week trend; spam catch rate (filtered spam / (filtered spam + user-reported misses if tracked)); malware/phish counts; percentage of outbound from connectors vs mailboxes; count of external auto-forwards.

4. Flag anomalies against the baseline — each flag gets a recommended action, not just a highlight:
   - Volume spike (inbound: campaign or attack; outbound: possible compromised account or runaway app — check the top-sender identity; a single mailbox dominating outbound is a security check, not a footnote — treat as a possible compromise indicator and escalate).
   - Catch-rate drop or user-reported-spam rise → anti-spam-policy-tuning review.
   - New top sender that is a device/app → confirm it's a known connector (email-connector-setup), not an abuse path.
   - New external auto-forwards since last period → mail-forwarding-audit.
   - Connector failures/TLS downgrades → investigate before the LOB app owner notices.

5. Output two artifacts: (a) a plain-text ticket note with the metrics table, period comparison, flags and recommended actions, and where each number came from; (b) if the client gets a formatted report, keep the note as the source of record anyway. State any report caps or lookback limits (most portal reports cover ~90 days) rather than presenting a truncated window as the full period — if the portal only shows 90 days, don't report "the quarter" from 90 days minus a week. No client-to-client comparisons in the deliverable; each report stands on its own tenant's data. Log time.

When in doubt about a security-flavored anomaly, escalate rather than just charting it.
```
