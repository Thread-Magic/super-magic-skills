---
name: Zapier Webhook Generic
description: The escape hatch — fire a generic webhook (Rewst, custom automation, homegrown endpoint) from a skill when no named Zapier app covers the system.
category: Connectors
tools: [search_tickets, add_ticket_note]
connectors: [Zapier: Webhooks by Zapier]
scope: single
flow: no
role: [Service & Ops Manager, Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Zapier Webhook Generic

**When to use:** "Kick off our Rewst onboarding workflow from this ticket," "POST the alert payload to <internal system>'s endpoint," or bridging to any system where a webhook is the only integration surface.

**Run it:** on one ticket.

## Prompt

```
When the target system has no Zapier app — a Rewst workflow, an internal automation server, a
vendor's inbound hook — a raw webhook is the last-resort transport: powerful and structureless —
no field validation, no find-before-create, no vendor semantics. Impose the structure it lacks.
This is the escape hatch, not the default: where a named Zapier app covers the target, use it —
apps carry validation and lookups raw webhooks lack.

It runs only if the member has connected Zapier with the Webhooks action enabled, and that is
deliberate: it can call any URL, so some tenants exclude it on purpose. If it's absent, apply the
Connector Degradation base skill — output the composed payload and endpoint name for the member
to fire from their own automation platform, and note the pending trigger on the ticket. Each
Zapier call costs 2 Zapier tasks.

1. Verify before promising. Confirm the Webhooks action (POST, PUT, GET) is enabled here, then
   that the endpoint is known and documented: the member or tenant runbook supplies the URL,
   method, content type and payload contract. No documented contract, no fire — guessing a
   payload triggers automations with guessed data. Never fire at a URL improvised from memory or
   scraped from an old ticket.

2. Keep URLs and headers secret-free. Auth material belongs in the tenant's stored config —
   curated-server locked fields, or the receiving system's own validation — never inline in
   output or pasted into a note. If the endpoint's design forces a secret-bearing URL, treat the
   whole URL as a credential: use it, don't quote it.

3. Compose the payload with discipline: exactly the fields the contract specifies, with stable
   names, ISO-8601 timestamps, the Thread ticket reference for traceability, explicit nulls, and
   an idempotency-friendly key (ticket number plus event type) wherever retries are possible. No
   padding — client data takes the same minimum-necessary, no-credentials sanitization as any
   external write.

4. Show the endpoint by name (not the secret-bearing URL), the method and the full payload,
   before firing.

5. Fire it and read the response honestly. A 2xx means the endpoint accepted the request, NOT
   that the automation succeeded — report it that way ("the workflow endpoint accepted the
   trigger", never "the onboarding completed") and capture any returned job or run id. On a
   non-2xx or timeout, report the actual status and body minus secrets, and do NOT retry blindly:
   it may have processed despite the error, and duplicate triggers do real work twice.

6. Leave a note — plain text, no markdown or emojis (PSA Note Discipline base skill): endpoint
   name, a summary of what was sent rather than secret detail, response status, any returned id,
   and honest wording — "accepted", not "done". Name where confirmation will actually appear: a
   Rewst notification, a status page.
```
