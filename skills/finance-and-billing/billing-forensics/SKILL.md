---
name: Billing Forensics
description: When someone asks "why is the client billed X" and the charge needs to be traced to its source across tickets, time entries, agreements, and vendor invoices.
category: Finance & Billing
tools: [search_tickets, search_clients, add_ticket_note]
connectors: [Zapier: QuickBooks, Zapier: Xero]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Billing Forensics

**When to use:** "Why was <client> billed $X in <month>?" / "where did this line item come from? I can't place it" / "the account manager needs the story behind this charge before the renewal call."

**Run it:** on a single charge, or across a client's invoice for a period — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Trace a specific charge back to its origin — the ticket, time entries, agreement line, or
vendor pass-through that produced it — and present the chain of evidence, including any link
that cannot be verified. If the member has QuickBooks or Xero connected, you can look up the
invoice directly there; otherwise work from what the requester pastes.

1. Pin down the charge: client, amount, invoice date/period, and line description as it
   appears. If the requester can paste the invoice line(s), start from that text.

2. If the accounting system is connected, look up the invoice detail in QuickBooks / Xero to
   get exact line items, quantities, and service dates. Otherwise work from the pasted detail.

3. Classify each line and trace it:
   - Labor → find the tickets and time entries behind it by searching the client + service
     dates; reconcile hours × rate to the line amount.
   - Recurring/agreement → match against the agreement quantity basis (seats, endpoints);
     quantities come from the requester's export or the agreement — cite which.
   - Product/pass-through → match to a procurement ticket or vendor invoice reference; if
     neither exists in reach, mark the link unverified.

4. Build the evidence chain per line: invoice line → source record(s) → supporting detail,
   with each hop explicitly cited (ticket number, entry date/tech/hours, export row).
   Reconcile the math: do the sources sum to the billed amount? Report any residual.

5. Deliver the story: a per-line trace table, the reconciliation result (fully explained /
   partially explained with residual / unexplained), and — where a line is unexplained or
   over-supported — what record a human should pull next (PSA agreement, vendor invoice PDF).

6. Offer to save the trace as a plain-text internal note on the related ticket for the
   account team.

Guardrails: never state a contractual or billing conclusion as fact without citing the
evidence for that hop — an unverifiable link is reported as "unverified", not bridged with an
assumption (an honest gap beats a tidy story). Time-entry evidence is the source of truth for
labor charges: if billed hours exceed logged hours, report the excess as unexplained; do not
rationalize it. Read-only forensics: no invoice edits, no credits, no client communication.
Result-cap honesty on ticket searches — a capped search means the labor trace may be
incomplete; say so before calling a charge unsupported. Keep the output internal; it may
expose rates and margins that never belong in a client-facing surface. No accounting connector
→ trace quality depends on what the requester pastes; state which lines couldn't be examined
at source.
```
