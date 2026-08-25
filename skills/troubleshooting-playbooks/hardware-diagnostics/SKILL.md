---
name: Hardware Diagnostics
description: Work desktop and laptop hardware faults — no-boot, random shutdowns, disk noises, battery and thermal — through POST stages, SMART, and warranty routing.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Hardware Diagnostics

**When to use:** A machine won't turn on or won't boot (any stage of dead); random shutdowns, freezes under load, fan roar, or a burning-hot laptop; a clicking/grinding disk, "SMART error" messages, or suspected failing storage; or a battery that dies in an hour and a repair-vs-warranty-vs-replace decision.

**Run it:** on the one device ticket you're working — a tech drives the hands-on checks and warranty routing; not unattended.

## Prompt

```
Find where in the power-on sequence the machine fails, read the health data it already
keeps, and route to warranty with the evidence the vendor demands.

Climb the Troubleshooting Ladder base skill first: past tickets for this device — prior
thermal, disk or crash tickets make today's symptom a progression, not a debut;
documentation for purchase date, warranty vendor and refresh policy: past refresh age
means minimal diagnosis and an early replacement call. With the RMM connected, read the
device record and activity, and hand the tech its deep link. Then get vendor, model and
serial — it drives diagnostics, warranty and the case. Where the sequence stops is the
diagnosis.

1. No power at all — outlet and strip, the adapter genuinely seated both ends (adapters
   fail more often than laptops, so swap a known-good one first), battery-only vs
   adapter-only, then the vendor's documented power-drain procedure. Desktop: PSU switch
   and cable, then the PSU.

2. Power but no POST — capture the beep or blink pattern exactly and decode it against the
   vendor's documentation for this model, never generically — a wrong decode orders the
   wrong part. Reseat only what the vendor allows; board-level faults go to warranty.

3. POSTs but won't boot — does firmware see the disk? Absent or intermittent is the
   storage branch. Present: run the vendor's built-in diagnostics before OS repair, so a
   dying disk doesn't eat an afternoon.

4. Boots but misbehaves under load — run the vendor diagnostic's memory test and read
   varying BSOD codes as corroboration; otherwise it's thermal or power.

Storage: any SMART pre-failure indicator, reallocated-sector growth or clicking means
failing now. Stop stressing the disk, verify backup state, copy or image the data off,
then replace. Data first, hardware second: a warranty replacement does not return their
files.

Battery and thermals: read the battery health report — design versus full-charge capacity,
cycle count — and replace below the vendor's threshold. Any swelling is a safety stop:
cease use, do not charge it, troubleshoot nothing further on that device. Compare idle and
load temperatures and check vents: dust fixes half, and shutdowns after cleaning are a
cooling fault.

Warranty routing: look up warranty by serial. In warranty, open the case with what vendors
require: serial, the diagnostic code or onboard failure ID, the symptom, the
troubleshooting done. Capture the case number. Out of warranty, cost the repair against
age and refresh policy; recommend with numbers, not vibes. Opening what the warranty
forbids voids it: when depot or onsite is entitled, route there over bench heroics.

Success is a clean vendor-diagnostic re-run and a normal working day. Note it (apply the
PSA Note Discipline base skill): model and serial, ladder stage, codes and health data,
data status, branch, warranty case number.
```
