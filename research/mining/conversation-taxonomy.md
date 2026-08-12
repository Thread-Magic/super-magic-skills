# Super Magic conversation taxonomy — all ~27,770 conversations (July 2026)

Merged from four full-coverage mining passes over `SUPER_AGENT_CONVERSATIONS`
(each slice read 100% of its rows — titles plus first user messages; no sampling).
All examples sanitized. Counts are cross-slice extrapolations; single-partner skews
were noted per slice and discounted where flagged.

## Headline shape of usage

| Bucket | Share | What it is |
|---|---|---|
| Unattended automation runs | ~20–25% | Super Magic invoked from Flows / skills / external APIs as an autonomous ticket worker |
| Working the ticket in front of you | ~24% | Summarize, troubleshoot, next steps, explain the ask, ticket forensics |
| Client-facing communication drafting | ~9–13% | Draft replies, polish tone, closures, follow-ups, difficult conversations |
| Ticket search & institutional memory | ~8–10% | Similar tickets, entity history, environment/asset knowledge |
| Ticket operations by chat | ~5–6% | Create/update/assign/schedule/merge/close + time entries |
| Reporting & analytics (leads/execs) | ~4–5% | Tech performance, queue health, trends, SLA, QA at scale |
| Ticket-context sessions on op. ticket types | ~11% | Onboarding/offboarding, M365 admin, hardware/network, procurement, telephony |
| Personal work management | ~3.5% | Daily digest, "what should I work on", EOD, calendar |
| Security & phishing | ~2.5% | Phish verdicts, header analysis, EDR/SOC alerts, containment |
| Documentation & knowledge | ~3% | IT Glue/Hudu/KB retrieval and creation |
| Automation building (meta) | ~2% | Mine tickets → intents; build flows/skills/views; tune triage agent |
| Device / RMM / infra ops | ~1.7% | NinjaOne lookups/reboots, Liongard queries, patching, backups |
| Thread product help & admin | ~2.5% | Config questions, capability probes, bug reports |
| CSM / vCIO / QBR | ~1.5% | QBR prep, health scans, churn analysis, roadmaps |
| Billing / finance / sales | ~1% | Billable analysis, invoice disputes, quotes, agreement profitability |
| Voice-call transcript processing | ~0.7% | Pasted transcripts → extract issue → act |
| Staff training & self-onboarding | ~0.5% | New-hire coach, quizzes, roleplay |
| Multilingual usage | ~0.7% | Dutch, Spanish, French, German, Norwegian, Bulgarian |
| Empty / test / social | ~6% | Aborted sessions, greetings, capability pokes |

## The automation-run majority (biggest single finding)

Partners operationalize Super Magic as an **unattended workforce**, not a chat assistant.
Recurring embedded-agent families (each observed across multiple slices):

1. **Auto-prioritization agents** on alert boards ("priority classification agent… set one of three priorities from title and description")
2. **Runbook recommenders** ("high-confidence only; a wrong runbook is worse than no recommendation; post the form link")
3. **Closure QA gates** triggered on status change (fetch full thread, grade closure quality, reopen + itemized note on fail)
4. **Status choreography** (courtesy-reply revert, "AI Working Issue" status, log-time-on-customer-responded)
5. **Catchall/company identification** on unassigned tickets (reassign only when unambiguous)
6. **Alert-title normalization** (classify alert, rewrite summary to standard, note)
7. **Sentiment explanation** on trigger ("why did this thread receive this score?")
8. **Duplicate hunters** with autonomous merge
9. **External JSON API integrations** ("respond with ONLY a raw JSON object": per-ticket root-cause diagnosis, self-service deflection analysis)
10. **Daily digest skills** ("summary of my open tickets — needs replies / urgent / prioritize")

## Role census (human sessions)

