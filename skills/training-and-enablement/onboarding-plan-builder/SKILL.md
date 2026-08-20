---
name: Onboarding Plan Builder
description: Draft a new tech's onboarding curriculum from the desk's own resolved tickets — the request types they'll actually face, in real volume order, with practice tickets per phase.
category: Training & Enablement
tools: [search_tickets, list_boards, search_members, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Staff Enablement, Time & Cost Savings (Capacity)]
---

# Onboarding Plan Builder

**When to use:** "Build an onboarding plan for our new tech" / "what should a new hire learn first?" / "what does our desk actually get asked?" — before a new starter, or when the current plan was written from memory rather than from the queue.

**Run it:** across the desk's resolved tickets over a window you choose — run it manually (not a Flow; it produces a plan, not a ticket action).

## Prompt

```
Build a phased onboarding curriculum for a new technician on this desk, drawn from what this desk
actually gets asked — not from a generic template. Work only from resolved tickets, so every
example has a known outcome a trainee can be measured against.

1. Ask for the window (default: the last 90 days), and which boards to include if the desk runs
   more than one. If the answer is "all of it", say which boards you looked at.

2. Read the resolved tickets in that window and group them by the request they actually were —
   the job to be done, not the words in the subject line. Password and access requests, mailbox
   changes, printers, device setup, connectivity, software installs, backup alerts, and so on.
   Merge near-duplicates into one group. Name each group the way a tech on this desk would say it.

3. For each group, work out four things from the tickets themselves:
   - How often it comes up, as a share of the window's volume.
   - How hard it is: single reply and closed, versus several touches, versus needing another team.
   - Whether it is mostly handled by the AI agent already, or lands on a human.
   - What good looks like, from the tickets that closed cleanly and quickly.

4. Order the groups into phases by what a new hire should be trusted with first: high volume and
   low complexity early, so they build confidence on work the desk sees every day; multi-touch
   and cross-team work later. Cover roughly the top 80% of real volume before the long tail, and
   say what share each phase accounts for.

5. Lay the plan out as phases — First day, Week 1, Week 2, and so on for as many as the material
   warrants. For each phase give: what they should be able to handle by the end of it, the
   request types it covers, and three to five real resolved tickets from that phase's types to
   practise on, named by number and one-line summary. Pick tickets with a clear thread and a
   documented resolution; note when a phase has thin pickings.

6. Flag what the tickets say about the desk itself, briefly: request types with no knowledge-base
   article behind them, groups where resolution times vary wildly between techs, and anything the
   AI agent already handles end to end that a new hire therefore does not need to learn by hand.

7. Finish with the plan in a form the trainer can use straight away, and say how to run it: paste
   the phases into the New Hire Onboarding Coach skill, which walks a trainee through those
   tickets and scores their replies.

Guardrails: work only from tickets that actually exist in the window — never invent a request
type, a volume figure, or a practice ticket to round out a phase. If a search may have hit a
result cap, say so and treat every share as approximate rather than presenting it as exact. If
the window is too thin to support a plan, say how thin it is and ask for a longer one instead of
padding it. Give volumes as shares and counts you can point at, and do not present this as an HR
or performance document about any individual tech.
```
