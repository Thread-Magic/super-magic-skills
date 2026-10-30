---
name: AI Request Risk Tiering
description: Score a client request involving AI tools, Copilot, new LLMs or MCP servers as low, moderate or high risk, then add the matching notes and send security approval or escalate before anyone does the work.
category: Security
tools: [search_tickets, search_contacts, send_approval, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Security & Compliance Owner, Service & Ops Manager]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# AI Request Risk Tiering

**When to use:** Clients now ask for Copilot licenses, ChatGPT access, browser AI extensions and MCP servers wired into their apps. Some are a license toggle; some quietly grant an AI write access nobody had before. You want every AI request tiered before work starts, with client sign-off where the risk is real.

**Run it:** on one ticket · or as a Flow (when a ticket is categorized as an AI request, or its title or body mentions AI, Copilot, an LLM or an MCP server). Replace the team and contact-type names with yours.

## Prompt

```
Assign this AI-related request a risk level from 1 to 3 and act on it. Read the title and the full thread.

RISK 3, high (any match): access to a new or unvetted AI service or LLM; installing an unknown or unvetted MCP server or AI extension; giving anyone (or an AI) write access they do not have today; changing a company-wide setting or data-sharing policy.
RISK 2, moderate: connecting an MCP server or AI integration between apps the user already uses, with no new access; an AI writing only where the user can already write.
RISK 1, low: assigning an AI license such as Copilot, AI troubleshooting, enabling a standard AI feature with no security or access change.
When signals span levels, take the highest. Not actually AI-related: make no changes and stop.

RISK 1: add a client-visible note: "This is a Risk Level 1 request. Please confirm it does not change security settings, data privacy, or who has write access."

RISK 2:
1. Add a client-visible note: "This is a Risk Level 2 request and needs security approval from your organization before we proceed."
2. Find this client's contacts with your security-approver contact type. Send them an approval that states the request, who asked, and the risk: "<requester> asked us to <short summary>. This creates <risk identified>. Please confirm you understand and accept this risk." None found: add an internal note that no approver is on file and stop.
3. Do not start the work until it is approved.

RISK 3:
1. Add an internal note: "High-risk AI request. Do not proceed. Needs review by <your AI or security consulting team>."
2. Add a client-visible note: "We have escalated this request to our <AI consulting> team to make sure the risk and the work are properly managed."
3. Move the ticket to <that team>.

Always add an internal note with the level, the specific signal that set it, and the action taken. Never approve a request yourself. Never invent approvers. Notes are plain text, no markdown or emojis.

As a Flow: act as above; your entire reply is the internal note.
```
