---
name: Hardware Diagnostics
description: Work suspected hardware faults on desktops and laptops — no-boot, random shutdowns, disk noises, battery/thermal complaints — through the POST/boot-stage ladder, storage and battery health reads, and warranty routing.
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
Hardware tickets reward discipline: identify where in the power-on sequence the machine fails, read the health data the machine already keeps (SMART, battery, thermals), and route to warranty with the vendor's required evidence instead of parts-cannon guessing. Software playbooks handle the OS; this one owns the metal.

Work it in this order:

1. History first. Search this device's past tickets — prior thermal/disk/crash tickets make today's symptom a progression, not a debut, and change the answer toward replacement. When the RMM is connected: check the device record for model, age, disk health, and last-seen, and its recent activity for alerts and the shutdown/crash pattern. When RMM/documentation integrations are absent for the tenant, note that and ask the tech to read these manually.

2. Docs second. Check the client's documentation and knowledge base for the device's record: purchase date, warranty status/vendor, and the client's refresh policy — a machine past refresh age gets minimal diagnosis and a replacement recommendation, and say so early.

3. Identify the machine precisely. Vendor, model, and serial/service tag (from the chassis, firmware screen, or RMM). The serial drives everything downstream: vendor diagnostics, warranty lookup, and the support case.

4. Ladder the power-on sequence — where it stops is the diagnosis:
   - No power (no lights, no fans) — power path: outlet/strip verified, the correct adapter genuinely seated both ends (laptop adapters fail more than laptops — swap a known-good one before anything), battery-only vs adapter-only behavior, and the vendor's documented power-drain/reset procedure for the model (verify on the web). Desktop: PSU switch/cable, then PSU itself.
   - Power but no POST (fans/lights, no display, or beep/blink codes) — capture the beep pattern or diagnostic-LED code exactly and decode it against the vendor's documentation for this model — never generically (codes differ per vendor/line). The code names the subsystem (memory, board, GPU). Reseat what the vendor's guidance allows (RAM is the classic); board-level faults -> warranty branch.
   - POSTs but no boot device / boot loops — firmware sees the disk? If absent/intermittent -> storage branch. Present but won't boot -> the line between hardware and OS: run the vendor's built-in hardware diagnostics (every major vendor ships one at boot) before OS repair, so a dying disk doesn't eat an afternoon of OS surgery.
   - Boots but misbehaves under load (shutdowns, freezes, throttling) -> thermal/power branch or memory (vendor diagnostic's memory test; varying BSOD codes corroborate — pair with the BSOD playbook).

5. Storage health. Read SMART status (the RMM surfaces it when connected; otherwise the vendor diagnostic or OS tools). Any pre-failure indicator, reallocated-sector growth, or audible clicking = treat as failing now: stop diagnostics that stress the disk, verify backup/sync state immediately, image or copy data off per the client's practice, then replace. Data first, hardware second — always in that order, and say so to the user.

6. Battery and thermals. Battery: generate/read the platform's battery health report (design vs full-charge capacity, cycle count); below the vendor's service threshold or swelling (any deformation = stop using the device immediately, do not charge it — safety first) -> battery replacement via warranty or parts. Thermals: temperatures at idle vs load, fan behavior, vent condition — dust and blocked vents fix half of these; repeated thermal shutdowns after cleaning -> cooling-system fault, warranty/repair branch.

7. Warranty routing — with the evidence the vendor demands. Look up warranty by serial on the vendor's site (on the web / the documented portal). In warranty: open the case with what vendors require — serial, the diagnostic code or the vendor-diagnostic's failure ID (the onboard diagnostics emit an error code precisely for this), symptom description, troubleshooting already done. Capture the case number in the ticket. Out of warranty: cost the repair against the client's refresh policy and the device's age, and recommend honestly — an out-of-warranty board replacement on a five-year-old laptop is rarely defensible; write the numbers.

Guardrails to hold throughout: data before hardware — at any failing-storage signal, backup/imaging comes before further diagnostics or repair (a warranty replacement doesn't return the client's files, and say so plainly). Decode beep/LED/diagnostic codes only against the vendor's documentation for that model on the web — never from generic memory; wrong decode sends the wrong part. Swollen batteries are a safety stop: cease use and charging immediately, handle per the vendor's guidance — no troubleshooting continues on that device. Physical repairs follow the vendor's service procedures and warranty terms — opening what the warranty says not to open voids it; when the vendor's depot/onsite is the entitled path, route there instead of bench heroics, and say when only the vendor can act. No remote execution — RMM reads inform, but hands-on steps are the tech's or user's; open the device in the RMM (a deep link for the tech, not script execution) for the handoff when it's connected. Recommend replace-over-repair with numbers (age, refresh policy, repair quote) — not vibes; the client decides with the evidence in front of them.

Verify and note. Post-repair: re-run the vendor diagnostic clean, and the user works a normal day without recurrence. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): model/serial, ladder stage reached, codes/health data captured, data-preservation status, branch, warranty case number if opened, verification.
```
