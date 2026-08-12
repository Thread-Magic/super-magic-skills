---
name: Conference Room AV
description: Keep Teams/Zoom Rooms working — room-system health, calendar and resource-mailbox checks, and a pre-meeting checklist for high-stakes boardroom events.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, get_ninjaone_device_activities, get_ninjaone_device_link, search_itglue, search_hudu, search_tickets, add_ticket_note, create_ticket, schedule_ticket]
connectors: [NinjaOne, IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Conference Room AV

**When to use:** "<room> isn't joining meetings / screen is black / nobody can hear us", bookings misbehaving, or "the board meets Thursday — make sure the room works".

**Run it:** on one room's ticket, on demand (not a Flow — proactive pre-meeting checks need scheduling, which Flows can't trigger).

## Prompt

```
Treat each meeting room as a small system — room device, display, camera/mic, calendar identity, network — and check it as a system.

1. Identify the room's stack from documentation (IT Glue / Hudu): platform (Teams Rooms, Zoom Rooms, or ad-hoc PC + peripherals), the room compute device hostname, the resource-mailbox address it books under, peripheral inventory. Undocumented room = finding one.
2. Device health: look up the room device in the RMM — resolve the client organization then the device without stopping to ask mid-lookup, and don't trust a class filter — for last contact, pending reboot, disk, OS/app update state; pull its active alerts and recent device activity for recent errors. Room systems degrade after weeks of uptime — a pending reboot older than vendor guidance is a top suspect. Peripheral faults need eyes-on: hand the tech a deep link into the device in the RMM plus a physical checklist (cables, HDMI/USB, display input).
3. Calendar-integration check when bookings misbehave: verify the resource mailbox exists and auto-accepts, the room device is signed into that account, and its password/certificate hasn't expired (sign-in expiry is the classic "console shows no meetings" cause). Mailbox-side fixes are an M365 admin handoff — specify exactly what to check; never place account passwords in notes.
4. Pattern check: read this room's ticket history. Three tickets in a month is one unreliable room, not three incidents — recommend the systemic fix (reboot schedule, firmware, replacement).
5. Pre-meeting checklist (proactive): schedule a follow-up ticket for the business day before. Remote pass: device online, healthy, no pending reboot, signed in, meetings visible on console, updates not about to auto-install mid-meeting. On-site pass (hand off as checklist): test call, verify camera/mic/speaker/display and content sharing, booking shows on the panel. Report pass/fail per item — never "should be fine".
6. Output: room status, cause hypothesis with evidence, actions taken vs handed off, checklist results for proactive checks. Leave plain-text notes (no markdown/emojis); open a ticket for systemic fixes.

Guardrails: never reboot a room system during business hours without checking the calendar for in-progress or imminent meetings. Sign-in and mailbox changes are handed to the M365 administrator, not performed here. A remote "all green" is not a pre-meeting pass — report unverified on-site items as unverified. If the room hardware is under an AV integrator's contract, package and route rather than opening the rack. Degrade gracefully if the RMM/docs are absent.
```
