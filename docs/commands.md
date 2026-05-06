# trie command reference

Every `trie` subcommand and flag, what it does, and when to reach for it.

## Global flags

| Flag | Effect |
| --- | --- |
| `--version` | Print the installed trie version and exit. |
| `--quiet`, `-q` | **Mute** mode — errors only. |
| `--verbose`, `-v` | **Chatty** mode — per-symbol detail and token / cache breakdowns. |
| `--help` | Show help. Accepted on every subcommand. |

Default verbosity (no flag) is **medium**: per-file progress with a running ETA, no token noise.

`--quiet` and `--verbose` are mutually exclusive.

All commands except `trie init` resolve their config by walking up from the current directory to find `trie.toml`. The directory containing `trie.toml` is the project root and the anchor for every relative path.

## Top-level commands at a glance

| Command | Networked? | What it does |
| --- | --- | --- |
| `trie init` | no | Set up trie in a Python project. Runs scan, optionally installs pre-commit hook. |
| `trie plan` | yes (free) | Scan + cost preview. Uses `count_tokens`, never `messages.create`. |
| `trie sync` | yes (paid) | Generate or refresh triefacts. Auto-detects bootstrap vs incremental. |
| `trie mcp install` | no | Register the trie MCP server with one or more coding agents. |
| `trie mcp serve` | no | Stdio MCP server. Hidden — agents spawn this via the snippet `install` writes. |

---

## `trie init`

Create `trie.toml`, add `.trie/` to `.gitignore`, build the initial symbol graph, and (optionally) install a pre-commit hook.

```
trie init [PATH] [--force] [--install-hooks/--no-install-hooks] [--scan/--no-scan]
```

| Argument / option | Default | Description |
| --- | --- | --- |
| `PATH` (positional) | current directory | Project root to initialise. |
| `--force`, `-f` | `false` | Overwrite `trie.toml` if it exists, and skip Python-project detection. |
| `--install-hooks` / `--no-install-hooks` | prompt in tty, else off | Tri-state. Default prompts interactively; `--install-hooks` forces on; `--no-install-hooks` forces off. |
| `--scan` / `--no-scan` | `--scan` | Build the symbol graph in `.trie/graph.db` immediately after writing config. |

Behavior:

