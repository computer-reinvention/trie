# trie tool extensions — capability-gap spec

Status: **active**. The trie-native opencode fork is built, tested, and
behaviour-validated against a live model (branch `feat/trie-native`, vendored as
the `opencode/` submodule).

**Implemented so far (in core trie + wired into the fork):** EXT-1 (`grep-str
--all-files` / `grep_str_all`), EXT-2 (`trie find` / `find_files`), EXT-3 + EXT-4
(`trie read --source` / `read_source`), EXT-8 (`trie write` / `write_file`),
EXT-11 (`trie blast-radius` + `trie_blast_radius` tool). Remaining: EXT-7
(sub-symbol/non-symbol line edits — deeper pipeline work), EXT-9 (multi-language
indexing — the structural unlock), and the deliberately-out-of-scope EXT-5
(binaries), EXT-6 (dir listing — partly covered by `find`), EXT-10 (external
dirs).

This file tracks the functionality a coding agent **loses** if it uses trie
tools *only* (no stock opencode file tools). The fork ships the replacements
anyway — it demotes the stock `grep`/`read`/`glob`/`edit`/`write` tools to
renamed "backup" tools and steers the agent to trie. Each backup tool is a
crutch; this spec is the plan to remove each crutch by widening core trie.

**Validated behaviour (live model, claude-haiku-4-5, via `opencode run`):**

- Code search → the model picks `trie_grep` / `trie_read` / `trie_trace`, never
  stock grep/read.
- Modify indexed code → the model uses `trie_patch` → `trie_patch_preview` →
  `trie_patch_apply`, never `fs_edit`; the change cascades to callers and is
  runtime-correct.
- Rename → the model traces the blast radius first, then drives
  `trie_rename_symbol`; the definition, imports, and call sites all cascade.
- New / non-indexed files → the model falls back to `fs_write` / `fs_edit`.
- Non-symbol-region edit on indexed code → the guard refuses the first
  `fs_edit`, the model reads the refusal and retries with `force: true` (the
  EXT-7 case below).

When an extension below lands in core trie, the fork can flip the corresponding
backup tool off (or stop steering around it). Every entry names the backup tool
it would retire.

---

## Root cause: trie indexes Python only

`trie/config.py:15` → `include = ["**/*.py"]`. Everything trie does — `grep`,
`grep_str`, `read`(triefact), `trace`, the patch/apply pipeline — operates on
*in-scope* files only. The `grep` text-match fallback shells `rg` against
in-scope bodies only (`trie/mcp_server.py`, `_require_ripgrep`). So in any
non-Python or mixed repo, trie covers a fraction of the tree.

Most gaps below are downstream of this. **EXT-9 (multi-language)** is the
umbrella fix; the others are useful even before that lands.

---

## Severity legend

- **Critical** — structurally impossible with trie today; the fork *must* keep
  a backup tool until the extension lands.
- **High** — frequent real-world need; agent will hit it regularly.
- **Medium** — occasional; backup is an acceptable stopgap.
- **Low** — rare or arguably better handled by backup forever.

---

## EXT-1 — Unscoped text search  ·  Critical · ✅ DONE

- **Lost:** searching text in non-indexed files (TS/JS, Go, JSON, YAML, md,
  lockfiles). Stock `grep`/`grep_str` search the whole tree.
- **Trie today:** `grep` fallback + `grep_str` only search in-scope source
  bodies; non-Python files are invisible.
- **Backup it retires:** `fs_grep` (renamed stock grep).
- **Proposed interface:** `trie grep-str <regexp> [--all-files]` and an
  equivalent `scope: "indexed" | "all"` arg on the MCP `grep_str` tool.
  `--all-files` runs gitignore-aware `rg` over the whole repo; in-scope hits are
  still attributed to enclosing symbols, out-of-scope hits return plain
  `file:line:text`.
- **Where:** `trie/cli.py` `grep_str_cmd` (~2581); MCP handler in
  `trie/mcp_server.py`; the rg invocation already exists for the fallback —
  generalize its glob filter.
- **Acceptance:** finds a literal string inside a `.ts` and a `.md` file.

## EXT-2 — Filename / path glob search  ·  Critical · ✅ DONE

- **Lost:** finding files by name/path pattern (`**/*.tsx`, `Dockerfile`,
  `*.config.*`). Stock `glob`.
- **Trie today:** no path/filename search at all — only symbol search.
- **Backup it retires:** `fs_glob` (renamed stock glob).
- **Proposed interface:** new `trie find <glob> [--all-files]` CLI + MCP tool.
  Returns matching paths, mtime-sorted, capped (mirror stock glob's 100-limit +
  truncation note). `--all-files` covers the whole tree; default could prefer
  indexed files first.
