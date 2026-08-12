---
name: Device Health Check
description: Diagnose one device via the RMM — alerts, activities, services, disk, reboot, and patch posture — then propose remediation with a deep-link handoff.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, list_ninjaone_windows_services, get_ninjaone_device_link, search_itglue, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Device Health Check

**When to use:** "<user>'s computer is slow/freezing — what does the RMM say?", a ticket names a device by hostname, or you need a baseline before touching a machine.

**Run it:** on one device, on demand (not a Flow — it's a hands-on diagnostic a tech reaches for).

## Prompt

```
One-pass health read of a single device, ending in a concrete remediation proposal the tech can act on through a deep link. Read-only skill. This needs the RMM connected.

1. Resolve the device without stopping to ask mid-lookup: identify the client organization from the ticket/prompt, then look up its devices in the RMM. If multiple candidates match, rank by organization match first, then most recent last-contact, and state which one you picked and why. Only ask if candidates are genuinely indistinguishable.
2. Pull in parallel: the device details (status, OS, last contact, disk, pending reboot), its active alerts, its recent activity (last 24-72h), and its Windows services to spot stopped services set to Automatic.
3. Infer the device's role from its hostname prefix where the convention is evident (DC/AD = domain controller, SQL/DB = database, FS = file server, RDS/TS = terminal server, HV/ESX = hypervisor). Say it is an inference, not a fact.
4. Check the recent activity for another tech already working the device (remote sessions, manual actions). If someone is active, flag it before proposing anything.
5. Co-hosted-VM contention check: if the device shares a public IP with other devices in the same organization, list those siblings and check whether any carries resource alerts.
6. Assess posture: disk free space (flag under ~15% or under 10 GB on system volume), pending reboot age, patch status and failed-patch activities, repeated/flapping alerts.
7. Cross-reference documentation (IT Glue) when available to confirm the asset and pick up known quirks.
8. Output a health summary: status line, risks ranked by severity, inferred role, and a remediation proposal per risk. For any hands-on remediation, hand the tech a deep link into the device in the RMM so they jump straight to it. Offer to leave the summary as a plain-text note (no markdown/emojis).

Guardrails: don't trust a class filter — verify the returned device's class in its details before reasoning about it as a server or workstation. If any listing may have capped, report counts as "at least N", never exact. This skill is read-only; actions (reboot, service restart) belong to the dedicated action skills and require requester confirmation before affecting a logged-in user. Role inference from hostname is a hint, never confirmed without documentation backing. If the RMM is not enabled, say so and fall back to ticket history and documentation only; do not fabricate device data.
```
