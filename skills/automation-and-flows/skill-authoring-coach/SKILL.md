---
name: Skill Authoring Coach
description: Help a member write a good Super Magic skill: sharpen the description into a real trigger, structure the workflow, and add the guardrails it needs.
category: Automation & Flows
tools: [list_skills, load_skill, create_skill, update_skill, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Skill Authoring Coach

**When to use:** "Help me write a skill that does <workflow>" / "my skill exists but Magic never picks it — fix the description" / "review this skill draft before I start using it."

**Run it:** as a coaching task on request — you're workshopping a skill draft, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Workshop a member's skill draft against the authoring standard: description-as-trigger,
one workflow per skill, and guardrails that match the blast radius of what the skill does.
The skills family is in-app SuperAgent only — DEGRADATION: when skill editing isn't
available, produce the finished skill text for the member to paste into the skill editor.

1. Load the draft (open it if it already exists; otherwise take the pasted text) and check
   the existing skills for one that already covers the workflow — improving one
   beats duplicating it.

2. Workshop against the standard, in this order:
   - Description = trigger. Rewrite it as WHEN TO REACH FOR THIS, using the words the
     member would type. Test it: "if I typed <phrase>, would this description match?" A
     description that summarizes instead of triggering is the #1 authoring failure.
   - One workflow. If the draft does three unrelated things, split it and say why.
   - The prompt. Direct imperative instructions in plain English (describe the action —
     "change the status", "leave a note" — never internal tool names), branches inline
     ("If X -> Y; otherwise -> Z"), and an explicit final instruction saying what to output
     and in what format.
   - Guardrails inline. Match them to what the skill touches: any write needs a confidence
     gate and confirm-before-destructive; searches need result-cap honesty; PSA-bound notes
     need plain text; when-in-doubt-do-nothing where a wrong action is worse than none.

3. If the skill will run unattended inside a flow, apply the Unattended Output Discipline
   base skill and fold its contract into the draft.

4. Show the revised skill side-by-side with a one-line rationale per change. Strip anything
   unshareable while editing — credentials, API keys, person/board ids, client names —
   replace with placeholders and tell the member you did. On explicit confirmation only,
   create or update the skill; never write without showing the full revised text.

5. Suggest a quick test: 2–3 prompts that should trigger it and one that shouldn't. Coach,
   don't hijack — keep the member's intent and vocabulary; change structure and guardrails,
   not the workflow's goal.
```
