# Edits — prose-first bidirectional workflow

## Concept

The agent never edits source directly during a session. It posts patch notes
against symbols in the graph. The system stores them, surfaces them through
all query tools, and materialises source + prose changes in a single deferred
batch at commit time.

```
session:   trie patch <qname> --note "use gzip instead of brotli" --reason "faster decompression"
           trie grep compress                                  # returns symbol WITH pending patch
           trie read mod/file:compress                         # shows prose + pending notes

commit:    trie patch --apply                                   # one pass, source + prose + cascade
```

## Patch primitive

```bash
trie patch <qname> --note "<implementation change>" --reason "<why the cascade needs to know>"
```

Fire and forget. The patch is stored in the graph DB immediately. The agent
continues — no merge, no queue management, no supersedes.

## Data model

Patches are stored in a new `patches` table linked to symbols:

```sql
CREATE TABLE IF NOT EXISTS patches (
    id INTEGER PRIMARY KEY,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    note TEXT NOT NULL,
    reason TEXT NOT NULL,
    session_id TEXT NOT NULL,
    created_at INTEGER NOT NULL
);
```

`ON DELETE CASCADE` — if a symbol is removed by a rescan, its patches disappear
automatically.

### Mid-session visibility

All query tools surface pending patches without modifying triefacts:

- **`trie read <qname>`** — returns symbol prose + its pending patch notes
- **`trie grep --name <pattern>`** — results carry a `pending_patches: N` count
- **`trie trace <qname>`** — nodes with pending patches are annotated

### Fire and forget semantics

The agent posts a patch and moves on. It does not:

- Track whether the patch was merged with an earlier one
- Worry about supersession
- Re-read the triefact to confirm the change

The system owns the queue. The agent owns the intent.

## Patch merging

Patches on the same symbol accumulate as separate rows. Merging happens once,
at `--apply` time, just before source + prose generation:

```
Input:  notes = ["use gzip instead of brotli", "add streaming fallback"]
        reasons = ["faster decompression", "large payload support"]
Output: merged_notes, merged_reasons
```

The merge prompt:

```
The following patch notes exist for this symbol. Some may contradict or
supersede earlier ones. Return the final list of notes with superseded
entries removed. Preserve chronological order for non-contradictory notes.

Existing notes:
<bullet> {note_1}  — {reason_1}
<bullet> {note_2}  — {reason_2}

Output the final list of bullet points, one per line. Empty list if nothing
remains.
```

The merge does NOT touch `old_prose`. It only compacts the notes list.

### Config

```toml
[edits]
# No config needed for merge strategy — merge is always at --apply time.
```

## Source and prose generation

Both outputs are produced in a single LLM call per symbol:

```
infer_source_and_prose(old_source, old_prose, merged_notes, merged_reasons)
                      → (new_source, new_prose)
```

Inputs:

- `old_source` — the exact source span: `source[start_line-1:end_line]`,
  including decorators and full signature. Available from the parser.
- `old_prose` — the triefact section body at session start (high-level purpose).
- `merged_notes` — compacted list of implementation detail changes.
- `merged_reasons` — one per note, the cascade directive.

Prompt shape:

````
You are updating a Python symbol based on implementation notes.
Output TWO sections: UPDATED_SOURCE and UPDATED_PROSE, separated by
the delimiter "---PROSE---".

