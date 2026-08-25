---
name: Inspector Read Discipline
description: Base skill defining how any Liongard inspector is read — resolve the environment, date the dataprint, verify field angles live, and state data age in every answer.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_events]
connectors: [Liongard]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Faster Resolution & Response]
---

# Inspector Read Discipline

**When to use:** Reading any system's configuration through Liongard, or writing an inspector skill. It's the shared contract every inspector playbook in this category stands on.

**Run it:** on one client's environment — read-only; Liongard never changes the target system.

## Prompt

```
A Liongard answer is only as good as the run behind it. Every inspector read follows the
same discipline, whatever the target system is.

1. Resolve the client's environment first. Rank the matches and state your pick. No
   environment means Liongard cannot answer for this client — go straight to degradation
   (step 6), don't approximate with a neighbouring tenant.

2. Find every inspector for the target system inside that environment, not the first one.
   Clients have multiple firewalls, multiple hypervisor clusters, multiple backup jobs —
   grabbing one and reporting it as "the" config is the most common wrong answer here. If
   nothing matches, try close name variants before concluding absence; inspector
   availability varies by Liongard subscription and version.

3. Date it before you trust it. Check each inspector's last-run status and timestamp. A
   failed or inactive inspector means the data is stale as of its last success — carry
   that caveat on every downstream statement. Repeated failures are themselves a finding
   worth raising, not just a caveat.

4. Read the dataprint two ways, and verify the angle. For precise values — counts,
   versions, lists — probe broadly first, then narrow, and check every field angle
   against the live dataprint, because schemas differ between inspector versions. For
   open-ended or cross-system questions, ask in plain language first, then confirm any
   number that will drive an action with a precise read.

5. State freshness in every output. Inspector name, last successful run, and the data age
   in plain terms: "as of 14:20 yesterday, 19 hours ago." A configuration answer without
   its age is wrong by omission, and an active incident deserves an explicit
   "verify live before acting" caveat.

6. Degrade honestly. Environment or inspector absent, inactive, or failing: fall back to
   the client's documentation (label it "documented, not inspected — may be stale"), then
   to ticket history (label it "inferred from ticket history"), and otherwise say so
   plainly and recommend the tech verify on-device. Never fill a gap with typical or
   default values. Absence of data is not absence of the system — say "no inspector found
   for <system> in this environment," never "the client has no <system>."

7. Output shape: a compact table of the values, the source line, the data-age line, and
   the caveats. If a result looks truncated, narrow the question rather than presenting a
   partial list as complete (see the Sweep Honesty base skill).

This is a read. Nothing here changes the target system, and a note only gets left on the
ticket when someone asks for one — then apply the PSA Note Discipline base skill.
```
