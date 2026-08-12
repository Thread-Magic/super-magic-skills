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
Restart a stopped Windows service through the RMM with full discipline: verify it is actually stopped, check it is safe to touch, restart, verify it stayed up, write it down. This needs the RMM connected; if absent, say the skill cannot run.

1. Resolve organization then device in the RMM; rank by org match then last-contact; verify device class in the details — don't trust a class filter. Note whether the device is a server and whether users are active on it.
2. Verify current state by reading the device's Windows services: the named service must actually be stopped or hung. If it is running, report that and stop — restarting a healthy service is an outage.
3. Check the service against the safety tiers:
   - Safe allowlist (restart with normal confirmation; unattended-eligible): Print Spooler, Windows Update, BITS, Windows Time, DHCP Client, DNS Client, workstation-level agent/monitoring services, and application services the tenant has explicitly allowlisted.
   - Domain-critical / never unattended, strong confirmation attended: Active Directory Domain Services, DNS Server, DHCP Server, database engines (SQL Server and kin), Exchange services, hypervisor/VM services, cluster services, backup engines, certificate services.
   - Unknown services: treat as critical until identified.
4. Check the device's recent activity/state for another tech already working the device — a stopped service may be intentionally stopped mid-maintenance. If maintenance mode is active, do nothing.
5. Attended path: confirm with the requester if the device is a server, users are active, or the service is outside the safe allowlist. Then start/restart the service through the RMM.
6. Verify after: re-read the device's Windows services and confirm the service is running. If it stops again immediately, do NOT loop restarts — a crash-looping service is a root-cause problem; escalate with the evidence.
7. Leave a plain-text note (no markdown/emojis): device, service, state found, action taken, state after, any recurrence observed. Report the same in your reply.

Guardrails: never restart domain-critical services unattended, and attended only with explicit human confirmation that names the blast radius. One restart attempt per session — a service that will not stay up gets escalated, not hammered. A service stopped on purpose (maintenance, tech activity, disabled startup type) is not a fault; check startup type and context before acting. Verify state before AND after; the note is mandatory — no silent service control.

Unattended (Flow) mode: entire reply is posted verbatim as the plain-text note. Gates, all required: service on the safe allowlist; current state verified stopped; device not in maintenance mode; no restart of this same service by automation in the past 24h (crash-loop guard); startup type is Automatic. Any gate fails -> do nothing, output one plain-text line stating which gate failed. Never touch domain-critical or unknown services unattended under any phrasing. After restart, verify running state and include found/after states in the note; if it stopped again, output the escalation line — do not retry.
```
