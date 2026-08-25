---
name: Security Onboarding New Client
description: Run a new-client security intake: MFA coverage, admin inventory, backup posture, EDR presence, and produce the day-one risk list before an incident.
category: Security
tools: [search_clients, search_contacts, search_tickets, search_ninjaone_devices, connectwise_rmm_search_devices, search_itglue, liongard_environment, liongard_identity, liongard_metric, add_ticket_note, create_ticket]
connectors: [NinjaOne, ConnectWise RMM, IT Glue, Liongard]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Security Onboarding New Client

**When to use:** A new client signed and onboarding is underway (this is the security chapter of the client-onboarding runbook); management asks "what are we inheriting?"; or a client came from another provider and their real posture needs verifying against what was claimed.

**Run it:** across a new client's environment (a day-one security intake).

## Prompt

```
Run the day-one security intake across four load-bearing controls — MFA, admin access,
backups, endpoint protection — and produce a ranked risk list of what could hurt this client
this week, with owners. Record an as-of date and source for every fact; inherited
documentation is routinely stale, so verify against a live read.

1. Establish sources: what the previous provider handed over, what tooling is connectable
   now (RMM agents, Liongard), and what only their staff can answer.
2. MFA coverage: the share of accounts enrolled AND enforced, not merely "capable"; the
   enforcement mechanism, and the exception list — service accounts, legacy-auth
   dependencies, "the owner doesn't like prompts". Every exception is a risk-list candidate;
   detailed pass to identity-mfa-health-check.
3. Admin inventory: every privileged account across identity, devices, firewall, backup
   console and line-of-business admin panels. Flag admin accounts used for daily work, shared
   credentials, live ex-employee or vendor standing access, and previous-provider access,
   which gets a dated transition plan. Deep pass: global-admin-audit.
4. Backup posture: what is backed up and, more to the point, what isn't — cloud mailboxes
   and file shares are routinely assumed-covered and aren't. Where copies live, whether any is
   offsite or immutable, and the last successful restore TEST, not the last successful job.
   "Never tested" ranks high on the list.
5. Endpoint protection: which product, on what share of the fleet — reconcile agent count
   against the RMM inventory and say "at least N" where a search may have capped (Sweep
   Honesty base skill). Who watches its alerts, and which classes are unprotected: servers,
   Macs, the warehouse machine.
6. Sweep the classics: end-of-life OS in production, RDP/VPN without MFA, credential
   spreadsheets (flag the location, never the contents), and email-security basics — route
   SPF/DMARC to dmarc-spf-failure-triage.
7. Produce the risk list, capped at the ten that matter. Each entry: risk / evidence /
   exposure in plain terms / recommended action / owner, ranked by what is exploitable now,
   not by audit category. Open tickets for the top items the client approves and hand the
   list to the account manager (cyber-risk-posture-review sets the cadence).

Never present partial visibility as a clean bill. State findings neutrally per the
defensive-writing-standard skill: this is an intake, not an indictment of the previous
provider, and the client may read it. Handoff credentials go straight to the desk's
credential store, never into a ticket or note. Remediation beyond the agreed onboarding scope is
quoted work for the account manager, never silently absorbed; the list recommends, the client
decides. Without RMM or Liongard, run on exports and interviews: mark unverified items
unverified and re-run once tooling lands.
```
