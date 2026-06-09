# Graph View Redesign — From Dashboard to Monitor

> Research notes for making the Ring 4 desktop graph an intuitive window into
> the codebase, in the spirit of Obsidian's graph view. Status: proposal.

---

## 0. Reframe: the graph is a MODEL of the system, not a map of code

The graph must not render one node per symbol. It is a **representation of the
system** at a chosen level of abstraction. Implications:

- **Default view = the tag/role layer**, not the symbol layer. ~10-15 role
  nodes with aggregated role-to-role flow. You drill down to reveal detail.
- **Not every symbol earns a place.** A _salience_ model decides what is worth
  drawing; trivial helpers and accessors stay hidden until you drill into
  their neighborhood.
- **Some nodes are special**: entry points (system boundaries) and hubs
  (load-bearing cores) are first-class, not just "big dots."

Tagging (shipped) was step one — the first **lens**. The rest of this section
is "what else can we extract from the data to make the model truthful."

### 0.1 Entry points need a RUBRIC, not a degree heuristic

"Entry point" is a **semantic** property (execution crosses into the system
from outside: a user at a CLI, an HTTP client, an agent calling an MCP tool,
the OS), **not a topological one.** The call graph cannot see the
outside-world edge that invokes it. Therefore:

- `inbound == 0` is unreliable — entry points _are_ called by tests and
  scripts, so their inbound is not actually 0; and unresolved calls make
  inbound noisy in general.
- `outbound` is noisy and incomplete — the scanner only captures direct,
  resolved, in-project calls (e.g. `sync_cmd` calls a private helper that
  calls `sync_single_file`; the direct edge to `sync_single_file` is absent).

So no single degree rule works. Use a **multi-signal weighted score**:

| Signal                                                                                                           | Strength            | Source                                                   | Notes                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Framework decorator** (`@app.command`, `@router.get/post`, `@*.route`, `@mcp.tool`, `@click.command`, `@task`) | strongest           | parser (decorators already extracted; NOT yet persisted) | The framework literally declares "outside calls this." Catches every CLI cmd / route cleanly. Validated on trie: every `*_cmd` carries `@app.command("...")`. |
| **`[project.scripts]` / entry_points**                                                                           | ground truth        | `pyproject.toml`                                         | Console entries by definition. trie: `trie = "trie.cli:app"`.                                                                                                 |
| **Production-only inbound == 0**                                                                                 | strong              | edges + caller `file_path`                               | inbound count **excluding callers in `tests/` and `scripts/`**. Directly fixes the "tests call entry points" problem.                                         |
| **LLM `boundary` field**                                                                                         | strong, semantic    | LLM (piggyback on tagging pass)                          | `entry` / `exit` / `internal`. The model reading the source knows intent. Same cost model as `role`.                                                          |
| **Name/convention**                                                                                              | weak, corroborating | name                                                     | `main`, `run`, `serve`, `handle`, `*_cmd`.                                                                                                                    |
| **High outbound**                                                                                                | tiebreaker          | edges                                                    | Orchestrator shape; ranks active doors above bedrock-roots.                                                                                                   |

The score yields **salience**, not a boolean — show the most-certain doors
first, degrade gracefully.

### 0.2 The dual: EXIT points and BEDROCK

The system boundary has two sides:

- **Entry / doors**: outside calls in (above).
- **Exit points**: the system calls _out_ — subprocess, sockets, filesystem,
  the Anthropic client, external APIs. Detectable via the same LLM `boundary`
  field (`exit`) plus structural hints (calls to `subprocess`, `socket`,
  `open`, `requests`, `anthropic`, etc.). Drawing exits makes the model's
  edge with the outside world complete.
- **Bedrock / foundations**: `outbound == 0` with high inbound — the
  most-depended-on primitives (constants, value types, leaf utils). Validated
  on trie: `cli:app` (in=91/out=0), `ModelResult`, `Config.Sync`. These are
  the _floor_ of the system (flows end here). The user's original "low
  outbound" instinct names this real, valuable class — it is the dual of an
  entry point, not an entry point itself.

System reads as a story: **doors → cores → bedrock**, with **exits** where it
reaches outside.

### 0.3 What else we can extract (best with current data)

**FREE — pure graph math on symbols + edges + roles (buildable now):**

