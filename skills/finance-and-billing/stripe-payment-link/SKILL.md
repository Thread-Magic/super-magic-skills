---
name: Stripe Payment Link
description: When approved out-of-contract work needs to be paid and you want a Stripe payment link generated and placed in the ticket reply draft.
category: Finance & Billing
tools: [search_tickets, search_clients, send_approval, add_ticket_note]
connectors: [Zapier: Stripe]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Stripe Payment Link

**When to use:** "Client approved the $450 out-of-scope fix — get them a payment link" / "add a Stripe link to my reply for the one-off project charge" / "collect payment for this T&M ticket via Stripe."

**Run it:** on one ticket with an approved charge — run it manually. Never a Flow: creating a payment link is a deliberate, approval-gated human act.

## Prompt

```
Generate a Stripe payment link for out-of-contract work the client has ALREADY approved, and
embed it in a drafted ticket reply — so payment collection rides inside the existing ticket
conversation.

1. Verify the approval first. Read the ticket and locate the client's explicit approval of the
   work AND the amount (an approval response via Thread's approval flow, or an unambiguous
   written yes to a stated price). No recorded approval → stop; offer to send an approval
   request and resume after the client approves. Never create a payment link for an amount the
   client hasn't agreed to.

2. Confirm the charge composition with me: amount, what it covers (tie it to the ticket's time
   entries or the quoted fixed price), tax handling per the desk's practice, currency.

3. Show the summary in chat — client, amount, description, the approval evidence you're relying
   on (quoted) — and get my explicit go-ahead.

4. Create the link in Stripe: description referencing the ticket number and work performed,
   exact approved amount, single-use where supported.

5. Draft the ticket reply containing the link: one short plain paragraph — work completed as
   approved on <date>, amount as agreed, link to pay, who to contact with questions. No
   urgency-pressure language. Leave the reply as a DRAFT for me to review and send.

6. Leave a plain-text internal note: payment link created, amount, approval reference, link
   destination — so the audit trail lives on the ticket.

Guardrails: money-moving actions are draft + approval-gated twice here — the client must have
approved the work and amount (evidence cited in your output), and I must approve link creation
and send the reply myself; this skill never sends the client-facing message. Never state the
charge is contractually owed without citing the agreement or approval evidence — the approval
message is your evidence; quote it. Amount discipline: the link amount must exactly match the
approved amount; any change (tax, adjustment) goes back to the client for re-approval before a
link exists. Time-entry evidence backs T&M amounts: if the approved sum doesn't reconcile with
logged time at the stated rate, flag the mismatch before creating the link. Requires the
member's Zapier connector with Stripe connected; if unavailable, say so — do not substitute an
unverified payment mechanism. Never create links for retainer/recurring agreement billing —
that belongs to the accounting system's invoicing flow, not ad-hoc links.
```
