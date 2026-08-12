---
name: Warranty Claim Handling
description: When a device fails and you need to know whether it's under warranty, how to file the claim, and how to arrange a loaner while it's away.
category: Finance & Billing
tools: [search_tickets, get_ninjaone_device, search_ninjaone_devices, web_search, add_ticket_note]
connectors: [NinjaOne]
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Warranty Claim Handling

**When to use:** "Is this laptop still under warranty?" / "walk me through the warranty claim for the failed device on this ticket" / "device is going in for repair — sort out the loaner plan."

**Run it:** on one device/ticket, or across a batch of failed-device tickets you point me at — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Determine whether a failed device is plausibly under warranty, lay out the vendor's claim
steps, and produce a loaner-logistics note so the user stays working while the device is
repaired.

1. Identify the device from the ticket: make, model, serial/service tag. If an RMM is
   connected, look up the authoritative record in NinjaOne (serial, model, and OS install or
   first-seen date as an age hint).

2. Assess warranty status: search the web for the vendor's warranty terms and, where the
   vendor offers a public serial lookup page, point the tech at it with the serial ready to
   paste. If purchase records exist in the ticket or documentation, cite the purchase date
   against the warranty length. State your conclusion as a confidence level ("purchased
   <date>, 3-year warranty → likely covered until <date>"), never as certainty unless the
   vendor lookup confirmed it.

3. Lay out the claim steps for this vendor: what the vendor will ask for (serial, fault
   description, troubleshooting already done), the diagnostic evidence to gather from the
   ticket/RMM before calling, and whether the device class typically gets onsite service,
   mail-in, or advance replacement.

4. Draft the fault description for the claim from actual ticket evidence — symptoms, when it
   started, troubleshooting performed with results. No exaggeration to force approval;
   misrepresenting a fault can void the claim.

5. Loaner logistics: leave a plain-text note covering — loaner source (client spare pool vs
   MSP stock, per ticket/docs), data-migration or profile plan, what happens to the failed
   device's disk if the vendor requires return (wipe/remove per policy), expected turnaround,
   and return checklist for when the repaired unit is back.

6. Output: warranty verdict with its evidence and confidence, claim step list, fault
   description draft, and the loaner note.

Guardrails: never assert warranty coverage as fact without evidence (vendor lookup result or
purchase record + term) — "likely covered" with the reasoning shown is the honest default; the
vendor's own system is the final word. Out-of-warranty repair costs are a billing question:
whether repair/replacement is covered by the client's agreement is a contractual call — flag
it for the account owner (see Out-of-Scope Billing Flag). Data safety before hardware: never
send a device to a vendor with client data on an unencrypted disk without flagging the
wipe/retention step. Do not fabricate serials, purchase dates, or claim numbers; every
identifier comes from the ticket, RMM, or the requester. No RMM connected → work from
ticket-stated details and say the serial should be verified on the physical device.
```
