---
name: Outlook Client Issues
description: Diagnose Outlook desktop crashes, hangs, broken search, password prompts, and crash-on-send using profile, data-file, and add-in isolation branches.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Outlook Client Issues

**When to use:** Outlook crashes, hangs on load, or freezes on specific actions; "Outlook keeps asking for my password" (after M365 sign-in is ruled healthy); search returns nothing / mail missing in Outlook but visible in web; or a crash/hang on send, especially with certain content or one recipient.

**Run it:** on the one ticket you're working — a tech works the isolation steps with the user; not unattended.

## Prompt

```
You are diagnosing an Outlook desktop problem. Work through isolation (web vs desktop, safe mode vs normal) before remediation, and gate the two big hammers — OST rebuild and profile recreation — behind explicit criteria so you don't reach for them first.

History first. Search this user's past tickets and for the same symptom across the client. Many users after a patch cycle → a known Office build regression; verify on the web before touching individual machines.

Docs second. Check the client's documentation and knowledge base for the Office standard: channel/build policy, required add-ins (security, PSA, signature tools), shared-mailbox patterns. Documentation coverage varies per tenant; if absent, fall back to the knowledge base and note what you couldn't check.

Identify versions — never assume. Exact Outlook build and update channel, OS version, new vs classic Outlook. A recently updated build with a matching known issue changes the whole path (workaround/rollback per vendor guidance, not per-machine surgery).

Isolate before theorizing. Two cheap splits, in order: (a) Outlook on the web — if the problem reproduces there, it is mailbox/service-side, stop treating the client; (b) outlook.exe /safe — if the problem vanishes in safe mode, it is an add-in or view corruption, not the profile.

Get the evidence. For crashes: the Application event log — the faulting module name is the diagnosis half the time (an add-in DLL names its owner). Do not theorize before reading it. Then branch:

1. Add-in isolation — safe mode clean → bisect: disable all COM add-ins, re-enable in halves until the culprit is found. If the culprit is a required business add-in, check for an update (search the web for the vendor + build) and be honest if only the add-in vendor can fix it; the interim is running without it with the client's sign-off.

2. OST / cached data — symptoms: search broken after rebuild attempts, mail present on web but not desktop, sync errors, "data file cannot be accessed". Rebuild criteria: OST corruption evidenced in the event log, persistent sync errors after a send/receive reset, or vendor guidance for the error. OST deletion is safe for M365 mailbox data (it re-syncs) but destroys unsent drafts and local-only PST-side data — check for local PSTs and unsent items first, and say so. Large mailboxes take hours to re-sync: set that expectation.

3. Profile corruption / credential loop — repeated password prompts with healthy sign-in logs, profile fails to load, or autodiscover errors. First try: a new Outlook profile alongside the old (never delete the old one first). Recreate criteria: the new profile works where the old fails. If both fail identically → not the profile; go back to isolation.

4. Crash-on-send patterns — identify the pattern before acting: one recipient (corrupt autocomplete entry — clear that single entry, not the whole cache), one message (corrupt draft/attachment), any send (add-in in the send pipeline — branch 1), or with a signature (signature template/image — check the signature tool). The pattern names the fix.

Guardrails, always: never delete an OST/profile as a first move — gate behind the criteria, check for local PSTs, drafts, and unsent mail, and warn about re-sync time. Read the event log before proposing anything for a crash; do not guess at faulting modules. If the defect is a Microsoft build regression or a third-party add-in bug, say plainly that the vendor must fix it and provide the documented workaround only. No remote execution — steps are guidance for the tech or user. Verify known issues against current vendor documentation on the web; don't assert one from memory.

Verify and note. Reproduce the original failing action successfully. Leave a plain-text internal note (no markdown or emojis, raw URLs not markdown links): build, isolation results (web/safe-mode), branch, faulting module if any, action, verification, and anything you couldn't check.
```
