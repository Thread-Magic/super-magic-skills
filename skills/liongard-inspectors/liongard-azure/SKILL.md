---
name: Liongard Azure Read
description: Answer Azure subscription questions via Liongard Azure inspector: resource inventory, spend signals, NSG changes, public exposure, unattached resources.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Azure Read

**When to use:** "What does <client> run in Azure?" / resource census, "did an NSG rule change / is anything exposed to the internet?", unattached-disk and orphaned-public-IP spend sweeps, or Azure change context on an outage or security ticket.

**Run it:** on one client — name the client and the Azure question.

## Prompt

```
Answer an Azure question for CLIENT_NAME from the Liongard Azure / Microsoft Cloud inspector. Read-only — no resource, NSG, or role changes originate here.

1. Find the Azure / Microsoft Cloud inspector(s) for this client and confirm each ran recently; date the data. Partners name and scope these differently (per-subscription vs. per-tenant) — enumerate ALL matching inspectors, don't grab the first. State scope honestly: "no resources found" means "none in inspected scope."
2. Read the values from the latest dataprints, verifying every field angle against the live dataprint (layouts shift with inspector versions):
   - Inventory → resource sections: VMs (size, OS, power state), storage accounts, app services, databases, VNets.
   - Exposure → NSG rules allowing inbound from any source on management ports (3389, 22), public IP assignments, storage accounts with public blob access. Exposure findings are security leads — flag and route remediation to a technician.
   - Spend signals → unattached managed disks, unassociated public IPs, stopped-but-allocated VMs, oversized VMs vs. observed role. Liongard captures configuration, not billing — present these as "cost-review candidates," never as dollar amounts.
   - Changes → check what changed for NSG modifications, new/deleted resources, role-assignment changes, with timestamps. On an outage ticket, lead with changes in the incident window.
   - Open-ended → ask in plain language, verify actionable answers with targeted reads.
3. Cross-check surprising inventory against ticket history: unclaimed new compute in a client subscription is a possible compromise (cryptomining is the classic) and escalates to security review.
4. Exposure and unexplained-resource findings surface even when unasked, flagged as security leads. Output: answer, evidence table, per-inspector data as-of timestamps, explicit scope ("subscription X only — no inspector on their second subscription" when true). Degradation: no Azure inspector → documentation and ticket history only, labeled "not instrumented"; recommend adding the inspector when Azure questions recur.
```
