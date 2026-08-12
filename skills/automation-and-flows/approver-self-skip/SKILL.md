---
name: Approver Self-Skip
description: Before firing an approval, check whether the ticket submitter IS the designated approver for that client — if so, skip send_approval and advance the ticket with an audit note instead of making an approver approve their own request. Answers the "don't ask the approver to approve themselves" workflow.
category: Automation & Flows
tools: [search_contacts, send_approval, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Approver Self-Skip

**When to use:** A flow reaches its send-approval step and the desk wants self-submitted requests from approvers to pass straight through; the client's office manager (the designated approver) files a request and shouldn't have to approve their own ticket; any approval-gated intake where approvers are also frequent requesters. A deterministic pre-check that wraps new-ticket-approval-gate / change-approval-sender. Runs at the flow's send-approval step — never on a timer.

**Run it:** on one ticket · or as a Flow (triggered at the approval step, on ticket create or status change into the approval stage).

## Prompt

```
When the person who submitted the ticket is the client's designated approver, sending them
an approval request is pure friction. Detect the self-approval case from the contact record,
skip the send, and advance the ticket with an audit note. The skip is the exception; sending
is the default.

Your entire reply is posted verbatim as the internal note — plain text, no narration, no
markdown. Exactly three outcomes: (a) exact match -> skip, advance status, audit note; (b) no
match -> send the approval as configured, one-line note; (c) unresolved -> no send, no status
change, note "Approver unresolved for <client>; approval not sent; needs human." Never
advance status without the audit note; never send AND skip.

1. Resolve the ticket's submitter contact and the client's designated approver(s) by looking
   up the contacts for this client carrying the desk's approver contact type/label.

2. Compare identities FROM THE CONTACT RECORDS ONLY: the submitter is the approver iff their
   contact record matches an approver contact (same contact ID, or same verified email on the
   contact record). Name similarity, email display names, or "probably the same person" do
   NOT count. If the submitter arrived via an unverified channel (plain email with no matched
   contact), always send the approval.

3. Match -> skip the approval. Advance the ticket out of the approval-waiting status (resolve
   the desk's configured post-approval status first) and leave a plain-text audit note:
   "Approval auto-skipped: submitter <contact> is the designated approver for <client>
   (contact-type match). No approval request sent." Always leave this note — a silently
   advanced ticket looks like a missed gate in QA.

4. No match, or cannot resolve -> send the approval normally to the
   designated approver. If you cannot resolve the approver contact type for this
   client, do not guess — send to nobody, leave a note that the approver is unresolved, and
   stop.

The skip is deterministic, not judgment-based: exact contact match -> skip; anything else ->
send. There is no "close enough". If the client has multiple designated approvers, the
submitter must match one exactly. Never skip approvals the desk marked as always-required
(e.g. spend above a threshold, offboarding) even for self-submitted tickets.
```
