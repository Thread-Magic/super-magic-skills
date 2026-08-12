---
name: Default Contact Autofill
description: When a ticket arrives with no contact, look up the company's documented default contact, confirm with a search, and assign under a confidence gate.
category: Triage & Routing
tools: [search_tickets, search_clients, search_contacts, assign_contact, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Default Contact Autofill

**When to use:** Alert- or system-generated tickets arrive with a company but no contact, "fill in the default contact when a ticket doesn't have one", or contactless tickets fail to notify anyone or won't sync cleanly to the PSA.

**Run it:** on one ticket · across all contactless tickets · or as a Flow (when a ticket is created without a contact).

## Prompt

```
Contactless tickets stall — SLAs, notifications, and PSA sync all depend on a contact. When a
ticket arrives with none, assign the company's documented default contact, but only after
confirming that contact exists and only when the company is unambiguous.

1. Read the ticket. If it already has a contact, do nothing.

2. Resolve the company unambiguously by searching clients. If the company itself can't be
   determined with confidence, do nothing.

3. Look up the company's documented default contact from the desk's per-company mapping
   configured alongside the skill (e.g. "this client's primary/billing contact"). Confirm that
   contact exists by searching contacts. The contact comes from the documented mapping + a
   contact search only — never from free text in the ticket body, and never a fabricated
   contact.

4. If the company is unambiguous AND a documented default contact resolves to a real contact
   record → set it as the contact. Never overwrite an existing contact — this skill only fills
   an empty one.

5. Leave a plain-text note: that no contact was present and which default was assigned (and
   why).

Confidence gate: assign only when the company is unambiguous and the default contact resolves
to a real record. Any doubt → leave the ticket contactless and note that a default could not
be confidently assigned. The contact assignment + one note are the only writes — no status/
priority/owner changes. Notes plain text (PSA compatibility).

Running as a Flow: fires on ticket create; the flow can scope to a contactless condition where
available. Your entire reply is the note, verbatim: "DEFAULT CONTACT ASSIGNED: <contact> for
<company>." or "NO ACTION. Reason: <contact already present | company ambiguous | no default
configured | default not found>." Deterministic stops: contact already present → no action;
company ambiguous → no action; default unconfigured or unresolvable → no action. Assign at most
once; never overwrite an existing contact.
```
