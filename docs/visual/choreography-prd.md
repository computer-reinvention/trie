# Choreography PRD — the living agent graph

> The desktop graph is a **live performance of the agent's cognition**. Attention
> is light, traversal is flow, edits are heat, cascade is a wavefront. The graph
> canvas, the chat tool-rows, and the patches panel move as one — a single score
> played on three instruments. Grounded in `docs/choreography-deep-research.md`.

Status: spec for implementation. Companion to `docs/graph-view.md` (architecture)
and `docs/cascade-editing-plan.md` (the patch pipeline).

---

## 1. Principles (from the research)

- **Purposeful, not blinking.** Every animation maps to a real agent action on a
  real symbol/edge. Nothing is inferred or decorative-only.
- **Faithful.** We only animate what the agent actually did (real qnames, real
  call edges, real cascade from `compute_cascade`).
- **Governed.** ≤6 concurrently animated elements; the rest dim to a static
  "touched" state. Bursts are staggered (20 ms/item, ≤500 ms total), not blitzed.
- **Lockstep.** One `Conductor` turns events into timed cues that paint all three
  surfaces from a single shared motion state, on one clock.
- **Calm by default, expressive on purpose.** Cinematic default, governed by the
  caps above; `restrained` and `off` are user-selectable.
- **Accessible.** Honor `prefers-reduced-motion` (movement → color/opacity state)
  but never lose the core "what is the agent touching" signal; a setting can
  override the OS when the user wants the full show.

### 1.1 Motion grammar (numbers)

| Token                      | Duration         | Easing                                  |
| -------------------------- | ---------------- | --------------------------------------- |
| Glance pulse (read/scan)   | 90–140 ms        | ease-out `cubic-bezier(0.2,0,0.38,0.9)` |
| Working loop (write/patch) | ~900 ms          | sine ease-in-out (breathing)            |
| Settle to rest             | 250 ms           | ease-out `cubic-bezier(0,0,0.38,0.9)`   |
| Stagger between items      | 20 ms            | — (sequence ≤ 500 ms)                   |
| Comet speed                | ≤ 0.5 link/frame | linear                                  |
| Cascade ring               | 20 ms/hop        | ease-out                                |

Concurrency cap: **6** bright elements; older → static touched ring; keep the
**most-recent N**.

### 1.2 Palette (CVD-safe, redundant cue, soft dark-theme glow)

| State          | Color            | Redundant cue    |
| -------------- | ---------------- | ---------------- |
| read           | `#3b82f6` blue   | solid focus ring |
| scan           | `#2dd4bf` teal   | dashed ring      |
| write          | `#f59e0b` amber  | filled glow      |
| patch (staged) | `#fb923c` orange | dashed ring + ✎  |
| cascade        | `#a78bfa` violet | expanding ripple |
| stale          | `#94a3b8` slate  | dashed, no glow  |
| error          | `#f43f5e` rose   | ✕ badge          |

Glows are tinted (node color), semi-transparent, ~20% desaturated, never pure
white.

---

## 2. The Conductor

`app/src/graph/conductor.ts` — a single frame-driven scheduler.

- **Cue**: `{ id, kind, target (qname|edge|file), color, startAt, duration, easing,
loop?, surfaces: ("graph"|"chat"|"patches")[] }`.
- **Intake**: `useOpenCodeSSE` → `agentChoreography.choreographFor(part)` → emits
  cues to the conductor (never pokes stores directly).
