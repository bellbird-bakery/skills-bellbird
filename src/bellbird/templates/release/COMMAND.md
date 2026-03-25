---
name: release
description: Bump the project version and update CHANGELOG.md by moving [Unreleased] entries to a new version section.
---

## User Input

```text
$ARGUMENTS
```

You are performing a version bump and changelog update for **{{project_name}}**.

## Execution Steps

### Step 1: Pre-flight Checks

1. Verify you're on the `{{main_branch}}` branch (abort if not)
2. Check for uncommitted changes and warn if present
3. Read the current version from `pyproject.toml`
4. Read the `[Unreleased]` section from `CHANGELOG.md`

### Step 2: Determine Bump Type

Based on user input (`$ARGUMENTS`):
- If user specified `patch`, `minor`, or `major` → use that
- If nothing specified → analyze the unreleased changelog entries:
  - **major**: Contains breaking changes or `BREAKING CHANGE`
  - **minor**: Contains `Added` entries (new features)
  - **patch**: Only `Fixed`, `Changed`, `Security`, etc.
  - Suggest the appropriate bump and ask for confirmation

### Step 3: Bump Version

Run `uv version --bump <type>` to update the version in `pyproject.toml`.

Also update `__version__` in `{{version_file}}` if it exists.

### Step 4: Update CHANGELOG.md

1. Replace the `## [Unreleased]` header content with an empty section
2. Insert a new version section below it: `## [X.Y.Z] - YYYY-MM-DD`
3. Move all unreleased entries under the new version section
4. Preserve the standard category order: Added, Changed, Deprecated, Removed, Fixed, Security

### Step 5: Commit

Stage `pyproject.toml`, `CHANGELOG.md`, and `{{version_file}}` (if updated), then commit:

```
release: vX.Y.Z
```

### Step 6: Report Results

Show:
- Previous version → New version
- Bump type applied
- Changelog entries included
- Suggested next steps (push, tag, etc.)

## Edge Cases

- **Not on {{main_branch}}**: Tell the user to switch branches first
- **Empty [Unreleased]**: Warn the user; ask if they want to proceed with an empty release or add changes first
- **No CHANGELOG.md**: Create one with the standard format
