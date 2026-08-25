---
name: Citrix Basics
description: First-line playbook for Citrix Virtual Apps and Desktops (CVAD/DaaS) — VDA registration, StoreFront vs Workspace, hung sessions — before escalating.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Citrix Basics

**When to use:** "<user> can't launch their Citrix app/desktop" (spinner, error, or nothing happens); sessions freeze/hang, disconnect repeatedly, or reconnect to a dead session; a published app is missing from a user's store or everyone lost access at once; or the client has Citrix, the MSP has no dedicated Citrix bench, and the desk needs a defensible first pass.

**Run it:** on the one ticket you're working — a generalist tech runs the first pass hands-on, then hands off to the Citrix admin.

## Prompt

```
Give a non-Citrix tech a defensible first pass on a Citrix Virtual Apps and Desktops or DaaS
ticket. Localize the failure — client, access layer, broker, VDA, session — and hand the
admin a diagnosis, not a symptom.

Climb the Troubleshooting Ladder base skill first, with these specifics. Establish the
deployment shape; it decides who can fix this. On-prem the client owns the Delivery
Controllers and StoreFront; on DaaS Citrix owns the broker plane — check their status page
first, as only Citrix can act on a platform incident. Note the access layer (StoreFront
URL or Workspace), any Gateway or NetScaler in path, and the named Citrix admin — no named
admin is itself a finding. Evidence: the exact client error ("Cannot start app", 1030, "SSL
error 61") and where it lands: before login is the access layer, after login without launch
is broker or VDA, in-session is the VDA.

1. Client-side, one user while others are fine from the same spot — an ancient or corrupt
   Workspace app (reinstall to the client standard), certificate errors from a missing
   intermediate or root on the endpoint, a stale store (remove and re-add), or the browser
   saving .ica files instead of launching.

2. StoreFront versus Workspace confusion — the user bookmarked the wrong entry point, or
   uses the internal StoreFront URL from outside: works in the office, dies at home. Correct them to the sanctioned URL for their location; if old and new stores answer
   with different app sets, flag the drift.

3. Missing app, or "you have no apps or desktops" — usually group membership (published to
   an AD group the user isn't in) or the wrong store. Check membership against the
   documentation; group changes follow the access-request process. Membership right
   and the app still hidden is broker territory.

4. Launch fails after the click (spinner, 1030-style, timeout) — the classic cause is VDA
   registration. A generalist with read access may look, not touch. Stop at naming the
   unregistered or oversubscribed VDA and whether it just rebooted; registration faults
   (time skew, DNS, listener) are the admin's.

5. Session hangs and ghost sessions — separate a dying network path (the session disconnects
   but survives) from a wedged session. The safe fix is the admin console's log-off of that
   single session, with the user's consent first — unsaved work dies.
   Recurring hangs on one VDA go to the admin; note any print action preceding them.

Attempt no Citrix-admin surgery — policy edits, delivery group or catalog changes, MCS or
PVS image work, Gateway or NetScaler config, license-server work — and never restart
Delivery Controllers, StoreFront or Gateway to test. The escalation package: deployment
shape, scope, verbatim errors, registration state, what changed, what you ruled out. Verify
by the user launching, and note it in plain text (PSA Note Discipline base skill).
```
