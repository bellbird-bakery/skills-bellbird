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

structure:
  docs/architecture/:
    - overview.md        # app structure, data models, UI patterns
    - data-models.md     # Django models by domain
    - service-layer.md   # import rules, tier classification
    - async-overview.md  # when to use async tasks
    - async-implementation-guide.md  # how to implement async

  docs/features/:
    - recalls.md         # MPI NZ compliance, mock recalls
    - ingredient-stock.md # recipe calculation, stock tracking
    - reporting.md       # CSV and PDF reports
    - dashboards.md      # KPI cards, chart cards
    - kanban-workflow.md # drag-drop pipelines
    - automatic-follow-up-system.md  # customer check-ins

  docs/integrations/:
    - xero.md           # invoicing, credit notes
    - woocommerce.md    # order imports, webhooks

  docs/operations/:
    - commands.md       # just, docker, django commands
    - configuration.md  # env vars, settings
    - deployment.md     # CI/CD, nginx
    - celery.md         # scheduled tasks
    - troubleshooting.md # common issues
    - learnings.yaml    # cross-cutting knowledge from /reflect (YAML-only)

  docs/standards/:
    - timezone.md       # datetime handling rules
    - templates.md      # HTML/CSS conventions
    - nginx-websocket.md # WebSocket proxy config

  docs/framework/:
    - speckit.md        # specification commands

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
  command: just docs
  build: just docs-build
  runs_on: host via uvx (not Docker)

adding_documentation:
  steps:
    1: Create docs/<category>/<name>.md
    2: Add frontmatter with all schema fields
    3: Update mkdocs.yml nav section
    4: Preview with just docs

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
    - Preview with just docs

capturing_learnings:
  command: /reflect
  purpose: After completing a task, capture undocumented knowledge
  workflow:
    - Reviews conversation context
    - Identifies knowledge gaps encountered
    - Adds to relevant doc OR docs/operations/learnings.yaml
    - Updates frontmatter if new topics added
  learnings_yaml_format:
    note: YAML-only file optimized for Claude, not human reading
    schema: See .claude/commands/reflect.md for entry format
```
