---
trie_version: 0.1.5
source: trie/sync/writer.py
file_fingerprint: 24f293a78cccc5d4636602b4fbef2a42ca35a7ec007a24e5010f4b73e2e11c16
last_synced_at: '2026-06-03T21:17:11Z'
defines:
- kind: module
  qualified_name: trie/sync/writer:__module__
  lines: 1-379
- kind: constant
  qualified_name: trie/sync/writer:SECTION_OPEN_RE
  lines: 42-47
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE_RE
  lines: 48-48
- kind: constant
  qualified_name: trie/sync/writer:SECTION_CLOSE
  lines: 49-49
- kind: constant
  qualified_name: trie/sync/writer:FRONT_MATTER_RE
  lines: 50-50
- kind: function
  qualified_name: trie/sync/writer:hash_body
  lines: 53-60
- kind: constant
  qualified_name: trie/sync/writer:_HEADING_RE
  lines: 63-63
- kind: constant
  qualified_name: trie/sync/writer:_SENTENCE_END_RE
  lines: 64-64
- kind: function
  qualified_name: trie/sync/writer:extract_one_liner
  lines: 67-98
- kind: constant
  qualified_name: trie/sync/writer:AGENT_FRONT_MATTER_KEYS
  lines: 106-111
- kind: class
  qualified_name: trie/sync/writer:Section
  lines: 115-120
- kind: class
  qualified_name: trie/sync/writer:Prose
  lines: 124-125
- kind: constant
  qualified_name: trie/sync/writer:Chunk
  lines: 128-128
- kind: class
  qualified_name: trie/sync/writer:TriefactFile
  lines: 132-313
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.parse
  lines: 137-184
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.empty
  lines: 187-188
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.get_section
  lines: 192-196
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.section_qnames
  lines: 198-199
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.upsert_section
  lines: 203-230
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.sort_sections
  lines: 232-254
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.remove_section
  lines: 256-261
- kind: method
  qualified_name: trie/sync/writer:TriefactFile._append_section
  lines: 263-274
- kind: method
  qualified_name: trie/sync/writer:TriefactFile.render
  lines: 278-313
- kind: function
  qualified_name: trie/sync/writer:render_for_agent
  lines: 316-378
incoming_refs: 67
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/writer:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c90405d227a60d4babaab62f1bb7b669d2c3b15b35b0cccb025fb762135105f4 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Parses and renders triefact files with embedded trie sections delimited by HTML comment sentinels.

- **Section format**: `<!-- trie:section symbol=name fingerprint=hash ... -->` with optional `body_fp` and `source_ref`
- **Fingerprints**: SHA-256 hashes ensure source/triefact coherence and detect manual tampering
- **Parsing**: Extracts YAML frontmatter and alternating prose/section chunks while preserving human content
- **Rendering**: Reconstructs complete triefact files with proper sentinel formatting and blank line separation
- **Agent rendering**: Strips internal bookkeeping (fingerprints, sentinels) for clean agent-facing Markdown
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_OPEN_RE fingerprint=e9ea14248a1eff91bf843154bab1c2f82ee305fad4f1ed4b3d3e25d705262257 body_fp=13932ad52655a8e7ab9b291e0714559e95ca0c0f4e3b41bc34775e04c581516b source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Regex pattern matching triefact section opening HTML comments with symbol name, fingerprint, and optional body_fp and source_ref fields.

- Matches line-anchored comments like `<!-- trie:section symbol=foo.bar fingerprint=abc123 -->`
- Uses named groups for extracting `symbol`, `fp`, `body_fp`, and `source_ref` metadata
- Backward compatible: `body_fp` and `source_ref` are optional for legacy sections
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE_RE fingerprint=49aa71874073d7e43da82cffb2e8446d3946ff6b664d86a74e4b8105f2ce602a body_fp=f7dc8b2dde7bd1b5c0eb62222998112d7b305d3cf65daa43bc1a4a882d08b964 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Regex pattern that matches HTML comment closing sentinels for trie documentation sections.

- Requires the comment to start at line beginning and end at line end
- Allows optional trailing horizontal whitespace after the comment
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:SECTION_CLOSE fingerprint=742e69c224d8d71b2d79094222e59b783d57ae9cf4e3a050b3874e1d05981d20 body_fp=520583f2b620aea2bbfaae9cdcb5f922e822c25036119e353ca6e7b3185c5f27 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Canonical HTML comment string used to close trie documentation sections in Markdown files.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:FRONT_MATTER_RE fingerprint=f100241e2f09e0c34d4dd9fbfafad078e9b2edeb64ad505b28512c83a51cdb48 body_fp=9254c9d02fb4b25f0638e2411d74cafb747378f61b30a224b651652875eecbbb source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Matches YAML frontmatter at the start of a file, capturing the YAML content between `---` delimiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:hash_body fingerprint=ab22edfb13d8ba9c75b86d2384923163f1c839f46c4a2ed06ca566491fc6f96d body_fp=f25338f018538e622517fca4e08a07b5ffe6b8ebe068f7ae63b1691e726cd353 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
## `hash_body(body: str) -> str`

