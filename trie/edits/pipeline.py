"""The stage/commit edit pipeline.

`stage` generates patched + cascade-affected symbols IN PARALLEL via the pluggable
backend, drives each to compiling source, runs LSP in a scratch tree, and returns a
fully-validated, inspectable `StagedChangeSet` — NO writes to the real source tree.

`commit` flushes the validated set to disk (atomically per `commit_mode`), wrapping
DB mutations in `store.transaction()` and restoring from in-memory before-images on
failure. No persistent journal; git is the cross-turn backstop.

The agent owns correctness; this pipeline owns speed (parallelism), blast-radius
(cascade), and well-formedness (compiling + LSP-clean) of the hand-off.
"""

from __future__ import annotations

import os
import shutil
import tempfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, replace
from pathlib import Path

from trie.config import Config
from trie.edits.apply import (
    _compile_check,
    _file_fixup,
    _lsp_diagnostics,
    _read_prose,
    _refresh_file,
    _write_prose_section,
    lsp_backends_for_file,
)
from trie.edits.backends import EditRequest, EditResult, SymbolEditBackend
from trie.edits.cascade_plan import neighbour_context
from trie.edits.infer import merge_notes
from trie.edits.report import (
    CODE_BACKEND_FAILED,
    CODE_ORPHAN_CREATE,
    CODE_SECOND_ORDER,
    CODE_SYNTAX_AFTER_CAP,
    STAGE_CASCADE,
    STAGE_COMPILE,
    STAGE_GENERATE,
    AppliedItem,
    ApplyReport,
    StagedChange,
    UnresolvedItem,
    session_note_ok,
)
from trie.graph.store import Store, SymbolDetail
from trie.models import TrieClient


def _splice(file_lines: list[str], start_line: int, end_line: int, new_src: str) -> list[str]:
    """Replace the [start_line, end_line] (1-indexed inclusive) span with new_src.

    An empty `new_src` removes the span entirely (used for deletions).
    """
    out = list(file_lines)
    if new_src == "":
        out[start_line - 1 : end_line] = []
        return out
    block = new_src if new_src.endswith("\n") else new_src + "\n"
    out[start_line - 1 : end_line] = [block]
    return out


def _fix_imports_for_structural(
    text: str,
    *,
    deleted_names: set[str],
    renamed: dict[str, str],
) -> str:
    """Rewrite `from ... import ...` lines after a delete/rename.

    - deleted names are dropped from import lists (line removed if it empties out)
    - renamed names are replaced with their new name (preserving any `as` alias)
    Only touches `from X import a, b` style lines (the common cross-file case);
    leaves everything else untouched. Deterministic, no LLM.
    """
    if not deleted_names and not renamed:
        return text
    out_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if not stripped.startswith("from ") or " import " not in stripped:
            out_lines.append(line)
            continue
        newline_suffix = "\n" if line.endswith("\n") else ""
        head, _, names_part = stripped.partition(" import ")
        # Skip parenthesized / star imports — too varied to rewrite safely.
        if "(" in names_part or "*" in names_part:
            out_lines.append(line)
            continue
        kept: list[str] = []
        for raw in names_part.split(","):
            item = raw.strip()
            if not item:
                continue
            base = item.split(" as ")[0].strip()
            alias = item[len(base) :] if " as " in item else ""
            if base in deleted_names:
                continue  # drop it
            if base in renamed:
                kept.append(f"{renamed[base]}{alias}")
            else:
                kept.append(item)
        if not kept:
            continue  # whole import line removed
        indent = line[: len(line) - len(line.lstrip())]
        out_lines.append(f"{indent}{head} import {', '.join(kept)}{newline_suffix}")
    return "".join(out_lines)


def _read_span(file_text: str, start_line: int, end_line: int) -> str:
    lines = file_text.splitlines(keepends=True)
    return "".join(lines[start_line - 1 : end_line])


