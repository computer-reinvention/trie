---
trie_version: 0.1.9
source: trie/config.py
file_fingerprint: f9d241cde408b238e3e7f5bab4000a0a1c5201985a4d168900b6901c179d5643
last_synced_at: '2026-07-25T06:05:53Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-482
- kind: class
  qualified_name: trie/config:TrieMeta
  lines: 9-10
- kind: class
  qualified_name: trie/config:Scope
  lines: 14-30
- kind: class
  qualified_name: trie/config:Triefacts
  lines: 34-36
- kind: class
  qualified_name: trie/config:Models
  lines: 40-43
- kind: class
  qualified_name: trie/config:Cascade
  lines: 47-53
- kind: class
  qualified_name: trie/config:LspBackend
  lines: 57-73
- kind: class
  qualified_name: trie/config:Edits
  lines: 77-116
- kind: class
  qualified_name: trie/config:LanguageConfig
  lines: 120-128
- kind: class
  qualified_name: trie/config:Sync
  lines: 132-176
- kind: class
  qualified_name: trie/config:Debug
  lines: 180-199
- kind: class
  qualified_name: trie/config:Mcp
  lines: 203-259
- kind: class
  qualified_name: trie/config:Diff
  lines: 263-290
- kind: class
  qualified_name: trie/config:Config
  lines: 294-354
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 308-332
- kind: method
  qualified_name: trie/config:Config.load
  lines: 335-338
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 341-354
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 357-358
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 361-481
incoming_refs: 223
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
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=54d24a44672076f46996a3143c80a8d75b426482d4256cacba0f6d5c7f7584f3 body_fp=5c5884eaa3d6be1aac461f511a163cadc94d636e92c667435bcd341db9bf6b75 source_ref=64675d426ee121ee07f6aca6b23643e1d1ad5991 role=model -->
Stores the trie library version string.

- `version`: Current version of the trie library
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Scope fingerprint=963e53b5f6fe65f50bfdb5957fc60ae9c740976cf6fb421f55185f3d760e6b83 body_fp=6ff57d75e40b0bc0ac222762573131c3a976c8d66cadd9c009329b5c53b86fe0 source_ref=64675d426ee121ee07f6aca6b23643e1d1ad5991 role=config -->
Defines file inclusion and exclusion patterns for trie's source scanning scope.

- `include`: glob patterns for files to process (defaults to Python, TypeScript, and TSX files)
- `exclude`: glob patterns for files to skip (defaults to hidden dirs, pycache, node_modules, build/dist)
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=597421696508c0e16a51d04c5d23089ed022da24e0d2df885d1c300a638848e1 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configuration for triefact output paths and source tree location.

- `root`: Directory where generated Markdown triefacts are stored, mirroring source structure
- `source_root`: Path to source tree root relative to config file location
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Models fingerprint=e882ddd5e301a630dc1f077967f9ec3f48511c22931d0bd32de2d39512854871 body_fp=112f6bc4a0a4cafa703e88491dc0d6829bfc57d431041d0a77dd1968e0486f36 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Specifies default model identifiers for different trie operations.

- `bootstrap`: Model used for initial triefact generation
- `cascade`: Model used for cascaded reference updates  
- `edits`: Model used for patch application and code fixes
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Cascade fingerprint=f75ec172dcb1f95fecfbf0a537fe3f1fed8dd874f90ff0fed3493c9b45b0b52f body_fp=ba914fb87d9a2eaf94e9bfa6080e00cd81768c53283d16f9846c9c3c65748ad6 source_ref=804cbe955566bb7dc234ec68033f1e84827f016f role=config -->
Configuration for cascade analysis that determines incremental sync depth and hub symbol handling.

- `max_judgments`: hard cap on pre_filter_cascade calls per apply run
- `surface_unresolved`: surface second-order cascades as ApplyReport.unresolved rather than chasing in-pipeline
<!-- trie:end -->
<!-- trie:section symbol=trie/config:LspBackend fingerprint=b9c2864ea0cd6bcd2cdb18b855ee096c71423d6f619e3d8132b5a2ee64091d4a body_fp=8d00d617494f8391cb23f825be93d94c4eff427ca707b5cca97e557956c5b1ed source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configures a language server backend for diagnostics during patch application.

- `output_format`: determines stdout parsing format - "pyright" or "ruff"
- `exit_ok_codes`: exit codes interpreted as "no diagnostics found"
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Edits fingerprint=a36dfe52ee715aae6c469e703a0098d9e87c9452bd686375f6932169ecfa2f44 body_fp=4b127f4d46af4f4af3cb65ca4219f797062affd2c614dc38963e63baebdbb27c role=config-management -->
Configures the patch-apply pipeline and LSP backend settings for code editing operations, including retry limits, LSP backend definitions, commit failure handling, and the edit generation backend (`"llm"`, `"opencode"`, or `"agent"`), where `"agent"` causes patch apply to return an agent-executable worklist instead of performing inline code generation.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:LanguageConfig fingerprint=53c630a38d44498a9e194e86c35198bb9a6d7eec5f7143a19503cfb475db89f8 body_fp=7ea5116333d3272467cb2cc54cd3c40fdc54b238da538ff650de7611b481d532 source_ref=64675d426ee121ee07f6aca6b23643e1d1ad5991 role=config -->
Dataclass holding per-language config overrides, keyed by backend name (e.g. `"typescript"`).

