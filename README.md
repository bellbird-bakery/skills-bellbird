# Bellbird

Template skills and commands for Claude Code projects.

## Install

```bash
uv tool install bellbird --from git+https://github.com/bellbird-bakery/skills-bellbird.git
```

## Usage

### List available templates

```bash
bellbird list
```

### Install templates into a project

```bash
# Interactive selection
bellbird init

# Install specific templates
bellbird init --skills documentation commit

# Install all templates
bellbird init --all

# Install into a different directory
bellbird init /path/to/project --all

# Overwrite existing templates
bellbird init --all --force
```

Skills are copied to `.claude/skills/<name>/SKILL.md` and commands to `.claude/commands/<name>.md` in the target project.

## Adding templates

Add a new template by creating a directory under `src/bellbird/templates/<name>/` with either:

- **`SKILL.md`** for skills (background context Claude loads automatically)
- **`COMMAND.md`** for commands (user-invoked via `/name`)

```markdown
---
name: my-template
description: What this template does.
---

Instructions here...
```
