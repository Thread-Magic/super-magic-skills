---
name: Email Connector Setup
description: Route LOB apps, scanners, and printers through Exchange Online using SMTP AUTH, direct send, or an IP/certificate-scoped relay connector.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Email Connector Setup

**When to use:** Get a device or application sending mail through Exchange Online the right way — "the copier's scan-to-email stopped working," "our LOB app / monitoring system needs to send notifications," "set up an SMTP relay for <application>," or reviewing an existing inbound connector's scope after a security review. Choose the sending method based on what the device actually needs (recipients, volume, sender address) and scope any connector so tightly that only the intended source can use it.

**Run it:** on one device or application — you choose the method and scope any connector, a technician executes in EAC/PowerShell and on the device (not a Flow: it needs a human at the console).

## Prompt

```
Choose the least-privileged sending method for a device or app, and scope any connector so
only the intended source can use it. The tech executes in EAC/PowerShell and on the device.
Apply the Write Guardrails base skill — never report a connector live on intention; when in
doubt do nothing and escalate.

1. Decision inputs: internal recipients only or external? From address? Daily volume?
   Modern TLS and authentication, or a legacy appliance? Static public IP? Pull its
   documented specs from client documentation (Connector Degradation base skill if off).

2. Pick the method, least privilege first:
   - SMTP AUTH client submission (smtp.office365.com:587): sends anywhere, needs a licensed
     mailbox. Legacy-auth surface — keep SMTP AUTH off tenant-wide and enable it only on
     that one account: a dedicated service mailbox, strong credential, no other roles, never
     a human's. Basic auth for SMTP is on Microsoft's deprecation path — check current
     status and prefer OAuth-capable devices.
   - Direct send (the tenant's MX endpoint): internal recipients only, no auth, no mailbox;
     subject to spam filtering, and the From can't be trusted externally. Fine for
     scan-to-email that only reaches staff.
   - SMTP relay with an inbound connector: sends external, no per-message auth — it trusts by
     static public IP or TLS certificate subject, and that IP must be in the client's SPF
     record. This one gets the most scrutiny.
   - High-volume app mail: flag Azure Communication Services Email or Exchange's high-volume
     offering rather than abusing relay; verify offerings.

3. Relay connector scope: exact source IPs — never a broad CIDR, never "any" —
   certificate-scoped where supported, every IP's owner documented. Recommend a firewall rule
   restricting outbound 25/587 to those devices. Never widen a scope to make it work: a
   range you don't control is an open relay carrying your client's domain. A new
   sending path on their domain is spoofing surface — get client approval for the method,
   address and scope.

4. Execution (verify module versions): EAC > Mail flow > Connectors for relay
   (New-InboundConnector), device-side SMTP settings, and the SPF update for relay IPs —
   coordinate with dmarc-spf-dkim-setup so it keeps alignment, and check the 10-DNS-lookup
   limit.

5. Verify: a test message from the device to an internal and, if in scope, external
   recipient, headers showing the intended path, confirmed by a message trace
   (mail-trace-investigation). Note it (PSA Note Discipline base skill: plain text, no
   markdown) — device, method and why, sending address, connector name and its exact IP or
   certificate scope, SPF change, approver, date, rollback (disable connector, revert SPF).
   Log time. A legacy device that can't do TLS is flagged as a risk, never quietly
   accommodated with weakened settings.
```
