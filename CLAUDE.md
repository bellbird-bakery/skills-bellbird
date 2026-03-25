# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bellbird is a CLI tool that distributes template Claude Code skills and commands into projects. It copies templates from its bundled `src/bellbird/templates/` directory into a target project's `.claude/` directory.

## Development Commands

```bash
uv sync                  # Install dependencies
uv run bellbird list     # Run CLI during development
uv run bellbird init     # Test installation
```

## Architecture

Single-module CLI (`src/bellbird/cli.py`) with two subcommands:
- **`list`** — scans `templates/` for SKILL.md/COMMAND.md files, parses YAML frontmatter, prints names and descriptions grouped by type
- **`init`** — copies selected templates into the target project

Templates live in `src/bellbird/templates/<name>/`. Each directory contains either:
- **`SKILL.md`** → installed to `<project>/.claude/skills/<name>/SKILL.md` (directory copy)
- **`COMMAND.md`** → installed to `<project>/.claude/commands/<name>.md` (single file)

Each template file has YAML frontmatter with `name` and `description` fields. The directory name is the fallback if frontmatter omits `name`.

## Adding Templates

Create `src/bellbird/templates/<name>/SKILL.md` or `COMMAND.md` with frontmatter:

```markdown
---
name: template-name
description: What this template does.
---

Instructions here...
```

## Key Details

- Python 3.14, managed with uv
- Build backend: hatchling
- Single dependency: pyyaml
- Entry point: `bellbird.cli:main`
- Version tracked in both `pyproject.toml` and `src/bellbird/__init__.py`
