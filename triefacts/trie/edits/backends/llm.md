---
trie_version: 0.1.9
source: trie/edits/backends/llm.py
file_fingerprint: c3b3ec518de4871852248ea4449e909e7c069306001955bc654049e4e2104adf
last_synced_at: '2026-06-17T16:43:21Z'
description: "In-process LLM edit backend \u2014 the default `SymbolEditBackend`."
defines:
- kind: module
  qualified_name: trie/edits/backends/llm:__module__
  lines: 1-112
- kind: constant
  qualified_name: trie/edits/backends/llm:INFER_SYSTEM_PROMPT
  lines: 16-21
- kind: function
  qualified_name: trie/edits/backends/llm:_format_bullets
  lines: 24-28
- kind: function
  qualified_name: trie/edits/backends/llm:_format_neighbours
  lines: 31-39
- kind: function
  qualified_name: trie/edits/backends/llm:build_user_prompt
  lines: 42-75
- kind: class
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend
  lines: 78-111
- kind: method
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend.__init__
  lines: 85-87
- kind: method
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend.generate
  lines: 89-111
incoming_refs: 3
outgoing_refs: 3
---
<!-- trie:section symbol=trie/edits/backends/llm:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9c90bd24c70a91904ed7fbbb9944d9b73944c47d23c215e4f9bc7070b0a6f527 source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=domain -->
Provides the default in-process LLM edit backend that generates symbol source code and documentation via TrieClient calls.

- Contains `InProcessLLMBackend` class implementing the `SymbolEditBackend` protocol
- Includes prompt formatting utilities for feeding context to the LLM
- Wraps LLM calls in exception handling to return structured `EditResult` responses
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:INFER_SYSTEM_PROMPT fingerprint=8afc23778924c3a217e26ecac06330b48c0c6a86e33f7540e1626dbf34ad4259 body_fp=9fc043e5d51bb8817fc7b8d066036c4100bd4d557f36aa85850fa9c5e3106c7c source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=config -->
System prompt template instructing LLMs to update Python source code and generate prose summaries from implementation notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_format_bullets fingerprint=06794d90cf80bcc5df24d952d26044ac387614b80ae7e03f9a9016945af35dd3 body_fp=382b03bfed78aff98fed55a03d0e74f6b1016639192a0b73a3c8c050a898e4cd source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=util -->
Formats notes and reasons into a bulleted markdown list with em-dash separators.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_format_neighbours fingerprint=33a29366c68047da459e83c1d07e3b1c4cb143b536a5e577c4f9d3303a80b99c body_fp=7d162a956e5f64e4c6418d99d662a16b760e39c70742487dff6ba47764b106c1 source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=util -->
Formats a list of neighbour symbols (callees or callers) into a labeled text block for LLM prompts.

- Returns "(none)" message when neighbours list is empty
- Each neighbour displays signature/qname plus optional one-liner description
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:build_user_prompt fingerprint=6b8b0316893439ffc18186bf55ca9883aa99e6fb6e3c198b803db0c4e8d40ec0 body_fp=fd94b1e6ec3cdb2e1d3a549a13b9818f293d9818d6cfc019aaa148222bbada5f source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=util -->
Renders an EditRequest into the user prompt for the LLM.

- Formats implementation notes with reasons as bullet points
- Includes callee/caller context to inform the LLM about dependencies  
- Adds special handling for "create" operations to indicate new symbol creation
- Returns structured prompt with symbol info, prose, notes, and source code
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend fingerprint=65334ff01ec835b103b86ca9e204296891170d1acb51def58c0960e143daf279 body_fp=13c63df107d567fdb170028bda5bdd3189d2a9a6693f7272dcb7965f251de62e source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=io -->
Generates new source code and prose for symbols by calling an LLM via TrieClient.

- `max_tokens`: Maximum tokens for LLM responses, defaults to 4096
- `generate`: Returns `EditResult` with new source/prose on success, error details on failure
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend.__init__ fingerprint=828227fd47c583b3ef2e580a997f6fac7b2194a5866ef4fadd607e5d1c5bc3f3 body_fp=07e96a997f456822ac23cc8d9cf58961274e99e93247414d89834d80936846be source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=model -->
Initializes an InProcessLLMBackend with a TrieClient and maximum token limit.

- `max_tokens`: limits the LLM response length (default 4096)
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend.generate fingerprint=d5f61bbaf4c47e8b48dbb2f635411c4ad84b260da764aefd84999bd433a2444c body_fp=e85dc44c1b706ee9a4975334e607c5e17c79a21f39bfd89ec70530527421fed1 source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=io -->
InProcessLLMBackend.generate processes an EditRequest through the LLM client and returns an EditResult with generated source and prose.

- Returns EditResult with ok=False and error message on any exception
- Uses build_user_prompt to format the request for the LLM
- Extracts source and prose from the SymbolEdit model output
<!-- trie:end -->