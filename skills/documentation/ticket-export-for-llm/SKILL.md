---
name: Ticket Export for LLM
description: Produce a clean, sanitized, self-contained export of a ticket for pasting into another AI tool — credentials and PII stripped, context preserved.
category: Documentation
tools: [search_tickets]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Ticket Export for LLM

**When to use:** "Export this ticket so I can paste it into another AI tool," handing an incident to a vendor's support chatbot or a specialized model, or any external analysis tool that only accepts pasted text.

**Run it:** on one ticket.

## Prompt

```
Package a ticket's full story into one clean text block another AI tool can work from,
with everything sensitive removed and everything technically relevant kept. Read-only:
never modify the ticket, and never send the export anywhere — the tech pastes it.

1. Read the complete ticket: description, all replies and internal notes in order,
   time entries, status/priority history.

2. Build the export in this structure:
   - Context header — anonymized one-liner: environment type, product/system involved,
     priority, current status, ticket age.
   - Problem statement — the reported issue with exact error text preserved.
   - Chronological thread — each entry as "[T+<offset>] <role: user | technician |
     system>: <content>", using relative times and roles instead of names.
   - Technical facts — versions, OS, configurations, diagnostics mentioned.
   - Current question — what the tech wants the other tool to figure out (ask if not
     stated).

3. Sanitize aggressively before output — sanitization is the product:
   - DELETE ENTIRELY: passwords, API keys, MFA codes, license keys, session tokens,
     the contents of any credential-store reference. Nothing credential-shaped ever
     survives, even partially masked.
   - REPLACE WITH PLACEHOLDERS: person names -> <user>/<technician>, client/company
     -> <client>, emails -> <user>@<client-domain>, hostnames -> <server-1>, public
     IPs -> <public-ip-1>, internal IPs kept only as subnet shape (10.x.x.x) when
     diagnostically relevant, phone numbers -> <phone>, ticket/invoice numbers ->
     <ticket-ref>. Keep placeholders CONSISTENT (<server-1> is the same machine every
     time) so the receiving model can reason across the thread.
   When unsure whether something identifies a person or client, redact it.

4. Do a second pass specifically for sensitive data quoted inside pasted logs,
   signatures, and email footers — the usual leak paths.

5. Preserve technical meaning — error messages, versions, and sequence of events stay
   verbatim; sanitize identity, not evidence. Do not invent context to fill gaps; mark
   unknowns as <not in ticket>.

6. Output the export as one plain-text block, prefixed with a one-line note of what
   was redacted (categories only). Remind the tech once that the export leaves Thread's
   environment, so it must comply with the client's data-handling agreement — flag
   regulated-industry clients (medical, legal, financial content) explicitly.
```