def _rename_source(old_source: str, detail: SymbolDetail, new_name: str) -> tuple[str, str | None]:
    """Rename the symbol's own definition within its source span.

    Deterministic-where-visible with refuse-on-ambiguity: replaces the `def`/`class`
    header name token. Returns (new_source, error). On a clean rename, error is None.
    Refuses (returns an error) when the new name is empty/invalid or the header
    token cannot be located unambiguously — caller surfaces it as unresolved.
    """
    if not new_name.isidentifier():
        return "", f"invalid rename target {new_name!r} (not a valid identifier)"
    old_name = detail.name
    if old_name == new_name:
        return "", f"rename target {new_name!r} equals current name"

    lines = old_source.splitlines(keepends=True)
    header_idx = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        for kw in ("def ", "class ", "async def "):
            if stripped.startswith(kw):
                after = stripped[len(kw) :]
                if after.startswith(old_name) and (
                    len(after) == len(old_name) or not after[len(old_name)].isidentifier()
                ):
                    header_idx = i
                    break
        if header_idx is not None:
            break
    if header_idx is None:
        return "", (
            f"could not locate the definition header for {old_name!r}; "
            "rename refused to avoid corrupting the source"
        )

    line = lines[header_idx]
    # Replace only the first occurrence of the name after the keyword.
    for kw in ("async def ", "def ", "class "):
        pos = line.find(kw)
        if pos != -1:
            name_pos = pos + len(kw)
            if line[name_pos : name_pos + len(old_name)] == old_name:
                lines[header_idx] = line[:name_pos] + new_name + line[name_pos + len(old_name) :]
                break
    return "".join(lines), None


def _synthesize_session_note(seed_qnames: list[str], create_grouped: dict[str, list[dict]]) -> str:
    """A truthful draft session note built from the pending ops.

    Returned as the `repatch` arg when the gate rejects a bad/empty note, so the
    cheap path (resend the draft) is also the honest path.
    """
    parts: list[str] = []
    for qn in seed_qnames:
        parts.append(qn.rsplit(":", 1)[-1])
    for creates in create_grouped.values():
        for cp in creates:
            parts.append(f"create {cp['target_qname'].rsplit(':', 1)[-1]}")
    summary = ", ".join(parts[:8])
    return f"edit {summary}" if summary else "batch edit"


@dataclass
class _GenJob:
    qname: str
    detail: SymbolDetail
    old_source: str
    old_prose: str
    notes: list[str]
    reasons: list[str]
    callees: list
    callers: list
    op: str = "modify"
    new_name: str = ""


