---
trie_version: 0.1.5
source: trie/edits/infer.py
file_fingerprint: afdf2df5e2a3a859f2fb1d76788b94c5cb2cb57c8578807d53b70e9808f0db37
last_synced_at: '2026-06-09T09:39:02Z'
defines:
- kind: module
  qualified_name: trie/edits/infer:__module__
  lines: 1-295
- kind: constant
  qualified_name: trie/edits/infer:MERGE_PROMPT
  lines: 13-19
- kind: constant
  qualified_name: trie/edits/infer:INFER_SYSTEM_PROMPT
  lines: 21-22
- kind: constant
  qualified_name: trie/edits/infer:BATCH_PRE_FILTER_PROMPT
  lines: 24-35
- kind: constant
  qualified_name: trie/edits/infer:FILE_GEN_PROMPT
  lines: 37-49
- kind: constant
  qualified_name: trie/edits/infer:FILE_FIXUP_PROMPT
  lines: 51-61
- kind: function
  qualified_name: trie/edits/infer:_format_bullets
  lines: 64-68
- kind: function
  qualified_name: trie/edits/infer:merge_notes
  lines: 71-86
- kind: function
  qualified_name: trie/edits/infer:infer_source_and_prose
  lines: 89-117
- kind: function
  qualified_name: trie/edits/infer:infer_file_source
  lines: 120-155
- kind: function
  qualified_name: trie/edits/infer:_build_caller_summaries
  lines: 158-205
- kind: function
  qualified_name: trie/edits/infer:_read_prose
  lines: 208-228
- kind: function
  qualified_name: trie/edits/infer:pre_filter_batch
  lines: 231-294
incoming_refs: 13
outgoing_refs: 4
---
<!-- trie:section symbol=trie/edits/infer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=51e52733e963bf3d48183853d2dfa4df351467373cac1a8e7cf5a3b4a9cf592a source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Provides LLM-driven inference functions for generating updated Python source code and documentation from implementation notes.

- `merge_notes()` — deduplicates and orders patch notes chronologically
- `infer_source_and_prose()` — generates updated source and prose for a single symbol
- `infer_file_source()` — applies symbol changes to an entire file at once
- `pre_filter_batch()` — filters caller symbols that need updates based on callee changes
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:MERGE_PROMPT fingerprint=f236ccc07197a3f11a346c733f4a4077b44217f3c952664d42fb8dfdd3251b68 body_fp=65572a29e22306c4394432395a2eb0c83e55615863bd2462a184322f3f64e94c source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Prompt template for deduplicating and merging contradictory implementation notes while preserving chronological order.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:INFER_SYSTEM_PROMPT fingerprint=03492b7e67e6343a9d05de7ac4c4923f98ac304cf4fa541ec9103643090f1948 body_fp=31e2b0d568b0e6c86b8f82775d3661e4846b9f25d0fa3ab4d370537dba59f3bc source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
System prompt instructing an LLM to update Python source code and generate high-level prose documentation from implementation notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:BATCH_PRE_FILTER_PROMPT fingerprint=1bbaed87a2efbbcc434fbaecdddfeb484e11070f4c70473d1879a4ce9c78d08c body_fp=1705ee5fbc6247b886ce958d3b21d4486977832cc00c4ac50b04b922f58d932f source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Prompt template for filtering caller symbols that require updates based on callee changes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_GEN_PROMPT fingerprint=973f3e453f3d2b3113d62123d1c6c1f38f217341fc89839c4c2ad947a7447759 body_fp=f3053169a7e937e99f786339fd8edcb61024e09de65727f000b552e9c990bc8f source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Template for LLM prompt that instructs updating multiple symbols within a single Python file.

- **file_path**: Path to the file being updated
- **file_content**: Current complete source code of the file
- **symbol_sections**: Formatted sections describing each symbol's required changes
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:FILE_FIXUP_PROMPT fingerprint=451cc0006d70946707bc0f7a83061fba80e697c059afc79f75fb7c098d132383 body_fp=5e00d1d591b8191b430fc267e8a6b7b3561b3aae5f962f5e12b806bfa01c139a source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Template string for prompting an LLM to fix Python diagnostics errors in file content.

