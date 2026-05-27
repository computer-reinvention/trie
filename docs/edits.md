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
regeneration always has the freshest upstream source.

### Ordering algorithm

1. **Build the working set** = {patched symbols} ∪ {neighbours reachable via
   inbound edges within `cascade.default_depth` hops} (same BFS as
   `compute_cascade`).

2. **Build the subgraph**: edges between working-set symbols from the `edges`
   table. Direction: caller → callee.

3. **Contract SCCs** (mutual recursion, re-exports). Symbols in a cycle are
   regenerated in a single LLM call with all their old sources + patches as
   context. No ordering within the cycle.

4. **Topological sort** the DAG of super-nodes: callee before caller.

5. **Apply in that order**:
   - Patched symbols: `infer_source_and_prose(old_source, old_prose, notes, reasons)`
     → writes new_source + new_prose
   - Unpatched neighbours: same call with callee's notes as context
     → writes new_source if call site changed, prose may stay unchanged
   - After each symbol: write source, write triefact section, update
     fingerprint, re-parse for downstream steps

### Cascade context for unpatched neighbours

A neighbour that wasn't patched directly receives the callee's merged notes
as context:

```

Old prose: {neighbour's existing prose}
Notes: {callee's merged notes}
Old source: {neighbour's source span}

```

The LLM sees: "this function's purpose didn't change, but a function it calls
did. Update the call site if needed."

## The apply pipeline (`trie patch --apply`)

```

1. Read all patches from DB, grouped by symbol_id
2. For each patched symbol: merge notes into compact list
3. Compute cascade working set (patched symbols + neighbours within depth)
4. Build DAG, topological sort
5. For each symbol in topological order:
   a. Run infer_source_and_prose()
   b. Validate: compile(new_source) passes
   c. Write new source to disk
   d. Update triefact section: body = new_prose, body_fp = hash(new_prose),
   section fingerprint = sha256(new_source)
   e. Update store: upsert_file + replace_file_symbols + replace_all_edges
   f. Re-read file into parse cache for downstream steps
6. Delete all applied patches from the DB
7. Run trie verify — if it passes, commit. If not, rollback.

````

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
trie patch --drop --session <id>                          # discard patches for one session
trie patch --drop --all                                   # discard everything
```

Existing query tools automatically include patch data:

```
trie read <qname>               # includes "pending_patches" in response
trie grep --name <pattern>      # each hit includes patch count
trie trace <qname>              # nodes with patches are annotated
```

## Risks and mitigations

| Risk                                    | Mitigation                                                                                                                                     |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Source reconstruction produces bad code | `compile()` check after every write; rollback on failure                                                                                       |
| Cascade order wrong                     | SCC contraction + topological sort guarantees order                                                                                            |
| Merge LLM misses a contradiction        | Merge prompt lists all notes chronologically with reasons; no explicit supersession needed because contradictions are rare at this granularity |
| Session interrupted mid-apply           | Git stash is the atomic unit; full rollback on any failure                                                                                     |
| Cascade loop (A patches B, B pulls A)   | SCC contraction merges them into one regeneration unit                                                                                         |
| Hub symbol patched (50+ neighbours)     | Same hub threshold guard as cascade; hubs are depth-0 only                                                                                     |
