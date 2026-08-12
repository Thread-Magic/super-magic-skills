---
name: Liongard QBR Evidence Pack
description: Assemble QBR-grade posture evidence for one client from multiple Liongard inspectors — identity risks, EOL exposure, cert and domain hygiene, and config drift — as a dated, sourced evidence pack the QBR deck can stand on.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_identity, liongard_domain, liongard_metric, liongard_detection, liongard_timeline, liongard_cyber_risk_dashboard, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion), Risk & Compliance]
---

# Liongard QBR Evidence Pack

**When to use:** "Pull the Liongard evidence for <client>'s QBR" / prep for a quarterly or strategic business review, or a vCIO wants defensible numbers behind a recommendation ("show me the EOL machines, not the claim").

**Run it:** on one client — name the client whose QBR you're prepping.

## Prompt

```
Build a QBR evidence pack for CLIENT_NAME from every Liongard inspector the client has. Evidence, not conclusions — read-only.

1. Inventory what evidence is possible: enumerate ALL of the client's inspectors and confirm each ran recently; anything older than the quarter is marked stale. The inventory itself is slide one — what's instrumented, what last ran when, and what isn't watched at all (monitoring gaps are roadmap items). Every downstream number carries its data date.
2. Assemble four evidence sections, headline findings only, verifying every field angle against the live dataprint:
   - Identity risk → the reconciled identity view plus M365/AD/Google/Okta/Duo reads as applicable: admin counts vs. benchmark, MFA/2SV coverage with stated denominators, stale enabled accounts, bypass users.
   - EOL exposure → OS fleet reads: OS build spread and machines past end-of-support (lifecycle dates verified against vendor lifecycle, not remembered), with coverage statements.
   - Domain & cert hygiene → the domain inventory: domain expiry and lock status, DMARC/SPF/DKIM presence, certs expiring next quarter.
   - Config drift → check what changed across the quarter (admin grants, policy loosenings, GPO/NSG/gateway changes), reconciled against ticket history so the pack distinguishes "changes we made on tickets" (service narrative) from "changes with no ticket" (findings). The cyber-risk summary scoring supplies summary numbers where the partner licenses it.
3. Trend against the previous pack: search prior QBR notes/tickets for last quarter's numbers and state per-metric movement — improved / unchanged / degraded. No fabricated trends — if no baseline exists, the column says "first measurement" and this pack becomes the baseline.
4. Rank findings across sections by client impact (exploitability x business consequence), identity usually leading; select the top 3–5 as the headline, everything else appendix.
5. Guardrails: every number carries a date and a source inspector — an undated number does not enter the pack. Fleet and identity percentages name their denominators or they don't ship. Stale/failed inspectors are reported as gaps, not silently skipped. Never inflate findings to justify a deal.
6. Output: instrumentation inventory (with gaps), the four sections (each finding = claim + evidence rows + data date + trend), the headline top-5, and a "recommended roadmap inputs" list. Leave it as a plain-text note on the QBR-prep ticket on request. If Liongard coverage is thin, produce the instrumentation-gap report alone — do not pad from memory or generic benchmarks.
```
