---
name: Internal IT Offboarding
description: Offboard departing MSP staff with client-credential rotation first, then tool deprovisioning, ticket reassignment, and client-facing transition notes.
category: MSP Business Operations
tools: [search_tickets, search_members, search_clients, search_knowledge_base, search_itglue, search_hudu, create_ticket, update_ticket, add_ticket_note, send_approval, log_time_entry]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Internal IT Offboarding

**When to use:** "Offboard <user> — last day is Friday." / "Terminate <user>'s access effective now." / an immediate-exit situation where access must be cut same-hour / auditing a past departure ("did we actually rotate everything when <user> left?") / building the internal offboarding checklist itself.

**Run it:** on one departing staff member's offboarding ticket — run it manually (not a Flow; every access change is staged for a human to approve and execute).

## Prompt

```
Run an MSP staff departure as a multi-tenant security event: the leaver held credentials into
client environments, so client-credential rotation comes FIRST, before internal deprovisioning.
You inventory, sequence and track; authorized admins execute.

1. Confirm the leaver, last working day, and whether this is a standard exit or an immediate one
   (access cut now, questions later); the mode changes ordering urgency, not the checklist.

2. CLIENT-CREDENTIAL ROTATION FIRST. Build the exposure inventory before touching internal
   accounts: vault and folder access in the password manager; shared and named admin accounts in
   client environments (domain admin, M365 global admin, firewall, hypervisor); the client sites
   their RMM or remote access reached; VPN profiles, client-issued accounts, any client that gave
   them a personal login. Source it from IT Glue, Hudu or the knowledge base plus their ticket
   history; post it as a rotation checklist and track each item to done. Rotate shared
   credentials, don't just remove access — removal is no help if they memorized it.

3. Internal cutover and seat reclaim, in strict order: sign-in blocked and sessions revoked, MFA
   cleared, mailbox handled (delegate to the manager before any license removal), chat and
   collaboration, then the PSA member account deactivated after ticket reassignment, RMM and docs
   users removed, remote-access licenses reclaimed. Note each seat.

4. Work handover. Reassign their open tickets to the covering tech or dispatch queue, adding a
   one-line context note where the thread doesn't speak for itself. Where the leaver was a
   client's primary contact, draft a warm, forward-looking transition note: "your primary
   engineer is now <name>; nothing else about your service changes." These are DRAFTS for a
   manager to approve and send.

5. Close with an audit note — plain text, no markdown or emojis (PSA Note Discipline base skill):
   rotation checklist done, accounts disabled with timestamps, seats reclaimed, tickets
   reassigned, clients notified. Log time.

Apply the Write Guardrails base skill: confirm before any write, never present a recommendation
as done, never invent data, when in doubt do nothing. For an immediate exit, block identity,
revoke sessions and remove vault access within the hour, and say what stays exposed until
rotated. No reason for departure in any note — internal factual ("offboarded effective <date>"),
client-facing warm and reason-free. No credentials in tickets, ever; reference the documentation
system. Keep the exposure inventory on the offboarding ticket — it is itself sensitive. If the
vault or docs platform can't produce a reliable access map (Connector Degradation base skill),
say what you couldn't verify and rotate the standard shared-credential set for every client their
ticket history touched — over-rotation is the safe direction.
```
