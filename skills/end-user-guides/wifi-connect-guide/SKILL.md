---
name: WiFi Connect Guide
description: Draft reply-ready instructions for an end user connecting a work device to wifi — office network, home network, and captive-portal awareness — "send the user wifi connection steps."
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
network by name, the home-wifi case, and the hotel/café captive-portal trap. Include only the
branches the ticket needs. Verify the wireless setup before you write; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's wireless setup FIRST by checking the client's documentation and past tickets: the office network's exact name (SSID) users should join, how it authenticates
   (certificate/auto-join on managed devices, sign-in with work credentials, or a password), and
   whether a guest network exists that users should NOT put work devices on. If the network name or
   auth style is unknown, ask the technician ONE question. NEVER put a wifi password in the draft —
   if the office network is password-based, say where to get it per the client's documented practice
   or have the tech deliver it out-of-band. Never invent an SSID.
2. Office branch, to end-user rules, one action per step with what-you'll-see cues:
   - Open the wifi list (cue per platform in plain words), pick the exact documented name —
     "spelling matters; if you see two similar names, the right one is exactly <documented SSID>."
   - The auth cue that applies: "it may just connect — that's our setup working" (certificate), or
     "a sign-in box appears; use your normal work login" (credentials).
   - The guest-network warning where one exists: "the network called <guest SSID> is for visitors'
     phones — work laptops don't belong on it; printers and shared drives won't work there." (Only
     include this when docs confirm a guest SSID exists; never speculate one into being.)
   - Off-ramp: "If it asks for anything these steps don't mention, or refuses your work login twice,
     stop and reply — retrying can lock your account."
3. Home branch (if needed): join their own network normally (their router password, which the desk
   never needs or wants — say so), then the one work-specific note per docs (e.g., "once online, the
   VPN handles the rest").
4. Captive-portal awareness (travel, if needed): "hotel and café wifi shows a welcome/agree page
   before the internet works; your laptop may look connected but nothing loads until you accept it."
   Steps: connect, open the browser, try any plain website to trigger the page, accept, then connect
   the VPN. Honest caveat: "some public networks block work tools entirely — if the VPN won't
   connect after the welcome page, use your phone's hotspot instead" — include the hotspot line only
   if the client permits it per docs; otherwise "reply and we'll advise."
5. Assemble per the Email Baseline Standard.

Guardrails: never transmit a wifi password in the draft and never invent an SSID — both come from
docs or the tech, or the draft doesn't ship. An unrequested three-part guide dilutes the one answer
the user wanted. Work credentials on wifi sign-in can lock the account when mistyped repeatedly —
the stop-after-two off-ramp stays in. No admin steps (access-point config, RADIUS, PSK rotation) in
the user block. Localizable. The client's documentation is available only when those integrations are enabled.
```
