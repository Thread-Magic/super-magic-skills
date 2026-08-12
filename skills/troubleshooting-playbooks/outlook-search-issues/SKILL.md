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
You are diagnosing an Outlook search problem. "Rebuild the index" is the last step, not the first — a rebuild takes hours, degrades search the whole time, and doesn't touch the two most common causes: the cached-mode window and server-vs-local search confusion. Diagnose which search engine answered and what population it searched.

Version identification first. Which Outlook? Classic desktop (Win32), new Outlook (search is service-side — local index advice is meaningless there), Mac, or web. Account type: Exchange Online / on-prem / hybrid, and cached mode vs online mode. Get this from File → Office Account + account settings, or the tell in behavior. Check the client's documentation and knowledge base for the standard (cached-mode slider policy, new-Outlook rollout state); documentation coverage varies per tenant — if absent, fall back to the knowledge base and note what you couldn't check.

History first. Search this user's and the client's past tickets: search complaints across many users at once on Exchange Online → likely a Microsoft service issue (check service health; if the index is Microsoft's, only Microsoft fixes it — be honest). One user, one machine → continue.

Reproduce with a discriminating test before theorizing. Have the user run the same query in Outlook on the web. OWA finds it + desktop doesn't → local problem (index or cached window). Neither finds it → the item is outside the mailbox (deleted, archived elsewhere) or a service-side indexing gap — stop blaming the client machine. Then branch:

1. Cached-mode window (the classic: "older mail missing from search") — cached mode only syncs the slider window (often 12 months by default) locally; classic desktop search against the local copy misses older items unless it extends to the server. Check the "Download Email for the past:" slider and whether results show the "find more on the server" affordance. Fix options honestly: widen the slider (bigger OST, sync time) or teach the server-results behavior — per client standard, not personal preference. This is not an index problem; do not rebuild.

2. Recent items missing (last hours/days) — indexing backlog: check Search → Indexing Status (or File → Options → Search) for "items remaining". A large number that shrinks = let it finish (after big OST changes/new profile this is normal — set expectations). A number that never shrinks → Windows Search service state, then branch 4.

3. Search errors / zero results with healthy mailbox — verify Windows Search service running; check whether Outlook is excluded from indexing locations (Indexing Options → Modify — Outlook silently absent is a known state after some updates); check for a recent Office/Windows update correlating with onset (search the web for the exact build + symptom — search regressions ship in updates regularly and the honest answer may be "known issue, fix pending from Microsoft").

4. Index actually damaged (only after 1–3 exhausted) — rebuild criteria, all required: OWA finds what desktop can't; indexing status stuck/errored; service healthy; no known-issue explanation. Then rebuild (Indexing Options → Advanced → Rebuild), warning the user: hours of degraded search across ALL indexed apps, machine should stay on. One rebuild — if a rebuild doesn't hold, the fix is elsewhere (OST/profile — hand to outlook-client-issues), not a second rebuild.

5. Online-mode / RDS-Citrix twist — online mode (common on session hosts) searches server-side; "index rebuild" advice is a category error there. Slow/failed search in online mode on session hosts = server reachability/latency or the host's config — pair with rds-avd-troubleshooting / citrix-basics.

Guardrails, always: never lead with an index rebuild, and never run more than one — a second rebuild for the same symptom means the diagnosis is wrong. Never recreate the Outlook profile or OST for a search complaint without the OWA-vs-desktop discrimination done first — profile surgery is outlook-client-issues territory and overkill for cached-window cases. Cached-slider changes affect OST size and sync duration — set expectations and follow the client's standard slider policy. New Outlook and online mode have no meaningful local index — do not give local-index advice there. Service-side indexing problems are Microsoft's to fix — reference service health honestly instead of churning the endpoint. All settings/rebuild steps are guidance for the tech or attended user — no script execution from here. Verify update-related known issues against current Microsoft documentation/release notes on the web; do not assert a known issue from memory.

Verify and note. Success = the original failing query returning the known-missing item in the user's own Outlook (after full re-index if one ran — verify "items remaining: 0", which may be next-day). Leave a plain-text internal note (no markdown or emojis, raw URLs not markdown links): Outlook flavor + mode, OWA-vs-desktop test result, branch, action, verification and time, and anything you couldn't check.
```
