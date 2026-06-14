# Attention Gravity Map — Implementation Plan

Status: First pass implemented (branch `agm`) — pending runtime validation
Companion to: [`attention_gravity_map.md`](attention_gravity_map.md) (the PRD)
Scope: trie core (Python) · opencode fork (submodule) · Electron desktop app

## Implementation status (first pass)

All phases 0–5 implemented on the `agm` worktree. Gates: core `uv run pytest`
(792 passing) + `ruff check` clean; app `tsc` clean except 3 pre-existing
`@/lib/sessionTitle` errors unrelated to AGM. Default `viz.engine` is still
`legacy` — AGM ships behind the toggle pending live runtime validation.

### Deviations / discoveries (need review)

1. **Server-side attention capture deferred.** The plan called for recording
   attention in opencode's `mapBusEvent`. That mapper is a pure SSE transform
   with no MCP handle, and a forked background subscriber inside the HTTP
   handler group is the wrong lifecycle home (fragile Effect scoping). Instead,
   attention is captured **client-side** from the app's existing SSE consumer
   (`useOpenCodeSSE` → `applyAGM`), which POSTs to the new
   `/desktop/graph/record-attention` route (durable in `.trie`). Tradeoff:
   attention is only captured while the desktop app is open; CLI-only sessions
   don't record yet (the core `record_attention_event` MCP tool exists and
   could be wired to a turn hook later). The HTTP routes are server-side, so any
   client can record.

2. **opencode `desktop.ts` typecheck is red on its own HEAD.** The
   `feat/trie-native` branch already had 17 `TS2345` errors in `desktop.ts`
   (every existing handler hits an `Unauthorized`/`UnknownError` channel
   mismatch under `tsgo`). The 3 new AGM handlers follow the identical
   established pattern and add 3 more of the same; they are no more broken than
   the 16 existing handlers and the fork builds/runs regardless. Not fixed
   (out of scope; would touch all handlers).

3. **No app test framework.** `app/` has no vitest/jest. The AGM engine modules
   (`agm/*`) are written pure/headless to be unit-testable, but tests are not
   added (introducing a test framework is a separate infra decision). Core
   Python AGM logic is fully tested (`tests/test_attention.py`, 35 tests).

4. **Pre-existing base issues (not AGM):** `app/src/lib/sessionTitle` is
   imported but missing on HEAD (3 tsc errors); `trie_mcp_entry.py` fails
   `ruff format --check`. Left untouched.

5. **Cutover not flipped.** Default stays `legacy`; AGM is opt-in via the
   `viz.engine` setting until validated against the 5s success criterion with a
   live agent session. Tuning (half-lives, propagation, gravity constants) is
   expected after first runtime observation.

This document is the authoritative implementation contract for AGM. Where it
diverges from the PRD, this document wins — the PRD's "universe/weather"
language is treated as an internal mental model only, and several PRD
ambiguities were resolved with the PRD author (see "Resolved ambiguities").

---

## 1. Core thesis

AGM visualizes the **agent's cognitive state projected onto the repository**,
not the repository's structure. The repository graph is substrate; attention is
the signal. A human observer should be able to answer "what is the agent
thinking about?" in under five seconds without reading logs, prompts, or code.

The single most important reframe from the review:

> **Historical mass is not decayed old live mass.** It is a long-term cognitive
> importance signal: *"how often does agent cognition return here across
> investigations?"* Optimize the design around that interpretation.

---

## 2. Foundational concepts and vocabulary

The PRD's bare word "mass" caused confusion. There is **no single "mass."**
Three distinct quantities, each with a different home, cadence, and meaning:

| Quantity | Home | Cadence | Decay | Meaning | Committed? |
| --- | --- | --- | --- | --- | --- |
| **Live mass** | app memory (`agmStore`) | every event, continuous | seconds–minutes (per event type) | the session signal; drives the visual | no |
| **Attention events** | `.trie` SQLite (compressed) | every event | n/a (pruned by recency) | replay buffer; bridges capture → persistence | no (rebuildable) |
| **Historical mass** | triefact sentinel `hist_mass=<v>@<ts>` | only at `trie sync` of that symbol | 21 days | recurrence-across-investigations importance | **yes (source of truth)** |

Supporting concepts:

