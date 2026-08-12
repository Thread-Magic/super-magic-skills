---
name: Messenger Deployment Audit
description: Report which clients use Messenger versus which are entitled — deployed and active vs. silent — surfacing adoption gaps worth a rollout conversation.
category: Voice & Messenger
tools: [search_clients, search_tickets, list_boards]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Messenger Deployment Audit

**When to use:** "Which of our clients have Messenger deployed and active?" / "who's entitled to Messenger but never uses it?" / QBR prep for one client's channel adoption story / after a Messenger rollout push, did the deployments stick?

**Run it:** across all active clients (or one client for QBR prep) — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Every client without Messenger deployed is still emailing and calling — the expensive
channels. Map entitled vs. deployed vs. actually-used from observable chat activity, and hand
back a gap list with the evidence behind each classification.

1. List the active clients. If the tenant's client records expose a Messenger/deployment
   status field, use it as the entitlement/deployment baseline; if not, say the baseline is
   inferred (step 3) — do not present inference as configuration.

2. Measure actual usage: read the chat/Messenger-sourced tickets per client over the window
   (default 90 days). Split searches per client or board where volumes are high, and state
   result-cap exposure — an undercount here mislabels a client as silent.

3. Classify each client:
   - Active — chat-sourced tickets in the window.
   - Deployed but silent — deployment status says enabled (or historical chat tickets exist)
     but zero chats in the window.
   - Not deployed / unknown — no deployment signal and no chat history ever.

4. For deployed-but-silent clients, pull one distinguishing fact where cheap: did they chat
   in a prior window (usage decayed — a different conversation than never-adopted)?

5. Output the report: counts by classification, then the gap list — client, classification,
   evidence (last chat date or "none found"), and the suggested motion (rollout for
   never-deployed; re-introduction or champion outreach for decayed). Order by client
   size/ticket volume so the biggest deflection wins come first.

6. Note the caveat block: window used, result-cap exposure, and whether deployment status was
   read from records or inferred from activity.

Guardrails: inference honesty is the whole product — "no chat tickets found" is evidence of
non-usage, not proof of non-deployment (a widget can be installed and unused); label every
classification with its evidence type. Entitlement may not be visible from ticket data at
all; if the tenant tracks it outside Thread, say the entitlement column needs that source
rather than guessing. Read-only: no client records are modified, no outreach is sent. Zero-
chat clients may be zero-chat by choice — the report recommends conversations, not conclusions
about client health. Sanitize for any exec-facing export: client names are fine internally; no
contact-level naming needed.
```
