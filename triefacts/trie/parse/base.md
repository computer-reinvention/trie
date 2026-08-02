---
trie_version: 0.3.0
source: trie/parse/base.py
file_fingerprint: 32755b1e9be88d882304884b3462e37e147c966ffd83885942b1ef22c593e143
last_synced_at: '2026-08-02T21:19:31Z'
description: The language-backend contract.
defines:
- kind: module
  qualified_name: trie/parse/base:__module__
  lines: 1-87
- kind: class
  qualified_name: trie/parse/base:LanguageBackend
  lines: 28-86
  signature: class LanguageBackend(Protocol)
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_file_data
  lines: 43-51
  signature: 'def extract_file_data( self, file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> FileData'
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_symbols
  lines: 53-61
  signature: 'def extract_symbols( self, file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.source_suffix
  lines: 63-70
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.system_prompt
  lines: 72-74
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.resolver
  lines: 76-86
  signature: def resolver(self) -> ReferenceResolver | None
incoming_refs: 8
outgoing_refs: 3
---
<!-- trie:section symbol=trie/parse/base:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=24bbdccbd9923bfbbf35ebe32e1a393d3daa6c67df3e8c8622e92a433129d18f source_ref=2716b92a3f2978f94b87918091dea1ad4a696738 role=model -->
Defines the `LanguageBackend` protocol — the contract every language plugin must satisfy to integrate with the parse engine.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend fingerprint=97b7a0787ca1f22f084f9bca36ca4d80b0a7ccfd92fac265127375a3f8a6fcb5 body_fp=81da423d9b11564625f723104a8b3abdbdaa460def4f8f9d950402a6a217d52e source_ref=3d599cf92c5207761d11072a3dca41b1f8017f84 role=model -->
## `class LanguageBackend(Protocol)`

Runtime-checkable `Protocol` defining the contract every language plugin must implement to make a file family indexable by the engine.

- `name`: human/config identifier, e.g. `"python"`, `"typescript"`
- `extensions`: owned file suffixes; longer suffixes (`.d.ts`) must precede shorter relatives (`.ts`)
- `extract_file_data`: parses symbols **and** outbound references in one pass
- `extract_symbols`: parses symbols only, skipping reference resolution
- `source_suffix`: canonical suffix for newly created files (write path, not read)
- `system_prompt`: language-tuned system prompt for triefact prose generation
- `resolver`: returns the paired `ReferenceResolver` for type-dependent edges, or `None` for tree-sitter-only extraction
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.extract_file_data fingerprint=1ff716464c4869c5e5e5d0e812778370922e00732b008c90e8ff183e625dcecb body_fp=abadd3080ec72a358e8bdd36f3d5190011255ace6ae00ffb4e1a70f5351c7928 source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=parsing -->
## `def extract_file_data( self, file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> FileData`

Parse one file into a `FileData` containing both symbols and outbound references in a single pass.

- `source_root`: used to resolve relative qnames; optional if path is absolute
- `source_text`: supply pre-read text to skip disk I/O
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.extract_symbols fingerprint=a2a8be4ea0453e476ac99ee85586d5f0e8f94cc807c5d265ff56d4ad407062b8 body_fp=14f8f0b3cfb62d967bf420c400958c7e47a19a81fd4737927978a9b474a5c84a source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=parsing -->
## `def extract_symbols( self, file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse one file into a list of `Symbol` objects, skipping outbound reference resolution.

- `source_text`: if provided, parse this string instead of reading `file_path` from disk.
- `source_root`: used to compute qualified names relative to the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.source_suffix fingerprint=073ed19d6644dbbd00c4ce7789a66179de16a56b40d0744963248cff6bf6df0d body_fp=2800c6929b0d38f580051f7cda4034c551d80d908d9733efca196513619912e6 source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
## `def source_suffix(self) -> str`

Return the canonical file extension for newly created files of this language, used to reconstruct a path from a qname.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.system_prompt fingerprint=127a1695b6d2660736131f6d96dc5dcef8b718b53ef6f2aacd11532818780f45 body_fp=428c937e445077a3b7f818718337cb8cde80ee78ab3ea9c78e50730c26afa493 source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
## `def system_prompt(self) -> str`

Return the language-tuned system prompt string used when generating `LanguageBackend` triefact prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend.resolver fingerprint=cb491c36be1eb40effae6bce4fa31211d9db7bd2526e330cf1704e31f69d6cce body_fp=c1497ae3ce3d4228e838b5d960497150cc36f04e696312e2dc9ecd176c15b9d9 source_ref=3d599cf92c5207761d11072a3dca41b1f8017f84 role=domain -->
## `def resolver(self) -> ReferenceResolver | None`

Return the `ReferenceResolver` paired with this `LanguageBackend`, or `None` for tree-sitter-only reference extraction.

- Returns `None` by default; override to add method-dispatch edge coverage.
<!-- trie:end -->