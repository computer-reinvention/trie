# Cascade-Based Editing Pipeline — Implementation Plan

## MSP (Minimum Sellable Proposition)

Three axes justify everything in this plan, in priority order. If a feature serves
none, it is cut.

1. **CONTEXT-WINDOW PRESERVATION (the primary win)** — editing by *intent*
   (`patch(qname, note=...)`) instead of by source keeps the agent's context full
   of *reasoning*, not *code*. The old source, the generated new source, and the
   callee/caller bodies needed to get the edit right all live in trie's separate
   generation context — which the agent never sees unless something fails. This is
   the structural equivalent of spawning a sub-agent per symbol: `patch` is a
   structured spawn of a one-symbol editor pre-loaded with callee/caller context;
   `ApplyReport` is its return value; `unresolved[]` is the spawn that needs
   attention. The agent spends its window on planning, not on holding diffs.
2. **EXECUTION SPEED** — the pipeline does in ONE parallel batch what an agent
   would do in N serial edit→read→fix round-trips. Win = wall-clock + token
   throughput.
3. **COGNITIVE OFFLOADING** — the pipeline removes bookkeeping the agent would
   otherwise hold in its head: who is affected (cascade), where each symbol lives
   (qname identity, no line-fumbling), what changed (the report), what still needs
   attention (`unresolved`).

**The hinge condition.** All three wins are conditional on the same property:
per-symbol edit success on par with direct edits, AND failures that land *cleanly*
in `unresolved` (localized to the exact symbol, with a one-call `repatch`). If the
agent must read every generated diff to trust it, the source re-enters its context
and the context-window win (axis 1) evaporates. Therefore the callee/caller context
fed into generation (§9) is not a nice-to-have — it is the mechanism that makes
par-success plausible, and par-success is what makes intent-editing worth more than
direct editing. The two compound: the context that raises success rate is the same
context-gathering work being offloaded.

**Validation path / fallback.** If intent-driven generation does not reach par, the
same `patch`-by-intent interface can be backed by targeted single-symbol `opencode`
instances (one isolated editor per symbol, given the targeted instruction + graph
context). The contract — one symbol, one targeted intent, isolated context, a
structured return — is identical either way, so the surface is worth building
regardless of which backend fulfills it.

Division of responsibility:

- **PIPELINE owns**: speed, parallelism, blast-radius discovery, well-formed output
  (compiling + LSP-clean), atomic hand-off, the change report.
- **AGENT owns**: correctness — does it do the intended thing, does it pass tests,
  does it fit the design. The agent verifies and re-patches. The pipeline never
  judges correctness.

The loop: post patches (declare intent by qname — short instructions, not source)
→ pipeline generates patched + cascade-affected symbols **in parallel**, each in
its own isolated context loaded with callee/caller information, drives each to
compiling/LSP-clean → atomic hand-off via `ApplyReport` → agent verifies → re-patch
the residue → repeat. The agent's context holds intents and the report, never the
source churn.

---

## 1. Ground-truth code facts (load-bearing)

- The current pipeline is **MOSTLY SERIAL**. `merge_notes` is one blocking LLM call
  PER SYMBOL inside a double loop (`apply.py:311`). `pre_filter_batch`
  (`apply.py:280`) and merge (`apply.py:300`) are sequential phases before
  generation. Only the final per-file source gen is parallel (`_process_one_file`
  via `ThreadPoolExecutor`, `apply.py:455`). → Parallelizing the LLM-bound surface
  is the #1 speed lever.
- Two cascade walks: `sync/cascade.py::compute_cascade` (mature: BFS, hop-ranking,
  hub guard, 7 tests) vs `edits/apply.py::_expand_callers` (raw SQL, bare set, 2
  tests). The latter is a strictly-worse subset → delete, unify on the mature one,
  reuse `hop_by_qname` for ordering.
- `apply` writes mid-pipeline (`apply.py:409,427`), LSP-checks the written file
  (`apply.py:413`), verifies dead-last + global (`apply.py:510`), leaves writes on
  verify failure, processes files concurrently (`apply.py:455`). → partial/dirty
  state is the CURRENT default; clean atomic hand-off must replace it.
- `patches.symbol_id NOT NULL REFERENCES symbols(id)`; `add_patch` raises KeyError
  on unknown qname; ~6 consumers assume `symbol_id` exists. → creates need a
  separate table, not a nullable column.
- `scan_project` re-parses every file (`scan.py:62`) + `replace_all_edges` rebuilds
  the WHOLE edge table (`store.py:351`); no incremental update. → re-scan after
  apply is a cost; incremental edge update is a Phase-2 speed win.
