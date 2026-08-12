---
name: Circuit Inventory
description: Refresh a client circuit inventory — internet, WAN/MPLS/SD-WAN, POTS-replacement — with carrier, circuit ID, site, bandwidth, and renewal dates.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, search_tickets, add_ticket_note, create_ticket, schedule_ticket]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Circuit Inventory

**When to use:** "What circuits does <client> have and who are the carriers?" — or an outage stalls because nobody can find the circuit ID or carrier account reference.

**Run it:** across a client's sites, on demand for renewal planning or an inventory refresh (not a Flow — it's a planning sweep, not a per-ticket event).

## Prompt

```
Assemble the living register of every line a client leases — carrier, circuit ID, site, bandwidth, contract/renewal — from documentation and ticket history, with the gaps named.

1. Pull documented circuits: search the documentation (IT Glue / Hudu) for circuit, ISP, WAN, and telecom docs per site. Per circuit capture: site, carrier, service type (DIA/broadband/MPLS/SD-WAN underlay/POTS-replacement), circuit ID, carrier account number BY REFERENCE (which doc holds it — never copy account passwords or PINs into output), bandwidth, static IPs by reference, contract term and renewal/expiry date, and the outage support phone number.
2. Mine ticket history for undocumented circuits: check for carrier names and outage tickets per site — a carrier in outage history but not documentation is a gap. Report capped searches as "at least N".
3. Special sweep for POTS/analog survivors: alarm lines, fax, elevator phones, fire-panel dialers. These hide outside IT docs; flag any site where docs are silent on analog lines as "unverified — confirm on site" (life-safety implications during carrier migrations).
4. Build the per-site table: carrier, type, circuit ID, bandwidth, renewal date, doc reference, last-outage date. Mark every cell you could not source; empty beats invented.
5. Renewal calendar: list by renewal date. For any renewal inside the client's typical renegotiation window (commonly 90-180 days out), schedule a dated follow-up ticket so renewals surface as work, not surprises.
6. Output the inventory plus a gap list (undocumented circuits, missing IDs, unknown renewal dates, unverified analog lines) with a recommended documentation task per gap. Offer to leave the summary as a plain-text note (no markdown/emojis) and open the doc/renewal tickets. Updating the documentation platform itself is a handoff.

Guardrails: account numbers, PINs, and portal credentials are referenced by document location only — never reproduced. Never invent a circuit ID, renewal date, or bandwidth to complete the table — unknowns stay unknown. Renewal dates of unknown age get a "verify with carrier" caveat (auto-renew clauses make stale dates costly). Contract/pricing decisions are account management's call; this surfaces dates and facts, it does not recommend switching carriers. If no documentation platform is connected, build from ticket history, label it "reconstructed, unverified", and lead with the recommendation to document properly.
```
