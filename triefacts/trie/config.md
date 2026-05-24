---
trie_version: 0.1.2
source: trie/config.py
file_fingerprint: 2c7f1cc694c5ad9a5c789bc8c2a480d17eba16f19127aac9fbd36c8d0100c072
last_synced_at: '2026-05-23T23:50:40Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-287
- kind: class
  qualified_name: trie/config:TrieMeta
  lines: 9-10
- kind: class
  qualified_name: trie/config:Scope
  lines: 14-23
- kind: class
  qualified_name: trie/config:Triefacts
  lines: 27-29
- kind: class
  qualified_name: trie/config:Models
  lines: 33-35
- kind: class
  qualified_name: trie/config:Cascade
  lines: 39-41
- kind: class
  qualified_name: trie/config:Sync
  lines: 45-65
- kind: class
  qualified_name: trie/config:Debug
  lines: 69-88
- kind: class
  qualified_name: trie/config:Mcp
  lines: 92-147
- kind: class
  qualified_name: trie/config:Config
  lines: 151-194
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 162-172
- kind: method
  qualified_name: trie/config:Config.load
  lines: 175-178
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 181-194
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 197-198
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 201-286
incoming_refs: 149
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=61627a2cc3c7ae6e0fc5dd6a9e82438b6c586d2e8280283184e8b0abb2bc93b9 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `trie/config`

Define configuration dataclasses and loading logic for `trie.toml` project configuration files.

- `Config.find_and_load`: walks up from a given path to locate `trie.toml`
- `ConfigNotFoundError`: raised when no `trie.toml` exists in the directory tree
- `DEFAULT_CONFIG_TOML`: ready-to-write string for `trie init`
<!-- trie:end -->
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=3a9f3f9b594eb2bc004d5ab6492991cf167ef4b9ae7b65e2738917beda05b61b body_fp=902860c5735258ea54f465b124a3a37d21f48734f0000d65250d5c135e87e5da source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `TrieMeta`

Holds the trie tool version string used in config serialization.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=9777dbd67a9881d6941229f88cec8d7a158ec8fee80321a584e061f25abf2cb2 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Scope`

Configure which source files trie includes and excludes via glob patterns.

- `include`: defaults to all `.py` files under the project root.
- `exclude`: defaults to `__pycache__`, `.venv`, `build`, and `dist` trees.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=54f1630e911bfe01aef7a0b728b56870aff680ad6c6b815e4b40b26e7e984a9b source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Triefacts`

Configure the output and source root directories for triefact generation.

- `root`: directory where generated Markdown triefact tree is written.
- `source_root`: source tree root, relative to the project file.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Models fingerprint=abf55624d4d046500cb6caf33a90cb62e33c0a2f319cfcb63d35d6a242726335 body_fp=6b56f51d7bc4d823432cba654a4d36d022d36e21776131f93d7c9c20bce4062c source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Models`

Store model identifiers for bootstrap and cascade LLM operations.

- `bootstrap`: model used for initial triefact generation.
- `cascade`: model used for incremental cascade sync.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Cascade fingerprint=0e7b3a716fd306199ce4ccbb537cb901c77f5a484dcc79d8132d1177378c9597 body_fp=fca6aee9a19f23f6b2a1009dc79b42236d31483bae6919fc129375f3e5d9abd8 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Cascade`

Configure reference-graph traversal behaviour for incremental sync.

- `hub_symbol_threshold`: symbols with more inbound refs than this are treated as depth-0 only, preventing utility hubs from over-invalidating.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Sync fingerprint=6e78bc409faa3564065bef1b86229e39b56fce1ec430f52e79b1e562be89d6fe body_fp=e0f1d9bcb760348118b9c38e2005b8b307f417ffacd41974040352e0d9be05d1 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Sync`

Control per-file LLM call parallelism and model-client retry behaviour during sync.

- `concurrency`: parallel per-symbol LLM calls per file; set to 1 for serial execution.
- `max_retries`: attempts before propagating 429/529 errors.
- `retry_base_delay_seconds`: base for exponential backoff (`base * 2**attempt + jitter`).
- `retry_cap_seconds`: maximum backoff delay before a retry attempt.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Debug fingerprint=74eb562287f2d40b4d10de5eeca4500a9792b9df3b3037d4e875d64dc1bcd8cc body_fp=0787385984eac94f0b7669820049335e6288393728b41060bf0e971d24cc70ad source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Debug`

