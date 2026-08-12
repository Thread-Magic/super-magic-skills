---
name: Access Request Handling
description: Work a request for access to a folder, calendar, distribution list, or shared mailbox — approval checked, least privilege applied, expiry set on anything temporary. Use when a ticket asks to "give <user> access to" a resource.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, update_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Access Request Handling

**When to use:** "Give <user> access to the finance shared folder" / "<user> needs the team calendar or projects DL" / "add me to the support shared mailbox" — any grant-access ticket where the approver and access level aren't yet pinned down.

**Run it:** on one ticket — identity- and approval-gated, so a human stays in the loop.

## Prompt

```
Turn this "give <user> access to <resource>" ticket into an approved,
least-privilege, documented grant — with an expiry and revert plan whenever the need
is temporary.

1. Identify precisely: look up the contact who needs access, which resource (exact
   folder path, calendar, DL, or mailbox name), what level (read, contribute, full),
   and for how long. If the request says only "access," ask — never assume full
   control.

2. Check the client's access policy in the knowledge base and their IT documentation
   (IT Glue): who owns or approves this resource? If an approver is defined, get their
   sign-off before granting (send an approval request, or use the client's documented
   channel). If the requester IS the resource owner, that counts.

3. Apply least privilege: grant the lowest level that satisfies the stated need.
   Reading files doesn't require contribute; viewing a calendar doesn't require editor.

4. If the need is temporary (project, covering leave, audit), set an explicit expiry
   date and create the revert as a real follow-up — a note with the removal date and
   owner, or a scheduled follow-up ticket — so the grant doesn't become permanent by
   neglect.

5. Execute the grant (or hand off to the tech/tooling that can), then verify the user
   can actually reach the resource before closing.

6. Post a plain-text internal note: who was granted what level on which resource, who
   approved, why, and any expiry with its revert plan. Log time and confirm to me.

Guardrails: no grant without an identified approver or documented standing policy that
covers it — "the user asked" is not approval. Least privilege is the default; escalate
any request for full control of a resource the user doesn't own. Every temporary grant
gets an expiry and a tracked revert. If the resource or its owner can't be identified
with confidence, do not grant — ask. Security-group membership routes to the Group
Membership Request skill; mailbox delegation specifics route to Shared Mailbox
Delegation.
```
