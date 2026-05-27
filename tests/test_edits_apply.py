from __future__ import annotations

from trie.edits.apply import (
    _build_dependency_subgraph,
    tarjan_scc,
    topo_sort_sccs,
)


def _edges_to_adj(edges: list[tuple[str, str]]) -> dict[str, set[str]]:
    adj: dict[str, set[str]] = {}
    for caller, callee in edges:
        adj.setdefault(caller, set()).add(callee)
        adj.setdefault(callee, set())  # ensure leaf nodes exist
    return adj


class TestTarjanSCC:
    def test_chain_no_cycle(self):
        """A -> B -> C: each node is its own SCC."""
        graph = _edges_to_adj([("A", "B"), ("B", "C")])
        sccs = tarjan_scc(graph)
        assert len(sccs) == 3
        for scc in sccs:
            assert len(scc) == 1

    def test_single_cycle(self):
        """A -> B -> C -> A: one SCC containing all three."""
        graph = _edges_to_adj([("A", "B"), ("B", "C"), ("C", "A")])
        sccs = tarjan_scc(graph)
        assert len(sccs) == 1
        assert sccs[0] == {"A", "B", "C"}

    def test_diamond(self):
        """A -> B, A -> C, B -> D, C -> D: all single-node SCCs."""
        graph = _edges_to_adj([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")])
        sccs = tarjan_scc(graph)
        assert len(sccs) == 4
        for scc in sccs:
            assert len(scc) == 1

    def test_disconnected_components(self):
        """A->B and C->D are independent."""
        graph = _edges_to_adj([("A", "B"), ("C", "D")])
        sccs = tarjan_scc(graph)
        assert len(sccs) == 4

    def test_isolated_nodes(self):
        """Nodes with no edges are each their own SCC."""
        graph = {"A": set(), "B": set(), "C": set()}
        sccs = tarjan_scc(graph)
        assert len(sccs) == 3

    def test_two_cycles(self):
        """A->B->A and C->D->C: two independent SCCs."""
        graph = _edges_to_adj([("A", "B"), ("B", "A"), ("C", "D"), ("D", "C")])
        sccs = tarjan_scc(graph)
        assert len(sccs) == 2
        for scc in sccs:
            assert len(scc) == 2

    def test_self_loop(self):
        """A->A: self-loop is its own SCC."""
        graph = _edges_to_adj([("A", "A")])
        sccs = tarjan_scc(graph)
        sccs_sorted = sorted([sorted(s) for s in sccs])
        assert sccs_sorted == [["A"]]

    def test_chain_followed_by_cycle(self):
        """A -> B -> C -> D -> C: SCCs: {A}, {B}, {C, D}."""
        graph = _edges_to_adj([("A", "B"), ("B", "C"), ("C", "D"), ("D", "C")])
        sccs = tarjan_scc(graph)
        sizes = sorted(len(s) for s in sccs)
        assert sizes == [1, 1, 2]


class TestTopoSortSCCs:
    def test_linear_chain(self):
        """A calls B, B calls C => order: [C], [B], [A] (callee first)."""
        graph = _edges_to_adj([("A", "B"), ("B", "C")])
        sccs = tarjan_scc(graph)
        ordered = topo_sort_sccs(graph, sccs)
        qnames = [next(iter(s)) for s in ordered]
        c_idx = qnames.index("C")
        b_idx = qnames.index("B")
        a_idx = qnames.index("A")
        assert c_idx < b_idx < a_idx

    def test_diamond(self):
        """A->B, A->C, B->D, C->D: D first, then B/C, then A."""
        graph = _edges_to_adj([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")])
        sccs = tarjan_scc(graph)
        ordered = topo_sort_sccs(graph, sccs)
        qnames = [next(iter(s)) for s in ordered]
        d_idx = qnames.index("D")
        a_idx = qnames.index("A")
        assert d_idx < a_idx

    def test_cycle_preserved_together(self):
        """A -> B -> C -> A: single SCC, stays together."""
        graph = _edges_to_adj([("A", "B"), ("B", "C"), ("C", "A")])
        sccs = tarjan_scc(graph)
        ordered = topo_sort_sccs(graph, sccs)
        assert len(ordered) == 1
        assert ordered[0] == {"A", "B", "C"}

    def test_cycle_with_caller(self):
        """X -> A -> B -> A: SCC {A,B}, then {X}."""
        graph = _edges_to_adj([("X", "A"), ("A", "B"), ("B", "A")])
        sccs = tarjan_scc(graph)
        ordered = topo_sort_sccs(graph, sccs)
        assert len(ordered) == 2


class TestBuildDependencySubgraph:
    def test_filters_to_qname_set(self):
        store = type("FakeStore", (), {})()
        store.references_out = lambda qn: {"A", "B", "C", "D"}
        qnames = {"A", "B"}
        sub = _build_dependency_subgraph(qnames, store)
        assert "A" in sub
        assert "B" in sub
        # Only A and B; "C" and "D" filtered out
        for callees in sub.values():
            for c in callees:
                assert c in qnames

    def test_no_callees(self):
        store = type("FakeStore", (), {})()
        store.references_out = lambda qn: set()
        sub = _build_dependency_subgraph({"A", "B"}, store)
        assert sub == {"A": set(), "B": set()}
