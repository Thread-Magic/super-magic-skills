---
name: Firewall Rule Change Request
description: Shepherd a firewall change from vague ask to change-ready spec — justification, source/destination/port/protocol, expiry, and routing to the approver.
category: Devices & Infrastructure
tools: [search_tickets, search_itglue, search_hudu, search_knowledge_base, update_ticket, add_ticket_note, send_approval, create_ticket, schedule_ticket]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Firewall Rule Change Request

**When to use:** A ticket asks to open a port, allow inbound access, whitelist a vendor IP, or set up a port forward — or "temporarily allow X for the audit/migration".

**Run it:** on one change-request ticket, on demand (not a Flow — every firewall change routes through human approval).

## Prompt

```
Turn "please open a port" into a complete, reviewable firewall change and hand it into change management. This skill prepares and routes the change — it NEVER touches the firewall.

1. Extract what is actually asked: requester, client, business justification in one sentence, and the traffic — source (IP/subnet/"any"?), destination, port(s), protocol, direction. If it came from a vendor document, quote the vendor's stated requirements rather than paraphrasing.
2. Tighten anything vague. "Any" as source on an inbound rule needs explicit pushback — ask for the vendor's published IP ranges or the specific remote subnet. Broad port ranges get the same treatment: which ports does the app actually document? Never widen a request to "make it work".
3. Classify permanence: if time-boxed (migration, audit, trial, contractor), the request must carry an expiry date and a scheduled removal. Propose a review date even for "permanent" inbound-exposure rules.
4. Context checks: check the documentation (IT Glue / Hudu) for the client's firewall documentation (which device, who administers it — MSP, co-managed IT, or ISP-managed changes the routing entirely) and any documented change-control policy; check the knowledge base for the desk's change procedure; read ticket history for prior requests touching the same destination (a duplicate or previously rejected request changes the answer).
5. Assemble the change spec as a plain-text block (no markdown/emojis): justification, requester, exact rule (source, destination, port, protocol, direction, NAT if applicable), permanence + expiry, rollback statement ("remove rule"), risk note for anything inbound or any-source. Leave it as a note on the ticket.
6. Route it: send it to the designated approver for sign-off with the spec summary. Once approved, hand off to whoever administers the firewall — via ticket assignment/status update, or open a change ticket on the appropriate board if the client's process requires a separate one. For temporary rules, create the removal task now: schedule a follow-up ticket dated at expiry.

Guardrails: this skill never implements the rule — it produces the spec and routes it; never report the change as done because the spec was approved. No inbound any/any, and no any-source inbound rule without an explicit, named risk acceptance from the approver in writing. Temporary rules without a created removal task are incomplete — do not close until the expiry follow-up exists. Never include firewall admin credentials, VPN PSKs, or management URLs with embedded secrets in the ticket; reference documentation by name. If the firewall is ISP- or co-managed, your output is a request package for the administering party and the ticket reflects waiting-on-external.
```
