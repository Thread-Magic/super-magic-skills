---
name: NAS / File Share Provisioning
description: Plan and document a new network share — folder structure, permission model, quota, backup inclusion — with an approval gate on the access model first.
category: Devices & Infrastructure
tools: [search_itglue, search_knowledge_base, search_ninjaone_devices, create_ticket, add_ticket_note, send_approval]
connectors: [IT Glue, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# NAS / File Share Provisioning

**When to use:** "Create a new share for the <department> team", provisioning a project/department folder, or restructuring an ad-hoc share into a proper permission model.

**Run it:** on one provisioning ticket, on demand (not a Flow — the access model routes through human approval).

## Prompt

```
Stand up a new file share right the first time: a sane folder structure, a permission model tied to groups (not individuals), a quota, and confirmed backup inclusion — with the access model signed off before anyone grants it. This skill designs and documents; it does not create shares or modify permissions.

1. Gather requirements: the host (NAS model or file server), the share's purpose, who needs access and at what level (read / read-write / full), expected size/growth, retention needs. Pull the client's storage/permission convention from the documentation (IT Glue) and any standard from the knowledge base; confirm the host exists and is healthy in the RMM.
2. Design the folder structure per the client convention — top-level share plus subfolders that map to how the team actually works, avoiding deeply nested exceptions that break inheritance.
3. Design the permission model on groups, not individuals: define the security groups (read-only, contributor, owner), map each to the folders, and rely on inheritance with the fewest possible break-inheritance exceptions. List exactly which group gets which right on which folder.
4. Set a quota appropriate to purpose and expected growth, and define the alert threshold — cross-reference storage-capacity-planning so the share is tracked against the host's headroom.
5. Confirm backup inclusion: verify the new share's path falls within an existing backup job's scope, or flag that a backup job must be extended to cover it. A share not in a backup is a hard finding — cross-reference backup-failure-triage for verifying the job actually runs.
6. Gate the access model before creation: route the folder structure + permission map for approval so a human authorizes the access grants. Do not represent share creation or permission changes as something this skill performs.
7. On approval, the tech creates the share and applies permissions in-console. Update documentation with the share path, permission model, quota, owner, and backup job. Output the provisioning plan and leave it as a plain-text note (no markdown/emojis) or open a ticket.

Guardrails: access-control changes require explicit sign-off before any grant. Permissions are assigned to groups, never to individual users; call out any requested individual grant as an exception to reconsider. Never provision a share without confirming it will be backed up — flag missing backup coverage as a blocker. Do not invent the client's group-naming or folder convention; if none is documented, propose one and mark it as proposed, not established.
```
