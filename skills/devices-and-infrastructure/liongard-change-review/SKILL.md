---
name: Liongard Change Review
description: Answer "what changed recently" from Liongard detections and timelines, correlating environment changes with new tickets after breakage or incidents.
category: Devices & Infrastructure
tools: [liongard_environment, liongard_detection, liongard_timeline, liongard_events, liongard_alert, search_tickets, add_ticket_note]
connectors: [Liongard]
scope: global
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Liongard Change Review

**When to use:** "Something broke at <client> this week — what changed?", incident investigation over a time window, or a periodic per-client change review.

**Run it:** across a client's whole environment over a window, on demand (not a Flow — it's a change-awareness sweep, not a per-ticket event).

## Prompt

```
Pull the change history Liongard's inspectors detected across a client's environment and line it up against tickets that appeared around the same time. Requires Liongard; if not enabled, say change detection is unavailable and degrade to ticket-history inference, clearly labeled as such.

1. Resolve the client to a Liongard environment; rank name matches and state your pick.
2. Fix the window: the requester's incident window plus padding (start 48-72h before the first symptom — changes precede symptoms), or default to the last 14 days for a periodic review.
3. Read the environment's posture in Liongard: its detected changes, the system-by-system timeline, and anything the inspectors escalated as events or alerts. Flag result caps and narrow by system or sub-window rather than trusting a truncated list.
4. Sort changes by risk relevance, highest first: identity/admin changes (new admin accounts, permission grants, MFA changes), security config (firewall rules, conditional access, DNS records), infrastructure (server roles, services, storage), licensing/subscription shifts, then routine churn. Note which system each came from and when.
5. Correlate with tickets: read the client's ticket history over the same window. Line up ticket open times against change times — a cluster of "can't log in" tickets hours after a conditional-access change is a lead. Present correlations as time-adjacency, not proven causation, and say which direction the evidence points.
6. Check the inverse: high-risk changes with NO corresponding ticket or documented work order deserve a flag of their own — an undocumented admin-account creation is a finding even when nothing is broken.
7. Output: the change list ranked by relevance (system, change, when, detected by), ticket correlations with strength, unexplained high-risk changes called out, recommended follow-ups. Offer a plain-text note (no markdown/emojis).

Guardrails: time-adjacency is not causation — every correlation is labeled with its strength; never assert "this change caused the outage" without corroborating evidence. Defensive writing on identity/security findings: an undocumented admin account is "unexplained — verify", never "breach"/"compromise" unconfirmed. Liongard sees only what its inspectors inspect — name the systems covered so absence of a detected change is not read as absence of change. Read-only — it reports and recommends; reverting changes is human-owned.
```
