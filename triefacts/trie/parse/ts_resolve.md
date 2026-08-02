---
trie_version: 0.3.0
source: trie/parse/ts_resolve.py
file_fingerprint: ef1593d8c04e1cd74148adcad2406bb0b305cce66ab5fb9760fe093a41910e86
last_synced_at: '2026-07-25T00:55:40Z'
description: "TypeScript module-specifier resolution \u2014 config + syntax, never type inference."
defines:
- kind: module
  qualified_name: trie/parse/ts_resolve:__module__
  lines: 1-311
- kind: constant
  qualified_name: trie/parse/ts_resolve:_SOURCE_EXTS
  lines: 29-29
- kind: constant
  qualified_name: trie/parse/ts_resolve:_INDEX_BASENAMES
  lines: 30-30
- kind: constant
  qualified_name: trie/parse/ts_resolve:_PRUNE_DIR_NAMES
  lines: 36-36
- kind: function
  qualified_name: trie/parse/ts_resolve:_iter_config_files
  lines: 39-52
  signature: 'def _iter_config_files(source_root: Path, name_pattern: str) -> list[Path]'
- kind: function
  qualified_name: trie/parse/ts_resolve:_strip_jsonc
  lines: 55-64
  signature: 'def _strip_jsonc(text: str) -> str'
- kind: function
  qualified_name: trie/parse/ts_resolve:_load_jsonc
  lines: 67-71
  signature: 'def _load_jsonc(path: Path) -> dict | None'
- kind: function
  qualified_name: trie/parse/ts_resolve:_module_key
  lines: 74-85
  signature: 'def _module_key(path: Path, source_root: Path) -> str | None'
- kind: class
  qualified_name: trie/parse/ts_resolve:TsConfig
  lines: 89-94
  signature: class TsConfig
- kind: class
  qualified_name: trie/parse/ts_resolve:TsResolver
  lines: 98-197
  signature: class TsResolver
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver.build
  lines: 112-120
  signature: 'def build(cls, source_root: Path) -> TsResolver'
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver.resolve
  lines: 124-131
  signature: 'def resolve(self, specifier: str, from_file: Path) -> str | None'
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_uncached
  lines: 135-144
  signature: 'def _resolve_uncached(self, specifier: str, from_file: Path) -> str | None'
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_alias
  lines: 146-161
  signature: 'def _resolve_alias(self, specifier: str) -> str | None'
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_workspace
  lines: 163-175
  signature: 'def _resolve_workspace(self, specifier: str) -> str | None: # Exact package name, or a subpath import `@scope/pkg/sub`.'
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._probe
  lines: 177-197
  signature: 'def _probe(self, target: Path) -> str | None'
- kind: function
  qualified_name: trie/parse/ts_resolve:_apply_path_pattern
  lines: 200-217
  signature: 'def _apply_path_pattern(pattern: str, targets: list[str], specifier: str) -> str | None'
- kind: function
  qualified_name: trie/parse/ts_resolve:_collect_tsconfigs
  lines: 220-238
  signature: 'def _collect_tsconfigs(source_root: Path) -> list[TsConfig]'
- kind: function
  qualified_name: trie/parse/ts_resolve:_resolve_tsconfig_chain
  lines: 241-269
  signature: 'def _resolve_tsconfig_chain(path: Path, *, seen: set[Path]) -> dict | None'
- kind: function
  qualified_name: trie/parse/ts_resolve:_collect_workspace_entries
  lines: 272-289
  signature: 'def _collect_workspace_entries(source_root: Path) -> dict[str, Path]'
- kind: function
  qualified_name: trie/parse/ts_resolve:_package_entry_file
  lines: 292-310
  signature: 'def _package_entry_file(pkg_dir: Path, data: dict) -> Path | None'
incoming_refs: 17
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/ts_resolve:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4a27989d5ff0781924614f5dd29e702280ac08777a1c399a9aae283653ed6a2d source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
Resolves TypeScript import specifiers to slash-form project module keys without type inference or LLM calls.

- Layers: relative path → tsconfig `paths`/`baseUrl` → workspace `package.json` names → unresolved.
- File probing tries `.ts`, `.tsx`, `.d.ts`, then `<dir>/index.{ts,tsx,d.ts}`.
- `TsResolver` is the public entry point; build once per scan via `TsResolver.build(source_root)`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_SOURCE_EXTS fingerprint=f9c1461402f2e9608034ceb2e99381bd98d1f8910823a5d2dd5c19f444170a9e body_fp=3467aa084a18208c2de0dd217f1c988143e24c646dc6bae326dbc5e299e48735 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=config -->
Tuple of recognised TypeScript source file extensions used for extension probing and file-type checks.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_INDEX_BASENAMES fingerprint=e534b4ebf323745a4b0799695af189d84f033e91fb17787839333afda95515f9 body_fp=133794583c7971adbf681bb43e2c1a654532bd8dbab97db2f0fba3305f5bed7c source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=config -->
Tuple of barrel/index filenames probed when a specifier resolves to a directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_PRUNE_DIR_NAMES fingerprint=48a28c64032ff1d7697eafd744072228f218481083904e1e89bae5ba395e6142 body_fp=e64f174efe6590c84c0ef1812cb700ea22c48ebff18ec11be06c54ab19d7e791 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=config -->
Set of directory names skipped during `os.walk` traversal to avoid descending into vendor and build trees.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_iter_config_files fingerprint=0685443b6a6379cdd09f570eab6bdf3d1732f9ec0c165618c6f71c827ec6251b body_fp=3cabff63f0ac8680e7c1f798a1a12abf9827ab977b606ed1ba137c2b7eda72d3 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=io -->
## `def _iter_config_files(source_root: Path, name_pattern: str) -> list[Path]`

