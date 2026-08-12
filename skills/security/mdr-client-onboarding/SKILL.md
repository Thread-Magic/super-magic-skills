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
Run the desk-side checklist for turning on managed detection: what's covered (and what
visibly isn't), where the alerts land and who works them, who may authorize containment at
3 a.m., and why the first month will be noisy — set on the record before the first alert
fires. Work it in order:

1. Asset scoping — coverage in writing: enumerate what the sensor/agent will cover using
   the RMM inventory and the client's documentation: endpoints, servers, identity tenant,
   mail, network devices. Produce the coverage list AND the exclusions list (unsupported OS
   versions, unmanaged/BYOD devices, that one appliance) — the uncovered list is the more
   important document, because everyone will later assume "the MDR watches everything."
   Record both with an as-of date.
2. Deployment verification: reconcile deployed-agent count against the in-scope asset
   count; the gap list becomes deployment tickets. "Purchased" is not "protected" — the
   onboarding isn't done until the reconciliation says so, with result-cap honesty on any
   counts.
3. Alert routing into the desk: agree and document where MDR alerts land (which
   board/queue), what identifiers the alert body carries for client attribution (tenant ID,
   domain — feed this to the security-alert-response routing step), the severity mapping
   between the provider's labels and the desk's tiers, and the after-hours path. Test the
   route with the provider's test alert before go-live.
4. Escalation contacts and authority — recorded in the client's documentation: client side,
   who the provider/desk may call at any hour, in what order, with verified phone numbers on
   file. Authority matrix: what the MDR provider may do autonomously (e.g. isolate a host)
   vs. what needs client approval vs. desk-executed actions. The pre-authorization decisions
   made here are what make compromised-account-containment and ransomware-response fast
   later — get them signed, not implied.
5. Baseline-noise period expectations, set with the client in advance: the first two to
   four weeks produce elevated alert volume while the provider learns the environment. Every
   alert still gets verified — baseline period is context for volume, never a reason to
   close unread. Recurring confirmed-benign patterns get fed back to the provider for tuning
   (security-noise-tuning discipline: narrow suppressions, at the source, never PSA
   auto-close).
6. Go-live record: coverage + exclusions, routing test result, severity mapping, authority
   matrix, baseline expectations, and a 30-day review ticket to reassess noise levels,
   coverage gaps, and whether escalations worked. Note the monthly-security-report skill as
   the ongoing reporting vehicle.

Guardrails — always:
- The exclusions list is mandatory output — never let "MDR onboarded" imply total coverage;
  state what is not watched.
- No alert is closed unverified because "it's the baseline period"; the period predicts
  volume, not verdicts.
- Containment authority must be written and client-signed before go-live — never assume the
  provider or desk may isolate hosts or disable accounts without documented authorization.
- Escalation phone numbers are verified at onboarding, not first used during an incident.
- Provider-severity labels map to desk tiers explicitly; don't inherit a foreign severity
  scale silently.
- Degradation: without RMM connectors, the deployment reconciliation runs on provider +
  client-supplied exports — record their as-of dates and gaps rather than presenting them as
  live truth. Never invent counts.
```
