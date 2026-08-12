---
name: Adobe Creative Cloud Licensing
description: Fix Adobe Creative Cloud sign-in loops, access-denied errors, and Admin Console entitlement gaps between named-user and shared-device licensing.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
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
You are diagnosing an Adobe Creative Cloud licensing / sign-in problem. Most Creative Cloud "it won't open" tickets are licensing, not the app. The truth lives in the Adobe Admin Console: whether the user has the right identity type, is assigned the product, and whether this machine should be named-user or shared-device licensed. Check entitlement first and reinstall last — reinstalling rarely fixes a licensing/identity problem and costs the user hours.

Licensing model and identity first. Check the client's documentation and knowledge base for the Adobe setup: the plan type (Creative Cloud for teams vs enterprise/VIP/ETLA), the identity model (Adobe ID vs Business/Enterprise ID vs Federated SSO), whether any devices are shared-device licensed (labs, shared workstations) vs named-user, and who administers the Admin Console. Named-user vs shared-device is the fork that decides everything — establish it before touching the client. Documentation coverage varies per tenant — note what you couldn't check.

History first. Search this client's past tickets for Adobe work: a recent license reassignment, an SSO/directory change, a plan renewal/expiry, or a device re-image. A user who "suddenly" lost access often had a license reclaimed or a plan lapse.

Check entitlement before theorizing. In the Adobe Admin Console (guide the admin): is the user present, with the correct identity type, and assigned the specific product/product profile? Is the plan active with seats available (not over-allocated)? For the app itself, get the exact sign-in error and whether Creative Cloud desktop signs in at all. Read the entitlement — don't reinstall on a hunch. Admin Console, packaging, and client steps are guidance for the Adobe admin / a tech, not remote execution; if the RMM is connected, open the workstation in it (a deep link for the tech, not script execution) for the hands-on handoff, otherwise have the tech work at the machine directly.

Branch:
1. Sign-in loop / repeated prompts — auth never sticks: usually a mismatch between the identity the user enters and the identity type Adobe expects (personal Adobe ID vs the org's Federated/Business ID), a Federated SSO problem (the IdP isn't returning the user, or the domain isn't claimed/linked), or stale local credentials. For SSO, test the federation and confirm the user's domain is linked to the directory; pair with the identity/SSO playbooks rather than toggling Adobe settings blindly. Clearing the local Adobe credential/OOBE state is a clean step, but confirm the identity mismatch first.
2. "No access" / expired for a licensed user — the user isn't assigned the product (or was unassigned), the plan has no free seats, or they're signed in with the wrong identity. Fix by assigning the correct product profile to the correct identity in the Console. Seat allocation is the client's licensing (and cost) decision — confirm with the account owner before consuming a seat; don't buy or allocate seats on your own authority.
3. Named-user vs shared-device mismatch — a shared/lab machine was licensed named-user (so it demands each person sign in and burns seats) or a personal workstation got the shared-device package. The fix is deploying the correct package for the use case (shared-device license package for labs, named-user for personal machines) — a packaging/deployment decision, not an end-user fix.
4. Provisioning / reclamation — a new hire needs access or a leaver's seat must be reclaimed: assign/unassign in the Console (pair with onboarding-and-access / employee-offboarding). Reclaiming a departed user's seat frees the license; confirm no shared assets are stranded first.

Adobe accounts and assets tie to people — refer to users by placeholder and keep identity details out of PSA notes. Do not invent Console menu paths, package types, or plan behaviours — check Adobe's current admin docs on the web and cite (Adobe changes these often).

Verify and note. Success is the user opening the actual licensed app signed in with the correct identity, with the seat showing assigned in the Console. Leave a plain-text internal note (raw URLs, not markdown, no emojis): licensing model, identity type, entitlement finding, branch, action or handoff, verification, and what you couldn't check.
```
