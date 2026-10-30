---
name: Alert Title Standardizer
description: Rewrite a security or monitoring alert ticket title into one standard shape of tool, company, alert and asset, so the board sorts, searches and bundles cleanly.
category: Triage & Routing
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Security & Compliance Owner]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Alert Title Standardizer

**When to use:** Alert emails arrive with titles like "[EXTERNAL] FW: Alert: Notification - New suspicious threat detected on JKS-DT07", each vendor in its own format. Analysts cannot scan the board, and bundling skills that match on the title miss half the duplicates.

**Run it:** on one ticket · or as a Flow (when a ticket is created on your security or monitoring board). Run it before any bundling or duplicate skill, since those match on the title.

## Prompt

```
Rename this alert ticket to the standard format: <Tool> - <Company> - <Alert> - <Asset>

1. Read the current title and the first message.

2. Identify the four parts:
- Tool: the product that raised the alert (for example SentinelOne, Blackpoint, Microsoft Defender, Sophos Central, Huntress, an RMM). Use the clean product name; strip brackets, "FW:", "[EXTERNAL]" and other mail artifacts.
- Company: the ticket's client name as it appears in the PSA, in full, unless a short form is part of the client's own branding.
- Alert: the core event ("New suspicious threat detected", "Agent disabled", "Suspicious sign-in", "Encryption suspended"). Drop filler like "Alert:" or "Notification:".
- Asset: the specific machine, user, mailbox, policy or device ID involved. If none is identifiable, leave this part out.

3. Build the title: "<Tool> - <Company> - <Alert> - <Asset>", or "<Tool> - <Company> - <Alert>" with no asset.

4. If the ticket is still on your catch-all company, use "Unknown client" for Company and say so in the note; never guess a client from the asset name.

5. If the title already matches the format, change nothing and stop.

6. Update the title, then add an internal note: "Title standardized. Old: <old>. New: <new>."

Never change anything but the title. Never invent an asset or a company. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the note, or nothing when no change was needed.
```
