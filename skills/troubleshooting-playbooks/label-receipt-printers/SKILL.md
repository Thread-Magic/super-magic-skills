---
name: Label and Receipt Printers
description: Troubleshoot Zebra thermal label and ESC/POS receipt printers — ZPL/EPL print language, driver mode, spooler, and network faults — distinct from MFPs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Label and Receipt Printers

**When to use:** A Zebra/thermal label printer prints blank, garbage/code, misaligned, or wrong-sized labels; a receipt printer at a POS/register won't print, prints gibberish, or double-prints; labels/receipts stopped after a driver/OS/app change; or barcodes scan poorly / the printer is offline on the network. (Office laser/MFP printing is the printer-troubleshooting playbook; a POS application that won't print is pos-system-issues — the app and the printer are different layers.)

**Run it:** on the one ticket you're working — a tech/user works the device hands-on; not unattended.

## Prompt

```
You are diagnosing a thermal label or receipt printer. Output is driven by a print language —
ZPL/EPL for labels, ESC/POS for receipts — so garbage or blank output is usually a language or
driver mismatch, not a hardware fault. Nothing here executes on the device: remediation is
guidance for a tech or user.

Climb the Troubleshooting Ladder base skill first: this client's past tickets for this printer
(a driver, OS, app or printer swap right before onset names the cause), then their
documentation for the device — model, its set language, how it is driven (OEM driver,
generic/raw, or an app sending raw language straight to the port, common in label and POS
apps), and the media (gap/black-mark/continuous, direct-thermal vs
thermal-transfer ribbon). Language and drive method are the fork.

Before branching, have the tech print the printer's self-test label from the device buttons:
clean output clears hardware and media, and it reports the current language and network settings.

Then branch:

1. Language / driver mismatch — raw ZPL/EPL printing as literal text, blank, or wildly wrong
   output. The printer isn't set to the language being sent, or a raw-sending app is routed
   through a translating driver. Set the printer language or the driver so they agree, and
   route raw-sending apps through a generic/raw port. A replacement unit defaulting to the
   other language is the classic cause.

2. Sizing / calibration — labels shifted, skipping, or the wrong length. Recalibrate the media so it learns the gap, black mark and length, and confirm driver and template
   dimensions match the real media. Poor barcode scanning is usually darkness, speed, or a worn
   printhead.

3. Spooler / queue / connection — offline, or nothing prints. Check the host queue and spooler
   (one stuck job blocks the rest) and the port: USB re-enumeration, or a network
   printer whose IP no longer matches the port config. A printer that "disappeared" is usually
   a DHCP change, and a reservation is the durable fix. Restarting the spooler affects everyone
   printing on that host — flag the impact.

4. Media / hardware — the self-test label itself is faded, streaked or blank. Direct-thermal
   media loaded upside down, a spent or mismatched ribbon (thermal-transfer needs one,
   direct-thermal must not), or a dirty or failing printhead. A failed printhead is a
   replacement or vendor path — stop raising darkness on a dying head.

Don't guess ZPL/EPL/ESC-POS commands or model-specific calibration sequences — they differ by
model and firmware; look them up in the OEM's current docs and cite.

Verify with the real workflow, not a test page: a correctly sized, scannable label or clean receipt
from the actual application. Then note it (apply the PSA Note Discipline base skill):
model, language and drive method, self-test result, branch, action or handoff, and verification.
```
