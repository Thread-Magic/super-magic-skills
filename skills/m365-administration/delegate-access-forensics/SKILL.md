---
name: Delegate Access Forensics
description: Investigate mailbox audit logs to identify Send As, Send on Behalf, and owner actions in delegation disputes and unauthorized-email claims.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket, log_time_entry, web_search]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Delegate Access Forensics

**When to use:** A delegation dispute — "an email went out from my address and I didn't send it," "messages are disappearing from the shared mailbox — who's deleting them?", "did the assistant read/move the manager's mail?", or a mailbox-permissions-audit finding needs "was it USED?" answered. If the pattern suggests compromise rather than a known delegate, the security runbooks (compromised-account-containment, account-takeover-runbook) lead; this skill supplies the mailbox-audit evidence. This skill resolves a delegation dispute with audit evidence instead of accusations: which identity performed the action, under which access type, when — and an honest statement of what the log cannot prove.

**Run it:** on one mailbox dispute — you frame the question and interpret the results, a technician runs the audit-log search (not a Flow: it needs a human at the console).

## Prompt

```
Prepare a mailbox-audit investigation. The tech runs the search; you frame the question,
interpret the identity fields, and report neutrally — never infer rows, report only what the
search returned.

1. Frame the question: which mailbox, which action (send, delete, move, read), what window,
   which suspected actor. Confirm the requester is authorized — the mailbox owner, their
   management, or the client's documented authority. This is HR- and legal-adjacent: no
   authorization on record, no search.

2. Check the evidence window first. Mailbox auditing is on by default in Exchange Online (since
   2019); retention is 180 days standard, longer with E5 — verify the tenant's actual retention
   and license tier against Microsoft's docs. If the event predates retention, say so up front:
   no log, no finding.

3. Prepare the search (verify current module versions): Search-UnifiedAuditLog -StartDate <t1>
   -EndDate <t2> -RecordType ExchangeItem with -ObjectIds or -FreeText, or Purview Audit scoped
   to the mailbox. Filter to the operations that answer it:
   - Sending: SendAs and SendOnBehalf are delegate sends; Send is the owner.
   - Deleting: SoftDelete, HardDelete and MoveToDeletedItems are three different behaviors —
     report which occurred.
   - Reading/moving: MailItemsAccessed (license-dependent), Move, Update, FolderBind.

4. Read the identity fields. UserId and UserKey are the acting identity; LogonType
   distinguishes Owner, Delegate and Admin; ClientInfoString and ClientIP show client and
   source. A SendAs by a delegate holding the permission is a different finding from a Send by
   the owner's own session at a foreign IP — that is compromise: reroute to the security
   runbooks before touching any permission; don't tip the attacker off.

5. Correlate: match rows to disputed items by subject, timestamp and Message-ID, and pull the
   current permission state to see whether the actor's access was granted, when and by whom.

6. Report neutrally: what the log shows (identity, access type, operation, timestamp, client
   and IP), what it does not (content is never captured; MailItemsAccessed depends on
   licensing), and the confidence level. Never state intent — not "X read the CEO's mail" when
   the evidence is a FolderBind under a Delegate logon. Absence inside a covered window is
   evidence; outside it, nothing. Mark result-cap truncation and name what you couldn't check
   (Sweep Honesty base skill).

7. Leave a plain-text note, no markdown or emojis (PSA Note Discipline base skill): the
   question, the authorization, search parameters, findings (operation, actor, logon type,
   timestamp, client), gaps and caveats, and the follow-up — revoke a grant, escalate to
   security, or no action. Reference the CSV export. Log the time.

When in doubt about authorization or compromise, do nothing, touch no permissions, and
escalate.
```
