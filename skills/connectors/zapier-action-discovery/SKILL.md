---
name: Zapier Action Discovery
description: META skill — before promising any workflow involving an external app, find out whether a Zapier action for it actually exists, what fields it takes, and what it will cost in tasks. Use for "can we integrate with <app>", "does Zapier have an action for X", "what Zapier tools do you have", or as step zero of designing any connector workflow.
category: Connectors
tools: []
connectors: [Zapier]
scope: global
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Zapier Action Discovery

**When to use:** "Can Super Magic post to / create records in / read from <app>?" or as step zero before designing any new connector workflow.

**Run it:** as a one-off discovery check (not tied to a single ticket).

## Prompt

```
The anti-vaporware skill: verify a Zapier action exists before the workflow is designed — named
exactly, with its real fields and limitations — because "Zapier has 9,000 apps" is not the same as
"Zapier has the action you need".

This needs the member's connected Zapier even to discover. Without it, answer from the verified known
inventory only, label it with its verification date, and recommend connecting Zapier to confirm — do
not stop. Discovery is read-only: finding an action must never enable or execute it; enabling writes
is the admin's deliberate move.

1. Check the curated server first. If the tenant runs a curated Zapier server, list what's actually
   pinned — those are the only actions available in locked mode, regardless of the catalog. An action
   existing in Zapier but not pinned means "ask the admin to add it", not "yes". When the catalog
   conflicts with the curated list, the curated list wins for "what can we do today".
2. Check the known-gaps list before searching (verified July 2026): Microsoft Bookings — no
   integration (use Calendly or Outlook Create Event); Microsoft Planner — none (use To Do, Linear,
   or Jira); Teams — cannot create meetings (use Outlook "Create Event" with an online meeting); Entra
   ID — writes only, no user search (resolve identity from the PSA/ticket side first); SmileBack —
   legacy app removed (use the native PSA integration). Match a gap → give the substitute immediately.
3. Search the catalog (dynamic-discovery mode) for the app and the specific verb needed. Capability
   claims require the exact action name — "Create Time Activity", not "something for timesheets".
4. Verify the action's shape before promising: required fields, whether the needed lookup exists (many
   apps have writes but weak Find actions), any mode/plan constraints.
5. State the cost: each successful Zapier call = 2 Zapier tasks. Estimate the workflow's consumption
   honestly (per-run calls × expected frequency) — a per-ticket, 3-call workflow on a 1,000-ticket/
   month board is 6,000 tasks/month; say that number out loud before anyone wires it.
6. Report the verdict in one of three forms: Exists (exact action name(s) as zapier: <App> "<Action>",
   required fields, task-cost estimate, and for recurring/unattended use the recommendation to pin it
   on a curated server with sensitive fields locked); Exists with caveats (the action plus the
   limitation that changes the design); Doesn't exist (say so plainly, name the nearest verified
   substitute, or route to Thread-native / Notion / Linear when they fit better). Never promise a
   workflow on an unverified action name, and carry the verification date — a verdict older than a few
   months should be re-verified before a build.
```
