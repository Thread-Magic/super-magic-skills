---
name: Shared Mailbox Access Guide
description: Draft reply-ready instructions for an end user to open a shared mailbox they've been granted — desktop, web, and mobile paths — "tell the user how to open the shared mailbox."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Shared Mailbox Access Guide

**When to use:** Access-request tickets at the fulfillment step ("access granted — send <user> the steps to open it") / "user says they were given access to <mailbox> but can't see it" / role changes where a team mailbox comes with the job.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for the moment after shared-mailbox access is granted: how it
actually shows up, on which device, and how long that takes — because "you now have access" without
the how is just a slower ticket. Verify access state and environment before you write; when unsure,
ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify access state and environment FIRST. From the ticket: has the grant
   actually been completed, and to which mailbox (display name only)? From client docs: which Outlook flavors the user runs and whether the user
   also has send-as/send-on-behalf rights — that changes what you promise. If the grant isn't
   confirmed done, do NOT send this guide; tell the tech the fulfillment step is still open. If the
   flavor is unknown, cover web (works everywhere) plus ONE desktop flavor confirmed from the ticket
   — not all five.
2. Write the matching paths, to end-user rules, one action per step with what-you'll-see cues:
   - The patience preamble (this kills most callbacks): "In desktop Outlook the mailbox usually
     appears by itself in the folder list on the left, under your own folders — but it can take up to
     a few hours after access is granted. If it's not there yet, that's normal."
   - Web path (the immediate-gratification route): sign in to webmail, right-click their own name in
     the folder list, choose add/open shared folder (cue: "a box asks for a name — type <mailbox
     display name> and pick it from the list"), and where it appears.
   - Desktop path: mostly "wait for it to appear, then restart Outlook once if it hasn't" — manual-add
     steps only for the confirmed flavor, version-cautious.
   - Sending as the mailbox (ONLY if the grant includes it): the From-field cue ("when writing an
     email, look for the From button; choose <mailbox display name> so the reply comes from the team
     address, not your own"), and the first-time note that the From button may need enabling from the
     options menu.
   - Off-ramps: "If it hasn't appeared anywhere by tomorrow morning, reply here." / "If you can read
     the mailbox but sending is rejected, stop and reply — that's a separate permission on our side."
3. Assemble per the Email Baseline Standard.

Guardrails: never send this guide before the grant is confirmed complete — instructions for access
that doesn't exist yet manufacture a "your steps don't work" reply. Promise send-as only when the
ticket/grant confirms it; reading and sending are separate permissions and conflating them is the #1
follow-up ticket. The propagation-delay expectation appears in every draft. No admin steps (adding
members, mailbox permissions, automapping) in the user block. Refer to the mailbox by display name
only; no addresses of uninvolved mailboxes, no permission-holder lists. Localizable. Docs tools
exist only when enabled.
```
