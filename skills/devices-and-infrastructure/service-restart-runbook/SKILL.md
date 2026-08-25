---
name: Service Restart Runbook
description: Restart a crashed Windows service via the RMM — allowlisted safe services only, state verified before and after, with a ticket note posted on completion.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_windows_services, control_ninjaone_windows_service, add_ticket_note]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Service Restart Runbook

**When to use:** A stopped-service alert fires (spooler, agent services, app services) or "restart the <service> on <device>".

**Run it:** on one device/service ticket · or as a Flow triggered when a stopped-service alert lands on the ticket.

## Prompt

```
Restart a stopped Windows service through the RMM with discipline: verify it really is
stopped, check it is safe to touch, restart, verify it stayed up, write it down. With no
RMM connected, say the skill cannot run.

1. Resolve organization then device in the RMM, ranking by org match then last-contact;
   verify class in the details (a class filter is not evidence). Note whether it is a
   server and whether users are active.

2. Verify current state from the device's Windows services: the named service must really
   be stopped or hung. If it is running, report that and stop — restarting a healthy
   service is an outage.

3. Check the service against the safety tiers:
   - Safe allowlist (normal confirmation; unattended-eligible): Print Spooler, Windows
     Update, BITS, Windows Time, DHCP Client, DNS Client, workstation agent and monitoring
     services, plus application services the tenant has explicitly allowlisted.
   - Domain-critical, never unattended, attended only on strong confirmation: Active
     Directory Domain Services, DNS Server, DHCP Server, database engines (SQL Server and
     kin), Exchange, hypervisor and VM services, cluster services, backup engines,
     certificate services.
   - Unknown services: treat as critical until identified.

4. Check recent activity for another tech on the device — a service may be stopped on
   purpose mid-maintenance. If maintenance mode is active, do nothing.

5. Attended: confirm with the requester if the device is a server, users are active, or
   the service is outside the safe allowlist. Restart it through the RMM, then re-read the
   services to confirm it is running. If it stops again immediately, do NOT loop restarts
   — a crash-looping service is a root-cause problem: escalate with the evidence.

6. Leave a note: device, service, state found, action taken, state after, any recurrence
   (apply the PSA Note Discipline base skill — plain text, no markdown or emojis); report
   the same in your reply.

Guardrails: domain-critical services are restarted only on explicit human confirmation
naming the blast radius. One restart attempt per session — a service that won't stay up is
escalated, not hammered. A service stopped deliberately (maintenance, disabled startup
type) is not a fault — check startup type and context first. The note is mandatory: no
silent service control.

As a Flow: your entire reply posts verbatim as the note. Gates, all required: on the safe
allowlist; verified stopped; device not in maintenance mode; no automated restart of this
same service in the past 24h (crash-loop guard); startup type Automatic. Any gate fails ->
do nothing, output one line naming the gate. Never touch domain-critical or unknown
services unattended, under any phrasing. After restarting, include found/after states in
the note; if it stopped again, output the escalation line and do not retry.
```
