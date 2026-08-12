---
name: Exchange On-Prem Mail Flow
description: Diagnose on-prem Exchange transport — stuck queues, send/receive connector faults, TLS/cert failures, backpressure — using Queue Viewer and protocol logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Exchange On-Prem Mail Flow

**When to use:** Mail is queuing on-prem and not delivering (internally or externally); a send/receive connector broke after a change or a "smart host"/relay stopped working; TLS/certificate errors appear in mail flow or a partner stopped accepting mail; or the transport service stopped, backpressure warnings fired, or the Exchange disk filled up.

**Run it:** on the one ticket you're working — a tech drives the queue viewer and shell hands-on; not unattended.

## Prompt

```
On-prem Exchange transport breaks in known places: a queue backing up behind one destination, a connector misconfigured or pointing at the wrong smart host, a TLS/certificate failure, or the transport service throttling itself under backpressure (usually disk). Read the queues and logs first. Delivery problems that cross a hybrid boundary belong to exchange-hybrid-issues; general mail-delivery diagnosis to mail-flow-delivery.

Work it in this order:

1. Version identification first. Check the client's documentation and knowledge base for the design: Exchange version and CU (an out-of-support CU changes what's advisable and safe — note it), single vs multi-role, the send-connector topology (direct-to-internet vs smart host), what handles inbound (a filtering gateway/MX in front?), and the transport certificate in use. If this org is hybrid, stop and use exchange-hybrid-issues for anything crossing the boundary. Documentation coverage varies per tenant — note what you couldn't check.

2. History first. Search this client's past tickets for mail work: a recent certificate renewal (transport TLS dies on cert expiry — sudden onset on a date is a cert until proven otherwise), a connector edit, an IP/firewall change, or a filtering-vendor change. Certificate and connector edits are the usual triggers.

3. Read the queues and logs before theorizing. Queue Viewer / Get-Queue — which queue, how deep, and the last error per queue (this alone usually names the destination and cause). Then the relevant protocol/transport logs: SMTP send/receive logs for a connector fault, and verbatim NDRs (the enhanced status code and generating server say which hop rejected). Read the actual error — not "mail isn't flowing" — and don't invent codes.

4. Branch:
   - Queue backing up behind one destination — one remote domain's queue is deep with a retry error: the far side is down/greylisting, your sending IP is on a blocklist (check reputation), or DNS/MX resolution for that domain is failing from the server. A single stuck message poisoning a queue can be handled per Exchange's tools; a reputation/blocklist problem is a delisting process, said honestly. Escalate when the block is your public IP's reputation — that's a deliverability/DNS effort (pair with dmarc-spf-dkim-setup), not a connector tweak.
   - Send/receive connector fault — a change broke relay or outbound: an anonymous relay receive connector's permitted-IP scope edited, a send connector's smart host/address-space/credentials wrong, or authentication changed. Read the connector config against the documented design; a "cleaned-up" connector is a classic cause. Never widen an anonymous relay connector's scope to "make it work" — open relays get abused.
   - TLS / certificate failure — mail fails with TLS errors after a cert renewal or expiry. The transport certificate must be enabled for SMTP and referenced by the connector; a renewed cert with a new thumbprint often isn't re-bound. Verify the cert is valid, trusted by partners, and assigned to SMTP. Pair with ssl-certificate-renewal.
   - Backpressure / transport stalled — the Transport service is rejecting/deferring because a resource crossed a threshold, almost always the disk holding the queue database or logs filling up (runaway logging, a huge queue, or logs never truncated). Free space at the source (why did it fill?) rather than just deleting; a stopped transport service that won't start cleanly needs the event log read. Escalate when it's a storage-sizing problem.

Guardrails to hold throughout: no remote execution — all EMS/EAC and queue operations are guidance for a tech with Exchange admin access. When the RMM integration is enabled, open the server in the RMM (a deep link for the tech, not script execution) to hand the tech onto it; otherwise ask the tech to reach it manually. Never open or widen an anonymous relay connector to resolve a relay complaint — an open relay is a security incident waiting to happen; scope it to known hosts and escalate the design if needed. Don't mass-delete queued messages to "clear" a queue — messages are mail; suspend/inspect, and when removal is warranted export first (removing NDR/poison messages is targeted, not wholesale). On out-of-support CUs, say so and set expectations honestly — some fixes require patching first. Quote NDR/enhanced status codes verbatim and verify meanings against Microsoft's current docs on the web (Microsoft Learn) — do not paraphrase from memory.

Verify and note. Success is the queue draining and a test message each direction with clean headers/NDR-free delivery. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): version/CU, the queue/last-error evidence, branch, action taken or handed off, verification and time.
```