1. **Skeleton classification**: every node tagged door / hub / bedrock / exit
   / normal from the rubric above.
2. **Salience score**: weighted blend of production-inbound, outbound,
   betweenness, boundary score, is_public. Drives what shows at each level
   and node size.
3. **Betweenness centrality**: real "traffic routes through me" metric —
   separates true bottlenecks from merely-popular leaves. Instant at ~1.4k
   nodes.
4. **Role-to-role aggregated flow edges**: GROUP BY over edges joined to
   roles. Makes L0 an architecture diagram; exposes layering violations
   (a `persistence -> api` edge is a visible smell).
5. **Connectivity communities** (label propagation / Louvain): clusters that
   actually clump by calls — a third grouping axis distinct from role/folder.
6. **Reachability depth from doors**: BFS from entry points → "how deep into
   the system." Drives a layout where doors sit on the rim, plumbing in the
   core; position gains consistent meaning.
7. **Orphans**: `inbound == 0 && outbound == 0` (production-only) — dead-ish
   code worth surfacing.

**CHEAP — one new signal:**

8. **Churn heat**: `git log` per file → recently/frequently edited symbols
   carry standing "heat." The persistent _monitor_ dimension on top of live
   agent pulses. One git call per file at scan time.

**LATER — LLM pass (like tagging):**

9. **Region labels**: short prose names for clusters ("sync hot path", "LSP
   backend"). Turns the satellite photo into a labeled atlas.
10. **`boundary` field**: fold into the existing tagging LLM call (entry /
    exit / internal) — see 0.1/0.2.

### 0.4 The unifying architecture

**One stable spatial map + levels of abstraction + a salience model + swappable
lenses (role / subsystem / churn / health).** Build the FREE tier as trie-side
`/desktop/graph/*` endpoints (same pattern as tagging) so the frontend
receives an already-meaningful "system model" — every node pre-classified,
pre-scored, grouped, with aggregated flow edges and depth. The frontend is
then purely a renderer of a truthful model.

### 0.5 Required data-layer additions

- **Persist decorators** on `symbols` (parser already extracts them; add a
  `decorators` column; bump SCHEMA_VERSION).
- **Add `boundary`** to the tagging LLM output + `triefact_sections`
  (entry/exit/internal), exactly like `role`.
- **Read `[project.scripts]`** from `pyproject.toml` at scan/summary time.
- New endpoint `GET /desktop/graph/system-model` returning the assembled
  model: roles (with counts), role-flow edges, per-node {salience, class,
  betweenness, depth, community, churn?}, and the landmark set for L1.

## 1. The problem with what we have

The current canvas is a **process-automation dashboard**, not a map of a
system. Concretely, the things that make it feel that way:

- **Nodes are rectangular cards** (220px, kind badge + name + one-liner +
  footer + ↓/↑ counts). Cards read as "rows in a table" or "steps in a
  pipeline." A system map wants _points_, not _forms_.
- **Edges are orthogonal smoothstep connectors** (`getSmoothStepPath`). Right
  angles are the visual language of flowcharts and BPMN diagrams — the exact
  "automation dashboard" cue we want to kill.
- **Layout is a rigid grid** (`gridLayout`, files in columns). Grids say
  "spreadsheet." Spatial meaning is arbitrary — position encodes nothing.
- **Grouping is by file** (FileGroupNode rectangles). Files are a storage
  detail, not how anyone _thinks_ about a system. Boxes-within-boxes is more
  dashboard chrome.
- **Everything is shown at full detail always.** No semantic zoom that
  actually changes what the graph _means_ at different scales.

The result: it looks like something you'd configure, not something you'd
explore.

## 2. What makes Obsidian's graph feel good

Obsidian's graph view is loved despite being _less_ functional than ours
because it nails **form**. The mechanics that produce the feeling:

1. **Dots, not cards.** A node is a small circle. Its label floats beside it
   and only appears when you're zoomed in enough or hovering. Low cognitive
   load; the eye sees structure, not text.
2. **Force-directed layout.** Nodes repel, links pull. Clusters _emerge_
   from connectivity — tightly-coupled things drift together, loners drift
   out. Position becomes meaningful for free. It also _breathes_: the gentle
   settling motion makes it feel alive, not static.
3. **Size encodes importance.** Node radius scales with degree (number of
   links). Hubs are visibly big; leaves are small. You read architecture at a
   glance.
4. **Color encodes category.** Obsidian colors by tag/folder/query. This is
   exactly our **role tags** — `api`, `domain`, `persistence`, etc. Color is
   the single most powerful "what kind of thing is this" channel.
5. **Hover reveals local structure.** Hovering a node highlights it and its
   direct neighbors and **dims everything else.** This is the killer
   interaction: instant "what touches this?" without losing the whole-system
   context.
6. **Curved links.** Slight curvature (bezier), not right angles. Organic,
   not engineered.
7. **Smooth zoom + pan as the primary verb.** You _fly through_ the space.
   Click-to-focus centers and zooms on a node.

None of these are about showing more data. They're about showing the _same_
data as a **landscape you navigate** rather than a **form you read**.

## 3. The core recommendation: switch the renderer

React Flow is a **node-based editor** framework — built for flowcharts,
pipelines, and DOM-rich nodes you wire together. It is structurally biased
toward the dashboard look, and rendering 1,379 content-rich DOM nodes is
heavy. We are fighting the tool.

**Recommendation: render the graph on a canvas with a force simulation,
using `react-force-graph-2d`** (the React wrapper around `vasturiano`'s
`force-graph`, which is the same family of tooling Obsidian-style views are
built on — canvas + `d3-force`).

Why this specific library:

- It gives us _every_ Obsidian behavior natively, no reinvention:
  - `nodeAutoColorBy('role')` → color clusters by our role tags
  - `nodeVal` (size by degree) → hubs visibly larger
  - `onNodeHover` + neighbor sets → highlight-and-dim (§2.5)
  - `linkCurvature` → curved links (§2.6)
  - `linkDirectionalParticles` → **dots that flow along a link** — this is
    our agent-activity channel (see §5)
  - `centerAt` + `zoom` → click-to-focus
  - `nodeCanvasObject` with `globalScale` → labels that fade in as you zoom
- Canvas scales to thousands of nodes at 60fps; our ~1.4k symbols / ~2.5k
  edges is squarely in its comfort zone (Obsidian routinely does more).
- `d3-force` is the actual engine; we can tune `forceManyBody` (repulsion),
  `forceLink` (ideal edge length), and `forceCollide` (no overlap).

Trade-off: we lose React Flow's DOM nodes (the expandable prose panel inside
a node). That's fine — prose belongs in a **side inspector panel**, not
crammed into a node on the canvas. Clicking a node opens the inspector; the
canvas stays a clean map. This is also more Obsidian-like (the note opens in
a pane; the graph stays a graph).