- Refuses to run unless a Python-project marker (`pyproject.toml`, `setup.py`, etc.) is present, unless `--force` is passed.
- Writes `trie.toml` with default scope, model, and cascade settings.
- Appends `.trie/` to `.gitignore` (or creates the file). Skipped if already present.
- Runs `scan_project` so you can immediately call `trie plan` or `trie sync`.
- Hook installation:
  - If `.pre-commit-config.yaml` exists → prints a snippet for you to add manually (we don't auto-edit your YAML).
  - Else if `.git/` is present → writes a marker-fenced block to `.git/hooks/pre-commit` (idempotent).
  - Else → skips with a note that this isn't a git repo.

Exit codes: `0` on success, `1` on init error.

---

## `trie plan`

Scan the project, then show the worklist and estimated cost.

```
trie plan [--model MODEL]
```

| Option | Default | Description |
| --- | --- | --- |
| `--model` | `[models].bootstrap` | Override the model used for the cost estimate. |

Networked but cheap: uses Anthropic's free `count_tokens` per file, never `messages.create`. Run before `trie sync` if you want to see the bill before paying it.

Output: scan breakdown (new / updated / unchanged / removed), plan header (`N files, ~$X estimated`), top-10 ranked files with `(symbols, score, ~$cost)`, and a "… and N more" tail if the worklist is longer.

---

## `trie sync`

Generate or refresh trie triefacts. Several modes; the default auto-detects.

```
trie sync [--file PATH] [--check] [--all] [--dry-run]
          [--budget USD] [--limit N] [--model MODEL]
```

| Option | Default | Description |
| --- | --- | --- |
| `--file PATH`, `-f` | — | Sync exactly one source file (smoke test of the LLM path). |
| `--check`, `-c` | `false` | Offline drift check. Exits 1 if any triefact is stale. No LLM, no scan. **Replaces v0.1 `trie check`.** |
| `--all` | `false` | Force a full re-pass over every file in scope, even when triefacts already exist. |
| `--dry-run` | `false` | Regenerate stale triefacts into `.trie/preview/` and print a unified diff against the live tree. **Replaces v0.1 `trie diff`.** |
| `--budget USD` | — | Cumulative actual-cost cap. Stops once reached (overshoots by at most one file). |
| `--limit N` | — | Cap on the number of files synced. |
| `--model MODEL` | bootstrap → `[models].bootstrap`; incremental → `[models].cascade` | Override the model. |

### Mode dispatch

The flags select the mode in this priority order:

1. **`--check`** → offline drift check; exits 1 on drift.
2. **`--file`** → single-file sync.
3. **`--dry-run`** → diff preview into `.trie/preview/`.
4. Else **auto-detect**:
   - If `--all` or no `triefacts/` directory exists yet → **bootstrap** (full pass).
   - Otherwise → **incremental cascade**.

### Per-mode behavior

**Single file (`--file`)**: cheapest LLM smoke test. Streams a one-line summary of symbols generated, stale sections removed, and (in `--verbose`) tokens / cache.

**Bootstrap (auto-detected first run, or `--all`)**: scans, builds the plan, prints it, then either honours `--budget`/`--limit` or asks for explicit confirmation in a tty. Non-interactive runs without a cap exit 1 to prevent surprise bills. Streams per-file `[N/M] file ✓ $cost` lines with ETA.

**Incremental (default after bootstrap)**: scans, reconciles orphans, runs `check_project`, computes the cascade (depth-1, hub-guarded), and re-syncs only affected files. Same per-file streaming output as bootstrap.

**Dry-run (`--dry-run`)**: identifies stale files via the same logic as `--check`, regenerates them into `.trie/preview/`, and prints unified diffs. Makes API calls — cap with `--budget`/`--limit`.

**Check (`--check`)**: re-fingerprints each in-scope source symbol and compares against the fingerprint stored in the matching triefact section sentinel. Reports `MISSING_TRIEFACT`, `MISSING_SECTION`, `STALE_SECTION`, `ORPHAN_SECTION`. This is the canonical pre-commit entry; `.pre-commit-hooks.yaml` calls `trie sync --check --quiet`.

`--check` is mutually exclusive with `--file`, `--all`, and `--dry-run`. `--file` is mutually exclusive with `--all`.

---

## `trie mcp install`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

```
trie mcp install [--target NAME ...] [--all] [--scope project|user]
                 [--print-only] [--dry-run]
```

| Option | Default | Description |
| --- | --- | --- |
| `--target NAME`, `-t` | auto-detect | Install for a specific agent. Repeat for multiple. |
| `--all` | `false` | Install for every known target. Skips per-target detection. |
| `--scope project\|user` | `project` | Project scope writes to a file inside the current project; user scope writes under your home dir. |
| `--print-only` | `false` | Print the JSON snippet that would be merged. Don't write any files. |
| `--dry-run` | `false` | Resolve the file path but don't write. |

Supported `--target` values:

| Slug | Display | Project path | User path |
| --- | --- | --- | --- |
| `claude-code` | Claude Code | `<project>/.mcp.json` | `~/.claude.json` |
| `claude-desktop` | Claude Desktop | — | `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) / `~/AppData/Roaming/Claude/claude_desktop_config.json` (Windows) / `~/.config/Claude/claude_desktop_config.json` (Linux) |
| `cursor` | Cursor | `<project>/.cursor/mcp.json` | `~/.cursor/mcp.json` |
| `windsurf` | Windsurf | — | `~/.codeium/windsurf/mcp_config.json` |
| `vscode` | VS Code | `<project>/.vscode/mcp.json` (uses `servers` key) | — |
| `codex` | Codex CLI | — | `~/.codex/config.json` |

Auto-detect (no `--target`, no `--all`): the installer checks for known config dirs / binaries on PATH and applies to whatever it finds. Errors out with a clear message if nothing is detected.

Behavior:

- The installer reads each target's existing JSON (if any), merges a `trie` entry under `mcpServers` (or `servers` for VS Code), and writes back atomically.
- Idempotent: re-running with no changes prints `skipped` for each target.
- Refuses to overwrite invalid JSON; prints an error so you can fix the file by hand.

The snippet written is:

```json
{ "command": "trie", "args": ["mcp", "serve"], "cwd": "<absolute project root>" }
```

---

## `trie mcp serve` (hidden)

Stdio MCP server entry point. Designed to be spawned by an agent harness, not run by users directly.

```
trie mcp serve
```

No options. Read-only — exposes four tools: `get_triefact`, `find_symbol`, `references_to`, `references_from`. Errors go to stderr only — stdout is reserved for the JSON-RPC stream and must not be polluted.

`trie mcp` (no subcommand) is a back-compat shim that runs the same code, so existing v0.1 snippets that reference `["mcp"]` keep working.

---

## Typical first-run flow

```bash
trie init                                # writes trie.toml, scans, prompts for hook install
trie plan                                # scan + cost preview, networked
trie sync --budget 2.00                  # first full pass, capped at $2
trie sync --check                        # pre-commit gate, offline
```

After that, day-to-day:

```bash
trie sync                                # incremental cascade
trie sync --dry-run --limit 5            # preview before paying
trie sync --check                        # pre-commit / CI gate
trie mcp install --target claude-code    # plug into your agent
```
