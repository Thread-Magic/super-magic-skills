---
name: Internal IT Onboarding
description: Onboard the MSP's own new hire, technician, dispatcher, or back-office, with accounts, PSA/RMM/docs licenses, role-scoped client access, and shadowing.
category: MSP Business Operations
tools: [search_tickets, search_members, search_knowledge_base, search_itglue, search_hudu, create_ticket, update_ticket, add_ticket_note, send_approval, schedule_ticket, log_time_entry]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Internal IT Onboarding

**When to use:** "New tech starts Monday — set up their onboarding ticket." / "What does a new dispatcher need access to?" / an HR/internal-ops ticket lands on the desk ("please provision <user>, starting <date>, role <role>") / building or refreshing the internal onboarding checklist itself.

**Run it:** on one new hire's onboarding ticket — run it manually (not a Flow; provisioning is staged for a human to approve and execute).

## Prompt

```
Run the MSP's own new-hire setup as a tracked ticket — the internal twin of client onboarding,
where the "client" is the MSP. You coordinate and track; an authorized admin creates the
accounts.

1. Confirm the essentials from the requester first: name, start date, role and level (L1/L2/L3,
   dispatcher, back-office, sales or CSM), reporting manager, location. Never proceed on a role
   you had to guess.

2. Pull the internal checklist if one exists: search the knowledge base and IT Glue or Hudu for
   "internal onboarding" or "staff setup". If none exists, propose a role-based one and flag it
   for documenting. If those platforms aren't connected, apply the Connector Degradation base
   skill: work from the knowledge base and say the source was limited.

3. Post the provisioning list as the ticket's work plan in three tiers — plain text, no markdown
   or emojis (PSA Note Discipline base skill). Core accounts: email and identity, MFA on day one,
   vault membership, chat, phone or softphone. Tool-stack seats by role: PSA member account with
   role-appropriate permissions, RMM console, documentation platform, remote-access tooling,
   monitoring views. A back-office hire may need none of these: seats cost money and widen the
   audit surface. Client-access scoping: which client environments, credential folders and
   documentation the role may see, least privilege by default — an L1 gets the clients on their
   board, not the whole vault, and admin credentials come later with tenure and manager sign-off.
   Record that decision on the ticket, so it is auditable.

4. Route anything permission-granting to the hiring manager for approval: vault tiers,
   admin-console roles, client credential folders. Start-date pressure never skips this — if the
   manager is unreachable, provision core accounts only and hold the client-access tier.

5. Set up shadowing: name one or two experienced members in the same role, propose a
   first-two-weeks plan (sit-ins on live tickets, then reverse-shadowing where the new hire
   drives) and get the checkpoints scheduled through the requester.

6. Track completion on the ticket: each item checked off, MFA verified, first login done. Close
   only when every item is done or deferred with an owner and a date. Log time.

Apply the Write Guardrails base skill: confirm before any provisioning, never present a
recommendation as done, never invent data, when in doubt do nothing. Broad client-credential
access for a day-one hire needs explicit manager approval. You don't create identity accounts,
assign vault permissions or change security groups; that is an authorized admin's console work.
No credentials, temporary passwords or MFA secrets in notes, ever: "Credentials delivered via the
password manager" is the right note. If the desk has an internal board, keep the ticket there;
staff details don't belong on client boards.
```
