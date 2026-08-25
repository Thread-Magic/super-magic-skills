---
name: LOB Database Locks
description: Clear record-locked-by-another-user tickets in LOB apps — find the locking session in the vendor admin console and release it approved-only, never kill DB.
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
You are clearing an LOB database-lock ticket. The fast wrong fix is killing the session at
the database; the right one is releasing it the way the vendor says to. A session killed
mid-write turns a lock ticket into a data-corruption ticket.

Climb the Troubleshooting Ladder base skill first: this client's past tickets for this app
and symptom (the prior lock ticket usually documents the vendor-approved release method;
repeat tickets shift the goal to fixing the cause), then their documentation for the app —
vendor, version, the database engine underneath, whether it is vendor-managed, and the
documented session/lock release procedure. If none is documented, find the vendor's;
procedures are version-specific.

Get the evidence: the exact lock message (record, batch, module and login locks are
different mechanisms) and which user or session the app names as holder. Then ask whether
that user is actually in the app before assuming a ghost session.

Branch:

1. The holder is real and present. Not a stuck lock — coordinate between the two users.

2. Ghost session with an app-level release. Most have a session manager or "release user"
   function. Before using it, get an explicit "I'm out, nothing unsaved" from the named user
   or their manager and record who said it — releasing a session with unsaved work destroys
   that work. Then guide the app admin through the vendor's procedure. If the console shows
   the session but release fails, take it to vendor support — do not drop to the database
   layer. If ghost sessions are eating licenses and crashes keep abandoning them, the crash
   is the real ticket.

3. No app-level tool, or the lock survives it. The vendor's method may be a lock file to
   remove or a vendor utility. Follow only a written vendor procedure for this exact
   version, and cite it. Preconditions: all users out where the procedure requires it, and a
   current backup confirmed before touching lock files — unknown backup state is a stop
   condition. If the only option left is killing a session at the database engine, stop and
   open a vendor case; a vendor-managed database was never the desk's to touch.

4. Recurring locks — same record type, time of day, or workflow. Find the pattern (a report
   opening tables exclusively during business hours, a record left open overnight, a timeout
   the vendor allows tuning) and fix that. Clearing lock after lock is treadmill work.

Never kill database sessions ad hoc, and never delete lock files outside a written,
version-matched vendor procedure. Every procedure is guidance for the app admin or tech, or
a vendor case.

Close the loop: have the blocked user retry the exact operation and check the record for
error flags. Then note it (apply the PSA Note Discipline base skill): lock type, holder
session, method and its source, who confirmed the user was out, and the verification.
```
