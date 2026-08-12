---
name: Doc Gap Detector
description: Find tickets where a security- or configuration-impacting change (firewall, MFA, DNS, admin access) was made with no linked or matching documentation update.
category: Documentation
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: global
flow: yes
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Doc Gap Detector

**When to use:** "Which changes last month never got documented?" — after a busy change window, during compliance/audit prep, or when a new engineer keeps finding the environment doesn't match the docs.

**Run it:** across all completed tickets in a window · or as a Flow (triggered to run the sweep on demand).

## Prompt

```
Sweep completed tickets for changes that alter a client's security posture or
configuration and verify each one left a documentation trail. Report the gaps; do not
fix them silently.

1. Pull resolved tickets for the window (default: last 30 days), running SEPARATE
   searches per change class: firewall/network rules, MFA/conditional access, DNS
   records, admin/privileged access grants, VPN config, backup config,
   licensing/tenant changes.

2. For each hit, confirm from the thread that a change was actually MADE (not merely
   proposed or recommended) — zero-assumption: a recommendation is not a change.

3. For each confirmed change, look for a documentation trail: a doc reference/link in
   the ticket notes, or a matching, recently updated entry in the documentation
   platform (IT Glue / Hudu where connected) and the knowledge base.

4. Classify each change: DOCUMENTED (trail found), GAP (no trail), or UNVERIFIABLE
   (docs platform not searchable for this tenant, or result cap hit). Absence of
   evidence is reported as a "gap to verify", not an accusation — the doc may live
   somewhere unsearchable; say so.

5. Output the gap report grouped by <client>: change made, ticket number, date,
   engineer, change class, and what documentation is missing. Rank security-impacting
   gaps (MFA, admin access, firewall) first. Report ONLY changes the thread confirms
   were executed — never list a recommendation or quote as an undocumented change.
   RESULT-CAP HONESTY: if searches cap out, state the sweep is partial and name the
   classes affected. If neither IT Glue nor Hudu is connected, check ticket notes and
   the Thread KB only, and say external doc platforms were not checked.

6. If asked, leave a plain-text internal note on each gap ticket ("Documentation gap:
   <change class> change has no doc update — please document") — but confirm the ticket
   list with the requester BEFORE posting any notes. That is the only write; never edit
   documentation or tickets beyond it.

UNATTENDED (Flow): the entire reply is the plain-text gap report, security-impacting
gaps first, no narration. Capped or unsearchable classes appear under an UNVERIFIABLE
heading, never silently dropped. No gaps found -> reply exactly "NO DOC GAPS FOUND."
(append " (SWEEP PARTIAL)" if any search capped). The per-ticket gap notes stay
attended — they require the requester to confirm the ticket list.
```
