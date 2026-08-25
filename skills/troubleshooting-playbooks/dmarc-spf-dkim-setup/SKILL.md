---
name: DMARC / SPF / DKIM Setup
description: Diagnose email authentication failures and build correct SPF, DKIM, and DMARC DNS records — new sending sources, alignment, and propagation expectations.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# DMARC / SPF / DKIM Setup

**When to use:** Recipients reject or junk a client's mail with SPF/DKIM/DMARC failure wording; someone asks you to set up or fix DMARC (or SPF/DKIM) for a domain; a new sending service (marketing tool, CRM, scanner, app) needs to send as the domain; or DMARC aggregate reports show failing sources.

**Run it:** on the one ticket in front of you — a tech drives the record work and hands DNS edits to whoever owns DNS access; not unattended.

## Prompt

```
Turn "our email is failing authentication" into a specific diagnosis — which mechanism,
which source, which alignment — and exact corrected records.

Climb the Troubleshooting Ladder base skill first: this domain's past authentication
work (a half-finished migration or earlier record change explains most sudden failures),
then the DNS host, who may edit it, and the documented sending-source inventory. An
incomplete inventory blocks any strict-enforcement recommendation.

Then get the evidence — the failing message's full headers (Authentication-Results) or a
DMARC report excerpt: which mechanism failed (SPF, DKIM, or DMARC alignment), for which
source, and what the receiver did (none, quarantine, reject). Then read the live TXT
records — root SPF, _dmarc, the DKIM selectors — and diagnose against what is published,
not the documentation.

Branch:

- SPF — the failing source is missing, or the record is broken. Check: does it include
  every legitimate source from the inventory; does it exceed the 10-DNS-lookup limit
  (silently fatal, and common); are there multiple SPF records (invalid)? Produce the
  exact corrected single record from each vendor's documented include. Prefer ~all;
  recommend -all only once the inventory is confirmed complete.
- DKIM — missing or broken signature. Which service should be signing (Microsoft 365,
  the gateway, a marketing tool), and is its selector's public key published? The fix is
  two-sided: enable signing at the source, publish the selector record the vendor names.
  If it can't sign, the client accepts SPF-only alignment there or changes vendor.
- DMARC alignment — SPF and DKIM each pass, yet DMARC fails because neither passes for
  the visible From domain. Classic with forwarders and third-party senders on their own
  envelope domain; the fix is a custom return-path or DKIM signing as the client's
  domain at that vendor. Check alignment explicitly.
- New DMARC rollout — p=none with rua reporting first, monitor a full business cycle,
  fix the failing legitimate sources, then quarantine (optionally with pct=), then
  reject. Refuse to jump straight to p=reject on a domain with unverified sources: a
  wrong policy silently drops the client's mail.

Deliver guidance, don't execute. DNS edits belong to whoever owns DNS access: give the
exact record name, type, value, and where it goes. State the TTL and the honest window:
up to the TTL, practically 24-48 hours at stragglers. One change, then wait and
re-verify; never thrash the record or say "it should work now" right after an edit.

After propagation, re-check the live records and a fresh Authentication-Results header.
If mail still junks once authentication passes, the lever is sender reputation and the
receiver, not more record edits. Note it (apply the PSA Note Discipline base skill):
diagnosis, records before and after, verification, enforcement plan.
```