- `activity.db` (`activity.py`): proven cross-process ephemeral channel, WAL,
  pid-liveness crash recovery (`:179`), `ActivityProgress`→`ActivityWriter` adapter
  (`:331`). `patch_apply` calls apply WITHOUT progress (`mcp_server.py:375`) →
  frontend shows idle during multi-minute applies.
- Session id minted twice with different semantics: per-server
  (`mcp_server.py:282`) vs per-invocation throwaway (`cli.py:2767`) → CLI
  `--session` drop is broken.
- `preview_patches` exists (`apply.py:587`, pure graph math, no LLM) but is
  CLI-only (`cli.py:2827`) — not exposed to agents. Blast radius is FREE to surface.

---

## 2. SPEED — parallel generation (the headline workstream)

The pipeline's "hyper fast" claim lives or dies here. Today three sequential LLM
phases (cascade pre-filter → per-symbol merge → per-file gen) with only the last
parallel. Target: collapse the LLM-bound surface into maximal concurrency.

- **2.1** Parallelize `merge_notes`. It is per-symbol independent
  (`apply.py:304-320`) but runs serially. Move into the thread pool: all per-symbol
  merges fan out at once.
- **2.2** Keep `pre_filter_batch` batched (already 8/call, `infer.py:226`) but run
  its batches concurrently rather than in a serial loop
  (`infer.py:226 for start in range(...)`).
- **2.3** Single fan-out for generation: patched symbols AND cascade-affected
  symbols are generated in ONE thread pool, not in cascade-then-generate phases.
  The `CascadePlan` (§3) gives the full target set up front, so there is no phase
  barrier between "discover cascade" and "generate."
- **2.4** Bound concurrency by `config.sync.concurrency` (shared knob, already
  exists). Preserve Anthropic prompt-cache warming where a shared prefix exists
  (the `single_file.py:476-488` warm-first-then-fan-out pattern) to avoid N cache
  writes.
- **2.5** Progress is streamed live (see §8) so a long parallel batch is
  observable, not a black box.

**Acceptance**: a 5-file / 12-symbol apply issues its merge + generation LLM calls
concurrently (bounded by `config.sync.concurrency`), not serially. Wall-clock is
dominated by the slowest single symbol's generate, not the sum.

### 2.6 Callee/caller context in generation — the success-rate mechanism

This is what makes the whole MSP defensible (see "hinge condition"). Each symbol's
generation context MUST include:

- the symbol's own current source + prose,
- the **callee** signatures + one-liner prose for everything this symbol calls
  (`store.references_out` → `get_symbol_detail`), so the edit respects the contracts
  it depends on,
- the **caller** signatures + usage prose for everything that calls this symbol
  (`store.references_in`), so the edit respects how its result is consumed,
- the session note (the unifying intent across the batch).

Rationale: the dominant silent-failure mode for a single-symbol LLM edit is a wrong
assumption about a callee's return/accept contract or a caller's usage. Feeding the
graph neighbours directly attacks that failure mode — and it is precisely the
context-gathering work the agent would otherwise do by hand before editing. So the
context that raises edit success rate IS the cognitive work being offloaded; the two
compound. This subsection is a hard requirement, not an optimization: without it,
par-success (and therefore axis 1) does not hold.

### 2.7 Pluggable generation backend (sub-agent / opencode — plug-and-play)

The per-symbol generator is a swappable backend behind ONE interface. This is a
first-class requirement, not a future hook: the MSP's fallback story (§MSP
"Validation path") depends on being able to swap the backend without touching the
pipeline, the cascade, the gates, or the agent surface.

**The interface.** Define a `SymbolEditBackend` protocol — one method, pure per
symbol, no shared mutable state (so the §2 thread pool fans it out safely):

```python
# trie/edits/backends/base.py
@dataclass(frozen=True)
class EditRequest:
    qname: str
    op: str                      # "modify" | "create" | "delete" | "rename"
    old_source: str              # "" for create
    old_prose: str
    merged_notes: list[str]      # the intent (from patches), already merged
    merged_reasons: list[str]
    session_note: str            # unifying batch intent
    callees: list[NeighbourCtx]  # signatures + prose (§2.6)
    callers: list[NeighbourCtx]  # signatures + prose (§2.6)
    file_path: str

@dataclass(frozen=True)
class EditResult:
    qname: str
    new_source: str
    new_prose: str
    ok: bool
    error: str | None = None     # populated on backend-level failure

class SymbolEditBackend(Protocol):
    def generate(self, req: EditRequest) -> EditResult: ...
```

