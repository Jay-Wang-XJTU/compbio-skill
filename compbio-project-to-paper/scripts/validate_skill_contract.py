#!/usr/bin/env python3
"""Validate the local contract and routing paths for this skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("Missing dependency: PyYAML. Install with `python -m pip install pyyaml`.") from exc


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "manifest.yaml",
    "agents/openai.yaml",
    "references/project-triage.md",
    "references/benchmark-and-evidence.md",
    "references/figure-story-and-color.md",
    "references/manuscript-architecture.md",
    "references/paper-patterns.md",
    "references/evaluation-cases.md",
    "scripts/extract_paper_structure.py",
)


def iter_paths(node: Any, parent: str = ""):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"path"} and isinstance(value, str):
                yield value
            elif key == "values" and isinstance(value, dict):
                for route in value.values():
                    if isinstance(route, str):
                        yield route
            else:
                yield from iter_paths(value, str(key))
    elif isinstance(node, list):
        for value in node:
            yield from iter_paths(value, parent)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "TODO" in skill_text:
        errors.append("SKILL.md contains TODO")
    match = re.match(r"^---\s*\n(.*?)\n---", skill_text, flags=re.DOTALL)
    if not match:
        errors.append("SKILL.md is missing leading YAML frontmatter")
        skill_meta = {}
    else:
        skill_meta = yaml.safe_load(match.group(1)) or {}

    manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8")) or {}
    if skill_meta.get("name") != manifest.get("name"):
        errors.append("SKILL.md and manifest.yaml names differ")

    openai = yaml.safe_load((ROOT / "agents/openai.yaml").read_text(encoding="utf-8")) or {}
    prompt = ((openai.get("interface") or {}).get("default_prompt") or "")
    if f"${skill_meta.get('name', '')}" not in prompt:
        errors.append("agents/openai.yaml default_prompt must mention the skill")

    for relative in iter_paths(manifest):
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            errors.append(f"manifest path must stay inside the skill: {relative}")
        elif not (ROOT / candidate).exists():
            errors.append(f"manifest path does not exist: {relative}")

    if errors:
        print("Skill contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