- **Scheduler**: one `requestAnimationFrame` loop advances all active cues,
  enforces the concurrency cap (excess → demote to static), applies staggering
  and decay, and writes **motion state**:
  - `nodes: Map<qname, { state, intensity, ring, glyph }>`
  - `edges: Map<edgeKey, { comets, color, until }>`
  - `ripples: Ripple[]` (origin, hop rings, color)
  - `chevrons: Chevron[]` (off-screen homing)
  - `trail: qname[]` (the agent's path this turn)
- **Consumers**: the graph canvas (`nodeCanvasObject` + overlay), chat tool-rows,
  and patch rows all read motion state for their qname/edge.
- **Timeline**: cues retain their schedule → the turn can be **replayed**.
- **Idle**: `pauseAnimation()` when no active cues and the force sim is at rest.

Reduced-motion transform happens in the conductor: motion cues become instant
color/opacity state; comets/ripples/pans are dropped; trail becomes numbered
breadcrumbs.

---

## 3. Event → motion mapping (lockstep)

Faithful extraction lives in `agentChoreography.choreographFor`. Each row paints
graph + chat tool-row + (where relevant) patch row in the same color/clock.

| Event / tool                                         | Symbols/edges                           | Graph                                                                                   | Chat tool-row      | Patches                                     |
| ---------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------- |
| `trie_read`, `trie_explain_symbol(_references)`      | `sym`/`qname`                           | blue glance pulse + focus; add to trail; comet from previous trail node along real edge | left bar blue, ◐→✓ | —                                           |
| `trie_trace`, `trie_trace_flow`, `trie_explain_flow` | `from`/`symbol1/2` + result edges/paths | blue pulse on targets; **sequential comets** along returned edges                       | blue bar           | —                                           |
| `trie_grep*`                                         | result `hits`                           | teal scan flash on hits (no camera move)                                                | teal bar           | —                                           |
| `trie_patch`                                         | `qname`                                 | orange staged ring; **ghost ripple** of blast radius (pre-fetched)                      | amber bar          | row appears, orange pulse                   |
| `trie_patch_apply` / commit                          | patched + cascade                       | amber write on patched → **violet wavefront** by `hop_by_qname` → green settle          | amber bar          | rows pulse in ring order; ApplyReport lands |
| `write`/`edit`/`str_replace`                         | `path`                                  | amber on file's symbols → stale                                                         | amber bar          | —                                           |
| `file.edited`                                        | `file`                                  | stale tint (skip `triefacts/`)                                                          | —                  | —                                           |
| `permission.asked`                                   | tool callID                             | pulsing ring on the awaiting symbol                                                     | amber prompt row   | —                                           |
| `session.status busy/idle`                           | —                                       | start/cease working loops; idle → settle, keep persistent touched rings                 | running spinner    | —                                           |
| `session.error`                                      | —                                       | rose flash on last active                                                               | rose row           | —                                           |

Persistent: touched nodes keep a static colored ring until the next user message
(`clearTrail` on send).

---

## 4. Signature behaviors

1. **Attention + path.** Current symbol holds a bright focus; prior symbols leave
   a fading **comet-tail trail** along the real edges crossed. Spatial memory of
   the agent's reasoning.
2. **Traversal flow.** `trace`/`flow` fire sequential directional comets
   (≤0.5 link/frame, arrowheads, bundled when dense).
3. **Cascade wavefront.** On apply, a BFS **ripple** expands along real dependency
   edges ordered by `compute_cascade.hop_by_qname` (ring N at `N×20 ms`); each
   cascaded node lights violet → settles applied; patch rows pulse in the same
   order.
4. **Off-screen homing.** Activity off-viewport → a glowing activity-colored
   **chevron at the screen rim** points to it; click to fly there.
5. **Cinematic-calm camera.** Eased follow that moves only when the active target
   drifts toward the edge; `off`/`edge-only`/`cinematic` selectable.
6. **Turn replay.** A transport bar re-plays the turn's choreography from the
   conductor's timeline.

---

## 5. Backend (real cascade)

- `blast_radius(qname)` MCP tool (`trie/mcp_server.py`): resolve qname → file →
  `compute_cascade(changed_files=[file], depth=2)`; return
  `{ qname, direct, cascade:[{qname, hop, file}], cascade_count, hubs_stopped_at }`.
- `/desktop/graph/blast-radius?qname=` desktop endpoint proxies it.
- Frontend `graphClient.blastRadius(qname)`; types replace the placeholder
  `BlastRadius` fields already in `PatchEntry`.

---

## 6. Settings (sensible defaults + configurable)

- `motion.intensity`: `cinematic` (default) | `restrained` | `off`.
- `motion.camera`: `cinematic` | `edge-only` (default) | `off`.
- `motion.reducedMotion`: `auto` (default; honors OS) | `force-on` | `force-off`.
- `motion.replay`: on (default).

Reduced-motion `auto` keeps essential color/opacity state and drops movement; the
core signal survives, satisfying the "override OS if it breaks the core" rule via
`force-off`.

---

## 7. Performance budget (F14–F15)

- Single rAF in the conductor; the force-graph frame callback reads motion state.
- Overlay layer (existing HTML overlay) for comets/ripples/chevrons; integer
  coords; object pooling for particles/ripples; `pauseAnimation()` when idle.
- `centerAt/zoom(…, ms)` for camera tweens. Target 60 fps at ~1.5k nodes / ~2.5k
  edges with ≤6 concurrent animations.

---

## 8. Build order

1. Conductor + motion state + animator easings/palette; route current effects
   through it (no regression).
2. Lockstep painting (graph + chat tool-rows + patch rows).
3. Traversal comets + comet-tail trail.
4. `blast_radius` backend + cascade wavefront (graph ↔ patches).
5. Off-screen chevrons + camera.
6. Reduced-motion + intensity/camera settings.
7. Turn-replay scrubber.
8. Perf pass + acceptance.

---

## 8a. Implemented status (v2)

Shipped: the Conductor store (FX + cue log + governance + path tail), a layered
FX overlay canvas (ripple rings, comet particles, comet-tail path, numbered
breadcrumbs), real hop-ordered cascade wavefront from `compute_cascade`,
off-screen homing chevrons, ambient HUD chip for non-symbol tools, full lockstep
(graph nodes + chat tool-rows + patch rows pulse from node state), redundant
line-style encoding per state + soft-glow primitive, full reduced-motion
compliance, camera modes, far-zoom edge fade, perf gating (overlay repaints only
on change), and the turn-replay transport.

Known follow-ups: fold the activity-cards rAF into the single FX scheduler;
offscreen sprite cache + particle pooling (current scale doesn't need it);
literal ghost-ripple visual on patch stage (currently notes only).

## 9. Acceptance scenarios

- **Explore parallel sync** (grep + read + trace): teal scan flashes on hits →
  blue read pulses with a comet-tail forming the path → off-screen chevron when a
  target is out of view → idle settles to persistent touched rings. Chat tool-rows
  mirror each step's color/status.
- **Add a docstring to `slugify`** (patch → apply): orange staged ring + ghost
  ripple → amber write → **violet cascade wavefront** to callers ordered by hop →
  green settle; patches panel rows pulse in ring order; ApplyReport lands. All
  three surfaces in lockstep.
- **Reduced-motion on**: identical information via color/opacity; zero pans,
  comets, or ripples; trail as numbered breadcrumbs.
