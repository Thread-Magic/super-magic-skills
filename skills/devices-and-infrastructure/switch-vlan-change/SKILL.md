---
name: Switch VLAN and Port Change
description: Prepare a switch port or VLAN change safely — blast-radius check, agreed change window, and a rollback config saved before anything on the switch changes.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, liongard_launchpoint, liongard_device, liongard_timeline, liongard_metric, search_tickets, add_ticket_note, send_approval, schedule_ticket, update_ticket]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Switch VLAN and Port Change

**When to use:** "Move the port in <room> to the voice/camera/guest VLAN", adding a VLAN or tagging it onto a trunk, or reviewing a proposed switch change for blast radius.

**Run it:** on one change-request ticket, on demand (not a Flow — the change routes through human approval and a change window).

## Prompt

```
Front-load the safety work for a VLAN or port change: identify exactly which port on which
switch, establish what else breaks, book a window, and make sure a known-good config is
saved BEFORE anything changes. Hand the spec to the implementing tech; this skill never
configures a switch.

1. Pin down the physical target — which switch, which port, which site — from the
   documentation (IT Glue / Hudu) switch records and port maps. With no port map, the
   first deliverable is "identify and label the port on site"; never guess a port number
   from memory or convention.

2. Blast radius, in widening circles: (a) what is on the port now — one desktop, or a
   downstream unmanaged switch feeding a whole room; (b) is it an uplink or trunk, since
   trunk changes affect every VLAN riding it; (c) what else shares the VLAN being modified
   (phones, APs, cameras, servers); (d) is spanning-tree or the management VLAN involved —
   a wrong change there severs remote access to the switch. Where a Liongard inspector
   covers the switch platform, read its change history (apply the Inspector Read
   Discipline base skill — confirm the inspector exists and last ran successfully, and
   date any config data you cite).

3. Classify risk: a single access port with one endpoint is low and can be done in
   business hours with the user's consent. Trunk, uplink, management VLAN, or anything
   feeding multiple users needs an after-hours window, with someone reachable on site in
   case remote access is lost.

4. Rollback FIRST, non-negotiable: the spec must require saving the running configuration
   (backup or export) before the change, and must state the rollback action — "restore
   saved config", or the explicit reverse commands. A change request with no captured
   pre-change config is not ready.

5. Assemble the change spec: target switch and port, current state, desired state,
   blast-radius findings, window, rollback plan, verification steps (endpoint gets the
   expected VLAN and DHCP scope, no new spanning-tree events, management access still up).
   Leave it as a note (apply the PSA Note Discipline base skill — plain text, no markdown
   or emojis) and route it for approval if the client's change process requires one.

6. Schedule a follow-up ticket for the agreed window, assigned to the implementing tech,
   carrying a verification note before it closes.

Guardrails: no trunk, uplink, or management-VLAN change without an after-hours window and
a captured pre-change config — decline to mark the spec ready otherwise. When in doubt,
widen the blast radius — an unmanaged switch hiding behind a port is common, so treat a
port whose downstream you cannot confirm as multi-user. Never put switch credentials or
SNMP strings in the ticket; reference documentation by name. If switch documentation does
not exist, say so and make documenting it part of the change.
```
