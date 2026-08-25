---
name: Sage 50 / Sage 100
description: Diagnose Sage 50 and Sage 100 problems: data-path faults, share permissions, Pervasive/Actian PSQL engine service, and multi-user access errors at close.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Sage 50 / Sage 100

**When to use:** Workstations can't connect to / open the company data, Pervasive/Actian PSQL or "Btrieve" status-code errors appear or the engine service is down, one workstation opens the company but others can't (multi-user broke after a change), or there's slowness/lock errors during month-end/year-end close.

**Run it:** on the one ticket you're working — a tech works it hands-on with the finance lead aware; not unattended.

## Prompt

```
Sage 50 and Sage 100 sit on a shared data path served by the Actian/Pervasive PSQL engine,
so most "Sage is broken" tickets are the data path, the engine service, or share
permissions.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: a recent
Sage or PSQL upgrade (a version mismatch between the server and workstation engines is a
classic break), a server IP or name change, a permissions, GPO or antivirus change.
Documentation: Sage 50 versus 100 and version, which machine hosts the data and the exact
path (UNC versus mapped drive — Sage is picky), the PSQL version, and whether the host runs
the engine in server mode. If Liongard covers the tenant, read service and share state from
it and date the dataprint (Inspector Read Discipline base skill). Evidence: the verbatim
Sage error or PSQL status code — 3xxx, 94 and 116 each mean something specific, so map it
to Actian's documented meaning.

1. Data path / connection — workstations can't find the company. The path config points at
   a stale server name or IP, or an inconsistent mapped drive. Confirm the host resolves by
   name and the path matches the documented one on every workstation. A host IP change from
   DHCP breaks everyone; the fix is a reservation, not a re-point.

2. Actian/Pervasive engine — engine errors or the service down. Confirm the service runs on
   the host in server mode (workstations run the workgroup engine; a mode or version
   mismatch is a top cause) and that server and workstation PSQL versions are compatible.
   Escalate when the engine won't start or reports database-level corruption — a vendor
   case, company data integrity at stake.

3. Permissions — one user in, others out, or read-only behavior. Share and NTFS
   permissions on the data folder must give those users full control; Sage writes lock and
   temp files there. Grant the intended group the rights it needs, never Everyone-Full.

4. Multi-user locking under load — lock errors or slowness at close: concurrent posting,
   antivirus scanning the live data files, or a workstation that crashed holding a lock. Exclusions for the data folder and engine are the vendor recommendation; request
   them through the security owner, never disable antivirus.

This is live accounting data, often mid-close: warn the finance lead before anything that
risks data state and schedule disruptive steps outside posting windows.
Restarting the engine disconnects every Sage user — confirm nobody is posting first. Never
hand-edit or repair company data files, and never delete lock or temp files while users are
in the company; corruption beyond Sage's own tools is a vendor case. Success is a second workstation opening the company in multi-user mode and
posting a test action. Note in plain text (PSA Note Discipline base skill): versions and
engine mode, path, status code, branch, action, verification.
```
