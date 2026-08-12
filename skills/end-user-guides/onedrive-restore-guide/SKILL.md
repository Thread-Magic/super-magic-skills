---
name: OneDrive Restore Guide
description: Draft reply-ready instructions for an end user to recover a deleted file or roll back to a previous version themselves in OneDrive/SharePoint — "send the user steps to restore their file."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# OneDrive Restore Guide

**When to use:** "User deleted a file — send steps to get it back themselves." / "User saved over a document and needs yesterday's version." / empowerment reply teaching a repeat requester to self-serve recovery.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for self-service file recovery — recycle bin for deletions,
version history for overwrites — scoped to where the file actually lived (personal OneDrive vs a
shared/SharePoint library), because the path differs and users rarely know which they're in. Verify
the stack and scenario before you write; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the storage stack and scenario FIRST. Confirm from the ticket and client docs that this client is on
   OneDrive/SharePoint (a client on a file server or another platform gets a different answer — do
   not send this guide). Then pin down: deleted vs overwritten, roughly when, and personal OneDrive
   vs a shared "Documents/Teams" location. If the location is unclear, the draft opens with the one
   distinguishing question ("Was this in your own OneDrive, or in a shared team folder?") and
   includes only the branch you can support.
2. Deleted-file branch, to end-user rules, one action per step with what-you'll-see cues:
   - Go in through the browser, not the desktop folder ("sign in to office.com the same way you do
     for webmail, open OneDrive").
   - Recycle-bin cue for the chosen branch (OneDrive left menu vs SharePoint site's recycle bin),
     sort by delete date, tick the file, Restore — cue: "the file goes back to exactly where it was,
     not to your desktop."
   - Honest time bound: deleted items are recoverable for a limited window (about 93 days on
     Microsoft's current default — phrase as "roughly three months," version-cautiously). If the
     deletion is older, the draft says to reply instead, because recovery moves to the admin side.
3. Overwritten-file branch: right-click the file (browser, or File Explorer with OneDrive) → Version
   history → cue ("a list of dates and times — each is a snapshot") → open the date they want →
   Restore. Reassure that restoring an old version doesn't destroy the current one (it becomes
   another version).
4. Off-ramps in both branches: "If the file isn't in the recycle bin, or version history is empty or
   greyed out, stop and reply with the file name and roughly when it was lost — we have deeper
   recovery options on our side." Never mention or describe the admin-side second-stage recycle bin
   or backup restore in the user draft.
5. Assemble per the Email Baseline Standard.

Guardrails: stack verification is mandatory — recycle-bin steps sent to a file-server client are
dead on arrival (that's a backup-restore request). Never promise recoverability ("it'll definitely
be there") — commit to the steps, not the outcome. If the ticket hints at mass deletion or
ransomware-pattern loss (many files, strange extensions), do NOT send self-service steps — flag to
the tech immediately; user-driven restores can destroy forensic state. Time-window numbers stay
approximate and version-cautious; retention is tenant-configurable. No admin steps in the user block.
Localizable. The client's documentation is available only when those integrations are enabled.
```