def stage(
    store: Store,
    config: Config,
    backend: SymbolEditBackend,
    project_root: Path,
    *,
    client: TrieClient | None = None,
    session_note: str = "",
) -> tuple[ApplyReport, list[StagedChange]]:
    """Generate + validate all pending patches in parallel. No real writes.

    Returns (report, staged_changes). On a clean stage, report.ok is True and the
    staged_changes are ready for commit; unresolved items carry repatch calls.
    """
    src_root = (project_root / config.triefacts.source_root).resolve()
    triefacts_root = (project_root / config.triefacts.root).resolve()

    grouped = store.get_all_patches_grouped()
    create_grouped = store.get_create_patches_grouped()
    report = ApplyReport(session_note=session_note)
    if not grouped and not create_grouped:
        return report, []

    # Resolve seed qnames.
    seed_qnames: list[str] = []
    patches_by_qname: dict[str, list[dict]] = {}
    for sym_id, patch_list in grouped.items():
        row = store._conn.execute(
            "SELECT qualified_name FROM symbols WHERE id = ?", (sym_id,)
        ).fetchone()
        if row is None:
            continue
        qname = str(row[0])
        if store.get_symbol_detail(qname) is None:
            continue
        seed_qnames.append(qname)
        patches_by_qname[qname] = patch_list

    report.requested = len(seed_qnames) + sum(len(v) for v in create_grouped.values())
    if not seed_qnames and not create_grouped:
        return report, []

    # Session-note gate: a multi-symbol apply requires an authored unifying intent.
    # Single-symbol applies skip it (the per-symbol note IS the intent there).
    if report.requested > 1 and not session_note_ok(session_note):
        draft = _synthesize_session_note(seed_qnames, create_grouped)
        report.ok = False
        report.error = "session_note_required"
        report.unresolved.append(
            UnresolvedItem(
                qname="<session>",
                stage=STAGE_GENERATE,
                code="session_note_required",
                message=(
                    "multi-symbol apply requires a session_note summarizing the "
                    "change as a unit (>= 12 chars, not boilerplate)"
                ),
                repatch={"tool": "commit", "args": {"session_note": draft}},
            )
        )
        return report, []

    # Build generation jobs (merge notes + neighbour context), then fan out.
    jobs: list[_GenJob] = []
    # qnames being directly edited (seeds + cascade) — used to avoid double-editing
    # a symbol that's both a seed and a caller of another seed.
    queued: set[str] = set(seed_qnames)
    # modify seeds with their merged notes, for the cascade pre-filter.
    modify_seeds: list[tuple[str, list[str], list[str]]] = []
    # delete seeds: callers MUST be updated (the callee is vanishing).
    delete_seeds: list[str] = []
    # rename seeds: (old_qname, new_local_name) — callers must update the call name.
    rename_seeds: list[tuple[str, str]] = []

    for qname in seed_qnames:
        detail = store.get_symbol_detail(qname)
        if detail is None:
            continue
        patches = store.get_patches_for_qname(qname)
        if not patches:
            continue
        # A symbol's op is taken from its patches. Structural ops (delete/rename)
        # do not coexist with modify on the same symbol in v1; if mixed, the last
        # structural kind wins and modify notes are ignored for it.
        op = "modify"
        new_name = ""
        for p in patches:
            if p.get("kind") in ("delete", "rename"):
                op = p["kind"]
                new_name = p.get("rename_to") or ""
        if op == "modify":
            if client is not None:
                merged_notes, merged_reasons = merge_notes(client, patches)
            else:
                merged_notes = [p["note"] for p in patches]
                merged_reasons = [p["reason"] for p in patches]
            if not merged_notes:
                continue
            modify_seeds.append((qname, merged_notes, merged_reasons))
        else:
            merged_notes = [p["note"] for p in patches if p["note"]]
            merged_reasons = [p["reason"] for p in patches if p["reason"]]
            if op == "delete":
                delete_seeds.append(qname)
            elif op == "rename":
                rename_seeds.append((qname, new_name))
        callees, callers = neighbour_context(qname, store)
        try:
            old_source = _read_span(
                (src_root / detail.file_path).read_text(), detail.start_line, detail.end_line
            )
        except FileNotFoundError:
            old_source = ""
        old_prose = _read_prose(qname, detail.file_path, triefacts_root)
        jobs.append(
            _GenJob(
                qname,
                detail,
                old_source,
                old_prose,
                merged_notes,
                merged_reasons,
                callees,
                callers,
                op=op,
                new_name=new_name,
            )
        )

    # --- AUTO-CASCADE: edit direct callers that depend on a modified seed -------
    # Symbol-accurate (uses references_in on each seed, NOT file-level cascade),
    # LLM-gated (pre_filter_batch decides which callers actually need updates),
    # single sweep (cascade callers don't themselves re-cascade this run).
    _expand_caller_jobs(
        modify_seeds,
        queued,
        jobs,
        store,
        config,
        client,
        session_note,
        src_root,
        triefacts_root,
        report,
    )

    # Delete/rename cascade: callers of a vanishing or renamed symbol are
    # DEFINITELY affected (their call site references it), so no LLM gate — emit a
    # precise instruction note and let generation rewrite the call site. Captured
    # before the re-scan removes/renames the seed (references_in needs it present).
    _expand_structural_caller_jobs(
        delete_seeds,
        rename_seeds,
        queued,
        jobs,
        store,
        src_root,
        triefacts_root,
        report,
    )

    staged: list[StagedChange] = []

    # PARALLEL GENERATION — the speed core. One fan-out across all symbols.
    # Structural ops (delete/rename) are deterministic and skip the backend.
    def _gen(job: _GenJob):
        if job.op == "delete":
            return job, EditResult(job.qname, new_source="", new_prose="", ok=True)
        if job.op == "rename":
            new_src, err = _rename_source(job.old_source, job.detail, job.new_name)
            if err is not None:
                return job, EditResult(job.qname, "", "", ok=False, error=err)
            return job, EditResult(job.qname, new_source=new_src, new_prose="", ok=True)
        req = EditRequest(
            qname=job.qname,
            op="modify",
            old_source=job.old_source,
            old_prose=job.old_prose,
            merged_notes=job.notes,
            merged_reasons=job.reasons,
            session_note=session_note,
            callees=job.callees,
            callers=job.callers,
            file_path=job.detail.file_path,
        )
        return job, backend.generate(req)

    concurrency = max(1, config.sync.concurrency)
    results = []
    if concurrency > 1 and len(jobs) > 1:
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            results = list(pool.map(_gen, jobs))
    else:
        results = [_gen(job) for job in jobs]

    # Group results by file, splice + compile-gate, build StagedChanges.
    by_file: dict[str, list] = {}
    for job, res in results:
        by_file.setdefault(job.detail.file_path, []).append((job, res))

    for file_path, items in by_file.items():
        full_path = src_root / file_path
        try:
            before_bytes = full_path.read_text()
        except FileNotFoundError:
            for job, _res in items:
                report.unresolved.append(
                    UnresolvedItem(
                        qname=job.qname,
                        stage=STAGE_GENERATE,
                        code="file_not_found",
                        message=f"source file {file_path} not found",
                        source_pointer=f"{file_path}",
                    )
                )
            report.ok = False
            continue

        # Apply spliced edits highest-line-first so earlier line numbers stay valid.
        items_sorted = sorted(items, key=lambda it: it[0].detail.start_line, reverse=True)
        file_lines = before_bytes.splitlines(keepends=True)
        per_symbol_new: dict[str, str] = {}
        per_symbol_prose: dict[str, str] = {}
        failed_in_file = False

        for job, res in items_sorted:
            if not res.ok:
                if job.op == "rename":
                    repatch = {
                        "tool": "rename_symbol",
                        "args": {"qname": job.qname, "new_name": job.new_name},
                    }
                else:
                    repatch = {
                        "tool": "patch",
                        "args": {"qname": job.qname, "note": "; ".join(job.notes)},
                    }
                report.unresolved.append(
                    UnresolvedItem(
                        qname=job.qname,
                        stage=STAGE_GENERATE,
                        code=CODE_BACKEND_FAILED,
                        message=res.error or "backend failed to generate",
                        source_pointer=f"{file_path}:{job.detail.start_line}",
                        repatch=repatch,
                    )
                )
                report.ok = False
                failed_in_file = True
                continue
            file_lines = _splice(
                file_lines, job.detail.start_line, job.detail.end_line, res.new_source
            )
            per_symbol_new[job.qname] = res.new_source
            per_symbol_prose[job.qname] = res.new_prose

        if failed_in_file:
            continue

        after_bytes = "".join(file_lines)
        if not after_bytes.endswith("\n"):
            after_bytes += "\n"

        # Deterministic import fixup for delete/rename: symbol-span splices cannot
        # touch module-level `import` lines, so a deleted/renamed callee leaves a
        # broken import. Rewrite those import lines here (drop deleted names, rename
        # renamed ones) so the caller file stays importable.
        after_bytes = _fix_imports_for_structural(
            after_bytes,
            deleted_names={q.rsplit(":", 1)[-1] for q in delete_seeds},
            renamed={q.rsplit(":", 1)[-1]: nn for q, nn in rename_seeds},
        )

        # Compile gate (well-formedness, not correctness).
        if not _compile_check(after_bytes):
            for job, _res in items:
                report.unresolved.append(
                    UnresolvedItem(
                        qname=job.qname,
                        stage=STAGE_COMPILE,
                        code=CODE_SYNTAX_AFTER_CAP,
                        message="spliced file does not compile",
                        source_pointer=f"{file_path}:{job.detail.start_line}",
                        repatch={
                            "tool": "patch",
                            "args": {
                                "qname": job.qname,
                                "source": per_symbol_new.get(job.qname, ""),
                            },
                        },
                    )
                )
            report.ok = False
            continue

        for job, _res in items:
            staged.append(
                StagedChange(
                    qname=job.qname,
                    op=job.op,
                    file_path=file_path,
                    old_source=job.old_source,
                    new_source=per_symbol_new.get(job.qname, ""),
                    new_prose=per_symbol_prose.get(job.qname, ""),
                    before_file_bytes=before_bytes,
                    after_file_bytes=after_bytes,
                    lsp_iterations=0,
                )
            )

    # --- create lane: new symbols placed into (existing) target files ---------
    _stage_creates(
        create_grouped, store, config, backend, project_root, session_note, report, staged
    )

    # --- LSP gate: ONE multi-file scratch overlay over ALL changed files -------
    # Single-file scratch is unsound for cross-file edits (e.g. a rename makes the
    # new name look undefined in a 1-file view, and the fixup LLM reverts it). We
    # materialize every changed file's final candidate together so the checker sees
    # a consistent tree, then fix each file against that whole-batch view.
    _multifile_scratch_lsp(staged, src_root, config, client)

    return report, staged


