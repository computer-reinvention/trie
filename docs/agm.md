# Attention Gravity Map (AGM)

The AGM is the **Attention** tab in the desktop app: a live, cognitive-state
visualization of what the agent is paying attention to *right now*, projected
onto the symbol graph. It is deliberately **representative, not accurate** — its
job is to let a human glance for 2–3 seconds and answer *what is the agent
focused on, where did it come from, and where is it heading?* without reading
logs.

This document describes the latest iteration. For the original design and the
core data model, see `docs/visual/attention_gravity_map.md` (PRD) and
`docs/visual/agm_implementation_plan.md`.

---

## Two views, two tabs

The graph area has two permanent tabs:

- **Attention** (`AGMCanvas`) — the live cognitive monitor (this doc). Default.
- **Topology** (`GraphCanvas`, legacy) — the static structural map: roles,
  subsystems, dependency edges, drill-in, search. Still reactive to live agent
  activity. Useful for "how is this codebase structured?" — the questions AGM is
  blind to by design (it only ever shows symbols that have attention).

Both canvases stay mounted so the topology view keeps animating even when
hidden. The old `viz.engine` settings toggle was removed in favour of tabs.

---

## The model: two clocks

AGM separates **what changes** from **how it animates**:

- **Model clock = tool calls.** Attention mass changes only when an agent tool
  call lands (ingest), plus a slow wall-clock decay tick (`MODEL_TICK_MS`, 250ms)
  so cooling symbols drift out smoothly. The model recompute produces a stable
  set of *targets* (where each symbol wants to be).
- **Render clock = frames.** The rAF loop never recomputes the model; it only
  eases drawn nodes toward their targets per the physics laws. Because targets
  are fixed between recomputes, the layout reliably settles to rest.

This split is what eliminated the per-frame "twitching".

### Mass

Two quantities (see `trie/attention.py`, mirrored in `app/src/api/types.ts`):

- **Live mass** — per-event field, continuous `exp` decay with per-event-type
  half-lives (grep 30s, read 3m, trace/write 10m). Drives the visual. Never
  dampened — mass is truthful observation, not judgement.
- **Historical mass** — long-term "how often does cognition return here across
  investigations", stamped in the triefact sentinel (`hist_mass=<v>@<ts>`),
  21-day half-life. Seeds the live field faintly; provides stable geography.

`display_mass = log(raw + 1)` so the field stays readable as mass grows.

---

## The layout: polar, fixed-centre

- The canvas centre is a **fixed crosshair** = the current attention origin
  (0,0). The world deforms around it; the camera never pans or follows. Only
  user zoom (scroll) scales.
- **Radius = relevance.** `radiusForMass` maps display mass to a radius:
  hottest near `R_MIN` (120, clearly outside the crosshair), cold/new at the
  perimeter `R_MAX` (620). As a symbol cools it drifts **outward** — it never
  disappears mid-investigation, it becomes peripheral.
- **Angle = stable geography.** A symbol's bearing comes from its role + a
  stable per-qname hash (`symbolAngle`); historical mass tightens it toward the
  role's core bearing. Angle does **not** change when live mass changes, so a
  symbol keeps its place while only its radius moves.
- **Same-role cohesion.** `applyClusterCohesion` pulls same-role members toward
  their centroid; attraction strength scales with historical mass.
- **Deterministic spread (`spreadTargets`).** Overlapping targets are fanned
  apart by angle in a stable order (by qname), preserving radius. Same inputs →
  same output every frame, so nothing jitters. Pills reserve their measured
  width; dots reserve a tight footprint.
- **Visible budget** (`VISIBLE_BUDGET`, 60). Only the top-N by mass render; the
  rest are dropped from the view (no "+N more" — the map is representative).

---

## Object types by tool intent

Each node tracks its **dominant intent** (the event type contributing the most
current decayed mass, `NodeMass.kind`). Rendering differs by intent:

