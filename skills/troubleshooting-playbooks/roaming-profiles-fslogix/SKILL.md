---
name: Roaming Profiles & FSLogix
description: Fix FSLogix and roaming-profile failures on session hosts: cannot attach VHD, temp profiles, sign-in hangs, and settings loss via FSLogix log codes.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Roaming Profiles & FSLogix

**When to use:** A user gets a temporary profile or "we can't sign you in" on RDS/AVD/shared PCs, FSLogix throws cannot-attach/open-VHD errors, settings/Outlook/Teams cache are lost moving between session hosts, or sign-ins hang at the profile stage after a storage or permissions change.

**Run it:** on the one ticket you're working — a tech works the file server/host console hands-on; not unattended.

## Prompt

```
Most FSLogix incidents are one story: the container is locked by a session elsewhere, real
or orphaned, or the share is unreachable. Find who holds the VHD open before suspecting
the container — deleting a container is deleting the user's profile.

Climb the Troubleshooting Ladder base skill first: one repeat user points at their
container, many at once at the share, permissions, storage or a bad host — check last
night for a host crash, storage failover or a permissions "hardening". From the client's
documentation: Profile container, ODFC or both, VHDLocations, Cloud Cache, storage
backend. A Profile failure breaks the whole profile; ODFC-only just empties the Outlook
and Teams cache. Check the FSLogix build against known-issue lists, then take the status
and error codes verbatim from the Profile/ODFC operational log for that sign-on.

1. Locked container — attach fails, "process cannot access". Open files/handles on the
   file server, or the storage platform's handle view, names the holder. A live session is
   not a bug; recurring concurrent sessions need a design answer (Cloud Cache, session
   limits) from the infra owner. A dead host is an orphaned lock: close the handle or
   break the Azure Files lease, and delete nothing. Escalate when locks recur without
   crashes.

2. Share/permission failure — access denied for many, often after storage work. Confirm
   VHDLocations resolves and the documented share/NTFS model still grants create-and-own;
   a "remove Everyone" hardening breaks new container creation while existing users keep
   working. Escalate when the storage platform's identity config is owned elsewhere.

3. Temporary profile while FSLogix looks healthy — check include/exclude group membership
   against the design, and for a stale local profile on that host; the supported cleanup
   removes the local profile, not the container.

4. Slow or bloated container — content, not attach: browser and Teams caches with no size
   discipline. Redirections.xml exclusions and ODFC scoping fix it, as a proposed change.

5. AV or backup interference — random attach failures or corruption. Verify the vendor's
   documented exclusions for VHD/VHDX paths and FSLogix processes on hosts and storage.

Rebuild only with consent: rescue data by mounting a copy read-only, then rename the
container — never delete — and only after the client acknowledges in the ticket what a
fresh profile loses (app settings, local caches, anything not redirected). Keep the
original until the user confirms nothing is missing. Never break a lock blind, and never
edit shared FSLogix GPO, registry or redirections config to fix one user.

Success is a fresh sign-in with the real profile attached and a clean handle view. Note it
(apply the PSA Note Discipline base skill): container type, log status and error verbatim,
lock holder, branch, action or escalation, verification.
```
