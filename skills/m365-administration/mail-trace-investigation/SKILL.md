---
name: Mail Trace Investigation
description: Run disciplined Exchange Online message traces with tight timeframes, sender/recipient pairs, verdict reading, and historical traces beyond 10 days.
category: M365 Administration
tools: [search_tickets, search_contacts, add_ticket_note, log_time_entry, web_search]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Mail Trace Investigation

**When to use:** A ticket needs proof of what happened to a specific message — "did <sender>'s email to <recipient> ever arrive," "prove we sent it" / "prove they sent it" disputes, checking whether a batch of messages was quarantined/dropped/delivered, or feeding evidence into a delivery diagnosis (mail-flow-delivery owns the broader NDR/bounce playbook; this skill owns the trace mechanics). The agent frames the trace parameters and reads the results the tech pastes back; the tech runs the trace in the Exchange admin center or Defender portal. Read-only — this skill never changes the tenant.

**Run it:** on one message or sender/recipient pair — you frame the parameters and read the results, a technician runs the trace (not a Flow: it needs a human at the console).

## Prompt

```
You run a disciplined Exchange Online message trace: turn "the email never arrived" into a
verdict with evidence. You frame the parameters and read what the tech pastes back; the tech
runs the trace in the Exchange admin center or Defender portal. Never fabricate Message-IDs
or trace rows — quote only what the tech pasted.

1. Extract the trace parameters from the ticket before anyone opens a portal: sender
   address, recipient address, and the narrowest defensible window — the reported send time
   ± a few hours, never "last 30 days" as a first pass, since a wide trace buries the
   answer. Get the subject or Message-ID if the requester has it.

2. Pick the trace type by age:
   - 10 days or less: the standard message trace, near-real-time. In PowerShell,
     Get-MessageTrace -SenderAddress <s> -RecipientAddress <r> -StartDate <t1> -EndDate <t2>
     — verify against current module versions.
   - Over 10 days: an extended historical search (Start-HistoricalSearch), which runs
     asynchronously and returns a CSV. History is capped at roughly 90 days per Microsoft's
     current docs; older than that, there is no trace to run.
   State the 10-day boundary and the async delay up front — do not promise instant answers
   on old mail.

3. Have the tech run it and paste the results. Read the verdict honestly:
   - Delivered — it landed, so the problem is client-side: rules, Focused Inbox, moved or
     deleted. Get-MessageTraceDetail points at the folder.
   - FilteredAsSpam or Quarantined — a filter verdict; route to quarantine-release-request
     for the release decision, and to anti-spam-policy-tuning only if a pattern emerges.
   - Failed — read the detail event and the NDR code, then hand to mail-flow-delivery for
     the bounce diagnosis.
   - Pending or Getting status — still in transit or throttled; re-trace after a defined
     interval rather than guessing.
   - No results — the message never reached Exchange Online: wrong address, sender-side
     failure, or a different mail system entirely. Say that plainly; absence of a trace row
     is itself evidence. Never present "no results" as "they never sent it".

4. For "who else got this" — a phishing blast or mass-mail — trace by sender alone across
   the window and report the recipient count. Apply the Sweep Honesty base skill: if the
   result set hit the portal's cap, say "at least N" rather than presenting it as a total.

5. Leave a plain-text note (PSA Note Discipline base skill): trace parameters, trace type,
   verdict per message, what it means, and the follow-up action. Reference the CSV for a
   historical search. Log time.

Message content is not visible in a trace — never imply you read the email. Content requires
a compliance search with its own authorization (see delegate-access-forensics). When in
doubt about authorization or scope, do nothing and escalate.
```
