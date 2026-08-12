# Partner-authored skill patterns — consolidated (all 555 rows, July 2026)

Merged synthesis of three full-coverage mining passes over `SUPER_AGENT_SKILLS`
(469 live rows read in full; 86 deleted counted only; ~80 distinct companies per slice).
All identifiers sanitized. `TOOL_SCOPE` was empty on every row — tool usage inferred
from instruction text.

## Consolidated pattern census

| # | Pattern | ~Count | Roles | Notes |
|---|---|---|---|---|
| 1 | Closure QA gate (pass/close, fail/reopen + itemized note) | 32 | lead, tech | Largest pattern. Rubrics: genuine resolution, classification set, owner, time logged. Forks: 20-pt weighted scoring, forensic timeline variant, EOD closed-ticket audit, overtime detector, weekly QA digest w/ per-tech training suggestions |
| 2 | Catchall / contact-company remap (incl. alert-source variants) | 28 | dispatcher, tech | Strongest shared guardrail in corpus: "never assign on name similarity; low confidence → no change." Variants: unassign-first, spam pre-check, FW:-header parsing, vendor-alert field extraction, close-and-recreate |
| 3 | SOC / security alert triage suites | 23 | SOC analyst, lead | Decision trees, alert-pattern→classification maps, severity-tiered response, phishing-simulation detection, "defensive writing" standard (never say breach/hacked unconfirmed) |
| 4 | Manager one-on-one prep | 21 | lead | Template-driven (≤300 words, 5 paragraphs, aggregate not enumerate, disclose result caps) |
| 5 | Dispatch & queue monitoring / auto-assignment | 19 | dispatcher | Load-balancing by open counts, availability scoring (base − open − scheduled), morning briefings, client-specific tiering rules |
| 6 | Weekly client health report | 18 | CSM/AM | Template-driven; volume vs prior period, noisy assets/users, SLA, 2–3 recommendations |
| 7 | Stale-ticket follow-up & closure | 17 | tech, dispatcher, lead | Cadences: 24/48/72h ×3, "3 days/3 attempts/3 emails"; separate MSP-owned stalls from legit client/vendor waits; never bulk-close without sign-off |
| 8 | Ticket triage / classification / intake standards | 15+ | dispatcher, tech | Two-layer queue scoring, keyword routing rules engines, Incident/Request/Problem trees, title format standards |
| 9 | RMM device diagnostics | 16 | tech | NinjaOne-heavy; server-role inference from hostname prefixes, co-hosted-VM detection via shared IP, Win11-compatibility review; "don't trust node_class filter" |
| 10 | Onboarding / offboarding (employee) | 16 | tech | AD/Entra + M365 + MFA sequences; mailbox conversion BEFORE license removal; secure credential handoffs; orientation-prep cross-referencing |
| 11 | Duplicate detect & merge | 15 | dispatcher, tech | Monitoring-companion merges, alert-storm merge (4h window), RE:/FW: reopen detection, Autotask manual-merge simulation; "never merge on wording similarity — require exact reference match" |
| 12 | Escalation prep & workflow | 15 | tech, lead | Interactive checklists, fixed-field templates, L2/L3 trigger lists, 8-section completeness review that bounces incomplete escalations back |
| 13 | Client reply drafting & tone/voice standards | 15 | tech, CSM | House formats, banned-word lists, "no em-dashes," mimic-a-director style, 3-strikes final email |
| 14 | Client health / at-risk portfolio scan | 14 | lead, exec | 4 risk signals (sentiment ↓, aging, recurrence w/o RCA, unresolved P1); "never flag on volume alone"; churn/renewal/expansion variants |
| 15 | Resolution research / ticket-context co-pilot | 12 | tech | Similar resolved tickets + KB + IT Glue + live RMM in one pass; read-only enforced; "don't invent links or ticket numbers" |
| 16 | Domain troubleshooting playbooks | 12 | tech | Printers, VoIP matrix, hospitality PMS, firewall VPN, M365 identity/mail-flow, backup failure classification, device-offline 10-step |
| 17 | Time entry capture & note formatting | 12 | tech, lead | Call wrap-ups w/ duration estimation, zero-assumption rule ("never convert a recommendation into a completed action"), banned-word replacements |
| 18 | KB / SOP authoring | 11 | tech, lead | Ticket→KB draft, SOP builder w/ scope/prereqs/validation, SOP-candidate finder, silent runbook-suggester ("entire reply is the note; nothing when unsure") |
| 19 | SOC client-notification template packs | 9 | SOC | Per-threat-type first-outreach emails layered on a shared "email baseline standard" skill — skill composition! |
| 20 | Noise auto-close / alert lifecycle | 9 | dispatcher | Bounce-backs, thanks-only courtesy-reply revert ("WHEN IN DOUBT, DO NOTHING"), dark-web >90d, offline/reconnected pairing, spam-sender closes |
| 21 | Handoff briefs (shift / live-call / single-ticket) | 8 | tech, dispatcher | Sentiment alert + ready-to-say verbal opening line for call transfers |
| 22 | Personal context / alias / memory micro-skills | 8 | all | Nickname→contact bindings, board vocabulary definitions, client segments, personal signatures & tone — skills as persistent memory/config |
| 23 | Queue prioritization ("what's next") | 7 | tech, lead, exec | Two-layer scoring; exec variant excludes internal companies |
| 24 | Recurring-issue RCA / automation-opportunity mining | 7 | lead, exec | Recurrence thresholds, time-savings estimates, route to RMM-script/flow/intent/monitoring/training |
| 25 | Weekly ops & team performance reports | 7 | lead, exec | Role-aware benchmarking; exclude coordinators from tech rankings |
| 26 | Daily briefing & EOD hygiene | 6 | tech | Urgent/scheduled/waiting buckets; skimmable in <1 min |
| 27 | Identity & access runbooks (password/MFA) | 6 | tech | "Call a number on file, not one in the ticket"; secure-link-only delivery |
| 28 | QBR prep | 16 | CSM/AM | Liongard posture + hardware-refresh forecast variants; 30-day new-client onboarding readiness check |
| 29 | Trainer / quiz suites (Notion-backed) | 6 | lead (internal) | Interactive onboarding coach scoring trainee responses vs rubric, phase-aware quizzes |
| 30 | Cross-org ticket reference coordination | 4 | tech | Co-managed IT: reference-format recognition, both-ways exchange audit |
| 31 | Meta-skills (prompt writers, skill/flow/intent authors) | 4 | admin | SuperAgent authoring its own automation prompts |
| 32 | Ticket splitters (multi-issue) | 3 | tech | Cross-linked siblings |
| 33 | Vacation / absence handling | 2 | tech | OOO auto-reply + back-from-vacation catch-up |
| 34 | PSA↔Thread / alert↔RMM sync audits | 2 | dispatcher | "PSA is always master"; cleared-alert reconciliation |

