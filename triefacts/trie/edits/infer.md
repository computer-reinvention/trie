---
trie_version: 0.1.5
source: trie/edits/infer.py
file_fingerprint: d2cce33aa120782d568d41b352cb21c73882c0976f289693162f086943835601
last_synced_at: '2026-05-28T14:26:44Z'
defines:
- kind: module
  qualified_name: trie/edits/infer:__module__
  lines: 1-274
- kind: constant
  qualified_name: trie/edits/infer:MERGE_PROMPT
  lines: 13-19
- kind: constant
  qualified_name: trie/edits/infer:INFER_SYSTEM_PROMPT
  lines: 21-22
- kind: constant
  qualified_name: trie/edits/infer:BATCH_PRE_FILTER_PROMPT
  lines: 24-31
- kind: constant
  qualified_name: trie/edits/infer:FILE_GEN_PROMPT
  lines: 33-45
- kind: constant
  qualified_name: trie/edits/infer:FILE_FIXUP_PROMPT
  lines: 47-57
- kind: function
  qualified_name: trie/edits/infer:_format_bullets
  lines: 60-64
- kind: function
  qualified_name: trie/edits/infer:merge_notes
  lines: 67-82
- kind: function
  qualified_name: trie/edits/infer:infer_source_and_prose
  lines: 85-113
- kind: function
  qualified_name: trie/edits/infer:infer_file_source
  lines: 116-151
- kind: function
  qualified_name: trie/edits/infer:_build_caller_summaries
  lines: 154-188
- kind: function
  qualified_name: trie/edits/infer:_read_prose
  lines: 191-211
- kind: function
  qualified_name: trie/edits/infer:pre_filter_batch
  lines: 214-273
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
<!-- trie:section symbol=trie/edits/infer:MERGE_PROMPT fingerprint=f236ccc07197a3f11a346c733f4a4077b44217f3c952664d42fb8dfdd3251b68 body_fp=0340430d91f2e979c534394a3149af4fc21519d191d82b5ec8dc2609a05d685b source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `MERGE_PROMPT`

Prompt template instructing the model to deduplicate and merge patch notes, removing superseded entries while preserving order.

- `{bullet_list}`: formatted `<bullet> note — reason` lines to merge.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:INFER_SYSTEM_PROMPT fingerprint=03492b7e67e6343a9d05de7ac4c4923f98ac304cf4fa541ec9103643090f1948 body_fp=c72ec03968a7da1d263f976288416e57c4f1f485c94ded1b8933d114f98aa4cc source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `INFER_SYSTEM_PROMPT: str`

System prompt instructing the LLM to output `UPDATED_SOURCE` and `UPDATED_PROSE` separated by `---PROSE---`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:BATCH_PRE_FILTER_PROMPT fingerprint=1bbaed87a2efbbcc434fbaecdddfeb484e11070f4c70473d1879a4ce9c78d08c body_fp=26f7333f4eb6b134d5d517d9ba9c1ebcf0747945b056adf90a76e28a850e807b source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `BATCH_PRE_FILTER_PROMPT`

Prompt template instructing the LLM to classify each caller as `SKIP` or `NOTE:/REASON:` given changed callee sections.

- `{callee_sections}`: formatted callee blocks injected by `pre_filter_batch`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_GEN_PROMPT fingerprint=973f3e453f3d2b3113d62123d1c6c1f38f217341fc89839c4c2ad947a7447759 body_fp=a992a0075991eb9a31e3633f6cf440f3bd81e4996da05b170b962611eb9a498d source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `FILE_GEN_PROMPT`

Prompt template for generating a complete updated file and per-symbol prose in one LLM call.

- `{file_path}`: path shown to the model for context
- `{symbol_sections}`: formatted descriptions of each symbol needing changes
- `{prose_delimiters}`: `---PROSE:<qname>---` markers instructing the model where to write each symbol's updated prose
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_FIXUP_PROMPT fingerprint=451cc0006d70946707bc0f7a83061fba80e697c059afc79f75fb7c098d132383 body_fp=4ec457eaf52320d10b4ead1488240767007e9f453043e09752a59244bee64361 source_ref=f97ce5a609a683072064193f919e4ced3a784d3b -->
## `FILE_FIXUP_PROMPT`

Prompt template instructing the LLM to fix all diagnostics errors in a file and return the complete corrected content.

