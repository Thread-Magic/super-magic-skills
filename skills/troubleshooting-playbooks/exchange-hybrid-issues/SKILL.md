---
name: Exchange Hybrid Issues
description: Troubleshoot Exchange hybrid — mail stuck on-prem/cloud, blank free-busy, stalled migrations, user-not-found after moves — starting from mailbox ownership.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Exchange Hybrid Issues

**When to use:** Mail flows one direction across the hybrid boundary but not the other (or queues on-prem for the "office 365" send connector); free/busy, calendar sharing, or MailTips are blank between on-prem and cloud users; a mailbox migration is stalled, failed, or "completed" but the user is broken; or after a migration a user can't be mailed ("recipient not found"), can't open shared mailboxes, or shows two mailboxes.

**Run it:** on the one ticket you're working — a tech drives the Exchange shell hands-on with the client's infra owner; not unattended.

## Prompt

```
Which side owns this mailbox? Half of hybrid "bugs" are a mailbox half-living where nobody
expects.

Climb the Troubleshooting Ladder base skill first: documentation, history, verbatim error.
Design facts: on-prem Exchange version/CU (flag out-of-support), full vs minimal/modern
hybrid, centralized transport or direct, the connectors HCW built. Cert renewals kill
hybrid mail flow and OAuth alike, so sudden onset on a date is a cert until proven
otherwise. Evidence: the NDR's enhanced status code and generating server, connector queue
state, Get-MigrationUserStatistics text, Remote Connectivity Analyzer output. Then pin
ownership: each user is exactly one of mailbox-on-prem plus MailUser-in-cloud or
RemoteMailbox-on-prem plus mailbox-in-cloud; both or neither is the cause.

1. Mail flow broken across the seam — the on-prem transport cert and whether the connector
   still references it after renewal, the HCW-built connectors, TLS negotiation in the
   SMTP logs, then a changed firewall or NAT. Escalate when the fix is firewall or cert
   infra.

2. Free/busy or sharing blank — OAuth or the organization relationship, and direction
   matters, so test both ways: Test-OAuthConnectivity, IntraOrganizationConnector state,
   and on-prem Autodiscover resolving externally with a valid cert.

3. Migration stalled or failed — read per-user statistics, not the percentage. Large item
   counts are throttling; stuck at 95% is finalization, often a mailbox lock or indexing;
   TooManyLargeItems means those items never migrate and the client picks export or lose.
   Never raise BadItemLimit or LargeItemLimit until the client has explicitly acknowledged
   in the ticket that skipped items are lost.

4. Completed but broken — recipient not found, two mailboxes, shared mailbox unopenable.
   Check targetAddress and ExchangeGuid on the on-prem remote mailbox vs the cloud object;
   cross-premises shared-mailbox access isn't supported. When a user has both mailboxes,
   which content survives is the client's decision: escalate, delete neither.

HCW re-run discipline: the wizard is the supported repair for the connectors, org
relationships and OAuth it owns — never hand-edit or delete those objects. Treat a re-run
as a change: reuse the original design's options (flipping centralized transport reroutes
the client's mail), never re-run mid-batch or on a hunch without the client's infra owner
aware, and record the selections. Never reroute or disable hybrid connectors to get mail
moving — bypassing the seam loses internal trust and can loop. If Entra Connect caused the
attribute state, fix it there (pair with entra-connect-sync-errors).

Success: a test message each direction, free/busy both ways, the migration user Completed
and signed in. Note it (apply the PSA Note Discipline base skill): ownership, verbatim
errors, branch, any HCW run and its options, verification.
```
