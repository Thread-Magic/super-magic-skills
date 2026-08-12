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
Rule out the big causes first (site outage, maintenance, decommission), reconstruct what happened from the device activity, then give the tech precise on-site guidance or an escalation call. This needs the RMM connected; if absent, degrade to ticket history + documentation and say the RMM view is unavailable.

1. Resolve the device: organization first, then look it up in the RMM. Rank candidates by organization match then most recent last-contact; state your pick. Verify device class in the details — don't trust a class filter.
2. Site-wide check FIRST: pull the organization's other devices. If several at the same site dropped around the same time, this is a network/site outage, not a device problem — switch to Network Outage Triage and say so.
3. Check maintenance: is the device in a maintenance window, or was maintenance recently set? Offline inside planned maintenance is not an incident — note it and stop unless the window expired.
4. Establish the timeline: read the device details for exact last-contact; read the recent activity for what happened just before it dropped (shutdown, reboot initiated, agent update, user logoff, patch install).
5. Alert history: pull the device's alerts — is this a flapper (repeated offline/online pairs)? Flapping suggests NIC/power/Wi-Fi, not hard failure.
6. Classify the likely cause: clean shutdown before drop -> powered off; patch/reboot activity before drop -> hung during restart; no preceding activity -> power loss, network path, or hardware; last contact weeks ago -> possibly retired.
7. Cross-check documentation (IT Glue) and recent tickets: was this scheduled for replacement, reimage, or decommission?
8. Check whether another tech is already on it — recent remote-session/manual activity means coordinate, don't duplicate.
9. If it looks local/power: give concrete physical checks (power/LED, network cable/Wi-Fi association, whether the machine responds locally, power-cycle guidance). The agent cannot see a powered-off machine — say what only on-site eyes can verify.
10. Escalate when: it is a server or shared infrastructure; it hosts services others depend on; it has been offline past the client's tolerance with no on-site explanation; or physical checks fail. Escalation output: timeline, evidence, checks done, next-tier steps. Offer to leave the diagnostic as a plain-text note (no markdown/emojis).

Guardrails: never mark an offline alert resolved just because the device came back — confirm stability before closing, and closing is the requester's call. Do not claim a cause you cannot evidence; distinguish "confirmed" from "likely". Long-offline devices are flagged "verify still in service", not treated as incidents.

Unattended (Flow) mode: entire reply is the plain-text diagnostic note posted verbatim. Input is the device id from the triggering alert (never name-guessed unattended); device unresolvable or the RMM not enabled -> output nothing. Branches inside the note: multiple devices at the site dropped together -> lead with "PROBABLE SITE OUTAGE - not a device issue" and skip per-device diagnostic; device in an active maintenance window -> the note is exactly "IN MAINTENANCE WINDOW - NO INCIDENT." Permitted write: the note only — never resolve or close the alert/ticket.
```
