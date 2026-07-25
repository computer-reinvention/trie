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

import contextlib
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
    ModuleRemark,
    StagedChange,
    UnresolvedItem,
    session_note_ok,
)
from trie.graph.store import Store, SymbolDetail
from trie.models import TrieClient
from trie.session_log import record_applied


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


def _per_symbol_compile_salvage(before_bytes, items, per_symbol_new, file_path):
    """Salvage a failed whole-file batch by keeping only symbols that compile.

    The whole-file splice didn't compile. Re-splice each successful symbol ALONE
    onto the original file and keep it only if that single-symbol result compiles;
    then splice all the survivors together (highest-line-first so spans stay
    valid) and confirm the combined file compiles. Returns
    ``(good_items, combined_after_bytes)``. If even the combined survivors fail
    (a cross-symbol interaction), returns ``([], original_bytes)``.

    This makes one bad generation cost only its own symbol instead of failing
    every other symbol in the file — the difference between "apply did nothing"
    and "apply landed 9 of 10".
    """
    good = []
    for it in items:
        job, res = it
        if not res.ok:
            continue
        single = _splice(
            before_bytes.splitlines(keepends=True),
            job.detail.start_line,
            job.detail.end_line,
            per_symbol_new.get(job.qname, ""),
        )
        candidate = "".join(single)
        if not candidate.endswith("\n"):
            candidate += "\n"
        if _compile_check(candidate, file_path):
            good.append(it)
    if not good:
        return [], before_bytes
    # Splice all survivors together, highest-line-first so earlier spans stay valid.
    lines = before_bytes.splitlines(keepends=True)
    for job, _res in sorted(good, key=lambda it: it[0].detail.start_line, reverse=True):
        lines = _splice(
            lines, job.detail.start_line, job.detail.end_line, per_symbol_new[job.qname]
        )
    combined = "".join(lines)
    if not combined.endswith("\n"):
        combined += "\n"
    if not _compile_check(combined, file_path):
        return [], before_bytes
    return good, combined


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
        per_symbol_remarks: dict[str, str] = {}
        per_symbol_deps: dict[str, tuple[str, ...]] = {}
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
            if res.module_remarks.strip():
                per_symbol_remarks[job.qname] = res.module_remarks.strip()
            if res.new_dependencies:
                per_symbol_deps[job.qname] = tuple(res.new_dependencies)

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
        if not _compile_check(after_bytes, file_path):
            # All-symbols splice didn't compile. Don't doom the whole file: a
            # single bad symbol (e.g. a body that smuggled in an import) would
            # otherwise mark every other (perfectly good) symbol in the file as
            # failed and commit nothing — which is what drove agents off the
            # pipeline into hand-edits. Degrade to per-symbol: re-splice each
            # symbol alone onto the ORIGINAL file and keep the ones that compile.
            good_items, after_bytes = _per_symbol_compile_salvage(
                before_bytes, items, per_symbol_new, file_path
            )
            bad_items = [it for it in items if it not in good_items]
            for job, _res in bad_items:
                report.unresolved.append(
                    UnresolvedItem(
                        qname=job.qname,
                        stage=STAGE_COMPILE,
                        code=CODE_SYNTAX_AFTER_CAP,
                        message="spliced symbol does not compile",
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
            if bad_items:
                report.ok = False
            if not good_items:
                continue
            items = good_items

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
                    module_remarks=per_symbol_remarks.get(job.qname, ""),
                    new_dependencies=per_symbol_deps.get(job.qname, ()),
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


def build_workorder(store, config, project_root, *, client=None, session_note=""):
    patches_by_sym_id = store.get_all_patches_grouped()
    create_grouped = store.get_create_patches_grouped()

    # Resolve seed qnames from symbol_id keys
    seeds = []
    unresolved = []
    for sym_id, patches in patches_by_sym_id.items():
        row = store._conn.execute(
            "SELECT qualified_name FROM symbols WHERE id = ?", (sym_id,)
        ).fetchone()
        if row is None:
            continue
        qname = row[0]
        detail = store.get_symbol_detail(qname)
        if detail is None:
            unresolved.append(
                {"qname": qname, "code": "not_found", "message": f"{qname} not found in store"}
            )
            continue
        seeds.append((qname, detail, patches))

    seed_qnames = [s[0] for s in seeds]

    # Session-note gate
    total_items = len(seeds) + sum(len(v) for v in create_grouped.values())
    if not session_note_ok(session_note) and total_items > 1:
        return {
            "ok": False,
            "mode": "workorder",
            "error": "session_note_required",
            "unresolved": [
                {
                    "qname": "<session>",
                    "code": "session_note_required",
                    "message": "A session_note is required when committing more than one symbol.",
                    "repatch": {
                        "tool": "commit",
                        "args": {
                            "session_note": _synthesize_session_note(seed_qnames, create_grouped)
                        },
                    },
                }
            ],
        }

    # Build items for modify/delete/rename seeds
    items = []
    for qname, detail, patches in seeds:
        # Classify op with last-structural-wins rule
        op = "modify"
        rename_to = None
        for p in patches:
            kind = p.get("kind")
            if kind in ("delete", "rename", "modify"):
                op = kind
                if kind == "rename":
                    rename_to = p.get("rename_to")

        # Merge notes and reasons
        if client is not None and op == "modify":
            notes, reasons = merge_notes(client, patches)
        else:
            notes = [p["note"] for p in patches if p.get("note")]
            reasons = [p["reason"] for p in patches if p.get("reason")]

        # Compute callers to review
        _callees, callers = neighbour_context(qname, store)
        callers_to_review = [c.qname for c in callers]

        item = {
            "qname": qname,
            "op": op,
            "file_path": detail.file_path,
            "start_line": detail.start_line,
            "end_line": detail.end_line,
            "notes": notes,
            "reasons": reasons,
            "callers_to_review": callers_to_review,
        }
        if op == "rename" and rename_to is not None:
            item["rename_to"] = rename_to

        items.append(item)

    # Build creates list by flattening create_grouped values
    creates = []
    for _target_file, cpatches in create_grouped.items():
        for cpatch in cpatches:
            creates.append(
                {
                    "target_qname": cpatch.get("target_qname", ""),
                    "target_file": cpatch.get("target_file", ""),
                    "anchor_qname": cpatch.get("anchor_qname", ""),
                    "parent_class": cpatch.get("parent_class", ""),
                    "note": cpatch.get("note", ""),
                    "reason": cpatch.get("reason", ""),
                }
            )

    # Compute expected_symbols
    item_qnames = [item["qname"] for item in items]
    create_qnames = [c["target_qname"] for c in creates]
    expected_symbols = sorted(set(item_qnames + create_qnames))

    return {
        "ok": True,
        "mode": "workorder",
        "session_note": session_note,
        "items": items,
        "creates": creates,
        "expected_symbols": expected_symbols,
        "unresolved": unresolved,
        "next": (
            "Edit the listed symbols natively with your own tools, honoring every note. "
            "Then run trie refresh to regenerate prose, and trie patch drop --all to clear the queue. "
            "Out-of-plan symbol edits should get an amending patch note before you finish."
        ),
    }


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
    end-of-file. The whole resulting file is compile-gated; on failure each symbol
    is re-placed alone against the pre-creates base image and the compiling subset
    is salvaged (mirroring the modify lane's per-symbol compile salvage). Only
    genuinely broken symbols surface as unresolved; their compiling siblings land
    normally.
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
                # True new-file creation: scaffold from empty. The generated
                # symbol source becomes the file body; commit() mkdirs parents
                # and the post-commit scan absorbs the new file into the graph.
                true_before = ""
            after_bytes = true_before

        before_bytes = true_before
        # Capture the pre-creates file image for per-symbol salvage.
        base_bytes = after_bytes

        # (qname, new_source, module_remarks, new_dependencies, anchor_qname)
        placed: list[tuple[str, str, str, tuple[str, ...], str | None]] = []
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
            anchor_qname = cp.get("anchor_qname")
            after_bytes = _place_new_symbol(
                after_bytes, res.new_source, anchor_qname, store, qname=qname
            )
            placed.append(
                (
                    qname,
                    res.new_source,
                    res.module_remarks.strip(),
                    tuple(res.new_dependencies),
                    anchor_qname,
                )
            )

        if not placed:
            continue

        if not after_bytes.endswith("\n"):
            after_bytes += "\n"

        if not _compile_check(after_bytes, file_path):
            # Per-symbol salvage: re-place each symbol alone against base_bytes
            # and check if it compiles individually.
            good: list[tuple[str, str, str, tuple[str, ...], str | None]] = []
            bad: list[tuple[str, str, str, tuple[str, ...], str | None]] = []
            for entry in placed:
                qname, new_src, remarks, deps, anchor_qname = entry
                candidate = _place_new_symbol(base_bytes, new_src, anchor_qname, store, qname=qname)
                if not candidate.endswith("\n"):
                    candidate += "\n"
                if _compile_check(candidate, file_path):
                    good.append(entry)
                else:
                    bad.append(entry)

            # Try to rebuild cumulatively from the good set.
            salvaged = False
            if good:
                rebuilt = base_bytes
                for entry in good:
                    qname, new_src, remarks, deps, anchor_qname = entry
                    rebuilt = _place_new_symbol(rebuilt, new_src, anchor_qname, store, qname=qname)
                if not rebuilt.endswith("\n"):
                    rebuilt += "\n"
                if _compile_check(rebuilt, file_path):
                    after_bytes = rebuilt
                    placed = good
                    salvaged = True
                    # Report the bad ones as unresolved.
                    for entry in bad:
                        qname, new_src, _remarks, _deps, _anchor = entry
                        report.unresolved.append(
                            UnresolvedItem(
                                qname=qname,
                                stage=STAGE_COMPILE,
                                code=CODE_SYNTAX_AFTER_CAP,
                                message=(
                                    "generated source for this symbol does not compile; "
                                    "sibling creates in the file were salvaged"
                                ),
                                source_pointer=file_path,
                                repatch={
                                    "tool": "create_symbol",
                                    "args": {"qname": qname, "source": new_src},
                                },
                            )
                        )
                    report.ok = False

            if not salvaged:
                # Nothing could be salvaged — fail all placed entries.
                for entry in placed:
                    qname, new_src, _remarks, _deps, _anchor = entry
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

        for qname, new_src, remarks, deps, _anchor in placed:
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
                    module_remarks=remarks,
                    new_dependencies=deps,
                )
            )


def _place_new_symbol(
    file_text: str,
    new_source: str,
    anchor_qname: str | None,
    store: Store,
    *,
    qname: str | None = None,
) -> str:
    """Insert new_source into file_text.

    Placement priority:
    1. A member create (`module:Parent.child`) is inserted INSIDE the parent's
       body, re-indented to member level, so a new class method/field lands in
       the class rather than at file scope (which would be invalid).
    2. An explicit `anchor_qname` → directly after that symbol's span.
    3. Otherwise end-of-file (or the whole file when empty).
    """
    block = new_source if new_source.endswith("\n") else new_source + "\n"

    # (1) Member create: route into the parent container's body.
    if qname is not None:
        module, _, local = qname.partition(":")
        if "." in local:
            parent_local = local.rsplit(".", 1)[0]
            parent_detail = store.get_symbol_detail(f"{module}:{parent_local}")
            if parent_detail is not None:
                parent_name = parent_local.rsplit(".", 1)[-1]
                placed = _insert_into_parent(file_text, block, parent_detail, parent_name)
                if placed is not None:
                    return placed

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


def _find_container_span(lines: list[str], name: str | None) -> tuple[int, int] | None:
    """Locate `name`'s container declaration span (0-indexed start, exclusive end).

    Used to recover a parent class/interface span when stored line numbers are
    stale. Finds the first line declaring the container by name (matching
    `class`/`interface`/`enum`/`namespace`/`def`-style headers loosely via the
    name + an opening `{` or `:`), then computes its end:
    - brace style: balance `{`/`}` from the opening line to the matching close.
    - colon/indent style (Python): the run of lines indented deeper than the
      header until the first line at or below the header's indentation.
    Returns None when not found.
    """
    if not name:
        return None
    header_idx = None
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        if name in ln and (
            stripped.startswith(("class ", "export class ", "interface ", "export interface "))
            or stripped.startswith(("enum ", "export enum ", "namespace ", "abstract class "))
            or (stripped.startswith(("class ", "def ")) and stripped.rstrip().endswith(":"))
        ):
            # Confirm the matched word is the declared name (next token).
            header_idx = i
            break
    if header_idx is None:
        return None

    opening = lines[header_idx]
    if "{" in opening:
        depth = 0
        seen = False
        for j in range(header_idx, len(lines)):
            for ch in lines[j]:
                if ch == "{":
                    depth += 1
                    seen = True
                elif ch == "}":
                    depth -= 1
            if seen and depth == 0:
                return (header_idx, j + 1)
        return None
    # Indentation (Python) style.
    header_indent = len(opening) - len(opening.lstrip())
    end = header_idx + 1
    for j in range(header_idx + 1, len(lines)):
        if not lines[j].strip():
            end = j + 1
            continue
        indent = len(lines[j]) - len(lines[j].lstrip())
        if indent <= header_indent:
            break
        end = j + 1
    return (header_idx, end)


def _insert_into_parent(
    file_text: str, block: str, parent_detail, parent_name: str | None = None
) -> str | None:
    """Insert `block` as the last member inside the parent container's body.

    Language-neutral: re-indents `block` to one level deeper than the parent's
    own indentation and splices it just before the parent's final line. For a
    brace language (TS/JS) the parent's last line is the closing `}`; for an
    indentation language (Python) it's the last member line, so we append after
    the body instead. Returns None when the span looks unusable (caller falls
    back to file-scope placement).

    `parent_detail`'s stored line numbers can be STALE when an earlier change in
    the same batch shifted the file (a modify stacked before this create). We
    validate the span against the current text using `parent_name`; if it no
    longer points at the parent declaration, we recompute the span by searching
    the text for the declaration, so same-file modify+create batches stay valid.
    """
    lines = file_text.splitlines(keepends=True)
    start = parent_detail.start_line - 1  # 0-indexed
    end = parent_detail.end_line  # 1-indexed inclusive → exclusive slice bound

    # The stored span can be STALE: an earlier in-batch modify shifts the
    # closing boundary (and possibly the opening) without updating the store.
    # The opening line rarely moves (classes are declared near file top), but the
    # `end` almost always does. So whenever we can verify by name, recompute the
    # WHOLE span from the text — brace-matched / indent-scanned — which is robust
    # to any in-batch shift. Fall back to the stored span only when we have no
    # name to search by.
    def _opens_parent(idx: int) -> bool:
        return 0 <= idx < len(lines) and parent_name is not None and parent_name in lines[idx]

    if parent_name is not None:
        span = _find_container_span(lines, parent_name)
        if span is not None:
            start, end = span
        elif not _opens_parent(start):
            return None

    if start < 0 or end > len(lines) or start >= end:
        return None

    # Parent's own indentation, from its opening line.
    opening = lines[start]
    parent_indent = opening[: len(opening) - len(opening.lstrip())]
    member_indent = parent_indent + "    "

    # Re-indent the generated block to member level. The block is generated as a
    # standalone declaration (no indentation); indent each non-blank line.
    reindented = "".join(
        (member_indent + ln if ln.strip() else ln) for ln in block.splitlines(keepends=True)
    )
    if not reindented.endswith("\n"):
        reindented += "\n"

    last_line = lines[end - 1]
    if last_line.lstrip().startswith("}"):
        # Brace language: insert before the closing brace line.
        head = "".join(lines[: end - 1])
        tail = "".join(lines[end - 1 :])
        sep = "" if head.endswith("\n\n") else ("\n" if head.endswith("\n") else "\n\n")
        return head + sep + reindented + tail
    # Indentation language (Python): append after the parent's body.
    head = "".join(lines[:end])
    tail = "".join(lines[end:])
    return head.rstrip("\n") + "\n\n" + reindented + ("\n" + tail if tail else "\n")


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
                fixed = _file_fixup(
                    client, fp, content, diags, max_tokens=config.edits.max_output_tokens
                )
                if fixed is None or not _compile_check(fixed, fp):
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
    session_note: str = "",
) -> ApplyReport:
    """Write the validated staged set to disk atomically; refresh + drop patches.

    all_or_nothing (default): any prior unresolved → write nothing.
    per_item: write each file's changes independently; failures stay unresolved.

    session_note: the unifying intent string for this commit, archived alongside
    the applied-patch records in the session log.
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

    # Build archive entries from patch notes BEFORE any file writes, because the
    # re-scan inside the try block cascades patch rows away.
    create_rows_by_qname: dict[str, list[dict]] = {}
    for rows in store.get_create_patches_grouped().values():
        for row in rows:
            create_rows_by_qname.setdefault(row["target_qname"], []).append(row)

    archive_entries: list[dict] = []
    for ch in staged:
        if ch.op == "create":
            rows = create_rows_by_qname.get(ch.qname, [])
        else:
            rows = store.get_patches_for_qname(ch.qname)
        if not rows:
            # Cascade-expanded callers have no patch rows of their own; skip.
            continue
        session_id = next((r["session_id"] for r in rows if r.get("session_id")), "")
        archive_entries.append(
            {
                "session_id": session_id,
                "session_note": session_note,
                "qname": ch.qname,
                "op": ch.op,
                "file_path": ch.file_path,
                "notes": [r["note"] for r in rows if r.get("note")],
                "reasons": [r["reason"] for r in rows if r.get("reason")],
            }
        )

    written: list[tuple[str, str]] = []  # (file_path, before_bytes) for rollback
    created_files: list[str] = []  # files that did NOT exist before → unlink on rollback
    try:
        # Write source first; the source tree (git-backed) is the unit we roll back.
        for file_path, changes in by_file.items():
            full_path = src_root / file_path
            before = changes[0].before_file_bytes
            after = changes[0].after_file_bytes
            if not full_path.exists():
                # True new-file creation: ensure parent dirs exist and remember to
                # unlink (not restore) this path if the commit later rolls back.
                full_path.parent.mkdir(parents=True, exist_ok=True)
                created_files.append(file_path)
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
        # Files that did not exist before are unlinked rather than restored.
        new_set = set(created_files)
        for file_path, before in written:
            target = src_root / file_path
            if file_path in new_set:
                target.unlink(missing_ok=True)
            else:
                target.write_text(before)
        report.ok = False
        report.committed = False
        report.error = f"commit failed, rolled back: {exc}"
        return report

    seen_deps: set[str] = set()
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
        # Post-apply agent actions: dedup deps across the batch (first-seen order),
        # collect module-level remarks the splice couldn't apply. format_files is
        # derived from applied files in to_dict().
        for dep in ch.new_dependencies:
            if dep not in seen_deps:
                seen_deps.add(dep)
                report.new_dependencies.append(dep)
        if ch.module_remarks.strip():
            report.module_remarks.append(
                ModuleRemark(
                    qname=ch.qname, file_path=ch.file_path, remarks=ch.module_remarks.strip()
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

    # Archive applied patch notes to the session log (advisory; never fail a commit).
    with contextlib.suppress(Exception):
        record_applied(project_root, archive_entries)

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
    return commit(
        store,
        config,
        project_root,
        report,
        staged,
        commit_mode=commit_mode,
        session_note=session_note,
    )


def record_intent(
    store: Store,
    config: Config,
    project_root: Path,
    *,
    session_note: str = "",
) -> dict:
    """Commit pending patch notes as intent — no code generation.

    The record backend treats the patch pipeline as an intent store: agents
    edit source natively, notes describe why, and apply archives them to the
    session log (feeding the digest archive and the intent gate) then clears
    the queue. trie never generates code on this path.

    Same session-note contract as the generating backends: more than one
    symbol requires a unifying `session_note`.
    """
    import time

    from trie.session_log import record_applied

    modify_qnames = store.get_patched_qnames()
    creates_by_file = store.get_create_patches_grouped()
    create_count = sum(len(rows) for rows in creates_by_file.values())
    total = len(modify_qnames) + create_count

    if total == 0:
        return {"ok": True, "mode": "record", "recorded": 0, "symbols": []}
    if total > 1 and not session_note.strip():
        return {
            "ok": False,
            "mode": "record",
            "error": "session_note_required",
            "message": "A session_note is required when recording more than one symbol.",
        }

    now = time.time()
    rows: list[dict] = []
    for qname in modify_qnames:
        patches = store.get_patches_for_qname(qname)
        if not patches:
            continue
        # Structural kinds keep their op; plain notes are modifies.
        kind = next(
            (p.get("kind") for p in patches if p.get("kind") in ("delete", "rename")),
            "modify",
        )
        session_id = next((p.get("session_id") for p in patches if p.get("session_id")), "")
        rows.append(
            {
                "qname": qname,
                "op": kind,
                "notes": [p.get("note", "") for p in patches if p.get("note")],
                "reasons": [p.get("reason", "") for p in patches if p.get("reason")],
                "session_id": session_id,
                "session_note": session_note,
                "ts": now,
            }
        )
    for _file, creates in creates_by_file.items():
        for c in creates:
            rows.append(
                {
                    "qname": c.get("target_qname", ""),
                    "op": "create",
                    "notes": [c.get("note", "")] if c.get("note") else [],
                    "reasons": [c.get("reason", "")] if c.get("reason") else [],
                    "session_id": c.get("session_id", ""),
                    "session_note": session_note,
                    "ts": now,
                }
            )

    record_applied(project_root, rows)
    store.delete_patches(all=True)
    store.delete_create_patches(all=True)

    return {
        "ok": True,
        "mode": "record",
        "recorded": len(rows),
        "symbols": [r["qname"] for r in rows],
        "session_note": session_note,
        "next": (
            "Intent recorded to the session log. The pre-commit digest will carry it; "
            "no code was generated — source changes are yours."
        ),
    }
