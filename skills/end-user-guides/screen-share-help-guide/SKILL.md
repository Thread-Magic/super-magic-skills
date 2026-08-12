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
Draft a client-ready instruction block for a user who needs to let a technician see or control their
screen for support, written for the specific remote-support tool this client uses — join flows differ
completely between tools, and the user is often already frustrated. Verify the tool before you write;
when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's remote-support tool FIRST by checking the client's documentation and past tickets: the RMM's remote tool (ConnectWise ScreenConnect/Control,
   NinjaOne remote, Datto RMM, etc.), a standalone tool (TeamViewer, AnyDesk, Zoho Assist), or a
   built-in (Quick Assist on Windows, Teams screen share). The experience differs — a code to read
   out, a link to click, an agent already installed that just needs approval, or a share button in a
   meeting. Note whether an unattended agent is already present (often the user just approves a
   prompt). If the tool is unknown, ask the technician ONE question.
2. Confirm the session model from the ticket: is the tech sending a link/code live, or does the user
   initiate? Draft the branch that matches so the steps line up with what the tech is doing.
3. Write the instruction block to end-user rules, one action per step with what-you'll-see cues:
   - Calm framing first: "This lets me see your screen so I can fix it faster — you stay in control
     and can end it anytime."
   - The join path for the identified tool: click the link the tech sends / go to the documented
     short URL and type the code the tech reads you / find the already-installed helper icon and
     approve the prompt. Cue exactly what appears ("a small window will ask to allow the connection —
     click Allow").
   - The consent/control cues: what the "give control" or "allow" prompt looks like, that a session
     banner shows while connected, and how to end it (the big Stop/End button) at any time.
   - Privacy note: close anything private first, since the tech sees the whole screen.
   - Off-ramp: "If nothing happens after you click, or you don't see the prompt, stop and reply or
     stay on the phone with me — don't download anything a pop-up suggests."
4. Assemble per the Email Baseline Standard.

Guardrails: anti-scam framing is mandatory — remote-support tools are a classic scam vector; the
draft tells the user to only ever start a session the desk itself requested, and never enter a code
given by an unexpected caller or download a remote tool from a link a pop-up/unknown caller provided.
Tool match matters. Do not fabricate a live session code or connect URL — the tech supplies the real
one; the guide describes where it goes. The "you can end it anytime / you stay in control"
reassurance appears in every draft. No admin steps (deploying the agent, unattended-access config,
RMM policy) in the user block — and note the agent cannot run scripts or push software via RMM; this
is purely the user-facing join. Localizable; version-cautious UI cues. Docs tools exist only when
enabled.
```