- **Where:** new command in `trie/cli.py`; new tool in
  `trie/mcp_server.py`; reuse `trie/scope.py` discovery for the indexed subset
  and a raw walk for `--all-files`.
- **Acceptance:** `trie find '**/*.ts'` lists TS files repo-wide.

## EXT-3 — `read` line-range + line-number prefixes  ·  Medium · ✅ DONE

- **Lost:** arbitrary line-window reads with `<line>:` prefixes (`offset`,
  `limit`, 1-indexed) on any file. Stock `read`.
- **Trie today:** `trie read <qname>` is symbol/triefact-centric; no
  offset/limit windowing on arbitrary files. (The old injected `read.ts` did
  some of this in TS; we want it native in trie.)
- **Backup it retires:** part of `fs_read` (renamed stock read).
- **Proposed interface:** `trie read --source --offset N --limit M <path>`
  emitting line-numbered output byte-comparable to stock read; honour the
  2000-char line truncation rule.
- **Where:** `trie/cli.py` `read_cmd` (~2476) — add a `--source` path mode.
- **Acceptance:** output matches stock `read` for a non-indexed file with
  offset/limit.

## EXT-4 — Read arbitrary (non-indexed) file contents  ·  Critical · ✅ DONE

- **Lost:** "show me this file" for configs/docs/TS source not in scope.
- **Trie today:** `read` qname/triefact only; no plain-file path for unsynced
  files.
- **Backup it retires:** `fs_read`.
- **Proposed interface:** subsumed by EXT-3's `--source` path mode (works for
  any path, indexed or not).
- **Acceptance:** `trie read --source path/to/app.ts` returns its contents.

## EXT-5 — Image / PDF attachment reads  ·  Low

- **Lost:** reading images/PDFs as base64 attachments
  (`SUPPORTED_IMAGE_MIMES`, PDF path in stock `read.ts`).
- **Trie today:** none; trie is text/graph only.
- **Backup it retires:** none — likely a permanent backup responsibility.
- **Proposed:** out of scope unless trie grows a binary/attachment path. Record
  as non-goal; keep `fs_read` for binaries.

## EXT-6 — Directory listing  ·  Medium

- **Lost:** `read` on a directory → entries with trailing `/`.
- **Trie today:** none.
- **Backup it retires:** part of `fs_read`.
- **Proposed:** fold into EXT-2 (`trie find`) — a bare-dir listing mode, or
  accept backup ownership.

## EXT-7 — Sub-symbol & non-symbol-region edits  ·  High

- **Lost:** exact line/string edits inside a symbol (1-char fix), and edits to
  regions that aren't symbols: module-level constants (not indexed —
  `USING_TRIE.md` "edge cases"), top-of-file comments, `if __name__ == ...`,
  import blocks the agent wants to hand-tune. Stock `edit` (oldString/
  newString/replaceAll).
- **Trie today:** patch regenerates the *whole symbol* body via LLM —
  non-deterministic and overkill for a one-line change; can't target
  non-symbol text at all.
