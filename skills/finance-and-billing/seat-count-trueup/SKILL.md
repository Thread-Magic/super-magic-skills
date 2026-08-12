---
name: Seat Count True-Up
description: Monthly true-up for per-seat and per-device agreements — compare actual counts from RMM and onboarding tickets against billing, and produce evidence.
category: Finance & Billing
tools: [search_tickets, search_clients, search_ninjaone_devices]
connectors: [NinjaOne, ConnectWise RMM]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance, Time & Cost Savings (Capacity)]
---

# Seat Count True-Up

**When to use:** the monthly billing run is coming and someone asks to "true up the seat counts" / "are we billing <client> for the right number of users/devices?" / finance found revenue flat while the desk swears clients grew.

**Run it:** across all per-seat/per-device clients, or on a single client you name — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
For each client billed per seat or per device, establish what the count actually is this
month — from RMM device inventory and onboarding/offboarding tickets — and compare it to the
count being billed, producing a true-up evidence pack: who is under-billed, who is
over-billed, and the tickets/devices that prove it. (For per-license SKUs like M365/AV/backup,
use License Billing Reconciliation instead.)

1. Confirm scope — all per-seat/per-device clients or one client — the billing month, and the
   source of the BILLED counts. Billed quantities live in the billing system, not Thread: ask
   the requester to paste or upload the current billed count per agreement. No billed counts =
   no true-up; offer the actual-count half of the pack alone, clearly labeled.

2. Per client, establish the actual count from the strongest available sources: pull the
   device inventory from NinjaOne if connected (otherwise, e.g. a ConnectWise RMM tenant, ask for a device export), filtered to
   billable device classes per the agreement (exclude spares/decommissioned; state the filter
   used).

3. Corroborate with movement tickets: read the onboarding/new-user and offboarding/termination
   tickets for the month. Movement should explain the delta between last month's and this
   month's counts; unexplained deltas get flagged rather than smoothed over.

4. Per agreement, compare actual vs billed: delta, direction (under-billed = revenue leak;
   over-billed = client-trust/credibility risk — flag both with equal seriousness), and the
   monetary impact if the per-unit rate is provided (labeled with the rate used).

5. Build the evidence pack per discrepancy: the device list or count with source and as-of
   date, the onboard/offboard ticket references, and a one-line narrative ("3 users onboarded
   in tickets <refs>, never added to billing"). Evidence must survive the client asking "prove
   it."

6. Output: a true-up table (client / billed / actual / delta / direction / monthly impact),
   the per-discrepancy evidence packs, a recommended adjustments list for the billing admin,
   and a methodology note — sources per client, device filters, as-of dates, searches run,
   caps hit.

Guardrails: this skill produces the evidence pack; it never changes billing, quantities, or
invoices — never convert a recommended adjustment into a completed one. Over-billing is
reported as prominently as under-billing (a true-up that only finds revenue is not credible).
Device counts are as-of-date snapshots with stated filters; a stale RMM agent is not a
billable seat — flag devices unseen for 30+ days separately. Never present capped device or
ticket searches as complete counts; disclose caps and re-split until counts are exact, since
billing math cannot run on floors. If no RMM integration is enabled, say so and fall back to
movement tickets only, labeled a weaker count basis. Monetary impacts use only rates the
requester supplied — never assumed per-seat pricing.
```
