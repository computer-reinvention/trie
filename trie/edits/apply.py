from __future__ import annotations

import contextlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from trie.check import check_project
from trie.config import Config, LspBackend
from trie.graph.store import Store
from trie.models import FixupOutput, TrieClient

from .infer import (
    FILE_FIXUP_PROMPT,
    INFER_SYSTEM_PROMPT,
    _build_caller_summaries,
    _read_prose,
    infer_file_source,
    infer_source_and_prose,
    merge_notes,
    pre_filter_batch,
)


def _parse_pyright_output(stdout: str) -> list[dict]:
    try:
        data = json.loads(stdout)
    except (json.JSONDecodeError, ValueError):
        return []
    diags = data.get("generalDiagnostics", [])
    result: list[dict] = []
    for d in diags:
        result.append(
            {
                "line": d.get("line", 0),
                "column": d.get("column", 0),
                "code": d.get("rule", "?") if d.get("rule") != "" else "pyright",
                "message": d.get("message", ""),
            }
        )
    return result


def _parse_ruff_output(stdout: str) -> list[dict]:
    try:
        data = json.loads(stdout)
    except (json.JSONDecodeError, ValueError):
        return []
    if isinstance(data, dict):
        data = [data]
    result: list[dict] = []
    for d in data:
        loc = d.get("location", {})
        result.append(
            {
                "line": loc.get("row", d.get("line", 0)),
                "column": loc.get("column", d.get("col", 0)),
                "code": d.get("code", "ruff"),
                "message": d.get("message", ""),
            }
        )
    return result


def _parse_tsc_output(stdout: str) -> list[dict]:
    """Parse `tsc --noEmit --pretty false` diagnostics.

    Each error line looks like:
        path/to/file.ts(12,5): error TS2322: Type 'x' is not assignable...
    We extract line/column/code/message; the file path is ignored (the checker
    is run per-candidate-file in the scratch tree).
    """
    result: list[dict] = []
    for raw in stdout.splitlines():
        line = raw.strip()
        if "): error TS" not in line and "): warning TS" not in line:
            continue
        try:
            loc_part, rest = line.split("):", 1)
            coords = loc_part.rsplit("(", 1)[1]  # "12,5"
            row_str, col_str = coords.split(",", 1)
            severity_code, message = rest.strip().split(":", 1)
            code = severity_code.split()[-1]  # "TS2322"
            result.append(
                {
                    "line": int(row_str),
                    "column": int(col_str),
                    "code": code,
                    "message": message.strip(),
                }
            )
        except (ValueError, IndexError):
            continue
    return result


_PARSERS = {
    "pyright": _parse_pyright_output,
    "ruff": _parse_ruff_output,
    "tsc": _parse_tsc_output,
}


def lsp_backends_for_file(file_path: Path, config: Config) -> list[LspBackend]:
    """Diagnostic checkers for a file: its language backend's defaults if any,
    else the configured `Edits.lsp_backends` fallback.

    A `[languages]` config override (config.languages[name].lsp_backends) takes
    precedence over the backend's built-in defaults when present.
    """
    from trie.parse import registry

    backend = registry.get_backend_for_file(file_path)
    if backend is not None:
        override = config.languages.get(backend.name)
        if override is not None and override.lsp_backends:
            return override.lsp_backends
        defaults = backend.lsp_backends()
        if defaults:
            return defaults
    return config.edits.lsp_backends


