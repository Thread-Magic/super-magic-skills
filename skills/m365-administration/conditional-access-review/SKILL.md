---
name: Conditional Access Review
description: Inventory a tenant's Conditional Access policies to find overlaps, legacy-auth gaps, unprotected apps, with report-only discipline for changes.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Conditional Access Review

**When to use:** A scheduled/periodic CA review for a managed tenant (quarterly is typical), "are <client>'s conditional access policies any good?" / insurance or audit prep, after an identity incident to find why CA didn't stop it, or before consolidating or migrating policies (e.g., off security defaults — see the security-defaults-vs-ca skill). CA policy sets rot in a specific way: exceptions accumulate, new apps arrive unprotected, and two policies quietly fight. This review inventories what the policies actually do today, finds the gaps, and enforces the report-only discipline for anything that changes.

**Run it:** as an on-demand review across every CA policy in the tenant — you compile the inventory, rank findings, and build remediation tickets, a technician exports policies and runs any changes (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
You compile and rank; the tech exports policies and runs every change. Apply the Write
Guardrails base skill — never invent policy contents or sign-in counts; when in doubt about
a policy's effect leave it in report-only and say so.

1. Inventory. Tech exports every CA policy, disabled and report-only included: state, users
   and groups in and out, apps, conditions (locations, platforms, client apps, risk),
   grants, session controls and last-modified date in one dated table — the artefact. Pull the client's documented CA standard from their documentation and the
   knowledge base (Connector Degradation base skill if neither is on).

2. Non-negotiables first:
   - Legacy authentication blocked for all users — the highest-value policy there is. Verify
     against sign-in logs filtered to legacy client apps; real traffic means blocking gets
     its own remediation ticket, not a silent enable.
   - MFA for all users; phishing-resistant MFA — plain MFA at minimum — on every admin role.
   - Break-glass accounts excluded from every policy (cross-check break-glass-account-audit).
     Critical both ways: no exclusion is a lockout risk, an excluded daily-driver account is
     a bypass. Verify these exclusions before ANY enablement from this review.

3. Find the rot:
   - Stale exceptions. Every exclusion needs a written justification and expiry
     (conditional-access-exception); any nobody can explain is a finding.
   - Overlaps. Same users or apps, different grants: work out the effective result (block
     wins, grants combine) and flag pairs nobody intended.
   - Coverage gaps. Apps or populations no policy touches, "All apps" versus named-app
     policies, admin roles missing from the admin policy, guests unhandled.
   - Report-only orphans. Months in report-only is a decision nobody made: graduate, or
     delete.
   Rank worst-first, a remediation each: step 2 failures critical, unjustified exclusions
   and sensitive-app gaps high, overlaps and naming medium. Sign-in-log evidence may be
   capped — apply Sweep Honesty: state the window, label counts observed-in-window, and say
   what you couldn't check.

4. Report-only discipline on every change: create in report-only, collect real sign-in data
   over days not minutes, have the tech review it for legitimate traffic that would have been
   blocked, then enable, with client approval for anything that can block users. What-if spot
   checks supplement report-only data, never replace it. Never enable a blocking policy the
   day it was written.

5. Output a note (PSA Note Discipline base skill: plain text, no markdown or emojis): dated
   table, ranked findings with evidence, remediation list. Raise a ticket per remediation,
   and schedule the next review. Keep tenant identifiers, full policy JSON and user lists
   out of PSA-synced notes; summarize, and store the export in the docs system.
```
