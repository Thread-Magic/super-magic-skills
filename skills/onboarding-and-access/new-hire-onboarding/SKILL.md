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
Run a new-hire onboarding request from intake to a tracked, role-appropriate provisioning
checklist. Work it, don't just plan it.

1. Gather from the ticket and the client's intake form if one exists: full name, start date,
   role and title, department, manager, location, requested apps and groups. Look up the
   client and manager records to anchor them. List everything missing and ask me for it in
   ONE message, not piecemeal.

2. Check the start date. Inside 48 hours, raise the priority using the board's real priority
   names and flag the dispatcher in a note so it can't sit in the queue.

3. Pull the client's onboarding SOP from the knowledge base and their IT documentation, then
   build the checklist in three categories: Required (every hire — account, mailbox, MFA,
   baseline groups), Conditional (role or department driven — license bundle, department
   groups, LOB apps), and Optional (requester extras needing explicit confirmation). Apply
   the Connector Degradation base skill when the documentation platform isn't connected.

4. Map role to access from the client's documented role profile. No profile: propose one
   from the closest documented role and have me confirm it — never invent a default. Low
   confidence in the mapping means ask, not provision.

5. On "mirror <user>" requests, confirm exactly whose access if it's ambiguous, enumerate
   that user's groups, licenses and delegations, then apply least privilege — copy only what
   the new role needs. Never silently copy admin roles, elevated groups, or delegated
   mailbox access; list those separately and require explicit approval for each.

6. Confirm the full plan with me, with a timeline: account-ready date and hardware ETA. Any
   license carrying cost gets sign-off first, by approval request or the client's documented
   approval channel.

7. Provision or hand off. Where Entra writes are available via Zapier, use the Entra User
   Lifecycle (Zapier) skill. On hybrid on-prem AD, run a delta sync after account creation
   and verify the object synced before assigning cloud licenses or groups.

8. Credentials: enforce MFA enrollment and force a password change at first sign-in. The
   temporary password travels only through the client's secure transfer method — never plain
   email, never pasted into the ticket.

9. Post the checklist as a note: each item under Required, Conditional or Optional with a
   status of Done, Pending or Blocked, and an owner (apply the PSA Note Discipline base
   skill). Confirm completion and the remaining timeline to me, and log time.

Base access on the role profile and the client's licensed solutions, never a generic
default. Don't invent SOP steps, group names or license SKUs — if the documentation is
missing, say so rather than guessing.
```
