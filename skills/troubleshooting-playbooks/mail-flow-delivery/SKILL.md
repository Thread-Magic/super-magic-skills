---
name: Mail Flow & Delivery
description: Diagnose email delivery — NDR bounces, mail not arriving, stuck outbound, one sender blocked — by decoding the bounce and tracing the actual mail path.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Mail Flow & Delivery

**When to use:** A user's email to a recipient bounced (an NDR is in hand or obtainable), "we're not receiving email from a sender/anyone," outbound mail is queued/delayed or an entire domain can't reach the client, or "their mail keeps landing in junk" / a needed sender is being blocked.

**Run it:** on the one ticket you're working — a tech traces the message hands-on; not unattended.

## Prompt

```
Mail problems are path problems: decode the bounce, map the real architecture, then
trace the message hop by hop.

Climb the Troubleshooting Ladder base skill first: past tickets for this sender,
recipient, or domain — several in one window means a path change (expired connector
certificate, gateway change, DNS edit), not a per-message problem. Then the documented
architecture: gateway or filter in front of Microsoft 365 or direct EOP, where MX
points, and any connectors, relays, or transport rules.

Then get the full NDR, not a paraphrase, and decode the enhanced status code: 5.1.x
recipient or address, 5.7.x policy or authentication (SPF, DKIM, DMARC, blocklists,
tenant blocks), 4.x.x transient (greylisting, throttling, queue delay).

Then find the failing hop: run a message trace and pull the gateway's log for the
message ID. The NDR names who rejected it — the client's stack or the far side; a
far-side rejection means the remedy sits with them or in the sending domain's records.
Then branch.

a. Authentication rejection (5.7.x, "not authenticated", DMARC or SPF failure) — pair
   with the DMARC/SPF/DKIM playbook. If the client's outbound is failing at recipients,
   the cause is their records or a new sending source — an app, printer, or marketing
   tool. Never offer "ask them to whitelist us" as the fix.

b. Gateway vs mail-flow mismatch — mail reaches the gateway but not the mailbox, or
   bypasses it. Check MX points where the documentation says, the inbound connector
   restricts delivery to the gateway's IPs, and EOP enhanced filtering is set for the
   gateway. Mail bypassing the filter is a security finding, not just a delivery bug.
   Connector and MX changes are change-controlled — route them to the owner.

c. Transport rules — the trace shows a rule acted (redirect, block, moderation). Name it
   and read its documented intent; if it is doing its job, the answer is an exception
   request, not a rule edit. Escalate a rule recently modified with broad impact.

d. Junk or quarantine — delivered but filtered. Find the verdict's source: gateway
   score, EOP SCL, or the user's junk settings. Fix the sender's authentication first,
   the filter policy second; per-user safe-sender lists are the last resort.

e. Transient (4.x.x) — check service health both sides, gateway queues, destination MX
   reachability. Retries take hours: don't "fix" what a retry resolves, but confirm
   delivery.

Never recommend broad allow-listing — whole domains, IP ranges, disabling filtering; it
trades a delivery ticket for a security hole. When the rejection is on the recipient's
side or from a blocklist, only they or a delisting request can act — say so, with
timelines.

Verify by tracing a fresh test message across the full path, not "try again". Note it
(apply the PSA Note Discipline base skill): NDR code, failing hop, branch, action,
verification trace.
```
