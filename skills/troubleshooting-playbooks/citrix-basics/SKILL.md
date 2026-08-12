---
name: Citrix Basics
description: First-line ladder for Citrix (Virtual Apps and Desktops / DaaS) tickets on desks without a Citrix specialist — VDA registration, StoreFront vs Workspace confusion, sessions hanging or apps not launching — knowing exactly what a generalist can check and when to hand to the Citrix admin.
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
You are giving a non-Citrix tech a defensible first pass on a Citrix (Virtual Apps and Desktops / DaaS) ticket. Localize the failure (client → access layer → broker → VDA → session), do the safe checks, and hand the Citrix admin a diagnosis instead of a symptom. Do NOT attempt Citrix-admin surgery (policies, delivery group edits, PVS/MCS image work).

Version identification first. Check the client's documentation and knowledge base for the deployment shape — it decides who can even fix things: on-prem Virtual Apps and Desktops (client-owned Delivery Controllers/StoreFront) vs Citrix DaaS/Cloud (Citrix owns the broker plane — check Citrix's status page before troubleshooting a cloud brokering failure; only Citrix can act on platform incidents, so reference their status/incident and set expectations honestly instead of troubleshooting the unreachable). Note the access layer (StoreFront URL vs Workspace), any Gateway/NetScaler in path, and who the named Citrix admin/partner is. Documentation coverage varies per tenant — note anything you could not check, including whether a named Citrix admin exists at all (if not, that gap is itself a finding for the account owner).

History first. Search this client's past tickets: one user → client device, account, or their session; one application → that app's VDA group or the app itself; everyone → access layer, Gateway cert, broker, or a licensing/platform event. Sudden farm-wide failure on a date smells like a certificate or an infrastructure change — ask what changed.

Get the error before theorizing. Exact client-side error text ("Cannot start app", "1030", "SSL error 61…", "Cannot connect to server") plus where it appears: before login (access layer), after login but app won't launch (broker/VDA), or in-session (VDA/session). Citrix error strings are specific and overloaded across versions — search the web for the verbatim text against Citrix's documentation rather than pattern-matching from memory. All checks here are guidance for the tech or read-only console observation; there is no script execution from this playbook.

Branch — the generalist's safe territory:
1. Client-side (one user, others fine from same location) — Workspace app version ancient or corrupt (reinstall current per client standard), SSL/cert errors on old clients (often missing intermediate/root on the endpoint), stale store config (remove and re-add the store/Workspace account), or the browser downloading .ica files without launching (file association). All safe to fix.
2. StoreFront vs Workspace confusion — users bookmark the wrong entry point after a migration, or use the internal StoreFront URL from outside (works in office, dies at home = missing the Gateway path). Confirm from the documentation which URL is sanctioned for the user's location and correct the user's entry point; if both old and new stores answer with different app sets, flag the drift to the Citrix admin rather than guessing which is authoritative.
3. Missing app / "have no apps or desktops" — usually group membership (published to an AD group the user isn't in) or the wrong store. Verify membership against the documentation; group fixes follow the client's access-request process (onboarding-and-access rules), not ad-hoc adds. Escalate when membership is right and the app still hides — that's enumeration/broker territory.
4. Launch fails after click (spinner, 1030-style, timeout) — the classic cause is VDA registration: the target VDA isn't registered with the broker (the client's admin console shows registration state; a generalist with read access may look, not touch). Safe generalist moves stop at identifying the unregistered/oversubscribed VDA and whether it just rebooted/patched. Registration failures (time skew, DNS, listener) and capacity are the Citrix admin's — hand off with: which VDA(s), registration state, when it broke, what changed.
5. Session hangs / freezes / ghost sessions — differentiate network path (user's connection dying → the session disconnects but survives; pair with wifi/vpn playbooks) from a wedged session. A wedged session's safe fix is the admin console's log-off/disconnect of THAT session, with the user's consent first — unsaved work dies. Recurring hangs across users on one VDA → that VDA to the admin; printing-triggered freezes are a known genre — note if a print action precedes hangs.

Escalate like a professional. The handoff to the Citrix admin/partner is the product of this playbook when the fix is beyond the branches above. It must contain: deployment shape, scope (who/what/since when), verbatim errors, VDA/registration observations, what changed, and what was already ruled out. Never attempt Citrix policy edits, delivery group/catalog changes, image (MCS/PVS) updates, Gateway/NetScaler config, or license server surgery, and never restart Delivery Controllers, StoreFront, or Gateway services "to see" — farm-wide blast radius, admin-owned every time.

Verify and note. Success = the user launching and using the resource; for handoffs, the admin's confirmation. Leave a plain-text internal note (raw URLs, not markdown): deployment shape, scope, error verbatim, branch, fixes done or the escalation package sent, verification and time, and what you couldn't check.
```
