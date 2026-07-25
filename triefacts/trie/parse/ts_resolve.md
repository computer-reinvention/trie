---
trie_version: 0.1.9
source: trie/parse/ts_resolve.py
file_fingerprint: 94c54a75804100759b8317af175c4bdbe01612cb9782892ccc3a426f3c5a7c67
last_synced_at: '2026-07-25T00:55:40Z'
description: "TypeScript module-specifier resolution \u2014 config + syntax, never\
  \ type inference."
defines:
- kind: module
  qualified_name: trie/parse/ts_resolve:__module__
  lines: 1-313
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
  lines: 39-54
- kind: function
  qualified_name: trie/parse/ts_resolve:_strip_jsonc
  lines: 57-66
- kind: function
  qualified_name: trie/parse/ts_resolve:_load_jsonc
  lines: 69-73
- kind: function
  qualified_name: trie/parse/ts_resolve:_module_key
  lines: 76-87
- kind: class
  qualified_name: trie/parse/ts_resolve:TsConfig
  lines: 91-96
- kind: class
  qualified_name: trie/parse/ts_resolve:TsResolver
  lines: 100-199
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver.build
  lines: 114-122
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver.resolve
  lines: 126-133
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_uncached
  lines: 137-146
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_alias
  lines: 148-163
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._resolve_workspace
  lines: 165-177
- kind: method
  qualified_name: trie/parse/ts_resolve:TsResolver._probe
  lines: 179-199
- kind: function
  qualified_name: trie/parse/ts_resolve:_apply_path_pattern
  lines: 202-219
- kind: function
  qualified_name: trie/parse/ts_resolve:_collect_tsconfigs
  lines: 222-240
- kind: function
  qualified_name: trie/parse/ts_resolve:_resolve_tsconfig_chain
  lines: 243-271
- kind: function
  qualified_name: trie/parse/ts_resolve:_collect_workspace_entries
  lines: 274-291
- kind: function
  qualified_name: trie/parse/ts_resolve:_package_entry_file
  lines: 294-312
incoming_refs: 3
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
<!-- trie:section symbol=trie/parse/ts_resolve:_iter_config_files fingerprint=0685443b6a6379cdd09f570eab6bdf3d1732f9ec0c165618c6f71c827ec6251b body_fp=3d82a348e7de9005c97325f9168d51a7b276c88a16cf0397e2e7c3cfcda20c01 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=io -->
Walk `source_root` returning sorted paths matching `name_pattern`, skipping `_PRUNE_DIR_NAMES` and hidden directories during traversal.

- `name_pattern`: `fnmatch`-style glob applied to filenames only, not full paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_strip_jsonc fingerprint=61822ab390fee1589f2995c128feeec989f5474d6ab7318042a6d5718c06a739 body_fp=f31251aa4c6264f0cf02a93a321a9d2b7bcd69d4df69dd22f920b30329e67dc8 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
Strip `//` line comments, `/* */` block comments, and trailing commas from a JSONC string to make it valid JSON.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_load_jsonc fingerprint=c2fcd3863dadbb360ce720aef4032bb9528338a03178fb18e5d5a04b911eee09 body_fp=d5e3404d276accc02201d11020c27dbe992e96f1ffddcd416be7b2812324b211 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=io -->
Read and parse a JSONC file at `path`, returning the parsed dict or `None` on read or parse failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_module_key fingerprint=cbdd3814254528830fa807505a1b072de6807d3ba4cb32088a448061904f3d81 body_fp=0b1578bf9499dffbc78e4fdead7d7fb0e2cfbbcad977d4d6d3c1d0bc12a04df6 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=util -->
Return the slash-form module key (relative path minus source extension) for a file under `source_root`, or `None` if outside it.

- `path` — resolved against the filesystem before relativity check
- Extensions stripped in longest-first order: `.d.ts`, `.tsx`, `.ts`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsConfig fingerprint=949cc41560b1d5f0346b01195882e4a2a17dfcd903dbd98992292f0cac0c2e3a body_fp=8370800fc1170952087455bf7f37f698be8965368fab0d527bf8d42b22f8e7e4 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=model -->
Dataclass holding the resolution-relevant fields parsed from one `tsconfig.json`.

- `base_url`: absolute resolved path, or `None` if `baseUrl` is absent
- `paths`: tsconfig `paths` mapping; empty dict when not set
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver fingerprint=40ab318d91e3e1ee0c8b40d1aee47de59805613ab02e0511945ce2655cddd700 body_fp=5f79463dc37c2e3993dcbbee8bc72879c5acf38f5da623e9c6974380fcfb6e0d source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
Resolves TypeScript import specifiers to slash-form project module keys across relative, tsconfig-alias, and workspace-package layers.

- `source_root`: resolved absolute root against which all module keys are computed
- `tsconfigs`: ordered list of parsed `TsConfig` objects; more-specific (deeper) configs first
- `workspace_entries`: maps `package.json` `name` to the package's resolved entry source file
- `_cache`: memoizes `(specifier, str(from_file))` → result to avoid redundant filesystem probing
- `build(source_root)`: classmethod; preferred constructor — eagerly reads tsconfigs and workspace `package.json` files
- `resolve(specifier, from_file)`: returns the module key string, or `None` if unresolvable; results are cached
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver.build fingerprint=ba2901ee79d977239dc20335784221e0128dd2d9ee6d8ed23798d92e8876bacc body_fp=9df86ddfce18b4969596f3fd520442bdfb6db1aee62897ed6165a2cebaddc5a3 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=orchestration -->
Construct a fully initialised `TsResolver` by scanning `source_root` for tsconfigs and workspace `package.json` files.

