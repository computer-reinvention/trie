from __future__ import annotations

import contextlib
import json
import subprocess
import time
import uuid
from collections import deque
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from pathlib import Path
from typing import Any

from trie.config import Config, LspBackend
from trie.graph.store import Store
from trie.models import ModelClient
from trie.parse.python import extract_symbols
from trie.scan import file_fingerprint
from trie.sync.writer import TriefactFile

from .infer import (
    INFER_SYSTEM_PROMPT,
    _build_caller_summaries,
    _read_prose,
    infer_source_and_prose,
    merge_notes,
    pre_filter_batch,
)

FIXUP_PROMPT_INLINE = """\
The following source code was generated for symbol {qname} but has
diagnostics errors. Fix the errors and return corrected source + prose.

```python
{source}
```

Diagnostics:
{diagnostics}

Fix each issue. Preserve the existing structure. Output:

```python
<fixed source>
```

---PROSE---
<updated prose>"""


def _parse_pyright_output(stdout: str) -> list[dict]:
    """Parse pyright --outputjson stdout into our normalised diagnostic format.

    Returns list of {line, column, code, message} dicts.
    """
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
    """Parse ruff --output-format json into our normalised diagnostic format.

    Returns list of {line, column, code, message} dicts.
    """
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
    """Run the first available LSP backend on a file and return diagnostics.

    Iterates the backend list in order. For each backend that resolves
    via shutil.which, runs it with `check_args + [file_path]`, parses
    stdout according to `output_format`, and returns diagnostics on
    first non-empty result. Returns empty list if no backend is available
    or all return clean.
    """
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
    """Format LSP diagnostics into a readable multi-line string."""
    lines: list[str] = []
    for d in diags:
        line = d.get("line", "?")
        col = d.get("column", "?")
        code = d.get("code", "?")
        msg = d.get("message", "")
        lines.append(f"  {line}:{col}  {code}  {msg}")
    return "\n".join(lines)


def _fixup_source(
    client: ModelClient,
    qname: str,
    source: str,
    prose: str,
    diagnostics: list[dict],
) -> tuple[str, str] | None:
    """Feed diagnostics back to the LLM for a fixup pass.

    Returns (new_source, new_prose) or None on failure.
    """
    from trie.models import GenerationRequest

    diag_text = _format_diagnostics(diagnostics)
    if not diag_text.strip():
        return (source, prose)

    request = FIXUP_PROMPT_INLINE.format(
        qname=qname,
        source=source,
        diagnostics=diag_text,
    )

    req = GenerationRequest(
        system_prompt=INFER_SYSTEM_PROMPT,
        cached_context="",
        request=request,
        max_tokens=2048,
    )

    resp = client.generate(req)
    text = resp.text.strip()

    delimiter = "---PROSE---"
    if delimiter not in text:
        return None

    before, after = text.split(delimiter, 1)

    new_source = before.strip()
    if new_source.startswith("```python"):
        new_source = new_source[len("```python") :].strip()
    if new_source.startswith("```"):
        new_source = new_source[3:].strip()
    if new_source.endswith("```"):
        new_source = new_source[:-3].strip()

    new_prose = after.strip()
    if new_prose.startswith("```"):
        new_prose = new_prose[3:].strip()
    if new_prose.endswith("```"):
        new_prose = new_prose[:-3].strip()

    return (new_source, new_prose)


def _get_file_paths_for_qnames(
    qnames: list[str],
    store: Store,
) -> list[str]:
    """Resolve a list of qnames to their defining file paths."""
    files: set[str] = set()
    for qname in qnames:
        detail = store.get_symbol_detail(qname)
        if detail is not None:
            files.add(detail.file_path)
    return sorted(files)


def _expand_callers(
    seed_qnames: list[str],
    store: Store,
    cascade_depth: int,
    hub_threshold: int,
) -> set[str]:
    """BFS from seed symbols through caller edges within `cascade_depth`.

    Returns the set of reachable caller qnames (does NOT include seeds).
    Stops expanding through symbols with inbound > hub_threshold.
    """
    working: set[str] = set()
    frontier: list[str] = list(seed_qnames)
    visited: set[str] = set(seed_qnames)

    for _ in range(cascade_depth):
        next_frontier: list[str] = []
        for qn in frontier:
            # Hub guard — don't expand through hubs
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


def _build_dependency_subgraph(
    qnames: set[str],
    store: Store,
) -> dict[str, set[str]]:
    """Build caller->callee adjacency for the given qname set."""
    adj: dict[str, set[str]] = {}
    for qname in qnames:
        callees = store.references_out(qname)
        filtered = {c for c in callees if c in qnames}
        if filtered:
            adj[qname] = filtered
        else:
            adj[qname] = set()
    return adj


