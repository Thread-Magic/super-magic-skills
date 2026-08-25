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

DURING (or immediately after) the emergency
1. Verify it qualifies: an active incident or imminent harm where waiting for normal
   approval is more damaging than acting. Name the incident ticket. "Urgent for the
   client" without service impact is a normal change on a fast calendar — route it back.
2. Create the emergency change record on the change board, titled "EMERGENCY CHANGE:
   <system> — <one-line what>", with the minimum in-flight fields: what is changing, why
   now (link the incident), who is executing, and the intended reversal if it makes things
   worse. Thirty seconds of typing, not a CAB submission.
3. Capture the authorization actually obtained — even emergencies need a named human
   saying go (on-call lead, or the client emergency contact per policy). Record who and
   how: send it for approval through the system where that exists, otherwise a note naming
   the verbal authorizer and the time. If the executor authorized themselves, record that
   plainly; it is reviewable, not hidden.
4. Timestamp actions in notes as close to real time as you can — contemporaneous fragments
   beat a polished reconstruction.

WITHIN 24 HOURS — the mandatory retro
5. Complete the record to full change-request standard: final what/why/scope, actual
   actions with times, actual result, rollback status, post-change validation evidence,
   and the risk assessment written honestly after the fact (what the blast radius really
   was). Still incomplete at 24h -> escalate to the change owner or lead by note; the debt
   never ages out silently.
6. Route the completed record for retroactive review: the approver, or the next CAB via
   cab-brief-builder, decides whether the call was right and whether the change stays or
   is re-done properly.
7. If the emergency fix is a temporary patch, open the follow-up normal change now and
   link it — emergency fixes become permanent by inertia.

MORNING-AFTER SWEEP: search for emergency changes created in the last 24-48h, check retro
completeness against step 5, leave an itemized gap note on incomplete ones, and flag
repeat offenders (same tech, serial incomplete retros) to the lead.

Guardrails: emergency is a justification class, not a convenience class — no incident, no
emergency; push back on laundering normal changes through the fast lane. You paper and
chase; you do not execute the change and do not retroactively approve it — that review is
a human's call. Never backfill the record to look like approval preceded action; the
honest, timestamped sequence is the defensible one. Notes are plain text, no markdown or
emojis (apply the PSA Note Discipline base skill) — this trail is what an auditor or an
angry client reads later.
```