def _expand_caller_jobs(
    modify_seeds: list[tuple[str, list[str], list[str]]],
    queued: set[str],
    jobs: list[_GenJob],
    store: Store,
    config: Config,
    client: TrieClient | None,
    session_note: str,
    src_root: Path,
    triefacts_root: Path,
    report: ApplyReport,
) -> None:
    """Add generation jobs for direct callers that depend on a modified seed.

    Symbol-accurate: callers come from `references_in(seed)`, so only true callers
    of the changed symbol are considered (not every symbol in the changed file).
    LLM-gated via `pre_filter_batch` when a client is available; otherwise (e.g.
    deterministic tests) cascade is skipped. Hub seeds (inbound over threshold) are
    not expanded, matching the read-side cascade guard. Single sweep.
    """
    if not modify_seeds:
        return

    from trie.edits.infer import _build_caller_summaries, _read_prose, pre_filter_batch

    hub = config.cascade.hub_symbol_threshold

    # Build (callee_qname, old_prose, caller_summaries, notes_reasons) pairs.
    callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]] = []
    for qname, notes, reasons in modify_seeds:
        callers_raw = store.references_in(qname)
        if not callers_raw or len(callers_raw) > hub:
            continue
        callers = _build_caller_summaries(callers_raw, store, triefacts_root, src_root)
        if not callers:
            continue
        detail = store.get_symbol_detail(qname)
        old_prose = _read_prose(qname, detail.file_path, triefacts_root) if detail else ""
        notes_reasons = list(zip(notes, reasons, strict=False))
        callee_pairs.append((qname, old_prose, callers, notes_reasons))

    if not callee_pairs:
        return

    # No client → cannot run the gated filter; surface callers as advisory instead
    # of guessing. (Deterministic test path.)
    if client is None:
        if config.cascade.surface_unresolved:
            for _qn, _op, callers, _nr in callee_pairs:
                for c in callers:
                    cqn = c["qname"]
                    if cqn in queued:
                        continue
                    queued.add(cqn)
                    cdetail = store.get_symbol_detail(cqn)
                    ptr = f"{cdetail.file_path}:{cdetail.start_line}" if cdetail else ""
                    report.unresolved.append(
                        UnresolvedItem(
                            qname=cqn,
                            stage=STAGE_CASCADE,
                            code=CODE_SECOND_ORDER,
                            message="caller of an edited symbol; review and re-patch if affected",
                            source_pointer=ptr,
                            repatch={"tool": "patch", "args": {"qname": cqn, "note": ""}},
                            blocking=False,
                        )
                    )
        return

    decisions = pre_filter_batch(client, callee_pairs, batch_size=8)
    for caller_qn, note, reason in decisions:
        if caller_qn in queued:
            continue
        detail = store.get_symbol_detail(caller_qn)
        if detail is None:
            continue
        queued.add(caller_qn)
        try:
            old_source = _read_span(
                (src_root / detail.file_path).read_text(),
                detail.start_line,
                detail.end_line,
            )
        except FileNotFoundError:
            continue
        old_prose = _read_prose(caller_qn, detail.file_path, triefacts_root)
        callees, callers = neighbour_context(caller_qn, store)
        jobs.append(
            _GenJob(
                caller_qn,
                detail,
                old_source,
                old_prose,
                [note or "update to match the change in a callee"],
                [reason or "cascade"],
                callees,
                callers,
                op="modify",
            )
        )


