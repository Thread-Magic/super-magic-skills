---
name: My Queue Summary
description: A technician asks what is on their plate, what needs replies, what is urgent, or what to work next — summarize their assigned tickets with a clear next step for each.
category: Reporting & Analytics
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# My Queue Summary

**When to use:** "Give me a summary of my open tickets — what needs replies, anything urgent," "what should I work on today?", "prioritize my queue," or a morning/EOD personal digest ("keep it to 3 lines").

**Run it:** across all of your own open tickets — manually on demand (read-only, and there's no ticket event for a Flow to trigger on).

## Prompt

```
Give an individual technician a prioritized read of their own open tickets — bucketed
into needs-replies, urgent, and everything else — with one clear next step per ticket.

1. Identify the requesting technician (look them up by name if needed) and pull their
   open ASSIGNED tickets. Scope strictly to the requesting tech's own
   tickets — never another member's queue. If the count may exceed the result cap,
   split the search per board or per status and disclose it ("showing the first N by
   priority") rather than presenting the list as complete.

2. Bucket the results:
   - Needs replies — the last message is from the client and awaiting the tech.
   - Urgent — high priority, imminent SLA target, or negative-sentiment thread.
   - Everything else — ranked by priority, SLA risk, then age.
   Exclude auto-closed statuses and junk/NOC noise boards.

3. For each ticket give a one-line state AND a concrete next step ("reply with the
   workaround", "chase the vendor", "schedule the visit") — not just a status. Do not
   invent ticket numbers or states; every line must come from a returned ticket.

4. Lead with the single most important ticket to work next and why. Do not dump a flat
   unranked list.

5. If the tech asked for a digest ("3 lines", "short version"), compress to: needs-
   replies count + the top one, urgent count + the top one, and the recommended next
   ticket. Nothing else.

This is read-only — it changes nothing.
```
