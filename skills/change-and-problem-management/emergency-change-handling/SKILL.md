---
name: Emergency Change Handling
description: Run break-glass discipline for an emergency change: minimal in-flight record, act-then-document, then chase full retro documentation to done in 24 hours.
category: Change & Problem Management
tools: [search_tickets, create_ticket, update_ticket, add_ticket_note, send_approval, list_boards]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Emergency Change Handling

**When to use:** "We had to change the firewall rule at 2am to stop the bleeding — paper it" / an incident response about to make a production change with no time for normal approval / the morning-after sweep for last night's emergency changes / an emergency change flagged as missing retroactive documentation.

**Run it:** on one emergency change · or as a morning-after sweep of recent ones.

## Prompt

```
Emergency changes trade approval order for speed — never the record. You may act before
the paperwork; in exchange the paperwork is not optional, not partial, and not late.
Cover both halves: the minimal record during, and the retro-documentation debt after.

DURING (or immediately after) the emergency:
1. Verify it qualifies: an active incident or imminent harm where waiting for normal
   approval is more damaging than acting. Name the incident ticket. "Urgent for the
   client" without service impact is a normal change on a fast calendar — route it back.
2. Create the emergency change record (on the change board, title
   "EMERGENCY CHANGE: <system> — <one-line what>") with the minimum viable in-flight
   fields: what is being changed, why now (link the incident), who is executing, the
   intended reversal if it makes things worse. Thirty seconds of typing, not a CAB
   submission.
3. Capture the authorization actually obtained — even emergencies need a named human
   saying go (on-call lead, client emergency contact per policy). Record who authorized
   and how (request approval through the system where available; otherwise a note naming the verbal authorizer and
   time). If the executor authorized themselves, record that plainly — it's reviewable,
   not hidden.
4. As actions happen, timestamp them in notes as close to real time as possible.
   Contemporaneous fragments beat a polished reconstruction.

WITHIN 24 HOURS (the mandatory retro):
5. Complete the record to full change-request standard: final what/why/scope, actual
   actions with times, actual result, rollback status, post-change validation evidence,
   and the risk assessment written honestly after the fact (what the blast radius really
   was). Incomplete after 24h → escalate to the change owner/lead by note; the debt does
   not silently age out.
6. Route the completed record for retroactive review: the approver (or next CAB via
   cab-brief-builder) reviews whether the emergency call was right and whether the change
   stays or gets re-done properly.
7. If the emergency fix is a temporary patch rather than the real fix, open the follow-up
   normal change now and link it — emergency fixes become permanent by inertia.

MORNING-AFTER SWEEP: search for emergency changes created in the last 24-48h;
check retro-documentation completeness against step 5's list; post an itemized gap note
on incomplete ones and flag repeat offenders (same tech, serial incomplete retros) to
the lead.

Guardrails: emergency is a justification class, not a convenience class — no incident, no
emergency; push back on laundering normal changes through the fast lane. Act-then-document
never becomes act-then-nothing: the 24h retro is the hard rule this skill enforces. The
agent papers and chases; it does not execute the change and does not retroactively approve
it — the retro review is a human's call. Never backfill the record to look like approval
preceded action when it didn't — the honest, timestamped sequence is the defensible one.
Plain-text notes throughout; this trail is what an auditor or angry client reads later.
```