Configure append-only JSONL telemetry; `TRIE_DEBUG` env var overrides `enabled` and optionally `log_path`.

- `enabled`: overridden by `TRIE_DEBUG`; env path value also sets `log_path`
- `log_path`: relative to project root, or absolute
- `log_to_stderr`: mirrors events to stderr; noisy in eval runs
- `capture_args`: includes MCP tool args in `mcp_call` events
- `capture_responses`: full response bodies; off by default due to size
- `redact_keys`: field paths to elide from logged events
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Mcp fingerprint=e46d773d9883e01b10f7457144cf15de8606a7e6b62e11581cbc8130132474f4 body_fp=114d33f098d2f0d287610ed0445b94d90d583338eeb1aabe7da134c0ce3059b9 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Mcp`

Server-side tuning knobs for the MCP `grep`, `read`, and `trace` tool surfaces; invisible to the agent.

- `grep_default_rank_by`: sort order — `"public_first"`, `"inbound_count"`, or `"alphabetical"`.
- `grep_fallback_max_files`: max in-scope files walked by ripgrep fallback before stopping.
- `grep_fallback_match_limit`: cap on candidate symbols returned after hub-ranking in fallback.
- `fuzzy_cutoff`: minimum rapidfuzz WRatio score (0–100) for any fuzzy hit to be included.
- `fuzzy_prose_pre_filter`: minimum score on name/one_liner before prose is read from disk.
- `fuzzy_prose_weight`: multiplier on prose score before taking max with name score.
- `read_max_neighbours_per_direction`: `0` = unlimited neighbours shown per direction.
- `read_prose_max_chars`: `0` = no prose truncation on read.
- `trace_hub_threshold`: symbols with more inbound refs are skipped in trace; default is effectively unlimited.
- `trace_prose_at_depth`: `0` = no prose attached to trace nodes.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config fingerprint=a550e09883e6c18df41905160eff158c7967ad28acfc1bbf54776be19224fac3 body_fp=9e0c55cb49b1e4aeb19da23603e40d6e502238a8a8b5fcdcb88c20afd540a5cf source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Config`

Aggregate all configuration sections parsed from `trie.toml` into a single dataclass.

- `from_dict(data)`: construct from a raw TOML dict, with per-section defaults.
- `load(path)`: parse a TOML file at `path` and return a `Config`.
- `find_and_load(start)`: walk up from `start` to find `trie.toml`; returns `(Config, config_dir)` or raises `ConfigNotFoundError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=2a49e1d83738c09e61cd41f62971e3bc5e6c4e3affac719b5f5b3a0498c717dc body_fp=4d082ee447df243674920d32d61358be027290fc28cebe9e563beebcce733ecc source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` instance from a plain dictionary, defaulting each section to an empty dict if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=27fd2dd76b1f1ef32e50534a62131424ad6a5b00c30ae5a767b639e231cc1b4a source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Config.load(cls, path: Path) -> Config`

Parse a TOML file at `path` into a `Config` instance.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=e5bb56fa118b02233fbbd87c3da1a69a15e3b8ba530425e1c01faef89755457d source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `Config.find_and_load(start: Path) -> tuple[Config, Path]`

Walk up the directory tree from `start` to find and load `trie.toml`, returning the config and its directory.

- `start`: directory to begin searching; resolves upward through all parents.
- Returns `(Config, Path)` where `Path` is the directory containing `trie.toml`, used as project root.
- Raises `ConfigNotFoundError` if no `trie.toml` exists in `start` or any ancestor.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=9384399004a8268f94c411734c5e6d97d8dba77626311796ea4dc7b2a7ca4637 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `ConfigNotFoundError(FileNotFoundError)`

Raised when no `trie.toml` is found during `Config.find_and_load` directory traversal.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:DEFAULT_CONFIG_TOML fingerprint=426323ff65b0749777c80398d4edf83a217cb91dd0f74a5eff4d84de9b0e4441 body_fp=b129bc1edefc4ffe6830d0196f5ea29cb428a8cafd2a463c5b2cef326ec793b6 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `DEFAULT_CONFIG_TOML`

Annotated TOML string written by `trie init` as the starter `trie.toml` file, reflecting all `Config` dataclass defaults.
<!-- trie:end -->