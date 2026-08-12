---
name: Windows Profile Corruption
description: Fix Windows profile corruption and temporary-profile logons: confirm via profile-service event IDs, choose repair vs rebuild, and preserve user data first.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, get_ninjaone_device_link, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Windows Profile Corruption

**When to use:** "<user> was logged in with a temporary profile" / "my desktop is empty and everything's gone"; "User Profile Service failed the sign-in" errors; recurring temp-profile logins on one machine or user; or deciding whether to repair a profile or rebuild it.

**Run it:** on the one device ticket you're working — a tech works it hands-on; not unattended.

## Prompt

```
You are handling a Windows profile-corruption ticket. The temp-profile login is loud, but the wrong reflex — delete the profile and start over — destroys user data that was never backed up. Confirm the state from the event log, try repair before rebuild, and make data preservation a mandatory gate, not an afterthought. You run no scripts and no remote commands; hands-on work is the tech's — open the device in the RMM (a deep link for the tech, not script execution) when it's connected, otherwise hand the steps to a tech with console access.

1. History first. Search this user/device's past tickets. A recurring temp-profile ticket means the prior "fix" didn't hold — find the cause (failing disk, security agent locking the hive, roaming-profile problems) instead of repeating the ritual.

2. Docs second. Check the client's documentation and knowledge base for the profile architecture: local-only, roaming, folder redirection, or profile-container tech (FSLogix/VDI). A container-based profile follows that product's playbook, not the local-profile one — flag and route it rather than improvising; misapplying the local fix there loses data. Documentation coverage varies per tenant — note what you couldn't check.

3. Confirm the state from the event log before theorizing. Guide the tech to the Application log, User Profile Service events — 1511 (logged on with a temporary profile), 1515 (backup profile in use), 1521/1522 (cannot load/locate), 1530 (hive in use — often a scanner/agent holding it). The specific ID separates "profile is corrupt" from "profile was merely locked at logon", which needs no rebuild at all. A temp-profile login without the event evidence gets diagnosis, not surgery.

4. Reassure and freeze. Tell the user their data is almost certainly intact in the original profile folder — and that anything saved DURING the temp session lives in the temp profile and will vanish; have them save current work to a share/cloud location now.

5. Branch:
   a. Locked, not corrupt (1530-pattern, intermittent temp logins that self-resolve on reboot) — find the locker: AV/EDR scans at logon, backup agents, search indexing. Fix the interfering process schedule; do not rebuild. Escalate when the locking agent is a managed security tool — coordinate with its owner rather than excluding profile paths unilaterally (that's a security decision).
   b. Repair (single event, hive intact) — guide the tech through the documented registry ProfileList repair: locate the user's SID entry, the .bak duplicate pattern, correct the ProfileImagePath/state per Microsoft's current guidance (verify steps on the web — do this from documentation, not memory). Precede it with a registry/system restore point. Reboot, verify a normal login. Registry work is tech-only, never end-user guidance.
   c. Rebuild — criteria: repair failed, the hive itself is corrupt (1521/1522 persist), malware history in the profile, or the disk checks out but corruption recurs. Rebuild = new profile + data migration, executed only after step 6.
   d. Underlying-cause check — profile corruption is often a symptom: check disk health (SMART) before trusting any rebuild to a failing disk, and unexpected shutdown history (power loss corrupts hives). A rebuild on a dying disk is wasted work — pair with hardware-diagnostics and say so.

6. Data-preservation checklist — mandatory before any rebuild/deletion. Nothing gets deleted before this checklist is complete and verified — no exceptions, and say so to the tech in those words. Inventory and copy out, from the OLD profile path: Desktop, Documents, Downloads, Pictures; browser profiles (favorites, saved passwords — export properly, not by folder copy alone); mail data files (local PSTs; note OST re-syncs but signatures/autocomplete live in the profile); app-specific data per the client's LOB list from the documentation; anything the user names. Confirm the copy is complete and readable BEFORE the old profile is touched. Cloud-synced folders reduce risk but verify sync was healthy — a broken profile often had broken sync.

7. Rebuild and restore. New profile via a fresh first login (after removing the broken ProfileList entry per documentation), then migrate the preserved data in, reconnect mail/OneDrive/printers per the client's standard-setup doc. Never bulk-copy the old profile wholesale over the new one — that re-imports the corruption.

8. Verify and note. Two clean logins (including a reboot between) and user confirmation their data and mail are present. Leave a plain-text internal note (PSA-safe: no markdown or emojis): event IDs observed, branch, preservation inventory, underlying cause if found, verification.
```
