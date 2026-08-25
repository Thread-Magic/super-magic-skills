---
name: Print Server Management
description: Operate a print server layer — spooler triage, disciplined driver deployment (no ad-hoc installs), and planning queue migrations to a new print server.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_windows_services, control_ninjaone_windows_service, get_ninjaone_device_activities, get_ninjaone_device_link, search_itglue, search_hudu, search_tickets, add_ticket_note, create_ticket, send_approval]
connectors: [NinjaOne, IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Print Server Management

**When to use:** Multiple users at a client can't print, the Print Spooler crashes repeatedly on a print server, or a print server is being retired and its queues must migrate.

**Run it:** on one print server, on demand (not a Flow — service restarts and migrations need requester consent and change windows).

## Prompt

```
Server-side printing: spooler triage, deliberate driver deployment, and queue migrations
that don't cost a day of "I can't print" tickets. Client- or co-managed server -> your
output is a recommendation package for their administrator.

1. Confirm the blast radius says "server": one user -> printer-troubleshooting; one
   printer, all users -> that device or its queue; many printers, many users -> the
   server. Identify it in documentation (IT Glue / Hudu) and locate it in the RMM,
   verifying the role in the device details — PRINT/PS hostnames and class filters are
   hints, not evidence.

2. Spooler triage: check the Print Spooler state in the device's Windows services and read
   recent activity for crash history. Repeated crashes are classically a corrupt job stuck
   in the queue, a bad driver (one printer's taking down the shared spooler), or a recent
   Windows print update — look for patches landing just before the crashes began. Prior
   spooler tickets on this server mean fixing the cause, not the symptom.

3. Restart with consent: a spooler restart kills in-flight jobs for everyone — confirm
   with the requester first (or note printing is already fully down), then restart the
   service through the RMM. A suspected stuck job means a queue purge (clearing the spool
   directory), which is hands-on — hand the tech a deep link into the device with the
   steps spelled out. If crashes resume, isolate the offending driver or queue; recurring
   restarts are a stopgap, and must be labelled one.

4. Driver discipline: drivers go out through the documented mechanism (print management,
   GPO, deployment tool), never installed one-off on the server mid-incident. Prefer the
   vendor's stable or universal line, stage on one queue before fleet-wide rollout, and
   record every change in documentation.

5. Queue migration (server replacement): inventory every queue on the old server (name,
   share name, driver, IP port, defaults) from documentation plus a hands-on export the
   tech performs. Plan the cutover: recreate queues on the new server, stage drivers,
   migrate user and GPO mappings, keep the old server's shares alive until mappings are
   confirmed switched. Communicate the window; keep names and shares stable — a rename
   breaks scripted and hard-coded mappings. Route the plan for approval, tracked as its
   own ticket.

6. Output findings, root-cause hypothesis with evidence, actions taken (service restarts
   only) and handoff steps with deep links, as a note (apply the PSA Note Discipline base
   skill — plain text, no markdown or emojis).

Guardrails: no driver installs or software deployment here — this integration cannot run
scripts, so driver work is a spec plus a deep-link handoff. Queue migrations happen in a
change window with a rollback (the old server stays up until verified); never big-bang a
cutover in business hours.
```