- `lsp_backends`: replaces the language backend's default checkers when non-empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Sync fingerprint=a93ade6800fe0ee90ea2e067bb805b9d35056a5197ebda7f91e37178abd868a8 body_fp=2013801001ddde408edcac871ea3d7fca942f2015fe17bb0eafaaf5ae6d96af4 source_ref=073d45150b29b0a304f40de8e0d78addf413edcc role=config -->
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
<!-- trie:section symbol=trie/config:Debug fingerprint=74eb562287f2d40b4d10de5eeca4500a9792b9df3b3037d4e875d64dc1bcd8cc body_fp=2667f14db51f0ee544a4a8580493f37ecbb1d507cde52c75f16c447bcff567c8 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configures telemetry logging for trie operations, controlled by the TRIE_DEBUG environment variable.

- `enabled`: defaults to False but overridden by TRIE_DEBUG env var
- `log_path`: JSONL file location, overridden when TRIE_DEBUG is a path
- `log_to_stderr`: mirrors events to stderr for development debugging
- `capture_responses`: includes full LLM response bodies in logs (large data)
- `redact_keys`: field paths to elide from logged data
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Mcp fingerprint=a3cc2e17786817953b72dd705739ff8061b22a2cb075f22a8ef2fc154ae66403 body_fp=03cb69ecda486cd711a6d42b1ccb4a4496b9262f65c6532b92eff329bd693a24 source_ref=d781ba02a70d89cf4245db2d94ab73c09402c2b8 role=config -->
Configuration dataclass for MCP agent tool behaviors including grep, read and trace settings.

- `grep_max_limit`: Maximum number of results returned by grep tool (default 50)
- `grep_fallback_max_files`: File limit for ripgrep fallback when symbol search fails (default 200)
- `grep_fallback_match_limit`: Symbol limit for fallback results after hub-ranking (default 30)
- `fuzzy_cutoff`: Minimum rapidfuzz score (0-100) for fuzzy matching inclusion (default 45.0)
- `fuzzy_prose_pre_filter`: Score threshold before reading triefact prose from disk (default 30.0)
- `read_max_neighbours_per_direction`: Neighbor limit per direction, 0 for unlimited (default 0)
- `trace_max_depth`: Maximum traversal depth for trace operations (default 5)
- `trace_hub_threshold`: Node count threshold for hub skipping in trace (default 50)
- `trace_max_nodes`: Maximum nodes returned by trace operations (default 200)
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Diff fingerprint=02d7b7c4a34c801654ba7e7ba0c3ee31d29e464c963c3cb640a04f17864788fb body_fp=747554c26372c258e537318bfc51b807c9efe899851acdf68fe92327964fd2fb source_ref=18c0228ab22574981e4c5031db011c5783d28510 role=config -->
Dataclass holding configuration for the per-commit digest system, where each commit produces one immutable file under `diffs_dir` and `write_path` is a symlink to the latest.

- `narrative`: when `True`, prepends an LLM-generated summary; falls back to raw evidence if no API key is available.
- `write_path`: symlink at project root pointing at the latest digest file; changing it also requires updating the pre-commit hook.
- `diffs_dir`: defaults to `"triefacts/triediffs"`; directory holding one immutable digest file per commit; lives inside the triefact tree, explicitly excluded from evidence collection to avoid feedback loops.
- `max_entries`: oldest digest files are pruned from `diffs_dir` when this cap is exceeded.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config fingerprint=bd03893efd146b7e3cae17bf6c86c1cc07e9115f2d9d65d1f2606be347c473ac body_fp=a2248608c74549bf774cae231f316786139ed9358c20f2a01e748e1e07d377b0 role=config-management -->
Root configuration dataclass aggregating all trie settings — including trie metadata, scope, triefacts, models, cascade, sync, MCP, debug, edits, diff, and per-language overrides — with TOML loading via `load`, upward directory-tree discovery via `find_and_load`, and structured deserialization from raw dictionaries via `from_dict`, which handles nested `LspBackend` and `LanguageConfig` instantiation as well as the new `[diff]` section.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=079ecac63c0bb42bb3272ed19038c26921a7a73a721c2d25d053f3c5cddf65b0 body_fp=f0a76767909d8d06244fc6aed85734b31fea3472b4f2e8a606814cab9d63fd6b source_ref=b09697b8931aaceed5b512251de7a0608042367e role=config -->
Creates a `Config` instance from a dictionary, deserializing `LspBackend` objects in edits and per-language `LanguageConfig` entries from the `languages` section, and populating `diff` from `data["diff"]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=77e4ce7fa1e8c65f89b23d443add922c44475b46ec65cdd9049ff7b2960fc2e8 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Config.load parses a TOML file at the given path and returns a Config instance.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=352f098bb7c212725a557f9d5585ddadf5c46a609462cdb1fbfd05ab47a4db64 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Config classmethod walks up directory tree from start path to find and load trie.toml configuration file.

• Returns tuple of (Config instance, config directory path)
• Raises ConfigNotFoundError if no trie.toml found in start or parent directories
<!-- trie:end -->
<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=f6e3f032efc4f68f4c9873696ebed4665095050944f2bd0a1764c6ba230f4219 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Exception raised when Config.find_and_load cannot locate a trie.toml file in the directory tree.
<!-- trie:end -->
<!-- trie:section symbol=trie/config:DEFAULT_CONFIG_TOML fingerprint=426323ff65b0749777c80398d4edf83a217cb91dd0f74a5eff4d84de9b0e4441 body_fp=588d0afe84fba88f4a2e835266d9b7764728d5b0011f27ed48f85ddcd1f6a4f7 role=config-management -->
Default TOML configuration template string used to generate initial `trie.toml` files, covering all configurable sections — scope, triefacts, models, cascade, sync, mcp, edits, diff, and debug — with inline documentation for each knob. The `[diff]` section is included as a commented-out block to document the digest knobs (`narrative`, `write_path`, and `max_entries`) that control how `trie diff --write` maintains the `TRIE_DIFF.md` session digest, making these options discoverable without activating them by default.
<!-- trie:end -->