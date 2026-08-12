---
name: Security Advisory Broadcast
description: Draft a security advisory going to many clients — new threat, vendor breach, or vulnerability — from verified facts with per-client relevance check.
category: Communication
tools: [search_clients, search_tickets, search_itglue, search_hudu, web_search, view_openDraft]
connectors: [IT Glue, Hudu]
scope: both
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Security Advisory Broadcast

**When to use:** "Vendor <X> disclosed a breach — draft the advisory for our affected clients" / "there's a critical vulnerability in <product> being exploited — notify clients who run it."

**Run it:** on one client's advisory · or across all clients who run the affected product.

## Prompt

```
Draft the one-to-many security notice that has to be right the first time: verified facts,
defensive wording, a clear "what we're doing / what you should do" split — and a relevance pass
so the list contains only clients the advisory actually applies to.

1. Verify before writing. Establish the facts online from PRIMARY sources — the vendor's own
   advisory/disclosure, or an official body (CERT/CISA-equivalent). Capture: what is affected
   (product, versions), what is confirmed vs under investigation, and the vendor's recommended
   action. Media coverage points to primary sources, it is never the source itself.

2. Per-client relevance check — mandatory before any send list exists. For each candidate
   client, verify they actually use the affected product/vendor: documentation (check IT Glue /
   Hudu where connected), ticket history, or my knowledge. Output two lists: confirmed relevant
   (evidence found — cite it) and unverified (no evidence either way — human decides). Never
   default the unverified list into the broadcast.

3. Draft, in this order:
   - What happened, in one or two verified sentences, naming the vendor/product and citing the
     vendor's own disclosure.
   - Whether this client is affected and how — written so each recipient reads "this concerns
     the <product> you use."
   - What we are doing: the desk's active response (assessing exposure, applying vendor patches
     as released, monitoring). Only actions actually underway.
   - What you should do: concrete client-side actions if any (reset passwords, expect a
     maintenance window, report suspicious emails) — or explicitly "no action needed right now."
   - What we don't know yet and when the next update comes, if evolving.

4. Keep it to one screen. Show me the draft plus BOTH recipient lists for review, labeled
   "SECURITY ADVISORY DRAFT." The human approves the confirmed list, decides the unverified
   list, and owns the send — a mass security broadcast is never sent autonomously.

Only verified facts — every claim traces to the vendor's advisory or an official source at
draft time. No speculation about attacker identity, scope, or motive; no repeating unconfirmed
media numbers. Defensive-writing governs vocabulary: no "breach"/"hacked"/"compromised" beyond
what the primary source states, no "your data is safe" without evidence. No advisory to a client
who doesn't run the product — irrelevant security mail trains clients to ignore relevant
security mail. Never reveal which other clients are affected or the count. If the desk itself
may be inside the blast radius (an MSP-tooling supply-chain event), STOP — that is a
declared-incident scenario where management and the incident policy govern. Without IT
Glue/Hudu, the relevance check runs on tickets + my knowledge only — say so, and expect a larger
unverified list.
```
