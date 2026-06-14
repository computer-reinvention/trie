from __future__ import annotations

import os
import re
from functools import lru_cache
from glob import translate as _glob_translate
from pathlib import Path

from trie.config import Scope


@lru_cache(maxsize=512)
def _compiled(pattern: str) -> re.Pattern[str]:
    """Compile a pathlib-style glob pattern to a regex with correct `**` semantics.

    `glob.translate(..., recursive=True)` reproduces the `Path.glob` behaviour the
    previous implementation relied on: `**` matches any number of directory
    segments (including zero), and `*` does not cross `/`.
    """
    return re.compile(_glob_translate(pattern, recursive=True, include_hidden=True))


def _matches(rel_posix: str, pattern: str) -> bool:
    """True if the project-relative POSIX path matches a pathlib-style glob pattern."""
    return _compiled(pattern).match(rel_posix) is not None


def _dir_is_pruned(rel_dir_posix: str, exclude: list[str]) -> bool:
    """True if every file beneath `rel_dir_posix` is guaranteed excluded.

    We prune a directory mid-walk when the directory itself matches an exclude
    pattern's "container" form. For an exclude like `**/tests/**`, the matching
    container is `**/tests` — so the `tests` directory (and everything under it)
    is pruned before we ever descend into it. This is what stops the walk from
    entering `node_modules`, `.venv`, etc.
    """
    for pattern in exclude:
        # Patterns that exclude a directory's whole subtree end in `/**`.
        # Strip the trailing `/**` to get the directory-container pattern.
        if pattern.endswith("/**"):
            container = pattern[: -len("/**")]
            if container and _matches(rel_dir_posix, container):
                return True
        # A bare directory pattern (no glob suffix) also prunes its subtree.
        elif _matches(rel_dir_posix, pattern):
            return True
    return False


def discover_files(project_root: Path, scope: Scope) -> list[Path]:
    """Return absolute paths of files under `project_root` matching `scope.include`
    patterns and not matching any `scope.exclude` pattern.

    Patterns use pathlib glob semantics: `**` matches any number of directory segments
    (zero or more). Patterns are evaluated relative to `project_root`. Directories matched
    by an exclude pattern recursively exclude all files beneath them.

    The walk prunes excluded directories *before* descending into them, so large
    vendored trees (`.venv`, `node_modules`, `dist`, …) covered by an exclude
    pattern never get traversed. This keeps discovery fast on repos that contain
    huge out-of-scope subtrees.
    """
    project_root = project_root.resolve()

    result: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(project_root, topdown=True):
        abs_dir = Path(dirpath)
        rel_dir = abs_dir.relative_to(project_root).as_posix()

        # Prune subdirectories in place so os.walk never descends into them.
        kept: list[str] = []
        for d in dirnames:
            child_rel = d if rel_dir == "." else f"{rel_dir}/{d}"
            if _dir_is_pruned(child_rel, scope.exclude):
                continue
            kept.append(d)
        dirnames[:] = kept

        for fname in filenames:
            rel = fname if rel_dir == "." else f"{rel_dir}/{fname}"
            if not any(_matches(rel, pat) for pat in scope.include):
                continue
            if any(_matches(rel, pat) for pat in scope.exclude):
                continue
            result.append((project_root / rel).resolve())

    return sorted(result)
