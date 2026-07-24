---
trie_version: 0.1.9
source: trie/session_diff.py
file_fingerprint: a15e28b78727eb95673be1840c4233583fe33a0c52a8fe65db477ac475ed410f
last_synced_at: '2026-07-23T16:52:13Z'
defines:
- kind: module
  qualified_name: trie/session_diff:__module__
  lines: 1-395
- kind: class
  qualified_name: trie/session_diff:SessionDiff
  lines: 8-27
- kind: method
  qualified_name: trie/session_diff:SessionDiff.is_empty
  lines: 16-18
- kind: method
  qualified_name: trie/session_diff:SessionDiff.session_ids
  lines: 20-27
- kind: function
  qualified_name: trie/session_diff:collect_session_diff
  lines: 30-63
- kind: function
  qualified_name: trie/session_diff:_diff_stat
  lines: 66-132
- kind: constant
  qualified_name: trie/session_diff:_FENCE
  lines: 135-135
- kind: function
  qualified_name: trie/session_diff:build_narrative_prompt
  lines: 138-210
- kind: constant
  qualified_name: trie/session_diff:_NARRATIVE_SYSTEM_PROMPT
  lines: 213-213
- kind: function
  qualified_name: trie/session_diff:synthesize_narrative
  lines: 216-239
- kind: function
  qualified_name: trie/session_diff:render_digest_section
  lines: 242-340
- kind: constant
  qualified_name: trie/session_diff:DIGEST_HEADER
  lines: 343-349
- kind: function
  qualified_name: trie/session_diff:upsert_digest
  lines: 352-394
incoming_refs: 7
outgoing_refs: 0
---
<!-- trie:section symbol=trie/session_diff:DIGEST_HEADER fingerprint=2489ada105087413e2d4eefcdb9e77dd574da2f5bd807a6667d71648801a55fe body_fp=85e5c4957d7e11c32ad8c0bf267b06034c8ddd71ad0de2c81852b931990343f2 source_ref=ae02b502c9f8e807253f03fc80f434a5d367070a role=model -->
Module-level constant holding the canonical header prepended to every `TRIE_DIFF.md` file.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff fingerprint=7c0b1e542ac3b479e297632536c9d57689d4ef3ee060d3adaadb6729307fa85d body_fp=099e1a45d5f9276ca9c87608b05863ae8aff4d045b9903a76b0d559c4f797a3c role=monitoring-telemetry -->
`SessionDiff` is a dataclass that bundles all evidence gathered for a single working session during a `trie diff` run: the raw git diff of the triefact tree (the observed effect), a list of patch notes that agents have already applied (stated intent from the session log archive), and a list of patch notes still pending in the store's patch queue. It exposes helpers to check whether there is anything substantive to report (`is_empty`) and to enumerate the distinct session identifiers that appear across both note collections (`session_ids`), providing a self-contained evidence package that downstream functions use to assemble prompts and synthesise intent-level narratives via the LLM.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.is_empty fingerprint=b504b8745ff4143898c9714c49334e7cddcc10cdc565b4138d8a7af47c65b935 body_fp=5234d8be87e1b1a18b15c598ba1072f96483ee8544646ea3d00c11b30fbe2976 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Return `True` when `SessionDiff` has no diff text, no applied entries, and no pending entries.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:SessionDiff.session_ids fingerprint=f8703e92cc108bac529c20bce6b83766f976d0424f7683d4e60f831b962e00f2 body_fp=a965b48afc59b753e1813be79724b80ffd65d52960bca31c9e3774495446941a source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Return distinct, non-empty session IDs from `SessionDiff.applied` and `SessionDiff.pending`, preserving insertion order.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_FENCE fingerprint=7c0a24375f67cb32fbd350a1aa89f4ee1f6465b35df8cd422b0b4544c79625fd body_fp=495f5faefeb45ddc9bcce9c02534008c66427931a9356c9dbaa0b4f96ac92de2 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=util -->
Module-level constant holding a triple-backtick string used to open and close fenced code blocks in prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_NARRATIVE_SYSTEM_PROMPT fingerprint=9f0fb70d148a2f9a31181a2d03b675ec6c42e804109a3de7167aa2febb914234 body_fp=c9f055d6ad0e960b05a339739ac09ef6051d7baa9eb0ff5e8fce3c6582a8ee63 role=llm-client -->
Module-level constant holding the system prompt injected into the LLM call by `synthesize_narrative`. It instructs the model to produce a coherent, intent-level markdown summary of a working session from patch notes and unified diff evidence, and explicitly requires that any sub-headings in the output use `###` or deeper — never `#` or `##` — so the narrative embeds safely beneath the `##` entry heading used by the digest format.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f7ac74e700c9f55a4df46bc527fd1934f92f28b128cdb3a9aa08fcdc246c476a source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=domain -->
Defines `SessionDiff` and utilities for collecting, formatting, and synthesising LLM narratives from per-session triefact diffs and patch notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:_diff_stat fingerprint=01b569d6a504b045da8ff566a94f2f6d372a02b875f3f6047a1e391511f3b18b body_fp=9099247353b6cc31473b3e8dca39518b294926a88d4e760e42ce0781bec66807 source_ref=ae02b502c9f8e807253f03fc80f434a5d367070a role=parsing -->
Parse a unified diff string into per-file line-change tuples `(path, added, removed)`.

