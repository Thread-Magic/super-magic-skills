---
name: Sweep Honesty
description: Base skill defining how a skill reports on a search or bulk sweep — result caps, what it could not see, and never presenting a partial pass as a complete one.
category: Automation & Flows
tools: [search_tickets]
connectors: []
scope: global
flow: no
role: [Dispatcher, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Sweep Honesty

**When to use:** Authoring or reviewing any skill that searches across tickets, sweeps a board, produces a count, or reports "everything that matches" — where a quietly truncated result set reads as a clean bill of health.

**Run it:** across a set of tickets — it's a base contract you fold into any skill that counts or sweeps.

## Prompt

```
A sweep that missed half the tickets and doesn't say so is worse than no sweep, because
the reader acts on it. Report what you actually saw.

1. Searches are capped. A ticket search returns up to 100 results, and a request runs
   about 30 steps. If you hit either ceiling, the number you have is a floor, not a
   total: say "at least 47" or "47 in the first 100 results — there may be more," never
   a bare "47". If the set is bigger than one pass, work it in chunks and say how many
   chunks you covered.

2. Say what the sweep covered, every time. Which boards, which statuses, what date
   window, and what you deliberately excluded. A count without its scope can't be
   compared to the same count next week, and the reader will assume the widest possible
   scope unless you tell them otherwise.

3. Zero is a real answer — report it as one. "No tickets matched" with the scope beside
   it is useful. Widening the search until something turns up, and not mentioning that
   you widened it, is not.

4. Note what you couldn't check. Tickets you couldn't open, a client whose documentation
   wasn't available, a board you don't have access to. One line, specific.

5. Don't average away the outliers. If two tickets are dragging the number, name them.
   The point of a sweep is usually to find the exceptions, not to produce a mean.

6. Separate what you counted from what you concluded. Give the raw finding first, then
   the read on it, so the reader can disagree with your interpretation without having to
   redo the count.

If the sweep leads to actions on the tickets it found, gate them with the Write
Guardrails base skill — confirm on the actual list, showing what's in it and how many,
never on the idea of the list.
```
