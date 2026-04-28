from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from trie.graph.store import Store


@dataclass(frozen=True)
class CascadeResult:
    """Files needing regeneration after a set of source changes.

    `changed_files` is the seed set (always included). `cascaded_from_change` is the subset
    of `affected_files` that came from following inbound edges, not direct changes —
    handy for telling the user "you edited 2 files, the cascade pulled in 5 more."
    """

    affected_files: list[str]
    changed_files: set[str]
    cascaded_from_change: set[str]


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
    if not seed_files:
        return CascadeResult(
            affected_files=[],
            changed_files=set(),
            cascaded_from_change=set(),
        )

    inbound_counts = store.inbound_count_per_symbol()
    affected_files: set[str] = set(seed_files)

    seed_qnames: set[str] = set()
    for f in seed_files:
        seed_qnames.update(store.qnames_in_file(f))

    visited: set[str] = set(seed_qnames)
    frontier: list[str] = list(seed_qnames)

    for _hop in range(max(0, depth)):
        next_frontier: list[str] = []
        for qname in frontier:
            if inbound_counts.get(qname, 0) > hub_threshold:
                # Hub symbol — skip outward expansion. The seed file itself is still
                # in `affected_files`, but we don't pull in every caller of the hub.
                continue
            for src_qname, src_file, _conf in store.references_in_with_files(qname):
                if src_qname in visited:
                    continue
                visited.add(src_qname)
                affected_files.add(src_file)
                next_frontier.append(src_qname)
        if not next_frontier:
            break
        frontier = next_frontier

    cascaded = affected_files - seed_files
    return CascadeResult(
        affected_files=sorted(affected_files),
        changed_files=seed_files,
        cascaded_from_change=cascaded,
    )
