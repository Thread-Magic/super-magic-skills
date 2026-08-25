---
name: OneDrive Restore Guide
description: Draft reply-ready instructions for an end user to recover a deleted file or roll back a previous version themselves in OneDrive or SharePoint.
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
shared SharePoint library), because the path differs and users rarely know which they're in. Draft
only: show it to me first, send nothing.

1. Verify the storage stack and scenario FIRST. Confirm from the ticket and the client's
   documentation that this client is on OneDrive/SharePoint; a client on a file server or another
   platform gets a different answer — do not send this guide, that's a backup-restore request.
   Then pin down: deleted vs overwritten, roughly when, and personal OneDrive vs a shared
   "Documents/Teams" location. If the location is unclear, open the draft with the one
   distinguishing question ("Was this in your own OneDrive, or in a shared team folder?") and
   include only the branch you can support.
2. Deleted-file branch, to end-user rules, one action per step with what-you'll-see cues:
   - Go in through the browser, not the desktop folder: "sign in to office.com the same way you do
     for webmail, then open OneDrive."
   - The recycle-bin cue for the chosen branch (OneDrive's left menu vs the SharePoint site's
     recycle bin), sort by delete date, tick the file, Restore — cue: "the file goes back to
     exactly where it was, not to your desktop."
   - The honest time bound: deleted items are recoverable for a limited window — about 93 days on
     Microsoft's current default, phrased version-cautiously as "roughly three months." If the
     deletion is older, the draft says to reply instead, because recovery moves to the admin side.
3. Overwritten-file branch: right-click the file (in the browser, or in File Explorer with
   OneDrive) → Version history → cue ("a list of dates and times — each is a snapshot") → open the
   date they want → Restore. Reassure them that restoring an old version doesn't destroy the
   current one; it becomes another version.
4. Off-ramps in both branches: "If the file isn't in the recycle bin, or version history is empty
   or greyed out, stop and reply with the file name and roughly when it was lost — we have deeper
   recovery options on our side." Never mention or describe the admin-side second-stage recycle bin
   or a backup restore in the user draft.
5. Assemble per the Email Baseline Standard.

Guardrails: never promise recoverability ("it'll definitely be there") — commit to the steps, not
the outcome. If the ticket hints at mass deletion or a ransomware pattern (many files, strange
extensions), do NOT send self-service steps — flag it to the tech immediately; user-driven restores
can destroy forensic state. Retention is tenant-configurable, so keep time-window numbers
approximate. No admin steps in the user block. Localizable. Docs tools exist only when enabled.
```