Computes SHA-256 hash of section body with leading/trailing whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_HEADING_RE fingerprint=b171a12459c1801f28b3970483335daeacef5462126ceb123ef5793ee735f80b body_fp=99086de5a8a2b5859b8df2d8e8d7c98da3d839a0666ffea2c1e8fe95524ea5d3 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Regex pattern matching Markdown headings with optional leading whitespace (0-3 spaces) followed by 1-6 hash characters and whitespace.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:_SENTENCE_END_RE fingerprint=46839332c70a94fc506bb56b7637497fd1a8b3a93af0eb5c4ff8390ddeb08946 body_fp=9af3df6824cb757c005266be172ce35df7bbb6674cedd309eb1036f48d8565f1 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Regex pattern that matches sentence boundaries: punctuation (`.!?`) followed by whitespace or end of string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:extract_one_liner fingerprint=fb87254713b9705aec49bf5aaed06df13d5765c8d66d19dd661b746b0045cd82 body_fp=02fa734880039fc4ef9072150fd1772cf409ddd6755a5fe60ce70a149dc18bbb source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Extracts the first sentence from a triefact section body, skipping headings and truncating to a character limit.

- Returns empty string if no usable text is found
- Collapses whitespace and adds ellipsis when truncated
- Stops at first paragraph break or sentence-ending punctuation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:AGENT_FRONT_MATTER_KEYS fingerprint=4ffdf447d675342eb7e62f591eb81f0dbe4b8236a7ecbc21145d49565aaf7fa7 body_fp=8294eda21e5594b41824b5d4aa60944267192f07531bea2c9d8f94d349761f2e source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Defines the frontmatter keys that are preserved when rendering triefacts for agents, filtering out trie's internal bookkeeping fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Section fingerprint=9ba5f768080a5d934fd87a6cab7e6eed1cd53c7a143db4e39169a3f1d1205a7a body_fp=dbad2945c8833b4544a3a27aabfec7a4ce8ea3d6277e24f19a6f8697f35f707a source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Immutable data container representing a parsed trie documentation section.

- `body_fingerprint`: SHA-256 over the body text; None for sections written by trie ≤0.1
- `source_ref`: git blob hash of the file when section was generated
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Prose fingerprint=cf49910dc87437bc09897192fbd13b0a347f9433a85c94f1e599b18c7eceaf2b body_fp=311cfa243f31011d450423a58e02e9136ed13f215e8e825758d63429733d58d7 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Represents verbatim text content between trie sections in a triefact file.

- text: Raw string content preserved exactly as written in the source file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:Chunk fingerprint=27a576a701491dcbdfeae28c3b7f87ee71a034e04c90aa8a336c241cf4a788c1 body_fp=053f0d0a4910d0fbf1cc2bf6dca20f21cc062ed857b3a63b85cbf21506ec62b0 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Type alias for a triefact file component that is either a documentation section or human-written prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile fingerprint=0bed48a61acf0cfc07707fcf183261f7e1de3e9bed89bcd9396c488f428e0104 body_fp=039ff9f2958dc5c080652a92f73341eefaa67b577cc6ab6525041b465f074af6 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Represents a triefact file containing YAML front matter and a sequence of documentation sections or prose blocks.

- `front_matter`: YAML metadata dictionary
- `chunks`: ordered list of Section or Prose chunks comprising the file content
- TriefactFile.parse() creates instance by parsing text with HTML comment delimited sections
- TriefactFile.empty() creates empty instance with no front matter or chunks
- TriefactFile.get_section() retrieves section by qualified name, returns None if not found
- TriefactFile.section_qnames() returns list of all section qualified names in order
- TriefactFile.upsert_section() replaces existing section or appends new one with auto-computed body fingerprint
- TriefactFile.sort_sections() reorders sections to match source line positions while preserving prose
- TriefactFile.remove_section() deletes section by qualified name, returns whether found
- TriefactFile.render() serializes to text with YAML front matter and HTML comment sentinels
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.parse fingerprint=d2f423ca6746de2c7f3e04dbb4ff83ee8a1b5b90dddec9f49559e442a2d86e55 body_fp=3a9073677b7d3797db86a921a68ecbb10ce0b448b2fd558f8f71972317e33390 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
## `TriefactFile.parse(text: str) -> TriefactFile`

