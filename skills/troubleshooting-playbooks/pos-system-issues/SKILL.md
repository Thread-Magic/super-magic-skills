---
name: POS System Issues
description: Work point-of-sale tickets — terminal frozen, "card payments not going through", back-office not syncing — by splitting terminal vs payment-gateway vs back-office, with a hard PCI boundary: no touching cardholder data flows without the processor.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# POS System Issues

**When to use:** "The register / POS terminal is frozen or offline" (often store-down urgency); "cash sales work but card payments are declining or timing out"; "sales aren't showing up in the back office / inventory isn't syncing"; or a receipt printer, barcode scanner, or cash-drawer peripheral misbehaving on a lane.

**Run it:** on the one ticket you're working — a tech works it with on-site staff and the vendor/processor; not unattended.

## Prompt

```
You are working a point-of-sale ticket. "The register is down" is really one of three tickets: the terminal/lane hardware, the payment path to the processor, or the back-office server the lanes sync with. Split them first because they have different owners — and because the payment path sits inside the PCI boundary, where the desk assists but the processor decides.

History first. Search this client's past tickets for POS. Prior tickets name the POS vendor, the payment processor, and who fixed it last time — the three facts that decide routing.

Docs second. Check the client's documentation and knowledge base for the POS profile: POS product and version, payment processor and terminal model, back-office server location, and any documented support boundaries (many POS vendors require all payment-device work to go through them or the processor). Documentation coverage varies per tenant; if absent, fall back to the knowledge base and say what you couldn't check.

Gauge urgency honestly. A store that cannot take payments is revenue-down — treat like an outage. Ask: can they take ANY payment (cash, offline card mode)? Some POS systems have store-and-forward/offline card capture; if in use, note that queued transactions must sync later and failures there are a processor conversation.

Identify versions. POS software version on the affected lane vs a working lane, terminal firmware if visible, back-office version. Never assume all lanes match.

Evidence before theory. Exact on-screen error at the lane, the decline/timeout message text for payments, and scope: one lane, all lanes, one store, all stores. Scope is the fastest fork — one lane is hardware/endpoint; all lanes points at network, back office, gateway, or vendor cloud. Then branch:

1. Terminal / lane offline — one lane down, others fine. Guide on-site staff: power-cycle the lane per the vendor's documented order (peripherals often must come up before the POS app), check cabling, verify the lane has network. If it's a hardware fault (dead terminal, failed printer), that goes to the POS/hardware vendor under the client's support contract, not desk repair — escalate.

2. Payment gateway / processor path — cash works, cards fail. First check the processor's and POS vendor's status pages (on the web) — processor incidents are common and end troubleshooting immediately. If no incident: verify the site's internet path is up and nothing changed on the firewall (new content filter, TLS inspection — see the SSL Inspection Issues playbook; payment terminals are certificate-pinned and break loudly under inspection). Anything requiring configuration of the payment device or the payment flow itself is the processor's or POS vendor's work — escalate. State the PCI boundary plainly: we do not modify cardholder data flows without the processor.

3. Back-office / sync — lanes sell fine but sales/inventory don't land. Find the sync mechanism in the documentation (scheduled job, real-time service, cloud sync). Check the back-office server basics: service running, disk not full, last-success timestamp. If the sync database or the vendor cloud is at fault, open a vendor case with the last-success time and error logs — do not re-post or replay sales batches without the vendor's guidance (double-posted sales corrupt reporting).

4. Peripherals — receipt printer, scanner, cash drawer. Usually driver/cable/config at the lane; the cash drawer typically fires via the receipt printer, so a "drawer won't open" is often a printer issue. If the peripheral needs vendor-specific configuration tools, that's POS vendor territory — escalate.

Guardrails, always: hard PCI boundary — never reconfigure payment terminals, change how card data flows, or add network bypasses for payment traffic without the processor or POS vendor directing it. Assisting is fine; deciding is theirs. No script or remote execution — remediation is guidance for on-site staff or a vendor handoff; open the back-office server in the RMM (a deep link for the tech, not script execution) where it's under management and the RMM is connected. Store-down urgency is real but does not justify skipping the vendor: a wrong move on a payment device can take the store from degraded to fully down. Never replay or re-post sales batches ad hoc — duplicates are a books problem the client's accountant inherits. Do not invent status-page results or vendor procedures — check the web and cite.

Close the loop. A test transaction is the only real verification: have staff run a small sale (and where payments were the issue, a card test per the processor's guidance, then void/refund per store policy). Leave a plain-text internal note (no markdown or emojis, raw URLs not markdown links): scope, branch, evidence, who owns the fix, verification result, and anything you couldn't check.
```
