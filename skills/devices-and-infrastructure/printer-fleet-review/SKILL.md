---
name: Printer Fleet Review
description: Cluster a client printer-related tickets to find chronic devices, quantify the time they burn, and recommend replace-vs-repair per problem printer.
category: Devices & Infrastructure
tools: [search_tickets, search_itglue, search_ninjaone_devices, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Printer Fleet Review

**When to use:** "<client> complains about printers constantly — what's actually going on?", QBR prep wanting the printer story with numbers, or deciding whether a troublesome printer is worth another repair.

**Run it:** across a client's printer-related ticket history, on demand (not a Flow — it's a trend/analysis pass, not a per-ticket event).

## Prompt

```
Mine the client's ticket history for printer pain, attribute it to specific devices, and turn "printers are always broken" into a per-device verdict: fix the spooler pattern, replace the chronic unit, or leave it alone. This output is internal.

1. Pull the client's printer-related tickets from ticket history — search per signal rather than one broad query: printing/printer terms, spooler, common vendor names in the client's environment, known printer hostnames. Window: 90-180 days. Flag result caps and report "at least N" where a search may be truncated.
2. Attribute each ticket to a device where possible: printer names/IPs in ticket text, cross-referenced against documentation (IT Glue printer/asset records) and any print servers or networked printers visible in the RMM. Tickets naming no device go into an "unattributed" bucket — report its size honestly rather than distributing it by guesswork.
3. Cluster and count: tickets per device, per failure type (driver/spooler, connectivity, hardware jams/quality, supplies, user-how-to), and per user/location. Separate infrastructure patterns (one print server's spooler dying weekly — a server problem) from device patterns (one unit jamming monthly).
4. Compute the cost signal: ticket count x rough handling time per ticket (from time entries where present; otherwise say estimates are used). A device generating hours of tech time per quarter has a comparable monthly cost to a lease on its replacement — make the comparison explicit but label the numbers as estimates.
5. Verdict per chronic device (3+ tickets in the window): repair/adjust when failures share one fixable cause (driver standardization, firmware, network drop); replace when failures are hardware-diverse on an aging unit, repair costs approach replacement, or supplies/parts are discontinued; investigate when the pattern points at environment (network segment, print server) rather than the unit.
6. Output: summary (printer tickets as share of the client's volume, trend vs prior period), chronic-device table (device, tickets, failure types, hours, verdict), infrastructure findings, and the unattributed count. Recommend next actions per verdict. Offer a plain-text note (no markdown/emojis).

Guardrails: replace-vs-repair is a recommendation with the evidence shown — never a purchase commitment, and never with invented pricing (hardware costs are the requester's to fill in). Attribution honesty — do not smear unattributed tickets across devices to make clusters look stronger. Time-cost figures built on estimates are labeled as estimates. Result-cap honesty across every ticket search; split searches per signal. Client-facing versions go through the Client-Facing Device Report skill's sanitization rules.
```
