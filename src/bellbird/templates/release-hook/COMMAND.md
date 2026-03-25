---
name: release-hook
description: Chain the full release workflow — docs, changelog, version bump, tag, and push.
---

## User Input

```text
$ARGUMENTS
```

You are running the full release workflow for **{{project_name}}**. This chains multiple release steps together with confirmation gates between each phase.

## Options

Parse `$ARGUMENTS` for:
- **Bump type**: `patch`, `minor`, or `major` (passed through to the version bump step)
- **`--dry-run`**: Show what each step would do without executing. Print `[DRY RUN]` before each action.
- **`--skip-docs`**: Skip the documentation validation step
- **`--no-push`**: Stop after tagging (do not push to remote)

If no bump type is specified, auto-detect from changelog entries (same logic as `/release`).

## Execution Steps

### Step 1: Pre-flight Checks

1. Verify you're on the `{{main_branch}}` branch — abort if not
2. Run `git status` — warn if there are uncommitted changes and ask to proceed or abort
3. Run `git pull --dry-run` to check if the local branch is behind the remote — warn if so
4. Read `CHANGELOG.md` and verify `[Unreleased]` has entries — warn if empty and ask whether to proceed

If any check fails, explain the issue and stop. Do not silently continue.

### Step 2: Documentation Check

> Skip this step if `--skip-docs` was passed.

Scan the project for documentation staleness:

1. Check that `README.md` exists
2. If a `docs/` directory exists, scan for broken internal links or references to removed files
3. If `pyproject.toml` has a version, verify it appears correctly in documentation where referenced
4. Report any issues found and ask the user whether to fix them now or continue

This is advisory — the user can choose to proceed even if issues are found.

### Step 3: Changelog Review

1. Read the `[Unreleased]` section of `CHANGELOG.md`
2. Display the entries grouped by category (Added, Changed, Fixed, etc.)
3. Ask the user to confirm the entries are complete, or if they want to add/edit anything before proceeding

Wait for explicit confirmation before continuing.

### Step 4: Version Bump

Run the `/release` command logic:

1. Determine the bump type (from `$ARGUMENTS` or auto-detect from changelog categories)
2. Run `uv version --bump <type>` to update `pyproject.toml`
3. Update `__version__` in `{{version_file}}` if it exists
4. Move `[Unreleased]` entries to a new `## [X.Y.Z] - YYYY-MM-DD` section in `CHANGELOG.md`
5. Stage `pyproject.toml`, `CHANGELOG.md`, and `{{version_file}}`
6. Commit with message: `release: vX.Y.Z`

Show the version change (old → new) and ask for confirmation before committing.

### Step 5: Git Tag

1. Read the new version from `pyproject.toml`
2. Create an annotated tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
3. Show `git log --oneline -1` and `git tag -l --sort=-version:refname | head -5` to confirm

### Step 6: Push

> Skip this step if `--no-push` was passed.

1. Show what will be pushed: the release commit and the new tag
2. Ask for final confirmation
3. Run `git push && git push --tags`
4. Confirm the push succeeded

### Step 7: Summary

Display a final summary:

```
Release complete for {{project_name}}:
  Version: X.Y.Z-1 → X.Y.Z
  Tag:     vX.Y.Z
  Branch:  {{main_branch}}
  Pushed:  yes/no
```

## Dry Run Behaviour

When `--dry-run` is active:
- Run all checks and display all information normally
- Prefix each action that would modify state with `[DRY RUN]`
- Do NOT execute any git commits, tags, version bumps, or pushes
- At the end, summarize what _would_ have been done

## Edge Cases

- **Not on {{main_branch}}**: Abort with clear instructions to switch branches
- **Uncommitted changes**: Warn and ask — do not silently stash or commit
- **Empty [Unreleased]**: Warn and ask if user wants an empty release
- **Tag already exists**: Warn that `vX.Y.Z` already exists and abort
- **Push fails**: Show the error, suggest `git push` manually, do not retry
- **No remote configured**: Skip push step and inform the user
