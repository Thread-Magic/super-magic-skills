---
name: Retention Policy Requests
description: Change Microsoft Purview retention and deletion policies with scope confirmed, legal-hold interaction flagged, and authorization documented.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Retention Policy Requests

**When to use:** A ticket asks to retain all mail for N years for compliance, auto-delete anything older than X in a location, or asks "why can't this user permanently delete emails?" (existing policy discovery). You turn a vague "keep email for seven years" into a precisely scoped, authorized, reversible-where-possible retention change. NOT for placing a legal hold — that is litigation-hold; this skill manages the general retention machinery around it.

**Run it:** on one client's request — you scope and confirm it, a technician drives the Purview portal (not a Flow: it needs a human at the console).

## Prompt

```
Turn a vague retention request into a precisely scoped, authorized change, with deletion
consequences and legal-hold interactions stated before anything ships. The tech drives the
Purview portal. Apply the Write Guardrails base skill — never invent data; when in doubt do
nothing and escalate.

1. Decompose the ask into Purview terms, confirming each with the requester:
   - Retain, delete, or retain-then-delete? For how long, dated from created or last
     modified?
   - Scope: which workloads (Exchange, SharePoint, OneDrive, Teams), which users or sites?
     Never assume org-wide; "all mail" is restated as an explicit location list first.
   - Adaptive or static scope, if the tenant uses adaptive scopes.

2. Discover current state: the tech lists existing retention policies and labels on the
   scope, plus any litigation or eDiscovery holds on the affected mailboxes, into the
   ticket. A new policy lands on top, and the principles of retention decide the winner:
   retention beats deletion, longest wins, explicit scope beats broad. Where policies
   conflict, present that outcome rather than promising the requested behavior. Pull documented client retention requirements (Connector Degradation
   base skill if IT Glue is off).

3. State the legal-hold interaction in the ticket before approval: a litigation or eDiscovery
   hold overrides any deletion policy and held items are preserved regardless. A deletion
   policy never "cleans up" held data, and removing a retention policy from held mailboxes
   does not release it. Correct the client in writing if they think deletion applies to held
   mailboxes.

4. Warn on the irreversible parts. Once a deletion policy starts processing it destroys data
   past the window — no undo for what is purged. Preservation Lock cannot be shortened or
   removed once applied: refuse it without explicit written client direction acknowledging
   that permanence.

5. Approval gate: the client's documented compliance or legal authority, not just someone in
   IT. For a delete action the approval text must restate the scope and the destruction
   consequence: no deletion policy ships without that named authority approving in writing.

6. Prepare the change: Purview portal steps, or `New-RetentionCompliancePolicy` and
   `New-RetentionComplianceRule` — verify module versions. Prefer a pilot location before
   org-wide where the client allows.

7. Verify after propagation, which can take up to a week: the policy shows distributed or On
   and a spot-check item behaves as expected. Set that expectation. Note it
   (PSA Note Discipline base skill: plain text, no markdown) — policy name, exact scope and
   locations, retain versus delete and duration, interaction with the step 2 holds, approver,
   application date, rollback (disable the policy; note what deletion already processed and
   cannot be rolled back). Log time.
```
