---
trie_version: 0.1.5
source: trie/edits/infer.py
file_fingerprint: d04b4c5db146a96bbda6c2fbd2a2c2029fc9891cfa05c68f35567a9be9a70aa3
last_synced_at: '2026-05-28T01:48:58Z'
defines:
- kind: module
  qualified_name: trie/edits/infer:__module__
  lines: 1-503
- kind: constant
  qualified_name: trie/edits/infer:BATCH_PRE_FILTER_PROMPT
  lines: 8-22
- kind: constant
  qualified_name: trie/edits/infer:FIXUP_PROMPT
  lines: 24-42
- kind: constant
  qualified_name: trie/edits/infer:CALLEE_SECTION
  lines: 44-52
- kind: constant
  qualified_name: trie/edits/infer:MERGE_PROMPT
  lines: 54-61
- kind: constant
  qualified_name: trie/edits/infer:INFER_SYSTEM_PROMPT
  lines: 63-67
- kind: function
  qualified_name: trie/edits/infer:_format_bullets
  lines: 70-74
- kind: function
  qualified_name: trie/edits/infer:merge_notes
  lines: 77-119
- kind: function
  qualified_name: trie/edits/infer:infer_source_and_prose
  lines: 122-191
- kind: constant
  qualified_name: trie/edits/infer:FILE_FIXUP_PROMPT
  lines: 194-208
- kind: constant
  qualified_name: trie/edits/infer:FILE_GEN_PROMPT
  lines: 210-229
- kind: function
  qualified_name: trie/edits/infer:_format_file_notes
  lines: 232-236
- kind: function
  qualified_name: trie/edits/infer:infer_file_source
  lines: 239-335
- kind: function
  qualified_name: trie/edits/infer:_build_caller_summaries
  lines: 338-362
- kind: function
  qualified_name: trie/edits/infer:_read_prose
  lines: 365-390
- kind: function
  qualified_name: trie/edits/infer:pre_filter_batch
  lines: 393-502
incoming_refs: 13
outgoing_refs: 4
---
<!-- trie:section symbol=trie/edits/infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=659ea56467bf29f76008367782cdce3123ef769b133a8992220527f963dc480e source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `trie/edits/infer`

LLM-powered helpers for inferring updated source/prose and filtering cascade edits.

- `merge_notes`: deduplicates and merges patch notes via LLM
- `infer_source_and_prose`: rewrites a symbol's source and prose given change notes
- `pre_filter_batch`: decides which callers need updates after a callee changes
- `_build_caller_summaries`, `_read_prose`: internal helpers for context assembly
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:BATCH_PRE_FILTER_PROMPT fingerprint=1bbaed87a2efbbcc434fbaecdddfeb484e11070f4c70473d1879a4ce9c78d08c body_fp=26f7333f4eb6b134d5d517d9ba9c1ebcf0747945b056adf90a76e28a850e807b source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `BATCH_PRE_FILTER_PROMPT`

Prompt template instructing the LLM to classify each caller as `SKIP` or `NOTE:/REASON:` given changed callee sections.

- `{callee_sections}`: formatted callee blocks injected by `pre_filter_batch`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FIXUP_PROMPT fingerprint=f89afdd4335a3a2c11212b96b0a94609ac061631572322a19a3cff86b8bb1524 body_fp=8a9a3b0ef2ee30d1c5a12b24de4ca0d7eabb2a34ca22ed4564c250866a43e635 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `FIXUP_PROMPT`

Prompt template for asking the model to fix diagnostic errors in generated source and return corrected source plus prose.

- `{qname}`: qualified name of the symbol being fixed.
- `{source}`: the erroneous generated source code.
- `{diagnostics}`: error messages to resolve.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:CALLEE_SECTION fingerprint=f9542d7d4b5c4b239e28d4880d2970fe7cecf7928bcbeb119c60bff574600777 body_fp=3b2ec654fa1975daa07195ea60ff0e806214919f16a9bf425a9e770a0c9c9b31 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `CALLEE_SECTION`

Template string for one callee block inside `BATCH_PRE_FILTER_PROMPT`, formatting tag, qname, old prose, notes, and caller table.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:MERGE_PROMPT fingerprint=f236ccc07197a3f11a346c733f4a4077b44217f3c952664d42fb8dfdd3251b68 body_fp=0340430d91f2e979c534394a3149af4fc21519d191d82b5ec8dc2609a05d685b source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `MERGE_PROMPT`

Prompt template instructing the model to deduplicate and merge patch notes, removing superseded entries while preserving order.

- `{bullet_list}`: formatted `<bullet> note — reason` lines to merge.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:INFER_SYSTEM_PROMPT fingerprint=03492b7e67e6343a9d05de7ac4c4923f98ac304cf4fa541ec9103643090f1948 body_fp=c72ec03968a7da1d263f976288416e57c4f1f485c94ded1b8933d114f98aa4cc source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `INFER_SYSTEM_PROMPT: str`

System prompt instructing the LLM to output `UPDATED_SOURCE` and `UPDATED_PROSE` separated by `---PROSE---`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_format_bullets fingerprint=276d8d146737b65b171b6b1d440db66fa18b94a20cbc45c2cf752f35f5cd26d4 body_fp=fa9311082ed03dc7dea30c1e09be2756327730eb16c9d941ae2cfa088a7afad6 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `_format_bullets(notes: list[str], reasons: list[str]) -> str`

