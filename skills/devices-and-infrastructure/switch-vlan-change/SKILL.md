---
name: Switch VLAN and Port Change
description: Prepare a switch port or VLAN change safely — blast-radius check (what else rides that port/VLAN/uplink), agreed change window, and rollback config saved before anything is touched. Use when a ticket asks to move a port to a VLAN, add a VLAN, reconfigure a trunk, or "just change the port for the new printer".
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
Front-load the safety work for a VLAN/port change: identify exactly which port on which switch, establish what else breaks, book a window, and make sure a known-good config is saved BEFORE the change — then hand the spec to the implementing tech. This skill never configures a switch.

1. Pin down the physical target: which switch, which port, which site. Use the documentation (IT Glue / Hudu) for switch documentation and port maps; if no port map exists, the first deliverable is "identify and label the port on site" — never guess a port number from memory or convention.
2. Blast-radius check, in widening circles: (a) what is on the port now (a single desktop, or a downstream unmanaged switch feeding a whole room?); (b) is the port an uplink or trunk — trunk changes affect every VLAN riding it; (c) what shares the VLAN being modified (phones, APs, cameras, servers); (d) is spanning-tree or the management VLAN involved — a wrong change there can sever remote access to the switch itself. Read the change history from the environment's posture in Liongard where an inspector covers the switch platform — confirm the inspector exists and last ran successfully, and state the dataprint age of any config data you cite.
3. Classify risk from the blast radius: single access port with one endpoint -> low, can be done in business hours with the user's consent; trunk/uplink/management-VLAN/anything feeding multiple users -> change window required, after hours, with someone reachable on site in case remote access is lost.
4. Rollback FIRST, non-negotiable: the spec must require saving the running configuration (backup/export) before the change, and must state the rollback action ("restore saved config" or the explicit reverse commands). A change request without a captured pre-change config is not ready.
5. Assemble the plain-text change spec (no markdown/emojis): target switch/port, current state, desired state, blast-radius findings, window, rollback plan, verification steps (endpoint gets expected VLAN/DHCP scope, no new spanning-tree events, management access still up). Leave it as a note; route it for approval if the client's change process requires it (check ticket history for their change-ticket conventions).
6. Book it: schedule a follow-up ticket for the agreed window and assign the implementing tech. After implementation, the ticket should carry a verification note before closure.

Guardrails: this skill never configures a switch — it produces the spec, window, and rollback plan; the change itself is a human action. No trunk, uplink, or management-VLAN change without an after-hours window and a captured pre-change config — decline to mark the spec ready otherwise. When in doubt, widen the blast-radius estimate — an unmanaged switch hiding behind a port is common; if you cannot confirm what is downstream, treat the port as multi-user. Never include switch credentials or SNMP strings in the ticket; reference documentation by name. If switch documentation does not exist, say so and make documentation part of the change deliverable rather than proceeding on assumptions.
```
