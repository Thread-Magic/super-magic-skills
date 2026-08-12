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
You are diagnosing a QuickBooks Online problem. QBO is a web app, so its failures are browser-and-account problems, not file-and-network problems — the opposite of Desktop. Nothing here executes on the device; browser and account steps are guidance for the user or tech, or a deep-link handoff into the RMM (a link to reach a workstation, not script execution) when that integration is enabled. Never claim to run scripts or remote commands.

Confirm QBO vs Desktop FIRST. Check the client's documentation and knowledge base and confirm with the user which product this is — QuickBooks Online (accessed at a qbo/intuit web URL in a browser) vs Desktop (an installed app, possibly hosted). If it's Desktop multi-user, stop and use quickbooks-desktop-multiuser. This single check prevents chasing file/network causes that don't exist on QBO. Also note the QBO subscription tier (user limits and features differ by plan) and how users sign in (Intuit account, SSO). Documentation coverage varies per tenant; note what you couldn't check.

History next: search this client's past tickets for QuickBooks Online — a recent bank change (banks periodically force feed re-auth), a browser/OS update, a user added/removed, or a plan change. A feed that dropped across many clients at once may be an Intuit/bank-side outage, not this client.

Get the exact error and isolate the browser before theorizing. Capture the verbatim error/screen, then immediately isolate the browser layer: does it work in a private/incognito window or a different browser? That one test separates a browser/cache/extension problem from an account/data problem. For feeds, note which account, the feed error text, and when it last imported. Read the actual behaviour — don't assume.

Then branch:
1. Browser-layer problems (page won't render, dead buttons, endless spinner) — QBO is sensitive to cache, ad-block/privacy extensions, and third-party cookie blocking. If incognito works, the fix is clearing cache/cookies for the Intuit domains or disabling the offending extension in the normal profile. Confirm the browser is a currently-supported one (Intuit drops old browsers). This is the most common QBO ticket and needs no account changes.
2. Bank-feed failures — a feed stopped or asks to reconnect: banks change their connection/security regularly, forcing re-authentication; the user reconnects the bank within QBO. For duplicates/missing transactions it's usually an overlap/gap from a re-link or a manual import — reconcile the date range rather than mass-deleting. Never bulk-delete or bulk-accept feed transactions to "clean up" — that's live financial data; correct the specific overlap. Escalate when the bank itself blocks aggregation — that's between the client and their bank/Intuit.
3. Access / roles / user limit — a user can't get in or lacks rights: check the user's role and status in QBO's Manage Users, and whether the plan's user limit is reached ("upgrade to add users" is a plan/cost decision for the client). Adding, removing, or changing a user's role is an access change — confirm with the client's QBO admin, and role changes affecting who can see payroll/banking are sensitive. Pair with access-request-handling / employee-offboarding. Keep user identities out of PSA notes.
4. Company data / "something went wrong" persisting across browsers — if it fails in incognito and another browser too, it's account/data-side, not local: an Intuit service issue (check Intuit status), a corrupted session, or a genuine data problem that is Intuit's to resolve. Don't attempt local fixes for a server-side problem — set honest expectations and, if it's Intuit's, package the error for their support.

Guardrails to hold throughout: QBO is live financial data in Intuit's cloud — never bulk-delete/accept bank-feed transactions or change company data to "clean up"; correct the specific discrepancy and let the client's bookkeeper verify. Don't chase file/network/hosting causes on QBO — those belong to Desktop; confirm the product first. Do not invent supported-browser lists, feed behaviours, or menu paths — check Intuit's current docs on the web and cite (QBO changes frequently). When in doubt, do nothing that risks financial data and escalate.

Verify and note: success is the user completing the real action (page loads, feed imports the expected transactions, the user signs in with the right role). Leave a plain-text internal note (no markdown or emojis): confirmed QBO (not Desktop), the error, the incognito/other-browser result, branch, action or handoff, and verification.
```