- **Heat** — the live, decaying field. "Live mass" *is* the heat field; we use
  "live mass" as the canonical term and reserve "heat" for the rendered glow.
- **Repository graph** — possible relationships (typed edges, see §6).
- **Attention graph** — actual reasoning paths the agent took (trace edges
  only); session-scoped; this *is* the trail.
- **Investigation** — a first-class, explicitly-created entity representing a
  user task. The meaningful unit of continuity (NOT turns).
- **Synthetic nodes** — non-code cognition surfaces (`Filesystem`, `Bash`,
  `Web`, `Database`, `Git`).

### Mass mathematics

Live mass is a **per-event field**, not a counter, decayed continuously by
wall-clock time (no frame/tick dependence):

```
live_mass(q, now) = Σ_e [ weight(type_e) · exp(-λ(type_e) · (now − ts_e)) ]
                    for every event e on symbol q
```

```
EVENT_WEIGHTS    = { grep: 10, read: 40, trace: 80, patch: 80 }
LIVE_HALFLIFE    = { grep: 30s, read: 180s, trace: 600s, patch: 600s }
λ(type)          = ln(2) / LIVE_HALFLIFE[type]
HISTORICAL_HALFLIFE = 21 days
```

Both live and historical mass are **logarithmically compressed for display**
(raw values grow unbounded; rendered values must not):

```
display_mass = log(raw_mass + 1)
```

**Mass is never dampened.** No role/test/util/hub coefficient. Mass answers
"how much attention was spent here?" — observation, not judgment. If
`StringUtils` dominates a debugging session, it dominates the map. Correction
for plumbing happens in **propagation, visibility, aggregation, and layout** —
never in mass.

---

## 3. Architecture & boundary rules

Three layers, strict separation. Anything that is data or computation belongs in
**trie core**; the opencode fork is a thin capture + proxy; the app runs the
live simulation and rendering.

```
agent tool call
   │
   ├─(opencode submodule: capture)─► trie core: record_attention_event
   │                                   └─► .trie compressed event store
   │
   └─(opencode SSE /event)─► app: agmStore.ingest ─► LIVE simulation ─► canvas

trie sync (regenerates a symbol's triefact)
   └─► fold attention events ─► hist_mass=<v>@<ts> in the triefact sentinel
                                 (SOURCE OF TRUTH; rebuilds .trie graph DB)
```

Boundary invariants:

1. **trie core** owns: event weights, decay constants, typed edges, the
   attention event store, historical-mass fold, all read endpoints.
2. **opencode submodule** owns: thin HTTP proxy routes + fire-and-forget event
   recording. **No mass math, no weights, no qname inference logic** beyond a
   shared parser. Nothing that belongs in trie lives here.
3. **Electron app** owns: live simulation (live mass, propagation, attention
   graph, investigations, gravity) and rendering.

The `/desktop/graph/*` HTTP routes correctly live in the opencode fork (it owns
the HTTP server; trie speaks MCP over stdio). The pattern for every endpoint:
**add a method to `TrieTools` in trie core, then a thin proxy route in the
opencode desktop handler.**

---

## 4. Resolved ambiguities (authoritative answers)

From the PRD-author review. These override any earlier "ship-fast" decisions.

### Mass & fairness
- The `grep*10 + read*40 + trace*80` formula produces **live mass only**.
  Historical mass never receives direct event increments.
- **No dampening** of utils/tests/hubs in either live or historical mass.
- **Tests are a first-class `Test` role, included by default.** Users may
  filter; the system never silently decides tests don't matter.
- Heavily-used utilities accrue **full** live mass.
- Fairness is a **display** concern (visibility / aggregation / layout /
  propagation), not a mass concern.
- Both masses **saturate via `log(raw+1)`** for display; raw grows unbounded.
- Counts are **decayed** (field model), not cumulative counters.

### Time
- **No tick.** Continuous wall-clock decay via stored timestamps and `exp`.
- Half-lives: live grep 30s / read 3min / trace 10min; historical **21 days**.
- Live mass decays **even while idle**.
- **Turns reset nothing.** Investigations are the only boundaries.

### Roles
- trie's LLM-inferred roles **are** the role layer. Role inference is outside
  AGM; AGM consumes roles.
