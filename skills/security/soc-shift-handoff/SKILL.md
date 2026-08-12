---
name: SOC Shift Handoff
description: Security-desk shift change with investigations in flight — hand off open security work with evidence state, containment-in-progress status, and watch items, so the incoming shift can act in minute one without re-deriving anyone's reasoning.
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
Specialize the shift handoff for security work, where the handoff cost is different: a
dropped ticket ages, but a dropped containment step or an un-passed watch item is how an
attacker gets their quiet hours. General open-queue items still go through the standard
shift-handoff skill; this covers the security board's extra freight. Work it in order:

1. Pull the security board's open work (result-cap honesty — a capped pull is disclosed,
   never presented as the full board). Order the handoff by operational urgency: active
   containment first, live investigations second, pending verdicts third, watch items last.
2. Active containment in progress — the section that can't be wrong: for each incident
   mid-containment, state exactly which checklist steps are DONE (with timestamps, from the
   running containment note) and which are NOT — "sign-in blocked and sessions revoked at
   <time>; password reset NOT yet done; MFA sweep NOT started." Name the single next action,
   its owner on the incoming shift, and any pending callback (client authority approval, IR
   firm, provider). An ambiguous containment state gets re-verified by the incoming shift
   before anything else — assume nothing.
3. Open investigations with evidence state: per investigation — current hypothesis and
   confidence, evidence collected so far and where it lives (which notes, which exports),
   evidence still outstanding and who owes it, and what would change the verdict. The
   incoming analyst should be able to resume the reasoning, not restart it.
4. Watch items — the security-specific category: things that are not tickets yet but the next
   shift must keep peripheral vision on ("expect follow-up alerts from <client>'s tuning
   change," "second failed-MFA cluster on <user> would upgrade ticket <ref> to containment,"
   "baseline-noise period for <client>'s new MDR — verify everything anyway"). Each with the
   trigger condition and the action it should trigger.
5. Time-critical header: anything with a clock — response-tier deadlines approaching,
   promised client updates due (with the committed time), scheduled containment reversals or
   account re-enables, and log-retention expiries threatening evidence (preserve-before
   dates).
6. Deliver as the one-pager in chat plus a plain-text handoff note on each active-containment
   and investigation ticket, so the state travels with the ticket even if the one-pager
   doesn't. Confirm the receiving shift or named member has acknowledged the
   active-containment items specifically — those are handed to a person, not to a queue.

Guardrails — always:
- Containment state is never summarized loosely: done-with-timestamp or explicitly-not-done,
  per step — "mostly contained" has no meaning and no place here.
- Evidence chain continuity: where evidence lives and what's outstanding transfers
  explicitly; an investigation whose evidence state can't be stated gets flagged as at-risk.
- Watch items must carry trigger + action, or they're trivia; the incoming shift verifies
  rather than trusts any ambiguous state.
- Active containments are acknowledged by a named person before the outgoing shift leaves —
  silence is not a handoff.
- Never omit an item to keep the page short; security handoffs prioritize completeness of the
  critical sections over the one-minute read target of the general skill.
- Verdict-affecting context (documented benign patterns, simulation campaigns in flight,
  pen-test windows) is handed forward — closing a real alert because nobody said the context
  expired is a handoff failure. Never invent timestamps or evidence state.
```
