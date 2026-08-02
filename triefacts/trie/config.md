---
trie_version: 0.3.0
source: trie/config.py
file_fingerprint: 3033640bbebc167f27cb85781bab69cd4504e8c4168f4e0e08d8b8b4516467cc
last_synced_at: '2026-08-01T14:59:14Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-437
- kind: class
  qualified_name: trie/config:TrieMeta
  lines: 9-10
  signature: class TrieMeta
- kind: class
  qualified_name: trie/config:Scope
  lines: 14-39
  signature: class Scope
- kind: class
  qualified_name: trie/config:Triefacts
  lines: 43-45
  signature: class Triefacts
- kind: class
  qualified_name: trie/config:Resolver
  lines: 49-69
  signature: class Resolver
- kind: class
  qualified_name: trie/config:Models
  lines: 73-75
  signature: class Models
- kind: class
  qualified_name: trie/config:Cascade
  lines: 79-85
  signature: class Cascade
- kind: class
  qualified_name: trie/config:Sync
  lines: 89-133
  signature: class Sync
- kind: class
  qualified_name: trie/config:Debug
  lines: 137-156
  signature: class Debug
- kind: class
  qualified_name: trie/config:Mcp
  lines: 160-217
  signature: class Mcp
- kind: class
  qualified_name: trie/config:Diff
  lines: 221-248
  signature: class Diff
- kind: class
  qualified_name: trie/config:Config
  lines: 252-303
  signature: class Config
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 265-281
  signature: "def from_dict(cls, data: dict) -> Config: # NOTE: [edits] and [languages] sections (and models.edits) in existing # trie.toml files are silently ignored \u2014 they configured the removed # code-generation pipeline (the patch pipeline is an intent store now)."
- kind: method
  qualified_name: trie/config:Config.load
  lines: 284-287
  signature: 'def load(cls, path: Path) -> Config'
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 290-303
  signature: 'def find_and_load(cls, start: Path) -> tuple[Config, Path]'
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 306-307
  signature: class ConfigNotFoundError(FileNotFoundError)
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 310-436
incoming_refs: 365
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=73508aef5ccf98a204e6bf0fa288e0420baac8315fc2fb1aa7e8d1bf91d72a01 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Defines configuration data structures and loading logic for the trie documentation system.

- TrieMeta: version metadata for the trie system
- Scope: file inclusion/exclusion patterns for documentation generation
- Triefacts: output directory and source root configuration
- Models: model selection for bootstrap, cascade, and edit operations
- Cascade: graph traversal settings including depth limits and hub thresholds
- Sync: concurrency and retry settings for parallel LLM operations
- Mcp: MCP server tool behavior knobs for grep, read, and trace operations
- Debug: telemetry and logging configuration with environment variable overrides
- Edits: patch application settings and LSP backend configuration
- LspBackend: language server configuration for diagnostics during patch apply
- Config: main configuration class with TOML loading and project discovery
- DEFAULT_CONFIG_TOML: template configuration with documentation comments
<!-- trie:end -->
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=4a567e8d864b6fbc3eaabdd2083b8c05be47d3d5171cb3d63ab8c8fb22f9f605 body_fp=bfad556268f5bdddd625c4a85071206b598873df3c1916b2760b4f1be7a56e98 source_ref=ef006806a3d41eb39becc803db256e1c63cbc46c role=model -->
## `class TrieMeta`

Stores the trie library version string.

- `version`: Current version of the trie library
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Scope fingerprint=95b891d347bbe687492ee429be84488431b0dbb88f8376795edaff2267b00e71 body_fp=9511c1e19ccb12cf69a5116ce124e239284a3fe50dff75fcc630b40e5cab20e7 source_ref=510dbd7539ccb0936ec4f10c68b018717709082e role=model -->
## `class Scope`

Defines file inclusion and exclusion patterns for trie's source scanning scope.

- `include`: glob patterns for files to process (defaults to Python, TypeScript/TSX, JavaScript, Go, Rust, C/H, and Lua files)
- `exclude`: glob patterns for files to skip (defaults to hidden dirs, pycache, node_modules, build/dist)
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=dd7e170576548fa2b22db840143c16fbc243d8c21007ee162582322a06b10506 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
## `class Triefacts`

Configuration for triefact output paths and source tree location.

- `root`: Directory where generated Markdown triefacts are stored, mirroring source structure
- `source_root`: Path to source tree root relative to config file location
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Resolver fingerprint=ad417019b30d58a20901fbe12f889884573fc0f71bce635342b37a5c26e28191 body_fp=1d4d8fba0f875875ccd808d4b6ae24e00df3bbc9ec5fd8f819ac630b361d3c8e source_ref=510dbd7539ccb0936ec4f10c68b018717709082e role=config -->
## `class Resolver`

