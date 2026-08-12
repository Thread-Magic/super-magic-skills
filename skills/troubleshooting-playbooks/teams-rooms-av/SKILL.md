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
You are diagnosing a Microsoft Teams Rooms device. A Teams Room is an appliance with a dedicated resource account, a bundle of USB peripherals, and a console — and "the room isn't working" is usually one of those four: the room account, a peripheral, the calendar, or a device that just needs the disciplined nightly-style restart. Check the device's own state and the room account before blaming Teams the service. General meeting call-quality belongs to teams-call-quality instead.

Work it in this order:

1. Device, platform, and room account first. Check the client's documentation and knowledge base for the room: the compute type (Teams Rooms on Windows vs Android — troubleshooting and management differ), the OEM/model, the peripherals (camera/mic/speaker/console make and connection), the display/HDMI setup, and the resource/room account (UPN, license — a Teams Rooms Pro/Basic license and a room mailbox are both required). Note whether the device is managed via the Teams Rooms Pro Management portal / Teams admin center. Documentation coverage varies per tenant — note what you couldn't check.

2. History first. Search this client's past tickets for this room: a recent room-account password change (rooms sign in with a stored credential — a password rotation or an MFA/Conditional-Access policy applied to the room account silently signs it out; this is the #1 "room stopped working"), a peripheral swap, a firmware/app update, or a network change. A room that died on a date usually traces to the account or a policy.

3. Read the device's own state before theorizing. On the console/device: is it signed in, what does the app show, are peripherals detected (the device settings list each one), and is the calendar populating? For account issues, check the room account's sign-in and license/mailbox state. Read the device — the user's phone-side experience of the same meeting is not the room's diagnosis.

4. Branch:
   - Room account / sign-in — signed-out, "can't sign in", or blank calendar: the stored credential broke (password rotated), the account got hit by a Conditional Access / MFA policy meant for people (room accounts need to be excluded or use resource-account-appropriate auth), or the license/room mailbox lapsed. Fix the account/policy, not the device — re-sign-in after correcting the cause. Escalate the CA/policy question to the identity owner; pair with m365-signin-issues. Never disable MFA broadly to fix a room — exclude the room account properly.
   - Peripheral health — a device isn't detected or is dead: Teams Rooms is USB-peripheral dependent — check the physical connection, USB hub/extender power (long HDMI/USB runs and unpowered hubs are a top cause), and whether the console shows the device. Reseating and a device restart re-enumerate USB; a genuinely failed peripheral is a hardware replacement. Escalate when it's failed AV hardware or cabling in the room fabric — that's a hardware/AV-integrator path.
   - Calendar / meeting join — the room won't show or join meetings: the room mailbox's calendar processing (does it accept and keep meeting details?), whether meetings were sent to the room, and whether the meeting is Teams-enabled. A room that shows meetings but can't join points back to sign-in/network; a room that never shows them points at the mailbox/calendar-processing config. Pair with the M365 admin side for mailbox calendar settings.
   - Restart discipline / app state — laggy, frozen console, or odd one-off behaviour: Teams Rooms devices are designed to restart regularly (a nightly maintenance restart is the vendor recommendation) and a device up for weeks accumulates problems. A controlled restart (not a hard power-pull) clears a surprising share of "weird" symptoms — do this early for one-off oddness, and set up/verify the scheduled restart if it's missing.

5. Verify and note. Success is a real test meeting: the room joins, camera/mic/speaker/display work, and the calendar shows correctly. Leave a plain-text internal note: platform (Windows/Android), the device-state evidence, branch (account/peripheral/calendar/restart), action or handoff, verification.

Rules throughout:
- No remote execution / script push — device, console, and portal steps are guidance for a tech on-site or an admin; hand off via the RMM/management portal deep link when that integration is enabled, otherwise ask the tech to do it. A controlled restart is fine; never hard-power-cycle repeatedly as a "fix". Never claim you restarted or reconfigured the device yourself.
- Room resource accounts are identities — never disable MFA/Conditional Access org-wide to fix one room; exclude the room account per Microsoft's guidance and route the policy change to the identity owner. Keep the room account's credentials out of PSA notes.
- Failed AV hardware/cabling is a hardware/integrator path — package the symptom, don't keep reseating a dead peripheral.
- Set up or verify the scheduled maintenance restart rather than relying on manual reboots — it prevents recurrence.
- Do not invent license SKUs, portal paths, or peripheral behaviours — check Microsoft's current Teams Rooms docs on the web and cite (Windows vs Android differ).
- Notes destined for a PSA sync are plain text: no markdown, no emojis, raw URLs rather than markdown links.
```
