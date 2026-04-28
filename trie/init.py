from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from trie.config import DEFAULT_CONFIG_TOML

GITIGNORE_LINE = ".trie/"


@dataclass
class InitResult:
    project_root: Path
    config_written: bool
    gitignore_updated: bool
    detected_markers: list[str]


class InitError(Exception):
    pass


def _detect_python_project(root: Path) -> list[str]:
    """Return non-empty list of detected Python project markers, or [] if none."""
    markers = []
    for marker in ("pyproject.toml", "setup.py", "setup.cfg", "requirements.txt"):
        if (root / marker).exists():
            markers.append(marker)
    if markers:
        return markers
    # Fallback: any .py file at the top level or one directory deep.
    for path in root.glob("*.py"):
        if path.is_file():
            return ["*.py files"]
    for path in root.glob("*/*.py"):
        if path.is_file():
            return ["*.py files"]
    return []


def _ensure_gitignore_entry(gitignore: Path, line: str) -> bool:
    """Append `line` to `gitignore` if not already present. Returns True if file changed."""
    if gitignore.exists():
        existing = gitignore.read_text()
        for existing_line in existing.splitlines():
            stripped = existing_line.strip()
            if stripped == line or stripped == line.rstrip("/"):
                return False
        # Append, preserving trailing newline behavior.
        suffix = "" if existing.endswith("\n") or existing == "" else "\n"
        gitignore.write_text(f"{existing}{suffix}{line}\n")
        return True
    gitignore.write_text(f"{line}\n")
    return True


def init_project(root: Path, *, force: bool = False) -> InitResult:
    """Initialise trie in `root`. Writes trie.toml and updates .gitignore.

    Raises InitError if `root` is not a Python project (override with `force=True`)
    or if trie.toml already exists (override with `force=True`).
    """
    root = root.resolve()
    if not root.is_dir():
        raise InitError(f"{root} is not a directory")

    markers = _detect_python_project(root)
    if not markers and not force:
        raise InitError(
            f"{root} does not look like a Python project (no pyproject.toml / setup.py / *.py). "
            "Re-run with --force to initialise anyway."
        )

    config_path = root / "trie.toml"
    if config_path.exists() and not force:
        raise InitError(f"{config_path} already exists. Re-run with --force to overwrite.")

    config_path.write_text(DEFAULT_CONFIG_TOML)

    gitignore = root / ".gitignore"
    gitignore_updated = _ensure_gitignore_entry(gitignore, GITIGNORE_LINE)

    return InitResult(
        project_root=root,
        config_written=True,
        gitignore_updated=gitignore_updated,
        detected_markers=markers or ["(forced — no markers detected)"],
    )
