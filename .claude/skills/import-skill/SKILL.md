---
name: import-skill
description: Import an existing Claude Code skill from another project and convert it into a bellbird template.
---

Import an existing skill into bellbird's template library.

## Usage

The user provides a path to either:
- A SKILL.md file directly (e.g., `~/projects/myapp/.claude/skills/commit/SKILL.md`)
- A skill directory containing a SKILL.md (e.g., `~/projects/myapp/.claude/skills/commit/`)
- A `.claude/skills/` directory to import multiple skills at once

## Steps

1. **Read the source SKILL.md** and check for existing YAML frontmatter (`name`, `description`).

2. **Determine the template name.** Use the `name` field from frontmatter if present, otherwise use the parent directory name. Confirm the name with the user if it's ambiguous. The name must be lowercase with hyphens (e.g., `my-skill`).

3. **Ensure valid frontmatter.** The template SKILL.md must have at minimum:
   ```yaml
   ---
   name: skill-name
   description: What this skill does.
   ---
   ```
   If frontmatter is missing or incomplete, read the skill content and draft a `name` and `description` for the user to confirm.

4. **Check for conflicts.** Look in `src/bellbird/templates/` for an existing template with the same name. If one exists, show a diff and ask the user whether to overwrite, rename, or skip.

5. **Copy to templates.** Place the file at `src/bellbird/templates/<name>/SKILL.md`. Copy any sibling files from the source skill directory as well (some skills include additional files).

6. **Verify.** Run `uv run bellbird list` to confirm the new template appears correctly.

## Batch import

When given a `.claude/skills/` directory, list all skills found and let the user select which to import. Process each selected skill through the steps above.