Format paired notes and reasons into a newline-joined `<bullet>` string for prompt injection.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:merge_notes fingerprint=9bf81759f45e5f11f8f120a224f9a6306b5ecb326a9a21f881ee645db4c1e129 body_fp=424fd9612a521d338c41d52c293033c09301ae02c06cd67eeb54eec1f2ecdcdc source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `merge_notes(client: ModelClient, patches: list[dict]) -> tuple[list[str], list[str]]`

Use an LLM to deduplicate and consolidate a list of patch notes, removing superseded entries.

- `patches`: dicts with `"note"` and `"reason"` keys
- Returns parallel lists of merged notes and their reasons
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_source_and_prose fingerprint=2daaa3db2f5642546e4730dd01357e5e1d23cdf4a50ca9ad5dcb0a4644b68130 body_fp=a8b051082fad1186a631642f85e6d42e8914e4221034ee3354c4e7c14dd3341e source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `infer_source_and_prose(client: ModelClient, old_source: str, old_prose: str, notes: list[str], reasons: list[str]) -> tuple[str, str]`

Call the LLM to produce updated source code and prose for a symbol given implementation notes.

- `notes` / `reasons`: paired lists describing what changed; consumed and discarded in output prose.
- Returns `(new_source, new_prose)` with fenced-code delimiters stripped.
- Raises `ValueError` if the LLM response lacks the `---PROSE---` delimiter.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_FIXUP_PROMPT fingerprint=451cc0006d70946707bc0f7a83061fba80e697c059afc79f75fb7c098d132383 body_fp=4ec457eaf52320d10b4ead1488240767007e9f453043e09752a59244bee64361 source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `FILE_FIXUP_PROMPT`

Prompt template instructing the LLM to fix all diagnostics errors in a file and return the complete corrected content.

- `{file_content}`: current file source with errors
- `{diagnostics}`: diagnostic messages to resolve
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_GEN_PROMPT fingerprint=973f3e453f3d2b3113d62123d1c6c1f38f217341fc89839c4c2ad947a7447759 body_fp=a992a0075991eb9a31e3633f6cf440f3bd81e4996da05b170b962611eb9a498d source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `FILE_GEN_PROMPT`

Prompt template for generating a complete updated file and per-symbol prose in one LLM call.

- `{file_path}`: path shown to the model for context
- `{symbol_sections}`: formatted descriptions of each symbol needing changes
- `{prose_delimiters}`: `---PROSE:<qname>---` markers instructing the model where to write each symbol's updated prose
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_format_file_notes fingerprint=06794d90cf80bcc5df24d952d26044ac387614b80ae7e03f9a9016945af35dd3 body_fp=d7cd0fb7f9c1046bf49eeb959f6dae325ec6d272424fd2f4dda162791f842542 source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `_format_file_notes(notes: list[str], reasons: list[str]) -> str`

Format paired notes and reasons as a Markdown bullet list, one `- note  —  reason` line each.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_file_source fingerprint=7834d5e90f2ba72aa1334ef03c007f2ad3e4e32e7ecd44dcb5b3469520827d55 body_fp=67c4498725baecf0fb7d538fd27a9bde2cfef9523aac163335de2c097e2e63b5 source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `infer_file_source(client: ModelClient, file_path: str, file_content: str, symbols_data: list[dict], *, max_tokens: int = 4096) -> tuple[str, dict[str, str]]`

Generate updated source and prose for all changed symbols in a file via a single LLM call.

- `symbols_data`: each dict requires `qname`, `old_source`, `old_prose`, `merged_notes`, `merged_reasons`.
- Returns `(new_file_content, {qname: new_prose})` parsed from delimited LLM output.
- Raises `ValueError` if the LLM response lacks the expected code-block delimiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_build_caller_summaries fingerprint=1f637644ec111c87bc1094c504a271999d692fea7ddf156db90198b689270541 body_fp=1cabad9a68226a4249ba596d367641cff11ecd922cd4622ed06cdb762636dac0 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `_build_caller_summaries(caller_qnames: list[str], store: Store, triefacts_root: Path) -> list[dict]`

Build caller summary dicts for the cascade pre-filter prompt.

- Returns `[{qname, signature, one_liner, prose}, ...]`; prose truncated to 200 chars.
- Silently skips any `qname` not found in `store`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_read_prose fingerprint=bc8321486f6ffff20d83b3174c944e906b7f6dfeb37d72d33264682a573434f2 body_fp=a9ffd531c1d9728a4ae256446e8af7f272634eb553508eff6c9b97fc5412f289 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `_read_prose(qname: str, file_path: str, triefacts_root: Path) -> str`

Read the triefact prose body for a symbol from its Markdown file, returning `''` if not found.

- `file_path`: source file path; `.md` suffix substituted to locate the triefact
- `triefacts_root`: base directory containing triefact Markdown files
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:pre_filter_batch fingerprint=7ab26b66712dadc5aeadfc9959a04288a1a3e25c3522009387bb5bba1a3513e0 body_fp=d0634e7893d565d3e6e4f3a1b5f2bba2f565956a2a4257b2592057abdf1a5552 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `pre_filter_batch(client: ModelClient, callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]], *, batch_size: int = 8) -> list[tuple[str, str | None, str | None]]`

Use an LLM to judge which callers of changed callees require source updates, processing in batches.

- `callee_pairs`: each entry is `(callee_qname, old_prose, callers, notes_with_reasons)`
- `callers`: list of `{qname, signature, one_liner, prose}` dicts per callee
- Returns `(caller_qname, note, reason)` tuples; SKIP decisions are excluded
<!-- trie:end -->