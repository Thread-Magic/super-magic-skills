---
name: MDR Client Onboarding
description: Onboard a client to a new MDR or SOC service: scope assets, wire alert routing into the desk, record escalation contacts, and set noise expectations.
category: Security
tools: [search_clients, search_contacts, search_tickets, search_ninjaone_devices, connectwise_rmm_search_devices, search_itglue, add_ticket_note, create_ticket, update_ticket]
connectors: [NinjaOne, ConnectWise RMM, IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner, Service & Ops Manager]
outcome: [Always-On Coverage, Risk & Compliance]
---

# MDR Client Onboarding

**When to use:** A client signed for MDR/SOC monitoring and the service is being stood up; alerts from a newly-enabled monitoring service start arriving and routing/expectations were never documented; or a service review asks "what exactly does the MDR cover for this client?"

**Run it:** on one client's onboarding (a service stand-up).

## Prompt

```
Run the desk-side checklist for turning on managed detection — all of it on the record before
the first alert fires.

1. Scope the assets in writing. Enumerate what the sensor or agent covers from the RMM
   inventory and the client's documentation — endpoints, servers, identity tenant, mail,
   network devices — and produce the coverage list and the exclusions list (unsupported
   OS versions, unmanaged or BYOD devices, that one appliance). The uncovered list is the more
   important document, because everyone will later assume the MDR watches everything. Date
   both.
2. Verify deployment: reconcile deployed-agent count against the in-scope asset count and turn
   the gap into deployment tickets, with "at least N" honesty on any count (Sweep Honesty base
   skill). "Purchased" is not "protected" — onboarding isn't done until the reconciliation
   says so.
3. Wire alert routing into the desk and document it: which board or queue alerts land on,
   what identifiers the alert body carries for client attribution (tenant id, domain — feed
   this to the security-alert-response routing step), the mapping from the provider's severity
   labels to the desk's tiers, and the after-hours path. Test the route with the provider's
   test alert before go-live.
4. Record escalation contacts and authority in the client's documentation: who the provider or
   desk may call at any hour, in what order, with phone numbers verified now, not during an
   incident. Then the authority matrix — what the MDR provider may do autonomously (isolate
   a host, say), what needs client approval, and what the desk executes. Get these
   pre-authorizations signed, not implied; they are what makes compromised-account-containment
   and ransomware-response fast later.
5. Set baseline-noise expectations with the client in advance: the first two to four weeks
   carry elevated alert volume while the provider learns the environment. Every alert is still
   verified — the baseline period predicts volume, never verdicts. Feed recurring
   confirmed-benign patterns back to the provider for narrow, at-source tuning
   (security-noise-tuning), never a PSA auto-close.
6. Write the go-live record: coverage and exclusions, routing test result, severity mapping,
   authority matrix, baseline expectations, and a 30-day review ticket to reassess noise,
   coverage gaps and whether escalations worked. Point ongoing reporting at
   monthly-security-report.

The exclusions list is mandatory output — never let "MDR onboarded" imply total coverage.
Containment authority must be written and client-signed before go-live: never assume the
provider or desk may isolate hosts or disable accounts without documented authorization.
Without RMM connectors the reconciliation runs on provider and client exports — record their
as-of dates and gaps rather than presenting them as live truth. Never invent counts.
```
