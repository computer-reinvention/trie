"""Assemble a high-level *system model* from the symbol graph.

The desktop graph view renders a *model of the system*, not one node per
symbol. This module turns the raw symbols + edges + LLM tags in the store into
a compact, already-meaningful structure the frontend can draw directly:

- every node classified (door / hub / bedrock / exit / normal) via a
  multi-signal rubric — decorators, pyproject scripts, production-only inbound,
  the LLM `boundary` field — never a single fragile degree heuristic;
- a salience score per node deciding what is worth drawing and how large;
- betweenness centrality (Brandes) to find true bottlenecks vs popular leaves;
- reachability depth from entry points (doors on the rim, plumbing in the core);
- connectivity communities (label propagation) as a grouping axis;
- role nodes with counts and aggregated role-to-role flow edges (the L0 view).

Everything here is pure graph math over data already in the store — no LLM
calls, no new dependencies. Betweenness and community detection are
hand-rolled (Brandes / label propagation) to keep trie dependency-free; both
are fast at the ~1.4k-node / ~2.5k-edge scale of a real project.
"""

from __future__ import annotations

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

# Caller scopes that don't count as "production" for entry-point detection:
# an entry point invoked only by tests/scripts is still an entry point.
_NON_PRODUCTION_PREFIXES = ("tests/", "test/", "scripts/", "script/", "examples/")


@dataclass(frozen=True)
class SystemNode:
    qname: str
    name: str
    kind: str
    file_path: str
    role: str
    boundary: str
    is_public: bool
    inbound: int  # total in-project callers
    outbound: int  # total in-project callees
    prod_inbound: int  # callers excluding tests/scripts
    cls: str  # door | hub | bedrock | exit | orphan | normal
    salience: float  # 0..1, drives "is it worth drawing" + node size
    betweenness: float  # 0..1 normalized
    depth: int  # BFS hops from nearest entry point; -1 if unreachable
    community: int  # connectivity-cluster id
    one_liner: str


@dataclass(frozen=True)
class RoleFlow:
    source: str
    target: str
    weight: int  # number of call edges crossing this role boundary


@dataclass(frozen=True)
class RoleSummary:
    role: str
    count: int
    door_count: int
    hub_count: int


@dataclass(frozen=True)
class SystemModel:
    nodes: list[SystemNode]
    roles: list[RoleSummary]
    role_flows: list[RoleFlow]
    landmarks: list[str] = field(default_factory=list)  # qnames for the L1 view


# ---------------------------------------------------------------------------
# Raw extraction
# ---------------------------------------------------------------------------


def _is_production(file_path: str) -> bool:
    return not file_path.startswith(_NON_PRODUCTION_PREFIXES)


def _load_raw(store: Store) -> tuple[
    dict[str, dict],
    list[tuple[str, str]],
]:
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
    edge_rows = conn.execute(
        "SELECT src_symbol_id, dst_symbol_id FROM edges"
    ).fetchall()
    edges: list[tuple[str, str]] = []
    for src_id, dst_id in edge_rows:
        s = id_to_qname.get(src_id)
        d = id_to_qname.get(dst_id)
        if s is not None and d is not None and s != d:
            edges.append((s, d))
    return nodes, edges