### Alternative considered: keep React Flow, add d3-force

We _could_ keep React Flow and drive `node.position` from a `d3-force`
simulation (React Flow + d3-force is a documented pattern). This avoids a
renderer swap and keeps DOM nodes. But it does **not** fix the root feel: the
nodes are still cards, performance with 1.4k live-simulated DOM nodes is
rough, and we'd still hand-build hover-dimming, particles, and zoom-fade.
It's more work for a worse result. Recommend against unless we have a hard
reason to keep DOM nodes.

## 4. Grouping by role (not file)

We just shipped LLM-inferred role tags. They become the **primary organizing
principle**:

- **Color** every node by `role` (stable hue per role; shared legend).
- **Cluster** by role via a weak `forceX`/`forceY` per-role centroid, OR a
  `forceCluster`-style custom force, so same-role nodes gravitate together
  _without_ hard rectangular containers. Clusters are felt, not boxed.
- **Legend / filter rail**: a small overlay listing roles with their colors.
  Clicking a role isolates it (dims all other roles) — the Obsidian
  "tag filter" interaction. This answers "show me the persistence layer"
  instantly.
- No `FileGroupNode` rectangles. File is demoted to metadata shown in the
  inspector and as a secondary grouping option in a dropdown
  (Group by: ▸ Role / File / None).

