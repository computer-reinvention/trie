---
trie_version: 0.1.0
source: trie/config.py
file_fingerprint: a5c738ec75736a93a83a6c0e2ff45816eb5403df4c70e8fbb88251cdc523c785
last_synced_at: '2026-05-14T18:31:11Z'
defines:
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
  qualified_name: trie/config:Debug
  lines: 45-64
- kind: class
  qualified_name: trie/config:Mcp
  lines: 68-90
- kind: class
  qualified_name: trie/config:Config
  lines: 94-135
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 104-113
- kind: method
  qualified_name: trie/config:Config.load
  lines: 116-119
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 122-135
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 138-139
incoming_refs: 88
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=43460a16db027d61c4297084d70ce0d1e70048e3c983aba83ed17fbd4935301a body_fp=fc099c55e56a7cbf7ea5a31d4965af5f5003dcad2f1ee09cc25a0896fe818bc3 -->
## `TrieMeta`

Dataclass holding the trie configuration version string.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=b3b1152151575a3929b7f163408dfcf58867b88055ac5288f00fca832210ae09 -->
## `Scope`

Define file inclusion and exclusion glob patterns for the source scan.

- `include`: defaults to `["**/*.py"]`
- `exclude`: defaults to common noise dirs (`__pycache__`, `.venv`, `build`, `dist`)
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=d18962b3781d45f1104269411b89d6b259d2e0f9581f6de2875d1d65ccbd998c -->
## `Triefacts(root: str = "triefacts", source_root: str = ".")`

Dataclass holding output directory and source root paths for triefact generation.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Models fingerprint=abf55624d4d046500cb6caf33a90cb62e33c0a2f319cfcb63d35d6a242726335 body_fp=a646ca6208b8882df9483e7d90482f586b393dae4406197e0df245e1be9b5313 -->
## `Models`

Dataclass holding model identifier strings for bootstrap and cascade triefact generation.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Cascade fingerprint=0e7b3a716fd306199ce4ccbb537cb901c77f5a484dcc79d8132d1177378c9597 body_fp=c93af3cec7aa32ea7ff16d0a2379b19de65d7d87e12297fd04775e734aca1cb4 -->
## `Cascade`

Configure reference-graph traversal defaults for incremental sync operations.

- `default_depth`: how many hops from changed symbols to re-document
- `hub_symbol_threshold`: symbols with more inbound refs than this are capped at depth 0
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Mcp fingerprint=08297d135a9e1a2021203c4386b558e9d0f34e51b60a346b43ddd0f6c8bdec2b body_fp=4391e9994b64fa0db1ed74df7737eeacf090584df2e7e5b43f25dc54b66b0abf -->
## `Mcp`

Configure server-side behavioural knobs for the MCP agent tools: `locate`, `explain`, and `walk`.

- `locate_default_rank_by`: accepts `"public_first"`, `"inbound_count"`, or `"alphabetical"`
- `explain_max_neighbours_per_direction`: `0` means unlimited
- `explain_prose_max_chars`: `0` means unlimited
- `walk_hub_threshold`: mirrors `Cascade.hub_symbol_threshold`
- `walk_prose_at_depth`: `0` disables prose on walk nodes
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config fingerprint=4e975acd9b360d1711641a075f5065301e2d739231ad404c67fc60059164632e body_fp=b70d4f8aa11ac7103c24e45e8d0fcb30aa6177225a95b498d890046c4ebdd723 -->
## `Config`

Aggregate configuration dataclass combining all subsection configs, with TOML loading helpers.

- `from_dict(data)`: construct from a raw parsed-TOML dict
- `load(path)`: parse a `trie.toml` file at the given path
- `find_and_load(start)`: walk up from `start` to find `trie.toml`; returns `(Config, config_dir)`
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=6018209163d6c185b3b2b8f92d4f9b1c2c356984c53fd36e5b9e05cd5ed37366 body_fp=5950b131f7183e8ca2fe6f05a0a557304101ba150695ed94d1e65d218a2d8dfd -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` from a plain dictionary, mapping each top-level key to its corresponding dataclass section.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=88eec6604a3cbdb1b8714dffc35b8dd1eba6d0a046fff4479f60ceb49d85584b -->
## `Config.load(cls, path: Path) -> Config`

Load and parse a `trie.toml` file at the given path into a `Config` instance.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=4498f82aec28c75a29c47ad25c74ce0809fb5b3ff6ea28371b9fdd371c981d03 -->
## `Config.find_and_load(cls, start: Path) -> tuple[Config, Path]`

Walk up the directory tree from `start` to find and load the nearest `trie.toml`.

- `start`: directory from which upward search begins
- Returns `(config, config_dir)` where `config_dir` is the `trie.toml` parent, used as project root
- Raises `ConfigNotFoundError` if no `trie.toml` exists in `start` or any ancestor
<!-- trie:end -->

<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6256b4341c270158e59803de88707514d739be49fb35d19064b2af73d181fcdd -->
## `ConfigNotFoundError(FileNotFoundError)`

Raised when no `trie.toml` is found during upward directory traversal.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Debug fingerprint=74eb562287f2d40b4d10de5eeca4500a9792b9df3b3037d4e875d64dc1bcd8cc body_fp=b8e41ebbd79947556dc6587935dd6b8bb394c6cab78dbc14e5652ee11eb50ffa -->
## `Debug`

Configure telemetry behaviour for trie's internal event logging.

- `enabled`: overridable at runtime via `TRIE_DEBUG` env var
- `log_path`: relative to project root, or absolute
- `capture_responses`: off by default; response bodies are large
- `redact_keys`: field paths to elide from logged events
<!-- trie:end -->