- `file_content`: Python source code with errors
- `diagnostics`: Error messages to address
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_format_bullets fingerprint=276d8d146737b65b171b6b1d440db66fa18b94a20cbc45c2cf752f35f5cd26d4 body_fp=2b929f50319b728e7169b14c5aae6b74989318303d98f0b88d5b234601c5fa79 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=code-editing -->
Formats lists of notes and reasons into bullet-point text with `<bullet>` prefixes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:merge_notes fingerprint=94dfc8addb1bd5773ab4bb3e59e5f6e274f144ce32f80b8cb25fb89f64ee037c body_fp=db377d7618c36731c51edfd5bb863c1ca91f2608dd50c578137928aae6d71676 source_ref=54a33c67c9d8e36844ac25ddbe9d64b173793af3 role=domain -->
Deduplicates and merges implementation note patches, returning consolidated notes and reasons.

- patches: list of dicts with "note" and "reason" keys
- Returns: tuple of deduplicated notes list and corresponding reasons list
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_source_and_prose fingerprint=6a6b9a2bd30ede6d692c4097578a5ba2440d3e24f2a42aa4ea5d4ba051f91a8d body_fp=4ca260804d6f6d0ee4de8c294ab9ffa5c320653a7bb5bf3d40fd2014d5b3206a source_ref=54a33c67c9d8e36844ac25ddbe9d64b173793af3 role=orchestration -->
Generates updated source code and prose documentation for a symbol using implementation notes via LLM inference.

- Returns tuple of (new_source, new_prose)
- Uses INFER_SYSTEM_PROMPT to guide LLM behavior  
- Formats notes and reasons as bulleted implementation notes in prompt
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_file_source fingerprint=9addb0f4c9d475f9f098ba59262116ec023f13c570665f8bb39c7326bb164db1 body_fp=267c8570762e9b3e70b576a54d8f9481d76760ef5f1bccd62899cef2dd2f2f2a source_ref=54a33c67c9d8e36844ac25ddbe9d64b173793af3 role=orchestration -->
Generates updated file content and symbol prose by applying multiple symbol changes through LLM inference.

- `symbols_data`: list of dicts containing `qname`, `old_source`, `old_prose`, `merged_notes`, and `merged_reasons`
- Returns updated file content and mapping of symbol qnames to updated prose descriptions
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_build_caller_summaries fingerprint=59cf63540993328f1a80d75600d7fb74fa0a58b329dae24318e5d01529c485ab body_fp=7cceef828f3fd8ecd38945e34b895bd968a0e5cbe55f30349fc8f3b356a536d3 source_ref=54a33c67c9d8e36844ac25ddbe9d64b173793af3 role=util -->
Builds caller summary dictionaries with symbol metadata, prose from triefact files, and source code.

- `prose` truncated to 200 characters from triefact section body
- `source` truncated to 800 characters from actual source file when `src_root` provided
- Returns empty list if caller has no symbol detail in store
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_read_prose fingerprint=e1a7046a605c3879cfdfc6f1f5061c1f7d0d2767cc919b6ca7bb05b92321a738 body_fp=38174f97de3023d749cde3168198b7cf9038182109fb23db13ad6e2e14565922 source_ref=f3c6b6754ac6e98c7524e99b8a14f67071f93724 role=documentation-sync -->
Extracts prose documentation for a symbol from its triefact markdown file.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:pre_filter_batch fingerprint=9d38b535f74cd6dfc4386afc93e14976a77f214e2b9e085824cbb09c0e36e9b2 body_fp=0a1e12bbc862446219ef3bf68ed513a2fa6c57e5f4c6a33c5f0d0cd1f6afe520 source_ref=54a33c67c9d8e36844ac25ddbe9d64b173793af3 role=orchestration -->
Determines which callers need updates when their callees change by batching LLM requests.

- `callee_pairs`: tuples of (callee_qname, old_prose, callers_list, notes_reasons_list)
- `batch_size`: number of callees to process per LLM request
- Returns tuples of (caller_qname, update_note, reason) for callers needing changes
<!-- trie:end -->