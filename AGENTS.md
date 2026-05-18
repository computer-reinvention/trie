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
`.mcp.json` / `opencode.json` / equivalent), exposing three navigation
tools: `locate`, `explain`, and `walk`. **Read [`USING_TRIE.md`](USING_TRIE.md)
for the full usage guide.**

One repo-specific note that goes beyond the general guide:

- **We dogfood.** A session where you reach for `grep` to answer a
  code-side question is a session that didn't exercise the thing we're
  building. `locate` handles every search inside source — including
  literal strings and module-level constants, via the rg-backed
  fallback. If a navigation flow feels awkward through these tools,
  that's a signal to fix the tool, not to silently fall back to grep.
  Note it in a session summary or open an issue.

## What's in scope

- Tests under `tests/` are in scope for documentation by default — they encode behavioural spec worth recording.
- Anything written to `.trie/` is gitignored cache. Safe to delete and regenerate.
- `tmp/` is gitignored scratch space and excluded from `trie verify`. Use it freely for session notes, throwaway scripts, snapshots.

## Dogfood loop

trie's own repo has a `trie.toml` at the root. The hook installed by
`trie setup` does the day-to-day work — the commands below are for
bootstrapping a new checkout, one-off operations, and debugging.

```bash
trie init && trie plan                  # plan adds free count_tokens cost preview
trie setup --target opencode            # install MCP + end-of-turn refresh hook
trie sync --limit 10                    # capped first-run bootstrap (one-time)
trie sync --file path/to/some.py        # smoke-test the LLM path on one file
trie sync --dry-run                     # preview unified diff before paying
trie refresh                            # manual refresh (hook also calls this)
trie verify                             # fingerprint-only drift gate
trie lock-check                         # pre-commit's "is a writer running?" probe
trie audit                              # telemetry summary for the last session
```

Once `trie setup` has registered the hook, prefer letting the hook drive
syncs — it runs `trie refresh` at the end of every agent turn, picks up
exactly the files just edited, and stamps the graph so MCP queries stay
honest. Manual `trie sync` is still available but will exit 2 if it
collides with an in-flight refresh; this is the system telling you the
hook is doing its job.

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


<!-- trie:docs (added by `trie setup`) -->
**trie is installed in this project.** Read [TRIE.md](TRIE.md) for the navigation tools (`trie_grep`, `trie_read`, `trie_trace`) — use them instead of grep for code search.
<!-- end trie:docs -->
