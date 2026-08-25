---
name: Teams Rooms AV
description: Fix Microsoft Teams Rooms devices: room account sign-in, camera, mic, display, touch console health, calendar join failures, and restart discipline.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Teams Rooms AV

**When to use:** A meeting room won't join meetings, the calendar is blank, or it shows "no upcoming meetings" when there are; camera, microphone, speaker, display, or the touch console is dead or not detected; the room can't sign in, shows signed-out, or the resource account/license lapsed; or the room "just stopped working" and hasn't been restarted in a long time. General meeting call-quality troubleshooting is teams-call-quality.

**Run it:** on the one ticket you're working — a tech works the room device hands-on; not unattended.

## Prompt

```
A Teams Room is an appliance with a dedicated resource account, a bundle of USB peripherals
and a console — so "the room isn't working" is nearly always the account, a peripheral, the
calendar, or a device that has not restarted in weeks. Call quality belongs to
teams-call-quality.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: a
room-account password change (rooms sign in with a stored credential, so a rotation — or an
MFA or Conditional Access policy landing on the room account — silently signs it out; this
is the number one cause), a peripheral swap, a firmware update, a network change.
Documentation: the compute type (Windows or Android — troubleshooting and management
differ), the OEM model, the peripherals and how they connect, the display setup, and the
resource account's UPN, license and room mailbox (both required). Evidence: the device
itself — signed in or not, what the app shows, peripherals detected in device settings,
the calendar populating — plus the account's sign-in and license state.

1. Room account or sign-in — signed out, can't sign in, or a blank calendar. The stored
   credential broke on a password rotation, a Conditional Access or MFA policy written for
   people caught the room account, or the license or room mailbox lapsed. Fix the account or
   policy, then sign back in. Never disable MFA broadly to fix a room — exclude the room
   account properly and route the policy change to the identity owner.

2. Peripheral health — a device isn't detected or is dead. Check the physical connection and
   the USB hub or extender's power; long HDMI and USB runs and unpowered hubs are a top
   cause. Reseating plus a device restart re-enumerates USB. A genuinely failed peripheral,
   or cabling in the room fabric, is a hardware and AV-integrator path.

3. Calendar and meeting join — the room won't show or join meetings. Check the room
   mailbox's calendar processing (does it accept invitations and keep meeting details?),
   whether meetings were actually sent to the room, and whether the meeting is Teams-enabled.
   A room that shows meetings but can't join points back at sign-in or network; one that
   never shows them points at the mailbox configuration.

4. Restart discipline — laggy, frozen console, or odd one-off behavior. These devices are
   designed to restart nightly; one up for weeks accumulates problems. A controlled restart
   clears a surprising share of weird symptoms — do it early for one-off oddness, then set
   up or verify the scheduled restart.

Never hard power-cycle repeatedly as a fix, and keep the room account's credentials out of
PSA notes. Success is a real test meeting: the room joins, camera, microphone, speaker and
display work, the calendar is correct. Note in plain text (PSA Note Discipline base skill):
platform, device-state evidence, branch, action, verification.
```
