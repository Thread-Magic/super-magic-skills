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
Draft a client-ready expectations-and-first-steps block for a machine handoff. Most "my new
computer is broken" tickets are unmanaged expectations — apps still installing, files still
syncing — so front-load what normal looks like. Draft only: show it first, send nothing.

1. Verify the client's deployment model FIRST, from their documentation and past tickets:
   zero-touch self-setup (the user signs in and the machine builds itself, Autopilot-style),
   tech-prepared handoff (mostly ready, user personalizes), or manual setup with a tech session
   booked. Also confirm how files move (cloud sync vs a tech-run transfer), whether the old
   machine stays with the user meanwhile, and the platform. If the model is unknown, ask the tech
   ONE question — the match is mandatory; a zero-touch guide handed to a manual-setup
   user strands them at a sign-in screen.
2. Write the matching guide to end-user rules, in labeled parts:
   - What to expect, the expectations vaccine: first sign-in uses their normal work login and
     the MFA prompt on their phone (keep it handy); apps install themselves over the first hours,
     so the machine may feel busy or restart; files reappear via sync gradually, newest first,
     and some icons show cloud marks before they are fully local. One honest time frame from the
     documentation ("most people are fully set up within <documented window>") — never invent
     one.
   - What to do, in order, one action per step with what-you'll-see cues: connect to wifi, sign
     in, approve MFA, sign in to the browser once so favorites and passwords sync, sign in to the
     password-manager extension if the client runs one, send a test email, print a test page if
     they print.
   - What NOT to do: don't install software from the web "to save time" — reply and ask instead;
     don't copy files with a personal USB drive or personal cloud; don't wipe, return or hand off
     the OLD machine until the desk confirms everything moved ("keep it powered off in a drawer
     until we say so"), always included, a premature wipe being the one unrecoverable failure in a
     refresh; don't ignore restart prompts on day one.
   - Off-ramps: "If sign-in fails, or a daily app hasn't appeared by <documented window>, stop
     and reply — include the app name." / "If anything asks for an admin name and password, stop
     and reply; you should never need one."
3. Name their line-of-business apps from prior tickets, so "is everything here?" is a concrete
   checklist rather than a vibe.
4. Assemble per the Email Baseline Standard.

Guardrails: don't promise every app returns automatically unless the documentation says so —
line-of-business apps often need a tech touch; list known exceptions honestly. No admin steps
(enrollment consoles, imaging, local-admin credentials) in the user block. Localizable. Docs tools
exist only when enabled.
```