def _expand_structural_caller_jobs(
    delete_seeds: list[str],
    rename_seeds: list[tuple[str, str]],
    queued: set[str],
    jobs: list[_GenJob],
    store: Store,
    src_root: Path,
    triefacts_root: Path,
    report: ApplyReport,
) -> None:
    """Cascade callers of deleted/renamed symbols. No LLM gate: the call site
    references a symbol that is vanishing (delete) or changing name (rename), so it
    is definitely affected. Emit a precise instruction and let generation rewrite
    the call site (a modify job on the caller)."""

    def _queue_caller(caller_qn: str, note: str, reason: str) -> None:
        if caller_qn in queued:
            return
        detail = store.get_symbol_detail(caller_qn)
        if detail is None:
            return
        queued.add(caller_qn)
        try:
            old_source = _read_span(
                (src_root / detail.file_path).read_text(),
                detail.start_line,
                detail.end_line,
            )
        except FileNotFoundError:
            return
        old_prose = _read_prose(caller_qn, detail.file_path, triefacts_root)
        callees, callers = neighbour_context(caller_qn, store)
        jobs.append(
            _GenJob(
                caller_qn,
                detail,
                old_source,
                old_prose,
                [note],
                [reason],
                callees,
                callers,
                op="modify",
            )
        )

    for qname in delete_seeds:
        short = qname.rsplit(":", 1)[-1]
        for caller_qn in store.references_in(qname):
            _queue_caller(
                caller_qn,
                f"the function `{short}` is being DELETED; remove or replace every "
                f"call to `{short}` here so this code no longer depends on it",
                f"callee {short} deleted",
            )

    for qname, new_name in rename_seeds:
        short = qname.rsplit(":", 1)[-1]
        for caller_qn in store.references_in(qname):
            _queue_caller(
                caller_qn,
                f"the function `{short}` has been RENAMED to `{new_name}`; update "
                f"every call from `{short}(...)` to `{new_name}(...)` (and the import "
                f"if present)",
                f"callee {short} renamed to {new_name}",
            )


