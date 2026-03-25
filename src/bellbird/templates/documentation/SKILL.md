---
name: documentation
description: Navigate and maintain project documentation. Docs have YAML frontmatter with structured metadata.
---

```yaml
# Documentation uses YAML frontmatter for Claude-optimized navigation.
# Each doc has: title, purpose, topics, answers, related, key_files

frontmatter_schema:
  title: Document title
  purpose: Brief description (for quick scanning)
  topics: List of keywords/concepts covered
  answers: Questions this doc answers (match against user queries)
  related: Paths to related docs
  key_files: Source files referenced

# Frontmatter is hidden from humans in MkDocs, visible to Claude

recommended_structure:
  docs/architecture/:
    purpose: System design and code organization
    examples:
      - overview.md        # app structure, patterns
      - data-models.md     # models by domain
      - service-layer.md   # import rules, tiers

  docs/features/:
    purpose: Feature-specific documentation
    examples:
      - feature-name.md    # how a feature works

  docs/integrations/:
    purpose: External API and service integrations
    examples:
      - api-name.md        # setup, auth, gotchas

  docs/operations/:
    purpose: Running and maintaining the project
    examples:
      - commands.md        # common commands
      - configuration.md   # env vars, settings
      - deployment.md      # CI/CD, hosting
      - troubleshooting.md # common issues
      - learnings.yaml     # cross-cutting knowledge (YAML-only)

  docs/standards/:
    purpose: Code conventions and patterns
    examples:
      - coding-style.md    # formatting, naming
      - testing.md         # test patterns

navigation:
  # To find the right doc, read frontmatter from likely candidates
  # Match user question against 'answers' field
  # Match keywords against 'topics' field

  by_question_type:
    system_design: docs/architecture/
    feature_behavior: docs/features/
    external_apis: docs/integrations/
    how_to_run: docs/operations/
    code_conventions: docs/standards/

serving:
  mkdocs:
    command: mkdocs serve
    build: mkdocs build
  justfile:
    command: just docs
    build: just docs-build

adding_documentation:
  steps:
    1: Create docs/<category>/<name>.md
    2: Add frontmatter with all schema fields
    3: Update mkdocs.yml nav section (if using MkDocs)
    4: Preview locally

  naming: lowercase-with-hyphens

  frontmatter_template: |
    ---
    title: Feature Name
    purpose: Brief description
    topics:
      - keyword1
      - keyword2
    answers:
      - What question does this answer?
    related:
      - ../category/other-doc.md
    key_files:
      - src/app/file.py
    ---

updating_documentation:
  steps:
    - Read existing frontmatter first
    - Update content AND frontmatter if topics change
    - Ensure related links are bidirectional
    - Preview locally

capturing_learnings:
  command: /reflect
  purpose: After completing a task, capture undocumented knowledge
  workflow:
    - Reviews conversation context
    - Identifies knowledge gaps encountered
    - Adds to relevant doc OR docs/learnings.yaml
    - Updates frontmatter if new topics added
  learnings_yaml_format:
    note: YAML-only file optimized for Claude, not human reading
    schema: See /reflect command for entry format
```
