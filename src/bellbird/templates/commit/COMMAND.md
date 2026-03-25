---
name: commit
description: Stage changes and create a commit with a well-formatted conventional commit message.
---

## User Input

```text
$ARGUMENTS
```

## Execution Steps

### Step 1: Analyze Current State

Run these commands to understand what needs to be committed:

1. `git status` - See all changed/untracked files
2. `git diff --staged` - See already staged changes
3. `git diff` - See unstaged changes
4. `git log --oneline -5` - See recent commit style for consistency

### Step 2: Determine What to Commit

Based on user input (`$ARGUMENTS`):
- If user specified files → stage only those files
- If user said "all" or similar → stage all changes
- If nothing specified → show the user what's changed and ask what to include

**Never commit:**
- `.env` files or credentials
- Large binary files (unless explicitly requested)
- Files in `.gitignore`

### Step 3: Stage Files

Run `git add <files>` for the appropriate files.

### Step 4: Generate Commit Message

Analyze the staged changes and generate a commit message following **Conventional Commits** format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, missing semicolons, etc (no code change)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Maintenance tasks, dependency updates, tooling
- `ci`: CI/CD changes
- `build`: Build system or external dependency changes

**Scope** (optional): The area of code affected.

**Subject rules:**
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Max 50 characters

**Body** (if needed):
- Explain *what* and *why*, not *how*
- Wrap at 72 characters
- Separate from subject with blank line

**Footer:**
- Reference issues: `Fixes #123` or `Closes #456`
- Breaking changes: `BREAKING CHANGE: description`

### Step 5: Present and Confirm

Show the user:
1. Files to be committed
2. Proposed commit message
3. Ask for confirmation or edits

### Step 6: Create Commit

Once confirmed, run:

```bash
git commit -m "$(cat <<'EOF'
<commit message here>
EOF
)"
```

### Step 7: Post-Commit

Show the result of `git log -1 --stat` to confirm the commit.

## User Shortcuts

The user can provide hints in `$ARGUMENTS`:
- `/commit fix the timezone bug` → type: fix, use description as basis
- `/commit feat: add dark mode` → use the provided type and subject
- `/commit all` → stage everything, analyze for message
- `/commit src/` → stage only files in src/, analyze for message

## Edge Cases

- **No changes**: If nothing to commit, inform user and exit
- **Merge conflicts**: Warn user to resolve conflicts first
- **Detached HEAD**: Warn user about the state
- **Large diff**: Summarize the changes rather than listing every line