def _lsp_diagnostics(file_path: Path, backends: list[LspBackend]) -> list[dict]:
    import shutil

    for backend in backends:
        cmd = shutil.which(backend.command)
        if cmd is None:
            continue
        try:
            result = subprocess.run(
                [cmd, *backend.check_args, str(file_path)],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            continue
        stdout = result.stdout.strip()
        if not stdout:
            continue
        parser = _PARSERS.get(backend.output_format)
        if parser is None:
            continue
        diags = parser(stdout)
        if diags:
            return diags
    return []


def _format_diagnostics(diags: list[dict]) -> str:
    lines: list[str] = []
    for d in diags:
        line = d.get("line", "?")
        col = d.get("column", "?")
        code = d.get("code", "?")
        msg = d.get("message", "")
        lines.append(f"  {line}:{col}  {code}  {msg}")
    return "\n".join(lines)


def _file_fixup(
    client: TrieClient,
    file_path: str,
    file_content: str,
    diagnostics: list[dict],
) -> str | None:
    diag_text = _format_diagnostics(diagnostics)
    if not diag_text.strip():
        return file_content

    user_prompt = FILE_FIXUP_PROMPT.format(
        file_path=file_path,
        file_content=file_content,
        diagnostics=diag_text,
    )

    result = client.run(
        FixupOutput,
        system_prompt=INFER_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        max_tokens=4096,
    )
    fixup: FixupOutput = result.output
    return fixup.content


def _compile_check(source: str) -> bool:
    try:
        compile(source, "<trie-patch>", "exec")
        return True
    except SyntaxError:
        return False


def _expand_callers(
    seed_qnames: list[str],
    store: Store,
    cascade_depth: int,
    hub_threshold: int,
) -> set[str]:
    working: set[str] = set()
    frontier: list[str] = list(seed_qnames)
    visited: set[str] = set(seed_qnames)

    for _ in range(cascade_depth):
        next_frontier: list[str] = []
        for qn in frontier:
            row = store._conn.execute(
                "SELECT COUNT(*) FROM edges WHERE dst_symbol_id = ("
                "SELECT id FROM symbols WHERE qualified_name = ? LIMIT 1"
                ")",
                (qn,),
            ).fetchone()
            if row and int(row[0]) > hub_threshold:
                continue
            for caller in store.references_in(qn):
                if caller not in visited:
                    visited.add(caller)
                    working.add(caller)
                    next_frontier.append(caller)
        if not next_frontier:
            break
        frontier = next_frontier

    return working


def _refresh_file(
    file_path: str,
    project_root: Path,
    config: Config,
    store: Store,
) -> None:
    from trie.sync.single_file import refresh_triefact_metadata

    source_path = (project_root / config.triefacts.source_root).resolve() / file_path
    refresh_triefact_metadata(source_path, project_root=project_root, config=config, store=store)


def apply_patches(
    store: Store,
    config: Config,
    client: TrieClient,
    project_root: Path,
    progress: Any | None = None,
) -> dict[str, Any]:
    """Apply all pending patches.

    When *progress* is provided, it must have:

        def stage(self, msg: str) -> None
        def file_start(self, fp: str, symbols: int) -> None
        def file_symbol(self, qn: str, notes: list[str]) -> None
        def file_generate(self) -> None
        def file_fixup(self, iteration: int, count: int) -> None
        def file_prose(self, qn: str) -> None
        def file_done(self, fp: str, ok: bool, error: str | None = None) -> None
        def refresh(self, fp: str) -> None
        def verify(self) -> None

    Returns a dict with:

        ok            bool
        total_files   int
        total_symbols int
        files         list[dict]   — one per file with per-symbol detail
        error         str | None
    """
    src_root: Path = (project_root / config.triefacts.source_root).resolve()
    triefacts_root: Path = (project_root / config.triefacts.root).resolve()

    grouped = store.get_all_patches_grouped()
    if not grouped:
        if progress:
            progress.stage("no pending patches — nothing to do")
        return {"ok": True, "total_files": 0, "total_symbols": 0, "files": [], "error": None}

    patches_by_qname: dict[str, list[dict]] = {}
    qname_to_file: dict[str, str] = {}
    file_to_qnames: dict[str, list[str]] = {}

    for sym_id, patch_list in grouped.items():
        row = store._conn.execute(
            "SELECT qualified_name FROM symbols WHERE id = ?", (sym_id,)
        ).fetchone()
        if row is None:
            continue
        qname = str(row[0])
        patches_by_qname[qname] = patch_list
        detail = store.get_symbol_detail(qname)
        if detail is None:
            continue
        qname_to_file[qname] = detail.file_path
        file_to_qnames.setdefault(detail.file_path, []).append(qname)

    if not qname_to_file:
        return {"ok": True, "total_files": 0, "total_symbols": 0, "files": [], "error": None}

    patched_qnames = list(patches_by_qname.keys())

    if progress:
        progress.stage("cascade — expanding caller graph")
    working = _expand_callers(
        patched_qnames,
        store,
        config.cascade.default_depth,
        config.cascade.hub_symbol_threshold,
    )
    all_qnames: set[str] = set(patched_qnames) | working

    callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]] = []
    for qn in patched_qnames:
        callers_raw = store.references_in(qn)
        if not callers_raw:
            continue
        callers = _build_caller_summaries(callers_raw, store, triefacts_root)
        if not callers:
            continue
        detail = store.get_symbol_detail(qn)
        if detail is None:
            continue
        old_prose = _read_prose(qn, detail.file_path, triefacts_root)
        notes_reasons = [(p["note"], p["reason"]) for p in patches_by_qname.get(qn, [])]
        callee_pairs.append((qn, old_prose, callers, notes_reasons))

    if callee_pairs:
        if progress:
            progress.stage("cascade — pre-filtering callee relationships")
        cascade_results = pre_filter_batch(client, callee_pairs, batch_size=8)
        cascade_applied = 0
        for caller_qn, note, reason in cascade_results:
            if note is None or reason is None:
                continue
            with contextlib.suppress(KeyError):
                store.add_patch(caller_qn, note, reason, "cascade")
                cascade_applied += 1
                if caller_qn not in qname_to_file:
                    detail = store.get_symbol_detail(caller_qn)
                    if detail is not None:
                        qname_to_file[caller_qn] = detail.file_path
                        file_to_qnames.setdefault(detail.file_path, []).append(caller_qn)
        if progress:
            progress.stage(
                f"cascade — {cascade_applied} new patches, "
                f"total expanded to {len(all_qnames)} symbols"
            )

    if progress:
        progress.stage("merge — consolidating per-symbol notes")
    file_groups: dict[str, list[dict]] = {}
    for fp, qnames_in_file in file_to_qnames.items():
        symbols_data: list[dict] = []
        for qn in qnames_in_file:
            patches = store.get_patches_for_qname(qn)
            if not patches:
                continue
            detail = store.get_symbol_detail(qn)
            if detail is None:
                continue
            merged_notes_list, merged_reasons_list = merge_notes(client, patches)
            if not merged_notes_list:
                continue
            symbols_data.append(
                {
                    "qname": qn,
                    "merged_notes": merged_notes_list,
                    "merged_reasons": merged_reasons_list,
                    "detail": detail,
                }
            )
        if symbols_data:
            file_groups[fp] = symbols_data

    if not file_groups:
        return {"ok": True, "total_files": 0, "total_symbols": 0, "files": [], "error": None}

    total_symbols_count = sum(len(v) for v in file_groups.values())
    if progress:
        progress.stage(f"source gen — {len(file_groups)} file(s), {total_symbols_count} symbol(s)")

    file_results: list[dict] = []
    failed: list[str] = []

    def _process_one_file(file_path: str, symbols: list[dict]) -> dict | None:
        full_path = src_root / file_path

        if progress:
            progress.file_start(file_path, len(symbols))

        try:
            file_content = full_path.read_text()
        except FileNotFoundError:
            if progress:
                progress.file_done(file_path, False, "file not found")
            return {"path": file_path, "ok": False, "error": "file not found"}

        symbol_details: list[dict] = []
        for sd in symbols:
            qn = sd["qname"]
            notes = sd["merged_notes"]
            if progress:
                progress.file_symbol(qn, notes)
            old_source = _read_source_span(sd["detail"], src_root)
            old_prose = _read_prose(qn, file_path, triefacts_root)
            symbol_details.append(
                {
                    "qname": qn,
                    "detail": sd["detail"],
                    "old_source": old_source,
                    "old_prose": old_prose,
                    "merged_notes": notes,
                    "merged_reasons": sd["merged_reasons"],
                }
            )

        if progress:
            progress.file_generate()

        def _fallback_per_symbol() -> tuple[str, dict[str, str]]:
            lines = file_content.splitlines(keepends=True)
            proses: dict[str, str] = {}
            for sd in symbol_details:
                new_src, new_prose = infer_source_and_prose(
                    client,
                    old_source=sd["old_source"],
                    old_prose=sd["old_prose"],
                    notes=sd["merged_notes"],
                    reasons=sd["merged_reasons"],
                )
                start = sd["detail"].start_line - 1
                end = sd["detail"].end_line
                lines[start:end] = [new_src] if new_src.endswith("\n") else [new_src + "\n"]
                if new_prose:
                    proses[sd["qname"]] = new_prose
            return "".join(lines), proses

        new_content: str = ""
        proses: dict[str, str] = {}
        try:
            new_content, proses = infer_file_source(client, file_path, file_content, symbol_details)
        except (ValueError, Exception):
            new_content, proses = _fallback_per_symbol()

        if not _compile_check(new_content):
            new_content, proses = _fallback_per_symbol()

        if not _compile_check(new_content):
            if progress:
                progress.file_done(file_path, False, "syntax error after generation + fallback")
            return {
                "path": file_path,
                "ok": False,
                "error": "syntax error after generation + fallback",
            }

        if not new_content.endswith("\n"):
            new_content += "\n"
        full_path.write_text(new_content)

        lsp_iterations = 0
        file_lsp_backends = lsp_backends_for_file(full_path, config)
        for i in range(config.edits.lsp_max_retries):
            diags = _lsp_diagnostics(full_path, file_lsp_backends)
            if not diags:
                break
            if progress:
                progress.file_fixup(i + 1, len(diags))
            fixed = _file_fixup(client, file_path, new_content, diags)
            if fixed is None:
                break
            if not _compile_check(fixed):
                if progress:
                    progress.file_done(file_path, False, "syntax error after fixup")
                return {"path": file_path, "ok": False, "error": "syntax error after lsp fixup"}
            if not fixed.endswith("\n"):
                fixed += "\n"
            full_path.write_text(fixed)
            new_content = fixed
            lsp_iterations += 1

        prose_written: list[str] = []
        for sd in symbols:
            qn = sd["qname"]
            prose = proses.get(qn, "")
            if prose:
                if progress:
                    progress.file_prose(qn)
                _write_prose_section(qn, file_path, prose, triefacts_root, src_root)
                prose_written.append(qn)

        result = {
            "path": file_path,
            "ok": True,
            "error": None,
            "symbols": [sd["qname"] for sd in symbols],
            "notes": [sd["merged_notes"] for sd in symbols],
            "lsp_iterations": lsp_iterations,
            "prose_written": prose_written,
        }
        if progress:
            progress.file_done(file_path, True)
        return result

    try:
        with ThreadPoolExecutor(max_workers=config.sync.concurrency) as pool:
            futures_map: dict[Any, str] = {}
            for fp, symbols in file_groups.items():
                f = pool.submit(_process_one_file, fp, symbols)
                futures_map[f] = fp

            for f in futures_map:
                fp = futures_map[f]
                try:
                    res = f.result()
                    if res is not None:
                        file_results.append(res)
                        if not res["ok"]:
                            failed.append(fp)
                except Exception as exc:
                    failed.append(fp)
                    file_results.append({"path": fp, "ok": False, "error": str(exc)})

    except Exception as exc:
        return {
            "ok": False,
            "total_files": len(file_results),
            "total_symbols": total_symbols_count,
            "files": file_results,
            "error": str(exc),
        }

    if failed:
        return {
            "ok": False,
            "total_files": len(file_results),
            "total_symbols": total_symbols_count,
            "files": file_results,
            "error": f"failed files: {', '.join(failed)}",
        }

    if progress:
        progress.stage("refresh — syncing triefact metadata")
    changed_file_paths = [r["path"] for r in file_results if r["ok"]]
    for fp in changed_file_paths:
        if progress:
            progress.refresh(fp)
        try:
            _refresh_file(fp, project_root, config, store)
        except Exception as exc:
            return {
                "ok": False,
                "total_files": len(file_results),
                "total_symbols": total_symbols_count,
                "files": file_results,
                "error": f"refresh failed for {fp}: {exc}",
            }

    # Clear the pending patches for everything that was written + refreshed
    # cleanly, BEFORE the whole-tree verify gate. The patch represents "apply
    # this edit to this symbol"; once the file is written and its triefact
    # refreshed, that intent is fulfilled. The global verify can be dirty for
    # unrelated reasons (other stale files in the tree), and letting it block
    # patch cleanup left applied patches stuck "pending" forever.
    for qn in all_qnames:
        store.delete_patches(qname=qn)

    if progress:
        progress.stage("verify — checking project consistency")
    result = check_project(project_root=project_root, config=config)
    if not result.is_clean:
        stale = [f"{i.source_path}: {i.reason.value}" for i in result.items]
        if progress:
            progress.verify()
        return {
            "ok": False,
            "total_files": len(file_results),
            "total_symbols": total_symbols_count,
            "files": file_results,
            "error": f"verify failed: {', '.join(stale[:5])}",
        }

    if progress:
        progress.stage(
            f"done — {len(changed_file_paths)} file(s), {total_symbols_count} symbol(s) applied"
        )

    return {
        "ok": True,
        "total_files": len(file_results),
        "total_symbols": total_symbols_count,
        "files": file_results,
        "error": None,
    }


