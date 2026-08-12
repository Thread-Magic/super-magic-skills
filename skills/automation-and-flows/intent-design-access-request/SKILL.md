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
Build an access-request intent that turns "can I get access to the finance folder" into a
ticket carrying the exact resource, the access level, a business justification, and the named
approver — so the technician's first action is granting, not chasing. Building intents is
admin-only; if you can't, output the complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "need access to", "can I get access",
  "add me to the distribution list", "share the folder with me", "permission to the shared
  drive", "access to the shared mailbox", "can't open the folder", "add me to the group",
  "need to see the <department> drive", "request access". Near-miss watch: "can't open the
  folder" may be a permissions PROBLEM rather than a request — ask which; "add a new user"
  belongs to the new-hire intent.
- Arguments: who needs access (requester, or on behalf of <user>); the exact resource (folder
  path / DL name / shared mailbox / application role, + platform if ambiguous); access level
  (read vs edit/full; send-as vs send-on-behalf for mailboxes); business justification (one
  sentence, required — it's what the approver reads); named approver (resource owner or
  requester's manager per client policy); duration (permanent or time-boxed).
- Reply flow: (1) collect arguments, confirm the summary including the exact resource string;
  (2) if the client's policy says the approver signs off first -> reply that the request was
  logged and approval is being sought; the ticket carries the approver for the desk's approval
  step (the desk's approval action pairs well); (3) create the ticket with a plain-text
  field block, route to the access/security board; (4) never grant, promise, or imply access
  — "your request has been submitted", not "you'll have access shortly".
- Handoff rule: all grants are human/workflow actions after approval. Requests for
  admin/privileged roles, security groups, or another user's mailbox get flagged elevated-risk
  and are never treated as routine.
- Variation hooks (per client): approver policy (resource owner vs manager vs central IT),
  platforms in play, whether time-boxed access is the default, elevated-risk resource list.
- Success metric: first-touch completeness (resource + level + justification + approver
  filled); secondary, median time from request to grant. The win is intake quality.

Steps:
1. List the existing intents — check for an existing access/permissions intent; prefer updating.
2. Search recent access-request tickets; mine phrasing for triggers and the back-and-
   forth for missing-argument candidates; note which resources recur (variation seed).
3. Draft the full spec with the elevated-risk flag rule explicit. Test plan: 5 should-match,
   3–5 should-not (incl. a "can't open file — corrupted" troubleshooting near-miss and a
   new-hire near-miss). Show before any write.
4. On explicit confirmation: create the intent, then set its variations.
5. Report what was created, restate the test plan, recommend activation after tests pass. Do
   NOT activate.

Guardrails: the intent never grants or promises access; replies must not state or imply
approval outcomes. Privileged/admin access and access to another person's data are always
flagged elevated-risk, never routine intake. Do not invent the client's approval policy or
resource names; placeholder (<folder>, <distribution list>) and flag before activation.
Confirm before any write; ticket field block in plain text.
```
