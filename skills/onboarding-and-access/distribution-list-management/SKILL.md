---
name: Distribution List Management
description: Add or remove distribution list members with owner approval and a documented reason logged on the ticket, keeping email groups clean and auditable.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Distribution List Management

**When to use:** "Add <user> to the sales distribution list" / "remove <user> from announcements — they moved teams" / "who approves changes to the leadership DL?" — or a DL change inside a broader onboarding/offboarding ticket.

**Run it:** on one ticket — approval-gated, so a human confirms membership changes.

## Prompt

```
Handle this DL membership change so every add and remove has an approver and a
rationale on record.

1. Identify the exact list (clients often have similarly named DLs — confirm the
   address, not just the display name), the member to add/remove (look up the contact),
   and the stated reason.

2. Find the list owner or the client's documented approval rule (check the knowledge
   base and their IT documentation in IT Glue). Get owner approval before changing
   membership (send an approval request, or use the client's channel). Exceptions:
   removals that are part of an authorized offboarding, and adds covered by a documented
   role profile (new sales hire → sales DL) — cite the covering policy instead.

3. Sanity-check the change: adding an external address to an internal list, or anyone
   to a broad-reach list (all-staff, leadership, client-facing), gets flagged to the
   approver explicitly rather than buried in a routine request.

4. Execute the change. If the list is synced from on-prem AD, make the change on the AD
   side, run an AD Connect delta sync, and verify before reporting done.

5. Post a plain-text note: list address, member added/removed, approver, and the
   documented rationale. Log time and confirm to me.

Guardrails: no membership change without owner approval or a citable standing policy.
External addresses and broad-reach lists always get an explicit approver callout —
never treat those as routine. Confirm the exact list address before changing anything;
a near-name match is not a match. Record the rationale — "user requested" alone is not
a rationale. Bulk cleanups (many removals at once) get a proposed list posted for
approval first — never bulk-remove unattended.
```
