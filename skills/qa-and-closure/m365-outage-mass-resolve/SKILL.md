---
name: M365 Outage Mass Resolve
description: After Microsoft confirms an M365 outage is resolved, find the open threads it caused, get approval, then close them with a customer resolution message.
category: QA & Closure
tools: [search_tickets, add_ticket_note, list_ticket_statuses, update_ticket, view_openDraft]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, Technician]
outcome: [Time & Cost Savings (Capacity), Faster Resolution & Response]
---

# M365 Outage Mass Resolve

**When to use:** Microsoft has posted the all-clear on an M365 incident (Exchange, Teams, SharePoint/OneDrive, sign-in) and the desk has a pile of "email is down" threads to close / "close out everything from this morning's Outlook outage."

**Run it:** across the open threads created since the outage began (attended only: nothing closes without explicit approval). For the close mechanics on a large batch, see qa-and-closure/bulk-ticket-operations.

## Prompt

```
Use this after Microsoft has confirmed an M365 outage is resolved: find the outage-related threads
created since it began, get approval, then close them and send customers a resolution message.

1. Confirm the all-clear first. Ask for the Microsoft Service Health incident ID (e.g. an MO, EX
   or TM number) or a link or status showing the incident is resolved. If none is given, stop.
   Never close anything while the outage may still be active.

2. Confirm scope: the outage start date (default today) and the affected services (Outlook or
   Exchange, Teams, SharePoint or OneDrive, sign-in, etc.).

3. Find candidates: open threads created on or after the start date, searching every variant of
   the affected services, singular and plural: Outlook, Exchange, Teams, M365, Microsoft 365,
   Office 365, email, can't send, can't receive, login, sign in, SharePoint, OneDrive. Keep paging
   until there are no more results. If a search is capped, say so; never present a partial list
   as complete.

4. Exclude and flag for manual review any thread that:
   - is a child thread (merged or bundled into another); handle it through its parent
   - has high or critical priority
   - has negative or very negative sentiment
   - has a latest customer message describing something unrelated to the outage, such as a
     password reset, new hire, license change or hardware issue (read the messages to check)

5. Present for approval: the count to close, the count excluded and why, and a few example
   threads with links. Offer to open the full set as a View. Do NOT close anything until the
   technician explicitly approves this list.

6. For each approved thread:
   - Add an internal note: "Closed as part of the M365 outage mass resolution. Microsoft incident
     [ID] confirmed resolved on [date/time]."
   - Add an external note, sent to the customer by email, with the message in step 7.
   - Close it: look up the statuses for the thread's own board and pick the closed status that
     best means Resolved or Closed. If several look similar, ask once which to use, then reuse
     it for every thread on that board.
   Notes are plain text, no markdown or emojis (apply the PSA Note Discipline skill). If a write
   fails or a thread changed since you listed it, stop and report before continuing.

7. Customer message: "Hi [First name], Microsoft has confirmed that the Microsoft 365 service
   disruption affecting [service] has been resolved. Your service should now be working
   normally. If you're still seeing problems, please reply to this message and we'll reopen
   your request right away. Thank you for your patience."

8. Wrap up: how many threads were closed, how many were skipped for manual review (with links),
   and any failures. Do not log time unless asked.
```
