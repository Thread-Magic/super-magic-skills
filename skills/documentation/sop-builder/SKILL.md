---
name: SOP Builder
description: Write a full standard operating procedure — scope, prerequisites, numbered procedure, validation, and escalation criteria — from a ticket, an existing rough doc, or a described process.
category: Documentation
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# SOP Builder

**When to use:** "Write an SOP for new-user setup / backup verification / <procedure>," a ticket resolution that needs to become a repeatable procedure, a rough checklist that needs formalizing, or a candidate flagged by sop-candidate-finder.

**Run it:** on one ticket or procedure.

## Prompt

```
Produce a complete, review-ready SOP DRAFT with every section a service desk needs
to run the procedure unattended by its author. A human approves and files it — never
auto-publish or write into IT Glue/Hudu/the KB yourself.

1. Gather source material: the ticket thread, any existing partial docs in the
   knowledge base / IT Glue / Hudu (where those connectors are enabled), and anything
   the requester pastes. If an SOP already exists for this procedure, propose a
   revision instead of a duplicate.

2. Draft the SOP in this fixed structure:
   - Title & purpose — what this procedure accomplishes, in one sentence.
   - Scope — which clients/environments/situations it covers, and explicitly what it
     does NOT cover.
   - Prerequisites — required access/roles, tools, portals, approvals, and info to
     collect before starting.
   - Procedure — numbered, imperative steps. One action per step. Include the
     expected result after any step where success is observable. Keep branches inline
     ("If X -> step 12; otherwise continue").
   - Validation — how to prove it worked: specific checks, what state to verify, what
     to record in the ticket.
   - Escalate when — concrete conditions that mean stop and escalate (errors, time-box
     exceeded, out-of-scope discovery), and to which tier/queue. This section is
     MANDATORY; an SOP without a stop condition is incomplete.
   - Revision block — placeholder for owner, date, and review cadence.

3. Sanitize: placeholders for client names, hostnames, IPs, tenants (<client>,
   <server>, <tenant>); strip credentials entirely and reference the credential store
   instead ("retrieve admin credentials from the documentation platform").

4. Pressure-test the draft: could a competent tech who has never done this follow it?
   Base the procedure on evidence (thread, docs, requester statements). Where you must
   fill a gap, mark it [verify: ...] for the reviewer rather than presenting a guess
   as fact. Keep language plain and localizable — no idioms; the SOP may run on a
   non-English desk.

5. Output the SOP in chat for review. Do not file it into any documentation platform
   yourself.
```
