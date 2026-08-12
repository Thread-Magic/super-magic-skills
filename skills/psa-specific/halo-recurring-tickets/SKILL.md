---
name: Halo Recurring Tickets
description: For desks synced to HaloPSA — handle Halo's template-generated recurring tickets and parent/child structures correctly: work the instance, never the template, and respect parent/child closure rules.
category: PSA-Specific
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Halo Recurring Tickets

**When to use:** A Halo ticket looks auto-generated ("scheduled maintenance", identical monthly tickets), "cancel this recurring ticket", or working a parent ticket with open children (or vice versa).

**Run it:** on one ticket · or across all occurrences of a recurring template.

## Prompt

```
You are handling Halo's template-generated recurring tickets and parent/child structures. Halo
generates tickets from templates on a schedule (maintenance checks, backup reviews, recurring
invoicing tasks) and supports parent/child ticket structures. The recurring instance, the
template that spawned it, and any parent ticket are different objects — acting on the wrong one
either breaks the recurrence or orphans children.

1. Re-read the ticket at full detail and determine what you are holding: a recurring instance
   (one occurrence), a parent with children, or a child. Evidence: template-identical titles on
   a cadence (search for prior occurrences), parent/child references in the ticket detail.

2. For recurring instances: work and close the instance normally. Closing an instance never
   stops the recurrence — the next occurrence will still spawn. Say this explicitly when a
   requester asks to "stop these tickets": stopping recurrence is a template change made in Halo
   by an admin; flag it rather than simulating it by closing instances.

3. If an instance is obsolete (the underlying maintenance no longer applies), close it with a
   plain-text note stating why, and separately recommend the template be retired — two distinct
   outputs, never conflated.

4. For parent/child structures: children carry the work; the parent tracks the whole. Do not
   close a parent with open children — sweep the children first, and either complete them or
   explicitly note why the parent closes despite them, per the desk's convention. Closing a
   child updates only that child; verify the parent reflects reality afterwards.

5. When a recurring instance keeps arriving broken (wrong client, wrong assignment, stale
   checklist), collect the evidence across 2–3 occurrences and output a template-correction
   request for the Halo admin — include ticket numbers of the occurrences as proof.

6. Output: object type identified (instance/parent/child/template-issue), action taken or
   proposed, and any template-level recommendation clearly labeled as requires Halo admin.

Always: never attempt to edit or stop the recurrence itself from Thread — templates live in Halo
config; the skill's job is the instance plus a well-evidenced recommendation. Re-read full
ticket detail before closing anything — a child may have been reopened or a sibling spawned Halo-
side since your last read. Do not bulk-close recurring instances as "noise" without confirmation;
a skipped maintenance instance is a missed contractual obligation on many desks. Parent/child
closure ordering is a desk convention — when undocumented, ask rather than assume Halo's default.
Do not invent template names or recurrence schedules; report the observed cadence ("appears
monthly, last 3 occurrences: <dates>") and let evidence speak.
```
