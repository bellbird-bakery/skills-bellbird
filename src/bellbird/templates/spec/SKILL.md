---
name: spec
description: Draft a feature spec by researching the codebase, docs, and git history — then present a complete draft for the user to refine.
---

You are drafting a feature specification. Your job is to do the research and produce a complete first draft — not to interview the user section by section. The user provides the intent; you do the legwork.

## Workflow

### 1. Get the Intent

Ask the user one question: **"What feature or change are you speccing out?"**

If their answer is clear enough to start research, start. If it's genuinely ambiguous (you can't tell what area of the codebase is involved), ask one clarifying question — no more.

### 2. Research the Codebase

Before writing anything, gather context autonomously:

- **Read project docs** — CLAUDE.md, README, architecture docs, any existing specs
- **Explore relevant code** — find the modules, patterns, and types that this feature would touch
- **Check git history** — recent commits and PRs in the relevant area for context on what's in flight
- **Identify constraints** — language, framework, build system, existing patterns, test conventions
- **Map key files** — the specific files and directories that implementation would involve

This is where you add the most value. The user shouldn't have to tell you what's in their own codebase.

### 3. Draft the Full Spec

Produce a complete spec draft in one pass. Fill in every section you can from your research. Where you lack information that only the user would know (business decisions, priority calls, stakeholder context), mark it clearly with `[TODO: ...]` rather than leaving the section empty or asking upfront.

Use this format:

```markdown
# [Title]

> [One-sentence summary]

---

## Context

[2-4 sentences. Ground this in what you found in the codebase and docs — current state, relevant recent changes, why this matters.]

---

## Goal

[Outcome, not implementation]

---

## Scope

**In scope**
- ...

**Out of scope**
- ...

---

## Requirements

### Must have
- [ ] ...

### Nice to have
- [ ] ...

---

## Constraints

- **[Category]**: [constraint]

---

## Key Files & Areas

```
[file tree with annotations — derived from your codebase exploration]
```

---

## Open Questions

- [ ] ...

---

## Decisions Made

- ...

---

## Acceptance Criteria

- [ ] ...
```

### 4. Present for Refinement

Show the full draft to the user. Highlight:
- Any `[TODO: ...]` items that need their input
- Open questions you surfaced during research
- Assumptions you made that they should validate

Let the user edit, correct, and refine. Update the spec based on their feedback.

### 5. Save and Hand Off to Spec Review

Save the spec to the location the user specifies (default: `SPEC.md` in the project root). Then offer to run the **spec-review** skill:

> "Spec saved. Want me to run a spec review to check for gaps before you move to planning?"

If the user accepts, invoke the `spec-review` skill against the saved spec. If the review surfaces issues, help the user resolve them and update the spec in place.

## Guidelines

- **Research first, ask second.** Only ask the user things you cannot find in the codebase, docs, or git history.
- **One draft, not nine questions.** Present a complete spec for the user to react to — it's faster to edit a draft than to answer an interrogation.
- **Be specific about files.** Key Files should contain actual paths you verified exist, not placeholders.
- **Flag gaps honestly.** Use `[TODO: ...]` for things you don't know. Don't invent requirements.
- **Keep it concise.** A good spec is short enough that someone will actually read it.
