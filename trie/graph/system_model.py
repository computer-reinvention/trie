"""Assemble a high-level *system model* from the symbol graph.

The desktop graph view renders a *model of the system*, not one node per
symbol. This module turns the raw symbols + edges + LLM tags in the store into
a compact, already-meaningful structure the frontend can draw directly.

Empirically grounded (against trie's own ~1.4k-symbol graph) decisions:

- **Tests are excluded from the model by default.** They are 55% of the raw
  graph and invert the architecture (every `test_*` reads as a door, and
  `test -> X` dominates the role-flow). They are flagged (`is_test`) so the
  frontend can toggle them, never silently dropped.
- **`__module__` container nodes are dropped** — zero-edge file stand-ins,
  redundant with subsystem grouping.
- **Blind-spot rule:** a zero-edge *method* whose owning *class* is connected
  is NOT dead code — it is a dynamic-dispatch blind spot (called via an
  instance, a dunder protocol, a property, or cross-language MCP). It inherits
  the class's connectivity context and is classified `internal`, never
  `orphan`. Empirically, 100% of trie's "orphan methods" are of this kind.
- **Multi-signal door rubric:** decorators (`@app.command`, routes, MCP tools),
  pyproject `[project.scripts]`, the LLM `boundary=entry` field, and
  production-only-inbound==0 — never a single fragile degree heuristic.
- **L0 components on two axes:** role (functional, ~11 groups) and subsystem
  (folder, ~26 groups), each with member counts and aggregated group-to-group
  flow (thresholded so L0 stays a readable architecture diagram).
- **Precomputed layered layout:** trie's production call graph is 99.6%
  acyclic, so a stable depth-layered layout exists. Positions are baked in so
  the client seeds from them (mental-map preservation) instead of a random
  force start.

Everything here is pure graph math over data already in the store — no LLM
calls, no new dependencies. Betweenness and community detection are hand-rolled
(Brandes / label propagation) with a scale guard so large graphs stay fast.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path

from trie.graph.store import Store

# Decorator patterns that mark a framework-registered entry point. The framework
# literally declares "the outside world calls this": Typer/Click commands, web
# routes, MCP tools, task runners. Matched against the symbol's decorator lines.
_ENTRY_DECORATOR_RE = re.compile(
    r"@[\w.]*\.(command|callback|route|get|post|put|delete|patch|tool|task)\b"
    r"|@(app|cli|click)\.\w+"
    r"|@\w*router\.\w+",
    re.IGNORECASE,
)

# Caller scopes that don't count as "production": an entry point invoked only by
# tests/scripts is still an entry point, and tests distort the whole model.
_TEST_PREFIXES = ("tests/", "test/")
_NON_PRODUCTION_PREFIXES = (*_TEST_PREFIXES, "scripts/", "script/", "examples/")

# Above this node count, exact Brandes betweenness (O(V*E)) is too slow for an
# interactive endpoint; we sample pivot sources instead.
_BETWEENNESS_EXACT_MAX = 3000
_BETWEENNESS_PIVOTS = 400

# Cache format version — bump to invalidate all cached models on logic changes.
_MODEL_CACHE_VERSION = 2


@dataclass(frozen=True)
class SystemNode:
    qname: str
    name: str
    kind: str
    file_path: str
    role: str
    boundary: str
    subsystem: str
    is_public: bool
    is_test: bool
    inbound: int  # total in-project callers
    outbound: int  # total in-project callees
    prod_inbound: int  # callers excluding tests/scripts
    cls: str  # door | hub | bedrock | exit | orphan | normal | internal | test
    salience: float  # 0..1, drives "is it worth drawing" + node size
    betweenness: float  # 0..1 normalized
    depth: int  # BFS hops from nearest entry point; -1 if unreachable
    community: int  # connectivity-cluster id
    one_liner: str
    x: float  # precomputed layout position
    y: float


@dataclass(frozen=True)
class GroupFlow:
    source: str
    target: str
    weight: int  # number of call edges crossing this group boundary


@dataclass(frozen=True)
class GroupSummary:
    key: str  # role name or subsystem path
    count: int
    door_count: int
    hub_count: int


@dataclass(frozen=True)
class ComponentAxis:
    """One L0 grouping axis: the component nodes + flow between them."""

    axis: str  # "role" | "subsystem"
    groups: list[GroupSummary]
    flows: list[GroupFlow]


@dataclass(frozen=True)
class SystemModel:
    nodes: list[SystemNode]  # production nodes (tests excluded unless requested)
    test_nodes: list[SystemNode]  # tests, kept separate for the toggle
    axes: dict[str, ComponentAxis]  # "role" and "subsystem"
    landmarks: list[str]  # qnames for the L1 view (most salient)
    stats: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------


def _is_test(file_path: str) -> bool:
    return file_path.startswith(_TEST_PREFIXES)


def _is_production(file_path: str) -> bool:
    return not file_path.startswith(_NON_PRODUCTION_PREFIXES)


def _subsystem_of(file_path: str) -> str:
    """Top-two path segments as the subsystem key: trie/sync, trie/cli.py, ..."""
    parts = file_path.split("/")
    return "/".join(parts[:2]) if len(parts) >= 2 else parts[0]


def _owning_class(qname: str) -> str | None:
    """Return the owning class qname for a method qname, else None.

    `trie/graph/store:Store.add_patch` -> `trie/graph/store:Store`.
    """
    if ":" not in qname:
        return None
    module, local = qname.split(":", 1)
    if "." not in local:
        return None
    return f"{module}:{local.rsplit('.', 1)[0]}"


# ---------------------------------------------------------------------------
# Raw extraction
# ---------------------------------------------------------------------------


def _load_raw(store: Store) -> tuple[dict[str, dict], list[tuple[str, str]]]:
    """Return ({qname: row}, [(src_qname, dst_qname), ...]) from the store."""
    conn = store._conn
    sym_rows = conn.execute(
        """
        SELECT
            s.id, s.qualified_name, s.name, s.kind, s.file_path, s.is_public,
            COALESCE(s.decorators, '') AS decorators,
            COALESCE(ts.role, '') AS role,
            COALESCE(ts.boundary, '') AS boundary,
            COALESCE(ts.one_liner, '') AS one_liner
        FROM symbols s
        LEFT JOIN triefact_sections ts ON ts.symbol_id = s.id
        """
    ).fetchall()
    id_to_qname: dict[int, str] = {r[0]: r[1] for r in sym_rows}
    nodes: dict[str, dict] = {}
    for r in sym_rows:
        # Drop module container nodes — zero-edge, redundant with grouping.
        if r[3] == "module":
            continue
        nodes[r[1]] = {
            "id": r[0],
            "qname": r[1],
            "name": r[2],
            "kind": r[3],
            "file_path": r[4],
            "is_public": bool(r[5]),
            "decorators": r[6],
            "role": r[7],
            "boundary": r[8],
            "one_liner": r[9],
        }
    edges: list[tuple[str, str]] = []
    # `contains` edges (class -> its own methods) are structural, not dependency
    # relationships. Including them would distort betweenness, depth, and the
    # door/hub/orphan classification this model is built on (e.g. every method
    # would gain an inbound edge from its class). The system model uses the
    # call/reference/import/inherit graph; `contains` stays out. It is still
    # exposed via `all_edges` for AGM attention propagation.
    for src_id, dst_id, kind in conn.execute(
        "SELECT src_symbol_id, dst_symbol_id, kind FROM edges"
    ):
        if kind == "contains":
            continue
        s = id_to_qname.get(src_id)
        d = id_to_qname.get(dst_id)
        if s is not None and d is not None and s != d and s in nodes and d in nodes:
            edges.append((s, d))
    return nodes, edges


def _pyproject_entry_targets(project_root: Path) -> set[str]:
    """Parse `[project.scripts]` console-entry targets from pyproject.toml.

    `trie = "trie.cli:app"` becomes the qname `trie/cli:app`.
    """
    pp = project_root / "pyproject.toml"
    if not pp.exists():
        return set()
    try:
        import tomllib
    except ModuleNotFoundError:  # pragma: no cover - py<3.11
        return set()
    try:
        data = tomllib.loads(pp.read_text())
    except Exception:
        return set()
    scripts = (data.get("project", {}) or {}).get("scripts", {}) or {}
    targets: set[str] = set()
    for spec in scripts.values():
        if isinstance(spec, str) and ":" in spec:
            module, obj = spec.split(":", 1)
            targets.add(f"{module.replace('.', '/')}:{obj}")
    return targets


# ---------------------------------------------------------------------------
# Graph metrics (dependency-free, scale-guarded)
# ---------------------------------------------------------------------------


def _betweenness(qnames: list[str], adj: dict[str, list[str]]) -> dict[str, float]:
    """Brandes' betweenness, normalized 0..1.

    Exact for graphs below `_BETWEENNESS_EXACT_MAX`; above that, sample a fixed
    set of pivot sources (deterministic order) and scale — keeps the endpoint
    interactive on large graphs at the cost of approximate centrality.
    """
    bc: dict[str, float] = dict.fromkeys(qnames, 0.0)
    if len(qnames) <= _BETWEENNESS_EXACT_MAX:
        sources = qnames
        scale = 1.0
    else:
        step = max(1, len(qnames) // _BETWEENNESS_PIVOTS)
        sources = qnames[::step]
        scale = len(qnames) / len(sources)

    for s in sources:
        stack: list[str] = []
        preds: dict[str, list[str]] = defaultdict(list)
        sigma = dict.fromkeys(qnames, 0.0)
        sigma[s] = 1.0
        dist = dict.fromkeys(qnames, -1)
        dist[s] = 0
        q: deque[str] = deque([s])
        while q:
            v = q.popleft()
            stack.append(v)
            for w in adj.get(v, ()):
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    preds[w].append(v)
        delta = dict.fromkeys(qnames, 0.0)
        while stack:
            w = stack.pop()
            for v in preds[w]:
                if sigma[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                bc[w] += delta[w] * scale
    mx = max(bc.values(), default=0.0)
    if mx > 0:
        for k in bc:
            bc[k] /= mx
    return bc


def _communities(qnames: list[str], undirected: dict[str, set[str]]) -> dict[str, int]:
    """Label-propagation community detection (deterministic, capped iterations)."""
    label: dict[str, int] = {q: i for i, q in enumerate(qnames)}
    order = sorted(qnames)
    for _ in range(20):
        changed = False
        for v in order:
            nbrs = undirected.get(v)
            if not nbrs:
                continue
            counts: dict[int, int] = defaultdict(int)
            for n in nbrs:
                counts[label[n]] += 1
            best = min(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0]
            if label[v] != best:
                label[v] = best
                changed = True
        if not changed:
            break
    remap: dict[int, int] = {}
    for v in order:
        remap.setdefault(label[v], len(remap))
    return {v: remap[label[v]] for v in qnames}


def _depth_from_entries(
    entry_qnames: list[str], adj: dict[str, list[str]], qnames: list[str]
) -> dict[str, int]:
    """Multi-source BFS depth from doors along caller->callee edges."""
    depth = dict.fromkeys(qnames, -1)
    q: deque[str] = deque()
    for e in entry_qnames:
        if e in depth:
            depth[e] = 0
            q.append(e)
    while q:
        v = q.popleft()
        for w in adj.get(v, ()):
            if depth[w] < 0:
                depth[w] = depth[v] + 1
                q.append(w)
    return depth


# ---------------------------------------------------------------------------
# Precomputed layered layout (mental-map-stable seed for the client)
# ---------------------------------------------------------------------------


def _layered_layout(
    qnames: list[str],
    depth: dict[str, int],
    subsystem: dict[str, str],
) -> dict[str, tuple[float, float]]:
    """Deterministic layout: y by depth-from-door, x grouped by subsystem.

    The production call graph is near-acyclic, so depth gives a clean vertical
    flow (doors at top, plumbing below). Within a depth band, nodes are grouped
    by subsystem and spread horizontally. Unreachable nodes (depth -1) sink to a
    bottom band. Positions are a stable seed; the client relaxes locally.
    """
    LAYER_H = 180.0
    X_GAP = 90.0
    max_depth = max((d for d in depth.values() if d >= 0), default=0)
    # bucket by (depth, subsystem) for stable ordering
    buckets: dict[int, list[str]] = defaultdict(list)
    for q in sorted(qnames, key=lambda q: (subsystem.get(q, ""), q)):
        d = depth.get(q, -1)
        band = d if d >= 0 else max_depth + 1
        buckets[band].append(q)
    pos: dict[str, tuple[float, float]] = {}
    for band, members in buckets.items():
        n = len(members)
        width = (n - 1) * X_GAP
        for i, q in enumerate(members):
            x = i * X_GAP - width / 2
            y = band * LAYER_H
            pos[q] = (round(x, 1), round(y, 1))
    return pos


# ---------------------------------------------------------------------------
# Classification rubric
# ---------------------------------------------------------------------------


def _has_entry_decorator(decorators: str) -> bool:
    return bool(decorators) and bool(_ENTRY_DECORATOR_RE.search(decorators))


def _classify(
    node: dict,
    *,
    inbound: int,
    outbound: int,
    prod_inbound: int,
    pyproject_targets: set[str],
    connected_classes: set[str],
    inbound_hi: int,
    outbound_hi: int,
) -> str:
    """Assign a skeleton class via the multi-signal rubric.

    Precedence: door > exit > hub > bedrock > (blind-spot -> internal) >
    orphan > normal. Doors win on any strong boundary signal. Tests are
    classified `test` upstream and never reach here.
    """
    qname = node["qname"]
    boundary = node["boundary"]

    is_door = (
        _has_entry_decorator(node["decorators"])
        or qname in pyproject_targets
        or boundary == "entry"
        or (node["is_public"] and prod_inbound == 0 and outbound > 0)
    )
    if is_door:
        return "door"
    if boundary == "exit":
        return "exit"
    if inbound >= inbound_hi and outbound >= outbound_hi:
        return "hub"
    if outbound == 0 and inbound >= inbound_hi:
        return "bedrock"
    if inbound == 0 and outbound == 0:
        # Blind-spot rule: a zero-edge member (method, or a typed-language
        # enum_member / property) whose owning container IS connected is reached
        # by dynamic dispatch or member access — not dead. Treat as internal.
        if node["kind"] in ("method", "enum_member", "property") and (
            _owning_class(qname) in connected_classes
        ):
            return "internal"
        return "orphan"
    return "normal"


def _salience(
    *,
    cls: str,
    prod_inbound: int,
    outbound: int,
    betweenness: float,
    is_public: bool,
    inbound_hi: int,
) -> float:
    """0..1 importance score: class weight + centrality + degree."""
    base = {
        "door": 0.85,
        "hub": 0.8,
        "exit": 0.55,
        "bedrock": 0.45,
        "normal": 0.2,
        "internal": 0.18,
        "orphan": 0.1,
    }.get(cls, 0.2)
    deg = min(1.0, (prod_inbound + outbound) / (max(1, inbound_hi) * 2))
    score = 0.55 * base + 0.30 * betweenness + 0.15 * deg
    if is_public:
        score = min(1.0, score + 0.05)
    return round(score, 4)


# ---------------------------------------------------------------------------
# Component-axis aggregation (L0)
# ---------------------------------------------------------------------------


def _build_axis(
    axis: str,
    key_of: dict[str, str],
    cls_by_q: dict[str, str],
    edges: list[tuple[str, str]],
    prod_qnames: set[str],
) -> ComponentAxis:
    """Aggregate production nodes into L0 component nodes + thresholded flow."""
    count: dict[str, int] = defaultdict(int)
    doors: dict[str, int] = defaultdict(int)
    hubs: dict[str, int] = defaultdict(int)
    for q in prod_qnames:
        k = key_of[q]
        count[k] += 1
        if cls_by_q[q] == "door":
            doors[k] += 1
        elif cls_by_q[q] == "hub":
            hubs[k] += 1
    groups = [
        GroupSummary(key=k, count=c, door_count=doors[k], hub_count=hubs[k])
        for k, c in sorted(count.items(), key=lambda kv: -kv[1])
    ]

    raw_flow: dict[tuple[str, str], int] = defaultdict(int)
    for s, d in edges:
        if s not in prod_qnames or d not in prod_qnames:
            continue
        ks, kd = key_of[s], key_of[d]
        if ks != kd:
            raw_flow[(ks, kd)] += 1

    # Threshold: keep top-3 outgoing per source group UNION any flow >= 10.
    # Empirically (trie) this turns a 62-edge near-hairball into ~21-31 clean
    # edges that read as an architecture diagram.
    by_source: dict[str, list[tuple[tuple[str, str], int]]] = defaultdict(list)
    for k, w in raw_flow.items():
        by_source[k[0]].append((k, w))
    keep: set[tuple[str, str]] = set()
    for items in by_source.values():
        for k, _w in sorted(items, key=lambda kv: -kv[1])[:3]:
            keep.add(k)
    for k, w in raw_flow.items():
        if w >= 10:
            keep.add(k)
    flows = [
        GroupFlow(source=k[0], target=k[1], weight=raw_flow[k])
        for k in sorted(keep, key=lambda k: -raw_flow[k])
    ]
    return ComponentAxis(axis=axis, groups=groups, flows=flows)


# ---------------------------------------------------------------------------
# Top-level assembly
# ---------------------------------------------------------------------------


def build_system_model(
    store: Store,
    *,
    project_root: Path,
    landmark_limit: int = 160,
) -> SystemModel:
    """Compute the full system model from the store. Pure graph math.

    Classification, metrics, salience, and the L0 component axes are computed on
    the PRODUCTION subgraph (tests excluded). Tests are returned separately,
    flagged, for the frontend toggle.
    """
    raw_nodes, all_edges = _load_raw(store)

    test_q = {q for q, n in raw_nodes.items() if _is_test(n["file_path"])}
    prod_q = [q for q in raw_nodes if q not in test_q]
    prod_set = set(prod_q)
    # Production subgraph edges only — tests must not pollute classification/flow.
    edges = [(s, d) for s, d in all_edges if s in prod_set and d in prod_set]

    # Degrees on the production subgraph.
    adj: dict[str, list[str]] = defaultdict(list)
    undirected: dict[str, set[str]] = defaultdict(set)
    inbound = dict.fromkeys(prod_q, 0)
    outbound = dict.fromkeys(prod_q, 0)
    prod_inbound = dict.fromkeys(prod_q, 0)
    for s, d in edges:
        adj[s].append(d)
        undirected[s].add(d)
        undirected[d].add(s)
        outbound[s] += 1
        inbound[d] += 1
        prod_inbound[d] += 1  # all production-only here

    # Connected classes — for the blind-spot rule. A class is "connected" if it
    # has any edge or any connected member.
    connected_classes: set[str] = set()
    for q in prod_q:
        if inbound[q] or outbound[q]:
            connected_classes.add(q)  # the class node itself may be connected
            owner = _owning_class(q)
            if owner:
                connected_classes.add(owner)

    def _hi(counts: dict[str, int]) -> int:
        vals = sorted(counts.values())
        if not vals:
            return 1
        idx = int(len(vals) * 0.9)
        return max(3, vals[min(idx, len(vals) - 1)])

    inbound_hi = _hi(inbound)
    outbound_hi = _hi(outbound)
    pyproject_targets = _pyproject_entry_targets(project_root)

    cls_by_q: dict[str, str] = {}
    for q in prod_q:
        cls_by_q[q] = _classify(
            raw_nodes[q],
            inbound=inbound[q],
            outbound=outbound[q],
            prod_inbound=prod_inbound[q],
            pyproject_targets=pyproject_targets,
            connected_classes=connected_classes,
            inbound_hi=inbound_hi,
            outbound_hi=outbound_hi,
        )

    betweenness = _betweenness(prod_q, adj)
    community = _communities(prod_q, undirected)
    door_q = [q for q in prod_q if cls_by_q[q] == "door"]
    depth = _depth_from_entries(door_q, adj, prod_q)

    role_of = {q: (raw_nodes[q]["role"] or "untagged") for q in prod_q}
    subsys_of = {q: _subsystem_of(raw_nodes[q]["file_path"]) for q in prod_q}
    positions = _layered_layout(prod_q, depth, subsys_of)

    def _make_node(q: str, cls: str, *, is_test: bool) -> SystemNode:
        rn = raw_nodes[q]
        x, y = positions.get(q, (0.0, 0.0))
        return SystemNode(
            qname=q,
            name=rn["name"],
            kind=rn["kind"],
            file_path=rn["file_path"],
            role=rn["role"],
            boundary=rn["boundary"],
            subsystem=_subsystem_of(rn["file_path"]),
            is_public=rn["is_public"],
            is_test=is_test,
            inbound=inbound.get(q, 0),
            outbound=outbound.get(q, 0),
            prod_inbound=prod_inbound.get(q, 0),
            cls=cls,
            salience=_salience(
                cls=cls,
                prod_inbound=prod_inbound.get(q, 0),
                outbound=outbound.get(q, 0),
                betweenness=betweenness.get(q, 0.0),
                is_public=rn["is_public"],
                inbound_hi=inbound_hi,
            ),
            betweenness=round(betweenness.get(q, 0.0), 4),
            depth=depth.get(q, -1),
            community=community.get(q, -1),
            one_liner=rn["one_liner"],
            x=x,
            y=y,
        )

    nodes = [_make_node(q, cls_by_q[q], is_test=False) for q in prod_q]
    test_nodes = [_make_node(q, "test", is_test=True) for q in sorted(test_q)]

    axes = {
        "role": _build_axis("role", role_of, cls_by_q, edges, prod_set),
        "subsystem": _build_axis("subsystem", subsys_of, cls_by_q, edges, prod_set),
    }

    landmarks = [n.qname for n in sorted(nodes, key=lambda n: -n.salience)[:landmark_limit]]

    from collections import Counter

    stats = {
        "production_nodes": len(nodes),
        "test_nodes": len(test_nodes),
        "edges": len(edges),
        "class_counts": dict(Counter(n.cls for n in nodes)),
        "role_count": len(axes["role"].groups),
        "subsystem_count": len(axes["subsystem"].groups),
    }

    return SystemModel(
        nodes=nodes,
        test_nodes=test_nodes,
        axes=axes,
        landmarks=landmarks,
        stats=stats,
    )


def system_model_to_dict(model: SystemModel, *, include_tests: bool = False) -> dict:
    """Serialize a SystemModel to the JSON shape the desktop endpoint returns."""

    def node_dict(n: SystemNode) -> dict:
        return {
            "qname": n.qname,
            "name": n.name,
            "kind": n.kind,
            "file_path": n.file_path,
            "role": n.role,
            "boundary": n.boundary,
            "subsystem": n.subsystem,
            "is_public": n.is_public,
            "is_test": n.is_test,
            "inbound_count": n.inbound,
            "outbound_count": n.outbound,
            "prod_inbound_count": n.prod_inbound,
            "cls": n.cls,
            "salience": n.salience,
            "betweenness": n.betweenness,
            "depth": n.depth,
            "community": n.community,
            "one_liner": n.one_liner,
            "x": n.x,
            "y": n.y,
        }

    nodes = list(model.nodes)
    if include_tests:
        nodes = nodes + list(model.test_nodes)

    def axis_dict(ax: ComponentAxis) -> dict:
        return {
            "axis": ax.axis,
            "groups": [
                {
                    "key": g.key,
                    "count": g.count,
                    "door_count": g.door_count,
                    "hub_count": g.hub_count,
                }
                for g in ax.groups
            ],
            "flows": [
                {"source": f.source, "target": f.target, "weight": f.weight} for f in ax.flows
            ],
        }

    return {
        "nodes": [node_dict(n) for n in nodes],
        "axes": {name: axis_dict(ax) for name, ax in model.axes.items()},
        "landmarks": model.landmarks,
        "stats": model.stats,
    }


# ---------------------------------------------------------------------------
# Caching — the model is deterministic per graph state; recompute only on change
# ---------------------------------------------------------------------------


def _graph_fingerprint(store: Store) -> str:
    """Cheap fingerprint of the graph state: symbol + edge + section counts and
    the max section timestamp. Changes whenever a scan or sync mutates the DB.
    """
    conn = store._conn
    sym = conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]
    edg = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    sec = conn.execute("SELECT COUNT(*) FROM triefact_sections").fetchone()[0]
    ts = conn.execute(
        "SELECT COALESCE(MAX(last_generated_at), 0) FROM triefact_sections"
    ).fetchone()[0]
    raw = f"{_MODEL_CACHE_VERSION}:{sym}:{edg}:{sec}:{ts}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def build_system_model_cached(
    store: Store,
    *,
    project_root: Path,
    landmark_limit: int = 160,
    include_tests: bool = False,
) -> dict:
    """Return the serialized system model, using an on-disk cache keyed by graph
    fingerprint. Recomputes only when the graph has changed since last build.

    The cache holds the full model (tests included); `include_tests` only
    controls what this call returns.
    """
    fp = _graph_fingerprint(store)
    cache_path = project_root / ".trie" / "system_model.json"
    cached: dict | None = None
    if cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text())
        except Exception:
            cached = None
    if cached is not None and cached.get("fingerprint") == fp:
        payload = cached["model"]
    else:
        model = build_system_model(store, project_root=project_root, landmark_limit=landmark_limit)
        # Cache the full model (tests included) so the toggle is free.
        payload = system_model_to_dict(model, include_tests=True)
        try:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps({"fingerprint": fp, "model": payload}))
        except Exception:
            pass  # cache is best-effort

    if include_tests:
        return payload
    # Filter tests out of the returned view (cache always stores them).
    return {
        **payload,
        "nodes": [n for n in payload["nodes"] if not n.get("is_test")],
    }
