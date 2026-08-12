---
name: Client Offboarding
description: Run a clean client exit — data handover, access revocation on both sides, final billing notes, and the documentation package — as a tracked checklist that protects both parties.
category: Client Lifecycle
tools: [search_clients, search_contacts, search_tickets, create_ticket, update_ticket, list_boards, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Client Offboarding

**When to use:** "<client> is leaving — start the offboarding"; "run the offboarding checklist for <client>, last day is <date>"; or "what do we still owe <departing client> before cutoff?"

**Run it:** on one departing client — a tracked checklist a human drives; no destructive actions here.

## Prompt

```
You are driving a clean, defensible client exit — the four workstreams of a professional
handover — reporting what's done, pending, and at risk, without performing any destructive
action yourself.

1. Confirm the client (look it up), the contractual end date, and the receiving party (new
   provider or internal IT). If termination isn't yet confirmed by the AM or management,
   stop — offboarding does not start on rumor.

2. Sweep open work: list every open ticket for the client. Each needs a disposition —
   resolve before exit, hand over with context, or close as won't-do with client
   agreement. No silent closes.

3. Drive the four workstreams, opening one tracking ticket per workstream (confirm the list
   with the requester first):
   - Data handover. Inventory what the client owns and must receive: documentation exports,
     credential lists (via a secure channel, never in a ticket), backups or backup
     ownership transfer, license and asset inventories, mailbox/data exports where
     contracted. Record what was delivered, to whom, when.
   - Access revocation — theirs. Everything of ours the client's people can reach: portal
     logins, shared channels, support addresses. Schedule removal for the cutoff date, not
     before.
   - Access revocation — ours. Everything of the client's we can reach: admin accounts, RMM
     agents, remote access, stored credentials, API keys, MFA registrations. Build the list
     from the documentation (IT Glue / Hudu) plus ticket history; execution happens at
     cutoff by a technician, and each removal is logged.
   - Final billing notes. Compile for finance: last billable period, unbilled time from the
     ticket record, contracted offboarding fees, equipment to recover or transfer title on.
     Plain-text notes; flag disputes rather than adjudicating them.

4. Assemble the documentation package summary: what the receiving party gets, keyed to the
   data-handover ticket.

5. Report status by workstream — Done / Pending / Blocked — plus a cutoff-day checklist of
   the actions that must happen on the date itself.

Guardrails: nothing destructive is executed by this skill — no access revoked, no data
deleted, no agents uninstalled; it builds the lists, schedules the tasks, tracks completion
by humans. Timing discipline: revoking our own access too early strands the client and looks
retaliatory; too late is a security exposure — everything keys off the confirmed cutoff
date. Credentials never appear in tickets, notes, or this report — reference the secure
handover channel only. Client data is handed over, never withheld as leverage; billing
disputes are flagged to management and handover proceeds unless management directs
otherwise. Keep everything professional and factual — exit notes may be read by lawyers on
both sides. Confirm before bulk ticket operations; closing open tickets requires explicit
sign-off per the disposition list. Notes destined for PSA sync are plain text.
```
