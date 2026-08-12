---
name: LOB Database Locks
description: Clear "record is locked by another user" and stuck-session tickets in line-of-business apps — identify the locking session through the app's own admin tooling and release it by the vendor-approved method only; never kill database sessions ad hoc.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# LOB Database Locks

**When to use:** "Record locked by another user" and that user is gone, at lunch, or "definitely not in it"; the whole LOB app says a batch/period/module is locked and nobody can work; a stuck login where the user crashed out but the app still counts them as signed in (sometimes eating a license); or repeat lock tickets on the same app where the pattern, not just today's lock, is the problem.

**Run it:** on the one ticket you're working — a tech drives this with the app admin and the vendor; not unattended.

## Prompt

```
You are clearing an LOB database-lock ticket. Someone opened a record, went to lunch, and now billing can't post. This is a race between the fast wrong fix (kill the session at the database) and the slow right one (find the session and release it the way the vendor says to). Enforce the second — a session killed mid-write is how a lock ticket becomes a data-corruption ticket. Work in order.

1. History first. Search this client's past tickets for the app + lock symptoms. The prior lock ticket usually documents the vendor-approved release method — the single most valuable artifact for this playbook. Repeat tickets shift the goal from clearing today's lock to fixing the cause.

2. Docs second. Check the client's documentation and knowledge base for the app's profile: vendor, version, database engine underneath, whether the database is vendor-managed, and — the key item — the documented session/lock-management procedure. If none is documented, finding it (vendor KB on the web, or asking the vendor) is step one, and documenting it afterward is part of closing the ticket. Documentation may be absent for this tenant — fall back to the knowledge base and say what you could not check.

3. Identify versions. App and version; lock-management procedures are version-specific, and old advice against a new version is how damage happens.

4. Evidence before theory. The exact lock message (record vs batch vs module vs login lock — different mechanisms), which user/session the app names as the holder, and when the lock appeared. Then verify reality: is that user actually in the app? Ask them or their neighbor before assuming a ghost session.

5. Branch on the evidence:
   a. The holder is real and present — not a stuck lock at all. The record is legitimately in use; coordinate between users. This is a conversation, not a ticket escalation.
   b. Ghost session, app-level release exists — the user crashed/disconnected and the app has an admin console for sessions (most LOB apps do: a user/session manager, a "clear locks" or "release user" function). Confirm with the named user that they are truly out and have no unsaved work — releasing a session with unsaved work destroys that work, so get an explicit "I'm out, nothing unsaved" from the named user or their manager and note who said it — then guide the app admin through the vendor's release procedure. This is the standard path; the app's own tooling releases cleanly because it knows its transaction state. Escalate when the console shows the session but release fails — vendor support with the session details; do not drop to the database layer on your own.
   c. No app-level tool, or lock survives it — the vendor's documented method may involve a lock file to remove (some file-based LOB apps) or a vendor utility. Follow only a written vendor procedure for this exact version (search the vendor KB on the web and cite it in the ticket; do not fabricate procedures or references). Preconditions: all users out of the app where the procedure requires it, and a current backup confirmed before touching lock files — if backup state is unknown, that is a stop condition. Escalate when the only remaining option is killing a session at the database engine — STOP. That is vendor territory: get vendor support on the case and act only under their direction. If the database is vendor-managed, it was never the desk's to touch — evidence and escalation only.
   d. License-eating stuck logins — users blocked because ghost sessions consume seats. Same discipline as branch b, plus note the frequency: if crashes keep abandoning sessions, the crash is the real ticket — pair with the LOB Application Framework playbook to root-cause and build the vendor case.
   e. Recurring locks — same record type, same time of day, same workflow. Look for the pattern: a report that opens tables exclusively during business hours, a user habit (record left open overnight), a client/app timeout setting the vendor allows tuning. Recommend the pattern fix to the client and vendor; clearing lock after lock is treadmill work.

Never kill database sessions ad hoc — no KILL SPID, no engine-level session drops, no deleting lock files outside a written, version-matched vendor procedure. The lock is annoying; a torn transaction is a restore. You do not run scripts or remote commands — every procedure is guidance for the app admin or tech, or a vendor case.

6. Close the loop. Have the blocked user retry the exact operation, and check the app for error flags on the affected record (a released lock with a half-written record is not a win — if the app offers a data-verify function, recommend running it). Leave a plain-text internal note (plain text, no markdown or emojis, raw URLs not links): lock type, holder session, method used and its source (vendor KB reference), who confirmed the user was out, verification result, and anything you couldn't check.
```
