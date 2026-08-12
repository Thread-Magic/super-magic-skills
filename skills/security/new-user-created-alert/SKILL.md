---
name: New User Created Alert
description: Investigate an unexpected user or admin account creation in a client tenant: check for an authorizing ticket and contain if no one can claim it.
category: Security
tools: [search_tickets, search_members, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Fewer Escalations & Less Noise, Risk & Compliance]
---

# New User Created Alert

**When to use:** A "new user created" or "user added to admin role" alert lands as a ticket; an unfamiliar account surfaces during another investigation; or a client asks "who created this account?"

**Run it:** on one ticket (a new-account or admin-grant alert).

## Prompt

```
Most new-account alerts are HR onboarding wearing a scary hat; a few are attacker
persistence. Check for the boring explanation first — an authorizing ticket — and escalate
hard only when nothing claims the account. Work it in order:

1. Extract the created account's facts: display name, UPN, assigned roles and licenses, the
   creating account, and the creation timestamp. Flag immediately if any administrative role
   was granted at creation — that raises the tier before any other checking.
2. Authorized-change cross-check BEFORE alarm: search the client's tickets for onboarding,
   new-hire, or change tickets in a window around the creation date whose subject or contact
   matches the new account's name. Also check whether the creating account belongs to the
   MSP's own technicians doing legitimate provisioning.
3. Match found → benign path: document the authorizing ticket reference, who performed the
   creation, and the match reasoning in a plain-text note; move to pre-closure per
   soc-classification-tree.
4. No match → verify with the client's authorized approver through a known, documented
   contact channel: "did you request or approve this account?" A verbal "sounds familiar" is
   not authorization — ask for the specific name and purpose.
5. Unclaimed account → treat as suspected persistence: have sign-in disabled on the new
   account now, contain fast, investigate second. Then investigate the CREATING account — an
   attacker needs existing privileged access to create users, so the creator is a suspected
   compromised account: run the account-takeover-runbook against it.
6. Admin-role creations get the strict version of every step: explicit change-approval
   evidence required, no closure on informal confirmation, and escalation to the client's
   security contact on any gap.
7. Document the decision, not just the action: the note records the account facts, every
   cross-check performed, who confirmed what, and the verdict reasoning.

Guardrails — always:
- Cross-check before alarm — a false alarm to a client about their own new hire erodes trust
  in every future alert.
- Never close on assumption: "the name looks like an employee" is not an authorizing ticket.
  Low-confidence match → treat as no match.
- An unexplained admin account is contain-first territory; when in doubt, escalate — a false
  escalation is cheap, a missed compromise isn't.
- Always investigate the creator on the malicious path, not just the created account.
- Defensive writing with the client: "an account creation we could not match to a request,"
  never "you were breached." Never invent ticket references.
```
