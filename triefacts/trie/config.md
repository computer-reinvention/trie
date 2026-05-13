---
trie_version: 0.1.0
source: trie/config.py
file_fingerprint: 367c96aaa1d094aefecbb071a68e4c30fced3c090cdbc9fecd83cf1fd686f39e
last_synced_at: '2026-05-12T18:29:23Z'
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
  qualified_name: trie/config:Config
  lines: 45-82
- kind: method
  qualified_name: trie/config:Config.from_dict
  lines: 53-60
- kind: method
  qualified_name: trie/config:Config.load
  lines: 63-66
- kind: method
  qualified_name: trie/config:Config.find_and_load
  lines: 69-82
- kind: class
  qualified_name: trie/config:ConfigNotFoundError
  lines: 85-86
incoming_refs: 84
outgoing_refs: 0
---
<!-- trie:section symbol=trie/config:TrieMeta fingerprint=43460a16db027d61c4297084d70ce0d1e70048e3c983aba83ed17fbd4935301a body_fp=712d90773a00e84ec127450f7adc73ecdd8f904ac9682d1a28a1707b5abd5c7c -->
## `TrieMeta(version: str = "0.1.0")`

Dataclass holding trie project metadata, currently just the version string.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Scope fingerprint=6cbb564ec0c0b501db7e8911984bf6acfafebeb45e6a2eebfa0290af5bc64ac9 body_fp=6bf6157478cdb8a3d167014a19adac115d89df3a74e6d9c8135cb51f98e8c7a8 -->
## `Scope`

Define file inclusion/exclusion glob patterns for source discovery.

- `include`: defaults to `["**/*.py"]`
- `exclude`: defaults to ignoring `__pycache__`, `.venv`, `build`, and `dist` trees
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Triefacts fingerprint=84cd9d09bda2f42fbf759b0a2513c408f1fb2318a52590091926390f71f50d50 body_fp=867d9de0cdf9fe238eff5af650185a2749827626611963174aa94e7b2ba03ab8 -->
## `Triefacts`

Configure output directory and source root for the generated triefact tree.

- **`root`**: directory where generated Markdown files are written.
- **`source_root`**: source tree root, resolved relative to the config file.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Models fingerprint=abf55624d4d046500cb6caf33a90cb62e33c0a2f319cfcb63d35d6a242726335 body_fp=a773da18b73cec7f5f6311f9c63d8e6807374fbd499a65da07a291b6068f2ca4 -->
## `Models`

Dataclass holding model identifiers for bootstrap and cascade documentation generation stages.

- **`bootstrap`**: model used for initial triefact generation.
- **`cascade`**: model used for incremental cascade updates.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Cascade fingerprint=0e7b3a716fd306199ce4ccbb537cb901c77f5a484dcc79d8132d1177378c9597 body_fp=f2560babf997ff4fb069b510bfe3bc296ec0a614880c6748aaec81bc7f4d356a -->
## `Cascade(default_depth: int = 1, hub_symbol_threshold: int = 20)`

Dataclass holding cascade reference-graph traversal settings.

- `hub_symbol_threshold`: symbols with more inbound refs than this are capped at depth 0.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config fingerprint=092fa4241507d5cde1d22e7ef6c6461f59f26b972f2dcb747b6e7353d3ccf244 body_fp=dc72a5e3340b7312873030134f6a74ef22c381bcd22d6861abfefc6aefb0f916 -->
## `Config`

Top-level configuration dataclass aggregating all trie settings sections.

- `from_dict(data)`: construct from a raw TOML-parsed dict, using section defaults for missing keys
- `load(path)`: parse a TOML file at `path` and return a `Config`
- `find_and_load(start)`: walk up from `start` to find `trie.toml`; returns `(Config, config_dir)` or raises `ConfigNotFoundError`
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.from_dict fingerprint=fb0ad61e34d984da8e8cad19320d9da716d4037da487e116da21654796bfbe78 body_fp=2bf0979978e6c0d0bf7a055ac2e18ad1ffcc1ea64610235eb2b096aac13bbb5b -->
## `Config.from_dict(cls, data: dict) -> Config`

Construct a `Config` from a nested dictionary, mapping each top-level key to its corresponding dataclass section.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.load fingerprint=5365299d7ecf0cdb6ae8bfad33855d997debd906c3d769b616f66b3f625a0f2b body_fp=6dae63ab6973f8ddb6b4b08e1aedd8d5fd96ad57cf32202562183a821cfa02c6 -->
## `Config.load(cls, path: Path) -> Config`

Parse a TOML file at `path` and return a `Config` instance.
<!-- trie:end -->

<!-- trie:section symbol=trie/config:Config.find_and_load fingerprint=aa065953b07157539253a6730a01aea9a6d2fb6f594dc2e94c3455328942d5e4 body_fp=c813cc7d259c0cb4dbf92cf1c6af8987f0f65ef29166870115c0a2f3ebb8e8e7 -->
## `Config.find_and_load(cls, start: Path) -> tuple[Config, Path]`

Walk up the directory tree from `start` to locate and load `trie.toml`.

- `start`: directory from which upward search begins
- Returns `(config, config_dir)` where `config_dir` is the `trie.toml` parent, used as project root
- Raises `ConfigNotFoundError` if no `trie.toml` found in `start` or any ancestor
<!-- trie:end -->

<!-- trie:section symbol=trie/config:ConfigNotFoundError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=bc918c2d873f650de69dcd7189e702ded1640fca32b381628c157c397951f887 -->
## `ConfigNotFoundError`

Raised when no `trie.toml` is found during upward directory traversal.
<!-- trie:end -->