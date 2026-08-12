# Thread Super Magic — authoritative tool catalog

The **only** tools a skill may use. Confirmed against a live Thread MCP + the in-app
SuperAgent census (July 2026). If a skill's prompt references anything not on this list, it
is either a hallucinated tool (fix it) or an unsupported capability (the skill gets removed).
When validating, every tool in a skill's `tools:` frontmatter and every tool named in its
prompt must appear here.

## Native — always available (no connector needed)

Reads: `search_tickets`, `search_clients`, `search_contacts`, `search_members`,
`search_knowledge_base`, `search_thread_docs`, `web_search`, `list_boards`,
`list_ticket_statuses`, `list_ticket_priorities`, `list_recap_templates`.
Writes: `add_ticket_note`, `update_ticket`, `create_ticket`, `assign_contact`,
`log_time_entry`, `merge_ticket`, `schedule_ticket`, `update_schedule_entry`,
`send_approval`, `run_assistive_ai` (features: auto_priority, auto_ct, recap, title — this
mutates the ticket).

## In-app SuperAgent only (usable when the skill runs inside Magic, not the external MCP)

`view_openDraft` and the views family (`view_save`, `view_list`, `view_duplicate`,
`view_getCurrent`, `view_listFilterAttributes`, `view_searchFilterValues`,
`view_getCurrent`, …); the skills family (`load_skill`, `create_skill`, `update_skill`,
`list_skills`, `run_skill_on_ticket`); `create_recap`; `get_next_thread`; `send_client_email`.
The **runbook family** (`list_ticket_runbooks`, `recommend_runbooks`, `search_runbooks`,
`get_runbook_form_link`, `open_runbook_form`) is in-app only AND requires the partner to have
built a runbook library — treat as connector-grade (tag `connectors: [Runbooks]`).

## Admin — Flows & Intents (admin token only)

Flows: `list_flows`, `get_flow`, `create_flow`, `update_flow`, `activate_flow`,
`list_flow_actions`, `list_flow_filter_attributes`, `list_flow_filter_attribute_values`.
Intents: `list_intents`, `get_intent`, `create_intent`, `update_intent`, `create_variation`,
`update_variation`, `set_variation_arguments`, `set_variation_replies`.

## Connectors — available only when the partner has the integration on (tag them)

- **TimeZest** — `create_timezest_scheduling_request`, `get_timezest_scheduling_requests`,
  `list_timezest_appointment_types`, `list_timezest_resources`.
- **NinjaOne** (RMM) — `list_ninjaone_organizations`, `search_ninjaone_devices`,
  `get_ninjaone_device`, `get_ninjaone_device_activities`, `get_ninjaone_device_link`,
  `list_ninjaone_alerts`, `reset_ninjaone_alert`, `list_ninjaone_windows_services`,
  `control_ninjaone_windows_service`, `reboot_ninjaone_device`,
  `set_ninjaone_device_maintenance`, `set_ninjaone_device_approval`.
  ⚠️ No script execution, software deploy, or policy push — remediation is a deep-link handoff.
- **Liongard** — `liongard_environment`, `liongard_launchpoint`, `liongard_alert`,
  `liongard_detection`, `liongard_metric`, `liongard_events`, `liongard_timeline`,
  `liongard_device`, `liongard_identity`, `liongard_domain`, `liongard_cyber_risk_dashboard`,
  `liongard_report`, `liongard_agents`, `liongard_query`. (Universal read plane: filter
  launchpoint by systemType + JMESPath metrics reach ~300 inspectors.)
- **IT Glue** — `search_itglue`. **Hudu** — `search_hudu`.
- **ConnectWise RMM** — `connectwise_rmm_*` (device/company/patch/software reads).
- **ImmyBot** — `search_immybot_computers`, `list_immybot_tenants`, `get_immybot_computer`,
  `list_immybot_maintenance_sessions` (read-only).
- **Member MCPs** (each member connects their own): **Notion** (`notion-search`,
  `notion-fetch`, `notion-create-pages`, `notion-update-page`, `notion-create-database`,
  `notion-create-comment`, `notion-get-users`, …), **Linear** (`list_issues`, `get_issue`,
  `create_issue`, `update_issue`, `create_comment`, `list_projects`, `list_cycles`, …),
  **Zapier** (referenced as `Zapier: <App> "<Action>"` — only apps/actions that genuinely
  exist; verify with the discovery step). Zapier known gaps: NO Microsoft Bookings, NO
  Planner, Teams has no meeting-create.

## NOT supported — never build on these (remove any skill whose core needs them)

- **SMS / texting** — no SMS channel or send path. SMS may only appear as an audited *auth
  factor* (e.g. "SMS is a weak MFA method"), never as a send capability.
- **Telephony control** — dialing, call routing, porting. (Voice AI is a product surface,
  not an agent tool.)
- **RMM script execution / software deploy / policy push** — see NinjaOne note.
- **Anything not listed above** — if a prompt names a tool not in this file, it's
  hallucinated. Fix the prompt or, if the tool is load-bearing, remove the skill.

## Flows constraint (affects any "unattended" skill)

Flows are ticket-**event** triggered with **no** schedule/cron and **no** duration / ticket-
age / time-in-status condition. Cadence/digest/sweep skills run **manually**, not as a Flows
variant. Flow-native actions are limited (set priority/status/board/agreement/team, assign,
Reply, Note, Auto-Prioritize/Categorize, Generate Title/Recap, Run Skill, New Super Magic
Agent); anything else happens only when a Flow calls Run Skill and the skill uses its own
tools. See research/AUTHORING.md for the full flow action/condition lists.
