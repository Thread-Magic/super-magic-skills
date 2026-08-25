---
name: Outlook Search Issues
description: Fix Outlook search returning nothing or incomplete results by isolating local index vs server search and cached-mode window before rebuilding the index.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Outlook Search Issues

**When to use:** Search returns nothing or misses messages the user can see by scrolling; "something went wrong and your search couldn't be completed" / "results may be incomplete"; recent messages (last hours/days) never appear in results; or search works in Outlook on the web but not desktop, or vice versa.

**Run it:** on the one ticket you're working — a tech works it with the user; not unattended.

## Prompt

```
"Rebuild the index" is the last step, not the first: it takes hours, degrades search
throughout, and touches neither common cause — the cached-mode window and
server-versus-local confusion.

Climb the Troubleshooting Ladder base skill first. Versions decide everything here: classic
desktop, new Outlook (search is service-side, so local-index advice is meaningless), Mac or
web; Exchange Online, on-prem or hybrid; cached or online mode, and the documented slider
policy. And history: many users complaining at once on Exchange Online is a Microsoft
service issue — check service health and say plainly only Microsoft can fix their index.

Discriminate first: run the same query in Outlook on the web. Web finds it, desktop doesn't:
a local problem, index or cached window. Neither finds it: the item is outside the mailbox
or the service index has a gap — stop blaming the machine.

Branch:
1. Cached-mode window — older mail missing. Cached mode syncs only the slider window (often
   12 months), so desktop search of the local copy misses older items unless it extends to
   the server. Check the slider and whether results offer find-more-on-the-server. Either
   widen it (bigger OST, longer sync) or teach the server-results behavior, per client
   standard. Not an index problem — do not rebuild.
2. Recent items missing — indexing backlog. Read indexing status for items remaining: a big
   number that shrinks is normal after a new profile or OST change. One that never shrinks
   means the Windows Search service — branch 3.
3. Errors or zero results on a healthy mailbox — confirm the Windows Search service runs and
   Outlook isn't missing from the indexing locations (silently absent after some updates).
   Correlate onset with a recent Office or Windows update and search the web for that build
   plus symptom — the honest answer may be a known issue awaiting a Microsoft fix.
4. Damaged index — only after 1 to 3, and only if every criterion holds: web finds what
   desktop can't, indexing status stuck or errored, service healthy, no known issue. Rebuild
   then, warning of hours of degraded search across every indexed app, machine left on. Once
   only; if it doesn't hold the fault is elsewhere — hand to the Outlook client playbook.
5. Online mode, including session hosts — search runs server-side, so index-rebuild advice
   is a category error there. Slow or failing search is reachability, latency or host
   config: pair with the RDS/AVD or Citrix playbook.

Never recreate the profile or OST for a search complaint before the web-vs-desktop test —
client-repair territory, and overkill for a cached-window case.

Verify the failing query returns the missing item in the user's own Outlook (after a
rebuild, items remaining at zero — possibly next-day). Note it (PSA Note Discipline base
skill): flavour and mode, web-vs-desktop result, branch, action, verification.
```
