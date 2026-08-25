---
name: Adobe Creative Cloud Licensing
description: Fix Adobe Creative Cloud sign-in loops, access-denied errors, and Admin Console entitlement gaps between named-user and shared-device licensing.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Adobe Creative Cloud Licensing

**When to use:** Creative Cloud apps prompt to sign in repeatedly or loop without completing; "you don't have access to this app" / "subscription expired" for a licensed user; confusion between named-user and shared-device (lab/classroom) licensing; or a new user can't get an app, a departed user's seat needs reclaiming, or federated/SSO sign-in fails.

**Run it:** on the one ticket in front of you — a tech works this with the Adobe admin, not unattended.

## Prompt

```
Most Creative Cloud "it won't open" tickets are licensing, not the app. The truth is in
the Adobe Admin Console: the right identity type, the product actually assigned, and
whether this machine should be named-user or shared-device licensed. Check entitlement
first, reinstall last.

Establish the licensing model and identity first, from the client's documentation: plan
type (teams vs enterprise, VIP or ETLA), identity model (Adobe ID vs Business or
Enterprise ID vs Federated SSO), which devices are shared-device licensed (labs, shared
workstations) rather than named-user, and who administers the Console. That last fork
decides everything else.

Then climb the Troubleshooting Ladder base skill: past Adobe tickets — a license
reassignment, an SSO or directory change, a plan lapse, a re-image; a "suddenly" lost
app usually means a seat reclaimed or a plan lapse. Then check entitlement with the
admin: is the user present, with the correct identity type and the specific product
profile assigned, on an active plan with seats free? Then take the exact sign-in error
and whether Creative Cloud desktop signs in at all.

1. Sign-in loop or repeated prompts. Usually the identity the user enters isn't the one
   Adobe expects (a personal Adobe ID against the org's Federated or Business ID), a
   Federated SSO fault (the IdP isn't returning the user, or the domain isn't claimed
   and linked to the directory), or stale local credentials. Pair with the identity/SSO
   playbooks rather than toggling Adobe settings blindly. Clearing the local Adobe
   credential and OOBE state is clean — but confirm the identity mismatch first.

2. "No access" or expired for a licensed user — not assigned the product, unassigned, no
   free seats, or signed in with the wrong identity. Fix by assigning the correct
   product profile to the correct identity. Seat allocation is the client's licensing
   and cost decision: confirm with the account owner before consuming a seat; never buy
   or allocate seats on your own authority.

3. Named-user vs shared-device mismatch — a lab or shared machine licensed named-user
   (so it demands each sign-in and burns seats), or a personal workstation given the
   shared-device package. The fix is deploying the correct package — a packaging
   decision, not an end-user fix.

4. Provisioning or reclamation — assign or unassign in the Console; pair with
   onboarding-and-access or employee-offboarding. Reclaiming a leaver's seat frees the
   license — confirm no shared assets are stranded first.

Adobe accounts tie to people: refer to users by placeholder and keep identity details
out of notes. Success is the user opening the licensed app on the correct identity, seat
assigned in the Console. Note it (apply the PSA Note Discipline base skill): licensing
model, identity type, entitlement finding, branch, action, verification.
```