- **Single-role membership** per symbol (preferred — keeps geography stable).
- Role positions are **fixed geography**, computed once from inter-role
  dependency flow, cached, deterministic. Roles never move and are never hidden.

### Edges & propagation
- Repository graph edge kinds: `calls`, `references`, `imports`, `contains`,
  `inherits`, `implements`, `depends_on`. Attention graph: `trace` only.
  **`depends_on` is deferred** (not derivable from the Python AST without new
  analysis; fabricating it would inject hallucinated topology — violates the
  truthfulness principle). v1 ships the six derivable kinds; the `edges.kind`
  column accommodates `depends_on` later.
- `trace` is both an event (live weight 80) and an attention-edge weight (1.0):
  the trace **event** creates attention **edges** (AuthService → SessionStore).
- Propagation: **one hop, weak (0.15)**. Multi-hop hallucinates attention.
- Propagated heat is **transient only** — it never contributes to historical
  mass.
- The attention graph is **session-only**, never persisted. Historical mass is
  the memory.
- Attention edges carry heat and decay like nodes.

### Investigations
- Created **explicitly from the user task** — never inferred/clustered.
- A new **user task** starts a new investigation. Default: a new user message
  opens an investigation labeled from that prompt; the agent may explicitly
  open/resolve/abandon/supersede via a trie tool (see §5).
- Label: **user prompt first, LLM summary second**, never graph-derived.
- Confidence ∈ [0,1] = **attention concentration** (spread = low, collapsed =
  high). It is a **real clustering layout force**, not decoration.
- **Negative evidence** exists only when the agent **explicitly emits** it
  ("Ruled out AuthService"); never inferred. Subtracts from **live** mass.
- **Multiple investigations** supported architecturally from day one (key by
  `investigation_id`), even if the UI initially shows one.
- Ends on **resolved / abandoned / superseded** — not when the conversation
  ends. First-class entities.

### Visibility / zoom / emergence
- Visibility thresholds are **relative** (to current max live mass), never
  fixed.
- The 20–100 visible cap is **soft** — salience thresholds + hysteresis, no
  flicker.
- Zoom is **manual, always**.
- Cooled symbols **disappear** (prevents junk accumulation).
- Cold **roles never disappear** (geography).

### Trails / camera
- **Trails are attention PATHS, not coordinates** (major PRD correction). Store
  `AuthService → SessionStore → RedisClient`. This is the attention graph.
- Trails persist **across the investigation**, not across sessions.
- The camera is **user-controlled**. The centroid is a layout anchor only; it
  never drives the camera.

### Persistence / replay / multi-agent
- **Replay is required.** Store **compressed** attention events (enough for
  replay, not every raw event forever).
- Historical mass is **cross-session** cognitive memory.
- Key everything by `agent_id`, `session_id`, `investigation_id` from day one
  (multi-agent architecturally ready; single-agent UI for v1).

### Aesthetic / motion
- Universe metaphor is **internal only**. UI reads like an activity map / system
  monitor / topology explorer — **not a planetarium**.
- Heat rendered via **opacity / glow / weight / border** — no rainbow thermals.
- Motion is **restrained**, communicates information, never decorative.
- Layout **never drifts on its own** — moves only when attention changes.

### Lifecycle edge cases
- **Rename**: transfer identity — live mass follows the symbol.
- **Delete**: live mass disappears; historical mass decays away over future
  syncs.
- **Create**: `new.live_mass = creator.live_mass × 0.5` (so new code isn't
  invisible).
- **Active subsystem**: don't force a winner — show top-N active roles.
- **Non-symbol actions** (bash/web/fs/db/git): **synthetic nodes** — omitting
  them makes the visualization systematically misleading.

---

## 5. Implementation phases

### Phase 0 — Contracts
- **`trie/attention.py`** (new): `EVENT_WEIGHTS`, `LIVE_HALFLIFE`,
  `HISTORICAL_HALFLIFE`, `PROPAGATION = 0.15`, repo edge kinds, attention edge
  kind, synthetic-node registry, `AttentionEvent` (frozen dataclass, keyed by
  agent/session/investigation).
- **`app/src/api/types.ts`**: mirror with `liveMass`/`historicalMass` split;
  `AttentionEvent`; `Investigation { id, label, confidence, status, scope,
  negativeEvidence }`; `{ from, to, kind }` edges; `agent_id/session_id/
  investigation_id` keys.

