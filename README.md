```
██████╗ ███████╗██╗     ██╗     ██████╗ ██╗██████╗ ██████╗
██╔══██╗██╔════╝██║     ██║     ██╔══██╗██║██╔══██╗██╔══██╗
██████╔╝█████╗  ██║     ██║     ██████╔╝██║██████╔╝██║  ██║
██╔══██╗██╔══╝  ██║     ██║     ██╔══██╗██║██╔══██╗██║  ██║
██████╔╝███████╗███████╗███████╗██████╔╝██║██║  ██║██████╔╝
╚═════╝ ╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝
```

*Claude Code Skills Manager - Template Distribution Tool*

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

## Included Templates

| Template | Type | Description |
|----------|------|-------------|
| `commit` | Command | Create commits with conventional format |
| `release` | Command | Bump version and update CHANGELOG.md |
| `release-hook` | Command | Chain the full release workflow — docs, changelog, version bump, tag, and push |
| `changelog` | Command | Add entries to the [Unreleased] section of CHANGELOG.md |
| `documentation` | Skill | Background context for documentation standards |

### Release workflow

The included commands support a chained release workflow:

1. **`/changelog`** — Add entries to `[Unreleased]` as you work
2. **`/release`** — Bump version, move unreleased entries to a version section, commit
3. **`/release-hook`** — Run the full chain: docs check → changelog review → version bump → tag → push

`/release-hook` accepts options:
- Bump type: `/release-hook minor`
- `--dry-run` — preview what would happen without executing
- `--skip-docs` — skip documentation validation
- `--no-push` — stop after tagging

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
