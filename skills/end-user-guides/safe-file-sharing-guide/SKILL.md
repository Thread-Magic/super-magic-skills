---
name: Safe File Sharing Guide
description: Draft reply-ready instructions for an end user to share files the approved way — links over attachments, right audience, external-sharing rules.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Safe File Sharing Guide

**When to use:** "User asked how to send a file to a client — send them the right way." / "User keeps emailing spreadsheets as attachments — send the share-a-link guide." / after an oversharing incident, the education reply.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for sharing files the way the client's policy intends —
the approved method, the audience choice that trips everyone up ("anyone with the link" vs
"specific people"), and the external-recipient path. Draft only: show it to me first, send
nothing.

1. Verify the client's sharing platform and policy FIRST, from their documentation and past
   tickets: OneDrive/SharePoint links (the common case) or another sanctioned tool; whether
   sharing outside the company is enabled, restricted or blocked; the default link audience; and
   any banned channels (personal Dropbox/Gmail, consumer transfer sites). If the
   policy is unknown — especially the external question — ask the technician ONE question; a
   guide that contradicts the tenant's settings teaches users the desk doesn't know its own
   systems.
2. Pick the scenario from the ticket — internal colleague, external recipient, too-big-for-email
   — and draft only that branch.
3. Write the block to end-user rules, one action per step with what-you'll-see cues:
   - The core habit as a benefit: "Send a link, not a copy — everyone sees the current version
     and you can un-share later."
   - The share flow on the client's platform: the Share button on the file (cue the dialog), then
     the audience decision made explicit — "the box near the top says who the link works for.
     'People you choose' is the safe default; 'Anyone with the link' means exactly that — anyone
     it gets forwarded to." This explanation appears in every draft.
   - View vs edit in one line: change the file, or just read it? Pick before you send.
   - External branch, ONLY if policy-verified as allowed: type the outside person's email into
     the share dialog rather than making an open link; cue what they'll experience ("an email
     from the system and maybe a code to enter — that's normal"). If external sharing is blocked,
     say so plainly and give the documented alternative.
   - The don'ts: no personal cloud accounts or file-transfer sites for work files, and don't
     make an "anyone" link just because it's fewer clicks.
   - Off-ramps, both in every draft: "If the sharing box won't accept the outside address, stop
     and reply — that's a policy setting, not a mistake you made." / "If you're sharing anything
     sensitive (payroll, health, contracts) and aren't sure, reply first."
4. Assemble per the Email Baseline Standard.

Guardrails: never instruct a workaround for a blocked path — personal accounts, consumer
transfer sites, zipping to evade. If the policy blocks it and the need is real, that's a
tech/admin ticket and the draft says so. This guide never green-lights sharing regulated data;
that call sits above it. No admin steps (tenant sharing settings, DLP, labels) in the user block.
Localizable; version-cautious dialog cues. Docs tools exist only when enabled.
```