def _read_source_span(detail: Any, src_root: Path) -> str:
    full_path = src_root / detail.file_path
    lines = full_path.read_text().splitlines(keepends=True)
    return "".join(lines[detail.start_line - 1 : detail.end_line])


def _write_prose_section(
    qname: str,
    file_path: str,
    prose: str,
    triefacts_root: Path,
    src_root: Path | None = None,
) -> None:
    from trie.sync.writer import TriefactFile

    rel_md = Path(file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md

    text = triefact_path.read_text() if triefact_path.exists() else ""
    tf = TriefactFile.parse(text) if text else TriefactFile.empty()

    # Compute fingerprint from the updated source so verify passes
    fingerprint = ""
    if src_root is not None:
        source_path = src_root / file_path
        if source_path.exists():
            try:
                from trie.parse import registry

                for sym in registry.extract_symbols(source_path, source_root=src_root):
                    if sym.qualified_name == qname:
                        fingerprint = sym.body_normalized_hash
                        break
            except Exception:
                pass

    tf.upsert_section(
        qualified_name=qname,
        fingerprint=fingerprint,
        body=prose,
        source_ref="",
    )
    with contextlib.suppress(TypeError, ValueError):
        tf.sort_sections({})
    triefact_path.write_text(tf.render() + "\n")


def preview_patches(store: Store, config: Config) -> dict[str, Any]:
    grouped = store.get_all_patches_grouped()
    patches_by_qname: dict[str, list[dict]] = {}
    for sym_id, patch_list in grouped.items():
        row = store._conn.execute(
            "SELECT qualified_name FROM symbols WHERE id = ?", (sym_id,)
        ).fetchone()
        if row is None:
            continue
        qname = str(row[0])
        patches_by_qname[qname] = patch_list

    patched_qnames = list(patches_by_qname.keys())

    working = _expand_callers(
        patched_qnames,
        store,
        config.cascade.default_depth,
        config.cascade.hub_symbol_threshold,
    )
    cascaded = sorted(working - set(patched_qnames))

    return {
        "total_patches": sum(len(v) for v in patches_by_qname.values()),
        "patched_symbols": len(patched_qnames),
        "patched_list": sorted(patched_qnames),
        "cascade_symbols": len(cascaded),
        "cascade_list": cascaded,
    }
