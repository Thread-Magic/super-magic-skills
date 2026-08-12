---
name: Invoice Dispute Investigation
description: When a client disputes a charge or questions an invoice line and you need to reconstruct the work evidence from tickets and time entries, then draft a factual response.
category: Finance & Billing
tools: [search_tickets, search_clients, search_contacts, add_ticket_note]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion), Fewer Escalations & Less Noise]
---

# Invoice Dispute Investigation

**When to use:** "<client> is disputing the 4.5 hours on their invoice — what actually happened?" / "client says they never asked for this work — pull the evidence" / "prep a response to this billing complaint."

**Run it:** on a single disputed charge, or across the disputed lines of an invoice you point me at — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Reconstruct exactly what work was done behind a disputed charge — tickets, time entries, who
asked for the work, and when — and produce an evidence summary plus a draft factual reply for
a human to review.

1. Identify the disputed item: client, invoice period, amount or hours, and any ticket
   numbers mentioned. If the dispute references an invoice line you cannot map to a ticket,
   say so — do not guess a mapping.

2. Look up the client and, if a person disputed it, the contact.

3. Read the relevant tickets and their full threads and time entries for the disputed period.
   Search per ticket reference first; broaden to the client + period only if references are
   missing.

4. Build an evidence timeline: who requested the work (quote the actual request message),
   what was done, each time entry (tech, date, duration, billable flag, note), and the
   resolution. Every claim in the timeline must point to a specific message or time entry.

5. Assess the dispute honestly: if the evidence supports the charge, say why; if entries are
   vague, duplicated, or unsupported by ticket activity, flag that too — the desk needs the
   truth before it responds.

6. Draft a client-facing reply that states facts only: what was requested, what was done,
   time recorded. No apology-implying-fault, no promise of credit, no restatement of contract
   terms as fact. Plain text, no markdown.

7. Offer to attach the evidence summary as a plain-text internal note. Do not send anything
   to the client.

Guardrails: never state a contractual or billing conclusion ("this is covered", "this is
billable per your agreement") as fact without citing the agreement evidence — if the agreement
text isn't available to you, present the time-entry evidence and leave the contractual call to
a human. Time entries are the source of truth for what was worked; ticket descriptions alone
are not proof of effort. The reply is a draft — never send it; a human owns the client
conversation and any credit decision. Do not invent ticket numbers, dates, or durations; if
evidence is thin, say the charge is weakly supported rather than papering over it. If the
disputing contact appears hostile or this is a repeat dispute, note that for the account owner
instead of escalating tone in the draft.
```
