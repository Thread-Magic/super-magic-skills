---
name: IIS Web App
description: Diagnose IIS web app failures — app pool crashes, rapid-fail protection, binding and SSL problems, HTTP 500/502/503 codes — using HTTP.sys and FREB logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# IIS Web App

**When to use:** An internal or client-facing site returns 500 / 502.x / 503, an app pool keeps stopping or recycling constantly, HTTPS broke after a cert renewal or the wrong cert is served, or a site works on the server but not remotely (or one app under a site fails while others work).

**Run it:** on the one ticket you're working — a tech with server access drives this; not unattended.

## Prompt

```
An IIS error page tells you nothing until you read the sub-status and the pool state. Decode
both before anyone recycles a pool or reinstalls anything.

Climb the Troubleshooting Ladder base skill first: past tickets for this site — a
deployment, a certificate renewal, a Windows or .NET patch, a service-account password
change (a pool whose identity password changed won't start) — then the documented server:
IIS version, whether a vendor app is hosted here, pool-to-site mapping, runtime version,
pool identity, expected bindings and certificates.

Evidence before theory: exact status and sub-status, pool Started/Stopped, the System log
for WAS and rapid-fail entries, the Application log for the app's exception, HTTP.sys logs.
For an intermittent 500, enable Failed Request Tracing. Never act on the browser's generic
"500".

Branch:
a. Pool crashing / rapid-fail — Stopped after WAS disabled it on N failures in the
   rapid-fail window: the worker process is dying. Read the Application log or crash dump
   for the exception — bad deployment, missing dependency, runtime mismatch, memory. Never
   fix a 503 by re-enabling a pool rapid-fail disabled; that hides a crashing app. Vendor
   code goes to the vendor with the exception.
b. Bindings and SSL — HTTPS failing, wrong certificate, or handshake errors after a renewal.
   A renewed certificate has a new thumbprint and often was never re-bound; SNI-versus-IP
   bindings and host/port collisions do the same. Check the HTTP.sys SSL binding, not just
   the IIS UI, and treat certificate work as a change (see the SSL certificate renewal
   playbook).
c. 500-series decode — 500.19 is configuration/web.config (bad section, locked config, file
   permissions); 500.21 means a runtime or module isn't registered; 500.0 and 502.5 mean the
   app or runtime process fails to start. Confirm the sub-status against its documented
   meaning on the web and fix that layer only.
d. 503 — almost always a stopped or disabled pool (branch a) or HTTP.sys with no listener
   for the binding. Confirm pool state first; it is infrastructure, rarely app code.
e. Recycling — constant recycling on interval, memory-limit or config-change triggers drops
   sessions and warms slowly. Read the recycle events: intended trigger, or a memory leak?
   Tuning a vendor app's recycling follows vendor guidance.

For a vendor application, never edit its web.config, pool runtime or identity without vendor
guidance — you break support and the app. Hand config changes to the vendor or app owner.
Restarting W3SVC or WAS, or recycling a pool, hits everyone on the host: flag that and
prefer off-hours.

Verify the failing request returns its real page, the pool stays Started and the right
certificate is served. Note it (PSA Note Discipline base skill): status and sub-status, pool
state, evidence, branch, action or handoff, verification.
```
