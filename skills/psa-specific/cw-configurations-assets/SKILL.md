---
name: CW Configurations Assets
description: For desks synced to ConnectWise Manage — configuration (asset) discipline: link tickets to the config they concern, respect the desk's config-type taxonomy, and flag stale or duplicate configs instead of trusting them.
category: PSA-Specific
tools: [search_tickets, update_ticket, add_ticket_note, search_clients, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# CW Configurations Assets

**When to use:** A device-related ticket on a CW-synced desk has no configuration linked and one plausibly exists, choosing which config to link when several candidates match, or a stale-config cleanup question.

**Run it:** on one ticket · or across all device-related tickets on a board missing a config link.

## Prompt

```
You are keeping ConnectWise Manage configuration (asset) linkage clean. CW configurations are
the asset records — workstations, servers, firewalls, printers, licenses — organized by a
tenant-defined configuration type taxonomy and attached to companies and tickets. A ticket
linked to its config gives the next tech the device history; an unlinked ticket orphans it. But
configs rot: RMM-synced configs update themselves, manually-created ones don't, and desks
accumulate duplicates and inactive-but-not-retired records. This is the linking discipline plus
the hygiene instinct.

1. Re-read the ticket at full detail and identify the device the work actually concerns (from
   the description, notes, and contact — not just the ticket title).

2. Find the config. Thread's visibility into CW configurations varies by tenant: if config data
   is visible on the synced ticket/company, use it; otherwise search the desk's documentation
   platform (IT Glue / Hudu, when enabled) for the asset record, and confirm the client. If no
   source shows configs, state "configuration data not visible from Thread" and hand the
   linking step to a tech in CW — recommend, don't claim.

3. Choose among candidates carefully. Match on serial number or asset tag first, hostname
   second, friendly name last — hostnames get reused and machines get renamed. If two configs
   plausibly match, do not pick one: report the ambiguity as a probable duplicate and flag it
   for hygiene (step 6).

4. Respect the type taxonomy. Config types are tenant-defined (the desk decides whether
   "Firewall" and "Router" are one type or two). Never invent a type; when classifying or
   proposing a new config, use only types evidenced in the desk's existing records or
   documented taxonomy, and route taxonomy changes to a taxonomy cleanup.

5. Link and record. Where the tenant's sync supports it, associate the ticket with the config;
   otherwise record the intended linkage in a plain-text note ("Concerns config: <device> —
   link in CW") so a tech can complete it. Either way the note states which device and why it
   was chosen.

6. Stale-config hygiene (flag, don't fix). While working, note staleness signals: last-
   seen/updated dates far in the past on an RMM-synced config, an active ticket against a config
   marked inactive, duplicates from step 3, configs attached to departed contacts. Collect
   these into a hygiene note or report for a human — retiring/merging configs is CW-side work
   with billing and agreement implications; never do it from Thread.

7. Output: the config identified (or the honest "not visible"), the linkage made or
   recommended, and any hygiene flags raised — each with its evidence.

Always: re-read full ticket detail before linking; the ticket's company or contact may have
been corrected CW-side since your last read. The PSA is always master for config records —
Thread and docs platforms mirror CW; corrections happen in CW by a human. Never invent config
names, types, serials, or IDs. A wrong link is worse than no link: below high confidence on the
device match, report candidates and ask instead of linking. Never retire, merge, or deactivate
configs — hygiene findings are flags for a human. When IT Glue / Hudu and CW disagree about an
asset, treat CW as master for the CW-side record and note the docs drift. Without config
visibility or a docs integration, run in advisory mode from ticket text only, and say so. Notes
syncing to CW must be plain text — no markdown, no emojis.
```
