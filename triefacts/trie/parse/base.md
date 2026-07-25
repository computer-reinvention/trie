---
trie_version: 0.1.9
source: trie/parse/base.py
file_fingerprint: d8355e20b8bb1e4f04ce493c5934c60c199a8abbd145289c06dfa980bcf2dd8e
last_synced_at: '2026-07-25T10:43:48Z'
description: The language-backend contract.
defines:
- kind: module
  qualified_name: trie/parse/base:__module__
  lines: 1-74
- kind: class
  qualified_name: trie/parse/base:LanguageBackend
  lines: 27-73
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_file_data
  lines: 42-50
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.extract_symbols
  lines: 52-60
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.source_suffix
  lines: 62-69
- kind: method
  qualified_name: trie/parse/base:LanguageBackend.system_prompt
  lines: 71-73
incoming_refs: 2
outgoing_refs: 2
---
<!-- trie:section symbol=trie/parse/base:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=24bbdccbd9923bfbbf35ebe32e1a393d3daa6c67df3e8c8622e92a433129d18f source_ref=2716b92a3f2978f94b87918091dea1ad4a696738 role=model -->
Defines the `LanguageBackend` protocol — the contract every language plugin must satisfy to integrate with the parse engine.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/base:LanguageBackend fingerprint=f46e32bbf4464a6d2df0f1c18a995fe6c65476851e991a87ce459594af039c5e body_fp=567e6be415b164a22c143b39988c2a56c7f8a01684dce4174be9937b7c88ab32 source_ref=2716b92a3f2978f94b87918091dea1ad4a696738 role=model -->
Runtime-checkable `Protocol` defining the contract every language plugin must implement to make a file family indexable by the engine.

- `name`: human/config identifier, e.g. `"python"`, `"typescript"`
- `extensions`: owned file suffixes; longer suffixes (`.d.ts`) must precede shorter relatives (`.ts`)
- `extract_file_data`: parses symbols **and** outbound references in one pass
- `extract_symbols`: parses symbols only, skipping reference resolution
- `source_suffix`: canonical suffix for newly created files (write path, not read)
- `system_prompt`: language-tuned system prompt for triefact prose generation
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
<!-- trie:section symbol=trie/parse/base:LanguageBackend.system_prompt fingerprint=127a1695b6d2660736131f6d96dc5dcef8b718b53ef6f2aacd11532818780f45 body_fp=c5868178c9f9837eacb6ffb67f56aa267e305593cedd6194f97a704ee0827cca source_ref=f83083eed86f54b5d2e684ea18671853d11614b5 role=domain -->
Return the language-tuned system prompt string used when generating `LanguageBackend` triefact prose.
<!-- trie:end -->