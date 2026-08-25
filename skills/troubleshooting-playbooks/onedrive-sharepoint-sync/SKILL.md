---
name: OneDrive / SharePoint Sync
description: Diagnose OneDrive and SharePoint sync — stuck processing changes, missing files, red X icons — separating client state, library limits, and permissions.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# OneDrive / SharePoint Sync

**When to use:** "OneDrive is stuck on processing changes" / red X or paused icon; "files I saved aren't showing up for a user or the team"; sync errors naming specific files or paths; or "a whole library stopped syncing after a reorganization."

**Run it:** on the one ticket you're working — a tech works it with the user; not unattended.

## Prompt

```
You are diagnosing a OneDrive / SharePoint sync problem. Most are misdiagnosed permissions or
library-limit problems, and most resets are unnecessary.

Climb the Troubleshooting Ladder base skill first: this user's past tickets and this library
(the same library failing for several users is server-side, one user only is client-side), then
the client's documentation for the file architecture — which libraries sync versus use shortcuts
or on-demand, known-large libraries, Known Folder Move policy. Get the OneDrive client version
and install type; old clients cause already-fixed failures. Then read the state: the icon, the
activity center's error list with exact file names and error text, and whether the account shown
is the right one. "It's not syncing" must become a specific error or a specific stuck state.

Then branch:

1. Client state — paused, signed out, throttled ("processing a large number of changes"), or
   crashed. Resume or re-sign-in; for a stuck-but-healthy client, close and restart OneDrive.
   That is the first move, not a reset. Stuck on one file makes that file the suspect; go to branch 2.

2. Library limits and item hygiene — errors naming specific items. Check path length, invalid
   characters, file size cap, and total item count in the synced scope; very large libraries
   degrade and belong on shortcut or on-demand patterns rather than full sync. Restructuring is
   a design fix, not a toggle: propose the architecture conversation, don't band-aid per user.
   Verify limits on the web; never invent one.

3. Permissions versus conflicts — "files are missing" is nearly always one of these and they
   look identical. Can they see the file in the browser? No means an access problem (pair with
   the file-share permissions playbook). Yes but not locally means a true sync issue. Conflict-copy
   files mean two people editing offline: the fix is co-authoring in supported formats.

4. Reset — unlink and relink ONLY when client state is corrupt (repeated crashes, phantom errors
   on files that don't exist), stuck over 24 hours after a restart with no named-file errors, or
   Microsoft's guidance for that error says reset. First confirm the error list shows no unsynced
   local-only changes, and have the user copy recently changed files aside. Reset re-downloads
   state and unsynced work is at risk — say that plainly.

Never tell a user to delete local folders to "clean up" sync; that deletion propagates. Any
destructive-looking step gets an explicit are-all-changes-uploaded check first. If it is a
Microsoft service incident, say only Microsoft can act and reference the incident.

Verify with a test file in both directions. Then leave a plain-text internal note (apply the PSA
Note Discipline base skill): state observed, branch, action, reset yes or no and why,
verification, and anything you couldn't check.
```
