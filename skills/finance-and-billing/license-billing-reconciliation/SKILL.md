---
name: License Billing Reconciliation
description: Reconcile a client's billing against reality — RMM devices, license export, onboarding tickets — to find missed adds, missed removals, and discrepancies.
category: Finance & Billing
tools: [search_tickets, search_clients, add_ticket_note, search_ninjaone_devices]
connectors: [NinjaOne, ConnectWise RMM]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance, Time & Cost Savings (Capacity)]
---

# License Billing Reconciliation

**When to use:** "Reconcile <client>'s M365 licenses against what we're billing them" / "did we ever remove billing for the people offboarded last quarter?" / "audit device count vs the per-endpoint line on <client>'s agreement."

**Run it:** across all per-license clients, or on a single client you name — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Cross-reference three sources — managed devices (RMM), licenses (e.g. an M365 license export),
and on/offboarding tickets — to find users and devices being billed that shouldn't be, and
ones that should be billed but aren't.

1. Gather the inputs. Billing quantities (what the client is currently invoiced for, per line
   item) and the license export come from the requester — paste or upload. Device inventory:
   pull the client's device list from NinjaOne if it is
   connected; otherwise (e.g. a ConnectWise RMM tenant) ask for a device export. If any of the three sources is missing, run a
   two-source reconciliation and state the blind spot.

2. Look up the client, then read the onboarding and offboarding tickets for the review period
   (search per signal: "onboarding", "new user", "offboarding", "termination" — separate
   searches, note any result caps).

3. Build the reconciliation:
   - Offboarded per tickets but still holding a license or a billed seat → missed removal
     (client overbilled, or MSP eating the vendor cost).
   - Onboarded per tickets but absent from the billing quantities → missed add (revenue
     leakage).
   - Licensed users with no matching device/ticket presence → possible stale account
     (security flag too).
   - Device count vs billed endpoint count → per-endpoint discrepancy.

4. Match on exact identifiers (email/UPN, device serial/hostname) — never on name similarity.
   Anything that only fuzzy-matches goes in an "unmatched, needs human review" bucket.

5. Output: per-line-item table of billed qty vs actual qty vs delta, then the named exceptions
   with the evidence for each (ticket reference, export row, device record). Estimate the
   monthly billing impact only from unit prices the requester supplied.

6. Offer to post the exception list as a plain-text internal note on a reconciliation ticket.
   Do not change any billing anywhere.

Guardrails: never state a billing discrepancy as fact without citing the evidence pair behind
it (the ticket + the export row, or the export row + the device record) — unverifiable deltas
are "needs review", not findings. Never match people or devices on name similarity; exact
identifier match or it goes to the review bucket. This skill finds discrepancies; it never
corrects them — billing changes happen in the PSA/accounting system by a human. Result-cap
honesty on ticket searches: a capped offboarding search means "at least N" — say the
reconciliation may be incomplete. If no RMM integration is enabled, say so and work from
provided exports only. Exports may contain personal data — keep the output internal, and don't
reproduce more identifier columns than the reconciliation needs.
```
