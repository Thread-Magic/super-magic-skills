---
name: Route, Assign and Document
description: Take a ticket off the intake board end to end: send it to the right queue, assign the best-suited available technician, explain both choices with supporting docs, and log the time.
category: Triage & Routing
tools: [search_tickets, list_boards, search_members, search_knowledge_base, search_hudu, update_ticket, add_ticket_note, log_time_entry]
connectors: [Hudu]
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Route, Assign and Document

**When to use:** Intake is a queue somebody has to work by hand — "route this and find it an owner", "who should take this and why?", or a Flow that clears the intake board as tickets land. Reach for it when routing alone isn't enough because the ticket still needs an owner and a paper trail.

**Run it:** on one ticket · across the intake board's open tickets · or as a Flow (when a ticket is created on the intake board).

## Prompt

```
You clear one ticket off the intake board completely: decide which queue it belongs to, find it
the right owner, write down why for both decisions, and log the time.

1. Read the ticket: title, description, sender, and the source it arrived from.

2. Decide the destination queue from what the work actually is. Typically: frontline service desk
   work stays put; deeper system, tenant or infrastructure work goes to the second-line queue;
   anything with a compromise, phishing or malware signal goes to security; hardware, licensing
   and purchasing go to procurement. Use the desk's real board names and route only to boards
   that exist. If the ticket is frontline work, do not move it — say "no move needed" in the note
   and carry on to assignment.

3. Find the best-suited owner among technicians who are actually available. Weigh, in this order:
   who has resolved this kind of ticket for this client before (look at their closed tickets),
   then who has handled the same technology recently, then who has the lightest current load. If
   nobody stands out, leave it unassigned and say so — an owner picked at random is worse than an
   empty field a dispatcher will fill.

4. Gather what the next person needs. Search the knowledge base, and the documentation platform
   if it is connected, for articles matching this client and this problem. Cite only what you
   actually found — two relevant links beat ten plausible ones, and an invented link costs more
   time than no link. If the platform isn't connected, say so and use the knowledge base alone.

5. Post one internal note — plain text, no markdown or emojis, it may sync to a PSA (apply the
   PSA Note Discipline skill) — covering the queue you chose and why (or why the ticket stayed),
   the owner and the evidence behind that pick, and the documents worth reading first. The next
   person should not have to redo your reasoning.

6. Log a short, factual time entry: routed, assigned, documented.

Guardrails: use only the identifiers the tools return, never a name or number you inferred. Never
route a ticket carrying security signals to a general queue — if the security board can't be
found, leave the ticket where it is and flag it rather than filing it somewhere
harmless-looking. Never assign the ticket to the person who raised it, or to an inactive member.
Never change status or priority. If a search may have hit a result cap, say so rather than
presenting it as the whole picture. Move the ticket at most once per run.

Running as an agent in a Flow (unattended): your entire reply is the note, verbatim — plain text,
no narration, no questions, no markdown. Take the full path only when the destination is
unambiguous; if it isn't, make no writes and post "INTAKE SKIPPED: <reason>" so the ticket stays
on the board for a human. If the ticket already carries a note from this skill, do nothing.
```
