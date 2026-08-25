---
name: AV/EDR Agent Offline Alert
description: Triage an AV/EDR agent-offline alert — decide if the device is off or up with a dead agent, quantify unprotected time, and route on the protection gap.
category: Alert Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# AV/EDR Agent Offline Alert

**When to use:** An "agent offline / sensor not checked in / endpoint unhealthy" alert fires from any endpoint-protection product; or a tech asks "is <device> actually unprotected or just powered off?"

**Run it:** on the alert ticket · or as a Flow that fires on the agent-offline alert ticket event.

## Prompt

```
Triage an AV/EDR agent-offline alert. An agent that stopped reporting means either the device is
off (usually benign) or it is up with its protection dead (a live gap). Frame it around
unprotected TIME.

1. Parse the alert: device, product, last check-in timestamp, alert age. The last check-in starts
   the potential protection gap — carry it through.

2. Check recurrence for this device over 30 days. An agent that repeatedly drops and returns is a
   broken-agent pattern (conflicting software, failed updates, tamper) — one reinstall ticket,
   not a series of one-offs. Sweep Honesty base skill: flag a capped search.

3. The pivotal check is whether the DEVICE is online — read its live RMM state. Device offline
   too, last contact near the agent's last check-in: powered off or off-network, so no active gap
   while it stays off and the gap starts when it powers on; route as device-offline follow-up,
   not a security incident. Device ONLINE with fresh contact but the agent silent: running
   unprotected right now, urgency scaling with gap duration.

4. For online-but-agent-dead, read the device's RMM activity around the last check-in — agent
   update, app install, user action, a reboot the service never survived — and check for
   service-stopped alerts.

5. Classify, then note it — plain text, no markdown or emojis (PSA Note Discipline base skill):
   verdict, device versus agent state, unprotected duration, recurrence, route, and — for a live
   gap — the window the endpoint ran without protection. Self-healed (agent has since checked in,
   device state agrees): close stating the gap window. Needs-tech (device online, agent dead):
   route as a protection gap — "unprotected since <timestamp>, N hours" — with evidence and the
   RMM deep link. Needs-client (BYOD or out-of-scope machine per the documentation): account
   owner. Noise (device decommissioned, never removed from the console): route as hygiene, never
   auto-close.

Never close on the assumption the device is off — "probably powered down" is not evidence. A
running device with dead protection is never noise. Don't attempt agent reinstalls or service
restarts: tamper-protected agents block them by design and this integration can't push software;
hand off with the deep link. Never state a device is protected; report last check-in times. If
the RMM isn't connected, apply the Connector Degradation base skill: say the device-state check
is unavailable and send anything not provably recovered to a human.

As a Flow: your entire reply is the note. Close ONLY when the agent has checked in after the
alert AND device state agrees. Device online, agent silent: always route to the security queue
with the gap duration. Both offline: device-offline queue. Recurrence of 3+ in 30 days:
broken-agent pattern. Anything unverifiable (no RMM, device not found, stale data): route to a
human, never close.
```
