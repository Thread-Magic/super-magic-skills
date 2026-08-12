---
name: Windows Update Client Failures
description: Diagnose Windows Update client failures: 0x8024xxxx and 0x800Fxxxx errors, update loops and rollbacks, and stuck scans across WU, WSUS, and Intune sources.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Windows Update Client Failures

**When to use:** One machine (or a handful) erroring on updates with an 0x8024xxxx / 0x800Fxxxx / 0xC1900xxx code; an update that installs, reboots, then rolls back ("We couldn't complete the updates"); "checking for updates" hanging, or a machine compliant in one console but stale in another; or RMM patch reports flagging a device repeatedly failing the same KB.

**Run it:** on the one device ticket you're working — a tech works it hands-on; not unattended.

## Prompt

```
You are diagnosing a single machine failing Windows updates. Two questions decide most of these tickets: (1) where does this machine think updates come from, and (2) what is the exact error code. Skipping to "reset Windows Update components" without those wastes the ticket. Fleet-wide failures point at the infrastructure — that's the wsus-patching-infrastructure playbook, not this one. You run no scripts from here; DISM/SFC/registry checks are guidance for the tech or a deep-link handoff to the RMM tech console.

1. History first. Search this device's and this client's past tickets for the same KB/error. Same KB failing across many machines -> known-bad update or infrastructure (WSUS approval/content) — check the vendor's known-issues page on the web and consider wsus-patching-infrastructure before touching individual machines. One machine -> continue here.

2. Docs second. Check the client's documentation and knowledge base for the patch design: WSUS server? Intune update rings? RMM-driven patching (pair with the RMM's own status rather than fighting it)? Dual scan/co-management history? Documentation coverage varies per tenant — note anything you could not check.

3. Identify the update source on the machine — do not assume. Guide the tech: Get-WindowsUpdateLog is heavy; faster truth is the registry/policy view — HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate (WUServer set = WSUS), MDM diagnostics / dsregcmd /status for Intune enrollment, and Settings -> Windows Update -> the "managed by your organization" banner. Update-source confusion is a first-class root cause: a machine pointed at a decommissioned WSUS never updates and never errors loudly; a machine with both WSUS policy and Intune rings can scan against the wrong source. If the source is stale/conflicting, fix the pointing (per the client's documented patch design — confirm it with the client's patch owner, don't invent one) before any repair ladder.

4. Get the code before theorizing. Exact error from Settings/Update history or CBS. Decode by family, verifying the specific code on the web rather than memory (codes are reused across contexts):
   - 0x8024xxxx (Windows Update agent) — commonly transport/source: can't reach the source, WSUS content missing, proxy/TLS interception. Test reachability to the actual source found in step 3.
   - 0x800F0831 / 0x800F09xx / 0x800F081F (servicing/CBS) — component store corruption or a missing servicing chain payload -> the repair ladder below.
   - 0x80070070-family (disk full) — check free space before anything clever; feature updates need tens of GB.
   - 0xC1900xxx (feature-update/setup) — driver/app compatibility; read the SetupDiag output rather than guessing.

5. The component-store repair ladder — in order, no skipping:
   a. DISM /Online /Cleanup-Image /ScanHealth then /RestoreHealth (note: on WSUS-managed machines RestoreHealth may need /Source or GPO "repair from Windows Update" allowed — a RestoreHealth 0x800f081f on a WSUS client is usually source, not corruption).
   b. sfc /scannow AFTER DISM (SFC repairs FROM the store DISM just fixed — running SFC first can "repair" from a corrupt store).
   c. Retry the update. Only if still failing: rename SoftwareDistribution/Catroot2 (the "reset components" step — safe but destroys update history and re-downloads everything; do it once, deliberately, not as a ritual, and never as step one — it destroys the evidence the diagnosis needs).
   d. Still failing -> in-place upgrade repair (keeps apps/files) is the honest next step; schedule it with the user rather than looping the ladder.

6. Rollback loops (installs then reverts). Find the failing component: SetupDiag for feature updates, CBS log around the reboot for cumulative ones. Common causes: a filter driver (AV/backup agent) or bad third-party driver. Pausing the SPECIFIC update while the vendor issue is confirmed is legitimate; disabling updates wholesale, blocking updates, or setting indefinite deferrals to close a ticket is not — note the re-review date instead.

7. Verify and note. Success = the previously failing KB shows Installed in update history and the compliance console the client actually uses reflects it (allow a check-in cycle). Leave a plain-text internal note (PSA-safe: no markdown or emojis): update source found, error code verbatim, ladder steps run and results, action or handoff, verification and time.

Many machines failing the same way = infrastructure. Stop and switch to wsus-patching-infrastructure (or the Intune/RMM equivalent conversation).
```
