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
Recurring maintenance is a promise on a schedule, usually contractual. Two failure modes
eat it: cycles closed with a bare "done" (no evidence the work happened), and cycles that
silently never open. Audit both — evidence per cycle, continuity across cycles.

1. Identify the recurring series in scope: search for the maintenance tickets over
   the audit window (by title pattern, board, or type — recurring series are usually
   recognizable by repeated titles on a cadence). Group tickets into their series (same
   title pattern + client).

2. PER-CYCLE EVIDENCE CHECK — for each closed cycle, grade the completion evidence:
   - STRONG: specific findings recorded (what was checked, what was found, values/counts —
     "verified last 30 backup jobs, 2 failures remediated, ticket <ref>"), plus time
     logged consistent with the work.
   - WEAK: a generic completion phrase that would be identical every month ("maintenance
     completed, all good") with time logged. Interchangeable notes across cycles are the
     signature of checkbox theater — flag when a series' last N closure notes are
     near-identical.
   - NONE: closed with no note or a bare status flip. Grade it NONE and say so; a closed
     ticket proves closure, not maintenance.
   Ticket data can prove documentation, not work — the grades are about evidence, and the
   report says exactly that.

3. CORROBORATE where possible: when the maintenance touches RMM-managed devices and
   NinjaOne is enabled, check the RMM's device activity history for
   actions consistent with the claimed window (patch events, reboots, maintenance mode).
   Corroboration upgrades confidence; its absence is noted, not damning. Skip gracefully
   when no RMM is connected.

4. SKIPPED-CYCLE CHECK — the continuity audit: from each series' cadence, verify a ticket
   exists for every expected cycle in the window. Missing cycle → flag with the
   last-completed date. Also catch the degraded forms: cycles opened but never touched, and
   cycles closed the same minute they opened.

5. Report per series: cycles expected / opened / closed, evidence grades, corroboration
   results, skipped cycles, and a trend call (healthy / degrading / theater). Route
   findings: weak-evidence habits to the lead as coaching data; skipped cycles to whoever
   owns the schedule (and if the series comes from a broken automation, say so — the fix is
   the generator, not the tech).

6. On request, post a plain-text audit note on each flagged ticket stating what evidence is
   missing, so the assigned tech can remediate the record while memory is fresh.

Guardrails: honesty about proof limits is the core — closed ≠ done, a note ≠ the work, and
the report never claims maintenance "happened," it grades the evidence that it did. Never
backfill or upgrade evidence on anyone's behalf. Do not reopen or close tickets in the audit
pass — findings are notes and reports; state changes are the owner's call. Identical-note
detection is a flag, not a verdict — the tech gets asked, not accused. Result-cap honesty:
capped searches mean possible missed cycles are reported as "unable to verify," not
"skipped."

Running unattended (Flows): trigger on a recurring maintenance ticket transitioning to
closed. Grade the closing evidence per step 2. STRONG or WEAK-with-time-logged → do nothing
(no note, no reply). NONE (no closure note, or closed within minutes of opening with no time
logged) → the entire reply is one plain-text internal note: "Maintenance closure check:
this recurring ticket was closed without completion evidence (no findings note / no time
entry). Please add what was checked and found, per the maintenance standard." Nothing else.
Never reopen the ticket, never change status, never message the client. When series
membership or the evidence grade is ambiguous, do nothing. Do not post if an identical
evidence-check note already exists.
```
