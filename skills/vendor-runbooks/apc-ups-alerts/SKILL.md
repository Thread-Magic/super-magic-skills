---
name: APC UPS Alerts
description: Work APC UPS alerts: on-battery events, low runtime, self-test failure, or replace-battery indicators. Separate utility issues from UPS hardware faults.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Always-On Coverage]
---

# APC UPS Alerts

**When to use:** An on-battery / power-restored event (or a burst of them) lands as a ticket; a self-test failed, replace-battery, or low-runtime alert arrives; or someone asks whether the protected equipment would actually shut down cleanly in an outage.

**Run it:** on the alert ticket · or as a Flow (triggered when a matching APC/UPS alert ticket is created).

## Prompt

```
Triage an APC (Schneider Electric) UPS alert from PowerChute, a Network Management Card
(NMC), or RMM forwarding. Every UPS alert is about the next outage. Self-tests, battery
replacement and configuration are technician actions you direct and record. Verify model
behavior against APC's documentation; never invent battery state.

1. Parse the alert: UPS identity and location, event class, battery status, runtime, load.
   The client's documentation says what it protects; that sets the stake.

2. On-battery events, utility question first. One brief event with a clean power-restored is
   a grid blip: log it with the runtime used. Repeated events in a window are site power
   quality (failing circuit, overloaded panel, utility work) — correlate other site devices
   in prior tickets, then hand it with timestamps to the client's electrician or utility,
   their infrastructure and not the desk's. Never serially close these as blips. Sustained
   on-battery now is a live outage: runtime remaining vs shutdown time needed — confirm the
   shutdown chain is armed (step 4), tell on-site contacts.

3. Self-test failure or replace-battery → the unit provides NO protection until replaced;
   the next outage likely drops the load instantly. Set the priority accordingly; never
   routine maintenance for a critical load. Check battery age (documented install date
   or the NMC; service life is roughly 3-5 years) and prior tickets for earlier warnings.
   Identify the replacement cartridge (RBC part) and order per the client's procurement
   process. Many models hot-swap — verify for the specific model, and prefer a low-risk
   window for critical loads. Afterwards run a self-test, record the pass, update the
   documented install date. Chronically short runtime on a healthy battery is load creep —
   the load outgrew the unit: route a right-sizing recommendation to account management with
   the numbers.

4. Shutdown verification: confirm PowerChute/NMC integration is configured on the protected
   servers and hosts and that thresholds leave enough runtime to finish; VM and host
   shutdowns take minutes, not seconds. Never claim equipment will shut down gracefully
   without configuration evidence or a test record; with neither, recommend a test in a
   maintenance window. Never self-test a suspect battery under critical load outside a
   window — the test itself can drop the load.

5. Note the event class, battery/runtime facts, verdict, replacement status and
   shutdown-chain state; set the priority. Plain text, no markdown or emojis (apply the PSA
   Note Discipline base skill). As a Flow, apply that note and priority directly and flag
   any physical or self-test decision for a human.

Without documentation you may not know what the UPS protects — say so; the technician
confirms on site. When in doubt do nothing irreversible and escalate.
```
