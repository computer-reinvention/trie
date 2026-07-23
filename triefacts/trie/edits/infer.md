---
trie_version: 0.1.9
source: trie/edits/infer.py
file_fingerprint: 31c267118dadd1368cd795308141ee0a105b9af3ca0e132aa3b22d5a9fe81da8
last_synced_at: '2026-07-20T23:25:49Z'
defines:
- kind: module
  qualified_name: trie/edits/infer:__module__
  lines: 1-344
- kind: constant
  qualified_name: trie/edits/infer:MERGE_PROMPT
  lines: 12-18
- kind: constant
  qualified_name: trie/edits/infer:INFER_SYSTEM_PROMPT
  lines: 20-21
- kind: function
  qualified_name: trie/edits/infer:_backend_for
  lines: 24-30
- kind: function
  qualified_name: trie/edits/infer:_system_prompt_for
  lines: 33-35
- kind: function
  qualified_name: trie/edits/infer:_fence_for
  lines: 38-40
- kind: constant
  qualified_name: trie/edits/infer:BATCH_PRE_FILTER_PROMPT
  lines: 43-54
- kind: constant
  qualified_name: trie/edits/infer:FILE_GEN_PROMPT
  lines: 56-70
- kind: constant
  qualified_name: trie/edits/infer:FILE_FIXUP_PROMPT
  lines: 72-82
- kind: function
  qualified_name: trie/edits/infer:_format_bullets
  lines: 85-89
- kind: function
  qualified_name: trie/edits/infer:merge_notes
  lines: 92-123
- kind: function
  qualified_name: trie/edits/infer:infer_source_and_prose
  lines: 126-161
- kind: function
  qualified_name: trie/edits/infer:infer_file_source
  lines: 164-204
- kind: function
  qualified_name: trie/edits/infer:_build_caller_summaries
  lines: 207-254
- kind: function
  qualified_name: trie/edits/infer:_read_prose
  lines: 257-277
- kind: function
  qualified_name: trie/edits/infer:pre_filter_batch
  lines: 280-343
incoming_refs: 15
outgoing_refs: 8
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
<!-- trie:section symbol=trie/edits/infer:_backend_for fingerprint=2f34da59ad1937d0feb67a6a8bd25393313a552e381e2ef3de2605dd18c4235e body_fp=82d80e482be58b61e80f1e2e7f17cbcecc18c9f1d843cd38b93cbcb6d9c0afc5 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=util -->
Resolve and return the language-specific backend for `file_path`, or `None` if the path is absent or unrecognised.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_system_prompt_for fingerprint=23fa700cfc201af321432bd9f865834255ba939ea87d7a2217a8cc1f7c01e779 body_fp=5e994765774157e52e54126599d33223b2db922303af239dd08e8c689e0ec376 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=util -->
Return the appropriate LLM system prompt string for the given file path, falling back to `INFER_SYSTEM_PROMPT` when no backend is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:_fence_for fingerprint=bf1935a046d1973fb537157386a4c803313e2811c8482a85cdb04089de69125a body_fp=7df63fac2ecfd992b37fc777f839d6965ba4723c6bcef8187720949d1971c8d1 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=util -->
Return the code-fence language string for `file_path`, defaulting to `"python"` when no backend is found.
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
<!-- trie:section symbol=trie/edits/infer:merge_notes fingerprint=38cf05d5252872271e75b079389f7f02a91982879efb3c13470d9b446ac63436 body_fp=562abcf30929708463cffd8d6f1a804ba07cacb64fd247ea00b06e94e26b2ff7 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=domain -->
Deduplicates and merges implementation note patches, returning consolidated notes and reasons; bypasses the LLM call for single-patch inputs and falls back to raw notes on any error.

- `patches`: list of dicts with "note" and "reason" keys
- Returns single-element inputs immediately without calling the LLM
- Falls back to unmerged notes if the LLM call raises or returns an empty result
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_source_and_prose fingerprint=bf3845311c74f9548a7f3a16146db8a418904243211496e1ebce9125000d8632 body_fp=3ba470da4c26c147962af0086bb06096836da65b26efd80c8559cb5a280a58bf source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=io -->
Generates updated source code and prose documentation for a symbol using implementation notes via LLM inference.

- `file_path`: selects the language backend for system prompt, code fence, and output parsing
- `max_tokens`: upper bound on LLM response length; defaults to 16384
- Returns tuple of (new_source, new_prose) parsed from free-text LLM output
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/infer:infer_file_source fingerprint=9700673afd79b117f218f25f7481174d3fdd3b03e9e5eaec5ebdd77c22948d6a body_fp=c104d7d305e7c1c38f2055a40ee6e17c246d8fc608f166346b325b87b27fafc1 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=io -->
Generates updated file content and per-symbol prose by applying multiple symbol changes through LLM inference via `client.run_text`, using a language-aware fence and text-parsing helpers.

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
<!-- trie:section symbol=trie/edits/infer:pre_filter_batch fingerprint=9d38b535f74cd6dfc4386afc93e14976a77f214e2b9e085824cbb09c0e36e9b2 body_fp=0a1e12bbc862446219ef3bf68ed513a2fa6c57e5f4c6a33c5f0d0cd1f6afe520 source_ref=694cc0728ce47184322f0b0cd4b5aec5484426a2 role=orchestration -->
Determines which callers need updates when their callees change by batching LLM requests.

- `callee_pairs`: tuples of (callee_qname, old_prose, callers_list, notes_reasons_list)
- `batch_size`: number of callees to process per LLM request
- Returns tuples of (caller_qname, update_note, reason) for callers needing changes
<!-- trie:end -->