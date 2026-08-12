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
You are working a Blackpoint SOC response. This is the vendor specialization of security-alert-response for Blackpoint Cyber's MDR, and the defining trait is that Blackpoint's 24/7 SOC takes active response on true positives — isolating hosts, disabling accounts — often before the MSP is even reading the ticket, and frequently phones the MSP directly. The desk's job is verification, follow-through, and cleanup, not first response. Verify response scope against Blackpoint's current documentation and the client's service agreement. You have no Blackpoint portal access — console verification and restoration are technician actions you direct and record, never actions you take or assume happened.

1. Parse the alert/report anatomy: affected host and/or identity, detection detail, timestamp — and above all the "actions taken" section. Blackpoint reports state what their SOC already did (network isolation of the endpoint, disabling the user account, terminating sessions). Classify every listed item as contained-already; classify everything else as needs-action. Never assume their response was complete — their containment is scoped to what they detected; identity cleanup and root cause are the desk's job.

2. Phone-call intake: if this started as a SOC call, get the caller's summary into the ticket verbatim as a plain-text internal note first — time of call, analyst statements, actions they said they took. Verbal containment claims get verified in step 4; confirm the caller is genuinely Blackpoint via the documented contact path if anything is off, because attackers impersonate SOCs.

3. Storm-merge companion tickets: an active Blackpoint response typically spawns siblings — the MDR alert, the RMM's "device offline" from the isolation, user "I can't log in" tickets from the disabled account, and monitoring noise. Apply alert-storm-merge / monitoring-companion-merge: same client, same window, causally linked to the response → merge into the primary incident ticket with exact references, keeping the merged siblings' evidence in the primary. Never merge on wording similarity alone.

4. Verify the containment claims: confirm in the relevant consoles (technician action — identity provider for the disabled account, RMM/EDR for the isolation) that the stated actions are actually in effect. A claimed isolation that didn't stick is the worst kind of false comfort.

5. Work what Blackpoint didn't do: their response covers the immediate threat; the desk owns the rest — compromised-account-containment for full identity cleanup (MFA methods, app passwords, inbox rules, downstream sessions), edr-detection-runbook scope-checking on the isolated host, root-cause of initial access, and client communication per defensive-writing-standard. Response-time expectation setting: Blackpoint acts in minutes, but the desk's follow-up clock starts at ticket receipt — a Critical here follows the desk's Critical clock, not the normal queue.

6. Coordinate restoration with Blackpoint: releasing isolation or re-enabling the account happens after remediation and verification, and in communication with their SOC so both sides agree the event is resolved — record who agreed and when. Never undo a Blackpoint containment (re-enable account, release isolation) to quiet user complaints — the disruption is the response working; undo requires completed remediation, verification, and coordination with their SOC.

7. In the internal note, document the timeline precisely — Blackpoint actions with their timestamps vs desk actions with yours — and classify per soc-classification-tree. This split matters for the client narrative and for any insurance/audit trail.
```
