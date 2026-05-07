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
| `trie plan` | yes (free) | Drift check + scan + cost preview. Uses `count_tokens`, never `messages.create`. |
| `trie sync` | yes (paid) | Generate or refresh triefacts. Auto-detects bootstrap vs incremental. |
| `trie verify` | no | Offline drift gate. Exits 1 on any drift in either direction. Pre-commit entry. |
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

Surface drift, scan the project, and show the worklist + estimated cost.

```
trie plan [--model MODEL]
```

| Option | Default | Description |
| --- | --- | --- |
| `--model` | `[models].bootstrap` | Override the model used for the cost estimate. |

Step 1 is the same offline drift check `trie verify` runs (same set of `StaleReason` outcomes; same bidirectional coverage). Drift is reported as a warning but does not abort — `plan` is informational, not a gate.

Then: networked but cheap. Uses Anthropic's free `count_tokens` per file, never `messages.create`. Run before `trie sync` if you want to see the bill before paying it.

Output: drift summary (or "coherent"), scan breakdown (new / updated / unchanged / removed), plan header (`N files, ~$X estimated`), top-10 ranked files with `(symbols, score, ~$cost)`, and a "… and N more" tail if the worklist is longer.

---

## `trie sync`

Generate or refresh trie triefacts. Several modes; the default auto-detects.

```
trie sync [--file PATH] [--all] [--dry-run]
          [--budget USD] [--limit N] [--model MODEL]
```

| Option | Default | Description |
| --- | --- | --- |
| `--file PATH`, `-f` | — | Sync exactly one source file (smoke test of the LLM path). |
| `--all` | `false` | Force a full re-pass over every file in scope, even when triefacts already exist. |
| `--dry-run` | `false` | Regenerate stale triefacts into `.trie/preview/` and print a unified diff against the live tree. **Replaces v0.1 `trie diff`.** |
| `--budget USD` | — | Cumulative actual-cost cap. Stops once reached (overshoots by at most one file). |
| `--limit N` | — | Cap on the number of files synced. |
| `--model MODEL` | bootstrap → `[models].bootstrap`; incremental → `[models].cascade` | Override the model. |

For LLM-free, exit-coded drift detection (e.g. pre-commit, CI gate), use `trie verify` instead.

### Mode dispatch

The flags select the mode in this priority order:

1. **`--file`** → single-file sync.
2. **`--dry-run`** → diff preview into `.trie/preview/`.
3. Else **auto-detect**:
   - If `--all` or no `triefacts/` directory exists yet → **bootstrap** (full pass).
   - Otherwise → **incremental cascade**.

### Per-mode behavior

**Single file (`--file`)**: cheapest LLM smoke test. Streams a one-line summary of symbols generated, stale sections removed, and (in `--verbose`) tokens / cache.

**Bootstrap (auto-detected first run, or `--all`)**: scans, builds the plan, prints it, then either honours `--budget`/`--limit` or asks for explicit confirmation in a tty. Non-interactive runs without a cap exit 1 to prevent surprise bills. Streams per-file `[N/M] file ✓ $cost` lines with ETA.

**Incremental (default after bootstrap)**: scans, reconciles orphans, runs the same drift check that `verify` runs, computes the cascade (depth-1, hub-guarded), and re-syncs only affected files. Same per-file streaming output as bootstrap.

**Dry-run (`--dry-run`)**: identifies stale files via the drift check, regenerates them into `.trie/preview/`, and prints unified diffs. Makes API calls — cap with `--budget`/`--limit`.

`--file` is mutually exclusive with `--all`.

---

## `trie verify`

Offline drift check. Exits 1 if any triefact has drifted.

```
trie verify
```

No options. No LLM, no scan, no DB writes. Designed for pre-commit hooks and CI.

Bidirectional coverage:

| `StaleReason` | Direction | Trigger |
| --- | --- | --- |
| `MISSING_TRIEFACT` | Code → Triefact | Source has public symbols but no triefact file. |
| `MISSING_SECTION` | Code → Triefact | Public symbol present but no section documents it. |
| `STALE_SECTION` | Code → Triefact | Source body changed but the section wasn't regenerated (`fingerprint` mismatch). |
| `ORPHAN_SECTION` | Triefact → Code | Section exists but its symbol has been renamed, made private, or deleted. |
| `TAMPERED_BODY` | Triefact → Code | Section body was edited between sentinels (`body_fp` mismatch). |
| `LEGACY_SECTION` | Triefact → Code | Section was written by trie ≤ 0.1 with no body fingerprint to verify — re-sync once to migrate. |

The same check runs as the first step of `plan` and `sync`; `verify` exists so CI and hooks can fail loudly. `.pre-commit-hooks.yaml` calls `trie -q verify`.

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
trie mcp install --target claude-code    # plug into your agent (optional, can run anytime)
trie plan                                # drift summary + scan + cost preview, networked but free
trie sync --budget 2.00                  # first full pass, capped at $2
trie verify                              # smoke-test the pre-commit gate
```

After that, day-to-day:

```bash
trie sync                                # incremental cascade — drift check then regenerate affected files
trie sync --dry-run --limit 5            # preview before paying
trie verify                              # called automatically by the pre-commit hook
```

### Per-subcommand role outside the first-run sequence

| Command | When you reach for it day-to-day |
| --- | --- |
| `trie init` | One-shot. Re-run with `--force` only if `trie.toml` got corrupted. |
| `trie plan` | "I haven't synced in a while — what's the bill if I do now?" Combines drift surface and cost estimate without spending a cent. |
| `trie sync` | Daily driver. Run after a meaningful refactor or before a PR. The cascade only touches files that actually need it. |
| `trie sync --file <path>` | Cheapest possible LLM smoke test after editing a single file. Useful for tuning prompts or checking a specific symbol. |
| `trie sync --dry-run` | "Is this regen going to be ugly?" Reviews the diff before committing tokens to a full sync. |
| `trie verify` | Pre-commit / CI / "is the tree coherent right now?". The pre-commit hook calls this — invoke it manually only when debugging the hook. |
| `trie mcp install` | One-shot per agent / per machine. Re-run after switching agents or after a fresh OS install. |
| `trie mcp serve` | Never run by hand — agents spawn it via the snippet `install` writes. |
