---
name: ISP Outage Tracking
description: Manage the lifecycle of a circuit outage in the carrier's hands — capture the carrier ticket reference, run the escalation clock, and keep the client informed on a cadence while waiting on the provider. Use when a site's internet/WAN is down and the ISP owns the fix.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, search_tickets, update_ticket, add_ticket_note, schedule_ticket, web_search, send_approval]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# ISP Outage Tracking

**When to use:** A site's internet/WAN circuit is down and troubleshooting points at the carrier, or a carrier ticket exists but the Thread ticket has gone quiet ("what's the status with the ISP?").

**Run it:** on one outage ticket, on demand (not a Flow — it runs an escalation clock and comms cadence a human owns).

## Prompt

```
Own the waiting: structure the carrier ticket reference, escalation timeline, and client-comms cadence so "waiting on the ISP" never means "nobody is watching".

1. Confirm the handoff is justified before parking the ticket on the carrier: demarc-side evidence (modem/ONT lights, the carrier status page via a web search, other tenants at the site affected) noted in the ticket. If the CPE (firewall/router) has not been ruled out, route back to network-outage-triage first.
2. Capture the carrier engagement as structured data in a plain-text note (no markdown/emojis): carrier name, carrier ticket/reference number, circuit ID (from the circuit docs in IT Glue / Hudu — reference IDs only, never account passwords/PINs beyond noting where documented), date/time opened, ETR given, carrier rep name if provided, callback commitment.
3. Set the ticket state honestly: move it to the waiting-on-vendor status the board uses, with the carrier reference in the summary so anyone picking it up sees it instantly.
4. Run the escalation clock: schedule a follow-up ticket at the earlier of the carrier's ETR or the desk's standard check interval (commonly 2-4 hours for a hard-down circuit; follow the client's SLA if documented). At each check: call/portal-check the carrier, append a timestamped update, and if the ETR has slipped twice or the carrier has gone unresponsive past its own commitment, escalate — ask for a supervisor/escalation desk and record the new reference. Business-impacting outages with no ETR after the first escalation may justify invoking the account team or a formal escalation email; get the service-desk lead's sign-off before invoking contractual remedies.
5. Client-comms cadence, independent of carrier progress: an update at engagement, at every ETR change, and at a fixed interval even when there is nothing new ("still with the carrier, next update by <time>"). "No news" updates are sent, not skipped. Match the client's documented communication preferences.
6. On restoration: verify from the site side (not just the carrier's word) before closing — connectivity restored, VPN/tunnels re-established, no flapping for a stabilization period. Close with a final note containing the full carrier timeline; if the outage may qualify for an SLA credit, flag it to whoever handles the client's billing rather than promising a credit yourself.

Guardrails: never invent or approximate a carrier ticket number, circuit ID, or ETR — if the reference is missing, the first action is obtaining it. Do not promise restoration times beyond what the carrier stated, and attribute the estimate ("the carrier's current ETR is..."). Account PINs and portal passwords stay in documentation — never in ticket notes. Waiting-on-vendor is a monitored state: a carrier ticket with no scheduled follow-up is a workflow failure — always leave the next check booked. SLA-credit eligibility is flagged, never asserted.
```
