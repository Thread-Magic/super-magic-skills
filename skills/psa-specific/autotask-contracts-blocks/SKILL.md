---
name: Autotask Contracts Blocks
description: Autotask contract mechanics: block-hour burn tracking, retainer-threshold alerts, and exclusions, overlapping contracts, and expired-contract edge cases.
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
You are working the mechanics underneath an Autotask contract: how block-hour and retainer
balances burn, what the desk's thresholds mean, and the coverage calls a ticket's type label
cannot settle. autotask-contract-categories labels a ticket; this one answers balance, burn
and contested calls.

1. Re-read the ticket and confirm the client; a burn read on the wrong company is worse than
   none. Establish what balance data you have. The true remaining balance lives
   in Autotask and is usually not synced into Thread. Thread evidences visible time entries
   plus burn-down notes per the desk's convention ("2.0h this session; ticket total 5.5h").
   Sum only that and
   present it as "visible burn: at least Xh across N tickets in <window>"; where a search may
   have capped, call the figure a floor (apply the Sweep Honesty skill). Never present visible
   burn as the contract balance.

2. Burn rate on hour-based contracts: characterize the trend from visible entries and phrase
   it conditionally ("at ~4h/week a 20h block lasts ~5 weeks"), never as a remaining balance.
   Recommend an Autotask-side check before anyone acts.

3. Thresholds. Where the desk documents them (commonly 75% and 90% consumed, or Autotask's
   own contract notifications) and visible burn plausibly crosses one, leave an internal note
   and route the client conversation to the account manager — never raise money with the
   client yourself.

4. Edge cases — resolve by evidence or escalate:
   - Exclusions: recurring contracts often exclude projects, after-hours or named
     services. Work matching a documented exclusion is billable even on a covered client.
   - Overlapping contracts: a client can hold a recurring contract and a block for projects.
     Which one a ticket burns is an Autotask-side setting; if not visible, say "contract
     attribution not visible from Thread" and ask before labelling.
   - Expired or lapsed: work after the end date is usually T&M, but a renewal may be in
     flight. Flag it; never assume either way.
   - Zero-dollar or internal contracts: covered but unbillable. Follow the desk's sheet.

5. Log time per the desk's convention, paired with the burn-down note on hour-based clients.
   Never adjust or delete an existing entry — corrections are Autotask-side human work.

6. Output what is and isn't visible, the burn evidence with its floor caveat, the coverage
   call or escalation, and any note left.

Autotask is master: terms, balances and attribution live there, and Thread-side figures are
evidence, never authority. Never guess — incomplete evidence goes to a human (apply the Write
Guardrails skill). Notes are plain text, no markdown or emojis (PSA Note Discipline), and
never carry rates, amounts or balance speculation where the client can see them. Without
contract data in Thread, run advisory-only from the desk's sheet and visible entries.
```
