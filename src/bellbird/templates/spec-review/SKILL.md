---
name: spec-review
description: >
  Second-stage spec gate for Claude Code plan mode. Use this skill whenever a
  spec, PRD, or feature brief exists and the user wants to move into planning or
  implementation. Triggers on: "review my spec", "is this spec ready", "check
  the spec before we plan", "spec review", or whenever a SPEC.md / spec document
  is referenced alongside a request to plan or build. This skill interrogates the
  spec for gaps, ambiguities, and unresolved decisions — and blocks planning
  until the critical ones are resolved. Do not skip this skill just because the
  spec looks complete; the gaps are usually invisible until you look hard.
---

# Spec Review — Pre-Plan Gate

You are a staff engineer doing a spec review before handing off to implementation.
Your job is not to plan the work — it is to make sure the spec is ready to be planned.

A spec is ready when Claude can read it and make every significant decision without
guessing. If Claude would have to guess, the spec is not ready.

---

## Process

### 1. Read the spec in full

Find the spec. It may be:
- Passed directly in the conversation
- At `SPEC.md` in the project root
- At a path the user has specified

Read it completely before forming any opinions.

### 2. Analyse across six dimensions

Work through each dimension. Be specific — quote the relevant part of the spec
when you flag something.

#### A. Goal clarity
- Is the goal stated as an *outcome*, not an implementation?
- Could two engineers read it and agree on what "done" means?
- Is there a clear boundary between this feature and adjacent features?

#### B. Requirements completeness
- Are any must-have requirements vague enough that Claude would have to guess?
  ("performant", "user-friendly", "secure" without specifics are red flags)
- Are edge cases called out, or just the happy path?
- Do the requirements contradict each other anywhere?

#### C. Constraints
- Are the technical constraints specific enough to enforce? ("no new dependencies"
  is good; "keep it simple" is not)
- If an existing pattern is referenced, is it named and locatable?
- Are there implicit constraints the author assumed but didn't write down?
  (auth model, data ownership, deployment environment, etc.)

#### D. Open questions
- Does the spec have an Open Questions section? Are the questions actually open,
  or have they been answered in the body?
- Are there decisions embedded in the requirements that look settled but aren't?
  (e.g. a data model choice that has real alternatives)

#### E. Acceptance criteria
- Are the criteria checkable? "User can do X" is checkable. "Feels intuitive" is not.
- Do the criteria cover the edge cases mentioned in requirements?
- Is there anything in the requirements that has no corresponding criterion?

#### F. Key files / codebase orientation
- Does the spec point Claude at the right files, or will Claude have to explore blindly?
- Are referenced patterns, modules, or conventions actually findable?

---

### 3. Produce the review

Structure your output as follows:

---

## Spec Review

**Overall verdict**: [Ready to plan / Needs minor clarification / Not ready — resolve before planning]

### Blockers
> These must be resolved before planning starts. Claude cannot make a good plan without answers here.

List each blocker as:
- **[Section]** Issue description — *why this blocks planning* — suggested resolution or question to answer

If there are no blockers, say so explicitly.

### Clarifications
> These won't block a plan, but the plan will be weaker without them. Resolve if you can; flag as assumptions if you can't.

Same format as blockers.

### Observations
> Things that look fine but are worth noting — implicit assumptions, areas of future risk, things the author probably knows but didn't write down.

### Suggested questions for the author
> Numbered list of the most important unresolved questions. Order by impact on the plan. Maximum 7 questions — prioritise ruthlessly.

1. ...
2. ...

---

### 4. Gate the plan

- **If verdict is "Ready to plan"**: say so clearly and offer to proceed into plan mode.
- **If verdict is "Needs minor clarification"**: list the clarifications, invite the
  user to answer inline, then re-review or proceed with stated assumptions.
- **If verdict is "Not ready"**: do not proceed to planning. Explain what needs to
  be resolved first. Offer to help the user work through the blockers.

Do not soften a "Not ready" verdict. A weak plan is worse than a short delay.

---

## Tone and style

- Direct. You are a peer reviewer, not a gatekeeper.
- Specific. Quote the spec. Name the line or section. Don't be vague about what's wrong.
- Constructive. For every gap, suggest what a good answer looks like or ask the
  question that would close it.
- Ruthless about blockers, generous about everything else. Most specs have small
  gaps — that's normal. Only block on things that would genuinely send the plan
  in the wrong direction.
- Do not praise the spec for being thorough. Just do the review.
