---
name: OneDrive Known Folder Move
description: Work OneDrive Known Folder Move rollout tickets — missing Desktop, sync conflicts, path-length and invalid-character legacy files — without unhooking KFM.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# OneDrive Known Folder Move

**When to use:** "My desktop files disappeared" / "my documents are gone" right after a KFM rollout hits a machine; OneDrive stuck on specific files with path/character/size errors since folders moved; duplicate folders ("Desktop" and "Desktop on <device>", conflict copies) after KFM applied on multiple machines; or a user/tech asking to turn KFM off on one machine because it's "causing problems." For general sync-client failures unrelated to KFM, use the OneDrive & SharePoint Sync playbook.

**Run it:** on the one ticket you're working — a tech works it with the user and escalates rollout gaps to the deployment owner; not unattended.

## Prompt

```
Known Folder Move redirects Desktop, Documents and Pictures into OneDrive. Its tickets are
mostly perception — "my files are gone" when they moved — plus a tail of legacy-file
friction. The forbidden fix is unhooking KFM on one machine to close a ticket: that forks
the user's files into two realities.

Climb the Troubleshooting Ladder base skill first: past tickets since the rollout date,
where clustering separates one machine's friction from a wave-wide comms failure; the
documented rollout plan (which folders redirect, silent versus prompted, schedule,
exclusions); the OneDrive client version, because old clients cause already-solved
problems; and this machine's KFM state, since half the confusion is machines mid-wave.
Evidence is OneDrive's own error list, which names each failing file and why, plus
OneDrive on the web for anything "missing".

1. "Where did my files go" — the folder moved, the user's mental map didn't. Show them
   Desktop and Documents under OneDrive and prove it with the web view. In bulk this is a
   comms gap: escalate to the rollout owner, since one paragraph to the wave prevents the
   rest. If the file is not in OneDrive web, not local, not in the recycle bin, stop
   reassuring — work the site recycle-bin tiers and restore options, and escalate as
   potential data loss rather than guessing.

2. Path length, invalid names, size — the client flags exactly what it cannot upload. This
   is legacy-file hygiene: work the error list item by item until it is zero. Hundreds of
   items, or deep structures from an old file-server migration, is a cleanup task to
   schedule rather than a live-call fix — escalate it.

3. Conflicts and duplicates — "Desktop on <device>" folders and conflict copies mean both
   versions were preserved and nothing was chosen for the user. Explain that, then help
   them merge. Never pick which version wins or delete a copy: the user decides, and where
   business-critical files diverged, their manager or the owner arbitrates.

4. KFM won't apply — usually an old client, a known folder holding something unmovable, or
   a legacy folder-redirection GPO fighting KFM. That collision belongs to the deployment
   owner, per Microsoft's documented migration path. Escalate with the specific error;
   per-machine hacks make the fleet inconsistent.

5. "Just turn it off for this machine" — refuse. Unhooking KFM while fleet policy expects
   it forks the user's files and recreates the unprotected-Desktop problem KFM exists to
   solve. A genuine incompatibility goes to the rollout owner as a documented policy
   exclusion.

Close when the icon is green with no failing items and the user finds their files
themselves — that proves the mental map is fixed, not just the sync. Note it (apply the
PSA Note Discipline base skill): KFM state, branch, evidence, what remains for the rollout
owner.
```
