---
name: Group Policy Troubleshooting
description: Diagnose "GPO not applying" — drive mappings, lock screens, software installs, security settings missing — by reading gpresult output and walking the scope/filtering/inheritance ladder before touching any policy.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, liongard_launchpoint, liongard_metric, liongard_timeline, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Group Policy Troubleshooting

**When to use:** A user's drive mappings, printers, or desktop settings didn't apply; a new GPO was created but machines aren't picking it up; settings apply to some users/machines but not others; or "Group Policy processing failed" events (1058, 1030, 7016, 8194) show up in the ticket.

**Run it:** on the one ticket you're working — a tech reads gpresult hands-on and makes targeted changes with the AD owner aware; not unattended.

## Prompt

```
The rule of this playbook: a GPO "not applying" is almost never a broken GPO — it is scope, filtering, inheritance, slow-link, or replication. Get a gpresult report and read which of those it is before proposing any edit.

Work it in this order:

1. History first. Search this client's past tickets on GPO/drive-mapping/policy symptoms. One machine -> local processing problem. Many machines since a date -> a policy or infrastructure change on that date; ask what changed (new GPO, DC work, VPN change) before anything else.

2. Docs second. Check the client's documentation and knowledge base for the AD layout: OU structure, naming convention for GPOs, which DCs exist, and whether users work over VPN (slow-link matters). If Liongard's Active Directory inspector is enabled, confirm it last ran clean, then use its inspector data and change timeline for GPO inventory and recent GPO changes — state the dataprint age. If Liongard is absent, rely on the documentation and the tech's console access. Documentation and Liongard coverage varies per tenant — note anything you could not check.

3. Get the report before theorizing. Guide the tech to run gpresult /h report.html (as the affected user, on the affected machine; /scope computer needs elevation) or gpupdate /force then gpresult. The report is the truth: Applied GPOs, Denied GPOs with the reason, and the processing time/link speed.

4. Read the Denied reason — it names the branch:
   - Not in scope (GPO absent from both lists) — the GPO isn't linked to an OU in the user's/computer's path. Verify which OU the object actually sits in (users moved between OUs is the classic). Fix is linking or moving the object per the client's OU convention — confirm with the client's AD owner before moving anything. Escalate when the OU design itself is the problem (flat OU, everything in the default Computers container — computers there get no OU-linked GPOs).
   - Denied (Security Filtering) — object isn't in the filtered group, or (post-MS16-072) "Authenticated Users" / "Domain Computers" lost Read on the GPO. Check group membership AND delegation-tab Read. Escalate when the filtering group is managed by another team or an IAM tool.
   - Denied (WMI Filter) — the WMI filter evaluates false on this machine (OS version filters go stale after upgrades). Test the WMI query on the machine before concluding.
   - Denied (Blocked / overridden) — Block Inheritance on the OU, or a higher Enforced GPO wins, or "loopback processing" changes which user settings apply on that machine (RDS/AVD hosts almost always use loopback — check before declaring a user GPO broken there). Map the precedence in the report's order; do not guess.
   - Slow link detected — report shows a slow link or the settings that failed are the bandwidth-gated types (software install, folder redirection, scripts, drive maps under some configs), typical on VPN. These only apply on fast links or at logon over fast links. Set expectations honestly: the fix is policy design (item-level targeting, Always On VPN timing), not repeated gpupdate.
   - Processing errors (events 1058/1030: cannot read gpt.ini/SYSVOL) — this is not a GPO problem, it is SYSVOL access or replication. Check whether the machine can reach \\<domain>\SYSVOL, and compare the GPO's version on two DCs (or check DFSR health). If versions differ across DCs -> hand off to the ad-replication-issues playbook; do not edit the GPO to "fix" it.

Guardrails to hold throughout: never edit, unlink, or re-permission a GPO as an exploratory step — every change hits every object in scope. Diagnose read-only; make one targeted change with the client's AD owner aware. Never enable Block Inheritance or Enforced to "make it work" — that trades one mystery for a permanent one. gpresult/gpupdate are guidance for the tech or an attended user — you never run remote script execution from here. If the same GPO shows different versions on different DCs, stop: that is replication, not policy — route to ad-replication-issues. Do not recite policy CSE behavior from memory when it decides the diagnosis — verify against Microsoft's current docs on the web, especially for drive-map/loopback/slow-link rules.

Verify and note. After the fix, gpupdate /force, sign out/in (user settings) or reboot (computer settings — some, like software install, only apply at boot), then a fresh gpresult showing the GPO in Applied. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): symptom, gpresult finding (denied reason or event IDs), branch, action taken or handed off, verification result.
```
