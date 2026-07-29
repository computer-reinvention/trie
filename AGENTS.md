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

trie indexes itself. The tool overrides installed for this workdir route
the built-in `grep` and `read` through trie and add the full trie
toolset (`trace`, the explain family, and the patch family) as custom
tools. The tools are self-describing; **read
[`USING_TRIE.md`](USING_TRIE.md) for the concepts, the edit workflow,
and the sharp edges.**

Repo-specific notes that go beyond the general guide:

- **We bootstrap trie with trie.** A session where you reach for shell
  `rg` to answer a code-side question is a session that didn't exercise
  the thing we're building. The `grep` tool handles every search inside
  source — including literal strings and module-level constants, via
  the rg-backed fallback. If a navigation flow feels awkward through
  these tools, that's a signal to fix the tool, not to silently fall
  back to shell grep. Note it in a session summary or open an issue.
- **Edit natively; record intent. Always.** You own code changes; the
  patch pipeline is the intent store. For every touched symbol, stage a
  note with `patch` / `create_symbol` / `batch_patch` (why, not what),
  then `patch_apply -N "<session intent>"` to archive them — apply
  generates no code. The pre-commit `trie intent` gate refuses commits
  with unexplained symbol changes and prints the fix commands.

## What's in scope

- Tests under `tests/` are in scope for documentation by default — they encode behavioural spec worth recording.
- Anything written to `.trie/` is gitignored cache. Safe to delete and regenerate.
- `tmp/` is gitignored scratch space and excluded from `trie verify`. Use it freely for session notes, throwaway scripts, snapshots.

## Bootstrapping loop

trie's own repo has a `trie.toml` at the root. The hook installed by
`trie setup` does the day-to-day work — the commands below are for
bootstrapping a new checkout, one-off operations, and debugging.

```bash
trie init && trie plan                  # plan adds free count_tokens cost preview
trie setup --target opencode            # install MCP + end-of-turn graph-sync hook
trie sync --limit 10                    # capped first-run bootstrap (one-time)
trie sync --file path/to/some.py        # regenerate one file's stale symbols
trie sync --file some.py --force        # full fresh rewrite (LLM smoke test)
trie sync --dry-run                     # preview unified diff before paying
trie sync --graph-only                  # graph rebuild + stamp; never the LLM
trie verify                             # fingerprint-only drift gate
trie lock-check                         # pre-commit's "is a writer running?" probe
trie audit                              # telemetry summary for the last session
```

There is no separate refresh command: `trie sync --graph-only` IS the
graph refresh (the turn hook runs it with `--after-turn`). Once
`trie setup` has registered the hook, prefer letting the hook drive graph
syncs — it fires at the end of every agent turn, picks up exactly the
files just edited, and stamps the graph so MCP queries stay honest. Its
output always reports both clauses ("graph …; prose …"); when it says
prose is stale, a plain `trie sync` regenerates it. Manual `trie sync`
will exit 2 if it collides with an in-flight graph sync; this is the
system telling you the hook is doing its job.

After changing trie's own CLI/hook surface, reinstall the global tool
(`uv tool install --force .`) — hooks resolve `trie` from PATH, and `trie
gate` warns when the installed version lags this checkout.

## Shipping

`scripts/ship.sh "<msg>"` commits, pushes to `origin/main`, and reinstalls the global `uv tool`. It pushes — don't run it casually.

## Git hygiene

- Don't commit `.env`, credentials, or anything under `.trie/` or `tmp/`.
- Commit messages follow `type(scope): subject` — see `git log` for the in-repo style.
- `trie verify` is the pre-commit gate; it refuses commits when the triefact tree drifts.

<!-- trie:docs (added by `trie setup`) -->
**trie is installed in this project.** Read [TRIE.md](TRIE.md) for the navigation tools (`grep`, `read`, `trace`) — use them instead of grep for code search.
<!-- end trie:docs -->