Old prose (the symbol's documented purpose):
{old_prose}

Implementation notes (what changed):
{bullet_list}

Old source:
```python
{old_source}
````

UPDATED_SOURCE: update the source to reflect the implementation notes.
Preserve the existing structure as much as possible.

UPDATED_PROSE: write the new triefact body for this symbol that reflects
both the old purpose and the implementation notes. Do NOT include bullet
points or implementation details — the prose is the high-level purpose.
The notes are consumed and discarded.

Output:

```python
<updated source>
```

---PROSE---
<updated prose>

```

### What happens on failure

The `--apply` pass stops at the first failure. All prior writes are reverted.

```

trie patch --apply: symbol `x/y/z:foo` failed source reconstruction
Reason: syntax error at line 5 (expected ':' in function definition)
Pending: 4 symbols, 3 applied, 1 failed — rolled back to pre-apply state

```

## Cascade ordering

The `--apply` pipeline processes symbols in topological order so downstream
regeneration always has the freshest upstream source. Cascade is **reactive**:
only callers of changed callees are considered, and only if the LLM judges
they need updating.

### Cascade pipeline

1. **Working set** = {patched symbols}. Cascade is built lazily via
   `_expand_callers()` — BFS on caller edges from each patched symbol up to
   `cascade.default_depth` hops. Hub symbols (inbound > `trace_hub_threshold`)
   are not expanded further.

2. **Topological sort** of the working set: callee before caller. SCC
   contraction from the earlier design was removed — the cascade model is
   simpler and cycles are rare enough to handle via the single-pass approach.

3. **Parallel execution** via `ThreadPoolExecutor` (concurrency from
   `config.sync.concurrency`). A symbol is submitted when all its callee-
   dependencies are finished. Each worker calls `_process_one()`.

### `_process_one()` — per-symbol pipeline

Each symbol in the working set goes through a single function:

1. **Merge notes**: collect all patches for this symbol (both agent patches
   and cascade notes from callees) and merge via LLM prompt.
2. **Generate source + prose**: `infer_source_and_prose(old_source, old_prose,
   merged_notes, merged_reasons)` → `(new_source, new_prose)`.
3. **Write source** to disk.
4. **Write triefact section**: body = `new_prose`, `body_fp` = hash(new_prose),
   section fingerprint = sha256(new_source).
5. **Re-parse** so downstream steps see the freshest symbol data.
6. **Signature + prose gate**: if `old_signature == new_signature` and
   `hash(old_prose) == hash(new_prose)`, the contract is unchanged and cascade
   is skipped entirely for all callers.
7. **Pre-filter cascade** (if gate didn't skip): call
   `pre_filter_cascade(client, callee_qname, caller_summaries, new_prose)`
   once. The LLM sees all callers simultaneously and returns per-caller
   SKIP or NOTE with implementation note + reason. This replaces the per-caller
   LLM call from the earlier design.

### Pre-filter cascade call

`infer.pre_filter_cascade()` does one LLM call per changed callee (not per
caller). The prompt includes:

- **callee qname** and **new prose** (the updated purpose)
- **signature** and **old one-liner** for each caller
- Each caller's **existing caller-side prose** (what it says about this callee)
  from the triefact section body
- The **cascade.reason** from the implementation note that triggered the change

The LLM returns `"[SKIP]"` for callers that don't need updating, or
`"[NOTE] <implementation note> -- <reason (from cascade)>"` for callers that
do. Callers that need updating get a new "cascade" patch posted to the store
with `session_id="cascade"`.

### Config

```toml
[cascade]
default_depth = 2            # BFS depth for caller expansion
max_judgments = 50           # max pre-filter LLM calls per apply run;
                             # beyond this, remaining unjudged callers
                             # get a conservative blanket note.

[sync]
concurrency = 4               # shared with sync pipeline; also controls
                              # how many patch workers run in parallel
```

### What changed from the earlier design

| Aspect              | Earlier                          | Now                                                        |
|---------------------|----------------------------------|------------------------------------------------------------|
| Cascade direction   | Bidirectional (file-level)       | Caller-edge only (call graph)                              |
| Per-caller decision | Always regenerated               | LLM-gated via `pre_filter_cascade`                         |
| LLM calls per cycle | 1 per caller                     | 1 per changed callee (collapsed)                           |
| Processing          | Sequential topo walk             | Dependency-aware parallel executor                         |
| SCC contraction     | Yes (cycles)                     | Removed (single pass, no fixpoint)                         |
| Merge               | Separate merge step per symbol   | Inline in `_process_one`                                   |

## The apply pipeline (`trie patch --apply`)

```

1. Acquire apply.lock (exclusive — no concurrent applies)
2. Read all patches from DB, grouped by symbol_id
3. Build initial working set = {qnames with patches}
4. Expand via call-graph BFS (_expand_callers): add callers within
   cascade.default_depth hops, stop at hub symbols
5. Topological sort working set: callee before caller
6. Parallel execution (ThreadPoolExecutor, concurrency from config):
   For each symbol in dependency order:
   a. Merge patches (agent + cascade notes from callees)
   b. infer_source_and_prose(old_source, old_prose, notes) → new_source, new_prose
   c. Validate: compile(new_source) passes
   d. Write new source to disk
   e. Update triefact section: body = new_prose, body_fp = hash(new_prose),
      section fingerprint = sha256(new_source)
   f. Re-parse for downstream steps
   g. If contract unchanged (sig + prose hash same): skip cascade
   h. Else: pre_filter_cascade(callers) → cascade notes posted to DB
7. Delete all applied patches from the DB
8. Run trie verify — if it passes, commit. If not, rollback.

```

### Locking

`apply.lock` (flock-based, shares the mechanism from `refresh_lock.py`)
prevents concurrent `--apply` runs. The lock is in `.trie/apply.lock`. If
another apply is in progress, `patch_apply` returns an error immediately.

### Triefact update

The new section body is the LLM's `new_prose` — a coherent rewrite that
subsumes the patch notes. The bullet notes are consumed and discarded.

`body_fp` is recomputed from `new_prose`. The section `fingerprint` is updated
to `sha256(new_source)` so the next `check_project` sees a match.

### What stays the same

- `scan_project()` — unchanged. The re-parse after each write keeps the graph
  up to date for downstream steps.
- `check_project()` — unchanged. Fingerprint comparison still detects drift.
- `verify` / `lock-check` — unchanged.
- Triefact sentinel format — unchanged.
- Cascade BFS algorithm (`compute_cascade`) — reused for neighbour set.

## Rollback

The entire `--apply` pass runs inside a git stash:

```bash
git stash push -m "trie-patch-apply-${session_id}"
for symbol in topological_order:
    validate_and_write(symbol)
if trie verify passes:
    git add -A && git commit -m "feat(edits): batch apply ${N} patches"
else:
    git stash pop  # restores pre-apply state
````

## Required migrations

### Graph store

New `patches` table (schema version 2 → 3 migration):

```sql
CREATE TABLE IF NOT EXISTS patches (
    id INTEGER PRIMARY KEY,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    note TEXT NOT NULL,
    reason TEXT NOT NULL,
    session_id TEXT NOT NULL,
    created_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_patches_symbol ON patches(symbol_id);
CREATE INDEX IF NOT EXISTS idx_patches_session ON patches(session_id);
```

### Query tools

- `Store.get_symbol_detail()` — add `pending_patches: list[dict]` field to
  `SymbolDetail`, populated via `SELECT note, reason FROM patches WHERE symbol_id = ?`
- `Store.grep_symbols()` — add `pending_patch_count` to each hit
- `TrieTools.read()` — include patches in the response envelope
- `TrieTools.grep()` — include patch count per hit

### Config

No config change needed. Merge is always at --apply time.

### Schema version

Bump from 1 to 2. Migration: `CREATE TABLE IF NOT EXISTS patches (...)`.

## CLI surface

```
trie patch <qname> --note "<text>" --reason "<text>"    # fire and forget
trie patch --apply                                        # merge + generate + cascade + commit
trie patch --preview                                      # show what --apply would do
trie patch --list                                         # show all pending patches
trie patch --drop <qname>                                 # discard patches for one symbol
trie patch --drop                                          # discard all patches for this session
trie patch --drop --all                                   # discard everything
```

Existing query tools automatically include patch data:

```
trie read <qname>               # includes "pending_patches" in response
trie grep --name <pattern>      # each hit includes patch count
trie trace <qname>              # nodes with patches are annotated
```

Human-readable CLI output now shows `[patched: N]` tags:

```
trie grep serve
  trie/cli:_run_mcp_serve — ...      [patched: 1]
  trie/mcp_server:build_server — ...
```

## Risks and mitigations

| Risk                                    | Mitigation                                                                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Source reconstruction produces bad code | `compile()` check after every write; rollback on failure                                                                                                                                         |
| Cascade order wrong                     | Topological sort guarantees callee before caller                                                                                                                                                 |
| Merge LLM misses a contradiction        | Merge prompt (within `_process_one`) lists all notes chronologically with reasons; no explicit supersession needed because contradictions are rare at this granularity                           |
| Session interrupted mid-apply           | Git stash is the atomic unit; full rollback on any failure                                                                                                                                       |
| Cascade loop (A patches B, B pulls A)   | Single pass, no fixpoint — if A and B are both patched, topo order ensures the last one processed sees the freshest version of the other; no SCC contraction needed                              |
| Hub symbol patched (50+ neighbours)     | `_expand_callers` stops at hubs (inbound > threshold); `max_judgments` caps pre-filter LLM calls; beyond cap, remaining callers get a conservative blanket note                                  |
| LLM incorrectly skips a caller          | `pre_filter_cascade` sees all callers simultaneously with full context; any caller whose prose references the callee is less likely to be skipped. The cap only triggers on high volume (>50)     |
| Race between apply and refresh hook     | `apply.lock` and `refresh.lock` are independent, named locks; hook's `trie refresh` uses its own lock. No deadlock because the two code paths never wait on each other's lock                   |
