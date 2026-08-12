---
name: SSPR Rollout
description: Plan and execute Entra self-service password reset: method choices, registration campaign, hybrid writeback checks, and helpdesk-ticket impact.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# SSPR Rollout

**When to use:** A client asks to "enable self-service password reset for <client>," or "we spend too much helpdesk time on password resets" and SSPR is the proposal, or SSPR is enabled but nobody uses it (a registration problem, not a feature problem), or a hybrid client asks for SSPR with on-prem passwords in play. SSPR is sold on one number — password-reset tickets that stop arriving — and this skill rolls it out so that number actually materializes: methods users will register, a campaign that gets them registered, and a before/after measurement so the client sees the payoff.

**Run it:** on one client's rollout — you prepare the plan, comms, and measurements, a technician executes the Entra configuration (not a Flow: it needs a human at the console).

## Prompt

```
You prepare the SSPR plan, comms, and measurements; the technician executes the Entra configuration. Never invent data — state search windows and date every point-in-time figure. Registration status numbers are point-in-time; date them.

1. Baseline the ticket load FIRST. Search the ticket history for password-reset volume for this client over the last 60-90 days (state the search window and note if results may be capped). This is the before-number; without it the rollout can never prove its value, and you must not promise ticket-volume reductions without it.

2. Check the plumbing. Cloud-only: straightforward. Hybrid (synced from AD): SSPR needs password writeback via Entra Connect and the appropriate licensing (Entra ID P1 or M365 Business Premium for writeback) — without writeback, cloud resets diverge from on-prem passwords, which is worse than no SSPR and a trust-destroying failure mode. Verify licensing and Entra Connect health before promising anything (verify current licensing requirements). State which case applies in the plan. Pull the client's documented tenant details from the client's documentation if connected; degrade gracefully if not.

3. Choose methods deliberately. Require two methods for reset. Prefer Microsoft Authenticator (app notification/code) plus a secondary; avoid security questions (weak, guessable) unless the client insists in writing — they are a documented-client-decision method, not a default. Align with the tenant's MFA registration via combined registration so users register once for both MFA and SSPR — check the mfa-methods-audit skill's findings if one exists for this tenant; phone-only populations affect the method choice.

4. Pilot, then broaden. Enable SSPR for a pilot group; pilot users register and perform a real reset end-to-end (including on-prem sync for hybrid). Only then broaden. Note: admin accounts always have SSPR enforced by Microsoft with two-method requirements — do not count them as pilot evidence for the user experience.

5. Run the registration campaign — THIS is the rollout. Enablement without registration produces nothing. Prepare user comms (what's changing, why, how to register, how long it takes), use registration campaign/nudge features where licensed, and report registration coverage weekly until it plateaus. Expect a temporary bump in tickets about registration itself — tell the client this up front so week one doesn't read as failure.

6. Approval and comms gate. Before broad enablement: send an approval request to the client contact with methods chosen, the registration requirement users will see at next sign-in, the campaign plan, and rollback (disable SSPR scope; registered methods persist harmlessly).

7. Measure and close the loop. At 30/60 days post-rollout: registration coverage, SSPR usage count, and password-ticket volume vs the baseline from step 1. Post the comparison (leave a plain-text note, dated, windows stated, result-cap honesty) — this is the deliverable the client was actually buying. Helpdesk verification discipline still applies: SSPR reduces reset tickets; it does not change the identity-verification ladder for the resets that still reach a human (see password-and-mfa-recovery). Schedule the measurement follow-up at rollout time so it happens. Log time.

When in doubt about writeback health or authorization, do nothing and escalate.
```
