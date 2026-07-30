"""Static validation for the Applied AI portfolio repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MAX_GITHUB_FILE_SIZE = 100 * 1024 * 1024
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

PROJECTS = [
    ROOT
    / "Computer-Vision-ITAI1378/Projects/01-Image-Processing-Fundamentals",
    ROOT / "Computer-Vision-ITAI1378/Projects/02-CIFAR10-SVM-Classifier",
    ROOT
    / "Computer-Vision-ITAI1378/Projects/03-Chihuahua-Muffin-Neural-Network",
]


def validate_notebooks(errors: list[str]) -> None:
    for project in PROJECTS:
        notebooks = list(project.glob("*.ipynb"))
        if len(notebooks) != 1:
            errors.append(f"{project.relative_to(ROOT)}: expected one notebook")
            continue

        path = notebooks[0]
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue

        if notebook.get("nbformat") != 4:
            errors.append(f"{path.relative_to(ROOT)}: expected nbformat 4")

        code_cells = [
            cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "code"
        ]
        executed = [
            cell for cell in code_cells if cell.get("execution_count") is not None
        ]
        if not code_cells or len(executed) != len(code_cells):
            errors.append(
                f"{path.relative_to(ROOT)}: not every code cell has an execution count"
            )

        error_outputs = [
            output
            for cell in code_cells
            for output in cell.get("outputs", [])
            if output.get("output_type") == "error"
        ]
        if error_outputs:
            errors.append(
                f"{path.relative_to(ROOT)}: contains {len(error_outputs)} error output(s)"
            )

        image_outputs = sum(
            1
            for cell in code_cells
            for output in cell.get("outputs", [])
            if "image/png" in output.get("data", {})
        )
        if image_outputs == 0:
            errors.append(f"{path.relative_to(ROOT)}: contains no saved PNG outputs")

        print(
            f"Notebook OK: {path.relative_to(ROOT)} "
            f"({len(code_cells)} code cells, {image_outputs} PNG outputs)"
        )


def validate_project_files(errors: list[str]) -> None:
    for project in PROJECTS:
        for required in ("README.md", "requirements.txt", "results", "report"):
            if not (project / required).exists():
                errors.append(
                    f"{project.relative_to(ROOT)}: missing required {required}"
                )


def validate_markdown_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts or "tmp" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
            ):
                continue
            target_path = markdown.parent / unquote(target.split("#", 1)[0])
            if not target_path.exists():
                errors.append(
                    f"{markdown.relative_to(ROOT)}: broken local link '{target}'"
                )


def validate_file_sizes(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "tmp" in path.parts:
            continue
        if path.stat().st_size >= MAX_GITHUB_FILE_SIZE:
            errors.append(
                f"{path.relative_to(ROOT)}: exceeds GitHub's 100 MB file limit"
            )


def contact_warnings() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "ADD PROFESSIONAL EMAIL" in readme:
        print("WARNING: Add a professional email before submission.")
    if "ADD LINKEDIN PROFILE URL" in readme:
        print("WARNING: Add a LinkedIn URL before submission.")


def main() -> int:
    errors: list[str] = []
    validate_project_files(errors)
    validate_notebooks(errors)
    validate_markdown_links(errors)
    validate_file_sizes(errors)
    contact_warnings()

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nPortfolio validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
