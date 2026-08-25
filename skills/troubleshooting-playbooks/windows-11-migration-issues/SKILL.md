---
name: Windows 11 Migration Issues
description: Handle post-upgrade Windows 11 migration tickets: driver regressions, reset default apps, missing printers, moved features, with rollback window checked.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Windows 11 Migration Issues

**When to use:** "Ever since the Windows 11 upgrade, X is broken" (audio, display, Wi-Fi, dock, LOB app); "my printer disappeared" / "my default PDF app changed" post-upgrade; a machine that refuses to upgrade or was skipped by the rollout (safeguard hold); or a user asking to go back to Windows 10 / a genuinely broken upgrade where rollback is on the table.

**Run it:** on the one ticket you're working — a tech works it and flags wave-level patterns to the rollout owner; not unattended.

## Prompt

```
Two clocks run on a Windows 11 wave: the rollback window, and the pattern clock — three
tickets with the same regression means pause the wave, not fix the fourth machine.

Climb the Troubleshooting Ladder base skill first: past tickets since the wave began —
five naming the same model or driver is a wave problem for the rollout owner, not an
individual fault; documentation for the migration plan: target version, ring schedule,
hardware standards, known-issue log; the exact build, model and current driver version
against what the vendor publishes for Windows 11 on that model; and whether the failure
really correlates with the upgrade date — users attribute everything to it for a month.

Check the rollback clock early: Windows deletes the previous installation after 10 days by
default, sooner if disk cleanup ran. If rollback is likely, priority inherits the
deadline.

1. Driver regression — audio, display, Wi-Fi or dock broken, or an inbox driver that
   replaced the vendor's on upgrade. Install the vendor's current Windows 11 driver for
   this exact model, never third-party sites. Where the vendor publishes none, the
   component may be end-of-support: confirm with the vendor, replace it, or roll back. The
   same driver on several machines is a pause-the-wave flag.

2. Defaults reset and "where did X go" — Settings > Default apps fixes one user, but the
   fleet fix is the deployment setting defaults by policy; escalate to the deployment
   owner when policy-managed defaults don't apply. A moved Start menu or taskbar is a
   training gap: answer it, and have the rollout ship a "what moved" note to the remaining
   rings.

3. Printer rediscovery — re-add from the print server or direct IP per the client's
   documented standard, with the Win11 driver; escalate when no Win11 driver exists.

4. LOB app breakage — check the vendor's Windows 11 support statement for the version in
   use; an unsupported combination is the first suspect, and an app upgrade conversation
   with client and vendor.

5. Upgrade refused or skipped — a safeguard hold or unmet hardware requirement; the
   readiness report says which. Never bypass holds or hardware checks with registry or
   media tricks on a managed fleet: the hold exists because something breaks, and
   ineligible hardware goes on the refresh list.

6. Rollback — materially broken, no fix inside the window. Verify eligibility, confirm
   with the user what returns and what does not (anything created since the upgrade may be
   lost), and get the client contact's explicit go-ahead. Past the window it is a reimage
   with data-preservation planning.

Verify the broken thing works — sound plays, the printer prints — not just that it boots.
Note it (apply the PSA Note Discipline base skill): upgrade date, build, branch, versions
before and after, the fix or rollback decision and who approved, any wave pattern.
```