Parses a triefact Markdown file into front matter and chunks of sections or prose.

- `text`: Complete triefact file content to parse
- Raises `ValueError`: When a trie section opening sentinel has no matching close sentinel
- Returns sections with body text stripped of leading/trailing newlines
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.empty fingerprint=cc0676809bee8efb34856efbd9c950ae148db930ab90e76ebd3d17bd1eefbc7e body_fp=6cf936ca08fbe35297aba62df1d57f17b36b1e42ae4b35ca3e713e0bed9c5270 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Creates an empty TriefactFile instance with no front matter or chunks.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.get_section fingerprint=aec43c04e2eaaaaf39f4d6be228e0198afa191d15abda68a3879b41b391204d8 body_fp=f1c864958afa692856b1379850a494d51197d0666b7036e896565c4f556bcd1c source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Returns the first Section in TriefactFile.chunks matching the given qualified_name, or None if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.section_qnames fingerprint=b3198e06079669f9cdabe77cd2292e047d5fc68e79e8ecb7e0a9f7bff28f0f60 body_fp=86e2903008214db684f493e3eef6b2c24911be73d69480eaf399c7ba5388e046 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Returns a list of qualified names for all Section chunks in the TriefactFile.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.upsert_section fingerprint=68a8c8a909c8f5a0c7c91dc04c4b6331439d75e93eb0e3af19524143d7c6fccc body_fp=962355e2e1f50dfdf3def9780b0cefdd401bb7469a576f2d5e32ae5576a1eb35 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Replaces an existing section in TriefactFile by qualified name or appends a new section at the end.

- `body_fingerprint`: Computed automatically from `body` parameter
- `source_ref`: When None, field is omitted from rendered sentinel
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.sort_sections fingerprint=3a5abfe00c1190b093875944af69f77a27689bb7a756b7a12c709e067e398038 body_fp=cfef4021f5a47b20f87f08420e8dd76e258fd075ea8f75961c34804d8d01ab14 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
## `TriefactFile.sort_sections(self, start_line_by_qname: dict[str, int]) -> None`

Reorders TriefactFile sections to match their source file line order based on provided line number mapping.

- `start_line_by_qname`: Maps qualified symbol names to their source line numbers
- Sections without mapping entries are placed at the end in original order
- Preserves non-whitespace prose chunks at the beginning
- Drops whitespace-only prose chunks (recreated during rendering)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.remove_section fingerprint=d8dc7a57db15d5144ac0f1cb113b03fbe74d7608b5e9b23572384079c5ce8032 body_fp=5996a343aba10297edc08202681264d31aa48a828166f217c0e477d2aaa9d56e source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Remove a section from TriefactFile chunks by qualified name, returning whether one was found.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile._append_section fingerprint=39d0ed815c7e15cf563957738a217245397a9ae9c72076762ea523a6b7cb189c body_fp=ad87f6b64e97ac718bc4115a03e680d7ec79e36773f752bac0d1c33121df28cd source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Appends a section to TriefactFile.chunks, ensuring proper blank-line separation from preceding content.

- Adds newlines to the last Prose chunk if it doesn't end with double newline
- Inserts a new Prose chunk with double newline after the last Section
- No prefix needed when appending to empty chunks or after front matter
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:TriefactFile.render fingerprint=b89097c162426efec69cd3120b0294e523ca70a0015b74ea3338ace3ca6c5abd body_fp=0c2282fc1ceb8572cccd00aff1f5997b531962fb6ecf2620655fc2fc9680023b source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Serializes TriefactFile to Markdown with YAML frontmatter and trie section sentinels.

- Emits frontmatter block if present, wrapped in `---` delimiters
- Preserves Prose chunks verbatim between sections
- Generates section sentinels with fingerprints and metadata fields
- Ensures blank line separation between consecutive sections
- Auto-computes body fingerprints for legacy sections missing them
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/writer:render_for_agent fingerprint=092ba74e28cdec14b0df2de55c6ab0105f9f6c074da00f6bcccb774d76160d8c body_fp=9d61dda9056130e0aebb96b39bbd6cf24b52590324d5425be84b7f1f8216aaf3 source_ref=b8bc54fd6dfe1be68bb60012cf18b620e9aac632 -->
Strips trie machinery noise from triefact text to produce clean agent-readable Markdown.

- Removes frontmatter bookkeeping fields, keeping only `description`, `defines`, `incoming_refs`, `outgoing_refs`
- Strips HTML comment sentinels around sections, preserving only body content
- Maintains blank line separation between consecutive sections
<!-- trie:end -->