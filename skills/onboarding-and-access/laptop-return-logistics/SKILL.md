---
name: Laptop Return Logistics
description: Get a company device back from a departing or remote user — coordinate the return box and prepaid label, send the templated return email with a deadline, confirm receipt, verify the wipe, update the asset record, then close. Includes the escalation path when the user goes silent.
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
Run this device return as a tracked sequence with dates on everything: box out, label
used, device received, device wiped, asset record updated, ticket closed. Nothing is
marked done until it verifiably happened.

1. Establish the facts on the ticket (read the ticket, look up the contact): who has the
   device, their current shipping address and personal contact (post-departure the work
   email may be dead — confirm a reachable address; the HR/client contact is the
   fallback), which device it is (asset tag/serial from the IT documentation in IT Glue
   or Hudu), and the return deadline per client policy.

2. Arrange the return kit: order the carrier return box with prepaid label per the
   desk's process (carrier portal or shipping vendor). Record the order confirmation and
   tracking number on the ticket when done — never note the box as ordered before it is.

3. Send the templated return email (draft the email where available; otherwise present
   the draft for a human to send): what to return (device + charger + accessories, by
   asset tag), what's coming (return box with prepaid label, expected arrival), how to
   pack it, the deadline, who to contact. Keep the tone neutral and procedural — this
   person may be a recent involuntary departure; no accusations, no legal threats
   (remedies for non-return are the client's call).

4. Track the sequence with dated plain-text notes and set follow-up checkpoints (schedule
   follow-ups): box delivered to user, label used / in transit, package received at
   destination.

5. On receipt: physically confirm the right device came back (asset tag/serial match
   against the record) and note condition and included accessories.

6. Wipe verification: the wipe itself runs through the desk's device-wipe process. This
   skill's job is verification — confirm the wipe action reports completed for THIS
   device before recording it, and note the completion evidence. If already remote-wiped
   pre-return, verify that status rather than re-running anything.

7. Update the asset record (IT Glue/Hudu per convention): status returned/in-stock,
   location, condition, wipe-verified date. If the docs tools are read-only for the
   tenant, note the exact record changes needed and route to whoever maintains the asset
   system — do not mark the record updated when only a request was made.

8. Close the ticket only when ALL of: device received and identity-confirmed, wipe
   verified, asset record updated (or update explicitly handed off). The closure note
   lists each with its date.

SILENT-USER ESCALATION: no response / box unused by a checkpoint → send a dated reminder
(attempt 2), then a final notice (attempt 3) stating the deadline and that non-return
escalates to the client contact — three-strikes, each attempt documented. After three
documented attempts with no return, hand off to the client's HR/management contact with
the full attempt timeline (payroll deduction, legal, police report are their remedies,
never threatened by the desk). In parallel, confirm the device is remotely locked/wiped
so a never-returned device is not a data risk.

Guardrails: zero-assumption rule throughout — box ordered, email sent, package received,
wipe completed, asset updated are each recorded only after they verifiably happened, with
a date; never convert "should happen" into "done". Wipe before closure is non-negotiable
when the device held company data. Verify the returned device is the RIGHT device (asset
tag/serial); wrong or partial returns keep the ticket open. Communications to a departed
employee are procedural and blameless. Personal shipping addresses are used for shipping
only — keep them out of client-visible notes. Notes are plain text and dated; this ticket
is the audit trail if the return becomes a dispute.
```
