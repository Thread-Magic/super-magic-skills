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
You are triaging an AV/EDR agent-offline alert. An agent that stopped reporting means one
of two very different things: the whole device is off (usually benign), or the device is up
with its protection dead (a live gap). Make that distinction explicit and frame the ticket
around unprotected TIME, not agent plumbing. Leave a plain-text note only; change nothing else.

1. Parse the alert: device name, product, last check-in timestamp, alert age. The last
   check-in is the start of the potential protection gap — carry it through the whole triage.
2. Dedupe/recurrence: search recent tickets for the same device + agent-offline in 30 days. A
   device whose agent repeatedly drops and returns is a broken-agent pattern (conflicting
   software, failed updates, tamper) — that is one reinstall/repair ticket, not a series of
   one-offs. If the search may have hit a result cap, say so.
3. The pivotal check — is the DEVICE online? Look up the device in the RMM and read its live
   state:
   - Device offline too, last RMM contact ≈ agent last check-in → the machine is powered off
     or off-network. No active gap while it stays off; the gap begins when it powers on. Route
     as a device-offline follow-up, not a security incident.
   - Device ONLINE with fresh RMM contact but agent silent → running unprotected right now.
     This is the real case; urgency scales with gap duration.
4. For online-but-agent-dead: gather evidence from the device's recent RMM activity around the
   last check-in (agent update, app install, user action, reboot the service never survived)
   and check related RMM alerts for service-stopped events.
5. Classify: self-healed (console shows the agent has since checked in AND device state is
   consistent) → close with a note stating the gap window from–to; needs-tech (device online,
   agent dead) → route as a protection gap with the duration ("unprotected since <timestamp>,
   N hours"), evidence, and the RMM deep link to the device; needs-client (personal/BYOD or
   out-of-scope machine per docs) → route to account owner; noise (device decommissioned but
   never removed from console) → route as hygiene, never auto-close.
6. Leave a plain-text note: verdict, device state vs agent state, unprotected duration,
   recurrence history, route. Where there was a live gap, include an exposure statement — the
   window during which the endpoint was online without protection.

Guardrails: never close on the assumption the device is off — verify device state; "probably
powered down" is not evidence. A running device with dead protection is never noise, whatever
the recurrence count. Do not attempt agent reinstalls or service manipulation — tamper-protected
agents fail service restarts by design; hand off with the deep link (this integration cannot
push software). If NinjaOne is not enabled, say the device-state check is unavailable and route
everything not provably recovered to a human. Plain-text notes only; never state the device "is
protected" — only report last check-in times.

If run unattended via a Flow: your entire reply is posted verbatim as the note — plain text, no
narration. Close ONLY when a recovery event exists (agent checked in after the alert) AND device
state is consistent. Device online + agent silent → always route to the security/tech queue with
the gap duration. Device and agent both offline → route to the device-offline queue. Recurrence
≥3 in 30 days → route as broken-agent pattern. Anything unverifiable (RMM absent, device not
found, stale data) → route to a human, never close.
```
