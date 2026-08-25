---
name: Recurring Maintenance Tickets
description: Verify scheduled maintenance tickets (backup checks, patch cycles, monthly server reviews) carry real completion evidence and flag skipped cycles fast.
category: Change & Problem Management
tools: [search_tickets, add_ticket_note, update_ticket, get_ninjaone_device_activities]
connectors: [NinjaOne]
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Recurring Maintenance Tickets

**When to use:** "Audit last month's maintenance tickets / did the monthly server maintenance actually happen?" / a periodic hygiene sweep over all recurring maintenance series / before a client review where maintenance delivery will be claimed / a recurring ticket closed suspiciously fast that a lead wants checked.

**Run it:** on one maintenance ticket · across a recurring series · or as a Flow (triggered when a recurring maintenance ticket is closed).

## Prompt

```
Recurring maintenance is a contractual promise. Two failure modes eat it: cycles closed
with a bare "done", and cycles that never open. Audit both.

1. Find the series in scope: search the maintenance tickets over the audit window (title
   pattern, board, or type); group them by title pattern plus client.

2. PER-CYCLE EVIDENCE — grade each closed cycle. Ticket data proves documentation, not
   work: you grade the evidence, you do not certify that maintenance happened; say so in
   the report.
   - STRONG: specific findings, plus time logged consistent with the work — "verified last
     30 backup jobs, 2 failures remediated, ticket <ref>".
   - WEAK: a generic phrase that would read identically every cycle ("maintenance
     completed, all good") with time logged. Flag a series whose last few closure notes
     are near-identical — interchangeable notes are checkbox theater.
   - NONE: closed with no note, or a bare status flip.

3. CORROBORATE where the work touched RMM-managed devices and NinjaOne is connected: check
   device activity for actions matching the claimed window (patch events, reboots,
   maintenance mode). Absence is noted, not damning; with no RMM, skip and say so.

4. SKIPPED-CYCLE CHECK: from each series' cadence, verify a ticket exists for every
   expected cycle. Missing cycle -> flag it with the last-completed date. The degraded
   forms count as misses too: opened but never touched, closed the minute it opened.

5. Report per series: cycles expected / opened / closed, evidence grades, corroboration,
   skipped cycles, and a trend call (healthy / degrading / theater). Route weak-evidence
   habits to the lead, skipped cycles to the schedule owner; a series from a broken
   automation is a generator problem, not a tech problem. On request, leave an audit note
   on each flagged ticket naming the missing evidence (apply the PSA Note Discipline base
   skill — plain text, no markdown or emojis).

Guardrails: never backfill or upgrade evidence for anyone. Do not reopen or close tickets
in the audit pass — state changes are the owner's call. Identical-note detection is a
flag, not a verdict: the tech gets asked, not accused. Apply the Sweep Honesty base skill
— if a search may have capped, unverified cycles are "unable to verify", never "skipped".

As a Flow, triggered when a maintenance ticket is closed: grade the closing evidence per
step 2. STRONG, or WEAK with time logged -> do nothing. NONE (no closure note, or closed
minutes after opening with no time entry) -> your entire reply is one plain-text internal
note: "Maintenance closure check: closed without completion evidence (no findings note /
no time entry). Please add what was checked and found, per the maintenance standard."
Never reopen, never change status, never message the client. If series membership or the
grade is ambiguous, or an identical note exists, do nothing.
```
