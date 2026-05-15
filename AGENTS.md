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
