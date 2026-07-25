from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from trie.config import DEFAULT_CONFIG_TOML

GITIGNORE_LINE = ".trie/"

PreCommitStrategy = Literal["git_hook", "framework", "none", "skipped"]

PRE_COMMIT_HOOK_MARKER = "# trie-verify (added by `trie init`)"
PRE_COMMIT_HOOK_END_MARKER = "# end trie-verify"
# The hook runs two checks in order:
#   1. `trie lock-check` — refuses the commit if a `trie refresh` or `trie sync`
#      is in flight. Committing during a write would capture a half-updated
#      triefact tree; better to fail loudly and let the user retry once the
#      writer finishes.
#   2. `trie verify` — the standard drift gate. Refuses commits when triefacts
#      have drifted from source.
# Both are wrapped in `command -v trie` so the hook degrades cleanly if trie
# isn't on PATH (uninstalled, fresh clone before `uv tool install`, etc.).
# Shell script block embedded in the project's .git/hooks/pre-commit file.
# Wrapped in marker comments for idempotent installation and performs three
# advisory/blocking steps when trie is available on PATH:
#
#   1. lock-check  — blocks the commit if an ongoing write holds the lock,
#                    preventing partial-state commits.
#   2. verify      — blocks the commit on drift detection, ensuring the
#                    triefact file is consistent with the working tree.
#   3. diff --write — writes an intent-level digest entry (patch notes +
#                    before/after symbol deltas, with an optional LLM
#                    narrative when [diff] config enables it) as a new
#                    immutable file under triediffs/ and repoints the
#                    TRIE_DIFF.md symlink at it, then stages both so every
#                    commit — and therefore every PR — carries its digest as
#                    a brand-new file (pure additions, never a diff-of-a-diff).
#                    The names are hardcoded to the default diff.write_path /
#                    diff.diffs_dir; users who change those config keys must
#                    edit their hook accordingly. This step is purely
#                    advisory: failure never blocks the commit.
PRE_COMMIT_HOOK_BLOCK = (
    f"{PRE_COMMIT_HOOK_MARKER}\n"
    "if command -v trie >/dev/null 2>&1; then\n"
    "    trie -q lock-check || exit $?\n"
    "    trie -q verify || exit $?\n"
    "    if trie -q diff --write >/dev/null 2>&1; then\n"
    "        git add TRIE_DIFF.md triediffs >/dev/null 2>&1 || true\n"
    "    fi\n"
    "fi\n"
    f"{PRE_COMMIT_HOOK_END_MARKER}\n"
)


@dataclass
class InitResult:
    project_root: Path
    config_written: bool
    gitignore_updated: bool
    detected_markers: list[str]
    scan_files_total: int = 0
    scan_symbols_total: int = 0
    scan_ran: bool = False
    pre_commit_installed: bool = False
    pre_commit_strategy: PreCommitStrategy = "skipped"
    pre_commit_path: Path | None = None


class InitError(Exception):
    pass


def _detect_supported_project(root: Path) -> list[str]:
    """Return non-empty list of detected project markers for any supported
    language, or [] if none.

    Checks well-known config markers (Python packaging, JS/TS `package.json` /
    `tsconfig.json`) first, then falls back to scanning for any file whose
    extension a registered language backend claims (top level or one dir deep).
    """
    from trie.parse import registry

    markers = []
    for marker in (
        "pyproject.toml",
        "setup.py",
        "setup.cfg",
        "requirements.txt",
        "package.json",
        "tsconfig.json",
    ):
        if (root / marker).exists():
            markers.append(marker)
    if markers:
        return markers
    # Fallback: any indexable source file at the top level or one directory deep.
    for pattern in ("*", "*/*"):
        for path in root.glob(pattern):
            if path.is_file() and registry.is_indexable(path):
                return [f"*{registry.get_backend_for_file(path).extensions[0]} files"]
    return []


# Backward-compatible alias (tests / external callers may import this name).
_detect_python_project = _detect_supported_project


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


def install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]:
    """Install a pre-commit hook that runs lock-check, verify, and digest refresh.

    Strategies:
      - "framework": project already uses the pre-commit framework
        (`.pre-commit-config.yaml` present). We don't touch user-owned YAML; the
        caller should print a manual snippet. Returns (False, "framework", None).
      - "git_hook": write/append a marker-fenced block to `.git/hooks/pre-commit`,
        idempotent. The block runs `trie lock-check`, `trie verify --quiet`, and
        `trie diff --write` (digest refresh) as advisory steps on each commit.
        Returns (True, "git_hook", hook_path) on first install,
        (False, "git_hook", hook_path) when the marker is already present.
      - "none": no `.git` directory; nothing to do. Returns (False, "none", None).
    """
    if (project_root / ".pre-commit-config.yaml").exists():
        return False, "framework", None
    git_dir = project_root / ".git"
    if not git_dir.is_dir():
        return False, "none", None
    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    hook_path = hooks_dir / "pre-commit"
    if hook_path.exists():
        existing = hook_path.read_text()
        if PRE_COMMIT_HOOK_MARKER in existing:
            return False, "git_hook", hook_path
        new_text = existing.rstrip() + "\n\n" + PRE_COMMIT_HOOK_BLOCK
        hook_path.write_text(new_text)
    else:
        hook_path.write_text("#!/bin/sh\n" + PRE_COMMIT_HOOK_BLOCK)
    hook_path.chmod(0o755)
    return True, "git_hook", hook_path


def init_project(
    root: Path,
    *,
    force: bool = False,
    install_hooks: bool = False,
    run_scan: bool = True,
) -> InitResult:
    """Initialise trie in `root`. Writes trie.toml, updates .gitignore, and (by
    default) runs the initial scan so the symbol graph is ready for `trie sync`.

    Raises InitError if `root` is not a Python project (override with `force=True`)
    or if trie.toml already exists (override with `force=True`).
    """
    root = root.resolve()
    if not root.is_dir():
        raise InitError(f"{root} is not a directory")

    markers = _detect_supported_project(root)
    if not markers and not force:
        raise InitError(
            f"{root} does not look like a supported project (no pyproject.toml / "
            "setup.py / package.json / tsconfig.json / source files). "
            "Re-run with --force to initialise anyway."
        )

    config_path = root / "trie.toml"
    if config_path.exists() and not force:
        raise InitError(f"{config_path} already exists. Re-run with --force to overwrite.")

    config_path.write_text(DEFAULT_CONFIG_TOML)

    gitignore = root / ".gitignore"
    gitignore_updated = _ensure_gitignore_entry(gitignore, GITIGNORE_LINE)

    result = InitResult(
        project_root=root,
        config_written=True,
        gitignore_updated=gitignore_updated,
        detected_markers=markers or ["(forced — no markers detected)"],
    )

    if run_scan:
        # Imported here to avoid pulling tree-sitter into the import graph for callers
        # that only need the dataclasses (e.g. tests that don't need a real scan).
        from trie.config import Config
        from trie.graph.store import Store
        from trie.scan import scan_project

        config, _ = Config.find_and_load(root)
        with Store(root / ".trie" / "graph.db") as store:
            scan_result = scan_project(project_root=root, config=config, store=store)
        result.scan_ran = True
        result.scan_files_total = scan_result.files_total
        result.scan_symbols_total = scan_result.symbols_total

    if install_hooks:
        installed, strategy, hook_path = install_pre_commit_hook(root)
        result.pre_commit_installed = installed
        result.pre_commit_strategy = strategy
        result.pre_commit_path = hook_path

    return result
