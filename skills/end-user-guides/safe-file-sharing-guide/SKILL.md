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
Draft a client-ready instruction block for sharing files the way the client's policy intends — the
approved method, the audience choice that trips everyone up ("anyone with the link" vs "specific
people"), and the external-recipient path, verified against what the tenant actually allows. Verify
the platform and policy before you write; when unsure — especially about external sharing — ask.
Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's sharing platform and policy FIRST by checking the client's documentation and past tickets: OneDrive/SharePoint links (the common case) or another
   sanctioned tool; whether sharing to people outside the company is enabled, blocked, or restricted;
   the client's default link audience; and any documented banned channels (personal Dropbox/Gmail,
   consumer transfer sites). If the policy is unknown — especially the external question — ask the
   technician ONE question; telling a user to "just share externally" against a blocking policy
   produces a confusing error, and describing a looser policy than reality is worse.
2. Determine the scenario from the ticket (internal colleague, external recipient, or too-big-for-
   email) and draft only the branch that applies.
3. Write the instruction block to end-user rules, one action per step with what-you'll-see cues:
   - The core habit, framed as a benefit not a rule: "Send a link, not a copy — everyone sees the
     current version, you can un-share later, and no mailbox fills up."
   - The share flow on the client's platform: the Share button on the file (cue the dialog), then the
     audience decision made explicit — "the box near the top says who the link works for; click it and
     choose. 'People you choose' is the safe default; 'Anyone with the link' means exactly that —
     anyone it gets forwarded to."
   - View vs edit in one plain line ("can they change the file, or just read it? Pick before you
     send").
   - External branch (ONLY if policy-verified as allowed): type the outside person's email in the
     share dialog rather than making an open link; cue what the recipient experiences ("an email from
     the system and maybe a code to enter — that's normal, it proves they're them"). If external
     sharing is blocked, say so plainly and give the documented alternative — never a workaround.
   - The don'ts, brief: no personal cloud accounts or file-transfer sites for work files, and don't
     make an "anyone" link just because it's fewer clicks.
   - Off-ramps: "If the sharing box won't accept the outside address, stop and reply — that's a policy
     setting, not a mistake you made." / "If you're sharing anything sensitive (payroll, health,
     contracts) and aren't sure, reply first — thirty seconds of asking beats un-sharing later."
4. Assemble per the Email Baseline Standard.

Guardrails: policy verification before drafting is the skill — the external-sharing capability differs
per tenant; a guide that contradicts the tenant's settings teaches users the desk doesn't know its own
systems. Never instruct a workaround for a blocked path (personal accounts, consumer transfer sites,
zipping-to-evade) — if the policy blocks it and the need is real, that's a tech/admin ticket, and the
draft says so. The audience-setting explanation appears in every draft. Sensitive-data hesitation
off-ramp stays in; this guide never green-lights sharing regulated data — that's a policy/compliance
call above its pay grade. No admin steps (tenant sharing settings, DLP, sensitivity labels) in the
user block. Localizable; version-cautious dialog cues. The client's documentation is available only when those integrations are enabled.
```