This makes the graph answer _architectural_ questions ("what are the layers,
how big is each, what crosses between them") instead of _filesystem_
questions.

## 5. The graph as a live monitor (the part that matters most)

The ask: "display stuff as it is touched / modified" — an intuitive monitor
of the system _and the changes_. The force-graph particle + highlight system
is purpose-built for this. Map agent activity (we already get it over the
`/desktop/event` SSE stream) onto canvas affordances:

| Agent action (SSE)                  | Canvas response                                                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `trie_read` / `trie_trace` a symbol | Node **pulses** (radius + glow ease up and back); a soft ring lingers briefly. "The agent is looking here."                      |
| Traversal (`trace` returns edges)   | **Directional particles** fire along those exact links, in sequence — you literally watch attention flow through the call graph. |
| `write_file` / patch on a symbol    | Node flares **amber** and grows; stays enlarged while "hot."                                                                     |
| File edited (`file.edited`)         | Node tinted **stale** until refresh; a subtle decay animation.                                                                   |
| Idle                                | Everything settles back to rest size/color.                                                                                      |

Because the layout is force-directed and _persistent_, the user builds a
mental map of where things live — so when a node lights up across the canvas,
they know _where_ in the system the agent just went, without reading a label.
That spatial memory is the whole point of a monitor vs. a log. The current
turn-history panel becomes the textual ledger; the graph becomes the
**ambient, spatial** view of the same events.

Particles are the single highest-leverage feature here: a dot traveling from
A→B along a curved link is the most legible possible representation of "the
agent moved from A to B," and it's one line of config.

## 6. Semantic zoom that changes meaning

Three regimes, driven by `globalScale` in `nodeCanvasObject`:

- **Far (whole system):** dots only, sized by degree, colored by role. No
  labels. You see the _shape_ of the codebase and its layers. Role clusters
  are obvious.
- **Mid:** labels fade in for hubs (high-degree nodes) only. You see the
  landmarks.
- **Near:** labels for everything; hover shows the one-liner as a tooltip.
  Click opens the inspector with full prose (from `/desktop/graph/read`).

This is "less is more" — the graph is _quietest_ when zoomed out, which is
when you want to read structure, and most detailed only where you're looking.

## 7. Concrete component plan

```
GraphCanvas/
  index.tsx              ← swap ReactFlow for <ForceGraph2D>
  useForceGraphData.ts   ← map store nodes/edges → {nodes:[{id,role,val,...}],
                            links:[{source,target}]}; build neighbor sets
  useAgentActivity.ts    ← subscribe to agentStore; drive pulses + particles
  paint.ts               ← nodeCanvasObject / linkCanvasObject (role color,
                            degree size, zoom-fade labels, highlight ring)
  RoleLegend.tsx         ← overlay; color swatches; click-to-isolate
  Inspector.tsx          ← side panel: prose, signature, file:line, neighbors
                            (replaces the in-node expanded panel)
```

State changes:

- `graphStore`: keep nodes/edges as data (drop React Flow `position` — the
  sim owns positions now). Add `role` to node data (already on the wire).
  Add `hoveredQname`, `isolatedRole`, and a derived neighbor index.
- `agentStore`: already has the turn event stream we need; add a small
  "active qnames + recently-traversed edges" slice the canvas can read for
  pulses/particles.

Data we already have (no backend work needed):

- `role` on every symbol (just shipped).
- `inbound_count` / `outbound_count` → node size (degree).
- `all-edges` endpoint → links.
- `/desktop/event` SSE → live activity.

## 8. Suggested build order

1. **Renderer swap + force layout + color-by-role + size-by-degree.** Static
   graph that already _looks_ right. Biggest perceptual win, lowest risk.
2. **Hover-highlight-and-dim + curved links + zoom-fade labels.** The
   Obsidian "feel."
3. **Inspector panel** (click → prose) replacing in-node prose.
4. **Live monitor**: pulses on read, particles on traverse, amber on write.
5. **Role legend + isolate-by-role filter.**
6. **Polish**: settling animation tuning, click-to-focus, mini-map (optional;
   force-graph has none built in — skip unless asked).

Steps 1–2 alone convert the feel from dashboard to map. Step 4 is the
"monitor" payoff.

## 9. Open questions for product

- **Node identity at far zoom:** dots-only, or always show labels for the top
  N hubs? (Recommend dots-only far, hub-labels mid.)
- **Do we keep file grouping at all** as a toggle, or go role-only? (Recommend
  toggle, role default.)
- **Edge density:** 2,524 edges may be visually noisy at full-system zoom.
  Option: hide edges below a zoom threshold and show only role-to-role
  aggregate flows when zoomed out. (Recommend: fade edges out at far zoom.)

```

```
