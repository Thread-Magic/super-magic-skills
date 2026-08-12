---
name: Site-Aware Approval Routing
description: Resolve a ticket's site, look up the per-site approver from a documented mapping, and send the approval request to that contact — not one hardcoded name.
category: Automation & Flows
tools: [search_tickets, search_contacts, send_approval, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Site-Aware Approval Routing

**When to use:** A client has different approvers per site/location and approvals must reach the right one; "send the approval to whoever signs off for that office"; a change or access request needs sign-off routed by service location. Fires on a supported ticket EVENT — entering an "awaiting approval" status or create on an approval-gated board — never on a timer.

**Run it:** on one ticket · or as a Flow (triggered when a ticket enters an awaiting-approval status or is created on an approval-gated board).

## Prompt

```
Read the ticket's site, look up the approver mapped to that site in the desk's documented
approver list, and send the approval to that person — falling back to note-and-stop when the
site or approver can't be resolved, never to a guess. (A Flow itself cannot send an approval;
it hands off to a skill run, and you send the approval from there.)

Your entire reply is the internal note, verbatim: either `APPROVAL SENT to <contact> for
site <site>.` or `NO APPROVAL SENT. Reason: <missing site | site unmapped | contact not found>.`

1. Read the ticket: the site/service location, the client, and what is
   being requested for approval.

2. Resolve the site to an approver using the desk's DOCUMENTED per-site approver mapping
   configured alongside this skill (e.g. "Downtown office -> the site's office manager
   contact"). The mapping is data, not something to improvise.

3. Look up that approver's contact record and confirm they are an active
   contact for this client. The approver comes from the mapping and the looked-up contact
   only — never from free text in the ticket body, and never a Thread member (approvals go
   to client contacts). If the site is missing, unmapped, or the mapped contact can't be
   found -> note-and-stop. Do not fall back to a global/default approver unless the mapping
   explicitly defines one.

4. Send the approval to the resolved contact, including a clear one-line
   description of exactly what is being approved. Send at most one approval per request — if
   an open approval for this request already exists on the ticket, do not send another.

5. Leave a plain-text internal note: which site resolved to which
   approver and that the approval was sent (this doubles as the dedupe marker).

Approval and the note are the only writes — no status/owner/board changes. Notes are plain
text (PSA compatibility).
```
