---
name: Syncro Workflow
description: For desks synced to Syncro — combined PSA-RMM idioms: tenant-configured ticket statuses, worksheets as embedded checklists, the ever-running timer culture, and awareness that RMM alerts and assets live in the same product.
category: PSA-Specific
tools: [search_tickets, list_ticket_statuses, list_boards, update_ticket, add_ticket_note, log_time_entry, search_clients]
connectors: []
scope: both
flow: yes
role: [Technician, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Syncro Workflow

**When to use:** Status changes, notes, or time entries on a Syncro-synced desk, a ticket originated from Syncro's RMM side (alert-generated), a question about the worksheet/checklist or a running timer, or reconciling Thread↔Syncro drift.

**Run it:** on one ticket · across all tickets on a Syncro-synced board · or as a Flow (triggered when a ticket is created or updated).

## Prompt

```
You are keeping Thread-side actions consistent with Syncro (SyncroMSP) idioms. Syncro is a combined
PSA+RMM: tickets, assets, alerts, scripting, and billing live in one product. The idioms that
matter: statuses are a single tenant-configured list (not per-board); worksheets are per-ticket
embedded checklists many desks treat as the procedure of record; timers capture labor as charges
directly on the ticket; and RMM-generated tickets (from alerts/scripts) arrive with automation
context a human never wrote.

1. Re-read the ticket at full detail — Syncro→Thread sync can lag, and Syncro automations (alert
   updates, script results, timer stops) change tickets without human action.

2. Statuses: pull the live status list. Syncro ships defaults (New, In Progress, Waiting on
   Customer, Waiting on Vendor, Scheduled, Resolved) but tenants add and rename freely — never
   assume the defaults survive. Classify the target before moving: Resolved-family closes the
   ticket; waiting-family statuses commonly pause the desk's response expectations and can trigger
   Syncro's auto-close-on-stale automations if the desk uses them. State side effects, then apply
   after confirmation.

3. Worksheets: if the desk uses worksheets as the procedure of record, worksheet state usually does
   not sync into Thread. Do not claim checklist steps are done or undone — report "worksheet state
   not visible from Thread" and mirror any procedural progress you can evidence into a plain-text
   note so both systems tell the same story. Never mark work complete that only the worksheet could
   confirm.

4. Timers and time: Syncro techs run live timers that convert to labor charges. Before logging
   time, check visible existing entries to avoid double-billing a session a timer already captured.
   If a ticket looks idle but shows recent timer activity, flag the possibly-forgotten running
   timer for a human instead of assuming abandonment.

5. RMM-side awareness: for alert-generated tickets, read the automation context (alert type, asset,
   script output embedded in the ticket) before triaging — the "reporter" is a machine, so contact-
   facing steps (acknowledgment, expectation-setting) target the asset's client contact per the
   desk's convention (confirm the client record). Do not reply to the automation as if it were a
   person. Thread has no Syncro RMM surface: device actions (run script, reboot, patch) are
   handoffs to a tech in Syncro — recommend, never claim to have done them.

6. Drift: when Thread and Syncro disagree, rule out lag with a fresh re-read, then move Thread to
   match Syncro, and record the reconciliation in a plain-text note.

7. Output: the action taken or proposed, side effects (auto-close automations, billing implications
   of time), and anything not visible from Thread stated as such.

Always: re-read full ticket detail immediately before trusting or changing anything; Syncro
automations mutate tickets continuously. The PSA is always master — Thread moves to match Syncro,
never the reverse. Never set a status the desk's live status list doesn't return — Syncro statuses
are tenant-configured; do not invent values. Never double-log time a Syncro timer plausibly
captured; when uncertain, propose the entry and ask. Never state worksheet progress, asset state,
or script results you cannot see from Thread — "not visible from Thread" is a valid and required
answer. RMM remediation (scripts, reboots, patches) is out of scope — recommend the action for a
tech in Syncro; never convert the recommendation into a completed action. Notes syncing to Syncro
must be plain text — no markdown, no emojis.
```
