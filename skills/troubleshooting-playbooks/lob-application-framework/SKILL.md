---
name: LOB Application Framework
description: Generic playbook for any line-of-business app failure — dental, legal, accounting, ERP — identify vendor and version, pull logs, build escalation packets.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# LOB Application Framework

**When to use:** Any application the desk has no specific playbook for — practice management, ERP, legal, accounting, industry software — that won't open, errors, or lost its database connection; an LOB app that broke after an update (its own or Windows); or deciding what the desk can fix versus what goes to the app vendor.

**Run it:** on the one ticket you're working — a tech drives the diagnosis and builds the vendor package; not unattended.

## Prompt

```
The Troubleshooting Ladder base skill applied to an application with no playbook of its own
— nine stages ending in a vendor package complete enough that the vendor can act.

1. History first. Past tickets for this app at this client: LOB apps repeat and the prior
   ticket often holds the local fix. Check the knowledge base.
2. Documentation second: vendor and support contract, server and database location, config
   notes, where vendor-portal credentials live (location only, never the credential),
   runbooks. Missing LOB documentation is its own follow-up.
3. Identify the software precisely: vendor, product, exact version and build (Help → About),
   server and client components with both versions, the database beneath. Client/server
   mismatch after a partial update is a top LOB failure — compare them now.
4. Scope and change correlation. One user or all, one workstation or everywhere? What
   changed — an app update, Windows patches, an AV or EDR rollout, server maintenance,
   licensing? LOB apps are usually broken BY their environment.
5. Get the log and error: the error verbatim, the app's own log (vendor docs say where), the
   Windows Application log at failure. Never work from "it errors out".
6. Known-issue search: the exact error string plus product and version on the web, and the
   vendor's support site. Their KB and release notes outrank forum folklore; never pass one
   off as vendor guidance.
7. Branch on what the desk can own.
   a. Environment-side, yours: connectivity to the app server or database, share and folder
      permissions, security-agent interference (check quarantine and exclusions against the
      vendor's published list; exclusion changes go to the security-policy owner), and
      workstation repair per vendor procedure.
   b. Application-side, theirs: defects, database corruption, licensing, upgrades. Never
      operate on an LOB database or files outside the vendor's documented procedures: it
      risks the client's data and their support. Go to 8.
   c. Update-correlated: follow the vendor's rollback guidance, and never improvise a
      rollback of an app that owns a database. If a Windows patch broke it, the interim is
      the vendor's compatibility fix; only they ship the real one.
8. Vendor-escalation package, the framework's real product. Send a case they can act on at
   once: client and server versions, OS versions, verbatim error, app-log excerpt at
   failure, scope (who, how many, since when), change correlation, what you tried and what
   happened, business impact, contract identifiers. Open it through the entitled channel,
   capture the case number, set a follow-up.
9. Verify and note. The user runs the actual failing workflow, not just app-opens. Note it
   (PSA Note Discipline base skill): app and version, scope, change correlation, error,
   branch, findings, case number, verification.
```