- **grep hits → small dots.** Faint exploration net, unlabeled. (grep result
  hits are also ingested at 0.25× weight and capped, so a broad grep can't flood
  the field.)
- **read / write(patch) / explain → name pills** — but only if in the top
  percentile (see below).
- **trace → constellations.** Trace events build the attention graph; bright
  violet edges connect traced symbols. Inter-symbol *repository* edges are
  disabled — the only node-to-node lines are trace constellations.

### Percentile naming

Only the **top `PILL_PERCENTILE`** (20%) of visible nodes by mass render as name
pills; everyone else is a dot. A hovered dot temporarily renders as a pill. The
threshold is computed once per model tick so spread and render agree.

---

## Radial spokes

Inter-symbol edges are off. Instead every node draws a **spoke to the centre**,
reinforcing "distance = relevance":

- Opacity scales with relevance: faint symbols → faint spokes (~0.08), hot
  symbols → strong spokes (up to ~0.4).
- The hovered node's spoke highlights (near-white, thicker).

---

## Motion

Everything animates on ease-in-out curves — nothing is ever instant:

- **Entry:** a new symbol spawns at the perimeter (its bearing) with `appear=0`
  and fades + scales in (smoothstep). It travels its journey via smoothstep
  interpolation (slow-start, fast-middle, slow-end).
- **Exit:** when a symbol leaves the target set it eases out to the perimeter
  and fades, then is removed — never a pop.
- **Speed bounds:** `ease` clamps per-frame movement to `[SPEED_FLOOR=1.2,
  SPEED_CEIL=12]` px/frame and snaps within the floor, so motion is calm and
  always settles. `maxDisplay` (the normalization denominator) is eased so a new
  hottest symbol doesn't snap-rescale the whole field.

---

## Interaction

- **Hover** any node → a codelens-style tooltip: a *reason pill* (why it's on the
  map — "found while exploring (grep)", "read by the agent", "traced — part of
  the reasoning path", "edited", "historically attended"), the symbol name ·
  role, its one-liner, live/historical mass, inbound/outbound degree, and the
  full qname. Hit-testing uses a generous radius so small dots are easy to grab.
- **Right-click** any node → the shared symbol context menu (`buildSymbolMenu`),
  also used by the Topology view: open triefact/source, read prose, trace
  callers/callees, show blast radius, mark as ruled out (negative evidence),
  start investigation here, ask agent about this, stage patch / rename / delete,
  copy qname, show attention stats.
- **New / switched session** clears live state (live mass, trail, investigation)
  while keeping historical-mass geography. Launch never replays the persisted
  event log as live mass, so a fresh session starts blank.

---

## Data ingestion

`useOpenCodeSSE.applyAGM` feeds the live engine from the same tool parts the
legacy choreography uses:

- Targets are validated against the loaded graph (`nodesByQname`). Non-symbol
  targets (module paths like `trie/cli.py` from file reads) route to the
  `Filesystem` synthetic node — they never appear as "untagged" floaters.
- grep query → full grep weight; grep hits → 0.25× weight, capped.
- trace chains build the attention graph (filtered to real symbols).
- bash / web / fs tools → synthetic nodes (Filesystem / Bash / Web / …).

Durable capture goes to `.trie/attention.db` via the `record_attention_event`
MCP tool (proxied through the opencode fork's `/desktop/graph/*` routes).

---

## Testing

The engine + layout are pure and headless-tested with Vitest
(`app/src/agm/*.test.ts`): decay/mass math, propagation, investigations,
attention graph, polar layout, deterministic spread, the no-overlap invariant,
visible budget, and behavioural simulations over realistic event sequences.

A simulation harness (`app/scripts/sim/`) renders the real engine over the real
trie graph + recorded `debug.jsonl` telemetry as ASCII frames — a faithful
lower-fidelity preview of on-screen behaviour. See `app/scripts/sim/out/`.
</content>
