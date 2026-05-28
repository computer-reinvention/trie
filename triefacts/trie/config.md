---
trie_version: 0.1.5
source: trie/config.py
file_fingerprint: d3319a14a8e4df719e1265fb0298a81b036ecbfc1f33d850990a6b430d3bc2e7
last_synced_at: '2026-05-28T01:38:05Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-342
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
  lines: 33-36
- kind: class
  qualified_name: trie/config:Cascade
  lines: 40-43
- kind: class
  qualified_name: trie/config:LspBackend
  lines: 47-63
- kind: class
  qualified_name: trie/config:Edits
  lines: 67-75
- kind: class
  qualified_name: trie/config:Sync
  lines: 79-99
- kind: class
  qualified_name: trie/config:Debug
  lines: 103-122
- kind: class
  qualified_name: trie/config:Mcp
  lines: 126-181
- kind: class
  qualified_name: trie/config:Config
  lines: 185-234
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 197-212
- kind: method
  qualified_name: trie/config:Config.load
  lines: 215-218
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 221-234
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 237-238
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 241-341
incoming_refs: 173
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=61627a2cc3c7ae6e0fc5dd6a9e82438b6c586d2e8280283184e8b0abb2bc93b9 source_ref=e4ba123c065b3ae251beea6b022a4c16bb2c9f72 -->
## `trie/config`

Define configuration dataclasses and loading logic for `trie.toml` project configuration files.

- `Config.find_and_load`: walks up from a given path to locate `trie.toml`
- `ConfigNotFoundError`: raised when no `trie.toml` exists in the directory tree
- `DEFAULT_CONFIG_TOML`: ready-to-write string for `trie init`
<!-- trie:end -->
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=042e1678d51e63de3de50f0abb830138d4b678a5fb1cb49d024bcb1909843280 body_fp=902860c5735258ea54f465b124a3a37d21f48734f0000d65250d5c135e87e5da source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
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
<!-- trie:section symbol=trie/config:Models fingerprint=e882ddd5e301a630dc1f077967f9ec3f48511c22931d0bd32de2d39512854871 body_fp=782d9bf82fd4d88ae390315b75eef8efd5e918eae9723853485986d03751a70e source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `Models`

Store model identifiers for bootstrap, cascade, and edits LLM operations.

- `bootstrap`: model used for initial triefact generation.
- `cascade`: model used for incremental cascade sync.
- `edits`: model used for the patch-apply pipeline.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Cascade fingerprint=9a685f1d6a6008e1bc16ca1ea29a753bdf3f64fc881a94cb31cf485d6ee42b01 body_fp=ae9452809ee29e3dce446b80e2a4ef6371eda8d53760df3df55fc9bb92889b88 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `Cascade`

Configure reference-graph traversal behaviour for incremental sync.

- `hub_symbol_threshold`: symbols with more inbound refs than this are treated as depth-0 only, preventing utility hubs from over-invalidating.
- `max_judgments`: hard cap on `pre_filter_cascade` calls per apply run.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:LspBackend fingerprint=b9c2864ea0cd6bcd2cdb18b855ee096c71423d6f619e3d8132b5a2ee64091d4a body_fp=14a8d984f56e041a7582a3e781d4be38875b2199f4f298120639c8f52b954f6e source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `LspBackend`

Configure a single language-server backend used for diagnostics during patch apply.

- `command`: binary name resolved via `shutil.which`
- `check_args`: CLI flags prepended before the file path argument
- `output_format`: `"pyright"` or `"ruff"`; controls stdout parsing into `{line, column, code, message}[]`
- `exit_ok_codes`: exit codes meaning "no diagnostics"; stdout is always read regardless
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Edits fingerprint=981676998916a9eb811467dfc40523109336af054a86d94aaa07898c1fdfc1d0 body_fp=273e16762a132905daa4823ef2ddc6af26654d4d1ab15a3eab69b7877b90f553 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `Edits`

Configure the patch-apply pipeline and LSP diagnostics.

- `lsp_max_retries`: attempts to fix LSP-reported diagnostics before giving up.
- `lsp_backends`: ordered list of LSP backends; first one found on PATH is used.
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
<!-- trie:section symbol=trie/config:Config fingerprint=39cdd983275490488052db937ca90d6b40f612dddf42cf46502e0a832b7dade6 body_fp=251ea66abeaf9b1507babd08892bdb45fa865718518e644022ec4e9da7aa1616 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `Config`

Aggregate all configuration sections parsed from `trie.toml` into a single dataclass.

- `edits`: new `Edits` field; `from_dict` deserialises `lsp_backends` entries into `LspBackend` instances before constructing it.
- `from_dict(data)`: construct from a raw TOML dict, with per-section defaults.
- `load(path)`: parse a TOML file at `path` and return a `Config`.
- `find_and_load(start)`: walk up from `start` to find `trie.toml`; returns `(Config, config_dir)` or raises `ConfigNotFoundError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=1b59860b1ffda417aa3d89ae97b50e688620da830b00253b94767622bf77c05d body_fp=7b483bef673a29e850ad8133a993cbaf5169fe875b255db58232ec39a1892b02 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` instance from a plain dictionary, deserialising `edits.lsp_backends` into `LspBackend` objects and defaulting each section to an empty dict if absent.
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