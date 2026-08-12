---
name: Server Diagnostics
description: Deep single-server review — services, activities, alert history, role inference, and change correlation via Liongard detections when the tenant is on.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_windows_services, get_ninjaone_device_activities, list_ninjaone_alerts, liongard_detection, liongard_timeline, get_ninjaone_device_link, add_ticket_note]
connectors: [NinjaOne, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Server Diagnostics

**When to use:** A server is slow or throwing alerts, "what happened on <server> last night?", or escalation prep on any server-class ticket.

**Run it:** on one server, on demand (not a Flow — it's a hands-on deep diagnostic, read-only).

## Prompt

```
A deeper cut than Device Health Check, for servers only: full service-state review, activity forensics, alert-pattern reading, role inference, and — when Liongard is on — correlation with detected environment changes. This needs the RMM connected. Read-only.

1. Resolve organization then server in the RMM; rank candidates by organization match then last-contact. Confirm from the device details that it really is a server — don't trust a class filter.
2. Infer the server's role from its hostname prefix (DC/AD, SQL/DB, FS, EX/MAIL, RDS/TS, HV/ESX, APP, WEB, BK/BAK) and cross-check against what services are actually running — a box named APP01 running SQL Server is a database server whatever its name says. State inferences as inferences.
3. Pull in parallel: its Windows services (stopped Automatic services, and the state of role-critical services for the inferred role), its recent activity (last 72h — reboots, patch installs, service events, remote sessions), and its alerts (active and recent — look for flapping and the first-occurrence time of the current problem).
4. Check whether another tech is already on the server: recent remote-control or manual activity. If so, surface it and coordinate rather than diagnosing in parallel.
5. Change correlation — when Liongard is enabled, read the environment's posture (detected changes and system timeline) over the incident window: config changes, new admin accounts, DNS/AD changes, license or policy shifts that line up with the first alert. When Liongard is not enabled, correlate using RMM activity only and say the change view is limited to the device itself.
6. Read the posture basics too: disk on all volumes (not just system), pending reboot age, uptime, patch failures.
7. Synthesize: what is broken, since when, what changed around that time, who else is involved, and the most probable cause ranked against alternatives.
8. Propose remediation as steps for the tech with a deep link into the device in the RMM. Anything hands-on (service restarts on domain-critical services, reboots, storage work) happens through the tech or the dedicated action skills — with user-impact confirmation first. Offer to leave the diagnostic as a plain-text note (no markdown/emojis).

Guardrails: servers get a higher bar — never restart services or reboot from within diagnostics, even if a fix looks obvious; hand off with the deep link or route to the Service Restart / Reboot skills, which carry their own gates. Distinguish evidence-backed findings from inference in the output ("activity shows X at 02:14" vs "hostname suggests this is a DC"). Flag result-cap truncation on alerts/activity — an incident window with capped results may be missing the key event. If the server hosts shared services, note the blast radius before proposing disruptive remediation. Liongard absent -> say change correlation is degraded; do not invent a change history.
```
