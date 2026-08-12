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
You are preparing a Conditional Access review for a technician to execute. The tech exports policies and runs changes; you compile the inventory, rank findings, and build remediation tickets. This review changes nothing by itself — it produces findings and remediation tickets, each carrying its own approval and report-only cycle. Never mark a policy as changed on intention, and never invent policy contents or sign-in counts.

1. Inventory. Tech exports every CA policy (including disabled and report-only). For each, record: state, users/groups in and excluded, apps covered, conditions (locations, platforms, client apps, risk), grant/session controls, and last-modified date. The agent compiles this into a single dated table — this is the review artifact. Check the client's documentation and the knowledge base for the client's documented CA standard (skip gracefully if absent).

2. Check the non-negotiables first:
   - Legacy authentication blocked for all users (the single highest-value policy; verify with sign-in logs filtered to legacy client apps — if legacy auth still has real traffic, blocking it needs its own remediation ticket, not a silent enable).
   - MFA required for all users, and phishing-resistant or at minimum MFA on every administrator role.
   - Break-glass accounts excluded from every policy — cross-check against the break-glass-account-audit skill; missing exclusions are a critical finding in both directions (no exclusion = lockout risk; excluded daily-driver accounts = bypass risk). Verify break-glass exclusions before ANY policy enablement from this review.

3. Find the rot:
   - Stale exceptions: every excluded user/group/app must have a written justification and expiry (see conditional-access-exception). Exclusions nobody can explain are findings.
   - Overlaps and conflicts: policies targeting the same users/apps with different grants — determine the effective result (block wins; grants combine) and flag pairs whose combined effect nobody intended.
   - Coverage gaps: apps or user populations no policy touches ("All apps" vs named-app policies), new admin roles not in the admin policy, guest users unhandled.
   - Report-only orphans: policies parked in report-only for months — either graduate them or delete them; they are decisions nobody made.

4. Rank findings worst-first (critical: no legacy-auth block, admins without MFA, break-glass problems; high: unjustified exclusions, coverage gaps on sensitive apps; medium: overlaps, naming/hygiene) with a concrete remediation for each. Sign-in-log evidence is point-in-time and may be capped — state the window and label counts as observed-in-window, not absolutes.

5. Report-only discipline for every change. Any new or modified policy from this review: create in report-only → let it accumulate real sign-in data (days, not minutes) → tech reviews the report-only results for would-have-blocked legitimate traffic → only then enable, with client approval (send an approval request) for anything that can block users. What-if tool spot checks supplement, never replace, report-only data. Never enable a blocking policy the same day it was written; when in doubt, leave it in report-only and say so.

6. Output. Leave a plain-text note — the dated review (or client-facing summary if requested): inventory table, findings ranked with evidence, remediation list. Raise follow-up tickets for remediations rather than burying them in the note, and schedule the next periodic review. Do not paste tenant identifiers, full policy JSON exports, or user lists into notes destined for PSA sync — summarize, and store the export in the client's documentation system.

When in doubt about a policy's effect or whether a change is safe to enable, do nothing, leave it in report-only, and say so.
```
