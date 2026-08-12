---
name: Printer Connect Guide
description: Draft reply-ready instructions for an end user to add or reconnect the office printer, matched to the client's actual print setup — "send the user steps to add the printer."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Printer Connect Guide

**When to use:** "Send <user> steps to add the printer near them." / new desk / moved desk / new machine tickets where the printer didn't follow / "user can't find the printer in their list."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for adding the office printer — written for how THIS client
delivers printers, because "add a printer" means something different in each setup. Verify the
delivery model before you write; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's print delivery model FIRST by checking the client's documentation and past tickets: (a) printers auto-deploy to managed machines, (b) users
   add from a print server, (c) a cloud print platform with its own client/portal (Universal
   Print/Printix/PaperCut), or (d) small-office direct/wifi printers. Also pull the printer's
   documented friendly name for the user's location. If the model or printer name is unknown, ask
   the technician ONE question.
2. Write ONLY the matching branch, to end-user rules, one action per step with what-you'll-see cues:
   - Auto-deploy: keep it short — where printers appear (Settings → the printers list, phrased
     version-cautiously), "give it a few minutes after sign-in on the office network," and the
     off-ramp. Do not include manual-add steps that fight the deployment.
   - Print server: open the add-printer search, pick the documented printer by its exact friendly
     name ("choose the one called exactly <documented name> — names matter here"), wait for the
     driver cue ("your computer sets it up by itself; a test-page option appears when done"). Don't
     expose raw server paths unless docs show users add by path at this client.
   - Cloud print platform: the platform's user-side flow only (its portal/app, sign in with work
     credentials, select the printer for their floor), per docs.
   - Direct/wifi: must be on the office network first; add from the printers list; cue the name/model
     match.
   - Universal off-ramps: "If the printer isn't in the list, stop and reply with where you sit —
     we'll map it from our side." / "If you're asked for a driver, a file, or an admin password,
     stop and reply — you should never need those."
3. Include the success test: print a test page (where the flow offers it) or a one-page print, and
   what to do if it queues forever ("if it says 'printing' for more than a couple of minutes with
   nothing coming out, reply — don't print it five more times").
4. Assemble per the Email Baseline Standard.

Guardrails: never invent a printer name, share path, or IP address — docs or ask; a user adding a
guessed printer prints to the wrong floor for a month. Delivery-model match is mandatory —
manual-add steps on an auto-deploy client create duplicate broken queues. The don't-print-it-again
line stays in every draft. No admin steps (driver installs, server queue management, deployment
policy) in the user block. Localizable; Windows/Mac cue differences only if the client has both per
docs. The client's documentation is available only when those integrations are enabled.
```
