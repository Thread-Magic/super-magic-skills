---
name: Status Check Intent Design
description: Design the "any update on my ticket?" intent: answer from real ticket status and last client-visible update, escalating only when the trail has gone cold.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Status Check Intent Design

**When to use:** "Build an intent for ticket status questions" / "techs get interrupted all day by 'any update?' messages" / Intent Mining shows update-requests as one of the biggest non-issue conversation types.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a status-check intent that turns "any update?" into a self-served answer: identify which
ticket, read its real status and the last client-visible update, and reply with that — pinging
a human only when the ticket is genuinely stale or the user rejects the answer. Building
intents is admin-only; if you can't, output the complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "any update on my ticket", "status of my
  ticket", "any news on", "has anyone looked at my request", "is my ticket being worked on",
  "following up on my ticket", "checking in on the issue I reported", "when will my ticket be
  fixed", "still waiting on", "ticket number <ticket> update". Near-miss watch: "any update?"
  inside an active ticket thread is conversation, not a new intent match; a follow-up that
  adds new symptoms should append to the ticket, not just report status.
- Arguments (identification): ticket number if they have it, otherwise enough to find it
  (roughly what it was about and when reported); if the requester has multiple open tickets
  and gave no number -> list their open tickets briefly and ask which; only the requester's
  own tickets (or their client's, per the client's visibility policy) — never resolve a status
  request against another contact's ticket.
- Reply flow (answer from the record): (1) locate the ticket by reading the requester's or
  their company's own tickets, strictly scoped; (2) reply with current status (translated
  to plain language — "Scheduled", not an internal code), the last client-visible update and
  its date, and the next expected step if recorded; (3) client-visible ONLY — never surface
  internal notes, tech names in blame-able contexts, or internal discussions; (4) if the
  ticket is waiting on the user, say so plainly and restate what is needed; (5) staleness
  branch — if there has been no client-visible activity beyond the desk's freshness threshold
  (admin-set, e.g. several business days), add a note to the ticket flagging the client asked
  for an update and the ticket appears stale, and tell the user the desk has been nudged; (6)
  if the user pushes back or expresses escalation-level frustration -> route to the human
  escalation path with the conversation attached; never argue the status.
- Handoff rule: the intent reports and nudges; it never changes priority, promises resolution
  dates, or reopens/closes tickets. Frustrated users get a human.
- Variation hooks (per client): status-name translations, freshness threshold, whether
  contacts may see all their company's tickets or only their own, escalation contact/path.
- Success metric: deflection rate on status conversations and reduction in tech interruptions;
  counter-metric: escalations that started as status checks.

Steps:
1. List the existing intents — check for an existing status/update intent; prefer updating.
2. Search recent "any update"-type notes and tickets; mine phrasing for triggers
   and measure how often the honest answer would be "waiting on you" vs "genuinely stale"
   (calibrates the freshness threshold with real data).
3. Agree the freshness threshold and visibility policy with the admin — these two decisions
   define the intent's behavior.
4. Draft the full spec (triggers, identification arguments, answer template, staleness branch,
   escalation branch, variations) plus a test plan (5 should-match, 3–5 should-not: in-thread
   follow-up and new-symptom near-misses). Show before any write.
5. On explicit confirmation: create the intent, then set its variations.
6. Report what was created, restate the test plan, recommend activation after tests pass. Do
   NOT activate.

Guardrails: client-visible information only — internal notes, private discussions, and status
jargon never appear in replies. Strict requester scoping: never return status for tickets the
asking contact is not entitled to see; when identification is ambiguous, ask, don't guess. No
promises: no resolution dates, no "shortly", no priority changes — the staleness nudge is a
plain-text note on the ticket, not a priority escalation. Confirm before any write.
```
