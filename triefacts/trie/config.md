---
trie_version: 0.1.2
source: trie/config.py
file_fingerprint: 0d55561161485e469d80188ad026c8199513be1dfc184a5320ebebec2466b9ff
last_synced_at: '2026-05-19T15:24:07Z'
defines:
- kind: module
  qualified_name: trie/config:__module__
  lines: 1-267
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
  lines: 92-127
- kind: class
  qualified_name: trie/config:Config
  lines: 131-174
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 142-152
- kind: method
  qualified_name: trie/config:Config.load
  lines: 155-158
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 161-174
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 177-178
- kind: constant
  qualified_name: trie/config:DEFAULT_CONFIG_TOML
  lines: 181-266
incoming_refs: 146
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=3a9f3f9b594eb2bc004d5ab6492991cf167ef4b9ae7b65e2738917beda05b61b body_fp=fc099c55e56a7cbf7ea5a31d4965af5f5003dcad2f1ee09cc25a0896fe818bc3 source_ref=91c1f83393b4cceef8bfb88e62c64c65b755bf42 -->
## `TrieMeta`

Dataclass holding the trie configuration version string.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=b3b1152151575a3929b7f163408dfcf58867b88055ac5288f00fca832210ae09 source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Scope`

Define file inclusion and exclusion glob patterns for the source scan.

- `include`: defaults to `["**/*.py"]`
- `exclude`: defaults to common noise dirs (`__pycache__`, `.venv`, `build`, `dist`)
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=d18962b3781d45f1104269411b89d6b259d2e0f9581f6de2875d1d65ccbd998c source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Triefacts(root: str = "triefacts", source_root: str = ".")`

Dataclass holding output directory and source root paths for triefact generation.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Models fingerprint=abf55624d4d046500cb6caf33a90cb62e33c0a2f319cfcb63d35d6a242726335 body_fp=a646ca6208b8882df9483e7d90482f586b393dae4406197e0df245e1be9b5313 source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Models`

Dataclass holding model identifier strings for bootstrap and cascade triefact generation.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Cascade fingerprint=0e7b3a716fd306199ce4ccbb537cb901c77f5a484dcc79d8132d1177378c9597 body_fp=c93af3cec7aa32ea7ff16d0a2379b19de65d7d87e12297fd04775e734aca1cb4 source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Cascade`

Configure reference-graph traversal defaults for incremental sync operations.

- `default_depth`: how many hops from changed symbols to re-document
- `hub_symbol_threshold`: symbols with more inbound refs than this are capped at depth 0
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Mcp fingerprint=3c60269ba347b83cd8ee1964fa80392c68b52e4443eb19fea19a629b8c69345a body_fp=0f73080f70cc7eef00ce74e0b544dec0515fe67221fc49bc155491bbdeb40566 source_ref=792b9254fc55c5a78e54944bc93a125b426d9104 -->
## `Mcp`

Configure server-side behavioural knobs for the MCP agent tools: `grep`, `read`, and `trace`.

- `grep_default_rank_by`: accepts `"public_first"`, `"inbound_count"`, or `"alphabetical"`
- `grep_fallback_max_files`: max in-scope files searched when no symbol-name match found
- `grep_fallback_match_limit`: cap on candidates returned after hub-ranking fallback; default 30; fallback never refuses as too noisy
- `read_max_neighbours_per_direction`: `0` means unlimited
- `read_prose_max_chars`: `0` means unlimited
- `trace_hub_threshold`: mirrors `Cascade.hub_symbol_threshold`
- `trace_prose_at_depth`: `0` disables prose on trace nodes
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config fingerprint=a550e09883e6c18df41905160eff158c7967ad28acfc1bbf54776be19224fac3 body_fp=d19d934b11a1133b82aa5d159576682fd2e297204fa1e979200d0683d985bf63 source_ref=e2aa05d59799353b5474d1cf35f500bdfbc368f9 -->
## `Config`

Aggregate configuration dataclass combining all subsection configs, with TOML loading helpers.

