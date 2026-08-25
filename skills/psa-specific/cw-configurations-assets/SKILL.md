---
name: CW Configurations Assets
description: ConnectWise Manage configurations (assets): link tickets to the right config, follow the desk's config-type taxonomy, and flag stale or duplicate configs.
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
You are keeping ConnectWise configuration (asset) linkage clean. Configurations are asset
records — workstations, servers, firewalls, printers, licenses — under a tenant-defined
configuration-type taxonomy, attached to companies and tickets. A linked ticket gives the next
tech the device history; an unlinked one orphans it. Configs also rot: RMM-synced records
update themselves, manual ones don't, and desks accumulate duplicates and
inactive-but-not-retired records.

1. Re-read the ticket at full detail and identify the device the work actually concerns, from
   the description, notes and contact rather than the title. The company or contact may have
   been corrected ConnectWise-side since your last read.

2. Find the config. Visibility varies by tenant: use config data on the synced ticket or
   company, otherwise search the desk's documentation platform (IT Glue or Hudu, when
   connected) for the asset record and confirm the client. If nothing shows configs, say
   "configuration data not visible from Thread" and hand the linking to a tech in ConnectWise;
   with no docs integration connected either, run advisory-only from ticket text and say so
   (apply the Connector Degradation skill).

3. Match on serial number or asset tag first, hostname second, friendly name last — hostnames
   get reused and machines get renamed. A wrong link is worse than no link: below high
   confidence, or where two configs match, report the candidates and ask instead of linking,
   flagging the pair as a probable duplicate for step 6.

4. Config types are tenant-defined — the desk decides whether Firewall and Router are one type
   or two. Never invent one; use only types evidenced in the desk's records or documented
   taxonomy, and route taxonomy changes to a taxonomy cleanup.

5. Where the tenant's sync supports it, associate the ticket with the config; otherwise record
   the intended linkage in a note ("Concerns config: <device> — link in ConnectWise") so a tech
   can finish it. Either way the note names the device and why.

6. Stale-config hygiene — flag, don't fix. Signals: a last-seen date far in the past on an
   RMM-synced config, an active ticket against a config marked inactive, the step 3 duplicates,
   configs attached to departed contacts. Collect them into a hygiene note for a human. Never
   retire, merge or deactivate a config from Thread; that is ConnectWise-side work with billing
   and agreement implications.

7. Output the config identified (or the honest "not visible"), the linkage made or
   recommended, and every hygiene flag with its evidence.

ConnectWise is master for config records; Thread and the docs platforms mirror it. Where a docs
platform disagrees, ConnectWise wins — note the drift. Never invent config names, types,
serials or IDs. Notes syncing to ConnectWise are plain text, no markdown or emojis (PSA Note
Discipline skill).
```
