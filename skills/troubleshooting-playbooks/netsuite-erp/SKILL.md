---
name: NetSuite ERP
description: Support NetSuite ERP tickets as an MSP — roles and permissions, saved-search visibility, SuiteScript/REST/CSV integration errors — no financial edits.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# NetSuite ERP

**When to use:** "I can't see / access this record or report" or an "insufficient privileges" error; a saved search or report returns wrong or no results; an integration (CSV import, SuiteScript, REST/SOAP/connector) is throwing errors; or a user can't log in, has the wrong role, or lands in the wrong subsidiary/center.

**Run it:** on the one ticket you're working — a tech diagnoses and hands ERP config to the admin/partner; not unattended.

## Prompt

```
NetSuite is cloud ERP: no server to fix, no file to repair. Nearly every MSP-supportable
ticket is access (roles and permissions), visibility (a saved search or report), or an
integration. Work those; financial configuration and customization belong to the
client's NetSuite administrator or implementation partner.

Scope that boundary first, from the client's documentation: who administers NetSuite,
the roles model, subsidiaries if OneWorld is in play, and which integrations the MSP
owns.

Then climb the Troubleshooting Ladder base skill: past NetSuite tickets for this client
— a role edit (a group losing access at once nearly always traces to one), a release
upgrade (two a year; deprecations shift), an integration change, a new user or
subsidiary — then the verbatim error and, critically, which role the user was in.
Permissions are role-scoped and a user with several roles behaves differently in each.
For integrations, get the execution log, script deployment log, or the failing import
rows.

Branch:

1. Roles and permissions — "insufficient privileges", or a record or tab missing. That
   is a role permission or a record-level restriction, not a bug. Identify the role and
   the exact permission and level it lacks. Changing a role affects everyone in it and
   can expose financial data, so it is the NetSuite admin's decision: gather the
   evidence and route it. Never self-edit a role to unblock a user.

2. Saved search or report — wrong or empty results. Usually the search's own criteria,
   the running user's role or subsidiary restricting visible rows, or the saved search's
   audience settings. A report that "broke" usually had criteria or a referenced field
   changed. Editing a shared saved search affects everyone using it — confirm ownership.

3. Integrations — CSV, SuiteScript, REST or SOAP, connector. Read the log: a CSV failing
   on specific rows (field mapping, mandatory fields, reference lookups), a SuiteScript
   error in the execution log, or a token-based-auth failure (expired token or role, a
   release deprecating an endpoint). Auth, connectivity, and mapping you own are yours
   to fix; SuiteScript code is the developer's or partner's — diagnose and hand off.

4. Login, wrong role, or wrong center. Check login status, assigned roles, and the
   default role and center; SSO and 2FA pair with the identity playbooks. A user
   "missing everything" is usually defaulted into a limited role.

NetSuite is the client's financial system of record: never edit financial configuration,
workflows, GL setup, or customizations, and never bulk-edit, delete, or mass-import
records without the admin's sign-off — mass updates are irreversible at scale.

Success is the user completing the action in the correct role. Note it (apply the PSA
Note Discipline base skill): the boundary, the error, the role context, branch, action,
verification.
```
