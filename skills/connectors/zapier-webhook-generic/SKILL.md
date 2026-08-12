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
vendor's inbound hook — a raw webhook is the last-resort transport. Powerful and structureless: no
field validation, no find-before-create, no vendor semantics. Impose the structure the transport
lacks: a documented endpoint, a disciplined payload, secret-free handling, and honesty about what a
200 does and does not prove. This is the escape hatch, not the default — when a named Zapier app
covers the target, use it (apps carry validation and lookups raw webhooks lack).

This runs only if the member has connected Zapier with the Webhooks action enabled — treat its
availability as deliberate: it can call any URL, so curated-server tenants may have excluded it on
purpose. If it's absent, degrade by outputting the composed payload and endpoint name for the member
to fire from their automation platform, and note the pending trigger on the ticket — do not stop.
Each Zapier call = 2 Zapier tasks.

1. Verify before promising: confirm the Webhooks action (POST/PUT/GET) is enabled for this tenant,
   then verify the endpoint is a known, documented one — the member or tenant runbook supplies the
   URL, method, content type, and payload contract. No documented contract → stop; guessing a payload
   triggers automations with guessed data. Documented endpoints only — never fire at URLs improvised
   from memory or scraped from old tickets.
2. Secret-free URLs and headers: auth material belongs in the tenant's stored config (curated-server
   locked fields, or the receiving system's own validation) — never inline in output, never pasted
   into a ticket note. If the endpoint's design forces a secret-bearing URL, treat the whole URL as a
   credential: use it, don't quote it.
3. Compose the payload with discipline: exactly the fields the contract specifies — stable names,
   ISO-8601 timestamps, the Thread ticket reference for traceability, explicit nulls, and an
   idempotency-friendly key (ticket number + event type) where retries are possible. No padding; client
   data is bound by the same minimum-necessary, no-credentials sanitization as any external write.
4. Show me the endpoint (by name, not secret-bearing URL), method, and full payload before firing.
5. Fire the webhook and read the response honestly. A 2xx means the endpoint accepted the request, NOT
   that the downstream automation succeeded — report it exactly that way ("the workflow endpoint
   accepted the trigger", never "the onboarding completed"). Capture any returned job/run ID. Non-2xx
   or timeout → report the actual status and body (minus secrets); do NOT retry blindly (it may have
   processed despite the error) — duplicate triggers do real work twice.
6. Leave a note (plain text): endpoint name, what was sent (summary, not secret detail), response
   status, any returned ID, and honest status wording ("accepted", not "done"). Name where confirmation
   will actually appear (a Rewst notification, a status page).
```
