---
name: NinjaOne Device Lookup from a Ticket
description: Figure out which device a ticket is about — from the person, their remembered devices, or a hostname in the thread — find it in NinjaOne, and drop the live device details and a deep link into the ticket so the tech starts with context.
category: Devices & Infrastructure
tools: [search_tickets, search_contacts, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_link, add_ticket_note]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# NinjaOne Device Lookup from a Ticket

**When to use:** A ticket comes in about "my laptop" or a named PC and the tech wants the device pulled up before they start; or a Flow that enriches new device tickets with live RMM detail automatically.

**Run it:** on one ticket · or as a Flow (when a device/endpoint ticket is created).

## Prompt

```
Identify the device this ticket is about, look it up in NinjaOne, and post the key details plus a
link into the ticket so the tech doesn't have to go hunting.

1. Read the ticket. Pull out the end user (name and email) and any device clue in the thread —
   a hostname, PC name, asset tag, or serial.

2. Decide the best search term for the device, in this order:
   a. A specific device name/hostname stated directly in the ticket body — this wins.
   b. Otherwise, look up the contact and check what's remembered about them — any device names,
      hostnames, or asset tags tied to that person from past work — and use that.
   c. If neither gives a device, fall back to searching by the user's name to see what's registered
      to them.

3. Search NinjaOne for the device. Choose the match carefully:
   - One clear match → use it.
   - Several candidates → prefer the one that matches the hostname exactly, or (if you have to lean
     on the user) the device most recently online / clearly assigned to them. If you still can't
     tell which is theirs, list the candidates in the note rather than guessing.
   - No match → say so; don't attach an unrelated device.

4. For the chosen device, pull its live details — online/offline status, last-seen time, OS,
   logged-in user, and any open alerts — and get its NinjaOne link.

5. Leave a plain-text internal note with the device name, those live details, and the link so the
   tech can jump straight in. Include a one-line note on how you identified it (from the thread, from
   the contact's remembered devices, or by user name). If NinjaOne isn't connected for this tenant,
   say so and stop — never fabricate device data or a link. Notes bound for the PSA are plain text —
   no markdown, no emojis.

Only report what NinjaOne actually returns. Don't invent hostnames, statuses, or links, and don't
attach a device you're not confident belongs to this user.

Running as a Flow: do the lookup and leave the plain-text internal note; if the device can't be
confidently identified, leave a short note saying so rather than guessing. Your entire reply is the
internal note — no narration, no questions.
```
