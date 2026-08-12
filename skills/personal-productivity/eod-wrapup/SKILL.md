---
name: End-of-Day Wrap-Up
description: A technician closing out their day — sweep my tickets for anything stale >24h, awaiting-client without a follow-up sent, status mismatches, and line up tomorrow's first moves.
category: Personal Productivity
tools: [search_tickets, add_ticket_note, update_ticket]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# End-of-Day Wrap-Up

**When to use:** "End of day wrap-up" / "close out my day" / "anything I forgot to follow up on before I leave?" — the end-of-shift hygiene sweep that catches what rots overnight and hands tomorrow-you a first move.

**Run it:** across your own open tickets — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are running my end-of-day wrap-up. Scope everything strictly to MY own open
tickets — never touch anyone else's.

1. Read my open tickets. If the result may be capped, say so plainly in the output —
   do not present a partial list as complete.

2. Run these four hygiene checks and report each as its own short section. If a
   section is clean, say "clean" in one word — do not pad.
   - Stale >24h: tickets with no activity from me in over 24 hours that are still
     mine to move. Give ticket, days quiet, suggested action.
   - Awaiting client, no follow-up sent: waiting-on-client tickets where the last
     outbound message predates the wait — the client may not know I'm waiting.
     Suggest a one-line follow-up for each.
   - Status mismatches: the thread says one thing, the status another (client
     replied but still shows waiting; work finished but not closed). State what the
     status should probably be. If the true state is ambiguous, flag it as "check
     this one" rather than proposing a change.
   - Missing wrap-up: tickets I worked today with no note or time entry recorded.
     Do NOT invent what I did — prompt me for it.

3. Present every proposed fix (follow-up text, corrected status, note to add) as one
   batch and ask once: "Apply these?" Do nothing destructive until I confirm.

4. Only after I confirm, apply approved fixes: leave the notes for follow-ups and
   wrap-up notes, and change the status for the mismatches. Keep any note plain text —
   no markdown, no emojis (it may sync to a PSA). Record only what was done; never
   convert a plan or recommendation into a completed action. Never auto-send a
   client-facing follow-up.

5. Finish with "Tomorrow's first moves": the 2-3 tickets to open first tomorrow and
   why (longest-waiting, scheduled, breaches first), one line each.

Keep the whole thing skimmable — I'm trying to leave. When in doubt, do nothing and
flag it.
```
