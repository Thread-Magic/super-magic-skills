---
name: Bitwarden Business
description: Run Bitwarden Teams/Enterprise admin work: organization and collection structure, group-based sharing, account recovery, and offboarding vault handover.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, search_itglue, search_hudu, search_knowledge_base, add_ticket_note, create_ticket, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Bitwarden Business

**When to use:** A client is deploying Bitwarden Teams/Enterprise and needs a rollout/structure plan; a Bitwarden admin task lands (collection/group setup, sharing, or account recovery); or an employee is offboarding and their Bitwarden organization access must be handled.

**Run it:** on the rollout or admin ticket.

## Prompt

```
Handle a Bitwarden Business ticket — the vendor specialization of password-manager-rollout,
which owns the deployment canon (vault architecture, sharing, emergency access, migration),
mapped onto Bitwarden organizations, collections, groups and account recovery. Console
changes are client-admin work you plan and track; structure and recovery decisions get
client sign-off. Credentials never appear in your output — locations and
counts only.

1. Structure and sharing. Each user keeps a personal vault, separate from the organization;
   shared credentials live in the organization, partitioned into collections by team or
   function, with access granted through groups (Enterprise), not per-user assignments that
   drift. Privileged items get a tightly scoped collection; the MSP's own access is a
   defined group with least-privilege membership. Record the structure in the client's
   documentation. Personal vault items are not org-visible, so any credential that must
   survive a departure belongs in a collection. Never share by pasting a password into
   email, chat or a ticket — Bitwarden Send is for one-off, expiring sharing with externals,
   not a substitute for collection membership. One canonical item per credential;
   shared-account passwords rotate when a member leaves (wire that into
   employee-offboarding).

2. Account recovery. Enterprise admin password reset works only if it is
   enabled AND the member is enrolled; enrollment is per user, so confirm it at rollout,
   not at the crisis. With SSO or trusted-device login, check the recovery implications
   first. Record who may invoke recovery and how it is logged; store
   recovery material offline or sealed, never in a ticket or the documentation
   platform in plaintext. Test the recovery path once before go-live. On self-hosted the MSP
   owns the server's availability, backups and updates, and recovery depends on it — flag
   that as its own responsibility with its own monitoring, distinct from vault content.

3. Offboarding: remove the departing user from the organization, revoking collection access,
   and confirm their personal vault held no business credentials. Flag every collection
   credential they could see for rotation, privileged first.

4. Migration and decommission per password-manager-rollout: inventory spreadsheets and
   browser stores (flag the location, never the contents; only the technician copies them
   into Bitwarden), migrate privileged then shared then personal, rotate-flag every migrated
   credential, delete old stores with evidence. Enterprise Vault Health and breach reports
   set rotation priority. Track adoption like security-awareness-coordination, a ticket per
   phase.

Without documentation-tool access the credential inventory relies on client interviews — say
so; expect an incomplete first pass. When in doubt do nothing irreversible and escalate.
```
