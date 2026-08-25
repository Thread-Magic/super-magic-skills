---
name: Device Offline Runbook
description: Work a device-offline alert or "won't connect" ticket — site-wide check first, maintenance windows, last activities, and clear escalate criteria.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, search_itglue, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Device Offline Runbook

**When to use:** A device-offline alert lands, "why is <device> offline?", or an offline device turned up in a fleet sweep and needs a verdict.

**Run it:** on one device/offline ticket · or as a Flow triggered when a device-offline alert lands on the ticket.

## Prompt

```
Rule out the big causes first — site outage, maintenance, decommission — then reconstruct
what happened from the device activity and give the tech precise on-site guidance or an
escalation. Needs the RMM connected; without it, fall back to ticket history and
documentation and say the RMM view was unavailable (Connector Degradation base skill).

1. Resolve the device: organization first, then look it up. Rank candidates by organization
   match, then most recent last-contact, and state your pick. Confirm the class in the
   device details, not from a filter.
2. Site-wide check FIRST. Pull the organization's other devices. Several at one site
   dropping around the same time is a network or site outage, not a device problem — say so
   and switch to Network Outage Triage.
3. Maintenance next. In a window, or one recently set? Offline inside planned maintenance
   is not an incident — note it and stop, unless the window has expired.
4. Build the timeline: exact last-contact from the device details, then recent activity for
   what happened just before it dropped — shutdown, reboot, agent update, logoff, patch.
   Repeated offline/online pairs in the alert history mean a flapper, pointing at NIC, power
   or Wi-Fi rather than hard failure.
5. Classify: clean shutdown before the drop means powered off; patch or reboot activity means
   hung during restart; nothing preceding means power, network path or hardware; last contact
   weeks ago means possibly retired.
6. Cross-check documentation and recent tickets — scheduled for replacement, reimage or
   decommission? Recent remote-session activity means another tech is on it: coordinate.
7. If it looks local or power-related, give concrete physical checks: power and LEDs, cable
   or Wi-Fi association, whether the machine responds locally, power-cycle guidance. You
   cannot see a powered-off machine — say what only on-site eyes can confirm.
8. Escalate when it is a server or shared infrastructure, hosts services others depend on,
   has been offline past the client's tolerance with no explanation, or the checks fail.
   Hand over the timeline, evidence, checks done, and next-tier steps.

Never mark an offline alert resolved just because the device came back — confirm stability
first, and closing is the requester's call. Distinguish "confirmed" from "likely" and claim
no cause you can't evidence. A long-offline device is flagged "verify still in service", not
worked as an incident. Offer the diagnostic as a note (PSA Note Discipline base skill).

As a Flow: your entire reply is the note. Input is the device id from the triggering alert —
never guess by name unattended; unresolvable device or no RMM means output nothing. Lead with
"PROBABLE SITE OUTAGE - not a device issue" and skip the per-device work when the site
dropped together; emit exactly "IN MAINTENANCE WINDOW - NO INCIDENT" inside a window. The
note is the only permitted write — never resolve or close the alert or ticket.
```
