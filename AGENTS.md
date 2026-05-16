# AGENTS.md

Working conventions for this repository. Read README and QUICKSTART for what trie is and how it's used; this file is just "how we work on it."

## Setup

```bash
uv sync --extra dev                     # editable install with test/lint deps
```

Python 3.11+, `uv` end-to-end. Don't add `pip`, `poetry`, or `setup.py`.

## Running tests and lint

```bash
uv run pytest                                              # full suite
uv run pytest tests/test_cascade.py                        # one file
uv run pytest tests/test_cascade.py::test_some_thing       # one test
uv run ruff check .                                        # lint
uv run ruff format --check .                               # format check
uv run ruff format .                                       # format in place
```

CI runs the same four commands. Tests + ruff must both pass before pushing.

## Coding conventions

- `from __future__ import annotations` at the top of every module.
- Dataclasses are `frozen=True` by default for value types; mutable only with a clear reason.
- Tests mirror the package layout under `tests/`; fixtures under `tests/fixtures/`.
- Use `pytest-mock` for collaborator stubbing — don't introduce `unittest.mock` directly.
- Ruff rules live in `pyproject.toml`. `E501` is ignored (100-char line length, soft). Tests skip `B011`. `cli.py` skips `B008` (Typer defaults).

## Navigating the codebase

trie indexes itself. An MCP server is registered for this workdir (see
`.mcp.json` / `opencode.json` / equivalent), exposing the three navigation tools
trie ships. For structural questions about the code — *where is X defined, what
calls Y, what's the signature of Z, is there already a helper for W* — prefer
these over `grep` and directory walks:

- `locate(predicate, rank_by?, limit?)` — find symbols by `name_contains`,
  `kind`, `scope_prefix` (e.g. `"trie/"` to skip tests), etc. Start here.
- `explain(qname)` — read one symbol's prose plus one-liners for its immediate
  callers and callees. Use after `locate`.
- `walk(from_qname, direction, depth?)` — trace the call graph outward
  (`"callers"` / `"callees"` / `"both"`). Use when one hop isn't enough.

`grep` and direct file reads remain appropriate for literal-string searches
(error messages, TODOs, config keys) and for reading a file once trie has
pointed at it.

We dogfood. If a navigation flow feels awkward through these tools, that's a
signal to fix the tool — not to silently fall back to grep. Note it.

## What's in scope

- Tests under `tests/` are in scope for documentation by default — they encode behavioural spec worth recording.
- Anything written to `.trie/` is gitignored cache. Safe to delete and regenerate.
- `tmp/` is gitignored scratch space and excluded from `trie verify`. Use it freely for session notes, throwaway scripts, snapshots.

## Dogfood loop

trie's own repo has a `trie.toml` at the root. The full loop:

```bash
trie init && trie plan                  # plan adds free count_tokens cost preview
trie sync --file path/to/some.py        # cheapest smoke test of the LLM path
trie sync --limit 10                    # capped first-run bootstrap
trie sync                               # day-to-day incremental cascade
trie sync --dry-run                     # preview unified diff before paying
trie verify                             # fingerprint-only drift gate
trie mcp install --target claude-code   # register the stdio server with an agent
trie mcp serve                          # the server itself; agents spawn this
```

## Shipping

```bash
uv build
uv tool install --force ./dist/trie-0.1.0-py3-none-any.whl
```

`scripts/ship.sh "<msg>"` commits, pushes to `origin/main`, and reinstalls the global `uv tool`. It pushes — don't run it casually.

## Git hygiene

- Don't commit `.env`, credentials, or anything under `.trie/` or `tmp/`.
- Commit messages follow `type(scope): subject` — see `git log` for the in-repo style.
- `trie verify` is the pre-commit gate; it refuses commits when the triefact tree drifts.
