---
name: Zapier DocuSign Authorization
description: Send change-authorization or offboarding-acknowledgment for signature from a ticket via DocuSign, track completion, and file the signed document.
category: Connectors
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: [Zapier: DocuSign]
scope: single
flow: no
role: [Service & Ops Manager, Security & Compliance Owner]
outcome: [Risk & Compliance, Time & Cost Savings (Capacity)]
---

# Zapier DocuSign Authorization

**When to use:** A change (firewall rules, domain transfer, data deletion) that needs the client's signed authorization, or an offboarding acknowledgment the client sponsor must sign.

**Run it:** on one ticket.

## Prompt

```
Signature-grade approval for signature-grade actions: send the tenant's authorization template for
signature via DocuSign (an envelope from a template), hold the gated work until the envelope
completes, and file the signed document where audits can find it.

This runs only if the member has connected Zapier with the tenant's DocuSign account. If it's
absent, degrade by preparing the field values and signer details for the member to send from
DocuSign directly — and still enforce the gate: no signature, no action. Each Zapier call = 2 Zapier
tasks; check envelope status at sensible checkpoints, not on a polling loop.

1. Identify the correct template: an envelope built from the tenant's existing change-authorization
   / offboarding-acknowledgment templates. No template for the case → stop and tell the member; do
   not compose ad-hoc legal-ish documents. Fill fields; don't edit template language — wording
   changes are a human/legal decision.
2. Resolve the signer from the ticket/contact record: the client's authorized signer per policy, not
   merely the requester — for offboarding, the requester is sometimes the person losing access; the
   signer never is. When the authorized signer is unclear, ask me — never guess a signer for a legal
   document.
3. Fill template fields from ticket facts only: what's authorized, systems affected, effective date,
   ticket reference. Show me signer + filled fields and wait for confirmation.
4. Send the envelope through DocuSign. Leave a note (plain text): envelope sent, template, signer,
   date. Set the ticket to the desk's waiting-on-signature status if one exists.
5. The gate: the authorized work does not start until the envelope status is completed — never on a
   promise, a verbal, or a sent-but-not-completed envelope. Check status on follow-up in DocuSign;
   declined/voided → route back to me with the reason; expired/silent past the tenant's window →
   one reminder, then human follow-up.
6. On completion: download the signed document, file it per tenant convention (client's SharePoint
   library — see Zapier SharePoint Ticket Filing — or attach to the ticket), and note completion
   with the storage location. An unfiled signature protects no one.
```
