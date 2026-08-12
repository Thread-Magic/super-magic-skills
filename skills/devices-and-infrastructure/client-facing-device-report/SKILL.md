---
name: Client-Facing Device Report
description: Produce a sanitized device inventory and health report a client contact can read — counts, health summary, and risks in business language, no internal jargon, no raw tool output. Use for "send <client> a summary of their devices" or QBR fleet slides.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, add_ticket_note]
connectors: [NinjaOne]
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Client-Facing Device Report

**When to use:** "Put together a device report I can send to <client>" or QBR/vCIO prep needs the fleet section in client-ready form.

**Run it:** across a client's whole fleet, on demand for a report or QBR (not a Flow — it's a reporting pass, not a per-ticket event).

## Prompt

```
Build the fleet story for the client's eyes: how many devices, how healthy, what risks deserve budget — written for a business reader, stripped of RMM jargon and anything internal. This needs the RMM connected.

1. Resolve the client organization and pull the fleet from the RMM — the device list, each device's details, and its active alerts. Verify device classes in the details, don't trust a class filter. If listings hit caps, get full coverage by segment before writing — a client-facing count must not be truncated; if full coverage is impossible, present ranges honestly ("more than N").
2. Compute client-safe aggregates: total managed devices split by type (computers, laptops, servers); healthy vs needing attention; devices nearing replacement age; operating systems approaching end of support.
3. Translate into business language. NO: internal-infrastructure hostnames beyond what the client knows, alert codes, RMM/tool names, node classes, internal tech names, ticket numbers, raw metrics. YES: "3 computers are running low on storage and may slow down", "2 machines run a Windows version that stops receiving security updates in <month/year>".
4. Frame risks as recommendations with a why, not alarms: each risk gets one plain sentence of impact and one of what you propose. Never imply negligence, never speculate about security incidents, never promise outcomes or prices.
5. Structure: one-paragraph summary (fleet size, overall health statement), a small counts table, "What needs attention" (3-5 items ranked), "Planning ahead" (aging hardware / OS end-of-support), "What we're doing" next steps. Keep it to one page.
6. Show the draft to the requester for review before it goes anywhere — this produces the draft; sending it to the client is the human's call. Offer to attach it as a plain-text note on the ticket.

Guardrails: nothing internal leaks — read the draft once as the client before delivering. Numbers must be exact or honestly ranged (a wrong count in front of a client damages trust and billing). No security claims either direction. No pricing, quotes, or committed dates — planning items point to a follow-up conversation. The requester reviews before any client delivery; this skill never sends anything itself. Write in the client's language if asked; avoid idioms. Degrade gracefully if the RMM is absent (say the live fleet view is unavailable).
```
