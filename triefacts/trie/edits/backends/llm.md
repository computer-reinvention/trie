---
trie_version: 0.1.9
source: trie/edits/backends/llm.py
file_fingerprint: 71f1cb8ce78d68e982f84d72c8c75c95fc88dde7651d0ee93766500143d37e78
last_synced_at: '2026-07-25T01:56:30Z'
description: "In-process LLM edit backend \u2014 the default `SymbolEditBackend`."
defines:
- kind: module
  qualified_name: trie/edits/backends/llm:__module__
  lines: 1-161
- kind: constant
  qualified_name: trie/edits/backends/llm:_NEIGHBOUR_CLAUSE
  lines: 22-25
- kind: constant
  qualified_name: trie/edits/backends/llm:INFER_SYSTEM_PROMPT
  lines: 26-31
- kind: function
  qualified_name: trie/edits/backends/llm:_backend_for
  lines: 34-40
- kind: function
  qualified_name: trie/edits/backends/llm:_system_prompt_for
  lines: 43-47
- kind: function
  qualified_name: trie/edits/backends/llm:_fence_for
  lines: 50-52
- kind: function
  qualified_name: trie/edits/backends/llm:_format_bullets
  lines: 55-59
- kind: function
  qualified_name: trie/edits/backends/llm:_format_neighbours
  lines: 62-70
- kind: function
  qualified_name: trie/edits/backends/llm:build_user_prompt
  lines: 73-115
- kind: class
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend
  lines: 118-160
- kind: method
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend.__init__
  lines: 125-130
- kind: method
  qualified_name: trie/edits/backends/llm:InProcessLLMBackend.generate
  lines: 132-160
incoming_refs: 3
outgoing_refs: 9
---
<!-- trie:section symbol=trie/edits/backends/llm:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9c90bd24c70a91904ed7fbbb9944d9b73944c47d23c215e4f9bc7070b0a6f527 source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=domain -->
Provides the default in-process LLM edit backend that generates symbol source code and documentation via TrieClient calls.

- Contains `InProcessLLMBackend` class implementing the `SymbolEditBackend` protocol
- Includes prompt formatting utilities for feeding context to the LLM
- Wraps LLM calls in exception handling to return structured `EditResult` responses
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_NEIGHBOUR_CLAUSE fingerprint=989c0a9da6668fc866801a925a56c3eec4baf293ed5d0627988b388f0b8398b3 body_fp=2350b6a7c1c6493f36269b81753ca32221cde6c3bec0fbd3218b9a8def848f9e source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=config -->
Sentence appended to every system prompt instructing the LLM to respect callee signatures and caller consumption patterns.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:INFER_SYSTEM_PROMPT fingerprint=18700df5a508a3eebed9030835cc0c8a5687f1199e3cf40e6ca18a1f21dd8a7a body_fp=9fc043e5d51bb8817fc7b8d066036c4100bd4d557f36aa85850fa9c5e3106c7c source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=config -->
System prompt template instructing LLMs to update Python source code and generate prose summaries from implementation notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_backend_for fingerprint=15bcb7a6486369ba0e1e7723a99af0246dab330eaa580aa76e62b6f382857352 body_fp=66671950642a3de6e42ddaacfc5f05c27c5e6b2ce657468f7d886ea03b1d34e8 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=util -->
Resolve and return the language backend for the given file path, or `None` if `file_path` is absent or unrecognised.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_system_prompt_for fingerprint=d811c0221c5ca57bb5f9bd5c4449f8c053affbba7c6244b0895fcb45483357d8 body_fp=53beb6561a810fbad1e1cc09c0ca79edca4149a0138b77cbacbaf06e2b5cd2a7 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=util -->
Return the system prompt string for the given file path, appending `_NEIGHBOUR_CLAUSE` to the language backend's prompt or falling back to `INFER_SYSTEM_PROMPT`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_fence_for fingerprint=bf1935a046d1973fb537157386a4c803313e2811c8482a85cdb04089de69125a body_fp=7df63fac2ecfd992b37fc777f839d6965ba4723c6bcef8187720949d1971c8d1 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=util -->
Return the code-fence language string for `file_path`, defaulting to `"python"` when no backend is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_format_bullets fingerprint=06794d90cf80bcc5df24d952d26044ac387614b80ae7e03f9a9016945af35dd3 body_fp=382b03bfed78aff98fed55a03d0e74f6b1016639192a0b73a3c8c050a898e4cd source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=util -->
Formats notes and reasons into a bulleted markdown list with em-dash separators.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:_format_neighbours fingerprint=33a29366c68047da459e83c1d07e3b1c4cb143b536a5e577c4f9d3303a80b99c body_fp=7d162a956e5f64e4c6418d99d662a16b760e39c70742487dff6ba47764b106c1 source_ref=eb90916dfbd9c9ba0da5fcc7686aa9fd79380eca role=util -->
Formats a list of neighbour symbols (callees or callers) into a labeled text block for LLM prompts.

- Returns "(none)" message when neighbours list is empty
- Each neighbour displays signature/qname plus optional one-liner description
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:build_user_prompt fingerprint=d66e4e6382bbd4bd64a18347710020585e2194a18391aa15a564855bf34a7374 body_fp=0dd9b6c57157bee4b8030f66273acb6469a370aae97bdb351c993d4cdfc3518e source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=domain -->
Renders an `EditRequest` into the user prompt for the LLM.

- Formats implementation notes with reasons as bullet points
- Includes callee/caller context to inform the LLM about dependencies
- Adds special handling for "create" operations to indicate new symbol creation
- Returns structured prompt with symbol info, prose, notes, source code, and output-format instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend fingerprint=ca68aaeafd5210c27b250ff5aea88d6e9dd29778f855ed41b89c610ac0f080f9 body_fp=c7e8e2a5ae0ff951d200bcf0274c5c25c6239da9576a1df5d3bdb126aa161e40 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=domain -->
Generates new source code and prose for symbols by calling an LLM via `TrieClient` using plaintext output parsing.

- `max_tokens`: Maximum tokens for LLM responses, defaults to 16384
- `output_retries`: Unused at call-site currently, stored for future retry coordination
- `generate`: Uses `run_text` with per-file system prompts; returns `EditResult` with new source, prose, module remarks, and new dependencies on success, or error details on failure
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend.__init__ fingerprint=7b70f88577677cd3db09de9b51d33e16ceaf5de66ec4046e3c39a33ac935efc2 body_fp=1a8f43279cd548fe8702425b867794065dfbd4d4222ffe7055524f5faf900308 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=domain -->
Initializes an `InProcessLLMBackend` with a `TrieClient`, maximum token limit, and output retry count.

- `max_tokens`: limits the LLM response length (default 16384)
- `output_retries`: number of generation retries on output failure (default 3)
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/llm:InProcessLLMBackend.generate fingerprint=7e39083442726c0865ec564d0216a25bf8f63ec6f0210ec367d8db581ab7ffc1 body_fp=0036e70ebddf5be4af6285fd713cd89f5e864908fad380d3b962b58a250da529 source_ref=b57a11233c1cdb0e62472879a35ccc265849f415 role=io -->
`InProcessLLMBackend.generate` processes an `EditRequest` through the LLM client and returns an `EditResult` with generated source and prose.

- Uses `run_text` (plaintext, no schema) instead of a structured model call; source and prose are parsed from the raw text output
- System prompt is resolved per-file language via `_system_prompt_for` rather than using a fixed constant
- Populates `module_remarks` and `new_dependencies` fields on success in addition to source and prose
- Returns `EditResult` with `ok=False` and error message on any exception
<!-- trie:end -->