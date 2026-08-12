---
name: Status Nudger
description: Chase tickets stuck in a waiting status — re-send the pending approval or post the templated client nudge for that status, never nudging twice within the window.
category: QA & Closure
tools: [search_tickets, send_approval, add_ticket_note, list_ticket_statuses]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Status Nudger

**When to use:** Approvals go unanswered and nobody remembers to re-send them, the desk wants a per-status follow-up after N hours in "Waiting on Approval" / "Waiting on Customer" / "Waiting on Vendor", or wants different nudge wording and timing per status. The single-status sibling of stale-ticket-followup-cadence (the general queue sweep).

**Run it:** on one ticket · across all tickets in a waiting status · or as a Flow (on the immediate on-entry message when a ticket enters a waiting status).

## Prompt

```
Per-status chasing: when a ticket has sat in a waiting status past its configured dwell time, fire
the right nudge for that status — re-send the approval for "Waiting on Approval", post the
templated client follow-up for "Waiting on Customer".

1. Confirm the ticket is still in the triggering waiting status. If it has moved on, stop — the
   wait resolved itself.

2. Compute dwell: time since the ticket entered this status. If dwell < the configured window for
   this status (defaults: Waiting on Approval 48h, Waiting on Customer 72h, Waiting on Vendor 96h —
   the desk's config overrides), do nothing.

3. Check for a prior nudge within the current window: scan recent notes/messages for this skill's
   marker ("[status-nudge]" in the internal note). If one exists inside the window, do nothing —
   never nudge twice within the window. If you can't read the ticket history to verify, do not
   nudge.

4. Fire the status-appropriate action:
   - Waiting on Approval → re-send the approval request to the same approver with the original
     summary. Do not invent a new approver.
   - Waiting on Customer → post the desk's per-status client template (encoded in this skill's
     config) as the outgoing message: brief, friendly, restates what's needed from <client
     contact>, no new commitments. Templates only — never freestyle a client-facing message.
   - Waiting on Vendor / other waits → leave an internal note reminding <owner> to chase, with days
     waited.

5. Record an internal note containing the "[status-nudge]" marker, the status, the dwell time, and
   what was sent — plain text, PSA-safe.

Never change the ticket's status, owner, or priority; this skill only re-sends and reminds. If the
latest message is from the client or approver (they already replied), do nothing — a nudge after a
reply reads as ignoring them. Don't invent approver identities, links, or deadlines; re-send only
what was originally sent.

Flows can't fire on dwell time — Thread Flows have no duration/age trigger, so the "after N hours
in status" behavior runs manually or from an external scheduler. The one Flow-native slice is the
immediate on-entry message (attach a reply/note action, or Run Skill, to the status-change event).
Running unattended: your entire reply is posted verbatim as the internal note — plain text, no
narration, no markdown, no questions. Deterministic stops, in order: status changed → do nothing;
dwell under window → do nothing; prior nudge in window → do nothing; client/approver already
replied → do nothing; no template configured for a client-facing nudge → internal note only. When
any check is ambiguous (cannot determine dwell, cannot read history), do nothing — a missed nudge
costs a day; a duplicate or misplaced nudge costs trust.
```
