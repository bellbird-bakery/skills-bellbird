# Bellbird

Template skills for Claude Code projects.

## Install

```bash
uv tool install bellbird --from git+https://github.com/bellbird-bakery/skills-bellbird.git
```

## Usage

### List available skills

```bash
bellbird list
```

### Install skills into a project

```bash
# Interactive selection
bellbird init

# Install specific skills
bellbird init --skills documentation

# Install all skills
bellbird init --all

# Install into a different directory
bellbird init /path/to/project --all

# Overwrite existing skills
bellbird init --all --force
```

Skills are copied to `.claude/skills/<name>/SKILL.md` in the target project.

## Adding templates

Add a new template by creating `src/bellbird/templates/<name>/SKILL.md` with frontmatter:

```markdown
---
name: my-skill
description: What this skill does.
---

Skill instructions here...
```
