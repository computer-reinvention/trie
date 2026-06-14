"""CascadePlan — the full edit target set, produced once, up front.

Unifies the edit pipeline on the mature `compute_cascade` (deleting the crude
`_expand_callers`). Produces every affected symbol with its hop distance and the
callee/caller context (§2.6) each edit needs, so the parallel generation stage
(§2) has everything in one object with no phase barrier between "discover cascade"
and "generate".
"""

from __future__ import annotations

from dataclasses import dataclass

from trie.config import Config
from trie.edits.backends import NeighbourCtx
from trie.graph.store import Store
from trie.sync.cascade import compute_cascade


@dataclass(frozen=True)
class CascadeNode:
    qname: str
    file_path: str
    hop: int  # 0 = seed (directly patched), 1 = direct caller, ...


@dataclass(frozen=True)
class CascadePlan:
    seeds: set[str]  # directly patched qnames
    cascaded: list[CascadeNode]  # caller symbols pulled in by the walk
    by_file: dict[str, list[str]]  # file_path -> qnames to (re)generate
    hub_stops: list[str]  # seed qnames whose expansion stopped at a hub

    @property
    def all_qnames(self) -> set[str]:
        return set(self.seeds) | {n.qname for n in self.cascaded}


def build_cascade_plan(
    seed_qnames: list[str],
    store: Store,
    config: Config,
) -> CascadePlan:
    """Walk the caller graph from `seed_qnames` via the mature compute_cascade.

    Replaces edits/apply.py::_expand_callers. Reuses hop_by_qname and
    file_by_cascaded_qname so callers never re-query the graph to learn placement
    or ordering.
    """
    seed_files: list[str] = []
    seen_files: set[str] = set()
    for qn in seed_qnames:
        detail = store.get_symbol_detail(qn)
        if detail is None:
            continue
        if detail.file_path not in seen_files:
            seen_files.add(detail.file_path)
            seed_files.append(detail.file_path)

    result = compute_cascade(
        changed_files=seed_files,
        store=store,
        depth=config.cascade.default_depth,
        hub_threshold=config.cascade.hub_symbol_threshold,
    )

    cascaded: list[CascadeNode] = []
    for qn in sorted(result.cascaded_qnames):
        fp = result.file_by_cascaded_qname.get(qn, "")
        hop = result.hop_by_qname.get(qn, 1)
        cascaded.append(CascadeNode(qname=qn, file_path=fp, hop=hop))

    by_file: dict[str, list[str]] = {}
    for qn in seed_qnames:
        detail = store.get_symbol_detail(qn)
        if detail is not None:
            by_file.setdefault(detail.file_path, []).append(qn)
    for node in cascaded:
        if node.file_path:
            by_file.setdefault(node.file_path, []).append(node.qname)

    return CascadePlan(
        seeds=set(seed_qnames),
        cascaded=cascaded,
        by_file=by_file,
        hub_stops=[],
    )


def neighbour_context(
    qname: str,
    store: Store,
    *,
    max_each: int = 12,
) -> tuple[list[NeighbourCtx], list[NeighbourCtx]]:
    """Return (callees, callers) NeighbourCtx for `qname` — the §2.6 context.

    Callees = what this symbol depends on (contracts it must respect).
    Callers = how this symbol's result is consumed.
    Capped at `max_each` per direction to bound prompt size on hub symbols.
    """
    callees: list[NeighbourCtx] = []
    for dep in store.references_out(qname)[:max_each]:
        d = store.get_symbol_detail(dep)
        if d is not None:
            callees.append(
                NeighbourCtx(qname=dep, signature=d.signature or "", one_liner=d.one_liner)
            )
    callers: list[NeighbourCtx] = []
    for src in store.references_in(qname)[:max_each]:
        d = store.get_symbol_detail(src)
        if d is not None:
            callers.append(
                NeighbourCtx(qname=src, signature=d.signature or "", one_liner=d.one_liner)
            )
    return callees, callers
