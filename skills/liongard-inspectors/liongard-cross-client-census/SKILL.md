---
name: Liongard Cross-Client Census
description: Answer "which clients run <system>?" across the book via Liongard launchpoint inventory: install-base census for zero-days, EOL waves, vendor risk.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query]
connectors: [Liongard]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# Liongard Cross-Client Census

**When to use:** A zero-day or critical CVE lands and you need "which clients run <vendor product>?"; a vendor breach or supply-chain event needs an exposure list across the book in minutes; an EOL wave needs "who still runs <product/version>?"; or standardization/stack questions ("how many clients are on <firewall brand>?").

**Run it:** across the whole book of business — name the system, and the affected versions if you're scoping a CVE.

## Prompt

```
Produce a cross-client install-base census for TARGET_SYSTEM (optionally version-scoped to AFFECTED_VERSIONS) across the whole book of business, from Liongard's inspector inventory. Read-only.

1. Enumerate all client environments, then find every inspector for TARGET_SYSTEM across them. Match generously — inspector naming varies (brand vs. product line), so check plausible aliases among the ~300 inspector types before declaring absence; a miss understates exposure.
2. State the census's honest shape up front: Liongard shows where an INSPECTOR exists, not where the product exists — the result is the *instrumented* install base. Clients running the product without an inspector are invisible. For high-stakes events, pair the inspector census with a ticket-history search across boards for the product name (per-signal result-cap honesty: "at least N") and documentation where available. Separate the output into "confirmed via inspector," "suggested by tickets/docs," and "unknown."
3. For each hit capture the triage columns: client, inspector last-run status and data age, and — where the question is version-scoped — read the version/build value from each hit's latest dataprint (verify field angles against the live dataprint; version fields differ per inspector). A CVE affecting 9.x-before-9.2 turns the census into a ranked patch list.
4. Rank by exposure: affected-version confirmed → version unknown but product confirmed → suggested-only. Failed/stale inspectors rank UP, not down — unknown version on an internet-facing product is exposure, not comfort.
5. Speed beats polish but never honesty: ship the confirmed tier immediately, keep widening the suggested tier — don't hold the list to perfect it. Version claims come from dataprints, dated; "version unknown" is written, not guessed.
6. Offer to open a ticket per affected client only on confirmation — deduplicate against open tickets first, one plain-text ticket per client with its specific evidence. Never blast the book on an unranked census.
7. Output: the census table (client, evidence tier, version where known, data age), the honest-scope statement, and the count summary "N confirmed, M suggested, coverage unknown for the rest." If the partner doesn't run Liongard, the census is tickets + documentation only and materially incomplete — say so.
```