Configure the type-aware LSP reference resolver that supplements tree-sitter with method/member-dispatch edges.

- `enabled`: master switch; `False` forces tree-sitter-only for all languages.
- `disabled_languages`: per-language opt-out from LSP even when a server is installed.
- `servers`: overrides the built-in server command per language; missing binary still degrades gracefully.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Models fingerprint=71d55e59c71604441f07795baebe1039c78e45ec5f83642cfc0fb12c800e214f body_fp=3fb447608426fd68605619204af5f3fb7e954ba0c002413e9a600e33834a7be4 source_ref=8290941270823de571094515addff8acc7bc9467 role=config -->
## `class Models`

Specifies default model identifiers for different trie operations.

- `bootstrap`: Model used for initial triefact generation
- `cascade`: Model used for cascaded reference updates
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Cascade fingerprint=f75ec172dcb1f95fecfbf0a537fe3f1fed8dd874f90ff0fed3493c9b45b0b52f body_fp=edc83194bc074af8781beb289201489f43e1aa7eebf1ec04178f03bfe131c0a9 source_ref=804cbe955566bb7dc234ec68033f1e84827f016f role=config -->
## `class Cascade`

Configuration for cascade analysis that determines incremental sync depth and hub symbol handling.

- `max_judgments`: hard cap on pre_filter_cascade calls per apply run
- `surface_unresolved`: surface second-order cascades as ApplyReport.unresolved rather than chasing in-pipeline
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Sync fingerprint=a93ade6800fe0ee90ea2e067bb805b9d35056a5197ebda7f91e37178abd868a8 body_fp=d23ee7cf7075a23f295ab3e6a0652378f7f0533d7416fec119640b520b5fb20f source_ref=073d45150b29b0a304f40de8e0d78addf413edcc role=config -->
## `class Sync`

Configuration dataclass for controlling parallelism and retry behavior during sync operations.

- `concurrency`: parallel per-symbol LLM calls within a single file (default 4)
- `file_workers`: concurrent files being processed (default 8)
- `max_inflight_requests`: global cap on total concurrent LLM calls (default 8)
- `max_retries`: retry attempts before propagating rate-limit errors (default 8)
- `retry_base_delay_seconds`: base exponential backoff delay (default 1.0)
- `retry_cap_seconds`: maximum backoff delay (default 60.0)
- `retry_total_seconds`: total wall-clock budget for one call's retry loop; 0 = unbounded (default 300.0)
- `request_timeout_seconds`: per-request timeout preventing indefinite hangs (default 120.0)
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Debug fingerprint=74eb562287f2d40b4d10de5eeca4500a9792b9df3b3037d4e875d64dc1bcd8cc body_fp=be792dd521eeb94d1ae9e8195b159d8db4ee007f3b6878a87354381dd37c61c4 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
## `class Debug`

Configures telemetry logging for trie operations, controlled by the TRIE_DEBUG environment variable.

- `enabled`: defaults to False but overridden by TRIE_DEBUG env var
- `log_path`: JSONL file location, overridden when TRIE_DEBUG is a path
- `log_to_stderr`: mirrors events to stderr for development debugging
- `capture_responses`: includes full LLM response bodies in logs (large data)
- `redact_keys`: field paths to elide from logged data
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Mcp fingerprint=8ef59f987061dad18825c0fbd216fd0eaf393f132fe55930b6acee33a0e59676 body_fp=10944ced3fa148defa01dfdadf5fd59ad46622ce44e61076a496397a02d66889 source_ref=d993ec8facf84f0075a976a1e538b2aea4e04d52 role=config -->
## `class Mcp`

Dataclass holding server-side tuning knobs for the MCP `grep`, `read`, and `trace` tools; never exposed to the agent.

