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
from trie.models import ModelClient

from .infer import (
    FILE_FIXUP_PROMPT,
    INFER_SYSTEM_PROMPT,
    _build_caller_summaries,
    _read_prose,
    infer_file_source,
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


_PARSERS = {
    "pyright": _parse_pyright_output,
    "ruff": _parse_ruff_output,
}


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
    client: ModelClient,
    file_path: str,
    file_content: str,
    diagnostics: list[dict],
) -> str | None:
    from trie.models import GenerationRequest

    diag_text = _format_diagnostics(diagnostics)
    if not diag_text.strip():
        return file_content

    request = FILE_FIXUP_PROMPT.format(
        file_path=file_path,
        file_content=file_content,
        diagnostics=diag_text,
    )

    req = GenerationRequest(
        system_prompt=INFER_SYSTEM_PROMPT,
        cached_context="",
        request=request,
        max_tokens=4096,
    )

    resp = client.generate(req)
    text = resp.text.strip()

    if "```python" not in text:
        return None
    _before, after = text.split("```python", 1)
    if "```" not in after:
        return None
    fixed, _rest = after.split("```", 1)
    return fixed.strip()


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
    client: ModelClient,
    project_root: Path,
) -> dict[str, Any]:
    src_root: Path = (project_root / config.triefacts.source_root).resolve()
    triefacts_root: Path = (project_root / config.triefacts.root).resolve()

    grouped = store.get_all_patches_grouped()
    if not grouped:
        return {"ok": True, "applied": 0, "failed": 0, "error": None}

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
        return {"ok": True, "applied": 0, "failed": 0, "error": None}

    patched_qnames = list(patches_by_qname.keys())

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
        cascade_results = pre_filter_batch(client, callee_pairs, batch_size=8)
        for caller_qn, note, reason in cascade_results:
            if note is None or reason is None:
                continue
            with contextlib.suppress(KeyError):
                store.add_patch(caller_qn, note, reason, "cascade")
                if caller_qn not in qname_to_file:
                    detail = store.get_symbol_detail(caller_qn)
                    if detail is not None:
                        qname_to_file[caller_qn] = detail.file_path
                        file_to_qnames.setdefault(detail.file_path, []).append(caller_qn)

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
        return {"ok": True, "applied": 0, "failed": 0, "error": None}

    changed_files: list[str] = []
    failed: list[str] = []

    def _process_one_file(file_path: str, symbols: list[dict]) -> bool:
        full_path = src_root / file_path
        try:
            file_content = full_path.read_text()
        except FileNotFoundError:
            failed.append(file_path)
            return False

        symbols_data_for_llm: list[dict] = []
        for sd in symbols:
            qn = sd["qname"]
            old_source = _read_source_span(sd["detail"], src_root)
            old_prose = _read_prose(qn, file_path, triefacts_root)
            symbols_data_for_llm.append(
                {
                    "qname": qn,
                    "old_source": old_source,
                    "old_prose": old_prose,
                    "merged_notes": sd["merged_notes"],
                    "merged_reasons": sd["merged_reasons"],
                }
            )

        try:
            new_content, proses = infer_file_source(
                client, file_path, file_content, symbols_data_for_llm
            )
        except (ValueError, Exception):
            failed.append(file_path)
            return False

        if not _compile_check(new_content):
            failed.append(file_path)
            return False

        if not new_content.endswith("\n"):
            new_content += "\n"
        full_path.write_text(new_content)

        for _ in range(config.edits.lsp_max_retries):
            diags = _lsp_diagnostics(full_path, config.edits.lsp_backends)
            if not diags:
                break
            fixed = _file_fixup(client, file_path, new_content, diags)
            if fixed is None:
                break
            if not _compile_check(fixed):
                failed.append(file_path)
                return False
            if not fixed.endswith("\n"):
                fixed += "\n"
            full_path.write_text(fixed)
            new_content = fixed

        for sd in symbols:
            qn = sd["qname"]
            prose = proses.get(qn, "")
            if prose:
                _write_prose_section(qn, file_path, prose, triefacts_root)

        changed_files.append(file_path)
        return True

    try:
        with ThreadPoolExecutor(max_workers=config.sync.concurrency) as pool:
            futures_map: dict[Any, str] = {}
            for fp, symbols in file_groups.items():
                f = pool.submit(_process_one_file, fp, symbols)
                futures_map[f] = fp

            for f in futures_map:
                fp = futures_map[f]
                try:
                    f.result()
                except Exception:
                    failed.append(fp)

    except Exception as exc:
        return {"ok": False, "applied": 0, "failed": len(failed) or 1, "error": str(exc)}

    if failed:
        return {
            "ok": False,
            "applied": len(changed_files),
            "failed": len(failed),
            "error": f"failed to process: {', '.join(failed)}",
        }

    for fp in changed_files:
        try:
            _refresh_file(fp, project_root, config, store)
        except Exception as exc:
            return {
                "ok": False,
                "applied": len(changed_files),
                "failed": 0,
                "error": f"refresh failed for {fp}: {exc}",
            }

    result = check_project(project_root=project_root, config=config)
    if not result.is_clean:
        stale = [f"{i.source_path}: {i.reason.value}" for i in result.items]
        return {
            "ok": False,
            "applied": len(changed_files),
            "failed": 1,
            "error": f"verify failed: {', '.join(stale[:5])}",
        }

    for qn in all_qnames:
        store.delete_patches(qname=qn)

    return {"ok": True, "applied": len(changed_files), "failed": 0, "error": None}


def _read_source_span(detail: Any, src_root: Path) -> str:
    full_path = src_root / detail.file_path
    lines = full_path.read_text().splitlines(keepends=True)
    return "".join(lines[detail.start_line - 1 : detail.end_line])


def _write_prose_section(
    qname: str,
    file_path: str,
    prose: str,
    triefacts_root: Path,
) -> None:
    from trie.sync.writer import TriefactFile

    rel_md = Path(file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md

    text = triefact_path.read_text() if triefact_path.exists() else ""
    tf = TriefactFile.parse(text) if text else TriefactFile.empty()

    tf.upsert_section(
        qualified_name=qname,
        fingerprint="",
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