def _stage_creates(
    create_grouped: dict[str, list[dict]],
    store: Store,
    config: Config,
    backend: SymbolEditBackend,
    project_root: Path,
    session_note: str,
    report: ApplyReport,
    staged: list[StagedChange],
) -> None:
    """Generate + place each new symbol; append StagedChanges with op='create'.

    Placement: after the anchor symbol's span if given and resolvable, else at
    end-of-file. The whole resulting file is compile-gated; on failure the symbol
    goes to unresolved with its generated source verbatim for re-patching.
    """
    src_root = (project_root / config.triefacts.source_root).resolve()
    for file_path, creates in create_grouped.items():
        full_path = src_root / file_path

        # If the modify/structural lane already staged edits for this file, stack
        # creates ON TOP of that lane's result so the file ends up with a single
        # coherent after_file_bytes (commit writes one per file). Otherwise start
        # from the on-disk original.
        prior = [ch for ch in staged if ch.file_path == file_path]
        if prior:
            true_before = prior[0].before_file_bytes
            after_bytes = prior[0].after_file_bytes
        else:
            try:
                true_before = full_path.read_text()
            except FileNotFoundError:
                # New-file creation is deferred (WS: new files). For now require the
                # target file to exist; surface a clear, re-patchable error.
                for cp in creates:
                    report.unresolved.append(
                        UnresolvedItem(
                            qname=cp["target_qname"],
                            stage=STAGE_GENERATE,
                            code="file_not_found",
                            message=f"target file {file_path} does not exist (new-file create "
                            "not supported in v1)",
                            source_pointer=file_path,
                        )
                    )
                    report.ok = False
                continue
            after_bytes = true_before

        before_bytes = true_before
        placed: list[tuple[str, str]] = []  # (qname, new_source)
        for cp in creates:
            qname = cp["target_qname"]
            req = EditRequest(
                qname=qname,
                op="create",
                old_source="",
                old_prose="",
                merged_notes=[cp["note"]] if cp["note"] else [],
                merged_reasons=[cp["reason"]] if cp["reason"] else [],
                session_note=session_note,
                callees=[],
                callers=[],
                file_path=file_path,
            )
            res = backend.generate(req)
            if not res.ok or not res.new_source.strip():
                report.unresolved.append(
                    UnresolvedItem(
                        qname=qname,
                        stage=STAGE_GENERATE,
                        code=CODE_BACKEND_FAILED,
                        message=res.error or "backend produced no source for new symbol",
                        source_pointer=file_path,
                        repatch={
                            "tool": "create_symbol",
                            "args": {"qname": qname, "note": cp["note"]},
                        },
                    )
                )
                report.ok = False
                continue
            after_bytes = _place_new_symbol(
                after_bytes, res.new_source, cp.get("anchor_qname"), store
            )
            placed.append((qname, res.new_source))

        if not placed:
            continue

        if not after_bytes.endswith("\n"):
            after_bytes += "\n"

        if not _compile_check(after_bytes):
            for qname, new_src in placed:
                report.unresolved.append(
                    UnresolvedItem(
                        qname=qname,
                        stage=STAGE_COMPILE,
                        code=CODE_SYNTAX_AFTER_CAP,
                        message="file does not compile after inserting new symbol",
                        source_pointer=file_path,
                        repatch={
                            "tool": "create_symbol",
                            "args": {"qname": qname, "source": new_src},
                        },
                    )
                )
            report.ok = False
            continue

        # Rewrite prior staged changes for this file so EVERY change to the file
        # shares the final after_file_bytes (commit writes one blob per file).
        for i, ch in enumerate(staged):
            if ch.file_path == file_path:
                staged[i] = replace(ch, after_file_bytes=after_bytes)

        for qname, new_src in placed:
            staged.append(
                StagedChange(
                    qname=qname,
                    op="create",
                    file_path=file_path,
                    old_source="",
                    new_source=new_src,
                    new_prose="",
                    before_file_bytes=before_bytes,
                    after_file_bytes=after_bytes,
                    lsp_iterations=0,
                )
            )


def _place_new_symbol(
    file_text: str,
    new_source: str,
    anchor_qname: str | None,
    store: Store,
) -> str:
    """Insert new_source after the anchor symbol's span, else at end-of-file."""
    block = new_source if new_source.endswith("\n") else new_source + "\n"
    if anchor_qname:
        detail = store.get_symbol_detail(anchor_qname)
        if detail is not None:
            lines = file_text.splitlines(keepends=True)
            insert_at = detail.end_line  # 1-indexed inclusive → slice index
            head = "".join(lines[:insert_at])
            tail = "".join(lines[insert_at:])
            return head + "\n\n" + block + tail
    if not file_text.strip():
        return block
    return file_text.rstrip("\n") + "\n\n\n" + block