### Phase 1 — Core (trie): typed edges, attention capture, historical mass
- **Typed edges**: add `kind` to `Reference` (`trie/parse/references.py`); tag
  `calls`/`references`/`imports`/`inherits`/`implements`/`contains` at parse
  time (new class-base pass for inherits/implements: ABC/Protocol →
  `implements`, ordinary subclass → `inherits`). Add `kind TEXT NOT NULL
  DEFAULT 'calls'` to the `edges` table (`trie/graph/store.py`);
  `replace_all_edges` writes it; `all_edges` returns it. `depends_on` deferred.
  Requires a clean reindex (`trie sync`) + passing `trie verify`.
- **Compressed attention-event store** (`trie/attention_store.py` or extend
  `trie/activity.py`): `.trie` SQLite, rebuildable. Compression = coalesce
  same-symbol/same-type events within a short window into one weighted event;
  cap event rate. Retention = last ~20 investigations or 7 days (whichever is
  larger), pruned oldest. Keyed by `agent_id/session_id/investigation_id`.
  Helpers: `record_attention_event`, `read_attention_events(since)`,
  `events_by_symbol_since(qname, ts)`, `prune`.
- **Historical mass in triefacts** (`trie/sync/writer.py`): add optional named
  group `hist_mass=<value>@<ts>` to `SECTION_OPEN_RE` **after `role`**
  (backward-compatible field order). `Section.historical_mass` /
  `historical_mass_ts`; renderer emits in fixed order; durable
  `set_section_historical_mass(qname, value, ts)` (minimal diff, mirrors
  `set_section_role`).
- **Sync-time fold** (`trie/sync/` single-file write path): when regenerating
  symbol X,
  ```
  hist = hist · exp(−ln2/21d · Δt)
       + (# of DISTINCT investigations that drew attention to X since last sync)
  ```
  This is the **recurrence** interpretation — count of returning investigations,
  not attention magnitude. Quantize to keep diffs quiet.
- **Graph DB**: `hist_mass` / `hist_mass_ts` columns on `triefact_sections`,
  rehydrated from the sentinel on rebuild (cache, not truth).
- **Synthetic nodes**: an AGM-level registry owned by the attention layer —
  **not** in the `symbols` table (which requires real file/line FKs). They carry
  live + historical mass and join trails, but never the call graph or
  triefacts. Because synthetics have no triefact to stamp, their historical mass
  is reconstructed from the compressed event store on demand and is explicitly
  best-effort — acceptable, since synthetics are session-cognition surfaces, not
  version-controlled code.
- **MCP tools** (`trie/mcp_server.py` `TrieTools`): `record_attention_event`,
  `attention(since)` (returns compressed events + weights + edge kinds + decayed
  historical mass + synthetic nodes), `set_investigation(label, status)`.
  Extend `all_edges` (kind), `system_model`/`all_symbols` (carry decayed
  historical mass for warm first paint; `include_tests=true` for AGM so the
  `Test` role is present).
- Gate: `uv run pytest && uv run ruff check . && uv run ruff format --check .`.

### Phase 1d — opencode submodule (thin capture + proxy)
- `groups/desktop.ts`: add `attention` (GET), `recordAttention` (POST),
  `setInvestigation` (POST) to `DesktopPaths`, schemas, the `.add(...)` chain.
- `handlers/desktop.ts`: thin `callTrieTool` proxies. In `mapBusEvent`, on
  tool-part **completion**, classify the `trie_*` tool → event type, extract
  qnames via a **shared parser** (reused by the app — no duplicated inference),
  classify bash/web/fs/db/git tools → synthetic nodes, and fire-and-forget
  `record_attention_event` keyed by the current `investigation_id`. No mass /
  fold / weight logic here.
- Gate: `bun typecheck` from `opencode/packages/opencode`.

### Phase 2 — App: AGM engine (pure, vitest-tested)
- `agm/weights.ts` — weight/half-life/propagation constants + `display_mass`.
- `agm/attentionModel.ts` — per-event live-mass field, continuous `exp` decay,
  per-type half-lives, `log(raw+1)` display, **no dampening**; live mass seeded
  faintly from historical on open.
- `agm/attentionGraph.ts` — trace events → attention edges (heat decays like
  nodes); this is the trail (paths, not coordinates); scoped to investigation.
