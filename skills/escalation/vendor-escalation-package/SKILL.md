---
name: Vendor Escalation Package
description: Assemble a third-party vendor support package — environment, repro steps, timeline, diagnostics, contract or entitlement reference — credentials stripped.
category: Escalation
tools: [search_tickets, add_ticket_note, search_knowledge_base, search_itglue, search_hudu, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Vendor Escalation Package

**When to use:** "Open a case with the vendor for this" / "prep this ticket for <vendor> support"; the desk has hit the limit of what it can do and vendor support is next; or the vendor bounced a case for missing info and it needs resubmitting properly.

**Run it:** on one ticket.

## Prompt

```
You are building the case package that gets a ticket past a vendor's L1 in one pass —
their intake questions answered before they're asked, in a copy-paste-ready block.

1. Read the full ticket thread and pull environment context: affected product, exact
   version/build, OS and platform, deployment shape (cloud/on-prem, single/multi-site),
   and affected scope at <client>. Use IT Glue / Hudu documentation for documented
   environment details where those connectors are enabled; otherwise ask the technician.

2. Build reproduction: numbered steps to reproduce (or "intermittent — occurs roughly
   X times per day since <date>"), expected vs actual behavior, and exact error text
   verbatim.

3. Collect diagnostics referenced in the ticket — log excerpts, screenshots, outputs.
   List each item and where it lives; flag anything the vendor will predictably ask for
   that is missing (e.g. a support bundle) so the tech gathers it before submitting.

4. Find the support entitlement: contract number, support agreement level, customer/site
   ID with the vendor, licensed-under name — from documentation (IT Glue / Hudu / the
   knowledge base). If not documented, leave the field blank and flag it; do not guess.
   Look up only the vendor's public case-submission process on the web, never entitlement
   data.

5. Scrub the package: remove passwords, API keys, tokens, and internal-only remarks from
   everything outgoing — including inside pasted log excerpts (mask as <redacted>).
   Replace internal jargon with plain language a vendor can follow.

6. Assemble in vendor-friendly order: Contact & entitlement / Environment / Problem
   summary / Repro steps / Timeline / Diagnostics attached / What we've ruled out /
   Impact & requested priority.

7. Output the package as a copy-paste block for the vendor portal or email. Offer to
   also post it as a plain-text internal note (with a placeholder for the vendor case
   number) — post only on confirmation. Do not submit to the vendor yourself.

Guardrails: credentials never leave — no passwords, keys, tokens, or internal admin
URLs in the outgoing package, even embedded in logs. Entitlement and contract refs come
from documentation only; a blank field beats a wrong contract number. Error text is
quoted verbatim, never paraphrased — vendors match on exact strings. "What we've ruled
out" lists only steps actually documented in the ticket. If IT Glue / Hudu are not
enabled, gather details from the technician and say which fields are unverified.
```