def _multifile_scratch_lsp(
    staged: list[StagedChange],
    src_root: Path,
    config: Config,
    client: TrieClient | None,
) -> None:
    """Run LSP + bounded fixup over ALL changed files in one consistent scratch tree.

    Mutates `staged` in place (each file's after_file_bytes may be replaced by an
    LSP-cleaned version). The whole-batch overlay (every changed file's candidate
    written, the rest of the package hardlinked) means a cross-file rename/delete
    is seen consistently — the checker won't flag the new name as undefined and the
    fixup won't revert it. LSP is a well-formedness gate, never a correctness gate;
    any error degrades to "leave candidates as-is".
    """
    if client is None:
        return
    # Latest candidate per file (all StagedChanges for a file share after_file_bytes).
    file_candidates: dict[str, str] = {}
    for ch in staged:
        file_candidates[ch.file_path] = ch.after_file_bytes
    if not file_candidates:
        return
    # Proceed only if at least one candidate file has a checker (a language
    # backend default or the configured fallback).
    if not any(lsp_backends_for_file(src_root / fp, config) for fp in file_candidates):
        return

    scratch_root = Path(tempfile.mkdtemp(prefix="trie-scratch-"))
    try:
        # Hardlink the whole package so imports resolve, then overlay candidates.
        _overlay_package(src_root, scratch_root)
        for fp, content in file_candidates.items():
            sf = scratch_root / fp
            sf.parent.mkdir(parents=True, exist_ok=True)
            sf.write_text(content)

        fixed_by_file: dict[str, str] = dict(file_candidates)
        for fp in file_candidates:
            content = fixed_by_file[fp]
            file_lsp_backends = lsp_backends_for_file(src_root / fp, config)
            for _ in range(config.edits.lsp_max_retries):
                sf = scratch_root / fp
                sf.write_text(content)
                diags = _lsp_diagnostics(sf, file_lsp_backends)
                if not diags:
                    break
                fixed = _file_fixup(client, fp, content, diags)
                if fixed is None or not _compile_check(fixed):
                    break
                if not fixed.endswith("\n"):
                    fixed += "\n"
                content = fixed
                sf.write_text(content)  # keep overlay consistent for other files
            fixed_by_file[fp] = content

        # Write back any LSP-cleaned candidates into the staged changes.
        for i, ch in enumerate(staged):
            new_after = fixed_by_file.get(ch.file_path)
            if new_after is not None and new_after != ch.after_file_bytes:
                staged[i] = replace(ch, after_file_bytes=new_after)
    except Exception:
        return
    finally:
        shutil.rmtree(scratch_root, ignore_errors=True)


_OVERLAY_SKIP_PARTS = {".trie", "__pycache__", "node_modules", ".git", "dist", "build"}


def _overlay_package(src_root: Path, scratch_root: Path) -> None:
    """Hardlink every indexable source file (+ each language's required config
    files, e.g. tsconfig.json / package.json) under src_root into scratch_root.

    Cheap (hardlinks, no copy) and gives the checker the full import graph.
    Globs come from the registered language backends, so a TS edit gets the
    `.ts`/`.tsx` graph plus tsconfig for module resolution. Candidate files are
    overwritten by the caller after this runs.
    """
    from trie.parse import registry

    globs: set[str] = set()
    extra_names: set[str] = set()
    for backend in registry.all_backends():
        globs.update(backend.overlay_globs())
        extra_names.update(backend.overlay_extra_files())

    def _link(path: Path) -> None:
        if any(part in _OVERLAY_SKIP_PARTS for part in path.parts):
            return
        rel = path.relative_to(src_root)
        dest = scratch_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            return
        try:
            os.link(path, dest)
        except OSError:
            dest.write_bytes(path.read_bytes())

    for pattern in globs:
        for path in src_root.rglob(pattern):
            if path.is_file():
                _link(path)
    for name in extra_names:
        for path in src_root.rglob(name):
            if path.is_file():
                _link(path)


