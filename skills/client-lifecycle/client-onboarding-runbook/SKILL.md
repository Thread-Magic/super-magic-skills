---
name: Client Onboarding Runbook
description: Take a newly signed client from MSA to service-desk readiness — boards and routing, contacts loaded, documentation intake, monitoring confirmed, and welcome communications — as a tracked checklist with tickets.
category: Client Lifecycle
tools: [search_clients, search_contacts, create_ticket, update_ticket, list_boards, search_knowledge_base, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Client Onboarding Runbook

**When to use:** "We just signed <client> — set up onboarding"; "run the new-client onboarding checklist for <client>"; or "is <client> ready for go-live? What's still missing?"

**Run it:** on one newly signed client — a tracked readiness checklist, run manually.

## Prompt

```
You are turning "we signed them" into "the desk is ready for their first ticket." Drive a
standard readiness checklist, open the tracking tickets, and report what's done, pending,
and blocked.

1. Confirm the client exists (look it up). If not yet in the system, stop and report that
   client creation is the prerequisite — do not proceed against a guessed record.

2. Gather the essentials from the requester if not provided: go-live date, agreement
   type/tier, primary sites, and the client's main point of contact.

3. Walk the readiness areas, checking current state before creating work:
   - Boards and routing. Look up the boards, confirm which one(s) the client's tickets
     should land on and that routing (email domain, catchall) is planned. Flag any domain
     overlapping an existing client — misrouting risk.
   - Contacts. Verify key contacts are loaded with correct emails; list who's still missing
     (at minimum: primary contact, an authorizer for approvals, billing contact).
   - Documentation intake. Check the documentation systems (IT Glue / Hudu / knowledge base,
     whichever is enabled) for environment docs — credentials process, network overview,
     LOB apps, escalation preferences. List what exists and what must be collected.
   - Monitoring and management. Confirm from the intake plan whether RMM agents, backup
     monitoring, and alert routing are scheduled — the desk shouldn't go live blind. This
     runbook tracks the task; it does not deploy agents.
   - Welcome communications. Draft the welcome note for client staff: how to reach support
     (channels, hours, what to expect), labeled DRAFT for the AM to send.

4. For each incomplete area, open one tracking ticket on the appropriate board — clear title
   ("Onboarding — <client>: load contacts"), owner if known, due before go-live. Confirm
   with the requester before creating tickets in bulk.

5. Output a readiness report: each area marked Ready / In progress / Blocked, the tickets
   created, and the top risks to the go-live date.

Guardrails: confirm before creating — list the tickets you intend to create and get a yes;
never create duplicate onboarding tickets (search first). Never invent client facts
(domains, sites, contact emails) — anything unconfirmed goes on the "collect from client"
list, not into records. Credentials received during onboarding are never pasted into
tickets or notes — reference the documentation system as the storage location. The welcome
communication is a DRAFT for a human to send. Integration degradation: if IT Glue/Hudu or
an RMM isn't connected, mark those areas "manual verification required" rather than skipping
silently. Tracking notes destined for PSA sync are plain text.
```
