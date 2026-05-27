from __future__ import annotations

import contextlib
import time
import uuid
from collections import deque
from pathlib import Path
from typing import Any

from trie.config import Config
from trie.graph.store import Store
from trie.models import ModelClient
from trie.parse.python import extract_symbols
from trie.scan import file_fingerprint
from trie.sync.cascade import compute_cascade
from trie.sync.writer import TriefactFile

from .infer import infer_source_and_prose, merge_notes


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


def _build_working_set(
    patched_qnames: list[str],
    store: Store,
    cascade_depth: int,
    hub_threshold: int,
) -> set[str]:
    seeded_files = _get_file_paths_for_qnames(patched_qnames, store)
    if not seeded_files:
        return set(patched_qnames)

    result = compute_cascade(
        changed_files=seeded_files,
        store=store,
        depth=cascade_depth,
        hub_threshold=hub_threshold,
    )
    working = set(patched_qnames) | result.cascaded_qnames
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
    # Map qname -> scc_index
    qname_to_scc: dict[str, int] = {}
    for idx, scc in enumerate(sccs):
        for qn in scc:
            qname_to_scc[qn] = idx

    # Build super-node DAG: edge from callee super-node to caller super-node
    super_in_degree: list[int] = [0] * len(sccs)
    super_adj: list[set[int]] = [set() for _ in range(len(sccs))]
    for v, callees in graph.items():
        v_scc = qname_to_scc[v]
        for c in callees:
            c_scc = qname_to_scc[c]
            if v_scc != c_scc and v_scc not in super_adj[c_scc]:
                # v calls c, so c is callee -> edge from c_scc to v_scc
                super_adj[c_scc].add(v_scc)
                super_in_degree[v_scc] += 1

    # Kahn's on super-nodes
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
    # Preserve trailing newline if the original file had one
    if original.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    full_path.write_text(result)