def tarjan_scc(graph: dict[str, set[str]]) -> list[set[str]]:
    """Iterative Tarjan's SCC. Returns list of SCCs (each is a set of qnames)."""
    index_counter = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    result: list[set[str]] = []

    def strongconnect(start: str) -> None:
        nonlocal index_counter
        work: list[tuple[str, int, bool]] = [(start, 0, False)]
        while work:
            v, _i, processed = work.pop()
            if not processed:
                if v in indices:
                    continue
                indices[v] = index_counter
                lowlink[v] = index_counter
                index_counter += 1
                stack.append(v)
                on_stack.add(v)

                if graph.get(v):
                    work.append((v, 0, True))
                    for w in list(graph[v]):
                        if w not in indices:
                            work.append((w, 0, False))
                        elif w in on_stack:
                            lowlink[v] = min(lowlink[v], indices[w])
                else:
                    if lowlink[v] == indices[v]:
                        scc: set[str] = set()
                        while True:
                            w = stack.pop()
                            on_stack.discard(w)
                            scc.add(w)
                            if w == v:
                                break
                        result.append(scc)
            else:
                if graph.get(v):
                    for w in list(graph[v]):
                        if w in on_stack:
                            lowlink[v] = min(lowlink[v], lowlink[w])
                if lowlink[v] == indices[v]:
                    scc = set()
                    while True:
                        w = stack.pop()
                        on_stack.discard(w)
                        scc.add(w)
                        if w == v:
                            break
                    result.append(scc)

    for node in graph:
        if node not in indices:
            strongconnect(node)

    return result


def topo_sort_sccs(
    graph: dict[str, set[str]],
    sccs: list[set[str]],
) -> list[set[str]]:
    """Topological sort of SCC super-nodes: callee before caller.

    Builds a DAG of super-nodes from the SCCs, then runs Kahn's algorithm
    on the reversed edges (callee -> caller) so callees sort first.
    """
    qname_to_scc: dict[str, int] = {}
    for idx, scc in enumerate(sccs):
        for qn in scc:
            qname_to_scc[qn] = idx

    super_in_degree: list[int] = [0] * len(sccs)
    super_adj: list[set[int]] = [set() for _ in range(len(sccs))]
    for v, callees in graph.items():
        v_scc = qname_to_scc[v]
        for c in callees:
            c_scc = qname_to_scc[c]
            if v_scc != c_scc and v_scc not in super_adj[c_scc]:
                super_adj[c_scc].add(v_scc)
                super_in_degree[v_scc] += 1

    queue: deque[int] = deque(i for i in range(len(sccs)) if super_in_degree[i] == 0)
    ordered: list[int] = []
    while queue:
        idx = queue.popleft()
        ordered.append(idx)
        for neighbour in super_adj[idx]:
            super_in_degree[neighbour] -= 1
            if super_in_degree[neighbour] == 0:
                queue.append(neighbour)

    return [sccs[i] for i in ordered]


def _source_span(
    file_path: str,
    start_line: int,
    end_line: int,
    src_root: Path,
) -> str:
    """Read the source span for a symbol from disk."""
    full_path = src_root / file_path
    lines = full_path.read_text().splitlines(keepends=True)
    return "".join(lines[start_line - 1 : end_line])


def _write_source_span(
    file_path: str,
    start_line: int,
    end_line: int,
    new_source: str,
    src_root: Path,
) -> None:
    """Replace the source span for a symbol on disk."""
    full_path = src_root / file_path
    original = full_path.read_text()
    lines = original.splitlines(keepends=True)
    before = lines[: start_line - 1]
    after = lines[end_line:]
    result = "".join([*before, new_source, *after])
    if original.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    full_path.write_text(result)


