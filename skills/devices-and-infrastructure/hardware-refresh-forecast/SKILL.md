---
name: Hardware Refresh Forecast
description: Build a 4-5-year refresh-cycle workbook for a client — which devices cross the age threshold in each upcoming period and what the per-client refresh budget looks like. Use for "refresh forecast for <client>", budget planning, or vCIO roadmap prep.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, search_itglue, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Hardware Refresh Forecast

**When to use:** "Which of <client>'s machines are due for replacement, and when?", or annual budget / vCIO roadmap prep needs a refresh line item.

**Run it:** across a client's whole fleet, on demand for budget/roadmap planning (not a Flow — it's a planning workbook, not a per-ticket event).

## Prompt

```
Turn fleet age data into a forward budget: devices grouped by the period they hit refresh age on a 4-5-year cycle, with unit counts and an estimated spend the client can plan against. This needs the RMM connected.

1. Confirm assumptions before computing, asking only if unstated: refresh cycle length (default 4 years laptops, 5 desktops, 5 servers), forecast horizon (default 3 years, by year or quarter), per-unit budget figures. If no unit costs are given, produce the forecast in unit counts and mark the spend column "pending unit pricing" — do not invent prices.
2. Pull the fleet and per-device details from the RMM. Verify class per device (laptop/desktop/server drive different cycles) — don't trust a class filter. Flag result caps; a truncated fleet makes the budget wrong, so page to full coverage or state the floor.
3. Establish each device's age from the strongest signal: documented purchase/deploy date (IT Glue) first, CPU-generation release window second, first-seen/OS-install date as a floor. Record which signal was used per device.
4. Exclude noise: devices offline 30+ days (verify still in service before budgeting their replacement) and devices already flagged for decommission.
5. Compute the workbook: per forecast period, the devices crossing the cycle threshold (device, class, age signal, current age), unit count per period, and spend per period where unit costs exist. Add a "past due" bucket for devices already beyond cycle — these front-load the first period.
6. Fold in known accelerators: devices terminally blocked from the current OS path (from a Win11 Readiness run, if available) move to the earliest period regardless of age.
7. Output the forecast as a period-by-period table plus a one-paragraph summary (fleet size, average age, past-due count, first-period spend). Offer a plain-text summary note (no markdown/emojis); note the client-facing version should be sanitized through the Client-Facing Device Report skill.

Guardrails: every age is labeled with its evidence signal; floors are stated as floors (a budget built on invented ages is worse than none). Never invent unit pricing, vendor quotes, or procurement timelines — counts are facts, dollars require inputs. Possibly-retired devices are excluded and listed for verification, not silently budgeted. This is a planning artifact, not a quote — say so. Result-cap honesty on all fleet listings. Degrade gracefully if the RMM is absent.
```
