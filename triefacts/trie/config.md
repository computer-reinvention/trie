---
trie_version: 0.1.0
source: trie/config.py
file_fingerprint: 9f0af96e163c73b22e79ee2758a555cb977b339bf8fff189ded61ea05796e80c
last_synced_at: '2026-05-14T17:25:40Z'
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
  qualified_name: trie/config:Mcp
  lines: 45-67
- kind: class
  qualified_name: trie/config:Config
  lines: 71-110
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 80-88
- kind: method
  qualified_name: trie/config:Config.load
  lines: 91-94
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 97-110
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 113-114
incoming_refs: 86
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=43460a16db027d61c4297084d70ce0d1e70048e3c983aba83ed17fbd4935301a body_fp=bc9414b9abc89da794009a987a52ac87930a819e13ddda9bd8b9560bfa16f2c2 -->
## `TrieMeta(version: str = "0.1.0")`

Dataclass holding trie project metadata, currently only the version string.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=ae10d5c827e0d29a2f30430ca93a5118597f6c1a90b09521a12f5d5339d0716f -->
## `Scope`

Define glob patterns controlling which files trie includes and excludes from analysis.

- `include`: defaults to `["**/*.py"]`
- `exclude`: defaults to common non-source dirs (`__pycache__`, `.venv`, `build`, `dist`)
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=f773f5b5678b98aa457df3c728dc288c6e9547181d3ad9343374e0e8a35f1dc5 -->
## `Triefacts(root: str = "triefacts", source_root: str = ".")`

Dataclass holding output and source root paths for the triefact tree.

- `root`: directory where generated Markdown triefacts are written.
- `source_root`: source tree root, relative to the project config file.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Models fingerprint=abf55624d4d046500cb6caf33a90cb62e33c0a2f319cfcb63d35d6a242726335 body_fp=a02fd59c9f5079344d0cbbb160a4f7ebb12f59cb6ca9f0332d461ef823a378a4 -->
## `Models(bootstrap: str = 'anthropic/claude-sonnet-4-6', cascade: str = 'anthropic/claude-sonnet-4-6')`

Store model identifiers for bootstrap and cascade triefact generation phases.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Cascade fingerprint=0e7b3a716fd306199ce4ccbb537cb901c77f5a484dcc79d8132d1177378c9597 body_fp=16b6a200f03fe99b647df461db6c328c61503f791d1cdd9062847033af411f51 -->
## `Cascade`

Configure cascade traversal behaviour for incremental sync.

- `default_depth`: reference-graph hops to traverse from a changed symbol.
- `hub_symbol_threshold`: symbols with more inbound refs than this are depth-0 only.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Mcp fingerprint=08297d135a9e1a2021203c4386b558e9d0f34e51b60a346b43ddd0f6c8bdec2b body_fp=c913c0c9e5999637ecb3f2ed7c7255f25f6745e44efca1e7dd6854999b049ca4 -->
## `Mcp`

Server-side configuration knobs for the MCP agent tools: `locate`, `explain`, and `walk`.

- `locate_max_limit`: max results returned by `locate`
- `locate_default_rank_by`: `"public_first"`, `"inbound_count"`, or `"alphabetical"`
- `explain_max_neighbours_per_direction`: `0` means unlimited
- `explain_prose_max_chars`: `0` means unlimited
- `walk_prose_at_depth`: `0` disables prose emission during walk
- `walk_hub_threshold`: mirrors `Cascade.hub_symbol_threshold`
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config fingerprint=ca2167c8e1550416b317abba5840ac91eb52127006eebaa8ed70c90fd6590350 body_fp=ac5bf01f98495a4c2d414eb0efaaf410fb808b426a90b6a185b86be4393dd69c -->
## `Config`

Aggregate configuration dataclass combining all trie subsections with TOML loading helpers.

- `from_dict(data)`: constructs `Config` from a raw parsed-TOML dict
- `load(path)`: reads and parses a TOML file at `path` into a `Config`
- `find_and_load(start)`: walks up from `start` to locate `trie.toml`; returns `(Config, config_dir)`
- `config_dir`: the directory containing `trie.toml`, used as project root for relative paths
- Raises `ConfigNotFoundError` if no `trie.toml` found in `start` or any ancestor
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=a5c8cbe96f34e67155d3a9298546b41ac8730998478c49a58b523b0b3d088600 body_fp=d7d3cca9719abbe70265f2853ef31b194556031e748eada977f363ca80c32145 -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` from a plain dictionary, mapping top-level keys to their respective dataclass sections.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=6dae63ab6973f8ddb6b4b08e1aedd8d5fd96ad57cf32202562183a821cfa02c6 -->
## `Config.load(cls, path: Path) -> Config`

Parse a TOML file at `path` and return a `Config` instance.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=5eefe47d08094e607e6e3eca1e277818b9d803f8853dbbdec33d0ce12e808b09 -->
## `Config.find_and_load(cls, start: Path) -> tuple[Config, Path]`

Walk up from `start` searching for `trie.toml`, returning the loaded config and its containing directory.

- `start`: directory from which upward search begins
- Returns `(config, config_dir)` where `config_dir` is the project root for resolving relative paths
- Raises `ConfigNotFoundError` if no `trie.toml` found in `start` or any ancestor
<!-- trie:end -->

<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6256b4341c270158e59803de88707514d739be49fb35d19064b2af73d181fcdd -->
## `ConfigNotFoundError(FileNotFoundError)`

Raised when no `trie.toml` is found during upward directory traversal.
<!-- trie:end -->