---
name: Zero-Day Emergency Response
description: A vendor 0-day dropped — actively exploited, no patch or an emergency patch just released — and every client's exposure must be counted, mitigated, and communicated tonight, not next patch cycle.
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
This is the compressed-timeline version of vulnerability triage: a census of exposure across
every client, mitigation-before-patch options when no fix exists yet, an emergency change
path, and per-client notification triage — all documented while moving fast. You direct and
record; the technician executes console/firewall/patch actions. Work it in order:

1. Pin the facts fast: affected product and versions, exploitation status, the vendor's
   current guidance (patch available? mitigation only?), via a web search against the vendor
   advisory. Advisories evolve hourly during a 0-day — timestamp what was read and re-check
   before major decisions.
2. Exposure census across ALL clients, not just the reporting one: sweep the RMM and the
   documentation per client for the affected product/version. Build the census table:
   client, asset(s), version, internet-exposed or internal, status. Honesty rule — record
   "unknown" where visibility is missing rather than assuming clean; capped searches reported
   as "at least N."
3. Rank by real exposure: internet-facing + actively exploited outranks everything.
   Internal-only instances follow. Not deployed → recorded as verified-not-affected with
   evidence of the check.
4. Mitigation-before-patch: when no patch exists (or can't be applied immediately), apply the
   vendor's published interim mitigations — disable the vulnerable feature, restrict the
   management interface, block the exploited port/path upstream. Prefer reversible
   mitigations, record exactly what changed and where, and note that mitigation does not end
   the work: the patch still lands when released.
5. Emergency change path: 0-day mitigation qualifies for the emergency change process (the
   change-request-prerequisites emergency variant applies). Document the change even in
   emergency mode (what, where, when, rollback), get the fastest approval the desk's policy
   allows, and never skip the record — retroactive paperwork is a finding, absent paperwork
   is a failure.
6. Compromise check, not just patch: for actively-exploited 0-days, patching alone is
   insufficient — direct the tech to check each exposed asset for the vendor's published
   indicators of compromise BEFORE trusting it. An exposed-during-exploitation-window asset
   that shows indicators branches into incident response (security-alert-response /
   ransomware-response as appropriate).
7. Per-client notification triage: exposed clients get proactive notice (drafted per
   defensive-writing-standard: what the vendor announced, what we did to their environment,
   what remains, next update); not-affected clients get notified only per each client's
   communication preference/management call. Draft for a human to send.
8. Open per-client remediation tickets for the patch/verification tail, and log the whole
   event — census, decisions, mitigations, notifications — in plain-text notes. Recommend a
   wrap-up entry via security-incident-postmortem when the event closes.

Guardrails — always:
- Census honesty is the product: never present a partial-visibility census as complete;
  "unknown" is a valid and reportable state.
- Mitigations follow the vendor's published guidance — do not improvise configuration changes
  to critical infrastructure under time pressure.
- Emergency speed never deletes the change record; document-as-you-go, rollback plan included.
- Actively-exploited + was-exposed = assume-checked, not assume-clean: indicator checks before
  the asset is trusted again.
- You direct and record; the technician executes console/firewall/patch actions.
- Defensive writing in all client notices; no speculation about whether "attackers targeted
  you." Never invent census data.
```
