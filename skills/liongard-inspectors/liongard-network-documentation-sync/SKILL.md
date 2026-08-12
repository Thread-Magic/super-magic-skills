---
name: Liongard Network Documentation Sync
description: Diff what Liongard inspectors see (firewalls, switches, wireless, hypervisors, servers) against the doc platform and draft network-doc corrections.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Liongard Network Documentation Sync

**When to use:** "Is <client>'s network documentation still accurate?", after a project or burst of emergency changes, onboarding a client whose docs came from a previous provider, or when a tech got burned by stale docs on a ticket.

**Run it:** on one client — name the client whose documentation you want audited.

## Prompt

```
Audit CLIENT_NAME's network/infrastructure documentation against what Liongard inspectors actually observe, and draft corrections. Read-only on both sides — corrections are drafts a human applies.

1. Resolve the client's environment, then enumerate EVERY inspector the client runs. This list is finding #1: systems inspected but undocumented, and documented systems with no inspector. Confirm each inspector ran recently; carry each read's age.
2. Pull the documented picture: search the client's documentation for firewall configs, switch/VLAN docs, wireless docs, server lists, hypervisor docs. Note each doc's last-updated date where visible.
3. For each system family present in both, read the live facts from the relevant inspector's latest dataprint using that system's angles (firewalls, switches, wireless, hypervisors, servers, backup). Verify every field angle against the live dataprint; schemas vary by inspector version. A failing inspector can make correct docs look wrong — never diff a stale read without saying so.
4. Diff into three buckets: Doc wrong (documented value contradicts the dataprint — VLAN map, firmware, missing hosts); Doc silent (inspected facts with no documentation home — undocumented SSIDs, admins, VPN tunnels, servers); Inspector silent (documented systems no inspector covers — a coverage gap to recommend, not proof the doc is wrong).
5. Use the inspector run history to date the drift where useful ("doc last updated <date>; inspector detected the change <date>").
6. Draft corrections per-document: the specific field-level updates with the inspector value, its as-of timestamp, and the source inspector named. Drafts only — never write to the doc platform. Never copy credentials, PSKs, or secrets into diffs or drafts; reference their documented location only.
7. Result caps: a large environment may exceed limits — audit per system family and state coverage ("audited firewall + wireless docs; servers pending") rather than implying a full sweep.
8. Output: the diff table (doc / claim / observed / source inspector / as-of / severity), the coverage-gap list both directions, and the correction drafts. Offer to leave a plain-text note. If no documentation platform is enabled, invert the deliverable: generate a from-scratch documentation skeleton from the inspector data, clearly labeled machine-observed and needing human review.
```