def _write_prose(
    qname: str,
    file_path: str,
    new_prose: str,
    section_fingerprint: str,
    triefacts_root: Path,
    src_root: Path,
) -> str:
    """Update the triefact prose for a symbol. Returns the new section fingerprint."""
    rel_md = Path(file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md

    full_source_path = src_root / file_path
    from trie.git_helpers import compute_blob_hash

    source_ref = compute_blob_hash(full_source_path) or ""

    text = triefact_path.read_text() if triefact_path.exists() else ""
    tf = TriefactFile.parse(text) if text else TriefactFile.empty()

    tf.upsert_section(
        qualified_name=qname,
        fingerprint=section_fingerprint,
        body=new_prose,
        source_ref=source_ref,
    )
    with contextlib.suppress(TypeError, ValueError):
        tf.sort_sections({})
    triefact_path.write_text(tf.render() + "\n")
    return source_ref


def _compile_check(source: str) -> bool:
    """Return True if `source` compiles as valid Python."""
    try:
        compile(source, "<trie-patch>", "exec")
        return True
    except SyntaxError:
        return False


def _process_one(
    qname: str,
    store_path: Path,
    client: ModelClient,
    src_root: Path,
    triefacts_root: Path,
    lsp_max_retries: int = 3,
    lsp_backends: list[LspBackend] | None = None,
) -> tuple[bool, bool]:
    """Process one symbol: merge notes → generate source+prose → write.

    After initial generation, runs LSP diagnostics (ruff check) on the
    written file and feeds errors back to the LLM for up to
    `lsp_max_retries` fixup iterations. Cascade notes are already posted
    to the store by the upfront batch pre-filter, so this just merges
    all patches (agent + cascade) and regenerates.

    Opens a dedicated Store per call (thread-safe). Returns (ok, changed).
    """
    store = Store(store_path)
    try:
        detail = store.get_symbol_detail(qname)
        if detail is None:
            return (True, False)

        patches = store.get_patches_for_qname(qname)
        if not patches:
            return (True, False)

        old_source = _source_span(detail.file_path, detail.start_line, detail.end_line, src_root)
        old_prose = _read_prose(qname, detail.file_path, triefacts_root)

        merged_notes, merged_reasons = merge_notes(client, patches)
        if not merged_notes:
            return (True, False)

        # Initial generation
        try:
            source, prose = infer_source_and_prose(
                client, old_source, old_prose, merged_notes, merged_reasons
            )
        except ValueError:
            return (False, False)

        if not _compile_check(source):
            return (False, False)

        # Write initial source to disk (needed for LSP diagnostics)
        _write_source_span(detail.file_path, detail.start_line, detail.end_line, source, src_root)
        full_path = src_root / detail.file_path

        # LSP fixup loop
        for _ in range(lsp_max_retries):
            diags = _lsp_diagnostics(full_path, lsp_backends or [])
            if not diags:
                break
            fixed = _fixup_source(client, qname, source, prose, diags)
            if fixed is None:
                break
            source, prose = fixed
            if not _compile_check(source):
                return (False, False)
            _write_source_span(
                detail.file_path, detail.start_line, detail.end_line, source, src_root
            )

        # Re-parse to get body hash for section fingerprint
        try:
            text = full_path.read_text()
            symbols = extract_symbols(full_path, src_root, source_text=text)
        except Exception:
            return (False, False)

        sym = next((s for s in symbols if s.qualified_name == qname), None)
        now_int = int(time.time())
        section_fp = sym.body_normalized_hash if sym else ("patch-" + str(now_int))

        _write_prose(qname, detail.file_path, prose, section_fp, triefacts_root, src_root)

        try:
            store.replace_file_symbols(detail.file_path, symbols)
            fp = file_fingerprint(text)
            store.upsert_file(path=detail.file_path, fingerprint=fp)
        except Exception:
            return (False, False)

        # Update triefact frontmatter
        rel_md = Path(detail.file_path).with_suffix(".md")
        triefact_path = triefacts_root / rel_md
        try:
            tf_text = triefact_path.read_text()
            tf = TriefactFile.parse(tf_text)
            tf.front_matter["file_fingerprint"] = fp
            triefact_path.write_text(tf.render() + "\n")
        except Exception:
            return (False, False)

        return (True, True)
    finally:
        store.close()


def apply_patches(
    store: Store,
    config: Config,
    client: ModelClient,
    project_root: Path,
) -> dict[str, Any]:
    """Apply all pending patches with upfront batch cascade expansion.

    Before any symbol is processed, the full cascade DAG is expanded
    statically (call-graph BFS, no LLMs). Then a single batch pre-filter
    call (or batch_size calls) judges all callee→caller relationships,
    and cascade notes are posted to the store. All symbols are then
    processed in a dependency-aware parallel scheduler — the cascade
    notes are consumed alongside agent patches in the same pass.

    Returns a dict with keys: ok (bool), applied (int), failed (int),
    error (str|None).
    """
    src_root: Path = (project_root / config.triefacts.source_root).resolve()
    triefacts_root: Path = (project_root / config.triefacts.root).resolve()
    session_id = uuid.uuid4().hex[:12]

    # 1. Read all patches
    grouped = store.get_all_patches_grouped()
    if not grouped:
        return {"ok": True, "applied": 0, "failed": 0, "error": None}

    # Resolve symbol_ids to qnames
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

    # 2. Build working set: seeds + transitive callers within depth
    working = _expand_callers(
        patched_qnames,
        store,
        config.cascade.default_depth,
        config.cascade.hub_symbol_threshold,
    )
    all_qnames: set[str] = set(patched_qnames) | working

    # 3. SCC contraction + topological sort
    graph = _build_dependency_subgraph(all_qnames, store)
    sccs = tarjan_scc(graph)
    scc_order = topo_sort_sccs(graph, sccs)
    flat_order: list[str] = [q for scc in scc_order for q in scc]

    if not flat_order:
        return {"ok": True, "applied": 0, "failed": 0, "error": None}

    # 4. Upfront batch cascade expansion + pre-filter
    # Build callee pairs for every seed symbol that has callers in the working set
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
        patches = patches_by_qname.get(qn, [])
        notes_reasons = [(p["note"], p["reason"]) for p in patches]
        callee_pairs.append((qn, old_prose, callers, notes_reasons))

    if callee_pairs:
        cascade_results = pre_filter_batch(
            client,
            callee_pairs,
            batch_size=8,
        )
        # Post cascade notes to store
        posted_qnames: set[str] = set()
        for caller_qn, note, reason in cascade_results:
            if note is None or reason is None:
                continue
            with contextlib.suppress(KeyError):
                store.add_patch(caller_qn, note, reason, "cascade")
                posted_qnames.add(caller_qn)
        # Expand working set to include cascade targets and re-sort
        if posted_qnames:
            extra_cascade = list(posted_qnames - all_qnames)
            if extra_cascade:
                extra_expanded = _expand_callers(
                    extra_cascade,
                    store,
                    config.cascade.default_depth,
                    config.cascade.hub_symbol_threshold,
                )
                all_qnames |= set(extra_cascade) | extra_expanded
                graph = _build_dependency_subgraph(all_qnames, store)
                sccs = tarjan_scc(graph)
                scc_order = topo_sort_sccs(graph, sccs)
                flat_order = [q for scc in scc_order for q in scc]

    # 5. Git stash
    stash_msg = f"trie-patch-apply-{session_id}"
    subprocess.run(
        ["git", "stash", "push", "-m", stash_msg],
        cwd=project_root,
        capture_output=True,
        check=False,
    )

    def _rollback() -> None:
        subprocess.run(
            ["git", "stash", "pop"],
            cwd=project_root,
            capture_output=True,
            check=False,
        )

    def _success_commit(applied_count: int) -> None:
        verify = subprocess.run(
            ["trie", "verify"],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if verify.returncode == 0:
            subprocess.run(
                ["git", "add", "-A"],
                cwd=project_root,
                capture_output=True,
                check=False,
            )
            subprocess.run(
                ["git", "commit", "-m", f"feat(edits): batch apply {applied_count} patches"],
                cwd=project_root,
                capture_output=True,
                check=False,
            )
        else:
            _rollback()
            raise RuntimeError(f"trie verify failed after applying {applied_count} symbols")

    applied = 0
    failed: list[str] = []
    processed: set[str] = set()

    # 5. Parallel dependency-aware scheduler
    try:
        with ThreadPoolExecutor(max_workers=config.sync.concurrency) as pool:
            pending = set(flat_order)
            futures: dict[Future, str] = {}

            while pending or futures:
                # Submit symbols whose callees are all processed
                ready: list[str] = []
                still_pending: list[str] = []
                for qname in pending:
                    callees = graph.get(qname, set())
                    if all(c in processed for c in callees):
                        ready.append(qname)
                    else:
                        still_pending.append(qname)
                pending = set(still_pending)

                for qname in ready:
                    f = pool.submit(
                        _process_one,
                        qname,
                        store.db_path,
                        client,
                        src_root,
                        triefacts_root,
                        config.edits.lsp_max_retries,
                        config.edits.lsp_backends,
                    )
                    futures[f] = qname

                if not futures:
                    break

                # Wait for first completion
                done, _ = wait(futures, return_when=FIRST_COMPLETED)
                for f in done:
                    f_qname = futures.pop(f)
                    try:
                        ok, changed = f.result()
                    except Exception:
                        failed.append(f_qname)
                        _rollback()
                        return {
                            "ok": False,
                            "applied": applied,
                            "failed": len(failed),
                            "error": f"exception processing {f_qname}",
                        }

                    if not ok:
                        failed.append(f_qname)
                        _rollback()
                        return {
                            "ok": False,
                            "applied": applied,
                            "failed": len(failed),
                            "error": f"failed to process {f_qname}",
                        }

                    if changed:
                        applied += 1

                    # Consume agent patches for this symbol
                    store.delete_patches(qname=f_qname)
                    processed.add(f_qname)

            if not failed:
                _success_commit(applied)
            else:
                _rollback()

    except Exception as exc:
        _rollback()
        return {
            "ok": False,
            "applied": applied,
            "failed": len(failed) or 1,
            "error": str(exc),
        }

    return {
        "ok": not failed,
        "applied": applied,
        "failed": len(failed),
        "error": None,
    }


def preview_patches(store: Store, config: Config) -> dict[str, Any]:
    """Preview what --apply would do. Returns summary data."""
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
