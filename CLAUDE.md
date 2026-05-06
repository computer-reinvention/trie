# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What trie is

trie generates a Markdown "triefact" file per source file, kept in a tree (`triefacts/`) that mirrors the source tree. A reference-graph cascade regenerates dependent triefacts when a referenced symbol changes; a fingerprint-based `trie sync --check` runs as a pre-commit gate to refuse merges when the tree drifts. An MCP server (`trie mcp serve`, registered via `trie mcp install`) exposes the tree to coding agents.

The README and QUICKSTART describe the user-facing model in detail; read them when the task is about behavior or UX. This file covers what's not derivable from those.

## Common commands

```bash
# Dev install (editable, with test/lint deps)
uv sync --extra dev

# Run the full test suite (233 tests as of v0.2.0)
uv run pytest

# Run one test file / one test
uv run pytest tests/test_cascade.py
uv run pytest tests/test_cascade.py::test_hub_threshold_caps_expansion

# Lint + import-sort check (CI-equivalent)
uv run ruff check .
uv run ruff format --check .

# Build wheel + install globally as a uv tool
uv build
uv tool install --force ./dist/trie-0.1.0-py3-none-any.whl

# End-to-end dogfood loop (in another project's directory)
trie init && trie plan                  # init runs scan; plan adds free count_tokens cost preview
trie sync --file path/to/some.py        # cheapest smoke test of the LLM path
trie sync --limit 10                    # auto-detected first-run bootstrap, capped
trie sync                               # day-to-day incremental cascade
trie sync --dry-run                     # preview unified diff before paying
trie sync --check                       # fingerprint-only drift gate; pre-commit entry
trie mcp install --target claude-code   # register the stdio server with an agent
trie mcp serve                          # the server itself; agents spawn this
```

`scripts/ship.sh "<msg>"` commits, pushes to `origin/main`, and reinstalls the global `uv tool` from git. Don't run it casually — it pushes.

## Architecture

The pipeline has three layers. Understanding which layer a task belongs to is the fastest way to find the right files:

**1. Parse + graph (offline, no LLM)** — `trie/parse/`, `trie/graph/store.py`, `trie/scan.py`

`parse/python.py` extracts `Symbol`s from a source file via tree-sitter. Each symbol carries a `body_normalized_hash` (whitespace/comment-stripped SHA-256) — that hash is the *fingerprint* the rest of the system pivots on. `parse/references.py` produces edges with a `confidence` field (`tree_sitter_import` | `name_match`). The confidence field exists so SCIP-precision edges can land in v0.2 alongside heuristics without breaking the cascade contract — preserve it.

`graph/store.py` is a SQLite-backed store (`<root>/.trie/graph.db`) with three live tables: `files`, `symbols`, `edges`, plus `triefact_sections` for fingerprint lookups. Schema is created on connect via `SCHEMA_SQL`. There's no migration tooling yet — bump `SCHEMA_VERSION` and add an idempotent `CREATE` rather than altering existing tables.

`scan_project` is the entry point: walk scope globs, hash files, re-parse only changed ones, upsert symbols + edges, garbage-collect dead rows.

**2. Generation (LLM-touching)** — `trie/sync/`, `trie/models.py`, `trie/cost.py`

`sync/single_file.py` is the leaf: build prompt, call the model, write the triefact. `sync/writer.py` parses and reassembles a triefact's section sentinels (`<!-- trie:section symbol=... fingerprint=... -->` / `<!-- trie:end -->`) — anything *outside* sentinels is human prose and is preserved byte-for-byte. Don't refactor the writer without preserving that contract; it's the load-bearing promise to users.

Three top-level sync modes wrap `sync_single_file`:
- `sync/bootstrap.py` — rank scope by `LOC × public_symbol_count`, run under `--budget` / `--limit`
- `sync/incremental.py` — default `trie sync`: scan → reconcile orphans → `check_project` for stale → `compute_cascade` → sync affected files
- `sync/cascade.py` — pure graph traversal: walk inbound edges from changed symbols up to `cascade.default_depth`, skipping symbols with more than `cascade.hub_symbol_threshold` inbound refs (the hub guard against `utils.py` invalidating the world)

`models.py` is the provider abstraction. v0.1 has only `AnthropicClient` (Anthropic's prompt-cache headers are wired into the `_payload` shape — `cached_context` is a separately-cached block). The `count_tokens` path has a known gotcha: Anthropic rejects empty text blocks, so `build_plan` passes `request=""` to size just the cached prefix and the payload builder must skip the empty block. An OpenAI-compatible client lands in v0.2 — keep `ModelClient` (Protocol) the contract.

`cost.py` carries per-model pricing tables for estimation and reconciliation.

**3. Verification + surfaces (offline)** — `trie/check.py`, `trie/diff_cmd.py`, `trie/mcp_server.py`, `trie/cli.py`

`check.py` is the pre-commit invariant: deterministic, no LLM, no DB writes. It re-fingerprints each in-scope source symbol and compares against the fingerprint stored in the matching triefact section sentinel. Four `StaleReason` outcomes drive the CLI exit code — keep them exhaustive.

`mcp_server.py` exposes four read-only tools over **stdio only** (HTTP transport deferred to v0.2 by deliberate decision — no auth/CORS surface): `get_triefact`, `find_symbol`, `references_to`, `references_from`. Read-only by design — only `trie sync` writes triefacts. Never log to stdout from the MCP path; it corrupts the JSON-RPC stream (`_run_mcp_serve` in cli.py routes errors to stderr for this reason).

`cli.py` is a Typer app with a nested `mcp` sub-app (`mcp_app`). Each subcommand resolves config via `Config.find_and_load` (walks up to find `trie.toml`) — the directory containing `trie.toml` is the project root and the anchor for all relative paths.

## Locked design decisions

These were settled in the v0.1 design pass. Don't relitigate without a user prompt:

- **License: MIT** (not Apache-2.0).
- **Default model: `anthropic/claude-sonnet-4-6`** for both bootstrap and cascade. Cost story works at Sonnet pricing. Cheaper providers swap via config (`[models].bootstrap = "openai/..."`); the OpenAI-compatible client itself lands in v0.2.
- **MCP transport: stdio only** in v0.1.
- **References: tree-sitter heuristic** (`tree_sitter_import` + same-module `name_match`), not SCIP. The `confidence` field on every edge is the seam SCIP will land through. SCIP precision is the top v0.2 priority.
- **Cascade defaults: depth 1, hub threshold 20.** Configurable per-project in `trie.toml`.
- **Dogfood target is an external small Python library**, NOT trie's own repo (avoids the recursion failure mode where breaking trie corrupts trie's own triefacts).
- **Tests are in scope by default** — they encode behavioral spec worth documenting.

## Conventions worth knowing

- Python 3.11+, tooling is `uv` end-to-end. Don't add `pip` / `poetry` / `setup.py`.
- `ruff` rules in `pyproject.toml`: `E F I B UP RUF SIM`, line length 100, `E501` ignored. Tests skip `B011`. `cli.py` skips `B008` (Typer's `Argument`/`Option` defaults are the canonical pattern).
- `from __future__ import annotations` at the top of every module — keep type hints lazy.
- Dataclasses are `frozen=True` by default for value types; mutable only when there's a clear reason.
- Tests live under `tests/` mirroring the package; fixtures under `tests/fixtures/`. Use `pytest-mock` for collaborator stubbing (already a dev dep) — don't introduce `unittest.mock` directly.
- Anything written to `.trie/` is gitignored cache — safe to delete and regenerate.