- `agm/propagation.ts` — one hop, factor 0.15, over the repo graph; transient
  heat only; never feeds historical.
- `agm/investigations.ts` — explicit lifecycle (open/resolve/abandon/supersede),
  prompt→LLM labels, concentration-confidence as a real clustering force,
  explicit negative evidence, multi-investigation by id.
- `agm/synthetic.ts` — Filesystem/Bash/Web/Database/Git nodes.
- `agm/gravity.ts` — fixed role wells (dependency-flow layout, cached) +
  attention attraction + investigation clustering + repulsion; reaches rest.
- `store/agmStore.ts` — attention-preserving `setModel` (re-key live + historical
  mass by qname across refreshes; rename transfers; delete decays; create
  inherits 0.5×).

### Phase 3 — Greenfield AGM canvas (minimal system-monitor aesthetic)
- `components/AGMCanvas/` — Canvas-2D driven by `gravity.ts` (the sim is the
  layout). Three layers (roles → active symbols → reasoning); relative
  visibility thresholds + hysteresis; cooled symbols disappear; roles always
  visible; manual zoom; layout moves only on attention change; top-N active
  roles (no forced winner); user-controlled camera.
- `agm/style.ts` — reuse the existing palette (`graph/style.ts`); heat as
  opacity/glow/weight/border (no thermal ramp); `ACTIVITY` intent flashes;
  quiet investigation rings; CVD-safe + dash redundancy; restrained motion.
- Toggle `viz.engine: "legacy" | "agm"` in `app/src/settings/schema.ts`.

### Phase 4 — Live wiring, replay, tuning
- SSE → `agmStore.ingest`, keyed by investigation. Three clocks: rAF sim /
  event push / model-refresh (attention-preserving). Hydrate historical mass +
  replay from the compressed event store (investigation-granularity replay wired
  to `ReplayControl`). Sync shimmer from `activity()` poll (distinct from
  cognition heat). Tune half-lives / propagation / concentration to the 5s
  success criterion via a replay harness.

### Phase 5 — Cutover + cleanup
- Default `viz.engine: agm` (keep `legacy` one release). Remove dead deps
  (`@xyflow/react`, `elkjs`, `web-worker`), the `.react-flow__node` CSS rule,
  and unused `SymbolNodeData`/`EdgeData`. Tests: pytest + ruff (core), vitest +
  `bun typecheck` (app), `bun typecheck` (submodule). Update `docs/visual/`.

---

## 6. Edge typing reference (v1)

| Kind | Source (Python AST) | Repo graph | Propagation weight |
| --- | --- | --- | --- |
| `calls` | call expressions, resolved identifiers | yes | 1.0 |
| `inherits` | ordinary base class | yes | 0.9 |
| `implements` | ABC / Protocol base | yes | 0.8 |
| `references` | attribute / name use (non-call) | yes | 0.7 |
| `imports` | import bindings | yes | 0.5 |
| `contains` | enclosing class → method | yes | 0.2 |
| `depends_on` | *(deferred — needs new analysis)* | later | — |
| `trace` | trace **event** creates attention edge | attention only | 1.0 |

---

## 7. Working agreements

- All AGM work happens in a git worktree branch **`agm`** created from the
  current HEAD (`git worktree add -b agm ../trie-agm HEAD`, then
  `git submodule update --init --recursive`, then `uv sync --extra dev`).
- The opencode submodule is a separate repo (branch `dev`, conventional
  commits); its edits are committed/pushed independently of trie.
- Reproducibility constraint: **historical mass must be reconstructable from
  triefacts** (no binary SQLite in version control). `.trie/*` is disposable
  cache, rebuilt like the graph DB.
- Truthfulness constraint: mass reflects observed attention; never infer,
  dampen, or fabricate it. Inference/abstraction (e.g. `depends_on`) is out of
  scope for the visualization layer.

---

## 8. Open items deferred (not v1)

- `depends_on` edge derivation.
- Arbitrary-timestamp replay scrub (v1 replays at investigation granularity).
- Multi-agent UI (data model is ready; UI shows one agent).
- PRD "Future Extensions": shared investigations, time-travel beyond replay,
  attention forecasting, production telemetry overlays, repository evolution
  timelines.
