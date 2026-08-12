---
name: Zapier Teams Approval Gate
description: Use Teams "Send Approval Request and Wait" as the human-in-the-loop gate before privileged or irreversible actions — offboarding, admin changes, out-of-contract spend. Use when a workflow needs a real named-human sign-off in Teams before proceeding.
category: Connectors
tools: [search_tickets, add_ticket_note, update_ticket, send_approval]
connectors: [Zapier: Microsoft Teams]
scope: single
flow: no
role: [Service & Ops Manager, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Zapier Teams Approval Gate

**When to use:** Offboarding steps that disable an account or forward a mailbox, or any client-billable / out-of-contract work the desk wants signed off in Teams before it's performed.

**Run it:** on one ticket.

## Prompt

```
A hard stop with a paper trail: put an approve/reject card in front of a named approver in Teams and
block until they answer. The privileged action happens only on an explicit approve — and the outcome
lands on the ticket either way.

This runs only if the member (or admin) has connected Zapier with a Teams account. If it's absent,
degrade to Thread's native approval request, or stop and tell the member no approval channel is
available — never skip the gate because the tool is missing. Each Zapier call = 2 Zapier tasks.

1. Name the gated action precisely: what will happen, to whom/what, and its reversibility. A vague
   approval approves nothing.
2. Resolve the approver: the client's authorized contact or internal manager per the tenant's
   policy — from the ticket/contact record, never from who happens to be online. Wrong approver =
   no gate at all.
3. Compose the request: exact action, subject (<user>, <system>), source ticket reference, any
   cost. It must be decidable from the card alone.
4. Show me the request + approver, wait for confirmation, then send the approve-and-wait card in
   Teams.
5. Branch strictly on the response:
   - Approved → proceed with the gated action; leave a note (plain text): what was approved, by
     whom, when, via Teams approval.
   - Rejected → do NOT proceed; note the rejection and route the ticket back to the requester/member.
   - Timeout / no response / ambiguous reply → treat exactly as not-approved. Silence is a no. Note
     the non-response; re-request only after a genuine timeout, never on every check-in.
6. One approval covers one action — never batch ten offboardings under one card unless the member
   explicitly defines the batch. Record completion separately after the approved action finishes;
   approval received and action done are two different facts and two different notes (audit-grade,
   plain text). On any uncertainty about approver identity or scope, stop and do nothing.
```
