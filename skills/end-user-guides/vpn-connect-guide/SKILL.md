---
name: VPN Connect Guide
description: Draft reply-ready instructions for an end user to connect to their company VPN using the client's actual VPN software — "send the user steps to get on the VPN."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# VPN Connect Guide

**When to use:** "Send <user> instructions to connect to the VPN." / remote-work or first-day-remote tickets / "user says the VPN 'isn't working' — send the correct connect steps first."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for connecting to the VPN — written for the specific VPN
client this customer runs (GlobalProtect, FortiClient, Cisco Secure Client/AnyConnect, SonicWall
NetExtender, WatchGuard, OpenVPN, Meraki, or another). There is no generic VPN guide; software name
and connect flow differ everywhere. Verify the software and portal before you write; when unsure,
ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's VPN software and portal FIRST. Search client docs and prior VPN tickets: the client name,
   whether it's pre-installed on managed machines (usual) or user-installed, the portal/server name
   the user selects (from docs only — NEVER invent or guess a hostname), and the sign-in style (work
   credentials + MFA, or certificate/always-on where the user does nothing). If any are unknown, ask
   the technician ONE question before drafting.
2. If docs show the VPN is always-on or auto-connecting, keep the draft short: how to check it's
   connected (icon state cue) and the off-ramp — do not send a manual connect procedure for a VPN
   the user should never touch.
3. Write the connect flow for the identified product, to end-user rules, one action per step:
   - Find the app: name it exactly, describe the icon and where it lives (system tray / menu bar).
   - What-you'll-see cues: the disconnected icon, what the sign-in window asks for, the expected MFA
     prompt, and what "connected" looks like (icon change, status word).
   - The success test: one plain check that proves they're on ("open <the documented internal
     resource cue> — if it loads, you're connected"), using only a check the client's docs support;
     otherwise use the icon state alone.
   - Off-ramps: "If the app isn't in the list at all, stop and reply — we'll install it." / "If
     sign-in fails twice, stop — don't keep retrying — and reply with a photo of the message."
   - Home-network reality note: "Hotel and café wifi sometimes blocks VPNs — if it works at home but
     not on public wifi, that's the network, not your account."
4. Assemble per the Email Baseline Standard.

Guardrails: never invent a portal address, server name, or profile name — docs or ask are the only
two sources; a guessed hostname is worse than no guide. Product match mandatory. No admin-side or
firewall-side steps, no reinstall/adapter/profile edits in the user block — those are tech actions.
Never include shared secrets, pre-shared keys, or certificate files. Repeated failed sign-ins can
lock the account — the stop-after-two off-ramp stays in every draft. Localizable; version-cautious
UI cues. The client's documentation is available only when those integrations are enabled; otherwise rely on the knowledge base and ticket history.
```
