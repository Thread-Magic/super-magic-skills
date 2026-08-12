---
name: Large File Share Guide
description: Draft reply-ready instructions for an end user to send a file that's too big for email, using the client's approved method — "the attachment bounced, tell the user how to send this big file."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Large File Share Guide

**When to use:** "User's attachment bounced for size — send them how to get the big file across." / "How do I send a 500 MB video to a client?" / "User keeps trying to email large files and they're being blocked."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for the specific problem of a file too big to email — the
attachment bounced or was blocked — routing the user to the client's approved large-file method
rather than a random consumer transfer site. This is the "too big for email" specialization of safe
file sharing; keep it focused on the size problem. Verify the method and external-sharing policy
before you write; when unsure — especially about external — ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's approved large-file method and external-sharing policy FIRST by checking the client's documentation and past tickets: usually a OneDrive/SharePoint share link,
   but some clients run a dedicated transfer tool or managed portal — and crucially whether sending
   to people OUTSIDE the company is allowed, restricted, or blocked. Note the mailbox attachment size
   limit if documented. If the method or external policy is unknown, ask the technician ONE question;
   a workaround against a blocking policy just produces a confusing error.
2. Determine the recipient from the ticket (internal colleague vs external client) and draft only
   that branch, since the external path depends on the verified policy.
3. Write the instruction block to end-user rules, one action per step with what-you'll-see cues:
   - The core reframe: "Big files don't go as attachments — you upload the file once and send a link.
     The recipient always gets the latest version and nothing bounces."
   - Upload + share on the client's platform: put the file in the sanctioned location, use the Share
     button, get a link. Cue the dialog and the audience choice — "People you choose" is the safe
     default; "Anyone with the link" means literally anyone it's forwarded to.
   - View-vs-edit in one line (do they need to change it or just receive it?).
   - External branch (ONLY if policy-verified as allowed): type the outside recipient's email in the
     share dialog rather than an open link; cue what they'll experience (a system email, possibly a
     one-time code — normal). If external sharing is blocked, say so plainly and give the client's
     documented alternative — never a workaround.
   - The don'ts, brief: no personal Dropbox/Google Drive/WeTransfer or consumer transfer sites for
     work files, and don't zip-and-split to sneak past the size limit.
   - Off-ramps: "If the share box won't accept the outside address, stop and reply — that's a policy
     setting, not your mistake." / "If the file is sensitive (contracts, payroll, health), reply
     first before sharing."
4. Assemble per the Email Baseline Standard.

Guardrails: policy verification before drafting is mandatory — the external-sharing capability
differs per tenant. Never instruct a consumer transfer site or personal cloud as a workaround — if
the approved path can't do it and the need is real, that's a tech/admin ticket, and the draft says
so. The audience-setting explanation and the sensitive-data off-ramp appear in every draft. No admin
steps (tenant sharing settings, attachment-size policy, DLP) in the user block. Localizable;
version-cautious dialog cues. The client's documentation is available only when those integrations are enabled; otherwise rely on the knowledge base and ticket history.
```