def _read_prose(
    qname: str,
    file_path: str,
    triefacts_root: Path,
) -> str:
    """Read the triefact prose body for a symbol. Returns '' if not found."""
    rel_md = Path(file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md
    if not triefact_path.exists():
        return ""
    text = triefact_path.read_text()
    tf = TriefactFile.parse(text)
    section = tf.get_section(qname)
    if section is None:
        return ""
    return section.body


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

    # Compute source_ref from current file content
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


def _process_symbol(
    qname: str,
    patches: list[dict],
    store: Store,
    client: ModelClient,
    src_root: Path,
    triefacts_root: Path,
    now: int,
) -> bool:
    """Process one symbol: merge notes, infer source+prose, validate, write."""
    detail = store.get_symbol_detail(qname)
    if detail is None:
        return False

    merged_notes, merged_reasons = merge_notes(client, patches)
    if not merged_notes:
        return True

    old_source = _source_span(detail.file_path, detail.start_line, detail.end_line, src_root)
    old_prose = _read_prose(qname, detail.file_path, triefacts_root)

    try:
        new_source, new_prose = infer_source_and_prose(
            client, old_source, old_prose, merged_notes, merged_reasons
        )
    except ValueError:
        return False

    if not _compile_check(new_source):
        return False

    # Write the new source to disk
    _write_source_span(detail.file_path, detail.start_line, detail.end_line, new_source, src_root)

    # Re-parse to get the body-normalized hash for the section fingerprint
    file_path_obj = src_root / detail.file_path
    try:
        text = file_path_obj.read_text()
        symbols = extract_symbols(file_path_obj, src_root, source_text=text)
    except Exception:
        return False

    # Use the actual body hash as the section fingerprint so staleness checks work
    sym = next((s for s in symbols if s.qualified_name == qname), None)
    section_fp = sym.body_normalized_hash if sym else ("patch-" + str(now))

    _write_prose(qname, detail.file_path, new_prose, section_fp, triefacts_root, src_root)

    try:
        store.replace_file_symbols(detail.file_path, symbols)
        fp = file_fingerprint(text)
        store.upsert_file(path=detail.file_path, fingerprint=fp)
    except Exception:
        return False

    # Update the triefact frontmatter file_fingerprint to match new source
    rel_md = Path(detail.file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md
    try:
        tf_text = triefact_path.read_text()
        tf = TriefactFile.parse(tf_text)
        tf.front_matter["file_fingerprint"] = fp
        triefact_path.write_text(tf.render() + "\n")
    except Exception:
        return False

    return True


def _process_cascaded(
    qname: str,
    callee_notes: list[tuple[str, str]],
    store: Store,
    client: ModelClient,
    src_root: Path,
    triefacts_root: Path,
) -> bool:
    """Process a cascaded (unpatched) neighbour with callee context."""
    detail = store.get_symbol_detail(qname)
    if detail is None:
        return True

    notes = [n for n, _ in callee_notes]
    reasons = [r for _, r in callee_notes]

    old_source = _source_span(detail.file_path, detail.start_line, detail.end_line, src_root)
    old_prose = _read_prose(qname, detail.file_path, triefacts_root)

    try:
        new_source, new_prose = infer_source_and_prose(
            client, old_source, old_prose, notes, reasons
        )
    except ValueError:
        return False

    if not _compile_check(new_source):
        return False

    if new_source == old_source and new_prose.strip() == old_prose.strip():
        return True

    _write_source_span(detail.file_path, detail.start_line, detail.end_line, new_source, src_root)

    # Re-parse to get the body-normalized hash for section fingerprint
    file_path_obj = src_root / detail.file_path
    try:
        text = file_path_obj.read_text()
        symbols = extract_symbols(file_path_obj, src_root, source_text=text)
    except Exception:
        return False

    sym = next((s for s in symbols if s.qualified_name == qname), None)
    section_fp = sym.body_normalized_hash if sym else ("cascade-" + str(int(time.time())))

    _write_prose(
        qname,
        detail.file_path,
        new_prose,
        section_fp,
        triefacts_root,
        src_root,
    )

    try:
        store.replace_file_symbols(detail.file_path, symbols)
        fp = file_fingerprint(text)
        store.upsert_file(path=detail.file_path, fingerprint=fp)
    except Exception:
        return False

    # Update the triefact frontmatter file_fingerprint to match new source
    rel_md = Path(detail.file_path).with_suffix(".md")
    triefact_path = triefacts_root / rel_md
    try:
        tf_text = triefact_path.read_text()
        tf = TriefactFile.parse(tf_text)
        tf.front_matter["file_fingerprint"] = fp
        triefact_path.write_text(tf.render() + "\n")
    except Exception:
        return False

    return True


def apply_patches(
    store: Store,
    config: Config,
    client: ModelClient,
    project_root: Path,
) -> dict[str, Any]:
    """Apply all pending patches.

    Returns a dict with keys: ok (bool), applied (int), failed (int),
    skipped (int), error (str|None).
    """
    src_root: Path = (project_root / config.triefacts.source_root).resolve()
    triefacts_root: Path = (project_root / config.triefacts.root).resolve()
    cascade_depth = config.cascade.default_depth
    hub_threshold = config.cascade.hub_symbol_threshold
    session_id = uuid.uuid4().hex[:12]
    now = int(time.time())

    # 1. Read all patches grouped by symbol_id
    grouped = store.get_all_patches_grouped()
    if not grouped:
        return {"ok": True, "applied": 0, "failed": 0, "skipped": 0, "error": None}

    # Resolve symbol_ids to qnames and merge notes
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

    # 2. Compute cascade working set
    working_qnames = _build_working_set(patched_qnames, store, cascade_depth, hub_threshold)
    cascaded_qnames = working_qnames - set(patched_qnames)

    # 3. Build dependency subgraph
    graph = _build_dependency_subgraph(working_qnames, store)

    # 4. SCC contraction + topological sort
    sccs = tarjan_scc(graph)
    ordered = topo_sort_sccs(graph, sccs)

    # 5. Git stash
    import subprocess

    stash_msg = f"trie-patch-apply-{session_id}"
    subprocess.run(
        ["git", "stash", "push", "-m", stash_msg],
        cwd=project_root,
        capture_output=True,
        check=False,
    )

    applied = 0
    failed: list[str] = []
    skipped = 0
    processed_qnames: set[str] = set()

    try:
        for scc in ordered:
            for qname in scc:
                if qname in patched_qnames:
                    ok = _process_symbol(
                        qname,
                        patches_by_qname[qname],
                        store,
                        client,
                        src_root,
                        triefacts_root,
                        now,
                    )
                    if ok:
                        applied += 1
                elif qname in cascaded_qnames:
                    callee_notes: list[tuple[str, str]] = []
                    for callee in graph.get(qname, set()):
                        if callee in patches_by_qname:
                            cnotes, creasons = merge_notes(client, patches_by_qname[callee])
                            callee_notes.extend(zip(cnotes, creasons, strict=False))
                    if callee_notes:
                        ok = _process_cascaded(
                            qname,
                            callee_notes,
                            store,
                            client,
                            src_root,
                            triefacts_root,
                        )
                        if ok:
                            applied += 1
                    else:
                        ok = True
                        skipped += 1
                else:
                    ok = True
                    skipped += 1

                if ok:
                    processed_qnames.add(qname)
                else:
                    failed.append(qname)

            # If any symbol in the SCC failed, abort
            if failed:
                break

        if not failed:
            # Delete applied patches from DB
            for qname in patched_qnames:
                if qname in processed_qnames:
                    store.delete_patches(qname=qname)

            # Run trie verify
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
                    ["git", "commit", "-m", f"feat(edits): batch apply {applied} patches"],
                    cwd=project_root,
                    capture_output=True,
                    check=False,
                )
            else:
                # Rollback
                subprocess.run(
                    ["git", "stash", "pop"],
                    cwd=project_root,
                    capture_output=True,
                    check=False,
                )
                return {
                    "ok": False,
                    "applied": applied - len(failed),
                    "failed": len(failed),
                    "skipped": skipped,
                    "error": f"trie verify failed after applying {applied} symbols",
                }
        else:
            subprocess.run(
                ["git", "stash", "pop"],
                cwd=project_root,
                capture_output=True,
                check=False,
            )

    except Exception as exc:
        subprocess.run(
            ["git", "stash", "pop"],
            cwd=project_root,
            capture_output=True,
            check=False,
        )
        return {
            "ok": False,
            "applied": applied,
            "failed": len(failed) or 1,
            "skipped": skipped,
            "error": str(exc),
        }

    return {
        "ok": not failed,
        "applied": applied,
        "failed": len(failed),
        "skipped": skipped,
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

    # Compute cascade
    working_qnames = _build_working_set(
        patched_qnames,
        store,
        config.cascade.default_depth,
        config.cascade.hub_symbol_threshold,
    )
    cascaded = working_qnames - set(patched_qnames)

    return {
        "total_patches": sum(len(v) for v in patches_by_qname.values()),
        "patched_symbols": len(patched_qnames),
        "patched_list": sorted(patched_qnames),
        "cascade_symbols": len(cascaded),
        "cascade_list": sorted(cascaded),
    }
