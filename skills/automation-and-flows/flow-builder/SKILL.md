---
name: Flow Builder
description: Design and create an automation flow from a plain-English ask — trigger, filters, actions, notification channels — with a dry-run description before anything is created. Use when asked to "build a flow", "automate X when Y happens", "notify the channel when a P1 comes in", or "set up an automation".
category: Automation & Flows
tools: [list_flows, get_flow, create_flow, update_flow, list_flow_actions, list_flow_filter_attributes, list_flow_filter_attribute_values, list_boards, list_ticket_statuses, list_ticket_priorities]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Flow Builder

**When to use:** "When a P1 comes in on the <client> board, notify the escalations channel" / "auto-set new email tickets to Needs Triage and assign the dispatcher" / "build a flow that runs the closure-QA skill when a ticket closes."

**Run it:** as a build task on request — you're authoring an automation, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Turn "when a ticket does X, do Y" into a correctly filtered flow. Building flows is admin-
only; if you can't, output the full flow spec (trigger, filters with exact values, actions)
for an admin to apply. Flows are ticket-EVENT triggered — there is no schedule/cron and no
ticket-age/duration/time-in-status condition; if the ask needs "after N hours" or "daily",
say so and make it a manual skill instead.

1. Parse the ask into trigger event, filter conditions, and actions. Ask one round of
   clarifying questions if the trigger ("created" vs "updated" vs "status changed to") is
   ambiguous — this is the most common flow bug.

2. Map every condition to real attributes — look up the actual filter attribute and its
   exact allowed values. NEVER guess a value string — "Priority 1" and "P1 - Critical" are
   different tenants' realities.

3. Map every action to a real flow action; look up any referenced board, status, or
   priority for its real id. Native flow actions are limited (set
   priority/status/board/agreement/team, assign, Reply, Note, Auto-Prioritize/Categorize,
   Generate Title/Recap, Run Skill, New Super Magic Agent) — anything else must run via
   Run Skill and that skill's own tools.

4. List the existing flows and check for ones on the same trigger and board. Flag overlaps:
   two flows firing on the same event can conflict or double-notify, and flow ordering may
   swallow the new one.

5. Present a DRY-RUN description before creating anything: "This flow fires when <event>.
   It matches tickets where <filters>. It then <actions>." Walk one concrete ticket
   through it, and one that would NOT match. For notification actions, state expected
   message frequency ("roughly N/day based on recent volume") so nobody builds a channel-
   spammer — estimate blast radius before any notification/auto-reply action.

6. On explicit confirmation ONLY: create (or update) the flow in an inactive state where
   supported. If the flow embeds an unattended agent prompt, apply the Unattended Output
   Discipline base skill to that prompt.

7. Report what was created, restate the dry run, and tell the admin to activate it
   themselves after eyeballing it — never activate without a separate, explicit yes.
```
