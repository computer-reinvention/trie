# `.trie/` — local state directory

Everything trie writes for a project lives under `.trie/`. The whole directory
is **gitignored and regenerable** — delete it and the next `trie init` + `trie
sync` rebuilds it. Nothing here is a durable artefact; the durable
output of trie is the triefact tree (`triefacts/`, committed) and the source it
describes.

This document is the map of what each file is, who writes it, and when it is
safe to delete.

## Layout

```
.trie/
├── graph.db          # the symbol graph (SQLite) — symbols, edges, sections
├── graph.head        # fingerprint stamp: what the graph was last built from
├── activity.db       # ephemeral live state: writer status + working-tree stale set
└── refresh.lock      # advisory flock held by an in-flight sync
```

## `graph.db` — the symbol graph

SQLite database holding the parsed symbol graph: one row per symbol (qualified
name, kind, file path, line range, signature, visibility), the call/import
edges between them, and the triefact section metadata joined per symbol
(one-liner, role, fingerprints).

- **Written by:** `trie sync` (full or `--graph-only`), bootstrap — anything that
  (re)indexes source or ingests triefacts.
- **Read by:** the MCP navigation tools (`grep`/`read`/`trace`/…) and the CLI
  query commands.
- **Concurrency:** opened with `check_same_thread=False` and guarded by an RLock
  on the hot mutation paths so the parallel sync scheduler's worker threads can
  share one connection.
- **Safe to delete?** Yes. Rebuilt from the committed triefact tree by a
  graph-only sync (no LLM cost) or from source by a full sync.

## `graph.head` — the freshness stamp

A small stamp recording the fingerprint the graph was last built from (git HEAD
+ file fingerprints). `trie verify` and `trie status` compare the current
working tree against this stamp to decide whether the graph has drifted.

- **Written by:** sync at the end of a successful (re)build.
- **Read by:** `trie verify` (pre-commit gate), `trie status`, the graph-sync
  freshness check.
- **Safe to delete?** Yes — the next graph sync re-stamps it. A missing stamp reads
  as "never indexed" and triggers a rebuild.

## `activity.db` — ephemeral live state

See [`trie/activity.py`](../trie/activity.py) for the authority. This SQLite DB
holds **transient runtime state only**, shared across the independent processes
that write to a project (a terminal `trie sync`, the end-of-turn
`trie sync --graph-only`
hook). None of them share memory, so the
live status and the stale set live on disk where any process can read them.

WAL mode lets readers (e.g. `trie status`, the MCP `activity` tool) read
while a writer commits. Three tables:

- **`status`** — a single row describing what the active writer is doing right
  now: `state` (`idle`/`scanning`/`syncing`/`refreshing`/`error`), `op`, `pid`,
  `current_file`, `done`/`total`, `error`. Reset to idle on clean exit.
  **Crash-safe:** a reader cross-checks the row's `pid` for liveness, so a stale
  "running" row left by a killed process reads back as idle.
- **`pending`** — one row per stale source file (the working-tree status),
  written by a graph-only sync and cleared as a full `trie sync` regenerates files.
  A present-but-empty set ("computed, clean") is distinguished from "never
  computed" via a marker in `meta`.
- **`meta`** — small key/value bookkeeping (e.g. the `pending_computed_at`
  marker above).

- **Written by:** `ActivityWriter` (wraps every sync/roles run) and the
  graph-sync path's `write_pending`/`clear_pending`.
- **Read by:** `trie status` and the MCP `activity` tool, which any client can
  poll for live writer status and the "N stale" count.
- **Safe to delete?** Yes — it is purely live state. A missing DB reads as
  "idle, nothing known"; the next writer recreates it.

## `refresh.lock` — the writer lock

An advisory file lock (flock) a sync acquires so two writers don't race
on the graph. `trie lock-check` (used by pre-commit) probes it to answer "is a
writer running right now?". A manual `trie sync` that collides with the
end-of-turn hook exits 2 rather than corrupting state — that exit is the
system telling you the hook is already doing the work.

- **Safe to delete?** Only when no writer is running. The OS releases the flock
  when the holding process exits, so a leftover file from a crash is harmless
  (the lock itself is not held).

## Durable vs. ephemeral — the rule

| Path                | Committed? | Regenerable? | Holds                          |
| ------------------- | ---------- | ------------ | ------------------------------ |
| `triefacts/`        | yes        | via sync ($) | the durable prose + sentinels  |
| `.trie/graph.db`    | no         | yes (free)   | parsed graph                   |
| `.trie/graph.head`  | no         | yes (free)   | freshness stamp                |
| `.trie/activity.db` | no         | yes (free)   | live writer status + stale set |
| `.trie/refresh.lock`| no         | n/a          | advisory writer lock           |
| `debug.jsonl`       | no         | n/a          | durable telemetry (append log) |

If a file is under `.trie/`, it is cache: safe to delete, cheap (or free) to
rebuild. The only paid rebuild is regenerating triefacts themselves via
`trie sync` (LLM calls); everything in `.trie/` is derived from those.