| Role | Share | Signature asks |
|---|---|---|
| Technician (L1–L3) | ~70% | per-ticket work, drafting, time entries, troubleshooting |
| Service manager / team lead | ~5% | tech performance, coaching, PIP candidates, QA sweeps, workload balancing, weekly KPI reports |
| Dispatcher / coordinator | ~2% | bulk assignment by load, round-robin, morning digests, P1/P2 template reports, scheduling |
| CSM / vCIO / account manager | ~3% | QBR prep, health scans, sentiment/churn, roadmaps, upsell, meeting prep ("meeting in 30 min — prep me") |
| Automation engineer / Thread admin | ~2% (+ configured the ~22% automated volume) | intents from ticket mining, flow building, skill authoring, triage-agent tuning |
| Owner / exec (CEO, COO, director) | ~0.5% | "review the service desk yesterday", zero-touch strategy, forecasts, "biggest glaring issues", queueing-theory staffing |
| Finance / billing | ~0.5% | billable vs unbillable, effective hourly rate per AYCE agreement, invoice disputes, license cost optimization |
| Trainer / onboarding guide | ~0.3% | "how is <new hire> doing", quizzes, roleplay, curriculum |
| Sales / pre-sales | ~0.2% | scope-of-work, quotes, prospect collateral, challenger-sale coaching |
| HR / internal ops | ~0.2% | PTO, expenses, facilities tickets, interview simulation |

## High-signal recurring prompts (verbatim-class, sanitized)

- "summarize this ticket and the current issue — likely next troubleshooting steps"
- "draft an email to <user>: account unlocked / called and left voicemail / still working with vendor"
- "write this nicely: …" / "make this better (no '—' characters)" / "mejorar ingles: …"
- "any similar tickets with a resolution?" / "has this user had this before and what fixed it?"
- "create a ticket for <contact> at <client>, assign to me, 30-min time entry, close it" (drive-by capture)
- "give me a summary of my open tickets — what needs replies, anything urgent"
- "analyze previous tickets and create intents based on common trends"
- "assign unassigned tickets to whoever is least busy"
- "I have a QBR today — generate an overall summary report for <client>"
- "why did this thread receive this sentiment score?"
- "evaluate all helpdesk technicians over the past three months"
- "what PC does <user> use?" / "do we have iDRAC creds?" / "what's the wifi password for this client?"
- "is this a phishing email? analyze this header"
- "search IT Glue for <client>'s new-user setup document"
- "what should I work on today?"

## Rare & creative use-cases → new-skill seeds

Business/exec: proactive business insight ("what's important that nobody asked about?"),
queueing-theory staffing model, ticket-volume forecasting, post-churn autopsy, churn-save
deep dive, EOS/rocks planning, client newsletter mining, health-score reconciliation.
Ops: engineer complexity scoring (3 independent partners), shift-overflow tracking,
Rewst/RPA feasibility scan, zero-touch opportunity mining (multiple partners, near-identical
phrasing), self-service deflection analyzer, bad-review dispute prep, morning huddle builder.
Comms/docs: post-mortem/RCA authoring, PIR docs, cyber-insurance form filling, SOC2/CMMC
evidence prep, compliance questionnaires, PDF/CSV report exports, PowerPoint IT roadmaps,
client-facing device report from RMM.
Tech: cross-platform step translation (Win→Mac), screenshot OCR + translation, password
generation to policy, VBA/Excel macro generation, AI-to-AI handoff prompts, export ticket
for another LLM.
People: interview simulation, new-hire coach + quizzes, technician self-review, mindset
coaching, training video outlines, Super Magic show-and-tell prep.
Voice: transcript intake pipeline (paste call → extract issue → ticket + time entry),
voicemail summarization, field-tech voice dictation, dead-air call filtering.
Cross-tool: Notion page creation, Teams praise messages, Outlook calendar reads, OpenSearch
log pulls, "what Zapier tools do you have?"
Delight: fun-fact client emails, persona replies ("explain as Mr T"), roasts/poems (leave out).

## Design implications

1. **Two product lines of skills:** attended (chat copilot) vs unattended (flow-embedded
   agent). Unattended skills need machine-grade output discipline ("your entire reply is
   the note"), deterministic guardrails, and JSON-mode variants.
2. **The head is automatable, the tail is monetizable.** Top-10 prompt families cover
   ~40% of volume — canonical skills for those must be excellent. The long tail (5,000+
   distinct patterns/slice) justifies the 1,000-skill catalog.
3. **Language matters:** ship localizable skills; ESL tone-polish is a daily-driver.
4. **Result-cap honesty and confidence gates** appear in partners' own prompts — bake in.
5. **Single-partner skew:** several heavy families come from one partner each; weight by
   distinct companies when prioritizing (done above).
