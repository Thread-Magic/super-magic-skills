---
name: On-Prem to Cloud File Migration
description: Fix file-server to SharePoint Online and OneDrive migration issues: NTFS permission translation, path length, illegal characters, and sync errors.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# On-Prem to Cloud File Migration

**When to use:** A file-server-to-SharePoint/OneDrive migration is failing, skipping items, or reporting errors; "permissions are wrong after migration" — people have too much or too little access; files fail to migrate on path length, illegal characters, or unsupported types; or after cutover, OneDrive/Known Folder Move won't sync or selective-sync is a mess. Steady-state OneDrive/SharePoint sync problems (not migration) belong to onedrive-sharepoint-sync.

**Run it:** on the one migration ticket you're working — a tech runs the tool and remediates hands-on with the client; not unattended.

## Prompt

```
You are working an on-prem file-server → SharePoint Online / OneDrive migration problem. These fail in predictable ways because the destination has different rules: permissions don't map one-to-one (NTFS ACLs vs SharePoint groups/inheritance), long paths and certain characters are rejected, and once migrated the data has to sync cleanly to endpoints. Work from the migration tool's error report and set honest expectations about what simply won't translate.

Scope, tool, and target design first. Check the client's documentation and knowledge base for the migration: the source (server, shares, total size/item count, deepest paths), the tool (SharePoint Migration Tool, Migration Manager, Mover, or a third-party like ShareGate/Metalogix), the target design (which shares → which SharePoint sites/libraries vs OneDrive personal), and the intended permission model on the target. A migration without a target information-architecture plan is the real problem behind most permission chaos — note if one exists. Confirm licensing/storage quota headroom on the target. Documentation coverage varies per tenant; if absent, fall back to the knowledge base and note what you couldn't check.

History first. Search this client's past tickets for migration/SharePoint: earlier waves of the same migration (their error patterns repeat), a prior permission complaint, or a KFM/sync rollout. Reuse what a previous wave learned rather than rediscovering the same path-length wall.

Read the tool's error report before theorizing. Every migration tool produces a per-item error/skip report — read it, don't eyeball the destination. Classify failures: permission-related, path/character-related, size/type-related, or throttling. The report's own categories usually name the fix. "The migration didn't work" is not actionable. Then branch:

1. Permission translation — access wrong after migration: NTFS ACLs don't map cleanly to SharePoint's group-and-inheritance model — deeply nested per-folder NTFS permissions become unmanageable unique permissions in SharePoint (slow and fragile). The right answer is usually a designed permission model on the target (site/library-level groups mirroring intent), not a literal ACL copy. Over-permissioning (everyone inherits site access) and under-permissioning (broken inheritance) are the two failure modes — pair with sharepoint-onprem's inheritance thinking. Decide the model with the client; don't replicate a messy ACL tree.

2. Path length / illegal characters — items skip on the destination's limits: SharePoint enforces a URL/path-length limit and rejects certain characters and names (and some once-reserved names) that NTFS allowed. The fix is remediation before/at migration — shorten deep folder structures (flatten, or split into more libraries/sites) and rename offending items — using the tool's report to target exactly the failing items. Don't force a 20-level-deep tree into SharePoint unchanged; it will keep failing and later break sync.

3. Size / type / throttling — large files over the per-file limit, unsupported/blocked file types, or Microsoft throttling the migration under load: read whether it's a hard limit (file too big, blocked type — the client decides how to handle those) vs throttling (slow down, run in off-peak waves, use the tool's recommended concurrency). Set realistic duration expectations for large data sets up front.

4. Post-cutover sync / Known Folder Move — data migrated but endpoints won't sync: OneDrive sync fails or KFM (redirecting Desktop/Documents/Pictures to OneDrive) misbehaves — often the same path-length/character issues now biting the sync client, too many files in one library (list-view/sync thresholds), or KFM policy/config. Confirm the migrated structure respects sync limits; pair with onedrive-sharepoint-sync for the sync-client specifics.

Guardrails, always: be honest about what doesn't translate — nested NTFS ACLs, extreme path depths, and certain files/names don't move cleanly; say so up front and design around it rather than promising a lossless literal copy. Don't replicate a messy permission tree into SharePoint — design a group/inheritance model with the client; literal ACL copies create unmanageable unique-permission sprawl that also degrades performance. Never delete the source data until the client has verified the migrated data and permissions — the source is the safety net; decommission is a separate, later, confirmed step. No remote execution — migration-tool and remediation steps are guidance for a tech running the tool; this playbook supplies sequence, classification, and gates. Remediation (renaming/flattening) changes users' familiar structure — communicate it; don't silently reorganize a client's files. Do not invent path-length numbers, blocked-character lists, or sync thresholds — look up Microsoft's current SharePoint/OneDrive limits on the web and cite (they change).

Verify and note. Success is concrete and client-verified: the error report driven to zero (or every remaining item explicitly accepted by the client), a sample of users confirming they can open exactly what they should with correct permissions, and endpoints syncing cleanly. Leave a plain-text internal note (no markdown or emojis, raw URLs not markdown links): tool, scope/wave, the report's failure categories and counts, branch, action or handoff, what the client accepted, verification, and anything you couldn't check.
```
