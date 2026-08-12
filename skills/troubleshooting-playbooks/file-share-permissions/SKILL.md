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
Effective access is the intersection of layers — share permissions, NTFS ACLs, inheritance, and the user's group memberships at logon time — and the ticket is always in the layer nobody checked. Ladder them in order and ban the classic bad fixes (Everyone/Full Control, per-user ACL sprinkling).

Work it in this order:

1. History first. Search past tickets for this share/folder and this user. A migration, folder move, or "cleanup" ticket in the window is the likely cause (moves within a volume carry ACLs; copies inherit the destination's — a folder that moved keeps stale permissions). A recent similar per-user fix suggests the group design is being bypassed — hold that for the fix step.

2. Docs second. Check the client's documentation and knowledge base for the permission design: the group-naming convention (role groups -> resource groups -> ACLs), which groups grant what on this share, and where the data lives (on-prem NTFS, or SharePoint/cloud — cloud shares follow the sharing-model of that platform; this NTFS ladder applies to SMB shares). Documentation coverage varies per tenant — note when no permission design is documented; that absence is itself the follow-up.

3. Pin the failing operation. Read vs write vs delete vs traverse — "can open the folder but not save" and "can't see the folder at all" are different layers. Get the exact path and the exact error.

4. Ladder the layers — in this order:
   - Share permissions — the ceiling for network access. A share granting Read caps everyone at Read regardless of NTFS. Check the share-level grants first; the common design is a broad share grant with NTFS doing the real control — verify which design this client documents.
   - NTFS ACLs — the actual grants on the folder/file. Guide the tech to read the ACL and compute effective access for the user (the Effective Access tool exists for exactly this) rather than eyeballing entries. Watch for explicit Deny entries — a single Deny overrides any number of Allows and is the answer to many mystery tickets.
   - Inheritance — broken/blocked inheritance mid-tree explains "has access to the parent but not this subfolder." Check whether the folder inherits, and whether someone disabled inheritance during a past fix (they usually did). Re-enabling inheritance can widen access — review what would flow down before flipping it.
   - Group membership and the token — the user's memberships versus what the ACL grants; nested groups included. Freshness matters: membership changes only land in the user's token at next logon — "I was added an hour ago and it still fails" is fixed by logoff/logon (or lock the workstation for Kerberos refresh per current guidance), not more ACL edits. AD replication lag between DCs adds the same false-negative — check before re-fixing.

5. Diagnose over-permission the same way, reversed. For "shouldn't see this": find which grant admits them (effective access names the group), then fix the membership or the grant — and treat unexplained broad grants (Everyone, Domain Users, Authenticated Users on sensitive paths) as findings to report, not just this ticket's fix.

6. Fix with least privilege, through the design. The correct fix is almost always group membership: add the user to the documented role/resource group. Per-user ACL entries are the anti-pattern that created this mess — refuse them unless the client's design has no fitting group, and then flag the design gap. Verify authority before granting: access changes to sensitive shares (HR, finance, exec) need the data owner's/manager's confirmation per the client's practice — request it rather than assuming the ticket itself is authorization.

Guardrails to hold throughout: never grant Everyone/Authenticated Users/Full Control to make a ticket go away — least privilege through the documented group design, and flag it when no design exists. Authorization before access: membership adds to sensitive resources require the data owner or manager sign-off per client practice — the ticket request alone is not consent. Deny entries, inheritance flips, and bulk ACL changes are high-blast-radius: review what changes downstream before recommending, and prefer the narrowest change that fixes the pinned operation. Remember token freshness — verify after logoff/logon before concluding a correct fix "didn't work" and stacking more grants. No remote execution — ACL reads and changes are performed by the tech; you supply the ladder and gates. Over-permission discoveries are security findings: report them to the client contact per practice rather than silently tightening (business processes may depend on the hole — but it gets decided, not ignored).

Verify and note. The user performs the exact failing operation after a fresh logon. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): layer identified, effective-access evidence, fix (which group, whose authorization), any findings (Deny entries, broken inheritance, broad grants) flagged for follow-up.
```
