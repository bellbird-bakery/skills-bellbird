"""Bellbird CLI - install template skills and commands into projects."""

import argparse
import shutil
import sys
from pathlib import Path

import yaml


def get_templates_dir() -> Path:
    """Return the path to the bundled templates directory."""
    return Path(__file__).resolve().parent / "templates"


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[3:end].strip()) or {}
    except yaml.YAMLError:
        return {}


def detect_template_type(template_dir: Path) -> str | None:
    """Detect whether a template is a skill or command."""
    if (template_dir / "SKILL.md").exists():
        return "skill"
    if (template_dir / "COMMAND.md").exists():
        return "command"
    return None


def list_templates() -> list[dict]:
    """List all available templates with their metadata."""
    templates_dir = get_templates_dir()
    if not templates_dir.exists():
        return []

    templates = []
    for template_dir in sorted(templates_dir.iterdir()):
        ttype = detect_template_type(template_dir)
        if ttype is None:
            continue
        md_file = template_dir / ("SKILL.md" if ttype == "skill" else "COMMAND.md")
        fm = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        templates.append({
            "name": fm.get("name", template_dir.name),
            "description": fm.get("description", ""),
            "type": ttype,
            "path": template_dir,
        })
    return templates


def cmd_list(args: argparse.Namespace) -> None:
    """List available templates."""
    templates = list_templates()
    if not templates:
        print("No templates found.")
        return

    skills = [t for t in templates if t["type"] == "skill"]
    commands = [t for t in templates if t["type"] == "command"]

    if skills:
        print(f"Skills ({len(skills)}):\n")
        for t in skills:
            print(f"  {t['name']}")
            if t["description"]:
                print(f"    {t['description']}")
            print()

    if commands:
        print(f"Commands ({len(commands)}):\n")
        for t in commands:
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
                print(f"Error: unknown template '{name}'. Use 'bellbird list' to see available templates.", file=sys.stderr)
                sys.exit(1)
            selected.append(template_names[name])
    elif args.all:
        selected = templates
    else:
        print("Available templates:\n")
        for i, t in enumerate(templates, 1):
            desc = f" - {t['description']}" if t["description"] else ""
            label = f"[{t['type']}]"
            print(f"  [{i}] {t['name']} {label}{desc}")

        print(f"\nEnter numbers (comma-separated), 'all', or 'q' to quit:")
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
        print("No templates selected.")
        return

    installed = []

    for template in selected:
        if template["type"] == "skill":
            dest = project_root / ".claude" / "skills" / template["name"]
            if dest.exists() and not args.force:
                print(f"  Skipped {template['name']} (already exists, use --force to overwrite)")
                continue
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(template["path"], dest)
        else:
            commands_dir = project_root / ".claude" / "commands"
            commands_dir.mkdir(parents=True, exist_ok=True)
            src = template["path"] / "COMMAND.md"
            dest = commands_dir / f"{template['name']}.md"
            if dest.exists() and not args.force:
                print(f"  Skipped {template['name']} (already exists, use --force to overwrite)")
                continue
            shutil.copy2(src, dest)

        installed.append(template)
        print(f"  Installed {template['name']} ({template['type']})")

    if installed:
        skills = [t for t in installed if t["type"] == "skill"]
        commands = [t for t in installed if t["type"] == "command"]
        parts = []
        if skills:
            parts.append(f"{len(skills)} skill(s) to .claude/skills/")
        if commands:
            parts.append(f"{len(commands)} command(s) to .claude/commands/")
        print(f"\nInstalled {', '.join(parts)}")
    else:
        print("\nNothing installed.")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bellbird",
        description="Install template skills and commands into Claude Code projects.",
    )
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List available templates")

    # init
    init_parser = subparsers.add_parser("init", help="Install templates into a project")
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
        help="Template names to install (default: interactive selection)",
    )
    init_parser.add_argument(
        "--all",
        action="store_true",
        help="Install all available templates",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing templates",
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
