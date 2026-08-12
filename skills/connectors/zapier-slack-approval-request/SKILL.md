---
name: Zapier Slack Approval Request
description: Use Slack "Request Approval" as the human-in-the-loop gate before privileged or irreversible actions when the desk lives in Slack rather than Teams — named approver, explicit approve/reject, silence means no. Use when a workflow needs real sign-off delivered in Slack.
category: Connectors
tools: [search_tickets, add_ticket_note, update_ticket, send_approval]
connectors: [Zapier: Slack]
scope: single
flow: no
role: [Service & Ops Manager, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Zapier Slack Approval Request

**When to use:** Offboarding, admin changes, or out-of-contract spend needing sign-off in a Slack-first shop, where the approver will actually answer in Slack.

**Run it:** on one ticket.

## Prompt

```
The Slack twin of the Teams approval gate — same pattern, different surface: put an approve/reject
decision in front of a named approver in Slack, and run the privileged action only on an explicit
approve, with the outcome recorded on the ticket either way.

This runs only if the member has connected Zapier with Slack. If it's absent, degrade to Thread's
native approval request, or stop and tell the member no approval channel is available — never skip
the gate because the tool is missing. Each Zapier call = 2 Zapier tasks.

1. Name the gated action precisely: what will happen, to whom/what, and its reversibility. A vague
   approval approves nothing.
2. Resolve the approver from the ticket/contact record or tenant policy — never from who's online in
   Slack. Wrong approver = no gate at all.
3. Compose the request so it's decidable from the message alone: exact action, subject (<user>,
   <system>), source ticket reference, any cost. Include a respond-by expectation if time-boxed.
4. Show me the request + approver, wait for confirmation, then send the approval request in Slack.
5. Branch strictly on the response:
   - Approved → proceed; leave a note (plain text): what was approved, by whom, when, via Slack
     approval.
   - Rejected → do NOT proceed; note the rejection and route the ticket back to the requester/member.
   - Timeout / no response / ambiguous reply → treat exactly as not-approved. Silence is a no; so is
     "approved" from anyone other than the designated approver, and so is a 👍 on some other message.
6. One approval covers one action — no batching unless the member explicitly defines the batch in the
   request text. Record completion separately after the approved action finishes; the approval record
   is mandatory, plain text, and audit-grade (action, approver, timestamp, channel). Re-request only
   after a real timeout. On any uncertainty about approver identity or scope, stop and do nothing.
```