- **Backup it retires:** `fs_edit` (renamed stock edit) for synced-code edits.
- **Proposed interface:** `trie patch <qname> --line-edit --old <s> --new <s>`
  (deterministic string replace within the symbol's span, no LLM), and index
  module-level constants as symbols so they become patchable. For
  module-header/`__main__` regions, consider a `__module__`-scoped edit.
- **Where:** `trie/edits/pipeline.py` (add a deterministic line-edit path that
  skips generation); `trie/parse/*` for constant indexing.
- **Acceptance:** change one line in a function with no LLM call; edit a
  module-level constant via patch.

## EXT-8 — Create/write arbitrary files  ·  Critical · ✅ DONE

- **Lost:** creating new non-Python files (configs, scripts, README, JSON) and
  whole new Python *files*. Stock `write`.
- **Trie today:** `create_symbol` makes a Python *symbol* inside an *existing
  synced file* only.
- **Backup it retires:** `fs_write` (renamed stock write).
- **Proposed interface:** `trie write <path>` for arbitrary file creation
  (re-scan after), and a "create new module file + first symbol" path in the
  pipeline. Largely unblocked by EXT-9 for code files.
- **Acceptance:** create a new `.ts`/`.md` file and a new `.py` module via trie.

## EXT-9 — Multi-language indexing  ·  High (umbrella)

- **Lost:** all of EXT-1/3/4/7/8 *for non-Python code*.
- **Trie today:** Python-only scope + parser.
- **Backup it retires:** narrows reliance on every `fs_*` tool for code in
  supported languages.
- **Proposed:** widen `trie.toml` `include` (e.g. `**/*.ts`) and add
  tree-sitter parser coverage per language. Track per-language parser support
  as a sub-checklist.
- **Acceptance:** a `.ts` file is grep/read/trace/patch-able.

## EXT-11 — Expose `blast_radius` as a CLI command  ·  Low · ✅ DONE

- **Lost:** the fork wanted a `trie_blast_radius` tool, but `blast_radius` is
  MCP-only — there is no `trie blast-radius` CLI subcommand, so the native tool
  (which shells the CLI) was dropped. The agent currently approximates it with
  `trie_patch_preview` and `trie_trace --direction callers`.
- **Trie today:** `blast_radius` exists in `trie/mcp_server.py` only.
- **Backup it retires:** n/a (adds a missing tool).
- **Proposed interface:** add `trie blast-radius <qname>` to `trie/cli.py`
  delegating to the same code the MCP tool calls; then re-add the
  `trie_blast_radius.ts` tool to the fork.
- **Acceptance:** `trie blast-radius pkg/mod:fn` prints the cascade set.

## EXT-10 — External-directory operations  ·  Medium

- **Lost:** reads/edits/searches on paths outside the worktree (stock tools'
  `assertExternalDirectory` bypass).
- **Trie today:** scoped to one `trie.toml` root; no cross-project.
- **Backup it retires:** none — cross-project stays with backup tools.
- **Proposed:** out of scope; record as permanent backup responsibility.

---

## Fork ↔ extension cross-reference

| Backup tool (fork) | Retired by | Status |
|---|---|---|
| `fs_grep`  | EXT-1, EXT-9 | ✅ EXT-1 done (`trie_grep_str all_files`); non-Python *symbol* search still needs EXT-9 |
| `fs_glob`  | EXT-2 | ✅ done (`trie_find`) — kept as backup for parity/edge cases |
| `fs_read`  | EXT-3, EXT-4 (binaries EXT-5, dirs EXT-6 stay) | ✅ text reads done (`trie_read` path mode + `read_source`); binaries/dirs stay |
| `fs_edit`  | EXT-7, EXT-9 | ⬜ pending (sub-symbol/non-symbol line edits) |
| `fs_write` | EXT-8, EXT-9 | ✅ `trie write`/`write_file` exists; fork keeps `fs_write` as the new-file tool (no graph benefit for new non-code files), so not wired as a competing fork tool |
| `apply_patch` | (model-specific; keep) | — |
| external-dir on all | EXT-10 (stays backup) | — |

> **Note on EXT-8 in the fork:** `trie write` / `write_file` is implemented in
> core trie (creates any file under the root, flags `needs_sync` for in-scope
> paths). It is intentionally *not* exposed as a separate `trie_write` fork
> tool: creating a brand-new non-code file gains nothing from routing through
> trie, and a competing write tool would muddy the main-vs-backup story the
> prompt teaches. The fork keeps `fs_write` for new files; the CLI/MCP
> `write_file` is available for scripted/parity use.

## Bugs found during fork scenario testing (fixed)

These surfaced while exercising the native tools end-to-end against a live
synced project; all are fixed in the same change set.

- **Edit guard symlink miss (fork).** `makeTrieProbes.synced` compared an
  agent-supplied path against the realpath'd project root with a raw
  `startsWith`. On macOS (`/tmp` → `/private/tmp`) and any symlinked path the
  guard silently failed to fire, so `fs_edit` could modify indexed code
  unchecked. Fixed by resolving both sides via `AppFileSystem.resolve`
  (realpathSync, ENOENT-safe) before comparison. `normalizePath` was a no-op
  off Windows — do not use it for this.
- **`patch apply` dumped raw tracebacks (fork).** On a crash (e.g. missing API
  key) the tool returned the full multi-line Python traceback to the agent.
  Fixed: only exit-1-with-stdout is treated as a structured ApplyReport;
  otherwise a `summarizeError` helper extracts the final exception line.
- **`patch list` / `patch preview` omit staged creates (trie core).** Create
  patches live in the `create_patches` table; the list/preview commands only
  read the modify/structural table, so a staged `create-symbol` showed "no
  pending patches" even though `apply` would process it. Fixed both commands
  to include creates.
- **`patch drop` leaves creates behind (trie core).** `delete_patches` doesn't
  touch `create_patches`; `drop --all`/`--qname`/`--session` now also call
  `delete_create_patches`, so the agent can actually undo a staged creation.

## Suggested implementation order

1. EXT-1, EXT-2 (search/glob over all files) — biggest day-one relief.
2. EXT-3/EXT-4 (`read --source`) — removes most `fs_read` use.
3. EXT-7 (`--line-edit` + constant indexing) — removes most `fs_edit` use.
4. EXT-8 (`trie write`) — removes `fs_write` use.
5. EXT-9 (multi-language) — the structural unlock; revisit all of the above.
