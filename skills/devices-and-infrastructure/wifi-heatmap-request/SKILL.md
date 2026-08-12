---
name: WiFi Heatmap / Site Survey Request
description: Decide whether a wireless problem warrants a heatmap/site survey, and capture the complete site information needed to commission one so the surveyor isn't sent back for missing details. Use when someone asks for a WiFi survey, reports chronic coverage/roaming issues, or is planning a new-site wireless deployment.
category: Devices & Infrastructure
tools: [search_itglue, search_knowledge_base, search_ninjaone_devices, create_ticket, add_ticket_note, create_timezest_scheduling_request]
connectors: [IT Glue, NinjaOne, TimeZest]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# WiFi Heatmap / Site Survey Request

**When to use:** "We keep having WiFi problems — can we get a heatmap?", chronic coverage dead-spots or roaming drops at a site, or planning wireless for a new office/expansion.

**Run it:** on one site-survey request ticket, on demand (not a Flow — it produces a brief and can open a scheduling request a human reviews).

## Prompt

```
Separate wireless problems a survey will actually fix from ones it won't, then gather the full site brief so a heatmap/site survey can be commissioned in one pass.

1. Qualify first — a survey is warranted when the problem is coverage/capacity/interference or a greenfield design; it is often NOT the right first step when the cause is a config issue, a single failing AP, a WAN/circuit problem, or a client-device issue. Sanity-check current infrastructure via the wifi-infrastructure-audit skill and the RMM/documentation before recommending a survey, so you don't commission one for a problem a config fix would solve.
2. Pick the survey type: predictive (from floor plans, for design/new-build), passive (measure existing RF for coverage), or active (throughput/roaming validation). State which fits the stated goal and why.
3. Capture the site-info checklist needed to commission the survey — mark each item captured / missing:
   - Site: address, floors/areas in scope, approximate square footage, and a floor plan (to scale if predictive).
   - Environment: building construction (drywall vs concrete/brick, warehouse racking, cold storage), ceiling height, known RF challenges.
   - Requirements: expected client count and device types, high-density areas, coverage-critical zones (VoIP/handhelds/video), outdoor/warehouse coverage needs.
   - Existing WLAN: vendor/controller, AP models and count, current SSIDs and bands, mounting.
   - Access & logistics: point of contact, site access/escort, hours, and any areas requiring special access.
4. Note environmental constraints that change the survey (occupied vs empty building, seasonal stock levels in a warehouse) since they affect measured RF and when the survey should run.
5. Produce the survey request brief: recommendation (survey yes/no and type), the completed site-info checklist with any missing items called out, and the scope. If a site visit is needed, offer to open a scheduling request (requires TimeZest; if absent, skip and note the visit must be booked manually). Leave the brief as a plain-text note (no markdown/emojis) or open a ticket for the survey engagement.

Guardrails: don't commission a survey by default — if the evidence points to config, a single AP, or a WAN problem, say so and route to the appropriate skill instead. A brief with missing checklist items must ship with those gaps flagged, not filled with assumptions about the site. This skill produces a request/brief and can open a scheduling request; it does not dispatch a technician or commit a survey date without the scheduling step. Do not invent floor plans, square footage, or AP counts — mark them missing when unknown.
```