- Prefers the `b/` side of each `diff --git` header; falls back to `a/` side; skips `/dev/null`.
- Strips `a/`/`b/` prefixes and leading absolute-path components to yield relative paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:build_narrative_prompt fingerprint=5773311045be8b578e3b765937c1e6be9ed0a79774f919b8cea167a0cc3883c1 body_fp=527197f111b13f32dd55a7e79273a8e63bf4766bd070e6b7b0e4a59a358c2ad9 source_ref=2fd24a66abd87a87819892d8d61ea7471cee29cb role=util -->
Assemble the LLM user prompt from a `SessionDiff`, ordering session intents, applied patch notes, pending patch notes, and the raw triefact diff as Markdown sections.

- `max_diff_chars`: hard character limit at which the diff block is truncated before inclusion.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:collect_session_diff fingerprint=e99566072d1aa60f6284e1dbe197404a57f1a14b1669e9463722b79ca36d44bb body_fp=ec00c194b0806130bfe826c4e1e4a08be17e9ec42620e7edd0add19d7fafd040 role=monitoring-telemetry -->
`collect_session_diff` assembles a complete `SessionDiff` for a given working session by retrieving the git diff of the triefact tree against a specified base ref, fetching applied patch-note entries from the session log (optionally restricted to entries recorded after a `since` timestamp and/or a specific `session_id`), gathering still-pending patch notes (both modifications and creations) from the store, optionally filtering everything down to a single `session_id`, and returning the bundled result.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:render_digest_section fingerprint=025c67ca420fd82556e0a6622ccc336dfce02743e20c50b2dbfb54c4ffcb3cf6 body_fp=40122379eb3e52b67c2fea6c5107520157fe2bf25bfc2d25429a5b46181ac667 role=monitoring-telemetry -->
Render a `SessionDiff` as a single markdown section string suitable for insertion into TRIE_DIFF.md. The entry opens with a `## <date> · base <ref>` heading; any optional LLM-generated narrative is embedded immediately after, with its H1 and H2 headings demoted to H3 (fence-aware, so code blocks are never mangled) so that no narrative heading competes with the entry heading. Deduped session notes are listed under `### Intent`, applied and pending trie operations under their own sub-sections, and per-file line-change statistics derived via `_diff_stat` appear under `### Triefact changes`.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:synthesize_narrative fingerprint=125367ea15e6796601e0dc15e8e08cb3d24b89b8b89b99efd6848e5d08ec3391 body_fp=53f5a21e457195ee275deb725021f6edc6a0c1d815dbcb9aabd1c16005ee3e6a role=llm-client -->
Synthesise a coherent intent-level session narrative from the collected evidence by calling the LLM client. The assembled evidence prompt is passed as a `cache_prefix` so that repeated `trie diff` runs within the Anthropic cache TTL reuse the cached evidence block rather than re-billing it; clients that do not accept `cache_prefix` (such as test fakes) are handled transparently via a `TypeError` fallback to the standard single-prompt call. The system prompt referenced as `_NARRATIVE_SYSTEM_PROMPT` is injected directly into the LLM call at runtime, so any updates to that string (including instructions to restrict narrative headings to `###` or deeper) are automatically picked up without changes here. Returns the narrative as stripped markdown text.
<!-- trie:end -->
<!-- trie:section symbol=trie/session_diff:upsert_digest fingerprint=24a841de36daa97019e66becc85e857937f964247eed76168fbf7eac8fb59b10 body_fp=df3f67421c4a0fdf319ef4ba89a5a0347c5af853e8610d90cc397eec6a77ee52 role=documentation-sync -->
Prepends a new digest section to the TRIE_DIFF.md content, replacing the head entry when it shares the same `base_short` commit (amend/retry deduplication), and otherwise inserting it at the front. Entry boundaries are detected only by lines that strictly match the canonical entry-heading shape (`## YYYY-MM-DD … · base <hex>`), so LLM narrative content that legally contains bare `##` headings can never be mistaken for entry delimiters. The result is truncated to `max_entries` and always starts with the canonical `DIGEST_HEADER`.
<!-- trie:end -->
