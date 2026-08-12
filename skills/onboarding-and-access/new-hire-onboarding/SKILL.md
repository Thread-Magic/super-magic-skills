---
name: New Hire Onboarding
description: Run a new-hire onboarding end to end with role-based accounts, licenses, groups, hardware, and MFA driven from the client's own onboarding checklist.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, update_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# New Hire Onboarding

**When to use:** "New hire starting Monday at <client> — set them up like the sales team" / "onboard <user>, role <role>, needs laptop and M365" / "same access as <user>" — any onboarding ticket that needs the full role-based checklist built and worked.

**Run it:** on one ticket — role- and approval-gated, so a human confirms the plan before provisioning.

## Prompt

```
Run this new-hire onboarding request from intake to a tracked, role-appropriate
provisioning checklist. Work it, don't just plan it.

1. Gather from the ticket (and the client's intake form if one exists): full name,
   start date, role/title, department, manager, location, requested apps/groups.
   Look up the client and manager records to anchor them. List everything missing
   and ask me for it in ONE message, not piecemeal.

2. Check the start date. If it is within 48 hours, raise the ticket priority (using
   the board's real priority names) and flag the dispatcher in a note so it can't
   sit in the queue.

3. Pull the client's onboarding SOP from the knowledge base and their IT documentation
   (IT Glue / Hudu) and build the checklist in three categories: Required (every hire
   gets these — account, mailbox, MFA, baseline groups), Conditional (role/dept
   driven — license bundle, dept groups, LOB apps), Optional (requester extras that
   need explicit confirmation). If IT Glue/Hudu aren't enabled, fall back to the
   knowledge base and say external docs weren't checked.

4. Map role to access from the client's documented role profile. If no profile
   exists, propose one from the closest documented role and have me confirm it —
   never invent a default. If confidence in the mapping is low, ask; do not provision.

5. For "mirror <user>" requests: confirm exactly whose access if ambiguous,
   enumerate that user's groups/licenses/delegations, then apply least privilege —
   copy only what the new role needs. Never silently copy admin roles, elevated
   groups, or delegated mailbox access; list those separately and require explicit
   approval for each.

6. Confirm the full plan with me including a timeline (account-ready date, hardware
   ETA). For licenses that carry cost, get sign-off first (send an approval request,
   or use the client's documented approval channel).

7. Provision or hand off provisioning. If Entra writes are available via Zapier, use
   the Entra User Lifecycle (Zapier) skill. If the client is hybrid on-prem AD, run
   an AD Connect delta sync after account creation and verify the object synced
   before assigning cloud licenses or groups.

8. Credentials: enforce MFA enrollment and force a password change at first sign-in.
   Deliver the temporary password ONLY through the client's secure transfer method —
   never plain email, never pasted into the ticket.

9. Post a structured checklist note (plain text, no markdown/emojis — it may sync to
   the PSA): each item under Required/Conditional/Optional with status Done / Pending
   / Blocked and an owner. Confirm completion and remaining timeline to me, and log
   time.

Guardrails: base access on the role profile and the client's licensed solutions,
never a generic default. Confirm before creating accounts or assigning anything with
license cost. Passwords travel only by secure transfer with change forced at next
sign-in. Do not invent SOP steps, group names, or license SKUs — if documentation is
missing, say so rather than guessing.
```
