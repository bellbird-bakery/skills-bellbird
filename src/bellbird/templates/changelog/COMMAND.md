---
name: changelog
description: Add an entry to the [Unreleased] section of CHANGELOG.md. Use this on feature branches to document changes.
---

## User Input

```text
$ARGUMENTS
```

You are adding a changelog entry to the `[Unreleased]` section of `CHANGELOG.md`.

## Execution Steps

### Step 1: Parse Input

From `$ARGUMENTS`, determine:
- The description of the change
- The category (if explicitly provided, e.g., "fixed: ..." or "added: ...")

### Step 2: Auto-Detect Category

If no explicit category, detect from keywords in the description:
- **Added**: add, new, create, implement, introduce, support
- **Changed**: change, update, modify, refactor, improve, migrate
- **Fixed**: fix, resolve, correct, repair, patch, bug
- **Removed**: remove, delete, drop
- **Deprecated**: deprecate
- **Security**: security, vulnerability, auth

If ambiguous, ask the user.

### Step 3: Format Entry

- Capitalize the first letter of the description
- Remove trailing period if present
- Remove the category keyword prefix if it was used for detection (e.g., "Fix login bug" → "Login bug" under Fixed)

### Step 4: Update CHANGELOG.md

1. Read `CHANGELOG.md` and find the `## [Unreleased]` section
2. Find or create the appropriate category subsection (e.g., `### Added`)
3. Add the entry as a bullet point: `- Description here`
4. Maintain standard category order: Added, Changed, Deprecated, Removed, Fixed, Security
5. Check for duplicate entries

### Step 5: Report

- Confirm which category was used (and whether it was auto-detected)
- Show the added entry
- If there are many unreleased entries (>20), suggest it may be time for a release

## Examples

```
/changelog Add customer notifications
→ ### Added
→ - Customer notifications

/changelog Fix login redirect bug
→ ### Fixed
→ - Login redirect bug

/changelog changed: Refactor order processing
→ ### Changed
→ - Refactor order processing
```

## Edge Cases

- **No CHANGELOG.md**: Create one with the standard Keep a Changelog format
- **No [Unreleased] section**: Add one at the top
- **Duplicate entry**: Warn the user and skip
- **No arguments**: Show current unreleased entries instead
