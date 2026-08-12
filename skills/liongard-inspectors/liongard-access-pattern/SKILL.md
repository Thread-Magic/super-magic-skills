---
name: Liongard Access Pattern
description: The base pattern for reading ANY system's config/state through Liongard — resolve environment, find the inspector launchpoint by systemType, verify it last ran successfully, then query the dataprint. Use it directly for systems without a dedicated skill, and follow it inside every liongard-inspectors skill.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline, liongard_alert]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Liongard Access Pattern

**When to use:** Any "what is <system>'s config/state at <client>?" question where Super Magic has no native integration for that system, "does <client> even have an inspector for <system>?", or as the shared discipline every other liongard-inspectors skill assumes. If a dedicated skill exists for the system, prefer it — it layers system-specific angles on top of this pattern.

**Run it:** on one client's system — name the client and the system you want read.

## Prompt

```
Read a system's configuration/state at CLIENT_NAME through Liongard. This is a read-only observation — Liongard never changes the target system.

1. Resolve the client's environment. Rank the matches and state your pick. If no environment exists, Liongard can't answer for this client — go straight to the degradation step.
2. Find the inspector for the target system (Meraki, FortiGate, Veeam, VMware, etc.) within that environment and confirm it ran recently. There may be several (multiple firewalls, multiple hypervisor clusters) — enumerate them all, don't grab the first. If nothing matches, try close name variants before concluding absence; inspector availability varies by Liongard subscription and version.
3. Verify before you trust: check each inspector's last-run status and timestamp. If the last run failed or the inspector is inactive, its data is stale as of the last success — carry that caveat on every downstream answer, and treat repeated failures as a finding worth a note. Check the run history if the status is ambiguous.
4. Read the values from the inspector's latest dataprint two ways. For precise values (counts, versions, lists), probe broadly first then narrow, and verify every field angle against the live dataprint since schemas vary by inspector version. For open-ended or cross-system questions where you don't know the shape, ask in plain language — then confirm any load-bearing number with a precise read before it drives action.
5. "What changed?" → check what changed: detected changes, run-over-run history, and anything already escalated.
6. State freshness in every output: inspector name, last successful run time, and data age ("as of <timestamp>, N hours/days ago"). A config answer without its age is wrong by omission.
7. If a result looks truncated, say so and narrow the question rather than presenting a partial list as complete. Absence of data is not absence of the system — say "no inspector found for <system> in this environment," never "the client has no <system>."
8. Degrade honestly when the environment or inspector is absent, inactive, or failing: check the client's documentation for documented config (label "documented, not inspected; may be stale") → check ticket history for prior work (label "inferred from ticket history") → else say so plainly and recommend the tech verify on-device. Never fill the gap with typical or default values.
9. Output: the answer, a source line ("Liongard <inspector> inspector, last ran <when>"), caveats, and — if this feeds a ticket — leave a plain-text note only on request.
```
