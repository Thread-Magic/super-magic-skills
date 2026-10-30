---
name: Deployment Compliance Grader
description: Grade each engineer's mandatory deployment checklist on a ticket against the client's onboarding guide in your documentation tool, flag engineers who logged work without the checklist, and flag stale documentation.
category: QA & Closure
tools: [search_tickets, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: single
flow: yes
role: [Service & Ops Manager, Technician]
outcome: [Staff Enablement, Risk & Compliance]
---

# Deployment Compliance Grader

**When to use:** Your engineers paste a mandatory checklist (a text-expander form) into a time entry or note on every new-user, new-workstation or device-setup ticket. You want every completed deployment graded against the client's documented setup steps, so you can see who needs training, who is doing great work, and which client guides are out of date.

**Run it:** on one ticket · or as a Flow (when a deployment ticket moves to its review or closed status). The grade lands on a weekly audit ticket you open each week, so leads review one ticket instead of hundreds. It also works as the grading step a Skill Director (`automation-and-flows/skill-director`) hands off to.

## Prompt

```
Grade the deployment work on this ticket and post one report to this week's audit ticket.

1. Read the whole ticket, every note and every time entry. A checklist is any entry that starts with your fixed heading (for example "This is a mandatory compliance form. It is not optional."). For each one capture the engineer, the date, and every line's answer. Drop-downs read "Not Completed" or a selected value; "N/A" is a valid, complete answer.

2. Non-compliance: an engineer who logged any note or time on this ticket but has no checklist entry is non-compliant. Capture their name, dates, entry type and hours. Ignore system and automated entries.

3. Find the client's setup guide in your documentation tool: search that client for "PC setup", "onboarding", "provisioning" and "deployment", then without the client filter if nothing comes back. Record its link and last-updated date. If the documentation tool is not connected, grade against the checklist alone and say so.

4. Compare each checklist to the guide: done, missed, or marked done but blank or wrong. Flag guide steps the checklist does not cover.

5. Grade each engineer who used the checklist 1 to 5 (5 all done, 4 minor gaps, 3 notable gaps, 2 significant gaps, 1 largely incomplete). Non-compliant engineers get 1. The ticket grade is the average across all engineers, rounded down.

6. Documentation freshness: if an engineer's notes contradict the guide (a tool the client no longer uses, a changed step, a new app), list each contradiction and recommend the guide update. Quote the note; never guess.

7. Report, plain text, no markdown or emojis:
Deployment grade - ticket <number> - overall <X>/5
Per engineer: name, date, grade, what was done, what was missed, one-line justification.
Engineers who did not use the checklist: name, dates, entry type, hours (or "None").
Steps missed by everyone. Guide used: <name, link, last updated>.
Documentation freshness: <contradictions and suggested updates, or "No changes suggested">.

8. Post it as one internal note on the open ticket titled "Weekly Deployment Audit week of <date>" (your timezone). Several match: prefer today's date, else the newest. None open: do not create one or post anywhere else; stop and say so.

Never post the grade on the source ticket or contact the client. Never invent answers, steps or dates.

As a Flow: your entire reply is the report. If no weekly ticket is open, make no changes and reply with one line saying so.
```
