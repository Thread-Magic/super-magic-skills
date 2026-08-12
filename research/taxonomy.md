# Role & outcome taxonomy (verified July 2026)

Two tagging axes on top of `category`, added to power role- and outcome-based browsing on
the docs site (category stays the primary navigation; these are filters). Every skill's
`role:` and `outcome:` frontmatter must draw only from these fixed enums — don't invent new
values. Both fields are multi-value; most skills carry 1-2 roles and 1-2 outcomes.

## `role:` — who reaches for this skill

Matches Thread's actual MSP personas, not SaaS-style titles (no "AE" — MSPs don't use it).

| Value | Who this is | Signal words in the skill |
|---|---|---|
| `Technician` | L1/L2/L3 service desk tech working tickets | "read the ticket", "reply", "troubleshoot", per-ticket work |
| `Dispatcher` | Triage lead / whoever assigns and routes | "route", "assign", "classify", "dispatch", "priority" |
| `Service & Ops Manager` | Runs the desk day to day | QA rubrics, SLA sweeps, queue hygiene, team-wide reporting |
| `CSM / Account Manager` | Owns the client relationship | Client health, QBR/SBR prep, risk scans, account-level summaries |
| `Security & Compliance Owner` | Security/audit-focused | Phishing, account takeover, audit prep, compliance checks |
| `Sales & Business Development` | Quoting, proposals, new business | Quoting, proposal drafting, lead handoff |
| `MSP Owner / Leadership` | Principal / exec | Portfolio-wide rollups, ROI, business-operations metrics |

## `outcome:` — what it's worth (browse-page filter facets)

Operational, not technical — this is the language a partner cares about, not the mechanism.
Card *display copy* should still be a bespoke verb-first line per skill (e.g. "Spot at-risk
accounts before they churn"), not the bucket name below — the bucket is the filter, not the
headline.

| Value | What it means |
|---|---|
| `Faster Resolution & Response` | Cuts time-to-first-response or time-to-resolution |
| `Fewer Escalations & Less Noise` | Reduces duplicate/reopened/misrouted tickets, alert noise |
| `Time & Cost Savings (Capacity)` | Frees tech/manager hours; billable-time recovery |
| `Always-On Coverage` | Works outside business hours or without a human watching |
| `Risk & Compliance` | Reduces security, audit, or compliance exposure |
| `Retention & Growth (CSAT/Expansion)` | Improves client health, CSAT/NPS, or surfaces expansion/churn signal |

## Tagging rule

Tag from the skill's actual mechanism, not its category. A category like `security` skews
toward `Risk & Compliance`, but a skill like Phishing Triage is *also* `Faster Resolution &
Response` (it resolves the report fast) — tag both if both are true. When genuinely
ambiguous between two roles or outcomes, tag both rather than guessing one.
