---
name: Laptop Return Logistics
description: Get a company laptop back from a departing or remote user with prepaid return label, templated email, deadline tracking, wipe verification, and escalation.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_itglue, search_hudu, add_ticket_note, update_ticket, schedule_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Laptop Return Logistics

**When to use:** an offboarding ticket reaches the "recover the device" step for a remote or departed user / "get <user>'s laptop back" / "send a return box to <user>" / a device recovery has stalled and someone asks where it stands.

**Run it:** on one ticket — a tracked recovery sequence a human drives to close.

## Prompt

```
Run this device return as a tracked sequence with dates on everything: box out, label used,
device received, device wiped, asset record updated, ticket closed.

1. Establish the facts: who has the device; a reachable shipping address and personal contact
   (after a departure the work email may be dead; the HR or client contact is the fallback); the
   asset tag and serial from IT Glue or Hudu; the return deadline per client policy.

2. Order the carrier return box with prepaid label per the desk's process; record the
   confirmation and tracking number once done — never note the box as ordered before it is.

3. Send the templated return email, or draft it for a human to send: what to return (device,
   charger, accessories, by asset tag), what is coming and when, how to pack it, the deadline,
   who to contact. Keep it neutral and procedural — this may be a recent involuntary departure,
   so no accusations.

4. Track it with dated plain-text notes (PSA Note Discipline base skill) and follow-up
   checkpoints: box delivered, label used or in transit, package received.

5. On receipt, confirm the right device came back — asset tag and serial matched against the
   record — and note condition and accessories. Then verify the wipe: it runs through the desk's
   device-wipe process, and your job is to confirm it reports completed for THIS device before
   recording it, with the evidence. If it was remote-wiped before return, verify that status
   rather than re-running it.

6. Update the asset record in IT Glue or Hudu: status returned or in-stock, location, condition,
   wipe-verified date. If those tools are read-only for this tenant, write out the exact changes
   needed and route them to whoever maintains the asset system — don't mark the record updated
   when only a request was made.

7. Close only when all three hold: device received and identity-confirmed, wipe verified, asset
   record updated or handed off. The closure note lists each with its date.

SILENT USER: no response, or the box unused by a checkpoint — send a dated reminder (attempt 2),
then a final notice (attempt 3) stating the deadline and that non-return escalates to the client
contact. After three documented attempts, hand off to the client's HR or management contact with
the full timeline; payroll deduction, legal action and police reports are their remedies, never
threatened by the desk. In parallel, confirm the device is remotely locked or wiped so a
never-returned device is not a data risk.

Zero assumptions: box ordered, email sent, package received, wipe completed and asset updated are
each recorded only after they verifiably happened, with a date. A wipe before closure is
non-negotiable when the device held company data. Wrong or partial returns keep the ticket open.
Personal shipping addresses are for shipping only — keep them out of client-visible notes.
```
