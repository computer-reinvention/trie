---
trie_version: 0.1.5
source: trie/edits/apply.py
file_fingerprint: 6872cb464280b74ac7932f505cb23d4221c2fda56e0817ab80bbf073679b1d24
last_synced_at: '2026-06-06T13:44:39Z'
defines:
- kind: module
  qualified_name: trie/edits/apply:__module__
  lines: 1-616
- kind: function
  qualified_name: trie/edits/apply:_parse_pyright_output
  lines: 27-43
- kind: function
  qualified_name: trie/edits/apply:_parse_ruff_output
  lines: 46-64
- kind: constant
  qualified_name: trie/edits/apply:_PARSERS
  lines: 67-70
- kind: function
  qualified_name: trie/edits/apply:_lsp_diagnostics
  lines: 73-98
- kind: function
  qualified_name: trie/edits/apply:_format_diagnostics
  lines: 101-109
- kind: function
  qualified_name: trie/edits/apply:_file_fixup
  lines: 112-135
- kind: function
  qualified_name: trie/edits/apply:_compile_check
  lines: 138-143
- kind: function
  qualified_name: trie/edits/apply:_expand_callers
  lines: 146-176
- kind: function
  qualified_name: trie/edits/apply:_refresh_file
  lines: 179-188
- kind: function
  qualified_name: trie/edits/apply:apply_patches
  lines: 191-537
- kind: function
  qualified_name: trie/edits/apply:_read_source_span
  lines: 540-543
- kind: function
  qualified_name: trie/edits/apply:_write_prose_section
  lines: 546-584
- kind: function
  qualified_name: trie/edits/apply:preview_patches
  lines: 587-615
incoming_refs: 24
outgoing_refs: 2
---
<!-- trie:section symbol=trie/edits/apply:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a240e61e0147c739eb5cd28dd5d4841e0cc3638151c3dc00315a599b3dfc1b23 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Applies pending code patches by cascading to callers, generating new source with LLM inference, fixing syntax errors via LSP diagnostics, and updating triefact documentation.

- **apply_patches()**: Main entry point that processes all pending patches with optional progress reporting
- **preview_patches()**: Shows what symbols would be affected without applying changes
- **_expand_callers()**: Finds symbols that call patched symbols up to cascade depth limit
- **_file_fixup()**: Uses LLM to fix LSP diagnostic errors in generated code
- **_lsp_diagnostics()**: Runs external tools (pyright, ruff) to detect code issues
- **_parse_pyright_output()**, **_parse_ruff_output()**: Parse JSON diagnostic output from static analysis tools
- **_compile_check()**: Validates Python syntax by attempting compilation
- **_read_source_span()**: Extracts source code lines for a symbol from its file
- **_write_prose_section()**: Updates triefact markdown with new documentation prose
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_parse_pyright_output fingerprint=3f78e0d19b87058172379c29ed45d41ac6a2dc8377978626de528aac643d4a90 body_fp=1929f1f7e9476599e5f1c663aa0a45ec489f0fd685abf5a95900262a90e93a72 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Parses Pyright JSON output into standardized diagnostic dictionaries with line, column, code, and message fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_parse_ruff_output fingerprint=73cb22cf0e4be716b9efcefa0839ad9656ee75a89e04bc1f63474b6f5d0ded39 body_fp=718b5227054b44310a039557798b48297e7dde986870836d26c82f5c60d8792d source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Parses JSON output from ruff linter into standardized diagnostic dictionaries.

- Returns empty list if JSON parsing fails or input is invalid
- Normalizes single dict output to list format for consistent processing
- Extracts line/column from either "location" object or top-level fields
- Uses "ruff" as default code when none provided
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_PARSERS fingerprint=b2a5f90b8926406f02cb4d57b896878b47a5719443a5587d105fd7e953b0ffe3 body_fp=0a7af5e9c42418fd7fd5bd63cbdee215a3722ffc970df069c495e921b899c037 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Maps LSP backend output format names to their corresponding diagnostic parser functions.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_lsp_diagnostics fingerprint=05ed364b4019b1dd4ee6b40ad27905b4e918ad82dad02288a52221ccf51d3133 body_fp=9f7ec5b77d4a171ca91ae826e7e73786ee6491cf573cd9c2ba540a7494d76089 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Runs LSP backends sequentially against a file and returns diagnostics from the first successful tool.

