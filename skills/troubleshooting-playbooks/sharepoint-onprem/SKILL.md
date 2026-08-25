---
name: SharePoint On-Prem
description: Diagnose on-premises SharePoint Server: search crawl failures, stale results, content-database mounting, and permission inheritance via ULS crawl logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# SharePoint On-Prem

**When to use:** Search returns stale/missing/no results or a crawl is stuck or failing; a site or content database won't mount or shows unhealthy; a user can't reach a site/library/item they should (or can reach one they shouldn't); or after a patch/upgrade sites are broken with "the farm needs configuration" or a service app is down.

**Run it:** on the one ticket you're working — a tech with farm-admin access works it hands-on; not unattended.

## Prompt

```
On-premises SharePoint Server concentrates its failures in three places: search, content
databases, and permission inheritance. Read the logs before acting. SharePoint Online
belongs to onedrive-sharepoint-sync.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: a recent
cumulative update — and whether PSConfig ran after it — a SQL change, a content-database
move, or a permissions change; broad breakage right after a patch usually means the upgrade
never finished. Documentation: version and build, server roles, the SQL back end and
content-database layout, search topology, and the authentication model. Evidence: for search, the crawl log's per-item errors and the search
service application's health; for a farm or site error, the ULS entry for the correlation ID
on the error page, not the yellow page itself; for content databases, their status in
Central Administration and SQL.

1. Search crawl failures or stale results — read the crawl log. A crawl stopped or paused,
   the crawl account lost access after a password change, the start address is wrong, or
   the index is corrupt. Stale results usually mean the crawl isn't completing: fix the
   account or connectivity and let it finish. Resetting a corrupt index
   is a rebuild-cost decision — set the expectation first.

2. Content database or site down — check its status in Central Administration and SQL, its
   schema version against the farm (a mismatch after a partial patch blocks the mount), and
   free space. Mounting, dismounting and database-level work go through the SQL owner.

3. Permission inheritance — a user can't reach what they should, or can reach what they
   shouldn't. Trace site to library to folder to item and find where inheritance broke and
   unique permissions were set. Fix at that level; never break inheritance further to patch
   one item — unique permissions at scale are unmanageable and slow, and restoring
   inheritance is often the fix. This is groups and inheritance, not NTFS.

4. Post-patch farm config — "the farm needs configuring", services down, or sites erroring
   after an update: the CU installed the binaries but PSConfig never completed on all
   servers. Finishing the upgrade is the documented fix, but it is a farm-level change:
   confirm a backup, plan a window, coordinate. Never run it reactively under pressure.

Never touch SharePoint's databases directly in SQL — editing, detaching or "fixing" a
content database is unsupported and corrupts the farm; act through SharePoint's own tools
and coordinate with the SQL owner. Success is fresh results after a completed crawl, a
healthy content database, or the user reaching exactly what they should. Note in plain text
(PSA Note Discipline base skill): version and build, the correlation ID or crawl-log
evidence, branch, action or handoff, verification.
```
