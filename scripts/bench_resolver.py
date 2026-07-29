#!/usr/bin/env python
"""Repeatable benchmark: tree-sitter vs tree-sitter + LSP resolver.

Runs reference extraction over a directory twice — once with the resolver
disabled (tree-sitter only) and once enabled — and reports the edge counts,
the method-dispatch edges recovered, and timing. Language-agnostic: it uses
the registry, so it measures whatever backends claim the files it finds.

Usage:
    uv run python scripts/bench_resolver.py <dir> [--ext .py] [--limit N]

Examples:
    uv run python scripts/bench_resolver.py trie
    uv run python scripts/bench_resolver.py path/to/rust/crate --ext .rs
"""

from __future__ import annotations

import argparse
import os
import time
from pathlib import Path

from trie.parse import registry


def _project_qnames(files: list[Path], source_root: Path) -> set[str]:
    qnames: set[str] = set()
    for f in files:
        try:
            for s in registry.extract_symbols(f, source_root=source_root):
                qnames.add(s.qualified_name)
        except Exception:
            pass
    return qnames


def _extract(files: list[Path], source_root: Path, qnames: set[str]):
    """Return (edge_pairs, method_edge_pairs) filtered to project-internal targets."""
    edges: set[tuple[str, str]] = set()
    method_edges: set[tuple[str, str]] = set()
    for f in files:
        try:
            fd = registry.extract_file_data(f, source_root=source_root)
        except Exception:
            continue
        for r in fd.references:
            if r.src_qname in qnames and r.target_qname in qnames:
                edges.add((r.src_qname, r.target_qname))
                local = r.target_qname.split(":", 1)[1]
                if r.kind == "calls" and "." in local:
                    method_edges.add((r.src_qname, r.target_qname))
    return edges, method_edges


def _reset_backend_caches() -> None:
    for b in registry.all_backends():
        if hasattr(b, "_resolver_built"):
            b._resolver_built = False
            b._resolver = None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("directory", help="Directory to benchmark (also the source root).")
    ap.add_argument("--ext", action="append", help="Restrict to these extensions (repeatable).")
    ap.add_argument("--limit", type=int, default=0, help="Cap number of files (0 = all).")
    args = ap.parse_args()

    root = Path(args.directory).resolve()
    exts = tuple(args.ext) if args.ext else None
    files = sorted(
        p
        for p in root.rglob("*")
        if p.is_file() and registry.is_indexable(p) and (exts is None or p.suffix in exts)
    )
    if args.limit:
        files = files[: args.limit]
    if not files:
        print(f"no indexable files under {root}")
        return

    qnames = _project_qnames(files, root)
    print(f"target: {root}")
    print(f"files: {len(files)} · project symbols: {len(qnames)}\n")

    # --- tree-sitter only ---
    os.environ["TRIE_DISABLE_RESOLVER"] = "1"
    _reset_backend_caches()
    t0 = time.perf_counter()
    ts_edges, ts_methods = _extract(files, root, qnames)
    ts_time = time.perf_counter() - t0

    # --- tree-sitter + resolver ---
    os.environ.pop("TRIE_DISABLE_RESOLVER", None)
    _reset_backend_caches()
    t0 = time.perf_counter()
    lsp_edges, lsp_methods = _extract(files, root, qnames)
    lsp_time = time.perf_counter() - t0
    # close any spawned servers
    for b in registry.all_backends():
        r = b.resolver() if hasattr(b, "resolver") else None
        if r is not None and hasattr(r, "close"):
            r.close()

    net_new = lsp_edges - ts_edges
    combined = len(ts_edges | lsp_edges)

    print(f"{'technique':<24}{'edges':>8}{'method-edges':>14}{'time':>10}")
    print("-" * 56)
    print(f"{'tree-sitter only':<24}{len(ts_edges):>8}{len(ts_methods):>14}{ts_time:>9.1f}s")
    print(f"{'tree-sitter + LSP':<24}{len(lsp_edges):>8}{len(lsp_methods):>14}{lsp_time:>9.1f}s")
    print("-" * 56)
    print(f"net-new edges from resolver: {len(net_new)}")
    if ts_edges:
        print(f"edge lift: +{len(net_new) / len(ts_edges) * 100:.0f}%")
    if combined:
        print(f"tree-sitter recall vs combined: {len(ts_edges) / combined * 100:.0f}%")
    print("\nsample recovered method edges:")
    for s, d in sorted(net_new)[:15]:
        print(f"  {s}  ->  {d}")


if __name__ == "__main__":
    main()
