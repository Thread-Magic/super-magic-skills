---
name: Teams Meeting Guide
description: Draft reply-ready instructions for an end user to join and run a Teams meeting — audio and camera checks, screen sharing, recording basics.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Teams Meeting Guide

**When to use:** "User has a big Teams meeting tomorrow — send a how-to." / "Send <user> steps to share their screen / record the meeting." / post-incident follow-up after a meeting went badly.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for the anxious meeting host: how to join cleanly, check
audio before anyone hears them, share a screen, and — policy permitting — record. Size it to what
the user actually asked, not a full Teams manual. Draft only: show it first, send nothing.

1. Verify the environment FIRST, from the client's documentation and past tickets: that the
   client actually runs Teams rather than another platform, whether the user has the desktop app
   or joins via browser, and — if recording is in scope — whether policy permits recording for
   regular users. If the recording policy is unknown and the user asked about it, ask the technician
   ONE question rather than promising a button that may be disabled — a missing button the guide
   promised is a credibility hit.
2. Write ONLY the sections the user needs (join, audio, sharing, recording), each to end-user
   rules, one action per step with what-you'll-see cues:
   - Join: click the meeting link in the calendar invite; cue the pre-join screen — "you'll see
     yourself on camera with mic and camera buttons BEFORE anyone can see or hear you; nothing is
     live yet." This one cue removes most meeting anxiety.
   - Audio check: on the pre-join screen, confirm the named mic and speaker match their headset,
     and use the test-call check where available ("look for a settings gear there"). Off-ramp: "If
     your headset isn't in the list, stop and reply before the meeting — usually a quick fix on
     our side."
   - Sharing: the share button cue, and the key distinction in plain words — sharing one WINDOW
     (they only ever see that window, safest) vs the whole SCREEN (everything, notifications
     included). Recommend window-share by default, and close email and chat first either way.
   - Recording, ONLY if policy-verified: where the record option lives (the "…" more menu), the cue
     that everyone is notified recording started, where the recording lands afterwards, and the
     etiquette line — "announce you're recording." That line stays in every recording section;
     recording carries consent and legal weight in some places, so never advise covert recording.
     If policy blocks recording, say so plainly instead of describing a button they don't have.
   - Day-of safety net: "Join 5 minutes early. If anything looks different from these steps,
     reply or call the desk — before the meeting, not during."
3. Assemble per the Email Baseline Standard.

Guardrails: never describe features the client's policy disables. Sections the user didn't ask
for get one offer line ("Want a screen-sharing walkthrough too? Reply and we'll send it"). The
Teams interface shifts constantly — cue by name and purpose ("the camera button"), never by
position or icon. No admin steps (meeting policies, org settings) in the user block. Localizable.
Docs tools exist only when enabled.
```
