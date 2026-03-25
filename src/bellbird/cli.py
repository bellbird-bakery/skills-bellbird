"""Bellbird CLI - install template skills into projects."""

import argparse
import shutil
import sys
from pathlib import Path

import yaml


def get_templates_dir() -> Path:
    """Return the path to the bundled templates directory."""
    return Path(__file__).resolve().parent / "templates"


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from a SKILL.md file."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[3:end].strip()) or {}
    except yaml.YAMLError:
        return {}


def list_templates() -> list[dict]:
    """List all available template skills with their metadata."""
    templates_dir = get_templates_dir()
    if not templates_dir.exists():
        return []

    templates = []
    for skill_dir in sorted(templates_dir.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        fm = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        templates.append({
            "name": fm.get("name", skill_dir.name),
            "description": fm.get("description", ""),
            "path": skill_dir,
        })
    return templates


def cmd_list(args: argparse.Namespace) -> None:
    """List available template skills."""
    templates = list_templates()
    if not templates:
        print("No templates found.")
        return

    print(f"Available skills ({len(templates)}):\n")
    for t in templates:
        print(f"  {t['name']}")
        if t["description"]:
            print(f"    {t['description']}")
        print()


def cmd_init(args: argparse.Namespace) -> None:
    """Copy selected template skills into the target project."""
    project_root = Path(args.project).resolve()
    if not project_root.is_dir():
        print(f"Error: {project_root} is not a directory.", file=sys.stderr)
        sys.exit(1)

    templates = list_templates()
    if not templates:
        print("No templates found.")
        return

    template_names = {t["name"]: t for t in templates}

    if args.skills:
        selected = []
        for name in args.skills:
            if name not in template_names:
                print(f"Error: unknown skill '{name}'. Use 'bellbird list' to see available skills.", file=sys.stderr)
                sys.exit(1)
            selected.append(template_names[name])
    elif args.all:
        selected = templates
    else:
        print("Available skills:\n")
        for i, t in enumerate(templates, 1):
            desc = f" - {t['description']}" if t["description"] else ""
            print(f"  [{i}] {t['name']}{desc}")

        print(f"\nEnter skill numbers (comma-separated), 'all', or 'q' to quit:")
        choice = input("> ").strip()

        if choice.lower() == "q":
            return
        if choice.lower() == "all":
            selected = templates
        else:
            selected = []
            for part in choice.split(","):
                part = part.strip()
                if not part.isdigit() or int(part) < 1 or int(part) > len(templates):
                    print(f"Error: invalid selection '{part}'.", file=sys.stderr)
                    sys.exit(1)
                selected.append(templates[int(part) - 1])

    if not selected:
        print("No skills selected.")
        return

    skills_dir = project_root / ".claude" / "skills"
    installed = []

    for template in selected:
        dest = skills_dir / template["name"]
        if dest.exists() and not args.force:
            print(f"  Skipped {template['name']} (already exists, use --force to overwrite)")
            continue

        if dest.exists():
            shutil.rmtree(dest)

        shutil.copytree(template["path"], dest)
        installed.append(template["name"])
        print(f"  Installed {template['name']}")

    if installed:
        print(f"\n{len(installed)} skill(s) installed to {skills_dir.relative_to(project_root)}/")
    else:
        print("\nNo skills installed.")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bellbird",
        description="Install template skills into Claude Code projects.",
    )
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List available template skills")

    # init
    init_parser = subparsers.add_parser("init", help="Install skills into a project")
    init_parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="Target project directory (default: current directory)",
    )
    init_parser.add_argument(
        "--skills",
        nargs="+",
        metavar="NAME",
        help="Skill names to install (default: interactive selection)",
    )
    init_parser.add_argument(
        "--all",
        action="store_true",
        help="Install all available skills",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing skills",
    )

    args = parser.parse_args()

    if args.command == "list":
        cmd_list(args)
    elif args.command == "init":
        cmd_init(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
