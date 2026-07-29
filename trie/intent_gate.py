"""The intent gate: refuse commits when changed symbols carry no patch notes.

The patch pipeline is an intent store, not a code generator: agents edit
source natively, stage a note per touched symbol (`trie patch <qname> -n …`),
and `trie patch apply` commits those notes to the session log. This module is
the enforcement half — it computes which symbols the working tree actually
changed relative to HEAD and checks each one has intent recorded, either as a
still-pending patch note or as an applied session-log row from this window.

Scoping is deliberately conservative ("don't pull in everything"):

- Only *direct* changes count: a symbol's `body_normalized_hash` differs
  between HEAD and the working tree. Formatting, comments, and line shifts
  don't change the normalized hash, so they demand no notes. No cascade:
  callers of a changed symbol are not pulled in.
- Synthetic `__module__` symbols are skipped — import shuffles and module
  residue are churn, not intent.
- Only in-scope, indexable source files are considered; docs, configs, and
  generated trees never gate.

The pre-commit hook runs `trie intent` between `verify` and the digest write:
uncovered symbols block the commit with a copy-pasteable worklist.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from trie.config import Config
    from trie.graph.store import Store

# Statuses a touched symbol can have relative to HEAD.
MODIFIED = "modified"
ADDED = "added"
REMOVED = "removed"


@dataclass(frozen=True)
class TouchedSymbol:
    qname: str
    status: str  # modified | added | removed
    file: str  # source-root-relative path (the working-tree side when present)


@dataclass(frozen=True)
class IntentReport:
    """Outcome of one gate evaluation."""

    touched: list[TouchedSymbol] = field(default_factory=list)
    uncovered: list[TouchedSymbol] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.uncovered


def _symbols_by_qname(
    file_path: Path, source_root: Path, *, source_text: str | None = None
) -> dict[str, str]:
    """{qname: body_normalized_hash} for one file side; {} when unparseable."""
    from trie.parse import registry

    try:
        symbols = registry.extract_symbols(
            file_path, source_root=source_root, source_text=source_text
        )
    except Exception:
        return {}
    return {
        s.qualified_name: s.body_normalized_hash
        for s in symbols
        if not s.qualified_name.endswith(":__module__")
    }


def touched_symbols(project_root: Path, config: Config) -> list[TouchedSymbol]:
    """Symbols whose normalized body differs between HEAD and the working tree.

    Empty outside a git repo or when HEAD doesn't exist (fresh repo) — the
    gate never blocks where it can't compute a baseline.
    """
    from trie.git_helpers import _run_git, show_file_at_ref
    from trie.parse import registry
    from trie.scope import discover_files

    src_root = (project_root / config.triefacts.source_root).resolve()

    out = _run_git(["diff", "HEAD", "--name-only"], cwd=project_root)
    if out is None:
        return []
    changed_rel = [
        ln.strip() for ln in out.decode("utf-8", errors="replace").splitlines() if ln.strip()
    ]

    # Untracked files never show in `diff HEAD` — brand-new modules would
    # escape the gate entirely without this.
    untracked = _run_git(["ls-files", "--others", "--exclude-standard"], cwd=project_root)
    if untracked is not None:
        for ln in untracked.decode("utf-8", errors="replace").splitlines():
            ln = ln.strip()
            if ln and ln not in changed_rel:
                changed_rel.append(ln)

    if not changed_rel:
        return []

    # Scope filter: only files trie indexes gate intent.
    in_scope = {p.resolve() for p in discover_files(project_root, config.scope)}

    touched: list[TouchedSymbol] = []
    for rel in changed_rel:
        abs_path = (project_root / rel).resolve()
        if not registry.is_indexable(abs_path):
            continue
        exists_now = abs_path.is_file()
        if exists_now and abs_path not in in_scope:
            continue

        head_text = show_file_at_ref(project_root, "HEAD", rel)
        before = (
            _symbols_by_qname(abs_path, src_root, source_text=head_text)
            if head_text is not None
            else {}
        )
        after = _symbols_by_qname(abs_path, src_root) if exists_now else {}

        try:
            file_key = str(abs_path.relative_to(src_root))
        except ValueError:
            file_key = rel
        for qname in sorted(set(before) | set(after)):
            if qname in before and qname in after:
                if before[qname] != after[qname]:
                    touched.append(TouchedSymbol(qname, MODIFIED, file_key))
            elif qname in after:
                touched.append(TouchedSymbol(qname, ADDED, file_key))
            else:
                touched.append(TouchedSymbol(qname, REMOVED, file_key))
    return touched


def _covered_qnames(project_root: Path, config: Config, store: Store) -> set[str]:
    """Qnames with intent on record for the upcoming commit.

    Coverage comes from either side of the apply boundary:
    - staged or sealed patch notes (modify/delete/rename + creates) in the
      qname-keyed patches tables, or
    - rows already consumed into this parent's digest entry.

    No timestamps anywhere: intent is staged, pending, recorded in this
    parent's digest entry (the digest write consumes pending BEFORE the commit
    lands, so a second gate run must see the digest as coverage), or already
    part of HEAD and not gating at all.
    """
    from trie.git_helpers import current_head
    from trie.session_diff import iter_digest_entries, rows_from_digest_entry

    # Staged AND sealed rows both cover: the applied flag is a lifecycle
    # marker, not a coverage boundary.
    covered: set[str] = set(store.get_patched_qnames())
    for _file, rows in store.get_create_patches_grouped().items():
        for row in rows:
            q = row.get("target_qname")
            if q:
                covered.add(q)

    # The uncommitted digest entry for the current parent: pending rows that
    # were already consumed into it still cover their symbols.
    head = current_head(project_root)
    if head:
        diffs_dir = getattr(getattr(config, "diff", None), "diffs_dir", "triefacts/triediffs")
        for entry in iter_digest_entries(project_root, diffs_dir=diffs_dir):
            if head.startswith(entry.get("parent", "\x00")):
                for row in rows_from_digest_entry(entry):
                    if row.get("qname"):
                        covered.add(row["qname"])
                break
    return covered


def _parent_qname(qname: str) -> str | None:
    """Owning-class qname for a method-shaped qname, else None.

    `pkg/mod:Class.method` → `pkg/mod:Class`. Only one level: nested attribute
    chains collapse to their top-level owner within the module.
    """
    mod, sep, local = qname.partition(":")
    if not sep or "." not in local:
        return None
    return f"{mod}:{local.split('.', 1)[0]}"


def evaluate(project_root: Path, config: Config, store: Store) -> IntentReport:
    """Run the gate: touched symbols minus covered ones.

    A note on a class covers its methods: when `mod:Class` has intent on
    record, `mod:Class.method` counts as covered too. Notes describing a new
    or reworked class naturally describe its methods; demanding a separate
    note per method produced commit-time failures for intent that was already
    written down (and each method remains individually notable when finer
    granularity is wanted).
    """
    touched = touched_symbols(project_root, config)
    if not touched:
        return IntentReport()
    covered = _covered_qnames(project_root, config, store)
    uncovered = [
        t for t in touched if t.qname not in covered and _parent_qname(t.qname) not in covered
    ]
    return IntentReport(touched=touched, uncovered=uncovered)