- `source_root`: resolved to an absolute path before scanning begins.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver.resolve fingerprint=5a5af109d81ff8b9a212f0bb26d36b2b3cbdb2564458f1ef4e7bf33833eaf8ff body_fp=c27bff13ac8e6aeab63f2b2c42d98669a4eac713821f3fe31f8e7ccf691aa2e4 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
Return the module key for `specifier` imported from `from_file`, memoizing results in `TsResolver._cache`.

- `specifier`: raw import string (relative path or bare module name)
- returns `None` if the specifier cannot be resolved to a project source file
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_uncached fingerprint=0bc0ffee95ec6b0108223b39d490216e0471766ff6fffe927461e7950f423935 body_fp=e4101abbce79c6e8b542c0b72ecb66d2b3b4d4515526c41b303b2796ea3bc22c source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
Dispatch `TsResolver` resolution through relative, alias, and workspace layers in order, returning the first matching module key or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_alias fingerprint=3115c46f6ff60ee246cf633c66f8bd31e813e73b33303c3d29880c3bcee34cd6 body_fp=bf71ed61e2349a15611dc0b0a9610f9f2c8b88511154123600f09b4ee33b16da source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
Resolve `specifier` against `TsResolver.tsconfigs` path aliases and `baseUrl`, returning the first matching module key or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._resolve_workspace fingerprint=088e169826b4d3f82b0947f55defd463eda11f3e47cd50ae3a51a16eca20bd13 body_fp=780a41d1929f870cdbf399e79fcc0f2e83401a9a8f8d045c7022b204b457bc54 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=domain -->
Resolve `specifier` against `TsResolver.workspace_entries`, matching exact package names or subpath imports (`@scope/pkg/sub`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:TsResolver._probe fingerprint=a85e06ea3f74a45671a2adcbeaa09aecd4db968b9425614e52c99a0f50ffd108 body_fp=6cdf1cf2891a6b7374cd8eddcdc267766baa5d95d2dc90b4973880baff7dba58 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=util -->
Resolves an extension-less or directory `Path` to a concrete source file's module key by probing `.ts`/`.tsx`/`.d.ts` extensions then `index.*` barrels.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_apply_path_pattern fingerprint=3607bd86f51e59fc631fb20b6ddf20c9c637a5f220a8ab177851f97883f88f5c body_fp=c2880d048afbdd9d131a1c76638cbb5e7aa4e1dde9c5fe03d9369da69f4acf1e source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
Match `specifier` against a single tsconfig `paths` pattern and return the rewritten baseUrl-relative path, or `None` if unmatched.

- `pattern`: supports at most one `*` wildcard; exact match also handled.
- `targets`: only the first element is used; empty list returns `None`.
- Returns the rewritten path with leading `./` stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_collect_tsconfigs fingerprint=f6e473fc42083674f0dc2ea3fbe54955bc74cd4ba48279fa3db690204013c5ba body_fp=9e6d55d1b4d67707b3128aee65650475e92bf83fb27fb9133a7b481b6372dddf source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=parsing -->
Scan `source_root` for all `tsconfig*.json` files, resolve their `extends` chains, and return `TsConfig` objects sorted deepest-first.

- Skips `node_modules`, `__pycache__`, `build`, `dist`, and hidden directories during traversal.
- Only includes configs that declare `paths` or `baseUrl`; others are dropped.
- Deepest (most specific) configs are sorted first so their aliases take precedence.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_resolve_tsconfig_chain fingerprint=94a9241f05633c8f7dcc97028d67c9f4e6e040e0935357e6b85ae810a79a66ff body_fp=35a2cad651353fb9985c74e3905749e78de53408950f1d931c28f1cf557acdcc source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
Recursively loads a tsconfig at `path`, resolves relative `extends` chains, and shallow-merges `compilerOptions` from parent into child.

- `seen`: cycle guard; returns `None` if `path` already visited.
- Non-relative `extends` (e.g. `@tsconfig/…`) are silently ignored.
- Returns merged config dict, or `None` on load failure or cycle.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_collect_workspace_entries fingerprint=919b9e8b6579433f440371ef24bfb363dac6ad661b47ce0b1200c7c82db913f6 body_fp=8d9b649cb30226cecaa696fe4dde3d5b8aaffca1a4a8cf1e34cf1417e541fd94 source_ref=ae4e18069a91b4770ec14c2b01b9f05cfca87edd role=parsing -->
Walk all `package.json` files under `source_root` (excluding `node_modules`) and map each package `name` to its resolved entry source file.

- Returns only packages whose entry resolves to a real `.ts`/`.tsx`/`.d.ts` file.
- Entry field preference: `module` → `main` → `types` → `typings` → `index.ts` → `index.tsx` → `src/index.ts` → `src/index.tsx`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/ts_resolve:_package_entry_file fingerprint=cb6d4f162e71cae31f5c59aa568a0427fcf8861e5180eae797b983b6e3c5b4a3 body_fp=2a9c844a048c5f568a686fb02639b9da7ed3c17a8496056eeb8da452ff686cb5 source_ref=b50fdc64267f30e46665f54d7acb9a7d696d10ae role=parsing -->
Probe `pkg_dir` for the first real source file matching `module`/`main`/`types`/`typings` fields, then fallback index paths, remapping compiled extensions to `.ts`/`.tsx`/`.d.ts` siblings.
<!-- trie:end -->