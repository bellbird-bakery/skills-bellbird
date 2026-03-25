# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bellbird is a CLI tool that distributes template Claude Code skills (SKILL.md files) into projects. It copies skill templates from its bundled `src/bellbird/templates/` directory into a target project's `.claude/skills/` directory.

## Development Commands

```bash
uv sync                  # Install dependencies
uv run bellbird list     # Run CLI during development
uv run bellbird init     # Test skill installation
```

## Architecture

Single-module CLI (`src/bellbird/cli.py`) with two subcommands:
- **`list`** — scans `templates/` for SKILL.md files, parses YAML frontmatter, prints names and descriptions
- **`init`** — copies selected template directories into `<project>/.claude/skills/<name>/`

Templates live in `src/bellbird/templates/<name>/SKILL.md`. Each SKILL.md has YAML frontmatter with `name` and `description` fields. The directory name is the fallback if frontmatter omits `name`.

## Adding a Template Skill

Create `src/bellbird/templates/<skill-name>/SKILL.md` with frontmatter:

```markdown
---
name: skill-name
description: What this skill does.
---

Skill instructions here...
```

## Key Details

- Python 3.14, managed with uv
- Build backend: hatchling
- Single dependency: pyyaml
- Entry point: `bellbird.cli:main`
- Version tracked in both `pyproject.toml` and `src/bellbird/__init__.py`