Everything the backend needs is in `EditRequest`; everything the pipeline needs is
in `EditResult`. The gates (compile / LSP / atomic write), the cascade, the report,
and the tool surface are all backend-agnostic — they consume `EditResult`, never the
backend.

**Backend 1 — `InProcessLLMBackend` (default).** Wraps the existing
`infer_source_and_prose` / `infer_file_source` path (`infer.py`). This is what ships
first; it reuses the prompt-cache warming (§2.4) and runs in the §2 thread pool.

**Backend 2 — `OpencodeInstanceBackend` (the fallback / sub-agent backend).** Spawns
a targeted, isolated `opencode` instance per symbol with the `EditRequest` rendered
into a tight single-symbol instruction (the intent + the callee/caller context +
"edit only this symbol, return the new body"). Each instance is its own process with
its own context window — literally the sub-agent model. The pipeline reads the
result (from the instance's structured output / a known file path) back into
`EditResult`. Concurrency is the same thread pool; the per-symbol process isolation
is exactly what keeps the orchestrating agent's context clean.

**Selection.** `config.edits.backend = "llm" | "opencode"` (default `"llm"`),
overridable per-run via `commit(backend=...)` / `--backend`. The factory lives in
`trie/edits/backends/__init__.py::make_backend(config, run_overrides) -> SymbolEditBackend`.
No other code branches on backend — adding a third backend is one class + one enum
value.

**Invariant.** The two backends are interchangeable: same `EditRequest` in, same
`EditResult` out, same gates downstream. A test fixture `FakeBackend` (deterministic
`EditResult`) is the canonical way to test the pipeline without LLM/opencode calls —
and it proves the plug-and-play contract holds.

---

## 3. COGNITIVE OFFLOADING — cascade discovery (so the agent never greps callers)

- **3.1** Unify on `compute_cascade`; DELETE `_expand_callers` (`apply.py:146-176`)
  and its use in `preview_patches` (`apply.py:601`). Reuse `cascaded_qnames`,
  `hop_by_qname`, `file_by_cascaded_qname`, hub guard.
- **3.2** `CascadePlan` (new module `trie/edits/cascade_plan.py`): the full target
  set produced ONCE, up front, so §2.3's single fan-out has everything it needs.

  ```
  CascadePlan{ seeds: set[str], cascaded: list[CascadeNode],
               by_file: dict[str, list[qname]], result: CascadeResult }
  ```

  No mechanical/semantic classifier in v1 — that's a Phase-2 SPEED optimization
  (deterministic propagation skips LLM calls), not a correctness gate.
- **3.3** Second-order cascade (editing B changed B's signature → B's callers) is
  NOT chased in-pipeline; it is reported in `ApplyReport.unresolved` so the agent
  decides. Single sweep keeps the batch bounded and fast.
- **3.4** Edge facts are INFORMATIONAL only — surfaced in the report, never a gate.
  The agent owns whether a missing/changed edge matters.

---

## 4. COGNITIVE OFFLOADING — deterministic identity & blast-radius surfacing

- **4.1** Everything addressed by qname (no line numbers for the agent). Symbol
  spans resolved from the store at apply time (`apply.py:540`), not by the agent.
- **4.2** `patch()` returns the blast radius immediately (free — graph math):
  `{patch_id, qname, pending_patch_count, blast_radius:{direct, cascade,
  cascade_count, hubs_stopped_at}}`. Agent learns the consequence at patch time.
- **4.3** Standalone `blast_radius(qname)` read-only tool (LLM-free) so the agent
  can probe impact WITHOUT staging a patch. Expose `preview_patches`
  (`apply.py:587`) as the `preview()` tool too (today CLI-trapped at `cli.py:2827`).

---

## 5. CLEAN HAND-OFF — well-formed output + atomic apply

The pipeline owns WELL-FORMEDNESS (compiling + LSP-clean), not correctness.

- **5.1** Compile gate: regenerate a non-compiling symbol up to a hard cap; if
  still broken, surface in `ApplyReport.unresolved` with the failed source verbatim.
- **5.2** LSP fixup loop: KEPT (bounded retries, `apply.py:411-429`) so the
  hand-off is lint/type-clean and the agent doesn't waste verification time on
  trivia.
- **5.3** Atomicity (clean hand-off, NOT correctness): stage builds validated
  candidates in memory; LSP runs in a scratch tree (`.trie/scratch/<run-id>/`,
  gitignored — real source tree only ever sees validated bytes); commit writes the
  validated set once, wraps DB mutations in `store.transaction()` (`store.py:211`),
  restores from in-memory before-images on failure. NO persistent journal (subset
  of git; wiped on schema bump). Configurable atomicity: `all_or_nothing`
  (default), `per_item`, `per_group`.

---

## 6. stage / commit topology (minimal round-trips = speed)

No two-phase write protocol. `preview()` = free checkpoint (LLM-free).
`commit(session_note)` = single paid close: stages all pending → parallel generate
→ well-formedness gates → atomic write → `ApplyReport`. One round-trip to apply.

---

## 7. Structural primitives (cognitive offload: agent declares, trie places)

Schema 5→6 (cache regenerable, `store.py:14-17`):

- `patches` gains `kind` (`'modify'|'delete'|'rename'`) + `rename_to`.
  modify/delete/rename target EXISTING symbols → reuse `add_patch`'s symbol_id
  guard.
- create gets a SEPARATE `create_patches` table (no nullable symbol_id threading
  through ~6 consumers): `{target_file, target_qname, anchor_qname, parent_class,
  note, reason, session_id, created_at}`.

Placement: creates ride the EXISTING whole-file rewrite (`infer_file_source`,
`apply.py:391`) by `target_file` — NO stored line anchors (stale after first
insert).

delete: surface live callers (`references_in`) in the report; agent decides.

rename: deterministic where references resolve; REFUSE-on-ambiguity (aliased
imports / getattr / strings) returning the suspicious sites — never silent-corrupt.

---

## 8. State exposure (cognitive offload: agent/frontend see state without asking)

- **8.1** `Store.patch_summary()` shared reader (total_patches, symbol_count,
  by_origin, qnames) — consumed by `patch_list`, `patch_list_cmd`, `status_cmd`.
- **8.2** Live parallel-apply progress → `activity.db` via `ApplyActivityProgress`
  adapting `apply_patches`' progress protocol (`apply.py:196`) into
  `ActivityWriter(op="apply")`. Wrap apply in the SAME lock the refresh hook
  respects (unify lock names).
- **8.3** Wire into: `trie status` (pending + live apply blocks, prose + `--json`);
  `activity()` MCP tool gains an apply sub-object `{phase, done, total,
  session_note}` for the frontend (crash-safe via pid-liveness, `activity.py:179`);
  `patch_list` gains `session_note` + `apply_in_progress`.

---

## 9. Agent interaction surface (cognitive offload: declare intent, get back work)

6 editing tools + `blast_radius`:

1. `patch(qname, note="" | source="", reason="")` — exactly one of `note|source`.
   `source=` bypasses inference (fast deterministic edit). Returns `blast_radius`.
2. `create_symbol(qname, source, file_path="", reason="")`
3. `delete_symbol(qname, reason="")` — returns dependents.
4. `rename_symbol(qname, new_name, reason="")` — returns auto-patched references.
5. `preview() -> {pending, cascade, totals, blockers, ready_to_commit}` — free.
6. `commit(session_note) -> ApplyReport`

- `blast_radius(qname) -> {direct, cascade, cascade_count, hubs_stopped_at}` — free.

**ApplyReport** (the hand-off artifact — agent acts on it without re-querying):

```
{ ok, session_note,
  applied: {symbols, files, files_detail:[{path, ok, symbols, lsp_iterations}]},
  cascade_applied: [{qname, note, origin}],
  unresolved: [{qname, stage:generate|fixup|refresh, code:<enum>, message,
                source_pointer, repatch:{tool, args}}],   # one-call recovery
  totals: {requested, applied, unresolved} }
```

- `code` is an ENUM, never a joined string (kills `apply.py:488,520`).
- `unresolved[].repatch` = ready-to-send call (`note=` for gen-fail;
  `source=<verbatim>` for compile-fail) → residue recovery is one obvious call.
- partial success first-class: `ok:false` + `applied.symbols:N` = "N landed, rest
  need you" → agent continues from residue, no full re-run.

**Error shape**: existing `{error:{code,message,suggestion}}` (`mcp_server.py:108`)
+ a `fix` field = ready-to-replay call with corrected arg (generalizes the
not_found suggestion, `mcp_server.py:304`). `fix:null` = "needs agent decision."

**session_note**: required on commit only when apply spans >1 symbol
(`apply.py:328` already computes total). Reject boilerplate (<12 chars / stoplist)
with a fix that PRE-FILLS a truthful draft synthesized from the pending ops →
honest path is cheap.

**session id**: injectable — `os.environ.get("TRIE_SESSION_ID")` or uuid fallback
(`mcp_server.py:282`); fix the CLI per-invocation bug (`cli.py:2767`). Unblocks the
fork via env injection.

---

## 10. Build order (try-the-pipeline-first; tests alongside each)

1. `ApplyReport` + staged-change-set object (the hand-off contract).
2. Cascade unification on `compute_cascade` (delete `_expand_callers`).
3. **`SymbolEditBackend` protocol + `EditRequest`/`EditResult` + `make_backend`
   factory + `InProcessLLMBackend` (wraps `infer.py`) + `FakeBackend` (tests).**
   The pipeline talks ONLY to the protocol from here on. **[PLUG-AND-PLAY SEAM]**
4. `CascadePlan` + SINGLE-FAN-OUT PARALLEL GENERATION of patched + cascade symbols
   (parallelize `merge_notes` + `pre_filter` batches) + second-order→unresolved.
   Generation calls the backend (step 3), filling `EditRequest` with §2.6 context.
   **[SPEED CORE]**
5. stage/commit + scratch-tree LSP + before-images + `store.transaction()` +
   atomicity + kept LSP fixup loop + compile-retry-to-cap.
6. Schema 5→6 + store API (kind/rename_to, create_patches).
7. Structural lanes: create → delete → rename.
8. Session note gate + injectable session id (fix `cli.py:2767`).
9. State exposure (patch_summary, ApplyActivityProgress, status/activity()/
   patch_list, lock unify).
10. Agent surface (6 tools + blast_radius + preview + ApplyReport.unresolved/repatch
    + fix errors; `commit(backend=...)` / `--backend` override).
11. Surface/docs (rewrite `docs/edits.md` — it over-promises git-stash rollback,
    topo sort, and `compute_cascade` reuse never built; update install templates).
12. Full sweep: `uv run pytest` / `ruff check` / `ruff format --check`.

**Phase 2** (after first trial):

- **`OpencodeInstanceBackend` (the sub-agent / fallback backend)** — one targeted
  `opencode` instance per symbol behind the same `SymbolEditBackend` protocol.
  Because the seam landed in step 3, this is purely a new class + an enum value;
  the pipeline, gates, cascade, report, and tools are untouched. Ship it the moment
  the in-process LLM backend's per-symbol success rate proves below par (§MSP hinge).
- Mechanical-propagation codemod fast path (deterministic AST transform for uniform
  changes; skip the LLM tower for those callers). Can itself be a third backend.
- Incremental per-file edge update (`update_file_edges`) — kill the full-reparse +
  global-edge-rebuild cost (`scan.py:62`, `store.py:351`) on re-scan.

---

## 11. Explicitly deferred / cut

**CUT** (correctness = agent's job, not the pipeline's): intent verification
(deterministic residue + LLM critic), test-execution apply gate, edge-assertion as
a gate (now informational only).

**CUT** (out of scope): all "better than direct edits" usefulness/strategy content,
the hybrid-as-product reframe.

**DEFERRED**: persistent rollback journal, deterministic call-site rewriting (needs
call-expr offsets in the edge table), role-scoped targeting, rich human diff editor,
semantic-cascade fixpoint, the opencode-fork process/language boundary (kept
boundary-agnostic via injectable session id + shared TrieTools core).

**NOT deferred — built as a seam in v1, second impl in Phase 2**: the pluggable
`SymbolEditBackend` (§2.7). The *interface* ships in v1 (step 3) so the default
LLM backend and the Phase-2 `OpencodeInstanceBackend` are plug-and-play; only the
second backend's implementation waits for the first trial's success-rate signal.

---

## 12. Top risks

- Parallel merge/gen must not corrupt shared state: all triefact/store mutation
  stays on the apply thread (the `single_file.py:490-519` plan/generate/apply split
  is the proven pattern); only LLM calls fan out.
- Scratch-tree LSP must resolve imports (hardlink the package, write candidates at
  mirrored paths); validate on a multi-file signature change before relying on it.
- rename refuse-on-ambiguity may false-positive; keep refusal explainable.
- compile-retry-to-cap can burn tokens on a hopeless symbol; cap low, then surface.
- Backend seam leaking: if any pipeline/gate/report/tool code branches on the
  concrete backend, the plug-and-play property is lost. Enforce it with a test that
  runs the full apply against `FakeBackend` — if that passes, no code below the seam
  knows which backend produced the `EditResult`.
- `OpencodeInstanceBackend` per-symbol process spawn cost; bound by the same
  `config.sync.concurrency` pool and reuse the `EditRequest`→instruction rendering
  so the only delta vs the LLM backend is where the text comes from.
