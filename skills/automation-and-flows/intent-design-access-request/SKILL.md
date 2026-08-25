---
name: Access Request Intent Design
description: Design an access-request intent for folders, distribution lists, and shared mailboxes — capture resource, justification, and approver on intake.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Access Request Intent Design

**When to use:** "Build an intent for folder/DL/mailbox access requests" / "access tickets never say what access or who approved it" / Intent Mining flagged permission/access changes as a top request type.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build an access-request intent that turns "can I get access to the finance folder" into a ticket
carrying the exact resource, the access level, a business justification and the named approver — so
the technician's first action is granting, not chasing. Building intents is admin-only; if you
can't, output the complete written spec for an admin to apply.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate
it; ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5
near-misses from the watch-outs below) and write only on explicit confirmation; do NOT
activate — the admin does that once the tests pass.

Spec:
- Triggers: "need access to", "can I get access", "add me to the distribution list", "share the
  folder with me", "permission to the shared drive", "access to the shared mailbox", "can't open
  the folder", "add me to the group", "need to see the <department> drive", "request access".
  Watch-outs: "can't open the folder" may be a permissions PROBLEM rather than a request — ask
  which; "add a new user" belongs to the new-hire intent; "the file is corrupted" is
  troubleshooting.
- Arguments: who needs access (the requester, or on behalf of <user>); the exact resource (folder
  path, DL name, shared mailbox, application role, plus the platform if ambiguous); access level
  (read vs edit/full; send-as vs send-on-behalf for mailboxes); a one-sentence business
  justification, required — it is what the approver reads; the named approver (resource owner or
  the requester's manager, per client policy); duration (permanent or time-boxed).
- Reply flow: (1) collect the arguments and confirm the summary, including the exact resource
  string; (2) where policy has the approver sign off first, reply that the request was logged and
  approval is being sought, and carry the approver on the ticket for the desk's approval step; (3)
  create the ticket with a plain-text field block and route it to the access or security board;
  (4) never grant, promise or imply access — "your request has been submitted", not "you'll have
  access shortly".
- Handoff rule: all grants are human or workflow actions after approval. Admin or privileged roles,
  security groups, and another user's mailbox are flagged elevated-risk, never routine.
- Variations per client: approver policy (resource owner vs manager vs central IT), platforms in
  play, whether time-boxed access is the default, the elevated-risk resource list.
- Success metric: first-touch completeness — resource, level, justification and approver all filled.

Guardrails: replies must never state or imply an approval outcome. Do not invent the client's
approval policy or resource names; placeholder (<folder>, <distribution list>) and flag before
activation. Field block in plain text, no markdown (apply the PSA Note Discipline base skill).
```
