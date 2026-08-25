---
name: Zero-Day Emergency Response
description: Coordinate an emergency response to an actively exploited zero-day: count each client's exposure, apply mitigations, and communicate the same night.
category: Security
tools: [search_tickets, search_clients, add_ticket_note, update_ticket, create_ticket, search_ninjaone_devices, connectwise_rmm_search_devices, search_itglue, web_search, view_openDraft]
connectors: [NinjaOne, ConnectWise RMM, IT Glue]
scope: global
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Zero-Day Emergency Response

**When to use:** A vendor announces an actively-exploited 0-day in a product the MSP deploys (firewall, RMM, hypervisor, mail, VPN, browser); a CISA/vendor emergency directive or out-of-band patch drops; or management asks "which of our clients are exposed to this?"

**Run it:** across all clients' assets (an emergency exposure census and response).

## Prompt

```
This is vulnerability triage on a compressed timeline. You direct and record; the technician
executes every console, firewall and patch action.

1. Pin the facts from the vendor advisory via a web search: affected product and versions,
   exploitation status, current guidance (patch, or mitigation only). Advisories change hourly
   during a 0-day — timestamp what you read and re-check before any major decision.
2. Census exposure across ALL clients, not just the one reporting: sweep the RMM and each
   client's documentation for the affected product and version. Build the table — client,
   assets, version, internet-exposed or internal, status. Record "unknown" where visibility is
   missing rather than assuming clean, and report a capped search as "at least N" (Sweep
   Honesty base skill).
3. Rank by real exposure: internet-facing and actively exploited outranks everything, then
   internal-only. Not deployed is recorded as verified-not-affected with evidence.
4. Mitigate before patching where no patch exists or none can be applied yet: apply the
   vendor's published interim mitigations — disable the vulnerable feature, restrict the
   management interface, block the exploited port or path upstream. Prefer reversible ones and
   record exactly what changed where. Mitigation doesn't end the work; the patch still lands
   when it ships.
5. Use the emergency change path — 0-day mitigation qualifies (the emergency variant in
   change-request-prerequisites). Document the change even in emergency mode: what, where,
   when, rollback. Get the fastest approval policy allows and never skip the record.
6. Check for compromise, don't just patch. For an actively exploited 0-day, patching alone is
   insufficient: have the tech check each exposed asset against the vendor's published
   indicators of compromise BEFORE it is trusted again. Indicators on an asset exposed during
   the exploitation window branch into incident response — security-alert-response, or
   ransomware-response as appropriate.
7. Triage notifications per client. Exposed clients get proactive notice drafted to the
   defensive-writing-standard skill (factual, no speculation about being targeted): what the
   vendor announced, what you did in their environment, what remains, next update.
   Not-affected clients are notified only per their stated preference or a management call.
   Draft for a human to send.
8. Open per-client remediation tickets for the patch and verification tail, and log the event
   — census, decisions, mitigations, notifications — in plain-text notes. Recommend a wrap-up
   via security-incident-postmortem when it closes.

Mitigations follow the vendor's published guidance — don't improvise configuration changes to
critical infrastructure under time pressure. Actively exploited plus was-exposed means
assume-checked, not assume-clean. Never invent census data.
```