def _pyproject_entry_targets(project_root: Path) -> set[str]:
    """Parse `[project.scripts]` console-entry targets from pyproject.toml.

    Returns a set of qnames in trie's `module:object` form. A pyproject entry
    `trie = "trie.cli:app"` becomes `trie/cli:app`.
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
        if not isinstance(spec, str) or ":" not in spec:
            continue
        module, obj = spec.split(":", 1)
        targets.add(f"{module.replace('.', '/')}:{obj}")
    return targets


# ---------------------------------------------------------------------------
# Graph metrics (dependency-free)
# ---------------------------------------------------------------------------


def _betweenness(
    qnames: list[str], adj: dict[str, list[str]]
) -> dict[str, float]:
    """Brandes' betweenness centrality on the unweighted directed graph.

    Returns values normalized to 0..1 by the maximum. O(V*E); fine at trie scale.
    """
    bc: dict[str, float] = dict.fromkeys(qnames, 0.0)
    for s in qnames:
        stack: list[str] = []
        preds: dict[str, list[str]] = {v: [] for v in qnames}
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
                if sigma[w] != 0:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                bc[w] += delta[w]
    mx = max(bc.values(), default=0.0)
    if mx > 0:
        for k in bc:
            bc[k] /= mx
    return bc


def _communities(
    qnames: list[str], undirected: dict[str, set[str]]
) -> dict[str, int]:
    """Label-propagation community detection on the undirected projection.

    Deterministic: nodes processed in a fixed order; ties broken by smallest
    label. Converges fast; capped iterations as a safety net.
    """
    label: dict[str, int] = {q: i for i, q in enumerate(qnames)}
    order = sorted(qnames)
    for _ in range(20):
        changed = False
        for v in order:
            nbrs = undirected.get(v, ())
            if not nbrs:
                continue
            counts: dict[int, int] = defaultdict(int)
            for n in nbrs:
                counts[label[n]] += 1
            # pick the most frequent neighbour label; tie -> smallest label id
            best = min(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0]
            if label[v] != best:
                label[v] = best
                changed = True
        if not changed:
            break
    # compact community ids to 0..k
    remap: dict[int, int] = {}
    for v in order:
        remap.setdefault(label[v], len(remap))
    return {v: remap[label[v]] for v in qnames}


def _depth_from_entries(
    entry_qnames: list[str], adj: dict[str, list[str]], qnames: list[str]
) -> dict[str, int]:
    """Multi-source BFS depth from entry points along caller->callee edges."""
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
# Classification rubric
# ---------------------------------------------------------------------------


def _has_entry_decorator(decorators: str) -> bool:
    return bool(decorators) and bool(_ENTRY_DECORATOR_RE.search(decorators))


def _classify(
    node: dict,
    *,
    prod_inbound: int,
    inbound: int,
    outbound: int,
    pyproject_targets: set[str],
    inbound_hi: int,
    outbound_hi: int,
) -> str:
    """Assign a skeleton class via the multi-signal rubric.

    Precedence: door > exit > hub > bedrock > orphan > normal. `door` wins on
    any strong boundary signal because being a system entrance is the most
    salient architectural fact about a symbol.
    """
    qname = node["qname"]
    boundary = node["boundary"]
    decorators = node["decorators"]

    is_door = (
        _has_entry_decorator(decorators)
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
    """0..1 importance score. Combines class weight, degree, centrality.

    Doors and hubs float to the top; trivial helpers sink near zero so the
    default view can omit them until the user drills in.
    """
    base = {
        "door": 0.85,
        "hub": 0.8,
        "exit": 0.55,
        "bedrock": 0.45,
        "normal": 0.2,
        "orphan": 0.1,
    }.get(cls, 0.2)
    # degree contribution (saturating)
    denom = max(1, inbound_hi)
    deg = min(1.0, (prod_inbound + outbound) / (denom * 2))
    score = 0.55 * base + 0.30 * betweenness + 0.15 * deg
    if is_public:
        score = min(1.0, score + 0.05)
    return round(score, 4)


# ---------------------------------------------------------------------------
# Top-level assembly
# ---------------------------------------------------------------------------


def build_system_model(
    store: Store,
    *,
    project_root: Path,
    landmark_limit: int = 60,
) -> SystemModel:
    """Compute the full system model from the store. Pure graph math."""
    raw_nodes, edges = _load_raw(store)
    qnames = list(raw_nodes.keys())

    # adjacency (caller -> callees) and reverse; plus undirected projection
    adj: dict[str, list[str]] = defaultdict(list)
    radj: dict[str, list[str]] = defaultdict(list)
    undirected: dict[str, set[str]] = defaultdict(set)
    inbound = dict.fromkeys(qnames, 0)
    outbound = dict.fromkeys(qnames, 0)
    prod_inbound = dict.fromkeys(qnames, 0)
    for s, d in edges:
        adj[s].append(d)
        radj[d].append(s)
        undirected[s].add(d)
        undirected[d].add(s)
        outbound[s] += 1
        inbound[d] += 1
        if _is_production(raw_nodes[s]["file_path"]):
            prod_inbound[d] += 1

    # thresholds derived from the distribution (90th percentile-ish via simple
    # heuristic): "high" = notably above the mean. Cheap and adaptive per project.
    def _hi(counts: dict[str, int]) -> int:
        vals = sorted(counts.values())
        if not vals:
            return 1
        idx = int(len(vals) * 0.9)
        return max(3, vals[min(idx, len(vals) - 1)])

    inbound_hi = _hi(inbound)
    outbound_hi = _hi(outbound)

    pyproject_targets = _pyproject_entry_targets(project_root)

    # classify
    cls_by_q: dict[str, str] = {}
    for q in qnames:
        cls_by_q[q] = _classify(
            raw_nodes[q],
            prod_inbound=prod_inbound[q],
            inbound=inbound[q],
            outbound=outbound[q],
            pyproject_targets=pyproject_targets,
            inbound_hi=inbound_hi,
            outbound_hi=outbound_hi,
        )

    # metrics
    betweenness = _betweenness(qnames, adj)
    community = _communities(qnames, undirected)
    door_qnames = [q for q in qnames if cls_by_q[q] == "door"]
    depth = _depth_from_entries(door_qnames, adj, qnames)

    # build nodes
    nodes: list[SystemNode] = []
    for q in qnames:
        rn = raw_nodes[q]
        cls = cls_by_q[q]
        sal = _salience(
            cls=cls,
            prod_inbound=prod_inbound[q],
            outbound=outbound[q],
            betweenness=betweenness[q],
            is_public=rn["is_public"],
            inbound_hi=inbound_hi,
        )
        nodes.append(
            SystemNode(
                qname=q,
                name=rn["name"],
                kind=rn["kind"],
                file_path=rn["file_path"],
                role=rn["role"],
                boundary=rn["boundary"],
                is_public=rn["is_public"],
                inbound=inbound[q],
                outbound=outbound[q],
                prod_inbound=prod_inbound[q],
                cls=cls,
                salience=sal,
                betweenness=round(betweenness[q], 4),
                depth=depth[q],
                community=community[q],
                one_liner=rn["one_liner"],
            )
        )

    # role summaries + role-to-role aggregated flow
    role_of = {q: (raw_nodes[q]["role"] or "untagged") for q in qnames}
    role_count: dict[str, int] = defaultdict(int)
    role_doors: dict[str, int] = defaultdict(int)
    role_hubs: dict[str, int] = defaultdict(int)
    for q in qnames:
        r = role_of[q]
        role_count[r] += 1
        if cls_by_q[q] == "door":
            role_doors[r] += 1
        elif cls_by_q[q] == "hub":
            role_hubs[r] += 1
    roles = [
        RoleSummary(role=r, count=c, door_count=role_doors[r], hub_count=role_hubs[r])
        for r, c in sorted(role_count.items(), key=lambda kv: -kv[1])
    ]

    flow: dict[tuple[str, str], int] = defaultdict(int)
    for s, d in edges:
        rs, rd = role_of[s], role_of[d]
        if rs != rd:
            flow[(rs, rd)] += 1
    role_flows = [
        RoleFlow(source=s, target=t, weight=w)
        for (s, t), w in sorted(flow.items(), key=lambda kv: -kv[1])
    ]

    # landmarks for the L1 view: the most salient symbols overall
    landmarks = [
        n.qname
        for n in sorted(nodes, key=lambda n: -n.salience)[:landmark_limit]
    ]

    return SystemModel(
        nodes=nodes, roles=roles, role_flows=role_flows, landmarks=landmarks
    )


def system_model_to_dict(model: SystemModel) -> dict:
    """Serialize a SystemModel to the JSON shape the desktop endpoint returns."""
    return {
        "nodes": [
            {
                "qname": n.qname,
                "name": n.name,
                "kind": n.kind,
                "file_path": n.file_path,
                "role": n.role,
                "boundary": n.boundary,
                "is_public": n.is_public,
                "inbound_count": n.inbound,
                "outbound_count": n.outbound,
                "prod_inbound_count": n.prod_inbound,
                "cls": n.cls,
                "salience": n.salience,
                "betweenness": n.betweenness,
                "depth": n.depth,
                "community": n.community,
                "one_liner": n.one_liner,
            }
            for n in model.nodes
        ],
        "roles": [
            {
                "role": r.role,
                "count": r.count,
                "door_count": r.door_count,
                "hub_count": r.hub_count,
            }
            for r in model.roles
        ],
        "role_flows": [
            {"source": f.source, "target": f.target, "weight": f.weight}
            for f in model.role_flows
        ],
        "landmarks": model.landmarks,
    }
