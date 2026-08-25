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
You prepare the SSPR plan, comms and measurements; the technician executes the Entra
configuration. Never invent data: state search windows and date every point-in-time figure,
registration coverage included.

1. Baseline the ticket load FIRST. Search this client's ticket history for password-reset
   volume over the last 60 to 90 days, stating the window (Sweep Honesty base skill: say "at
   least N" if results may be capped). Without this before-number the rollout can never
   prove its value; never promise a ticket-volume reduction until you have it.

2. Check the plumbing. Cloud-only is simple. Hybrid (synced from AD) needs password
   writeback via Entra Connect plus its licensing — Entra ID P1 or M365 Business Premium.
   Without writeback a cloud reset diverges from the on-prem password, which is worse than
   no SSPR. Verify licensing and Entra Connect health before promising anything; state
   which case applies. Documented tenant details are in the client's documentation; continue
   without them (Connector Degradation base skill).

3. Choose methods deliberately. Require two methods for a reset. Prefer Microsoft
   Authenticator plus a secondary. Avoid security questions — weak and guessable, a
   documented client decision in writing, never a default. Use combined registration so users
   register once for MFA and SSPR, and check any mfa-methods-audit findings: a
   phone-only population changes the method choice.

4. Pilot first. Enable SSPR for a pilot group, have them register and perform a real
   end-to-end reset (including on-prem sync for hybrid), then broaden. Microsoft already
   enforces SSPR with two methods on admin accounts, so they are not evidence of the ordinary
   user experience.

5. Run the registration campaign — this is the rollout; enablement without registration
   produces nothing. Prepare user comms (what changes, why, how to register), use
   registration campaign or nudge features if licensed, and report coverage weekly until
   it plateaus. Warn the client to expect a temporary bump in registration tickets, so week
   one doesn't read as failure.

6. Approval gate before broad enablement. Send an approval request to the client contact
   with the methods chosen, the registration prompt at next sign-in, the campaign plan, and
   rollback (disable the SSPR scope; registered methods persist harmlessly).

7. Close the loop at 30 and 60 days: registration coverage, SSPR usage, and password-ticket
   volume against the step 1 baseline. Schedule that follow-up at rollout time,
   and post the comparison in a dated plain-text note (PSA Note Discipline base skill). SSPR
   reduces reset tickets; it does not change the identity-verification ladder for the resets
   that still reach a human (see password-and-mfa-recovery). Log time.

When in doubt about writeback health or authorization, do nothing and escalate.
```
