# Skill authoring spec

The format, quality bar, and capability ground rules for every skill in this library.
Written for humans and for AI writers generating skills at scale.

## File format

One folder per skill: `skills/<category-slug>/<skill-slug>/SKILL.md`

```markdown
---
name: Short Title Case Name
description: When to reach for this skill, in one line — it is the trigger the agent matches.
category: Human Readable Category
tools: [tool_a, tool_b]
---

# Short Title Case Name

One- or two-sentence framing: what this skill does and the outcome it produces.

## When to use

- 2–5 bullets of concrete situations (mirror real prompts partners type).

## Steps

1. Numbered, imperative steps. Reference tools by name where a call happens.
2. Keep branches inline ("If X → do Y; otherwise → Z").
3. End with what to output/post and in what format.

## Guardrails

- The non-negotiables. Confidence gates before writes. What NOT to do.
- Degradation note when an integration may be absent for the tenant.

## Unattended (Flows) variant   ← only for skills that run embedded in Flows

- Output discipline ("your entire reply is posted verbatim — no narration").
- Deterministic stop conditions; when in doubt, do nothing.
```

## Quality bar (from what actually propagates)

1. **Description = trigger.** Write it as *when to use this*; the agent matches against it.
2. **One workflow per skill.** Superset of the partner variants, not ten near-duplicates.
3. **Guardrails are the product.** Every skill that writes must carry: confidence gate,
   confirm-before-destructive, and a "when in doubt, do nothing" posture where relevant.
4. **Result-cap honesty.** If a search may hit a cap, say so in output rather than
   presenting an estimate as exact. Split searches per signal per board when scanning.
5. **Plain-text notes** where PSA compatibility matters (no markdown/emojis in notes
   destined for a PSA sync).
6. **No fabrication.** "Do not invent links, ticket numbers, or documentation."
   Zero-assumption rule: never convert a recommendation into a completed action.
7. **Sanitized.** No partner/client names, no people, no credentials, no board/person IDs.
   Use placeholders: <client>, <user>, <device>, "the VIP board".
8. **Localizable.** No idioms that break translation; note where desks run non-English.

## Capability ground rules (July 2026 — see research/tool-surface.md)

**Thread native (always safe to reference):** search_tickets, create_ticket, update_ticket,
add_ticket_note, log_time_entry, merge_ticket, schedule_ticket, update_schedule_entry,
assign_contact, send_approval, run_assistive_ai, search_clients, search_contacts,
search_members, search_knowledge_base, search_thread_docs, web_search, list_boards,
list_ticket_statuses, list_ticket_priorities, list_recap_templates,
create/update/get/list_flow(+actions/filter_attributes/filter_attribute_values),
create/update/get/list_intent, set_variation_arguments, set_variation_replies,
update_variation, create_timezest_scheduling_request, get_timezest_scheduling_requests,
list_timezest_appointment_types, list_timezest_resources.

**In-app SuperAgent only (note degradation for external MCP):** runbooks family
(list_ticket_runbooks, recommend_runbooks, get_runbook_form_link, search_runbooks,
open_runbook_form), views family (view_list, view_save, view_duplicate,
view_listFilterAttributes, view_searchFilterValues, view_getCurrent), skills family
(load_skill, create_skill, update_skill, list_skills, run_skill_on_ticket),
view_openDraft, send_client_email, create_recap.

**NinjaOne (when enabled):** list_ninjaone_organizations, search_ninjaone_devices,
get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link,
list_ninjaone_alerts, reset_ninjaone_alert, list_ninjaone_windows_services,
control_ninjaone_windows_service, reboot_ninjaone_device, set_ninjaone_device_maintenance,
set_ninjaone_device_approval.
⚠️ NOT supported: running scripts, deploying software, pushing policies, script library.
The remediation handoff is get_ninjaone_device_link (deep link the tech in).

**Liongard (when enabled):** liongard_environment, liongard_launchpoint, liongard_alert,
liongard_detection, liongard_metric, liongard_events, liongard_timeline, liongard_device,
liongard_identity, liongard_domain, liongard_cyber_risk_dashboard, liongard_report,
liongard_agents, liongard_query.

⭐ **Liongard is a universal read plane.** There is no per-inspector tool, but the generic
tools reach ALL ~300 Liongard inspectors: `liongard_launchpoint` filters by systemType
(e.g. "Meraki", "Palo Alto", "Veeam") to find any inspector's launchpoint, config, and
last-run state; `liongard_metric` evaluates any metric/JMESPath expression against any
inspector's dataprint; `liongard_detection`/`liongard_timeline` surface change history for
any system; `liongard_query` answers natural-language questions across all of it. This
means skills can read config/state from firewalls, switches, hypervisors, backup platforms,
cloud tenants, and LOB systems that Super Magic has NO native integration for — as long as
the partner runs the Liongard inspector. Skills using this pattern must (a) verify the
inspector exists and last ran successfully (launchpoint/timeline) before trusting data,
(b) state dataprint age in output, and (c) degrade to docs/ticket-history when the
inspector is absent.

**Docs (when enabled):** search_itglue, search_hudu.
**ConnectWise RMM (when enabled):** connectwise_rmm_search_devices,
connectwise_rmm_list_companies, connectwise_rmm_get_device (+ patch/software reads).
**ImmyBot (when enabled):** search_immybot_computers, list_immybot_tenants,
get_immybot_computer, list_immybot_maintenance_sessions (read-only today).

**MCP connectors (member-authenticated; note in guardrails that the member must have
connected them):**
- Notion: notion-search, notion-fetch, notion-create-pages, notion-update-page,
  notion-move-pages, notion-duplicate-page, notion-create-database,
  notion-update-data-source, notion-create-view, notion-update-view,
  notion-query-data-sources, notion-create-comment, notion-get-comments, notion-get-users.