- `{file_content}`: current file source with errors
- `{diagnostics}`: diagnostic messages to resolve
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_format_bullets fingerprint=276d8d146737b65b171b6b1d440db66fa18b94a20cbc45c2cf752f35f5cd26d4 body_fp=fa9311082ed03dc7dea30c1e09be2756327730eb16c9d941ae2cfa088a7afad6 source_ref=f5a6700288cce84d22e15676231ab46d62977035 -->
## `_format_bullets(notes: list[str], reasons: list[str]) -> str`

Format paired notes and reasons into a newline-joined `<bullet>` string for prompt injection.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:merge_notes fingerprint=94dfc8addb1bd5773ab4bb3e59e5f6e274f144ce32f80b8cb25fb89f64ee037c body_fp=b7d20c3bd56eb79750708e3b7621d5cdec29bb2f7a9f74ae25f16b7ecec060e4 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `merge_notes(client: TrieClient, patches: list[dict]) -> tuple[list[str], list[str]]`

Use an LLM to deduplicate and consolidate a list of patch notes, removing superseded entries.

- `patches`: dicts with `"note"` and `"reason"` keys
- Returns parallel lists of merged notes and their reasons
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_source_and_prose fingerprint=6a6b9a2bd30ede6d692c4097578a5ba2440d3e24f2a42aa4ea5d4ba051f91a8d body_fp=20ee5e25d4068a7c0534f002eeebd29345eaa8abe6a7daf43e64fdcbfd1b7194 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `infer_source_and_prose(client: TrieClient, old_source: str, old_prose: str, notes: list[str], reasons: list[str]) -> tuple[str, str]`

Call the LLM to produce updated source code and prose summary for a symbol given implementation notes.

- Returns `(new_source, new_prose)` derived from the `SymbolEdit` model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_file_source fingerprint=9addb0f4c9d475f9f098ba59262116ec023f13c570665f8bb39c7326bb164db1 body_fp=a0aacdf95b67d4c912f58aeab874245f1687daef3b3150a34bb3388e3e2b3180 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `infer_file_source(client: TrieClient, file_path: str, file_content: str, symbols_data: list[dict], *, max_tokens: int = 8192) -> tuple[str, dict[str, str]]`

Generate updated source and prose for all changed symbols in a file via a single LLM call.

- `client`: now typed as `TrieClient`; uses `client.run` with structured `FileEdit` output instead of raw text parsing.
- `max_tokens`: default raised from `4096` to `8192`.
- `symbols_data`: each dict requires `qname`, `old_source`, `old_prose`, `merged_notes`, `merged_reasons`.
- Returns `(new_file_content, {qname: new_prose})` extracted directly from the structured `FileEdit` response.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_build_caller_summaries fingerprint=0c8f7cd3556632d62b031c157ae585fcf54543078428521b391f3f5f80c8aac9 body_fp=1cabad9a68226a4249ba596d367641cff11ecd922cd4622ed06cdb762636dac0 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `_build_caller_summaries(caller_qnames: list[str], store: Store, triefacts_root: Path) -> list[dict]`

Build caller summary dicts for the cascade pre-filter prompt.

- Returns `[{qname, signature, one_liner, prose}, ...]`; prose truncated to 200 chars.
- Silently skips any `qname` not found in `store`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_read_prose fingerprint=e1a7046a605c3879cfdfc6f1f5061c1f7d0d2767cc919b6ca7bb05b92321a738 body_fp=a9ffd531c1d9728a4ae256446e8af7f272634eb553508eff6c9b97fc5412f289 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `_read_prose(qname: str, file_path: str, triefacts_root: Path) -> str`

Read the triefact prose body for a symbol from its Markdown file, returning `''` if not found.

- `file_path`: source file path; `.md` suffix substituted to locate the triefact
- `triefacts_root`: base directory containing triefact Markdown files
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:pre_filter_batch fingerprint=326577084ea9bfa1bac4f27dd77047736f358a461af89380db54a0e7df3f99ea body_fp=bbfb92ce3a672d36c3d0a83ceae0b4a090f46955bdf4f2f60781918f2c796d24 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 -->
## `pre_filter_batch(client: TrieClient, callee_pairs: list[tuple[str, str, list[dict], list[tuple[str, str]]]], *, batch_size: int = 8) -> list[tuple[str, str | None, str | None]]`

Use an LLM to judge which callers of changed callees require source updates, processing in batches.

- `callee_pairs`: each entry is `(callee_qname, old_prose, callers, notes_with_reasons)`
- `callers`: list of `{qname, signature, one_liner, prose}` dicts per callee
- Returns `(caller_qname, note, reason)` tuples; SKIP decisions are excluded
<!-- trie:end -->