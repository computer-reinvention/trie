"""Freshness gate: keep the graph + triefact tree current with respect to disk and HEAD.

The eval workflow runs agents in long sessions that span many turns. Between turns
the agent edits source files; between sessions a `git pull` can bring in
collaborators' work. Without a gate, the MCP server's view of the project drifts
from reality and the agent loses trust in trie's answers.

This module provides two trigger points:

  - `ensure_fresh_before_turn(...)`: cheap probe at turn start. Catches the
    "someone pulled" case (HEAD moved) and the "someone edited between turns"
    case (mtime moved). No-op when nothing changed since the last refresh.

  - `ensure_fresh_after_turn(...)`: filesystem sweep at turn end. Catches the
    "agent edited inside the just-finished turn" case. Reuses the same scan +
    cascade + sync machinery as `before_turn`.

Both triggers ultimately call `run_incremental`, which already handles
scan-then-cascade-then-sync correctly. The novelty here is in *deciding when to
call it*, recorded in a stamp file at `.trie/graph.head`. The stamp carries:

  - the git HEAD SHA at the last refresh, and
  - a map of `in-scope-relative-path -> last-seen-mtime` so we can detect file
    changes without re-reading bytes.

The stamp lives under `.trie/`, gitignored: it's a per-checkout artefact, not
a versioned state file. Different developers can hold different stamps without
collision; the trie command takes responsibility for keeping each one accurate.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from trie import telemetry
from trie.activity import write_pending
from trie.config import Config
from trie.git_helpers import current_head, is_git_repo
from trie.graph.store import Store
from trie.models import TrieClient
from trie.scan import scan_project
from trie.scope import discover_files
from trie.sync.incremental import (
    IncrementalResult,
    compute_incremental_worklist,
    run_incremental,
)
from trie.sync.progress import ProgressCallback
from trie.sync.single_file import backfill_section_records

STAMP_FILENAME = "graph.head"


class NotAGitRepoError(RuntimeError):
    """Raised when the freshness gate is invoked outside a git repository.

    trie's freshness model assumes the project is under git: HEAD comparison is
    the primary trigger for cross-session refresh. We refuse to run otherwise
    rather than degrade silently into "always-fresh after first scan" — the
    latter would let drift accumulate undetected during eval runs, which is
    exactly what this module exists to prevent.
    """


@dataclass(frozen=True)
class Stamp:
    """One refresh's worth of recorded state.

    `head` is the commit SHA the graph was built against. `mtimes` is the
    seen modification timestamp for every in-scope source file at that moment.
    Both halves are needed: HEAD alone misses intra-session edits, mtimes alone
    can't tell a `git pull` from a local edit.
    """

    head: str
    mtimes: dict[str, float]

    def to_json(self) -> dict[str, Any]:
        return {"head": self.head, "mtimes": self.mtimes}

    @classmethod
    def from_json(cls, raw: dict[str, Any]) -> Stamp | None:
        """Construct from a parsed JSON dict. Returns None when the dict is
        malformed (older format, hand-edited, partial write). The caller treats
        an unreadable stamp the same as a missing one — by re-running a full
        refresh."""
        head = raw.get("head")
        mtimes = raw.get("mtimes")
        if not isinstance(head, str) or not isinstance(mtimes, dict):
            return None
        coerced: dict[str, float] = {}
        for k, v in mtimes.items():
            if isinstance(k, str) and isinstance(v, int | float):
                coerced[k] = float(v)
        return cls(head=head, mtimes=coerced)


def stamp_path(project_root: Path) -> Path:
    """Conventional location for the stamp under `.trie/`."""
    return project_root / ".trie" / STAMP_FILENAME


def read_stamp(project_root: Path) -> Stamp | None:
    """Return the recorded stamp, or None if missing/unreadable.

    Failure modes (file missing, malformed JSON, wrong schema, encoding error)
    all collapse to None — the caller treats every failure as "force a full
    refresh", which is the correct conservative behaviour."""
    path = stamp_path(project_root)
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(raw, dict):
        return None
    return Stamp.from_json(raw)


def write_stamp(project_root: Path, stamp: Stamp) -> None:
    """Write a stamp atomically by writing-then-renaming.

    A torn write would corrupt the stamp, leaving us unable to detect freshness
    until the next refresh. The rename keeps the on-disk state always-valid:
    either the old stamp or the new one is visible, never a partial write."""
    path = stamp_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(stamp.to_json(), indent=2, sort_keys=True))
    os.replace(tmp, path)


