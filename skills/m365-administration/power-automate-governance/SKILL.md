---
name: Power Automate Governance
description: Bring Power Automate under control — find orphaned flows owned by leavers, reassign ownership before it breaks, and govern which connectors staff can use. Use when a client asks who owns their flows, reports an automation that "just stopped," offboards a power user, or wants to restrict Power Platform connectors.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Risk & Compliance]
---

# Power Automate Governance

**When to use:** A client reports a scheduled automation that stopped working (often: owner's account disabled), asks "who owns all these flows," offboards a user who built automations, or wants to restrict which connectors staff can use in Power Automate. This is about a client's Microsoft Power Automate (Power Platform) tenant — distinct from Thread's own automation Flows. NOT for building a specific business flow for the client (that's a project), and NOT for Thread's automation Flows.

**Run it:** on one client's request — you inventory and prepare the handover, a technician drives the portals (not a Flow: it needs a human at the console).

## Prompt

```
You govern the Power Automate estate MSPs inherit whether they like it or not: flows built by staff, owned personally, running silently — until the owner leaves and the automation dies with their account. This covers ownership hygiene, offboarding handover, and connector governance for a CLIENT's Power Automate (Power Platform) tenant, not Thread Flows. Largely a proposal + prepared handover; the tech drives the portals. Never invent data.

1. Inventory before governing. With the client's Power Platform admin, list flows per environment, their owners, their run state (on/off, recent failures), and the connectors each uses. Flag flows owned solely by disabled/departed users and flows failing repeatedly — those are the time-bombs. (Check the client's documentation for documented flow ownership — skip gracefully if not connected.)

2. Orphaned-flow reassignment. A flow owned only by a leaver stops when the account is disabled. For each, identify the business process it drives and a suitable new owner (or co-owner) BEFORE the account is removed — add a co-owner so the flow survives account deletion. Where the process is dead, propose disabling the flow rather than leaving it to fail silently. Sequence this into offboarding so it happens before the account goes.

3. Connector governance. Recommend Data Loss Prevention policies for Power Platform that classify connectors (business / non-business / blocked) so a flow can't quietly bridge, say, corporate SharePoint to a personal consumer service. Scope per environment; a blanket block breaks existing flows — assess what current flows use before restricting, and stage it.

4. Reassignments and connector policies are client-visible and can stop automations — get client approval (send an approval request) with the affected flows and connectors listed. Never disable a flow or change ownership on assumption; a "dead-looking" flow may run monthly.

5. Prepare execution for the tech (verify against current portals): Power Platform admin center (environments, DLP policies, flow ownership) and the Power Automate portal (add co-owners, enable/disable flows). Note that deep flow management may require the client's Power Platform admin rights, not just M365 admin — verify access before promising changes.

6. Verify with evidence: reassigned flows show the new owner and still run (check next run/history); disabled flows are intentionally off; the DLP connector policy shows applied and existing critical flows still function. Document what/why/when/rollback — leave a plain-text note: flows inventoried, orphans reassigned/co-owned or disabled (with the business process each serves), connector policy set, approver, date, and rollback (restore prior owner; re-enable a flow; remove/relax the DLP policy). Log time.

Guardrails: Add a co-owner to a leaver's business-critical flows BEFORE their account is disabled — sequence into offboarding, don't discover it after it breaks. Never disable a flow or reassign ownership on assumption; confirm the process is dead or the new owner is right, with client approval. Connector DLP policies can break existing flows — assess current connector use and stage the rollout per environment. Deep management may need Power Platform admin rights; verify access before promising changes. This is a client's Power Automate, not Thread Flows. Capture prior owners/states as rollback. When in doubt, do nothing and escalate.
```
