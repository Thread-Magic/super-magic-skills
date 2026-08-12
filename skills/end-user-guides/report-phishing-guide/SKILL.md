---
name: Report Phishing Guide
description: Draft reply-ready instructions telling an end user what to do with a suspicious email — the client's report-button path, never forwarding it around — "tell the user how to report a phish."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Report Phishing Guide

**When to use:** "User asked what to do with a suspicious email — send the reporting steps." / after a phishing verdict, the "here's what to do next time" education reply / proactive broadcast material during a phishing campaign.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for the user staring at a suspicious email: report it
through this client's actual reporting mechanism, don't click anything, don't forward it to
colleagues "to warn them." Verify the mechanism before you write; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's reporting mechanism FIRST by checking the client's documentation and past tickets: the built-in Outlook Report button, a security-vendor
   add-in button (KnowBe4 Phish Alert, Huntress, Proofpoint, etc. — name whichever docs show), or a
   documented report-to mailbox. Check whether the button exists on both desktop and mobile. If no
   mechanism is documented, ask the technician ONE question — telling a user to press a button they
   don't have teaches them to ignore you.
2. Check the urgency branch. If the ticket suggests the user already clicked a link or entered
   credentials, this is NOT an education reply — route to the tech/security incident flow
   immediately; the user-facing message then comes from that flow, not this guide.
3. Write the instruction block to end-user rules, one action per step:
   - Calm frame: "You did the right thing by asking. Here's the safe routine, every time."
   - The don'ts, plainly and first: don't click links, don't open attachments, don't reply, and
     don't forward it to coworkers — forwarding spreads the dangerous link and breaks the technical
     trail we use to trace it. (This never-forward rule is the point of this skill; it appears in
     every draft with the plain reason.)
   - The report path with a what-you'll-see cue ("in the toolbar at the top of the message, look for
     the button named <documented button> — after you press it the email disappears from your inbox;
     that's normal and means it worked").
   - What happens next, honestly, per client docs (or "you won't hear back unless action is needed").
   - The it-might-be-real reassurance: "we'd always rather you report ten real ones than miss one
     fake."
   - Off-ramp: "If you already clicked a link or typed your password anywhere, call the desk right
     now instead of emailing — that changes what we do and minutes matter."
4. Assemble per the Email Baseline Standard, including its defensive-writing rules (no "you were
   hacked" language).

Guardrails: the one documented exception to never-forward: if the client's mechanism IS a report
mailbox, describe the forward-as-attachment routine exactly as their docs specify, and still ban
forwarding to anyone else. Mechanism match is mandatory; don't describe a vendor button the client
doesn't run. This guide never renders a verdict on a specific email — verdicts belong to the
phishing-triage incident flow; if the user attached the suspect email, hand off there first. No
admin steps (quarantine, mail-flow rules, purge) in the user block. Never include the suspicious
link or a defanged copy in the outgoing draft. Localizable — the clicked-already off-ramp must
survive translation with its urgency intact. The client's documentation is available only when those integrations are enabled.
```
