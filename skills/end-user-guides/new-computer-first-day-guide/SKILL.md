---
name: New Computer First Day Guide
description: Draft reply-ready instructions for an end user receiving a new or replacement computer — what to expect, what to do first, and what NOT to do.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# New Computer First Day Guide

**When to use:** "User is getting their replacement laptop tomorrow — send a what-to-expect guide." / hardware-refresh projects: the standard note that ships with every device / "user says half their apps are missing on the new machine."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready expectations-and-first-steps block for a machine handoff. Most "my new computer
is broken" tickets are really unmanaged expectations — apps still installing, files still syncing —
so front-load what normal looks like. Verify the deployment model before you write; when unsure, ask.
Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's deployment model FIRST by checking the client's documentation and past tickets: zero-touch/self-setup (user signs in and the machine builds itself — e.g.,
   Autopilot-style), tech-prepared handoff (mostly ready, user personalizes), or manual setup with a
   tech session booked. Also confirm: how files move (cloud sync like OneDrive vs a tech-run
   transfer), whether the old machine stays with the user during transition, and platform
   (Windows/Mac). If the model is unknown, ask the technician ONE question — a zero-touch guide handed
   to a manual-setup user strands them at a sign-in screen.
2. Write the matching guide to end-user rules, in three labeled parts:
   - What to expect (the expectations vaccine): first sign-in uses their normal work login plus the
     MFA prompt on their phone (keep the phone handy); apps install themselves over the first hours —
     the machine may feel busy or restart; files reappear via sync gradually, newest first; some
     icons show placeholder/cloud marks before files are fully local. One honest time frame per docs
     ("most people are fully set up within <documented window>").
   - What to do, in order, one action per step with what-you'll-see cues: connect to wifi (office or
     home), sign in, approve MFA, open the browser and sign in once so favorites/passwords sync, sign
     in to the password-manager extension if the client runs one, send one test email, print one test
     page if they print.
   - What NOT to do: don't install software from the web "to save time" — reply and ask instead;
     don't copy files with a personal USB drive or personal cloud; don't wipe, return, or hand off the
     OLD machine until the desk confirms everything moved ("keep it powered off in a drawer until we
     say so"); don't ignore restart prompts on day one.
   - Off-ramps: "If sign-in fails, or an app you use daily hasn't appeared by <documented window>,
     stop and reply — include the app name." / "If anything asks for an admin name and password, stop
     and reply; you should never need one."
3. Tailor the daily-driver checklist from the ticket where possible (their known LOB apps from prior
   tickets) so "is everything here?" is a concrete list, not a vibe.
4. Assemble per the Email Baseline Standard.

Guardrails: deployment-model match is mandatory — never describe an auto-building machine to a client
whose techs image manually. The keep-the-old-machine rule appears in every draft — premature wipe of
the old device is the one unrecoverable failure in a refresh. Time frames come from client docs or the
ticket; never invent an SLA. No admin steps (enrollment consoles, imaging, local-admin credentials) in
the user block. Don't promise every app returns automatically unless the docs say so — LOB apps often
need a tech touch; list known exceptions honestly. Localizable. The client's documentation is available only when those integrations are enabled.
```