def commit(
    store: Store,
    config: Config,
    project_root: Path,
    report: ApplyReport,
    staged: list[StagedChange],
    *,
    commit_mode: str | None = None,
) -> ApplyReport:
    """Write the validated staged set to disk atomically; refresh + drop patches.

    all_or_nothing (default): any prior unresolved → write nothing.
    per_item: write each file's changes independently; failures stay unresolved.
    """
    mode = (commit_mode or config.edits.commit_mode or "all_or_nothing").lower()
    src_root = (project_root / config.triefacts.source_root).resolve()
    triefacts_root = (project_root / config.triefacts.root).resolve()

    if not staged:
        return report

    if mode == "all_or_nothing" and report.blocking_unresolved:
        # A blocking failure occurred during stage; commit nothing. Advisory
        # (non-blocking) unresolved items — e.g. second-order cascade — do not
        # block the commit.
        report.ok = False
        report.committed = False
        return report

    # Group staged changes by file (one before-image per file).
    by_file: dict[str, list[StagedChange]] = {}
    for ch in staged:
        by_file.setdefault(ch.file_path, []).append(ch)

    # Capture create-patch ids BEFORE any scan: a re-scan that introduces the new
    # symbol does not remove its create_patch row, so we clear them explicitly.
    create_qnames = [ch.qname for ch in staged if ch.op == "create"]
    written: list[tuple[str, str]] = []  # (file_path, before_bytes) for rollback
    try:
        # Write source first; the source tree (git-backed) is the unit we roll back.
        for file_path, changes in by_file.items():
            full_path = src_root / file_path
            before = changes[0].before_file_bytes
            after = changes[0].after_file_bytes
            full_path.write_text(after)
            written.append((file_path, before))

        # Always re-scan touched files so the graph absorbs the new symbol roster,
        # edges, AND refreshed line numbers. Structural ops obviously need it, but
        # pure modifies do too: a modify that changes a symbol's line count shifts
        # every later symbol in the file, and a stale start_line/end_line breaks the
        # next rename/delete/modify on that file (it reads the wrong span). scan is
        # idempotent and only re-parses changed files.
        from trie.scan import scan_project

        scan_project(project_root=project_root, config=config, store=store)

        for file_path, changes in by_file.items():
            for ch in changes:
                if ch.new_prose:
                    _write_prose_section(
                        ch.qname, file_path, ch.new_prose, triefacts_root, src_root
                    )
            _refresh_file(file_path, project_root, config, store)

        # Drop applied patches. Modify/rename/delete patch rows on symbols that
        # were removed/renamed are already gone via FK cascade after the re-scan;
        # delete_patches is a harmless no-op there. Create patches need explicit
        # removal (they live in their own table, unaffected by symbol cascade).
        for ch in staged:
            if ch.op != "create":
                store.delete_patches(qname=ch.qname)
        for qn in create_qnames:
            store.delete_create_patches(target_qname=qn)
    except Exception as exc:
        # Restore source from in-memory before-images (no persistent journal).
        for file_path, before in written:
            (src_root / file_path).write_text(before)
        report.ok = False
        report.committed = False
        report.error = f"commit failed, rolled back: {exc}"
        return report

    for ch in staged:
        report.applied.append(
            AppliedItem(
                qname=ch.qname,
                op=ch.op,
                file_path=ch.file_path,
                prose_written=bool(ch.new_prose),
                lsp_iterations=ch.lsp_iterations,
            )
        )

    # Forward-wiring advisory: a freshly CREATED symbol that nothing references is
    # an orphan — the system can't auto-discover who should call it (the edge does
    # not exist yet). Surface it so the agent wires it in (or confirms it's an
    # entrypoint). Side-effects of a new symbol must be considered by the caller it
    # gets wired into; that wiring is a follow-up patch on that caller.
    for qn in create_qnames:
        detail = store.get_symbol_detail(qn)
        if detail is not None and detail.inbound_count == 0:
            report.unresolved.append(
                UnresolvedItem(
                    qname=qn,
                    stage=STAGE_CASCADE,
                    code=CODE_ORPHAN_CREATE,
                    message=(
                        f"created `{qn.rsplit(':', 1)[-1]}` but nothing calls it yet; "
                        "wire it into a caller (patch the caller to use it) or confirm "
                        "it is an entrypoint"
                    ),
                    source_pointer=f"{detail.file_path}:{detail.start_line}",
                    repatch={"tool": "patch", "args": {"qname": "<caller-qname>", "note": ""}},
                    blocking=False,
                )
            )

    report.committed = True
    report.ok = not report.blocking_unresolved
    return report


def stage_and_commit(
    store: Store,
    config: Config,
    backend: SymbolEditBackend,
    project_root: Path,
    *,
    client: TrieClient | None = None,
    session_note: str = "",
    commit_mode: str | None = None,
) -> ApplyReport:
    """One-shot: stage then commit. The `commit()` MCP tool calls this."""
    report, staged = stage(
        store, config, backend, project_root, client=client, session_note=session_note
    )
    return commit(store, config, project_root, report, staged, commit_mode=commit_mode)
