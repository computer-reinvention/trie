---
trie_version: 0.1.9
source: trie/parse/base.py
file_fingerprint: f3f666a184e72d163e83313c467ee528121f1919fd6139e928850e278a4da564
last_synced_at: '2026-07-20T09:54:37Z'
description: The language-backend contract.
defines:
- kind: module
  qualified_name: trie/parse/base:__module__
  lines: 1-121
- kind: class
  qualified_name: trie/parse/base:LanguageBackend
  lines: 30-120
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_file_data
  lines: 45-53
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_symbols
  lines: 55-63
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.source_suffix
  lines: 65-72
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.lsp_backends
  lines: 74-79
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.overlay_globs
  lines: 81-84
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.overlay_extra_files
  lines: 86-89
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.system_prompt
  lines: 91-93
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.edit_system_prompt
  lines: 95-103
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.code_fence
  lines: 105-109
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.validate_syntax
  lines: 111-120
incoming_refs: 2
outgoing_refs: 2
---
<!-- trie:section symbol=trie/parse/base:__module__ fingerprint=680a84777e03cae0d8ae4a267255a1d1e1389fc035f3febba8abe400af5e1940 body_fp=24bbdccbd9923bfbbf35ebe32e1a393d3daa6c67df3e8c8622e92a433129d18f source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=parsing -->
Defines the `LanguageBackend` protocol — the contract every language plugin must satisfy to integrate with the parse engine.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend fingerprint=5c8229b017a58182d8dae28554026cbddd076e7510d1d6c0788669344d47c729 body_fp=f218b36fdb49ffaf66d6409e811e416f5c788f2a6825b5cfc010d5423f712e4a source_ref=0eca4c9baf924e4dc9487aac225bd4e76306dc05 role=model -->
Runtime-checkable `Protocol` defining the contract every language plugin must implement to make a file family indexable by the engine.

- `name`: human/config identifier, e.g. `"python"`, `"typescript"`
- `extensions`: owned file suffixes; longer suffixes (`.d.ts`) must precede shorter relatives (`.ts`)
- `extract_file_data`: parses symbols **and** outbound references in one pass
- `extract_symbols`: parses symbols only, skipping reference resolution
- `source_suffix`: canonical suffix for newly created files (write path, not read)
- `lsp_backends`: default diagnostic checkers; engine falls back to `Edits.lsp_backends` when empty
- `overlay_globs`: file globs hardlinked into the edit scratch tree for the checker
- `overlay_extra_files`: non-source config files (e.g. `tsconfig.json`) needed in the scratch tree
- `system_prompt`: language-tuned system prompt for triefact prose generation
- `edit_system_prompt`: separate language-tuned prompt for the edit pipeline (source editing, not prose)
- `code_fence`: Markdown code-fence tag used when embedding source in edit prompts
- `validate_syntax`: cheap syntax gate returning `True` when source is well-formed; must never raise
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.extract_file_data fingerprint=1ff716464c4869c5e5e5d0e812778370922e00732b008c90e8ff183e625dcecb body_fp=e8aabd5a373676ea59cc86b4242443f728a1bf0de281ba71414fbd82f731b9a9 source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=parsing -->
Parse one file into a `FileData` containing both symbols and outbound references in a single pass.

- `source_root`: used to resolve relative qnames; optional if path is absolute
- `source_text`: supply pre-read text to skip disk I/O
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.extract_symbols fingerprint=a2a8be4ea0453e476ac99ee85586d5f0e8f94cc807c5d265ff56d4ad407062b8 body_fp=306d33058cc79036506b77f85486d309e6680d23d28daf0ace975979e47ba7db source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=parsing -->
Parse one file into a list of `Symbol` objects, skipping outbound reference resolution.

- `source_text`: if provided, parse this string instead of reading `file_path` from disk.
- `source_root`: used to compute qualified names relative to the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.source_suffix fingerprint=073ed19d6644dbbd00c4ce7789a66179de16a56b40d0744963248cff6bf6df0d body_fp=9af3857ed549a53344088e1523bda8f67d4a28020785978853c3887ef12e5b57 source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return the canonical file extension for newly created files of this language, used to reconstruct a path from a qname.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.lsp_backends fingerprint=193bfc316da9483f28a00c445cdc747529f89496effcd8c62d4aca513290618f body_fp=88cf7a62602350d223ac098887e761df4acab53cc7d00e8b19dd284186d8b1be source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return the default LSP diagnostic checkers for `LanguageBackend`'s edit pipeline; `Edits.lsp_backends` is used as fallback when the returned list is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.overlay_globs fingerprint=4639812d1625fcb8161c6c37ed7529c81c3d1136be910a361ff1ed5874e41710 body_fp=b62c360ba815be0ce8d15179f32aa3fd1b81999d1b792c1d3160f9e688fbf07f source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return globs for source files hardlinked into the edit scratch tree so the language checker sees the full import graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.overlay_extra_files fingerprint=c8a3492c94d77802d1f8c3bf90a3c5f11480884045aaca431b8425ac49ef18e0 body_fp=a8e320e298fa5f456b0700ccbb6c8cb7861bd60b3103114ef66b27fc6183cb9b source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return non-source config file basenames `LanguageBackend` requires hardlinked into the edit scratch tree for the checker.

- Returns empty tuple for Python; TypeScript needs `tsconfig.json`, `package.json`, etc.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.system_prompt fingerprint=127a1695b6d2660736131f6d96dc5dcef8b718b53ef6f2aacd11532818780f45 body_fp=c5868178c9f9837eacb6ffb67f56aa267e305593cedd6194f97a704ee0827cca source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return the language-tuned system prompt string used when generating `LanguageBackend` triefact prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.edit_system_prompt fingerprint=2570f925d0cdcc69707f60e0f426d7ee3c4cec647e31224a2850e69d9d709452 body_fp=333391961c8b2a168aba70d07893fa8a710a4bf7f67455e14702f6a719f9cff2 source_ref=0eca4c9baf924e4dc9487aac225bd4e76306dc05 role=domain -->
Return the `LanguageBackend`-specific system prompt string for the edit pipeline, distinct from the prose-documentation prompt.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.code_fence fingerprint=cbe80e40f4d5044c21373fbce284d0a019699ff6c29675e07d32f25c46f2e9b6 body_fp=7a7415c38dadd5c8de462f9d790d03308ec93cce5e7cc35aa6d7b5a361703d47 source_ref=0eca4c9baf924e4dc9487aac225bd4e76306dc05 role=domain -->
Return the Markdown code-fence language tag string for this `LanguageBackend`, used when embedding source in edit prompts.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.validate_syntax fingerprint=38a30c4c9d4a1c5204bd8b52eedb056488fdb84973ae8ae1b847f5bb55b7157f body_fp=a20ee8dcdff63f407f57ba4a8ca8165d1facc46da2d58b2c7d6fdb9067e09378 source_ref=0eca4c9baf924e4dc9487aac225bd4e76306dc05 role=domain -->
Return `True` if `source` is syntactically valid for this `LanguageBackend`'s language; never raises.

- `file_path`: project-relative target path; extension may affect validation (e.g. `.tsx`).
- Returns `True` on internal error to degrade gracefully; LSP/tsc pass is the real gate.
<!-- trie:end -->