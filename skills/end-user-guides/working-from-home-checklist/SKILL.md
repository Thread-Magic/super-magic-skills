---
name: Working From Home Checklist
description: Draft a reply-ready remote-work setup checklist for an end user — connectivity, VPN, phone, and how to get help — tailored to the client's stack.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Working From Home Checklist

**When to use:** "Send <user> a work-from-home setup checklist." / new-remote-arrangement tickets, storm/office-closure days, first-day-remote for a new hire / "user says nothing works from home."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready sanity checklist for a user setting up (or struggling) at home, ordered so
each item proves the layer below it — which turns "nothing works from home" into "item 3 fails," a
ticket the desk can act on. Draft only: show it to me first, send nothing.

1. Verify the client's remote stack FIRST, from their documentation and past tickets: does remote
   access go through a VPN (which one), a remote-desktop or virtual-desktop portal, or straight
   cloud apps? Is there a softphone remote workers need? Any remote-work policies (approved-device
   rules, hotspot allowance)? If the access model is unknown, ask the technician ONE question — it
   is the checklist's spine, and a list naming a VPN the client lacks misdirects every failure
   report.
2. Write the checklist in dependency order, to end-user rules — each item one check, with a
   what-success-looks-like cue and a note-and-continue instruction ("if this one fails, jot it
   down and keep going — then reply with your list"). Never alphabetize or reshuffle:
   1. Home internet works at all: any ordinary website loads on the work laptop. (Cue: "if even
      this fails, it's your home wifi or router — restarting the router fixes most; your provider
      owns the rest.")
   2. Sign-in and MFA: they can sign in to the laptop and approve the phone prompt.
   3. The access layer — exactly the one this client uses: VPN connects, or the remote-desktop
      portal loads and they can open their desktop, or cloud apps simply load. One item, their
      flavor.
   4. Mail and calendar open and show today's mail.
   5. Files: the documents they use daily open (mapped drive via VPN, or cloud files, per stack).
   6. Phone and meetings: the softphone registers or a Teams test call works — name the actual
      telephony app from the documentation; skip if the client has none.
   7. How to get help when the work laptop is the problem: the desk's phone number and the portal
      or email reachable from a personal device, because "email the helpdesk" is useless when
      email is what's broken. Take the contact channel from the documentation — never invent a
      phone number or portal URL.
3. Add two environment notes, brief: work laptops on home wifi are fine per the documentation,
   but public and hotel wifi has its own captive-portal trap; and household bandwidth ("video
   calls stutter when someone else is streaming").
4. Open with the off-ramp framing: "Run through these in order — most take under a minute. If
   everything passes, you're set. If anything fails, reply with the item numbers that failed."
5. Assemble per the Email Baseline Standard.

Guardrails: keep it to roughly 7 items; extras (monitor, ergonomics, home printer) only if the
ticket asked. No admin steps and no home-router configuration beyond "restart it." Localizable.
Docs tools exist only when enabled.
```
