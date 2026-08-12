# Super Magic — Full Tool Surface (observed July 2026)

The capability map skills can draw on. Sources: the connector reference, the live MCP tool
list, and a census of every tool call Super Magic has made in production (354k messages,
~28k conversations). Tools marked ⭐ were observed in real usage but are missing from the
published connector reference.

> **How to read the census.** The call log records *attempts*, including calls to tools
> that don't exist — the model guessed a plausible name and failed. Anything with 1–2
> calls and a name variant smell (`add_ticket_`, `view.list`, `run_ninjaone_script`,
> misspelled `liongard_*`/`notion-*` forms) is a hallucinated attempt, **not** a
> capability. Ground truth for what a skill may use is the live MCP tool list for the
> tenant (which varies by member permissions + enabled integrations). Failed attempts
> are kept below in "Demand signals" — they show what techs *wanted* the agent to do.

## Ground truth vs demand

**NinjaOne actually supports:** device/org lookups, hardware/OS detail, activities, alerts
+ reset, Windows services start/stop/restart, reboot (normal/forced), maintenance mode,
device approval, remote-session deep link.
**NinjaOne does NOT support (yet):** running scripts, deploying software, pushing
policies, script library access, custom scripts. Skills must not assume script execution —
the remediation step is "deep-link the tech into NinjaOne."

## Demand signals — tools the agent reached for that don't exist

Failed/hallucinated call attempts worth treating as product-gap votes:
`run_ninjaone_script`, `get_ninjaone_device_software`, `get_ninjaone_device_os_patch_status`,
`list_ninjaone_device_roles`, `send_client_email` (if unavailable per tenant),
`get_next_thread`, various Liongard bulk/metric endpoints, Notion SQL-variant names.
When a skill's natural next step is one of these, the skill should say what to do instead
(deep link, manual step note, or approval request).

**In-app vs external MCP surface.** The in-app SuperAgent census shows tool families the
external Thread MCP does not expose (runbooks, views management, load/create/update_skill,
view_openDraft, send_client_email, recaps beyond templates). A live check against a demo
tenant's external MCP shows: ticket CRUD + searches, flows/intents/variations, TimeZest,
recap templates, send_approval, run_assistive_ai, web_search — and integration tools only
when that integration is enabled for the tenant. Skills should degrade gracefully when a
tool family isn't present ("if runbook tools are unavailable, search the KB instead").

## Thread native — tickets & PSA

| Tool | Observed calls | Notes |
|---|---|---|
| search_tickets | 66,062 | The workhorse. Every skill leans on it. |
| search_knowledge_base | 8,692 | Internal KB + past resolved threads |
| search_clients | 6,877 | |
| add_ticket_note | 5,895 | Internal + external notes |
| update_ticket | 5,494 | Status, priority, assignee, board |
| search_contacts | 3,938 | |
| search_members | 2,306 | |
| search_thread_docs | 1,897 | Thread product docs |
| log_time_entry | 1,179 | |
| list_ticket_statuses / list_ticket_priorities / list_boards | 3,859 | Discovery calls |
| create_ticket | 636 | |
| schedule_ticket / update_schedule_entry | 450 | |
| assign_contact | 103 | |
| merge_ticket | 53 | |
| send_approval | — | Available, low observed use |
| run_assistive_ai | 219 | Auto-title/category/priority/recap |
| list_recap_templates / get_recap_template / create_recap ⭐ | 49 | Recap workflows |
| web_search | 1,756 | Built-in web lookup |
| send_client_email ⭐ | 1 | Direct external email — high guardrail need |
| get_next_thread ⭐ | 2 | Queue-walking |
| view_openDraft ⭐ | 406 | Reads the member's open reply draft |

## Thread native — runbooks ⭐ (entire family absent from reference)

| Tool | Observed calls |
|---|---|
| list_ticket_runbooks | 1,795 |
| get_runbook_form_link | 640 |
| recommend_runbooks | 79 |
| search_runbooks | 12 |
| open_runbook_form | 5 |

## Thread native — views ⭐ (inbox view management)

view_searchFilterValues (802), view_listFilterAttributes (271), view_save (144),
view_list (67), view_getCurrent (54), view_duplicate (13), view_open (11), view_delete (1).

## Thread native — automation building

| Family | Tools | Observed |
|---|---|---|
| Flows | list/get/create/update_flow, list_flow_actions, list_flow_filter_attributes(+values), activate_flow | ~1,230 |
| Intents | list/get/create/update_intent, variations, set_variation_arguments/replies | ~990 |
| Skills | load_skill (841), create_skill (226), update_skill (192), list_skills, run_skill_on_ticket | ~1,270 |

Super Magic builds its own automations — meta-skills (skills that create flows,
intents, views, and other skills) are a first-class category.

## NinjaOne (RMM)

search/get devices (919), device activities (127), alerts (207+), organizations (244),
windows services (96), device link (29), reboot (9), reset alert (12), maintenance mode (11),
device approval. (Script execution, software deploy, policy push: NOT supported — the
1-count `run_ninjaone_script` etc. in the census were failed attempts; see Demand signals.)

## ConnectWise RMM ⭐ + Automate ⭐ + ImmyBot ⭐ (in tool settings, absent from reference)

connectwise_rmm_search_devices (51), list_companies, get_device, patch status, software,
scripts, tasks, sites. ImmyBot: search_immybot_computers, list_immybot_tenants,
list_immybot_maintenance_sessions, get_immybot_computer. Integration keys also exist for
`integration_automate` (ConnectWise Automate).

## Liongard

Heavily used (~1,600 calls): launchpoint (331), metric (227), environment (163),
cyber_risk_dashboard (155), identity (151), device (109), alert (71), detection (60),
timeline (50), agents (30), report (19), query (9), domain, plus raw API access via
lg-readme endpoints.

## TimeZest

create_timezest_scheduling_request (82), list appointment types (62), resources (47),
get requests (62).

## Documentation sources

search_itglue (1,547), search_hudu (96).

## MCP connectors (member-authenticated)

| Connector | Observed usage |
|---|---|
| Notion | ~1,000 calls: fetch (301), update-page (253), query-data-sources (119), search (83), create-pages (48), create-database (11), get-users, SQL-style queries |
| Linear | Early: list_issues, list_teams, list_issue_labels, save_issue, list/search_customers, get_issue_status, list_team_states |
| Zapier | Early: run_tool, discover_zapier_actions, get_configuration_url, and Firecrawl actions (extract/crawl/scrape/search/agent) |

## Enablement snapshot (companies with the integration toggled on)

IT Glue 137 · TimeZest 59 · NinjaOne 54 · Hudu 33 · Liongard 20 · CW RMM 17 ·
Automate 12 · ImmyBot 3. Write-tool opt-ins are still rare (create/update ticket,
merge, schedule, log time ≤ 4 companies each) — write-heavy skills need guardrails
that assume approval-style flows.

## Adoption curve

Apr 2026: 59 convos / 2 companies → May: 189 / 7 → Jun: 9,194 / 143 → Jul (half month):
18,328 / 435 companies / 2,125 members. Partner-authored skills: 469 live (232 personal,
237 shared), 86 deleted.
