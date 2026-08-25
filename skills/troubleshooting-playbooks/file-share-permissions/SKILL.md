---
name: File Share Permissions
description: Diagnose access-denied file share tickets by laddering effective permissions across share vs NTFS vs inheritance and group membership, at least privilege.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# File Share Permissions

**When to use:** A user gets Access Denied on a share or folder (or suddenly lost access); a user can see a folder they shouldn't (over-permission report); a new hire can't reach what their role should reach; or after a migration/reorg a team's access is inconsistent.

**Run it:** on the one ticket you're working — a tech ladders the permissions hands-on and confirms authorization; not unattended.

## Prompt

```
Effective access is the intersection of share permissions, NTFS ACLs, inheritance and group
memberships at logon; the ticket is always in the layer nobody checked.

Climb the Troubleshooting Ladder base skill first: past tickets for this share and user: a
migration, move or "cleanup" in the window is the likely cause — a move within a volume
carries its ACLs, a copy inherits the destination's. Then the documented design — naming
convention, which groups grant what here, where the data lives. This ladder is NTFS/SMB;
cloud shares follow their platform's model, and no documented design is itself the
follow-up. Pin the failing operation — read, write, delete or traverse — with the exact path
and error: "can open but not save" and "can't see it" are different layers.

Ladder them:
1. Share permissions — the ceiling: a share granting Read caps everyone at Read whatever
   NTFS says. The common design is a broad share grant with NTFS doing the real control —
   verify this client's.
2. NTFS ACLs — the actual grants. Compute effective access with the Effective Access tool,
   not by eye, and look for explicit Deny: one Deny overrides any number of Allows and
   answers most mystery tickets.
3. Inheritance — broken mid-tree explains "has the parent but not this subfolder". Check
   whether the folder inherits, and whether an earlier fix disabled it (it usually did).
   Re-enabling widens access — review what flows down first.
4. Group membership and the token — memberships versus what the ACL grants, nested included.
   Membership reaches the token only at next logon, so "added an hour ago and it still
   fails" is fixed by a logoff and logon, not more ACL edits; AD replication lag does the
   same. Check both before re-fixing.

Over-permission runs the ladder backwards: effective access names the group admitting them;
fix that membership or grant. Unexplained broad grants (Everyone, Domain Users,
Authenticated Users on sensitive paths) get reported to the client contact, not silently
tightened — a process may depend on the hole, but that gets decided, not ignored.

Fix through the design, at least privilege: add the user to the documented role or resource
group. Per-user ACL entries are the anti-pattern that created this mess: refuse them unless
no group fits, and flag the design gap. Never grant Everyone, Authenticated Users or Full
Control to close a ticket. Access to sensitive shares (HR, finance, exec) needs the data
owner's or manager's confirmation per client practice: the ticket request alone is not
consent, so ask. Deny entries, inheritance flips and bulk ACL changes have wide blast radius
— prefer the narrowest fix for the pinned operation.

Verify with the user doing the failing operation after a fresh logon. Note it (PSA Note
Discipline base skill): layer, effective-access evidence, the fix and whose authorization,
findings for follow-up.
```
