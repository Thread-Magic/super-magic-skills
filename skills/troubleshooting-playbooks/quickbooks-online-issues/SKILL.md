---
name: QuickBooks Online Issues
description: Fix QuickBooks Online browser problems: bank-feed failures, multi-user role errors, cache and extension issues; distinguish QBO from Desktop before acting.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# QuickBooks Online Issues

**When to use:** A user reports QuickBooks web problems (pages won't load, dead buttons, "something went wrong"), bank feeds stopped importing or show duplicate/missing transactions, a user can't access the company or hit a user limit, or login works elsewhere but not in one browser/machine.

**Run it:** on the one ticket you're working — a tech works it with the user; not unattended.

## Prompt

```
QuickBooks Online is a web app: its failures are browser-and-account problems, not
file-and-network ones. So confirm QBO vs Desktop FIRST — QBO is reached at an Intuit web
URL in a browser, Desktop is an installed app, possibly hosted. If it's Desktop
multi-user, stop and use quickbooks-desktop-multiuser; chasing file and network causes
that don't exist on QBO is the classic waste. Note the subscription tier (user limits
and features differ by plan).

Then climb the Troubleshooting Ladder base skill: past QuickBooks tickets for this
client — a bank forcing feed re-auth, a browser or OS update, a user or plan change; a
feed that dropped across many clients at once is an Intuit or bank outage — then the
verbatim error, then the test that splits the problem: does it work in a
private/incognito window or another browser? For feeds, note the account, the error
text, and when it last imported.

Branch:

1. Browser layer (won't render, dead buttons, endless spinner). QBO is sensitive to
   cache, ad-block and privacy extensions, and third-party cookie blocking. If incognito
   works, clear cache and cookies for the Intuit domains or disable the offending
   extension. Confirm the browser is one Intuit currently supports — it drops old ones.

2. Bank feeds. A feed that stopped or asks to reconnect usually means the bank changed
   its connection or security; the user re-authenticates inside QBO. Duplicates or
   missing transactions are normally an overlap or gap from a re-link or a manual import
   — reconcile the specific date range. Never bulk-delete or bulk-accept feed
   transactions to clean up; that is live financial data. Escalate when the bank itself
   blocks aggregation — that sits between the client and their bank or Intuit.

3. Access, roles, user limit. Check the user's role and status in QBO's Manage Users and
   whether the plan's user limit is reached — "upgrade to add users" is the client's
   cost decision. Any role change is an access change: confirm with the client's QBO
   admin; treat payroll and banking visibility as sensitive. Pair with
   access-request-handling or employee-offboarding; keep user identities out of notes.

4. Still failing in incognito and a second browser — it's account or data side: an
   Intuit service issue (check their status page), a corrupted session, or a problem
   only Intuit can resolve. Set honest expectations and package the error for them.

Never change company data to "clean up" a discrepancy — correct the specific item and
let the client's bookkeeper verify. Check Intuit's current docs for menu paths and
supported browsers rather than reciting them.

Success is the user completing the real action — page loads, feed imports, user signs in
with the right role. Note it (apply the PSA Note Discipline base skill): QBO confirmed
not Desktop, the error, the incognito result, branch, action, verification.
```
