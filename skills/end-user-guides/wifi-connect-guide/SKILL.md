---
name: WiFi Connect Guide
description: Draft reply-ready instructions for an end user connecting a work device to wifi — office network, home network, and captive-portal awareness.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# WiFi Connect Guide

**When to use:** "Send <user> steps to get on the office wifi." / new device or new hire tickets where wifi is the first step / "user travels next week — send the hotel-wifi survival note."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for getting a work device online — the correct office
network by name, the home-wifi case, and the hotel captive-portal trap. Include only the branches
the ticket needs; an unrequested three-part guide dilutes the one answer the user wanted. Draft
only: show it first, send nothing.

1. Verify the client's wireless setup FIRST, from their documentation and past tickets: the office
   network's exact name (SSID) users should join, how it authenticates (certificate or auto-join on
   managed devices, work credentials, or a password), and whether a guest network exists that users
   should NOT put work devices on. If the name or auth style is unknown, ask the tech ONE
   question. NEVER put a wifi password in the draft — if the office network is
   password-based, say where to get it per documented practice, or have the tech deliver it out of
   band. Never invent an SSID.
2. Office branch, to end-user rules, one action per step with what-you'll-see cues:
   - Open the wifi list (cue it per platform in plain words) and pick the exact documented name:
     "if you see two similar names, the right one is exactly <documented SSID>."
   - The auth cue that applies: "it may just connect — that's our setup working" (certificate), or
     "a sign-in box appears; use your normal work login" (credentials).
   - The guest-network warning where the documentation confirms one exists — never speculate one
     into being: "<guest SSID> is for visitors' phones — work laptops don't belong on it, and
     printers and shared drives won't work there."
   - Off-ramp, always included: "If it asks for anything these steps don't mention, or refuses your
     work login twice, stop and reply — retrying can lock your account."
3. Home branch, if needed: join their own network with their router password, which the desk
   never needs or wants — say so. Then the one work-specific note from the documentation ("once
   online, the VPN handles the rest").
4. Captive-portal awareness for travel, if needed: "hotel and café wifi shows a welcome page
   before the internet works; your laptop may look connected but nothing loads until you accept
   it." Steps: connect, open the browser, try any plain website to trigger the page, accept, then
   connect the VPN. Honest caveat: "some public networks block work tools entirely — if the VPN
   won't connect after the welcome page, use your phone's hotspot instead" — include the hotspot
   line only where the documentation permits it; otherwise "reply and we'll advise."
5. Assemble per the Email Baseline Standard.

Guardrails: never transmit a wifi password in the draft and never invent an SSID — both come from
the documentation or the tech, or the draft doesn't ship. No admin steps (access-point config,
RADIUS, PSK rotation) in the user block. Localizable. Docs tools exist only when enabled.
```
