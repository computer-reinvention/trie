from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from trie import telemetry
from trie.graph.store import Store


@dataclass(frozen=True)
class CascadeResult:
    """Files and symbols needing regeneration after a set of source changes.

    `changed_files` is the seed set (always included). `cascaded_from_change` is the subset
    of `affected_files` that came from following inbound edges, not direct changes —
    handy for telling the user "you edited 2 files, the cascade pulled in 5 more."

    `hop_by_file` maps each file in `affected_files` to its minimum hop distance from any
    seed file. Seed files themselves have hop 0. A file reached by a depth-1 reference
    has hop 1, and so on. Consumers can sort cascade-pulled files by hop distance to
    regenerate closest-to-the-change first — those are the sections whose prose is most
    likely to need real updates rather than just paraphrase drift.

    `cascaded_qnames` is the per-symbol projection: every qualified name reached by
    walking inbound edges from seed-file symbols. Seed-file symbols themselves are NOT
    included here (callers already know to regen everything in directly-stale files, or
    they have a more precise per-symbol stale set from `check_project`). This is the
    information that lets sync skip untouched symbols inside cascade-pulled files —
    the central premise of symbol-level regeneration.

    `hop_by_qname` mirrors `hop_by_file` but per symbol: minimum BFS distance from any
    seed-file symbol. Seed qnames map to 0; the first ring of callers to 1; etc.

    `file_by_cascaded_qname` maps each entry of `cascaded_qnames` to its defining file
    (the symbol's own file_path, not the file of the symbol it references). Lets
    callers project the cascade onto a per-file regen set without a follow-up DB query.
    """

    affected_files: list[str]
    changed_files: set[str]
    cascaded_from_change: set[str]
    hop_by_file: dict[str, int]
    cascaded_qnames: set[str]
    hop_by_qname: dict[str, int]
    file_by_cascaded_qname: dict[str, str]


def compute_cascade(
    *,
    changed_files: Iterable[str],
    store: Store,
    depth: int = 1,
    hub_threshold: int = 20,
) -> CascadeResult:
    """Walk inbound edges from symbols in `changed_files` up to `depth` hops.

    Hub guard: a symbol with more than `hub_threshold` inbound references is *not* expanded.
    Its callers are too numerous; treating it as depth-0 prevents utility hubs (utils.py,
    common types) from invalidating the whole codebase on every minor change.

    The returned `affected_files` list is sorted alphabetically with the original
    `changed_files` always included.
    """
    seed_files = set(changed_files)
    with telemetry.timed(
        "cascade",
        seeds=len(seed_files),
        depth=depth,
        hub_threshold=hub_threshold,
    ) as tele:
        if not seed_files:
            tele["affected_files"] = 0
            tele["cascaded_from_change"] = 0
            tele["hub_skips"] = 0
            return CascadeResult(
                affected_files=[],
                changed_files=set(),
                cascaded_from_change=set(),
                hop_by_file={},
                cascaded_qnames=set(),
                hop_by_qname={},
                file_by_cascaded_qname={},
            )

        inbound_counts = store.inbound_count_per_symbol()
        affected_files: set[str] = set(seed_files)
        hop_by_file: dict[str, int] = dict.fromkeys(seed_files, 0)

        seed_qnames: set[str] = set()
        for f in seed_files:
            seed_qnames.update(store.qnames_in_file(f))

        visited: set[str] = set(seed_qnames)
        frontier: list[str] = list(seed_qnames)
        # Seed qnames are at hop 0 in `hop_by_qname` for consistency with `hop_by_file`,
        # but they are NOT included in `cascaded_qnames` — that set is reserved for
        # symbols reached *by* the cascade walk, distinct from seeds.
        hop_by_qname: dict[str, int] = dict.fromkeys(seed_qnames, 0)
        cascaded_qnames: set[str] = set()
        file_by_cascaded_qname: dict[str, str] = {}
        hub_skips = 0

        for hop_idx in range(max(0, depth)):
            current_hop = hop_idx + 1  # files reached this iteration are 1 hop from frontier
            next_frontier: list[str] = []
            for qname in frontier:
                if inbound_counts.get(qname, 0) > hub_threshold:
                    # Hub symbol — skip outward expansion. The seed file itself is still
                    # in `affected_files`, but we don't pull in every caller of the hub.
                    hub_skips += 1
                    continue
                for src_qname, src_file in store.references_in_with_files(qname):
                    if src_qname in visited:
                        continue
                    visited.add(src_qname)
                    affected_files.add(src_file)
                    cascaded_qnames.add(src_qname)
                    file_by_cascaded_qname[src_qname] = src_file
                    # Min-hop semantics: a file reachable via multiple paths keeps the
                    # shallowest distance. BFS visits shallowest first, so dict.setdefault
                    # would also work; explicit min is safer if the traversal order ever
                    # changes (e.g. priority-queued by inbound weight in a future ranking).
                    existing = hop_by_file.get(src_file)
                    hop_by_file[src_file] = (
                        current_hop if existing is None else min(existing, current_hop)
                    )
                    # Per-symbol hop tracking mirrors per-file: BFS visits shallowest
                    # first, so the first time we see a qname is also its min hop.
                    existing_q = hop_by_qname.get(src_qname)
                    hop_by_qname[src_qname] = (
                        current_hop if existing_q is None else min(existing_q, current_hop)
                    )
                    next_frontier.append(src_qname)
            if not next_frontier:
                break
            frontier = next_frontier

        cascaded = affected_files - seed_files
        tele["affected_files"] = len(affected_files)
        tele["cascaded_from_change"] = len(cascaded)
        tele["cascaded_qnames"] = len(cascaded_qnames)
        tele["hub_skips"] = hub_skips
        tele["max_hop"] = max(hop_by_file.values(), default=0)
        return CascadeResult(
            affected_files=sorted(affected_files),
            changed_files=seed_files,
            cascaded_from_change=cascaded,
            hop_by_file=hop_by_file,
            cascaded_qnames=cascaded_qnames,
            hop_by_qname=hop_by_qname,
            file_by_cascaded_qname=file_by_cascaded_qname,
        )
