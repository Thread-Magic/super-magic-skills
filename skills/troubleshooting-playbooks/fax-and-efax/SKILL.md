---
name: Fax & eFax
description: Work fax tickets — analog line dead, ATA-based fax failing or corrupting pages, eFax/cloud-fax not sending or receiving — across the line / ATA-settings / service-portal matrix, with healthcare-grade reliability expectations taken seriously.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Fax & eFax

**When to use:** Faxes aren't sending or being received on a physical fax machine; faxes partially transmit, arrive garbled, or fail only on long documents (classic ATA symptoms); an eFax portal / fax-to-email stopped working or inbound faxes stopped arriving; or a healthcare or legal client reports fax failure (treat as workflow-critical, not legacy).

**Run it:** on the one ticket you're working — a tech drives this with on-site staff and the carrier/vendor; not unattended.

## Prompt

```
Fax is not dead — in healthcare, legal, and finance it is a compliance-anchored workflow with hard reliability expectations. Modern fax fails at one of three layers: the line itself (analog or its VoIP replacement), the ATA that bridges a physical fax machine onto VoIP, or the eFax service that replaced the machine entirely. Identify the layer before anyone re-sends the same document a sixth time.

Work it in this order:

1. History first. Search this client's past tickets for fax. Fax setups are bespoke; the prior ticket usually documents which architecture this client actually has, which is half the diagnosis.

2. Docs second. Check the client's documentation and knowledge base for the fax architecture: true analog line (POTS), fax-over-VoIP through an ATA, or a cloud eFax service — plus the carrier or eFax vendor, the fax number(s), and where they terminate. Documentation may be absent for this tenant — fall back to the knowledge base and say what you could not check.

3. Set expectations by vertical. For healthcare and similar clients, ask what the fax carries (referrals, orders, prescriptions) and whether there is an interim path (the eFax portal, a second line) — the workflow may need a bridge before the fix.

4. Identify the architecture and versions. Which of the three layers exists here, ATA make/model/firmware if present, and whether anything changed: carrier migration (POTS lines are being retired and migrated to VoIP widely — a "line" that used to work may not be analog anymore), phone-system replacement, or an eFax vendor change.

5. Evidence before theory. The failing direction (send, receive, both), the machine's error code or transmission report, whether failures are total or partial (fails mid-page, long documents only), and one concrete failed fax: destination number, time, page count.

6. Branch:
   - Analog line — total failure on a POTS-connected machine. Guide on-site: plug a handset into the wall jack — dial tone or not is the fork. No dial tone -> carrier ticket (line fault or, increasingly, a quiet POTS retirement); the desk's role is opening it with the carrier and tracking. Dial tone but no fax -> the machine or its settings; test with a known-good fax number. Nobody on the desk can fix copper — when the line is dead it's carrier only.
   - ATA / fax-over-VoIP — partial pages, garbled output, long-document failures, intermittent success. This is the signature of fax on a compressed voice path. Check the ATA's fax handling per its docs: T.38 fax relay vs G.711 pass-through, and error correction (ECM) settings on the machine; a mismatch between ATA config and what the carrier's platform supports is the usual cause. Baud step-down (9600) is a legitimate stabilizer. Escalate when settings match vendor guidance and failures persist — the carrier must confirm T.38 support end-to-end; this is a carrier/VoIP-vendor conversation with the failed-call examples attached.
   - eFax service — portal or fax-to-email failing. Check the vendor's status page first (on the web). Then the boring causes: inbound notification emails landing in spam/quarantine, a changed user password breaking the portal login, sender not on the account's authorized list, attachment format/size outside the vendor's limits. Escalate when the vendor's platform is failing or a number was ported/misrouted — vendor case with fax IDs and timestamps from the portal's own log.
   - Receive-only failure — sends fine, nothing arrives. Verify the number still routes correctly: a recent port, carrier migration, or forwarding change can silently send inbound faxes elsewhere. Test by sending to the number from a known source and tracing where it lands. Escalate when routing is wrong at the carrier level — carrier ticket; number routing is theirs.

Guardrails to hold throughout: no script or remote execution — remediation is guidance for on-site staff, ATA admin-panel guidance for the tech, or a carrier/vendor case. Never read, transcribe, or attach fax content into ticket notes — for healthcare and legal clients the content is regulated; reference metadata (time, page count, destination) only. Do not promise fax reliability on a voice-optimized VoIP path — if the client needs healthcare-grade reliability, say plainly that T.38 end-to-end or a cloud eFax service is the defensible architecture, and treat that as a recommendation, not an action taken. Carrier and number-routing faults are vendor-only — open the case, attach evidence, track it; do not improvise around it. Do not invent vendor limits, status-page results, or ATA settings — look up the exact model/vendor on the web and cite.

Close the loop. A successful test fax in the failing direction — with a transmission confirmation or portal delivery record — is the only verification that counts here; for compliance-sensitive clients, note the confirmation artifact in the ticket. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): architecture, direction, branch, evidence, fix or carrier/vendor case reference, verification result.
```
