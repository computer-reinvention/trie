---
trie_version: 0.1.5
source: trie/config.py
file_fingerprint: f291c477946f706816fb0189693cef21acb0ed4df2e764d79014db06e80c8bf6
last_synced_at: '2026-06-06T14:02:58Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-358
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
  lines: 79-109
- kind: class
  qualified_name: trie/config:Debug
  lines: 113-132
- kind: class
  qualified_name: trie/config:Mcp
  lines: 136-192
- kind: class
  qualified_name: trie/config:Config
  lines: 196-245
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 208-223
- kind: method
  qualified_name: trie/config:Config.load
  lines: 226-229
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 232-245
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 248-249
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 252-357
incoming_refs: 188
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
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=042e1678d51e63de3de50f0abb830138d4b678a5fb1cb49d024bcb1909843280 body_fp=5c5884eaa3d6be1aac461f511a163cadc94d636e92c667435bcd341db9bf6b75 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Stores the trie library version string.

- `version`: Current version of the trie library
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=f0981331a4d23c70eaa4a1b4852d41bf666781c20075471a91517687e833a47b source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Defines file inclusion and exclusion patterns for trie's source scanning scope.

- `include`: glob patterns for files to process (defaults to all Python files)
- `exclude`: glob patterns for files to skip (defaults to common build/cache directories)
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
<!-- trie:section symbol=trie/config:Cascade fingerprint=9a685f1d6a6008e1bc16ca1ea29a753bdf3f64fc881a94cb31cf485d6ee42b01 body_fp=1d7b8a2a09490d3154cf72f4f010ef0739004c2e594ee3387432e088d9c0090c source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configuration for cascade analysis that determines incremental sync depth and hub symbol handling.

- `max_judgments`: hard cap on pre_filter_cascade calls per apply run
<!-- trie:end -->
<!-- trie:section symbol=trie/config:LspBackend fingerprint=b9c2864ea0cd6bcd2cdb18b855ee096c71423d6f619e3d8132b5a2ee64091d4a body_fp=8d00d617494f8391cb23f825be93d94c4eff427ca707b5cca97e557956c5b1ed source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configures a language server backend for diagnostics during patch application.

- `output_format`: determines stdout parsing format - "pyright" or "ruff"
- `exit_ok_codes`: exit codes interpreted as "no diagnostics found"
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Edits fingerprint=981676998916a9eb811467dfc40523109336af054a86d94aaa07898c1fdfc1d0 body_fp=675a8133bfc2f789d009cc960146c2a8499eecf68a828726f3a008b27a4181ff source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Configures patch-apply pipeline and LSP backend settings for code editing operations.

- `lsp_max_retries`: maximum retry attempts when LSP diagnostics fail
- `lsp_backends`: ordered list of language server configurations, first available backend is used
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Sync fingerprint=1d2cc3d22d744e4bc691bb719df31b592f4ec7e83562507eb0aa5afea030a84c body_fp=32e299dc9fef9f368e1794a54ae3a69995384c46d45f5f95ff937ce11862130f source_ref=6e0c09981b45ff5a650aded507505c52801d4c8d role=config -->
Configuration dataclass for controlling parallelism and retry behavior during sync operations.

- `concurrency`: parallel per-symbol LLM calls within a single file (default 4)
- `file_workers`: concurrent files being processed (default 8)  
- `max_inflight_requests`: global cap on total concurrent LLM calls (default 8)
- `max_retries`: retry attempts before propagating rate-limit errors (default 8)
- `retry_base_delay_seconds`: base exponential backoff delay (default 1.0)
- `retry_cap_seconds`: maximum backoff delay (default 60.0)
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
<!-- trie:section symbol=trie/config:Config fingerprint=39cdd983275490488052db937ca90d6b40f612dddf42cf46502e0a832b7dade6 body_fp=810d52d6eaae856bf9fafdbecce3ff43ce41b64e37981496dcbbb568759030e3 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Root configuration dataclass aggregating all trie settings with TOML loading and file discovery methods.

- `from_dict`: creates Config from parsed TOML data, handling nested LspBackend instantiation
- `load`: reads and parses TOML file at given path 
- `find_and_load`: walks up directory tree to locate trie.toml, returns config and project root
<!-- trie:end -->
<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=1b59860b1ffda417aa3d89ae97b50e688620da830b00253b94767622bf77c05d body_fp=371aded0106d5e41dbd1966059a46ee160739822820aa6d074a018bf5ec6efd1 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Creates Config instance from dictionary data, handling special deserialization for LspBackend objects in edits section.
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
<!-- trie:section symbol=trie/config:DEFAULT_CONFIG_TOML fingerprint=426323ff65b0749777c80398d4edf83a217cb91dd0f74a5eff4d84de9b0e4441 body_fp=b42d949487ff91589ee223e4dc92306a5b14caaa4c01ca7233593f01345255d5 source_ref=59b06d551b5158372b2b8155ef9e26fb80cec296 role=config-management -->
Default TOML configuration template string used to generate initial `trie.toml` files.
<!-- trie:end -->