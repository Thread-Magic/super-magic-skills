---
name: Tech Morning Ritual
description: A technician's 15-minute start-of-day runbook: digest, schedule check, easy-win pick, and a first-response sweep before diving into ticket work.
category: Role Rituals
tools: [search_tickets, search_members, list_boards]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Tech Morning Ritual

**When to use:** "Start my day" / "what should I work on today" / "run my morning ritual" — a tech logging in who wants the queue pre-digested before the huddle.

**Run it:** across your own queue and accounts — run it manually (not a Flow; Flows can't schedule a morning cadence).

## Prompt

```
You are running my morning ritual as a chain of existing skills, in a fixed sequence. Scope everything strictly to MY own queue and MY accounts — do not read or act on other members' tickets. Time-box the whole ritual to ~15 minutes. Propose, don't apply: show me everything before you change or send anything, and when in doubt, do nothing.

Run these skills IN ORDER:
(1) Run the personal-productivity/daily-digest skill: my open tickets, what needs replies, anything urgent, overnight arrivals on my queue. If a live P1 is in my queue, STOP the ritual here and point me at the P1 — the ritual serves me, not the reverse.
(2) Schedule check (~2 min): check today's scheduled ticket work and appointments; if my calendar connector is available use it, otherwise ask me to confirm my blocks and note that the calendar step degraded. Flag any collision between scheduled work and urgent items from step 1.
(3) Run the personal-productivity/easy-win-finder skill and pick exactly ONE quick-close candidate to do before lunch. One, not a list.
(4) First-response sweep: from the digest, isolate tickets in MY queue with a client message and no tech reply yet, oldest first. For each, either draft the reply with the communication/client-reply skill (drafts only — do not send without my explicit confirmation) or explicitly defer it with a reason.
(5) Commit: output the ritual card with today's calendar conflicts (if any), the one easy win, the first-response list with what was drafted or deferred, and the single named "first move" I start with right now.

Time-short version (I have under 5 minutes): run only step 1 (digest), step 4 (first-response sweep — client silence compounds fastest), and the one-line first move. Skip easy-win and calendar and mark them "skipped: time".

Guardrails, all inline:
- Skip-with-note beats fake completion: any skipped step appears in the output as "skipped: <reason>", never silently dropped.
- Disclose result caps: if a queue search may have truncated, say so in the card rather than presenting a partial list as complete.
- Never invent tickets, ticket numbers, links, or client details — report only what the searches return.
- This is a read; do not create tickets or notes as a side effect. The only writes are client replies I have confirmed.
- If a chained skill's connector (e.g. calendar) is unavailable for this tenant, note the degradation and continue with the rest.
- Any note or reply that may sync to the PSA is plain text — no markdown, no emojis.
```
