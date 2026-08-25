---
name: Blackpoint SOC Response
description: Work Blackpoint MDR SOC calls: confirm what analysts contained (host isolation, account disable), finish the response, and merge companion ticket storms.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, merge_ticket, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Blackpoint SOC Response

**When to use:** A Blackpoint SOC alert, incident email, or call-summary lands as a ticket; a Blackpoint analyst phoned the desk about an active threat and someone needs the follow-up worked; or multiple Blackpoint tickets from one event need consolidating.

**Run it:** on the alert ticket.

## Prompt

```
Work a Blackpoint SOC response — the vendor specialization of security-alert-response for
Blackpoint Cyber's MDR. Their 24/7 SOC takes active response on true positives — isolating
hosts, disabling accounts — often before the MSP has read the ticket, and frequently phones the
desk. Your job is verification, follow-through and cleanup, not first response. Console
verification and restoration are technician actions you direct and record.

1. Parse the report: affected host and identity, detection detail, timestamp — and above all the
   "actions taken" section. Their report states what the SOC already did — network isolation,
   disabling the account, terminating sessions. Everything listed is contained-already;
   everything else is needs-action. Never assume their response was complete — their containment
   is scoped to what they detected, and identity cleanup and root cause are the desk's job.

2. If this started as a SOC call, get the caller's summary into the ticket verbatim first — time
   of call, analyst statements, actions they said they took. Confirm the caller really is
   Blackpoint via the documented contact path if anything is off; attackers impersonate SOCs.

3. Merge the companion storm: an active response spawns siblings — the MDR alert, the RMM's
   "device offline" from the isolation, "I can't log in" tickets, monitoring noise. Per
   alert-storm-merge and monitoring-companion-merge: same client, same window, causally linked
   to the response → merge into the primary incident ticket with exact references, keeping the
   siblings' evidence. Never merge on wording similarity alone.

4. Verify the containment claims: the technician confirms in the identity provider that the
   account is disabled and in the RMM or EDR that the isolation is in effect. A claimed
   isolation that didn't stick is the worst kind of false comfort.

5. Work what Blackpoint didn't. Their response covers the immediate threat; the desk owns
   compromised-account-containment for identity cleanup (MFA methods, app passwords, inbox
   rules, downstream sessions), edr-detection-runbook scope-checking on the isolated host, root
   cause, and client communication per defensive-writing-standard. Blackpoint act in minutes,
   but the desk's clock starts at ticket receipt — a Critical here follows the desk's Critical
   clock.

6. Coordinate restoration: releasing isolation or re-enabling the account happens after
   remediation and verification, and in agreement with their SOC — record who agreed and when.
   Never undo a Blackpoint containment to quiet user complaints; the disruption is the response
   working.

7. Note the timeline precisely — Blackpoint's actions with their timestamps versus the desk's
   with yours — and classify per soc-classification-tree. The split matters for the client
   narrative and any insurance or audit trail.
```