Walk `source_root` returning sorted paths matching `name_pattern`, skipping `_PRUNE_DIR_NAMES` and hidden directories during traversal.

- `name_pattern`: `fnmatch`-style glob applied to filenames only, not full paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_strip_jsonc fingerprint=61822ab390fee1589f2995c128feeec989f5474d6ab7318042a6d5718c06a739 body_fp=ba325adfd15f5567acab3bd4ae38ca1649f91f4d273c22f315f15515ca5c1f71 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
## `def _strip_jsonc(text: str) -> str`

Strip `//` line comments, `/* */` block comments, and trailing commas from a JSONC string to make it valid JSON.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_load_jsonc fingerprint=c2fcd3863dadbb360ce720aef4032bb9528338a03178fb18e5d5a04b911eee09 body_fp=410dc48aa4c4003a08451b4dd183ba93ca70b89ea16921e187cf6b394a4c5cc9 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=io -->
## `def _load_jsonc(path: Path) -> dict | None`

Read and parse a JSONC file at `path`, returning the parsed dict or `None` on read or parse failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_module_key fingerprint=cbdd3814254528830fa807505a1b072de6807d3ba4cb32088a448061904f3d81 body_fp=d150f0323a4a9d5d51bce6323d19aa6f29ea192e5748b9f147f3771e8865f917 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=util -->
## `def _module_key(path: Path, source_root: Path) -> str | None`

Return the slash-form module key (relative path minus source extension) for a file under `source_root`, or `None` if outside it.

- `path` — resolved against the filesystem before relativity check
- Extensions stripped in longest-first order: `.d.ts`, `.tsx`, `.ts`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsConfig fingerprint=949cc41560b1d5f0346b01195882e4a2a17dfcd903dbd98992292f0cac0c2e3a body_fp=a0fb7bbcee14dfd7ff894c63036d5c2ef9d5ee3ef5555d83c5e6aedb14957d2e source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=model -->
## `class TsConfig`

Dataclass holding the resolution-relevant fields parsed from one `tsconfig.json`.

- `base_url`: absolute resolved path, or `None` if `baseUrl` is absent
- `paths`: tsconfig `paths` mapping; empty dict when not set
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver fingerprint=40ab318d91e3e1ee0c8b40d1aee47de59805613ab02e0511945ce2655cddd700 body_fp=bf68c217bf6d58f85bc25cd516e8c8316c283da650a60cac559a5103e441495e source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
## `class TsResolver`

Resolves TypeScript import specifiers to slash-form project module keys across relative, tsconfig-alias, and workspace-package layers.

- `source_root`: resolved absolute root against which all module keys are computed
- `tsconfigs`: ordered list of parsed `TsConfig` objects; more-specific (deeper) configs first
- `workspace_entries`: maps `package.json` `name` to the package's resolved entry source file
- `_cache`: memoizes `(specifier, str(from_file))` → result to avoid redundant filesystem probing
- `build(source_root)`: classmethod; preferred constructor — eagerly reads tsconfigs and workspace `package.json` files
- `resolve(specifier, from_file)`: returns the module key string, or `None` if unresolvable; results are cached
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver.build fingerprint=ba2901ee79d977239dc20335784221e0128dd2d9ee6d8ed23798d92e8876bacc body_fp=3d57bbba66fdb0cddbf09d4b92529b728a4bb230297668259a2e8224574b10fe source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=orchestration -->
## `def build(cls, source_root: Path) -> TsResolver`

Construct a fully initialised `TsResolver` by scanning `source_root` for tsconfigs and workspace `package.json` files.

- `source_root`: resolved to an absolute path before scanning begins.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver.resolve fingerprint=5a5af109d81ff8b9a212f0bb26d36b2b3cbdb2564458f1ef4e7bf33833eaf8ff body_fp=feb8ab7bde862bc1fadb64ef5584829d809a5f839ad14119f6d53f9e14d397f2 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
## `def resolve(self, specifier: str, from_file: Path) -> str | None`

Return the module key for `specifier` imported from `from_file`, memoizing results in `TsResolver._cache`.

- `specifier`: raw import string (relative path or bare module name)
- returns `None` if the specifier cannot be resolved to a project source file
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_uncached fingerprint=0bc0ffee95ec6b0108223b39d490216e0471766ff6fffe927461e7950f423935 body_fp=527f97151be27e82b204bbbc925e215fd820fc635fbc63fcd32d90134ebda89d source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
## `def _resolve_uncached(self, specifier: str, from_file: Path) -> str | None`

