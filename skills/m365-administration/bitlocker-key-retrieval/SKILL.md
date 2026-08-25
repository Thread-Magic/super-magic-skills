---
name: BitLocker Key Retrieval
description: Handle BitLocker recovery key requests with identity verification, device-ownership match, secure delivery, key rotation, and audit note.
category: M365 Administration
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# BitLocker Key Retrieval

**When to use:** Anyone asks for a BitLocker recovery key or a device is stuck at the blue recovery screen — a user stuck at the recovery prompt, a device prompting after a BIOS/firmware update or hardware change, a tech needing the key for a legitimate repair/reimage, or data recovery from a disk pulled out of a decommissioned machine. A BitLocker recovery key unlocks the entire disk — handing it to the wrong person is handing over the machine's data. This request is an identity verification problem first and a console lookup second, and the key never lands in the ticket.

**Run it:** on one request — you verify identity and build the audit trail, a technician does the Entra/Intune lookup and delivers the key over a verified channel (not a Flow: it needs a human at the console).

## Prompt

```
You verify identity and build the audit trail; the tech does the Entra/Intune lookup and
delivers the key over a verified channel. Apply the Write Guardrails base skill — never treat
a request as verified on intention, and when in doubt about identity, ownership or the
trigger do nothing and escalate per the client's security process. The key never appears in
tickets, notes, chat or email.

1. Verify identity FIRST, before any lookup. Call back a number already on file (look the
   contact up — never a number supplied in the ticket), or follow the client's documented
   verification procedure (Connector Degradation base skill if their documentation isn't on).
   A key request is a known social-engineering play and VIP pressure is the costume: no
   verification, no key, whatever the seniority or urgency. A third party asking "on behalf
   of" the user, or about someone else's device, is verified with the device's owner or the
   client's IT authority, not the requester.

2. Match requester to device. Have the user read out the recovery key ID from the recovery
   screen — not a guessed device name — and confirm it maps to a device whose registered
   owner is the verified requester, or that the client authority approved a repair. The key ID also ensures the right key when the user has several devices.

3. Why did recovery trigger? Firmware or BIOS update, TPM change, hardware swap and
   boot-order change are the benign classics. No plausible trigger — or prompts across
   several devices at once — is a security event before a support task: escalate per the
   client's security process before unlocking anything.

4. Retrieve. The tech looks the key up by key ID in Entra (device object, BitLocker keys) or
   Intune. If the device never escrowed, say so — never imply the data is recoverable when
   the key does not exist. Escalate to data-recovery options, flag the
   escrow gap as a finding, and check whether stale-device-cleanup deleted the object.

5. Deliver over a verified channel only: read the key to the verified user on the callback,
   or use the client's documented secure channel. Never paste it into the ticket, a
   note, email or chat — those all sync and persist.

6. Rotate after use. Once the device is unlocked and healthy, the tech rotates the recovery
   key (Intune supports rotation on Entra-joined devices; verify current behavior) so the
   disclosed key is dead — part of the job, not optional. If rotation isn't available for
   this device type, record that the disclosed key remains valid: residual risk for the note.

7. Audit note (PSA Note Discipline base skill: plain text, no markdown): requester,
   verification method, device and key ID — the ID is safe, the key is not — why recovery
   triggered, delivery channel, rotation or residual-risk flag, and the tech who executed. It
   proves the control worked without weakening it.
```