- Returns empty list if no backends produce diagnostics or if all tools fail
- Skips backends whose commands are not found in PATH
- Uses configured check_args and output_format for each backend
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_format_diagnostics fingerprint=f8f1a2a1db2af1f7d97e5492cd064ae2f56b6574b386af817e0a4e13e5490c56 body_fp=dd40ea53611c19768ecf0ce91283a911c80749520b7b9390e3e3a7fef52351aa source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Formats diagnostic messages from LSP backends into a human-readable string with line:column positions.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_file_fixup fingerprint=bbadd2dda12f9b9865bdf44285d919b279240223f85f1fca9335ac9413ccd9e7 body_fp=a62a14c70277c17d6757e988996b7a48867adaced13d0de6e86b9aec7c2b5344 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=orchestration -->
Uses LLM client to fix diagnostic issues in file content, returning corrected code or original if no diagnostics.

- Returns None if LLM fails to generate fix, original content if diagnostics are empty
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_compile_check fingerprint=7a854ad40befe46ef361c13e67a4678144ea8a66457bd5ceeb3562379b1703cf body_fp=1017686e8f2277f506b67ab920df22daf551148d046db5c4ce2f251a025758a5 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Compiles Python source code to check for syntax errors, returning True if valid.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_expand_callers fingerprint=3b8ad849b2ca5152c41cf726107bdb2e7194d9434696c747cf3a92eb2c4dabd8 body_fp=820918d91cd2c48bf16ebb028ff59fe9c7312826318adca723b058867193daf3 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=change-detection -->
Expands seed symbols to include their callers up to cascade_depth levels, skipping hub symbols.

- `hub_threshold`: symbols with more than this many callers are skipped as hubs
- `cascade_depth`: maximum levels of caller expansion to perform
- Returns set of caller qualified names discovered during expansion
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_refresh_file fingerprint=cb12cf48ef733d72f2273ca2661a206c03fd153e474426a121e05919824950cf body_fp=955ded022f1c7bd954e595349b4351a1c217a03811eeb235cbfe4e97dcad3124 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=documentation-sync -->
Updates triefact metadata for a single file after source code changes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:apply_patches fingerprint=34152c4a10101626598cdf65b430179eaebdc1213a49e9710db538fcb37aee10 body_fp=4c0e509848276e6bb2558bda3fb5122414ced0db033038adaf8519a35e7cab1b source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Applies all pending patches by cascading changes, generating source and prose, running LSP fixups, and verifying project consistency.

- **patches**: groups patches by symbol, expands to caller symbols via cascade
- **generation**: uses LLM to generate new source code and triefact prose
- **fixups**: runs configured LSP backends to fix diagnostics iteratively
- **verification**: checks project consistency and refreshes metadata
- **concurrency**: processes files in parallel using ThreadPoolExecutor
- **progress**: optional callback interface for progress reporting
- **returns**: dict with ok status, file/symbol counts, per-file results, and error details
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_read_source_span fingerprint=43f69c6b8bf7cdf184ce904aba0f8a6e02e68bdef37b33c43b59ff4df640eb73 body_fp=72248a93a0397e62b5741b62d77e4393f1edbc78acf03619fc32956caaee910f source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Extracts source code lines from a file between specified start and end line numbers.

- Uses 1-based line numbering from detail object
- Preserves line endings in the extracted span
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_write_prose_section fingerprint=8af674914055253618af885b0cd4c3668e2e7e6ddb737d486007b02b58a61a00 body_fp=ca4201fe30a99d8eee3d573ef2ca84278000fd5429b048029ef2586f3818c8b9 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=documentation-sync -->
Updates or creates a prose documentation section for a symbol in its triefact file.

- Creates triefact markdown file if it doesn't exist
- Extracts symbol fingerprint from source for verification
- Upserts section with qualified name, fingerprint, prose body and empty source ref
- Sorts sections and writes updated triefact file
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:preview_patches fingerprint=40df1bfff989b701a17843747fb88bcd6b9a12a390a9f1fbf23fc30b1d899b30 body_fp=cd367a1b7bd8a4638d49ceefd29dc45b2da63d6c7b2f5412139e98fa0dcbbb80 source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 role=code-editing -->
Returns a preview of pending patches and their cascade impact without applying them.

- Returns dict with patch counts, affected symbol lists, and cascade expansion details
<!-- trie:end -->