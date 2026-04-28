from __future__ import annotations

from pathlib import Path

from trie.config import Scope


def discover_files(project_root: Path, scope: Scope) -> list[Path]:
    """Return absolute paths of files under `project_root` matching `scope.include` patterns
    and not matching any `scope.exclude` pattern.

    Patterns use pathlib glob semantics: `**` matches any number of directory segments
    (zero or more). Patterns are evaluated relative to `project_root`. Directories matched
    by an exclude pattern recursively exclude all files beneath them.
    """
    project_root = project_root.resolve()

    included: set[Path] = set()
    for pattern in scope.include:
        for path in project_root.glob(pattern):
            if path.is_file():
                included.add(path.resolve())

    excluded: set[Path] = set()
    for pattern in scope.exclude:
        for path in project_root.glob(pattern):
            resolved = path.resolve()
            if resolved.is_file():
                excluded.add(resolved)
            elif resolved.is_dir():
                for sub in resolved.rglob("*"):
                    if sub.is_file():
                        excluded.add(sub.resolve())

    return sorted(included - excluded)