- `from_dict(data)`: construct from a raw parsed-TOML dict; now includes `sync` field
- `load(path)`: parse a `trie.toml` file at the given path
- `find_and_load(start)`: walk up from `start` to find `trie.toml`; returns `(Config, config_dir)`
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=2a49e1d83738c09e61cd41f62971e3bc5e6c4e3affac719b5f5b3a0498c717dc body_fp=5950b131f7183e8ca2fe6f05a0a557304101ba150695ed94d1e65d218a2d8dfd source_ref=e2aa05d59799353b5474d1cf35f500bdfbc368f9 -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` from a plain dictionary, mapping each top-level key to its corresponding dataclass section.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=88eec6604a3cbdb1b8714dffc35b8dd1eba6d0a046fff4479f60ceb49d85584b source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Config.load(cls, path: Path) -> Config`

Load and parse a `trie.toml` file at the given path into a `Config` instance.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=4498f82aec28c75a29c47ad25c74ce0809fb5b3ff6ea28371b9fdd371c981d03 source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Config.find_and_load(cls, start: Path) -> tuple[Config, Path]`

Walk up the directory tree from `start` to find and load the nearest `trie.toml`.

- `start`: directory from which upward search begins
- Returns `(config, config_dir)` where `config_dir` is the `trie.toml` parent, used as project root
- Raises `ConfigNotFoundError` if no `trie.toml` exists in `start` or any ancestor
<!-- trie:end -->

<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6256b4341c270158e59803de88707514d739be49fb35d19064b2af73d181fcdd source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `ConfigNotFoundError(FileNotFoundError)`

Raised when no `trie.toml` is found during upward directory traversal.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Debug fingerprint=74eb562287f2d40b4d10de5eeca4500a9792b9df3b3037d4e875d64dc1bcd8cc body_fp=b8e41ebbd79947556dc6587935dd6b8bb394c6cab78dbc14e5652ee11eb50ffa source_ref=435b779093e30070dbf454dc787d8b346cc4ebc9 -->
## `Debug`

Configure telemetry behaviour for trie's internal event logging.

- `enabled`: overridable at runtime via `TRIE_DEBUG` env var
- `log_path`: relative to project root, or absolute
- `capture_responses`: off by default; response bodies are large
- `redact_keys`: field paths to elide from logged events
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Sync fingerprint=6e78bc409faa3564065bef1b86229e39b56fce1ec430f52e79b1e562be89d6fe body_fp=78c3e901fbf90ff552b71a69efb20c994abeaabd9bfb2b5280c96edc9dffa7bd source_ref=e2aa05d59799353b5474d1cf35f500bdfbc368f9 -->
## `Sync`

Control per-file sync parallelism and model-client retry behaviour.

- `concurrency`: parallel LLM calls per file; 1 disables parallelism
- `retry_base_delay_seconds`: exponential-backoff base for 429/529 retries
- `retry_cap_seconds`: maximum backoff delay before propagating error
<!-- trie:end -->

<!-- trie:section symbol=trie/config:DEFAULT_CONFIG_TOML fingerprint=426323ff65b0749777c80398d4edf83a217cb91dd0f74a5eff4d84de9b0e4441 body_fp=ad5e7a7f545ea257b0e6b6bddf6d6234a9764d9a0494fce62e643fc80772739a source_ref=049680f42014e6367cc29b3f2c95407827b715e4 -->
## `DEFAULT_CONFIG_TOML: str`

Template TOML string containing fully-commented default configuration for a `trie.toml` project file.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=35129a2db5d510fbea595aa81525b50427443bc38e437108ed8d37bd8df7e487 source_ref=049680f42014e6367cc29b3f2c95407827b715e4 -->
## `config`

Define all configuration dataclasses and loading logic for `trie.toml` project configuration.

- `Config.from_dict`: constructs a `Config` from a raw TOML-parsed dict
- `Config.load`: reads and parses a `trie.toml` at the given `Path`
- `Config.find_and_load`: walks up from `start` returning `(Config, project_root_dir)`
- `ConfigNotFoundError`: raised when no `trie.toml` is found in the directory tree
- `DEFAULT_CONFIG_TOML`: ready-to-write string for `trie init`
<!-- trie:end -->