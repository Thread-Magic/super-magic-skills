---
name: Contract Renewal Routing
description: Catch contract renewal and expiry notices landing in the service queue and route them to the right owner — retitled to a standard, moved to the sales/AM board, with context attached.
category: Client Lifecycle
tools: [search_tickets, update_ticket, add_ticket_note, list_boards, search_clients, search_members]
connectors: []
scope: single
flow: yes
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Contract Renewal Routing

**When to use:** "Route this renewal notice to the right place"; a sweep ("find any contract/renewal notices sitting in the support queues"); or automatically catching renewal notices as they arrive.

**Run it:** on one ticket · sweep the support queues · or as a Flow that catches renewal notices on ingestion.

## Prompt

```
Renewal notices, expiry warnings, and vendor agreement emails don't belong in the tech
queue — but losing one costs real money. Recognize them, retitle to a standard, and hand
them to the owner who acts on them, with enough context to act.

1. Identify the candidate ticket(s): the ticket in context, or sweep the recent open
   tickets on support boards for renewal/expiry language (renewal, expires, expiration,
   auto-renew, agreement term, license expiry).

2. Qualify each candidate — it must genuinely be an agreement/renewal notice (vendor
   contract, license subscription, domain/certificate expiry, client MSA anniversary), not
   a support issue that mentions "renewal". If uncertain, leave it where it is and flag it
   instead of moving it.

3. Extract the facts the owner needs: which client or vendor, what agreement, the
   renewal/expiry date, auto-renew or action-required, and any stated deadline or price
   change.

4. Determine the destination (look up the boards): agreement and renewal work goes to the
   sales/AM board (or the board the desk designates); domain/certificate expiries may go to
   the appropriate technical board — follow the desk's convention, and ask once if none is
   known.

5. Route the ticket: retitle to the standard "Renewal — <client/vendor>: <agreement> —
   <date>"; move it to the destination board and set the owning role (AM/sales owner) if the
   desk's convention names one.

6. Attach context in a plain-text note: the extracted facts and where the notice came from,
   so the owner never has to re-read the original email chain.

7. Report what was routed, where, and anything left unrouted with the reason.

Running unattended in a Flow (per-ticket on ingestion): qualify silently; if the ticket is
not confidently a renewal notice, do nothing and produce no output. On a confident match,
retitle, move, and note exactly as in steps 5–6 — the note is plain text and your entire
reply is the note content, no narration. Never assign to a person unless the flow
configuration names the owner. Deterministic stop: one ticket, one decision, at most one
move + one note.

Guardrails: low confidence → no move; a wrongly routed support ticket is worse than an
unrouted notice. Never alter the renewal facts — dates and terms are quoted from the notice,
not inferred; if the date is ambiguous, say so in the note. Do not respond to the vendor or
client, and never accept/decline a renewal — this routes; humans decide. Confirm before bulk
moves when sweeping (more than a couple). Notes are plain text. Do not invent owners — if no
routing convention or owner is known, park the ticket with a flag note and report it.
```
