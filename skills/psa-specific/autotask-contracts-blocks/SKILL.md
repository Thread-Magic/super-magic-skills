---
name: Autotask Contracts Blocks
description: For desks synced to Autotask — deeper contract mechanics beyond type labels: block-hour burn tracking from visible time entries, retainer-threshold alerting conventions, and the edge cases (exclusions, overlapping contracts, expired-contract work) that misclassify coverage.
category: PSA-Specific
tools: [search_tickets, search_clients, update_ticket, add_ticket_note, log_time_entry]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Autotask Contracts Blocks

**When to use:** "How many hours has this client burned?" / "are they close to exhausting their block?" on an Autotask desk, an early-warning note as a retainer trends toward exhaustion, or a contested coverage call the type label alone can't settle (exclusions, overlapping or lapsed contracts).

**Run it:** on one ticket · or across all of a client's tickets in a window.

## Prompt

```
You are working the mechanics underneath an Autotask contract — how block-hour and retainer
balances burn, what the desk's alert thresholds mean, and the edge cases where the simple type
label gives the wrong answer. Use the base coverage read (autotask-contract-categories) to
label a ticket; use this when the question is about the balance, the burn, or a coverage call
the type label can't settle.

1. Re-read the relevant ticket(s) and confirm the client. A coverage and burn read against the
   wrong company is worse than no read.

2. Establish what balance data you actually have. The contract's true remaining balance lives
   in Autotask and is usually not synced into Thread. What Thread can evidence: time entries
   on tickets you can see, and burn-down notes left per the desk's convention ("2.0h this
   session; ticket total 5.5h"). Sum only what is visible, present it as "visible burn: at
   least Xh across N tickets in <window>," and if any search may have hit a result cap, say
   the figure is a floor, not a total. Never present visible burn as the contract balance.

3. Burn-rate read (hour-based contracts): from visible entries, characterize the trend —
   hours per week, notably heavy tickets, and whether the pace would exhaust a block of the
   size the desk documents — phrased conditionally ("at ~4h/week, a 20h block lasts ~5 weeks")
   without asserting the actual remaining balance. Recommend an Autotask-side balance check
   before anyone acts on the projection.

4. Retainer alert conventions: if the desk documents thresholds (commonly 75%/90% consumed,
   or Autotask's own contract notifications), do the Thread-side half — when visible burn
   plausibly crosses a threshold, leave a plain-text internal note flagging it and route the
   client conversation per the desk's playbook (account manager, not the tech). Do not message
   the client about money directly.

5. Edge cases — resolve by evidence, else escalate:
   - Exclusions: recurring contracts commonly exclude projects, after-hours, or named
     services. If the work matches a documented exclusion, it's billable even on a "covered"
     client — flag it for billing.
   - Overlapping contracts: a client can hold a recurring contract AND a block for projects.
     Which one the ticket burns is an Autotask-side setting; if not visible, say "contract
     attribution not visible from Thread" and ask before labeling.
   - Expired/lapsed contract: work after end-date is usually T&M by default — but renewal may
     be in flight. Flag it; never assume either way.
   - Zero-dollar/internal contracts: some desks carry internal or warranty contracts; work on
     them is covered-but-unbillable. Follow the desk's sheet.

6. Time entries you create: log time per the desk's convention, always paired with the
   burn-down note on hour-based clients. Never adjust or delete existing entries — corrections
   are Autotask-side human work.

7. Output: what is visible vs not visible, the burn evidence with its floor-honesty caveat,
   the coverage determination or the explicit escalation, and any notes left.

Always: re-read full detail before any read or write; contract association on a ticket can be
corrected Autotask-side at any time. The PSA is always master — contract terms, balances, and
attribution live in Autotask; Thread-side figures are evidence, never authority. Never state
or estimate a contract's remaining balance unless it is actually visible from Thread ("visible
burn ≥ Xh; balance not visible" is the required phrasing). Never guess coverage on edge cases
— exclusions, overlaps, and lapses go to a human when evidence is incomplete. Threshold flags
go to the desk's designated owner (account manager); never raise billing anxiety directly with
the client. Plain-text notes only; never put rates, amounts, or balance speculation in notes
the client can see. Without contract data synced into Thread, run advisory-only from the
desk's documented sheet and visible time entries — state that limitation in every output.
```
