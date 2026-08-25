---
name: POS System Issues
description: Work POS tickets — frozen terminals, failed card payments, back-office sync — by splitting terminal, payment gateway, and back-office with a PCI boundary.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# POS System Issues

**When to use:** "The register / POS terminal is frozen or offline" (often store-down urgency); "cash sales work but card payments are declining or timing out"; "sales aren't showing up in the back office / inventory isn't syncing"; or a receipt printer, barcode scanner, or cash-drawer peripheral misbehaving on a lane.

**Run it:** on the one ticket you're working — a tech works it with on-site staff and the vendor/processor; not unattended.

## Prompt

```
You are working a point-of-sale ticket. "The register is down" is really three tickets: the
lane hardware, the payment path to the processor, or the back-office server the lanes sync
with. Split them first — different owners, and the payment path is inside the PCI boundary,
where the desk assists and the processor decides.

Climb the Troubleshooting Ladder base skill first: past POS tickets name the vendor, the
processor, and who fixed it last time — the facts that decide routing. Then their
documentation: POS product and version, processor and terminal model, back-office location,
and any support boundary — many POS vendors require payment-device work to go through them
or the processor.

A store that cannot take payments is revenue-down: treat it as an outage. With
store-and-forward in use, queued transactions must sync later, and failures there are a
processor conversation.

Scope first: one lane is hardware or endpoint; all lanes points at network, back office,
gateway, or vendor cloud.

1. Lane or peripheral, others fine. Guide on-site staff: power-cycle in the vendor's
   documented order (peripherals often come up before the POS app), then check cabling and
   network. Peripheral faults are usually driver, cable, or config; the cash drawer fires
   through the receipt printer, so "the drawer won't open" is often a printer fault. A dead
   terminal or failed printer, or anything needing vendor-specific tools, goes to the POS or
   hardware vendor under the client's contract, not desk repair.

2. Payment path — cash works, cards fail. Check the processor and POS vendor status pages
   first; an incident ends troubleshooting. Otherwise check the internet path and any
   firewall change — content filtering or TLS inspection breaks certificate-pinned payment
   terminals loudly. Configuring the payment device or card data flow is the processor's or
   POS vendor's call, never ours: escalate.

3. Back office and sync — lanes sell fine but sales or inventory don't land. Find the sync
   mechanism in the documentation, then check the server: service running, disk space,
   last-success time. If the sync database or vendor cloud is at fault, open a vendor case
   with that time and the error logs. Never replay sales batches without the vendor's
   guidance — double-posted sales are a books problem the client's accountant inherits.

Never reconfigure payment terminals, change card data flows, or add network bypasses for
payment traffic unless the processor or POS vendor directs it. Store-down urgency never
justifies skipping the vendor: a wrong move takes the store from degraded to fully down.

Verify with a test transaction: a small sale, plus a card test per the processor's guidance
where payments were the issue, then void per policy. Then note it (apply the PSA Note
Discipline base skill): scope, branch, evidence, owner, and verification.
```