- `grep_fallback_max_files`: max in-scope files walked by the ripgrep fallback when name-match returns nothing.
- `grep_fallback_match_limit`: cap on candidate symbols returned from the ripgrep fallback after hub-ranking.
- `fuzzy_cutoff`: minimum rapidfuzz WRatio score (0–100) to include a hit in any fuzzy result.
- `fuzzy_prose_pre_filter`: minimum score on name/one-liner before prose is read from disk; prevents O(N) disk reads.
- `fuzzy_prose_weight`: multiplier on prose-derived score so prose-only matches rank below name matches.
- `read_max_neighbours_per_direction`: `0` = unlimited neighbour symbols returned by `read`.
- `read_prose_max_chars`: `0` = unlimited prose characters returned by `read`.
- `trace_hub_threshold`: symbols with more inbound refs than this are skipped during `trace`/`trace_flow` expansion.
- `trace_prose_at_depth`: `0` = no prose attached to trace results.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Diff fingerprint=02d7b7c4a34c801654ba7e7ba0c3ee31d29e464c963c3cb640a04f17864788fb body_fp=4521fe4015187aaa0e50c829372b9142fce33e22788e41f86cfe26d9767bbe06 source_ref=18c0228ab22574981e4c5031db011c5783d28510 role=config -->
## `class Diff`

Dataclass holding configuration for the per-commit digest system, where each commit produces one immutable file under `diffs_dir` and `write_path` is a symlink to the latest.

- `narrative`: when `True`, prepends an LLM-generated summary; falls back to raw evidence if no API key is available.
- `write_path`: symlink at project root pointing at the latest digest file; changing it also requires updating the pre-commit hook.
- `diffs_dir`: defaults to `"triefacts/triediffs"`; directory holding one immutable digest file per commit; lives inside the triefact tree, explicitly excluded from evidence collection to avoid feedback loops.
- `max_entries`: oldest digest files are pruned from `diffs_dir` when this cap is exceeded.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config fingerprint=12a4bc43770566272abef892091eaa23d8f73dc8d31081651a1acd5706d8cb84 body_fp=ce0aeaeb0b8b5c2ef8819a76130f23f311635843f8868db6496cce005624da50 source_ref=510dbd7539ccb0936ec4f10c68b018717709082e role=config -->
## `class Config`

Root configuration dataclass aggregating all subsection configs, with classmethods to construct from a dict, a TOML file path, or by walking up the directory tree.

- `from_dict`: silently drops `models.edits` and top-level `[edits]`/`[languages]` keys from legacy configs; now also populates the `resolver` field.
- `find_and_load`: raises `ConfigNotFoundError` if no `trie.toml` is found in `start` or any ancestor; returns `(Config, config_dir)` where `config_dir` is the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=4cb497239f0a398bed137fee387e56f6208055e895b78ab78d1bdc4ee9745a28 body_fp=1b55ff0d56608905edc9c2bbe3e78d2e091d9db12f823bb41a48e3b3e5e55867 source_ref=510dbd7539ccb0936ec4f10c68b018717709082e role=config -->
## `def from_dict(cls, data: dict) -> Config: # NOTE: [edits] and [languages] sections (and models.edits) in existing # trie.toml files are silently ignored — they configured the removed # code-generation pipeline (the patch pipeline is an intent store now).`

Creates a `Config` instance from a dictionary, silently ignoring `[edits]`, `[languages]`, and `models.edits` sections from legacy trie.toml files, and populating all remaining fields including `diff` and `resolver` from the input dict.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=442177abeb5c3de45896d7e0eb434e43cf594d179b17f6fc8085e6e6ef2d2ec4 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
## `def load(cls, path: Path) -> Config`

Config.load parses a TOML file at the given path and returns a Config instance.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=51c03c958b72c25c012d0631b6d84a58b2512093119863c9d457d05eb639ecc6 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
## `def find_and_load(cls, start: Path) -> tuple[Config, Path]`

Config classmethod walks up directory tree from start path to find and load trie.toml configuration file.

• Returns tuple of (Config instance, config directory path)
• Raises ConfigNotFoundError if no trie.toml found in start or parent directories
<!-- trie:end -->
<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=eb33adf4c1c9b5aa8eea6f040ec0f9cb782e9c925ee8206aa1a772a094ee879d source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
## `class ConfigNotFoundError(FileNotFoundError)`

Exception raised when Config.find_and_load cannot locate a trie.toml file in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:DEFAULT_CONFIG_TOML fingerprint=426323ff65b0749777c80398d4edf83a217cb91dd0f74a5eff4d84de9b0e4441 body_fp=588d0afe84fba88f4a2e835266d9b7764728d5b0011f27ed48f85ddcd1f6a4f7 role=config-management -->
Default TOML configuration template string used to generate initial `trie.toml` files, covering all configurable sections — scope, triefacts, models, cascade, sync, mcp, edits, diff, and debug — with inline documentation for each knob. The `[diff]` section is included as a commented-out block to document the digest knobs (`narrative`, `write_path`, and `max_entries`) that control how `trie diff --write` maintains the `TRIE_DIFF.md` session digest, making these options discoverable without activating them by default.
<!-- trie:end -->