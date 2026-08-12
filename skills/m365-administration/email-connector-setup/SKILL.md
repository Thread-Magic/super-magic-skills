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
You are choosing the least-privileged mail-sending method for a device or application and scoping any connector so only the intended source can use it. You prepare and verify; the technician executes in EAC/PowerShell and on the device. Never report a connector as live on intention — never invent data.

1. Gather the decision inputs (read the ticket for context): does it send only to internal recipients or external too? What From address? Daily volume? Can the device do modern TLS and authentication, or is it a legacy appliance? Does it have a static public IP? (Check the client's documentation for the device's documented specs; skip gracefully if neither is connected.)

2. Pick the method — least privilege first:
   - SMTP AUTH client submission (smtp.office365.com:587): sends anywhere, needs a licensed mailbox for the sending account. Caveats: SMTP AUTH is legacy-auth surface — keep it disabled tenant-wide and enable it only on the single sending account; basic auth for SMTP is on Microsoft's deprecation path, so verify current status against Microsoft's current docs and prefer OAuth-capable devices. Use a dedicated service mailbox, never a human's account.
   - Direct send (via the tenant's MX endpoint): internal recipients only, no authentication, no mailbox needed. Mail is subject to spam filtering and the From can't be trusted externally. Fine for scan-to-email that only goes to staff.
   - SMTP relay with an inbound connector: sends external, no per-message auth — the connector trusts by static public IP or TLS certificate subject. Requires the static IP in the client's SPF record. This is the one that can become an open relay if scoped sloppily; it gets the most scrutiny.
   - High-volume/app-generated mail at scale: flag Azure Communication Services Email or Exchange's high-volume mail offering as the right tool instead of abusing relay — verify current offerings against Microsoft's current docs.

3. Least-scope rules for a relay connector: restrict to the exact source IP(s) — never a broad CIDR, never "any"; certificate-scoped where the device supports it; document every IP's owner. If the client's firewall can also restrict outbound 25/587 to the devices in question, recommend it. Never widen a connector's IP scope to "make it work" — a connector scoped to a range you don't control is an open relay with your client's domain on it.

4. Approval: new sending paths on the client's domain are spoofing surface — send an approval request for the method, sending address, and scope.

5. Prepare execution for the tech (PowerShell labeled: verify against current module versions): EAC > Mail flow > Connectors for relay (New-InboundConnector), device-side SMTP settings per method, SPF update for relay IPs (coordinate with dmarc-spf-dkim-setup guidance so the SPF edit doesn't break alignment or blow the 10-lookup limit). Relay IPs go into SPF deliberately; check the 10-DNS-lookup limit before adding.

6. Verify via evidence: test message from the device to an internal and (if in scope) external recipient, delivered with headers showing the intended path; a message trace (mail-trace-investigation) confirming it. Document what/why/when/rollback in a plain-text note: device/app, method chosen and why, sending address, connector name and its exact IP/certificate scope, SPF change if any, approver, date, and rollback (disable connector <name>; revert SPF). Log time.

SMTP AUTH stays disabled tenant-wide; per-account enablement only, on a dedicated service account with a strong credential and no other roles. Legacy devices that can't do TLS get flagged as a risk in the note, not silently accommodated with weakened settings. When in doubt, do nothing and escalate.
```