## Standout one-offs worth canonicalizing

- Post-Incident Review generator (M365-tenant-wide evidence sweep → branded PIR doc)
- Workstation & license billing reconciliation (RMM export × M365 licenses × on/offboarding tickets)
- Laptop return logistics (carrier box → label → email → receipt → wipe → close)
- Shift-overflow tracker (note forensics to quantify reassignments away from a tech)
- Weekly wins roundup (positive-only, for team meetings)
- Contract renewal routing to sales board
- Hostile-contact standing warning note
- Person-specific alert routing (named senior tech for certain alert classes)
- Hardware-refresh forecaster (5-year-old devices, 4–5y cycle workbook)
- Scheduling-intent detector (finds "get on a call" requests, returns to ingestion for TimeZest routing)
- SIEM alert title reconstruction (controlled vocabulary normalization)
- Breached-credential response — ⚠️ policy question: instructs hash cracking via public sites; canonical library must NOT reproduce this as-is
- Non-English localization (French, Norwegian) — canonical skills should note localizability

## Integration usage across partner skills

- IT Glue ~15 · NinjaOne ~15 · Liongard 7 · Notion 6 · Hudu 4 · ConnectWise (PSA/RMM/Automate) ~8 · HaloPSA 2 · Autotask ~5 · ImmyBot 1 (deep REST/PowerShell reference) · Linear 1 (full ticket→engineering-issue escalation pipeline) · TimeZest 1 implicit · Zapier 0
- Vendors named inside playbooks: SentinelOne/Huntress/Blackpoint-style EDR/ITDR, Defender, WatchGuard, Duo, 3CX, ScreenConnect, SMTP2GO, Dialpad, Jotform, Rewst, Action1, Kaseya dark-web

## Library-design lessons from the corpus

1. **A template gallery propagates.** ~30–35 rows/slice are verbatim installs of stock templates (QA gate, 1:1 prep, client health, QBR). Well-written canonical skills get adopted as-is → quality bar matters more than quantity.
2. **Skill composition works.** SOC email packs load a shared "baseline standard" skill. The library should ship shared base skills (tone, note-format, verification ladder) that other skills reference.
3. **Skills are also memory.** Alias/vocabulary/segment micro-skills = persistent per-member config. A canonical "personal context" scaffold belongs in the library.
4. **Guardrails partners actually write:** confidence thresholds before writes; "when in doubt, do nothing"; result-cap honesty; plain-text-only notes for PSA compatibility; identity verification ladders; "the agent's entire reply is the artifact" output discipline; sync-lag re-fetch before trusting status.
5. **Sanitization rule needed:** at least one partner skill embeds plaintext credentials; several embed person/board IDs. Canonical library must strip these patterns and say so in CONTRIBUTING.