- Linear: list_issues, get_issue, create_issue, update_issue, list_comments,
  create_comment, list_issue_statuses, list_issue_labels, create_issue_label,
  list_projects, create_project, update_project, list_cycles, list_teams, list_users,
  list_documents, get_document.
- Zapier: reference as `zapier: <App> "<Action>"` (e.g. `zapier: Microsoft Teams "Send
  Channel Message"`). Verified inventories in research/connectors.md. Known gaps:
  NO Microsoft Bookings, NO Planner, Teams has no meeting-create (use Outlook "Create
  Event"), Entra ID has writes but no user search.

## ⛔ Capability honesty — verify before you build (read this first)

A skill may ONLY promise an outcome Thread/Super Magic can actually deliver. Before writing
a skill, confirm the capability exists — via the live Thread MCP tool list for the tenant,
the flow-capability lists below, or the connector reality check. If it can't be verified,
don't build it.

**Things Thread does NOT support (do not build skills whose core outcome is one of these):**
- **SMS / texting** — there is no SMS channel and no supported SMS-send path. SMS may only
  appear as an *auth-factor being audited* (e.g. "SMS is a weak MFA method"), never as a
  send capability. (Removed: zapier-twilio-sms-updates, zapier-ringcentral-telephony,
  sms-channel-etiquette.)
- **Telephony control** (dialing, call routing, porting) — Voice AI is a product surface,
  not an agent tool.
- **RMM script execution / software deploy / policy push** — see NinjaOne note above.

**Connector reality (production-verified).** The only member-MCP connectors that exist are
**Notion, Linear, Zapier** (SUPER_AGENT_MCP_CATALOG). In the entire production history the
only connectors partners actually invoked are Notion (heavy), Linear (light), and Zapier
(light — mostly Firecrawl web-scraping). Zapier's 9,000-app catalog is *theoretically*
reachable, but a Zapier-app skill is only real when (a) the member has connected Zapier,
(b) that app is authenticated in their Zapier, and (c) the specific action exists. Every
Zapier skill MUST open with that verify-first gate (zapier-action-discovery) and stay
honest that it depends on member setup. Do not add Zapier skills for apps that don't map to
a genuine, supported MSP↔Thread workflow.

## Flows — exact ground truth (a skill's "Unattended (Flows) variant" must fit this)

Skills run **manually** (a member invokes them in chat / on a ticket) OR **through a Flow**
(the `Run Skill` / `New Super Magic Agent` flow action fires them). A skill whose only
viable mode would be an unsupported flow trigger cannot exist as a Flows skill "right now" —
make it a manual skill and OMIT the Unattended section, or drop it.

**Flows are ticket-EVENT triggered, evaluated against conditions. Flows are NOT scheduled
and have NO cron.** There is no "daily/weekly/nightly" flow. Recurring digests and sweeps
are **manual** skills (or run by an external scheduler), never a Flows variant.

**Flow CONDITIONS (filter attributes) that exist** — board, status (+ status name),
priority, type/subType/item, ticketType/ticketCategory, summary, site/serviceLocation/
territory/city/addressLine1/country, company/companyType, contact/contactType, team, owner,
member, source, agreement/agreementName/agreement_type, sla, severity, budgetHours,
opportunity, threadSentiment (number) + sentimentRange, inbox/messenger touchpoint,
**dateEntered (day-of-week), timeEntered (time-of-day), date**.
**Conditions that DO NOT exist** — ticket **age / duration / time-in-status / time-since-
last-update / elapsed time**, "minutes remaining on SLA", or any relative-time trigger.
So skills keyed on "after N hours idle", "dwell time in a status", "N days stale",
"X minutes after appointment end" CANNOT be flow-triggered. A flow CAN fire on the *event*
of entering a status; it CANNOT fire "N hours after" that. Correct the Unattended section
accordingly (fire-on-event, not fire-after-duration), or make the skill manual-only.

**Flow ACTIONS that exist (the only things a flow can DO natively):** set priority, set
status, set board, assign member, set agreement, set resource team, Reply, Note,
Auto Prioritize, Auto Categorize, Generate Title, Generate Recap (template), **Run Skill**,
**New Super Magic Agent**. A flow CANNOT natively send email/SMS, create/merge/schedule a
ticket, log time, send an approval, call a webhook, or run a Zapier action. Those only
happen when a flow calls Run Skill / New Super Magic Agent and the *skill* (running as a
Super Magic agent) uses its own tools. So an Unattended variant's writes are limited to
what a Super Magic agent can do when invoked — state that, and keep unattended writes
conservative.

## Category taxonomy

triage-and-routing · qa-and-closure · communication · documentation · escalation ·
onboarding-and-access · devices-and-infrastructure · security · reporting-and-analytics ·
account-management · scheduling-and-dispatch · automation-and-flows · finance-and-billing ·
sales-and-quoting · client-lifecycle · training-and-enablement · personal-productivity ·
troubleshooting-playbooks · compliance-and-audit · connectors (cross-tool workflows that
exist because of Notion/Linear/Zapier) · psa-specific (ConnectWise/Autotask/Halo idioms) ·
vendor-runbooks (named security/backup/infra products) · liongard-inspectors (reading any
system through Liongard's inspector data) · m365-administration ·
change-and-problem-management · voice-and-messenger · industry-packs (vertical-specific
client support) · msp-business-operations (the MSP's own internal ops)

**Vendor names are allowed** (Veeam, Huntress, SentinelOne, Datto…) — they are products,
not partner data. The sanitization bar covers partners, clients, people, credentials, and
environment-specific identifiers only. Keep vendor guidance factual and version-cautious
("verify against the vendor's current docs").
