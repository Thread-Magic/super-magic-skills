---
name: Group Policy Troubleshooting
description: Diagnose GPO not applying — missing drive mappings, lock screens, software installs — by reading gpresult and walking scope, filtering, and inheritance.
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
A GPO "not applying" is almost never a broken GPO — it is scope, filtering, inheritance,
slow link, or replication. Name which before proposing any edit.

Climb the Troubleshooting Ladder base skill first: past GPO and drive-mapping tickets,
the client's documented AD layout (OU structure, GPO naming, DCs, VPN users), and scope
— one machine is local processing, many since a date is a change. With the Liongard
Active Directory inspector on, read its GPO inventory and change timeline, dated.

Then get the report: gpresult /h report.html as the affected user on the affected
machine (/scope computer needs elevation). Applied GPOs, Denied GPOs with their reason,
and link speed are the truth — the Denied reason is your branch:

1. Not in scope (in neither list) — no link to an OU in the object's path. Check which
   OU it actually sits in; users moved between OUs is the classic. Fix by linking or
   moving per the client's OU convention. Escalate when the OU design itself is the
   problem: a flat OU, or computers left in the default Computers container, which gets
   no OU-linked GPOs.

2. Denied (filtering). Security Filtering: the object isn't in the group, or
   post-MS16-072 Authenticated Users / Domain Computers lost Read on the GPO — check
   membership AND Read on the delegation tab. WMI Filter: the query evaluates false
   here; OS-version filters go stale after upgrades, so test it on the machine. Escalate
   when another team or an IAM tool owns the group.

3. Denied (blocked or overridden) — Block Inheritance on the OU, a higher Enforced GPO,
   or loopback changing which user settings apply. RDS and AVD hosts almost always use
   loopback; check that before calling a user GPO broken.

4. Slow link — the report says so, or the failing settings are the bandwidth-gated
   types: software install, folder redirection, scripts, some drive maps. Typical over
   VPN; the fix is policy design (item-level targeting, VPN timing), not repeated
   gpupdate.

5. Processing errors — events 1058/1030, cannot read gpt.ini from SYSVOL. That's SYSVOL
   access or replication, not policy: check the machine reaches \\<domain>\SYSVOL, then
   compare the GPO version across two DCs or check DFSR health. Differing versions is
   replication — hand to ad-replication-issues, don't edit the GPO to "fix" it.

Never edit, unlink, or re-permission a GPO exploratorily — every change hits every
object in scope. Diagnose read-only, then make one targeted change with the client's AD
owner aware; never enable Block Inheritance or Enforced to make it work.

Verify with gpupdate /force, a sign-out for user settings or a reboot for computer
settings (software install only applies at boot), then a fresh gpresult showing the GPO
in Applied. Note it (apply the PSA Note Discipline base skill): symptom, denied reason
or event ID, branch, action, verification.
```