Dispatch `TsResolver` resolution through relative, alias, and workspace layers in order, returning the first matching module key or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_alias fingerprint=3115c46f6ff60ee246cf633c66f8bd31e813e73b33303c3d29880c3bcee34cd6 body_fp=798c897b2aec5972377f881d465cd8f6879811603fcf617bf8353d292747558d source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
## `def _resolve_alias(self, specifier: str) -> str | None`

Resolve `specifier` against `TsResolver.tsconfigs` path aliases and `baseUrl`, returning the first matching module key or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_workspace fingerprint=088e169826b4d3f82b0947f55defd463eda11f3e47cd50ae3a51a16eca20bd13 body_fp=168863f22714b4171d633d64dad24ce845a6c773b7baba11b9f9894b4ba40e8b source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
## `def _resolve_workspace(self, specifier: str) -> str | None: # Exact package name, or a subpath import `@scope/pkg/sub`.`

Resolve `specifier` against `TsResolver.workspace_entries`, matching exact package names or subpath imports (`@scope/pkg/sub`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._probe fingerprint=a85e06ea3f74a45671a2adcbeaa09aecd4db968b9425614e52c99a0f50ffd108 body_fp=593d48a5fa1c5cfbbb1358b9a4e59bd04095cb8cf2dba0a0a87cf313b4d962ca source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=util -->
## `def _probe(self, target: Path) -> str | None`

Resolves an extension-less or directory `Path` to a concrete source file's module key by probing `.ts`/`.tsx`/`.d.ts` extensions then `index.*` barrels.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_apply_path_pattern fingerprint=3607bd86f51e59fc631fb20b6ddf20c9c637a5f220a8ab177851f97883f88f5c body_fp=bbe3fd83f1c248ad13d6b1eaa2e2d9aa925fce19c1ae8f68eb830652dfce80c3 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
## `def _apply_path_pattern(pattern: str, targets: list[str], specifier: str) -> str | None`

Match `specifier` against a single tsconfig `paths` pattern and return the rewritten baseUrl-relative path, or `None` if unmatched.

- `pattern`: supports at most one `*` wildcard; exact match also handled.
- `targets`: only the first element is used; empty list returns `None`.
- Returns the rewritten path with leading `./` stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_collect_tsconfigs fingerprint=f6e473fc42083674f0dc2ea3fbe54955bc74cd4ba48279fa3db690204013c5ba body_fp=d3344cc271984bfa0f62bfe23f4267011a46b123ec9a09ddccbb39cafd0d1c12 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=parsing -->
## `def _collect_tsconfigs(source_root: Path) -> list[TsConfig]`

Scan `source_root` for all `tsconfig*.json` files, resolve their `extends` chains, and return `TsConfig` objects sorted deepest-first.

- Skips `node_modules`, `__pycache__`, `build`, `dist`, and hidden directories during traversal.
- Only includes configs that declare `paths` or `baseUrl`; others are dropped.
- Deepest (most specific) configs are sorted first so their aliases take precedence.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_resolve_tsconfig_chain fingerprint=94a9241f05633c8f7dcc97028d67c9f4e6e040e0935357e6b85ae810a79a66ff body_fp=b44583cdf8f858732cc1a4ddd69d42d7d14023584a4547be42d777b21f84be8a source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
## `def _resolve_tsconfig_chain(path: Path, *, seen: set[Path]) -> dict | None`

Recursively loads a tsconfig at `path`, resolves relative `extends` chains, and shallow-merges `compilerOptions` from parent into child.

- `seen`: cycle guard; returns `None` if `path` already visited.
- Non-relative `extends` (e.g. `@tsconfig/…`) are silently ignored.
- Returns merged config dict, or `None` on load failure or cycle.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_collect_workspace_entries fingerprint=919b9e8b6579433f440371ef24bfb363dac6ad661b47ce0b1200c7c82db913f6 body_fp=9402403d4f6f413d15854596cbc5f11ef76ee565dc44b60f43cdb7cb50b24d48 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=parsing -->
## `def _collect_workspace_entries(source_root: Path) -> dict[str, Path]`

Walk all `package.json` files under `source_root` (excluding `node_modules`) and map each package `name` to its resolved entry source file.

- Returns only packages whose entry resolves to a real `.ts`/`.tsx`/`.d.ts` file.
- Entry field preference: `module` → `main` → `types` → `typings` → `index.ts` → `index.tsx` → `src/index.ts` → `src/index.tsx`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_package_entry_file fingerprint=cb6d4f162e71cae31f5c59aa568a0427fcf8861e5180eae797b983b6e3c5b4a3 body_fp=8bc7d2310a85c93960ab8480dc54badbf1fb862d6bad56820af98c4d1234d772 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
## `def _package_entry_file(pkg_dir: Path, data: dict) -> Path | None`

Probe `pkg_dir` for the first real source file matching `module`/`main`/`types`/`typings` fields, then fallback index paths, remapping compiled extensions to `.ts`/`.tsx`/`.d.ts` siblings.
<!-- trie:end -->