---
name: Screen Share Help Guide
description: Draft reply-ready instructions for an end user to start a remote-support screen share with the desk using the client's actual remote tool.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Screen Share Help Guide

**When to use:** "Send the user how to start a screen share so I can help them." / "User agreed to a remote session — send the join steps." / "I need to see the user's screen — send them the connect link/code steps."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for a user who needs to let a technician see or control
their screen, written for the specific remote-support tool this client uses — join flows differ
completely between tools, and the user is often already frustrated. Draft only: show it to me
first, send nothing.

1. Identify the client's remote-support tool FIRST, from their documentation and past tickets: the
   RMM's remote tool (ConnectWise ScreenConnect/Control, NinjaOne remote, Datto RMM), a standalone
   tool (TeamViewer, AnyDesk, Zoho Assist), or a built-in (Quick Assist on Windows, Teams screen
   share). The experience differs — a code to read out, a link to click, an agent already installed
   that just needs approval, or a share button in a meeting. Note whether an unattended agent is
   already present, in which case the user often just approves a prompt. If the tool is unknown,
   ask the technician ONE question.
2. Confirm the session model from the ticket: is the tech sending a link or code live, or does the
   user initiate? Draft the branch that matches what the tech is doing.
3. Write the instruction block to end-user rules, one action per step with what-you'll-see cues:
   - Calm framing first: "This lets me see your screen so I can fix it faster — you stay in control
     and can end it anytime." That reassurance appears in every draft.
   - The join path for the identified tool: click the link the tech sends, or go to the documented
     short URL and type the code the tech reads you, or find the already-installed helper icon and
     approve the prompt. Cue exactly what appears: "a small window will ask to allow the connection
     — click Allow."
   - The consent and control cues: what the "give control" or "allow" prompt looks like, that a
     session banner shows while connected, and how to end it (the big Stop or End button) at any
     time.
   - Anti-scam framing, mandatory: only ever start a session the desk itself requested; never enter
     a code given by an unexpected caller, and never download a remote tool from a link a pop-up or
     unknown caller provided. Remote-support tools are a classic scam vector.
   - Privacy note: close anything private first, since the tech sees the whole screen.
   - Off-ramp: "If nothing happens after you click, or you don't see the prompt, stop and reply or
     stay on the phone with me — don't download anything a pop-up suggests."
4. Assemble per the Email Baseline Standard.

Guardrails: do not fabricate a live session code or connect URL — the tech supplies the real one;
the guide only describes where it goes. No admin steps (deploying the agent, unattended-access
config, RMM policy) in the user block; this is purely the user-facing join, and the agent cannot
run scripts or push software from here. Localizable; version-cautious interface cues. Docs tools
exist only when enabled.
```