def scan_mtimes(project_root: Path, config: Config) -> dict[str, float]:
    """Return `{source-rel-path: mtime}` for every in-scope file.

    Uses `os.stat` rather than reading file bytes — significantly cheaper for
    the common "nothing changed" path, which is what we want when this runs on
    every turn boundary.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    out: dict[str, float] = {}
    for abs_path in discover_files(project_root, config.scope):
        if not abs_path.is_relative_to(src_root):
            continue
        try:
            stat = abs_path.stat()
        except FileNotFoundError:
            continue
        rel = str(abs_path.relative_to(src_root))
        out[rel] = stat.st_mtime
    return out


def _require_git(project_root: Path) -> str:
    """Return current HEAD or raise `NotAGitRepoError`. Used by ensure_fresh
    variants — they refuse to run outside git rather than silently allow
    drift."""
    if not is_git_repo(project_root):
        raise NotAGitRepoError(
            f"{project_root} is not inside a git repository. The freshness gate "
            "requires git to compare HEAD between turns."
        )
    head = current_head(project_root)
    if head is None:
        raise NotAGitRepoError(
            f"git is available at {project_root} but `git rev-parse HEAD` failed. "
            "An empty repo with no commits won't work here — make at least one "
            "commit before running the freshness gate."
        )
    return head


def _mtimes_differ(a: dict[str, float], b: dict[str, float]) -> bool:
    """True iff `a` and `b` disagree on any key.

    Handles three change shapes: new file (in `b` but not `a`), removed file
    (in `a` but not `b`), modified file (different mtime). All count as drift.

    Float comparison is exact here: filesystems report mtime with fixed
    precision and we only ever compare values written by `os.stat` from the
    same FS to the same FS.
    """
    if a.keys() != b.keys():
        return True
    return any(b.get(k) != va for k, va in a.items())


@dataclass(frozen=True)
class FreshnessResult:
    """Outcome of an ensure_fresh call.

    `refreshed` is True iff the graph was rebuilt. `head` is the SHA of HEAD at
    the time of the check. `incremental` carries the underlying result only when
    an inline LLM sync ran (the opt-in `--sync` path); the default refresh is
    graph-only and leaves it None.

    `stale_files` lists triefacts whose prose now lags their source after a
    `mtimes_moved` refresh — the work a subsequent `trie sync` would do. The
    default refresh marks these stale (writing `.trie/pending.json`) rather than
    regenerating them inline, so the turn-boundary hook stays fast.
    """

    refreshed: bool
    reason: str
    head: str
    incremental: IncrementalResult | None = None
    stale_files: tuple[str, ...] = ()


def ensure_fresh_before_turn(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: TrieClient,
    progress: ProgressCallback | None = None,
    sync_prose: bool = False,
) -> FreshnessResult:
    """Cheap freshness probe to run at the start of an agent turn.

    Four states (see `_ensure_fresh` for the full rationale):
      1. `no_stamp` → graph scan only (no LLM). First run in this checkout.
      2. `head_moved` → graph scan only (no LLM). Someone pulled; trust the
         committed triefact prose.
      3. `mtimes_moved` → graph scan only (no LLM by default); drifted triefacts
         are marked stale in `.trie/pending.json` for a later `trie sync`. Pass
         `sync_prose=True` to regenerate prose inline (the old behaviour).
      4. `unchanged` → no-op fast path.

    Refresh is the *fast* gate: keeping the LLM out of the turn boundary is the
    whole point. Prose regen is decoupled into `trie sync`.
    """
    return _ensure_fresh(
        project_root=project_root,
        config=config,
        store=store,
        client=client,
        progress=progress,
        trigger="before_turn",
        sync_prose=sync_prose,
    )


def ensure_fresh_after_turn(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: TrieClient,
    progress: ProgressCallback | None = None,
    sync_prose: bool = False,
) -> FreshnessResult:
    """Always-on freshness sweep to run at the end of an agent turn.

    Reuses the same machinery as `ensure_fresh_before_turn` — the same
    HEAD/mtime checks drive the same refresh path. The semantic difference is
    one of intent: this hook fires after the agent has finished editing, so
    in steady state it picks up exactly the files the agent just touched. If
    HEAD also moved (unusual but possible — the agent ran `git pull` itself),
    that's caught too.

    Graph-only by default (fast); `sync_prose=True` regenerates inline.
    """
    return _ensure_fresh(
        project_root=project_root,
        config=config,
        store=store,
        client=client,
        progress=progress,
        trigger="after_turn",
        sync_prose=sync_prose,
    )


def _ensure_fresh(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: TrieClient,
    progress: ProgressCallback | None,
    trigger: str,
    sync_prose: bool = False,
) -> FreshnessResult:
    """Shared freshness implementation. `trigger` is a telemetry label only.

    Branches by reason. Every path rebuilds the graph from source via
    `scan_project` (fast, no LLM). Prose regeneration is decoupled: by default
    even `mtimes_moved` only *marks* drifted triefacts stale (in
    `.trie/pending.json`) instead of regenerating them inline, so refresh stays
    fast at the turn boundary. `sync_prose=True` restores inline regen.

    Rationale:
      - `no_stamp`: first run in a fresh checkout. Auto-spending LLM dollars on
        first contact would be hostile; scan rebuilds the graph cheaply so MCP
        queries work immediately. Prose regen is opt-in via `trie sync`.
      - `head_moved`: a `git pull` brought in committed triefacts; re-LLMing
        them would discard a teammate's work. Scan rebuilds the graph against
        the new code; committed prose stays as-is.
      - `mtimes_moved`: local source edits drift prose from source. Graph-only
        by default — the drift is recorded as stale and a later `trie sync`
        regenerates it. With `sync_prose=True`, `run_incremental` fires inline.
    """
    with telemetry.timed("freshness_gate", trigger=trigger) as tele:
        head = _require_git(project_root)
        stamp = read_stamp(project_root)
        current_mtimes = scan_mtimes(project_root, config)

        # An empty store overrides every stamp-based verdict. The stamp records
        # *when* we last refreshed, not *whether the graph still exists*: a
        # wiped/regenerated/corrupted `.trie/graph.db` leaves a valid stamp
        # pointing at no data. Treating that as "unchanged" returns a no-op
        # refresh against an empty graph — every query then comes back empty
        # while looking healthy. Detect it up front and
        # force a graph rebuild (scan only, no LLM — the committed triefacts
        # are trusted as-is, same as the head_moved path).
        store_empty = store.count_symbols() == 0

        reason: str
        if store_empty:
            reason = "empty_store"
        elif stamp is None:
            reason = "no_stamp"
        elif stamp.head != head:
            reason = "head_moved"
        elif _mtimes_differ(stamp.mtimes, current_mtimes):
            reason = "mtimes_moved"
        else:
            reason = "unchanged"

        tele["head"] = head
        tele["reason"] = reason
        if stamp is not None:
            tele["previous_head"] = stamp.head

        if reason == "unchanged":
            if store.count_section_records() < store.count_symbols():
                backfill_section_records(project_root, config, store)
            return FreshnessResult(refreshed=False, reason=reason, head=head, incremental=None)

        if reason == "mtimes_moved":
            if sync_prose:
                # Opt-in inline regen: `run_incremental` handles scan + cascade +
                # LLM sync with diff-aware regen. Slow; only when explicitly asked.
                result = run_incremental(
                    project_root=project_root,
                    config=config,
                    store=store,
                    client=client,
                    progress=progress,
                )
                write_stamp(project_root, Stamp(head=head, mtimes=current_mtimes))
                # Inline sync regenerated everything that drifted, so the working
                # tree is clean: drop the whole pending set.
                write_pending(project_root, stale=[], head=head)
                tele["files_synced"] = result.files_synced
                tele["actual_cost_usd"] = result.actual_cost_usd
                return FreshnessResult(refreshed=True, reason=reason, head=head, incremental=result)

            # Default: graph-only. Rebuild the symbol graph from source (fast,
            # no LLM) so MCP queries reflect current code, then record which
            # triefacts now lag their source in `.trie/pending.json`. A later
            # `trie sync` regenerates the prose. The turn boundary stays fast.
            worklist = compute_incremental_worklist(
                project_root=project_root, config=config, store=store
            )
            if store.count_section_records() < store.count_symbols():
                backfill_section_records(project_root, config, store)
            write_stamp(project_root, Stamp(head=head, mtimes=current_mtimes))
            stale = tuple(worklist.affected_files)
            write_pending(project_root, stale=list(stale), head=head)
            tele["stale_files"] = len(stale)
            return FreshnessResult(
                refreshed=True, reason=reason, head=head, incremental=None, stale_files=stale
            )

        # `no_stamp`, `head_moved`, and `empty_store`: rebuild the graph without
        # firing the LLM. The triefacts on disk reflect whatever the user / team
        # committed; we trust them. The graph becomes consistent with the code;
        # any prose drift introduced by new code is the user's call to address
        # with `trie sync` when they're ready to spend. For `empty_store` this is
        # a pure recovery rebuild from the existing triefacts.
        scan_result = scan_project(project_root=project_root, config=config, store=store)
        if store.count_section_records() < store.count_symbols():
            backfill_section_records(project_root, config, store)
        write_stamp(project_root, Stamp(head=head, mtimes=current_mtimes))
        tele["files_scanned"] = scan_result.files_total
        tele["symbols_total"] = scan_result.symbols_total
        tele["edges_total"] = scan_result.edges_total
        return FreshnessResult(refreshed=True, reason=reason, head=head, incremental=None)
