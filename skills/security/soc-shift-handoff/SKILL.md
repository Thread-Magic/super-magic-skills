---
name: SOC Shift Handoff
description: Hand off open security investigations at shift change: evidence state, containment progress, and watch items so the next shift can act immediately.
category: Security
tools: [search_tickets, search_members, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Security & Compliance Owner, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# SOC Shift Handoff

**When to use:** Shift change on a security/SOC board with open investigations or active incidents; an incident spans shifts and the responder is rotating out mid-containment; or a security lead wants the overnight picture before the day shift takes over.

**Run it:** across the security board's open work (a shift handoff).

## Prompt

```
A dropped ticket ages; a dropped containment step or an un-passed watch item is how an
attacker gets their quiet hours. General open-queue items still go through the shift-handoff
skill — this covers the security board's extra freight.

1. Pull the security board's open work, disclosing a capped pull rather than presenting it as
   the full board (Sweep Honesty base skill). Order by operational urgency: active
   containment, then live investigations, then pending verdicts, then watch items.
2. Active containment is the section that can't be wrong. For each incident mid-containment,
   state which checklist steps are DONE, with timestamps from the running containment note,
   and which are NOT: "sign-in blocked and sessions revoked at <time>; password reset NOT yet
   done; MFA sweep NOT started." Name the single next action, its owner on the incoming shift,
   and any pending callback — client authority approval, IR firm, provider. An ambiguous
   containment state is re-verified by the incoming shift before anything else.
3. Open investigations travel with their evidence state: current hypothesis and confidence,
   evidence collected and where it lives (which notes, which exports), evidence still
   outstanding and who owes it, and what would change the verdict. The incoming analyst should
   resume the reasoning, not restart it.
4. Watch items aren't tickets yet, but the next shift keeps peripheral vision on them: "expect follow-up alerts from <client>'s tuning change", "a
   second failed-MFA cluster on <user> upgrades ticket <ref> to containment", "baseline-noise
   period for <client>'s new MDR — verify everything anyway". Each needs a trigger and the action it
   triggers, or it's trivia.
5. Head the page with anything on a clock: approaching response-tier deadlines, promised client
   updates with committed times, scheduled containment reversals or account re-enables,
   and log-retention expiries that threaten evidence.
6. Deliver the one-pager in chat plus a plain-text handoff note on each active-containment and
   investigation ticket, so the state travels with the ticket. Confirm that the receiving shift
   or a named member has acknowledged the active-containment items specifically — those are
   handed to a person, not to a queue. Silence is not a handoff.

Containment state is never summarized loosely: done-with-timestamp or explicitly-not-done, per
step — "mostly contained" has no meaning here. An investigation whose evidence state can't be
stated is flagged at-risk. Never omit an item to keep the page short; completeness of the
critical sections beats the one-minute read. Hand forward verdict-affecting context —
documented benign patterns, simulation campaigns in flight, pen-test windows ; closing a real alert
when nobody said the context expired is a handoff failure. Never invent timestamps
or evidence state.
```
