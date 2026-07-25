---
trie_version: 0.1.9
source: trie/edits/textgen.py
file_fingerprint: 2d5d4e609970d3964e42caec9dd5842854402816fa88b6aa8f5929f64fa0eb84
last_synced_at: '2026-07-20T23:25:33Z'
description: Plaintext code-generation protocol + parser.
defines:
- kind: module
  qualified_name: trie/edits/textgen:__module__
  lines: 1-223
- kind: constant
  qualified_name: trie/edits/textgen:PROSE_OPEN
  lines: 46-46
- kind: constant
  qualified_name: trie/edits/textgen:PROSE_OPEN_QNAME
  lines: 47-47
- kind: constant
  qualified_name: trie/edits/textgen:PROSE_END
  lines: 48-48
- kind: constant
  qualified_name: trie/edits/textgen:REMARKS_OPEN
  lines: 55-55
- kind: constant
  qualified_name: trie/edits/textgen:REMARKS_END
  lines: 56-56
- kind: constant
  qualified_name: trie/edits/textgen:NEW_DEPS_OPEN
  lines: 63-63
- kind: constant
  qualified_name: trie/edits/textgen:NEW_DEPS_END
  lines: 64-64
- kind: constant
  qualified_name: trie/edits/textgen:_FENCE_RE
  lines: 73-73
- kind: constant
  qualified_name: trie/edits/textgen:_SINGLE_PROSE_RE
  lines: 75-78
- kind: constant
  qualified_name: trie/edits/textgen:_QNAME_PROSE_RE
  lines: 80-85
- kind: constant
  qualified_name: trie/edits/textgen:_REMARKS_RE
  lines: 87-90
- kind: constant
  qualified_name: trie/edits/textgen:_NEW_DEPS_RE
  lines: 92-95
- kind: function
  qualified_name: trie/edits/textgen:code_block_instructions
  lines: 98-107
- kind: function
  qualified_name: trie/edits/textgen:single_prose_instructions
  lines: 110-117
- kind: function
  qualified_name: trie/edits/textgen:new_deps_instructions
  lines: 120-130
- kind: function
  qualified_name: trie/edits/textgen:module_remarks_instructions
  lines: 133-150
- kind: function
  qualified_name: trie/edits/textgen:multi_prose_instructions
  lines: 153-159
- kind: function
  qualified_name: trie/edits/textgen:parse_code
  lines: 162-184
- kind: function
  qualified_name: trie/edits/textgen:parse_single_prose
  lines: 187-190
- kind: function
  qualified_name: trie/edits/textgen:parse_qname_prose
  lines: 193-198
- kind: function
  qualified_name: trie/edits/textgen:parse_module_remarks
  lines: 201-204
- kind: function
  qualified_name: trie/edits/textgen:parse_new_deps
  lines: 207-222
incoming_refs: 36
outgoing_refs: 0
---
<!-- trie:section symbol=trie/edits/textgen:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3d9167f853fc8efdd7add6f03110966f3ebc42800a8837cde659d28da829ccd7 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Define the plaintext code-generation protocol: delimiter constants, compiled regexes, instruction-fragment builders, and parsers for fenced-block model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:PROSE_OPEN fingerprint=22a631ba87b7172007ea936f6fb7fc7fddc4625c19d16193d53829cac07b7878 body_fp=07fff90135bc13a71d7a003ec197d5974ea7194e42c53d9283b4acb3e1257761 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Opening delimiter string marking the start of an unnamed prose section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:PROSE_OPEN_QNAME fingerprint=e2f703197392ad694338d72fdb52822c78a414819aa072ad25ace2903fa8f9b4 body_fp=decbf6ad375f724047a7247450d8488365e42c123982ceb1308fb79d8dad1d81 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Opening delimiter for a named prose section carrying a `qname=` attribute in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:PROSE_END fingerprint=269866a6428941c72ede53e02c74fea213df5399292ab18d4330fd897e8d2b36 body_fp=ba4d5c0081342d2f7f83fdb9b8f71095243ec40be040ee0de41ff00b31fe292e source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Closing delimiter string that marks the end of a prose section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:REMARKS_OPEN fingerprint=bec92bfc86213fb3388d340d9c157a4683ad6d16a76ca786a88f639f7bfb97ab body_fp=5d756bf0e74e4db327531135ea768e93ca98b9d70f38d1139cd37fbd8cabde81 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=model -->
Opening delimiter string for the optional module-level remarks section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:REMARKS_END fingerprint=344b1e6714459a4cbb53f8912a296ad5d85dc7cdfe76eac481045fbfa413420c body_fp=ef72d18cf7f43d6497a2233ff93d879e030fc69cd206fe316779b09edf15da5f source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Closing delimiter for the `<<<MODULE-REMARKS>>>` section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:NEW_DEPS_OPEN fingerprint=57859e89129188ebdbc34288f69f8573fd91f84546a973346e0b47de315f955e body_fp=3c960d7b43ce77569779eb1d2a5f8dc6cd7bd6f10af4b6adb2ed2c8c62e6c516 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Opening delimiter string marking the start of the new-dependencies section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:NEW_DEPS_END fingerprint=2b39c539b7bac8c3b3294a92dacce0e46a109f26acbb1ee08af51e39c64f7e00 body_fp=60080a649fb676858f7809da361a85c88a9fdc108a659948d354545d22708978 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=config -->
Closing delimiter string marking the end of a `<<<NEW-DEPS>>>` section in model output.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:_FENCE_RE fingerprint=b7a0a1d1e0b7e6f915adeec9b560f5d040f73ddeef8420cc2bf9452844eb5b4c body_fp=f82cbbf1e8ff4ec9db6e0db55b6927497d71bd889c88e0a2c6dd04b8ccfe5713 source_ref=2920ec6006972c7096f62c8d592bc70268fd37ba role=parsing -->
Compiled regex matching a fenced code block, capturing the body in group 1; closing fence must start at column 0, allowing trailing spaces/tabs, so mid-line triple-backticks in the code body do not terminate the match early.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:_SINGLE_PROSE_RE fingerprint=5939b8c408399ff054462c5d30bad5117c980b3ebb01562bd89524ba54028c76 body_fp=0796a568427f693ea4259e5f5b4053e12fcb1bdd03d30857bf24a3a20269e94b source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Compiled regex matching a single `<<<PROSE>>>` … `<<<END>>>` block, capturing the prose body in group 1.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:_QNAME_PROSE_RE fingerprint=2d398dfa4db47498bba1255f88e35aee60a21934beacbd9d643ac00edc6623b7 body_fp=1910de0ea8fb53cbf5b91d9c5773c9e865ca2c2223468b22e1975d97bce55d30 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Compiled regex matching a `<<<PROSE qname=...>>>` section, capturing named groups `qname` and `prose`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:_REMARKS_RE fingerprint=1c7a5c6a4956d87e25c4be6cef90e46ef0b927305dcc68962522130e2157e0e0 body_fp=ebc57b734fe278bc86825c5e186224616547eedc595a702e9c821c20d411ec5b source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Compiled regex matching a `<<<MODULE-REMARKS>>>` … `<<<END-REMARKS>>>` delimited block, capturing its content in group 1.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:_NEW_DEPS_RE fingerprint=1a9564cbf8aed590a49a85136fa624473b5bc5902c6f217f2bd4304771ef0f75 body_fp=0326008c25fc0ee0d2afa1ee52abf7d9094ae0790b45dfd00ed86e6c22d806fd source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Compiled regex matching a `<<<NEW-DEPS>>>` … `<<<END-DEPS>>>` delimited block, capturing its body in group 1.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:code_block_instructions fingerprint=45fbfc43e4b99c388c3b700d81e77d9db0858be020dec4d6f1ea7ac6c3859cbf body_fp=ac81eb86cf0e28b1fa4ce4eafbcc61c819b13d4c9110a02be9bf0439318d9cbf source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=util -->
Return a prompt instruction string directing the model to emit one fenced code block using `fence` as the language tag.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:single_prose_instructions fingerprint=830d55d30d1c0b2b5b0c11e458d1a55d4b7034398ab847049a4da47975d4737b body_fp=311c6c626249af2ed4f06b939ced59c1c25415bcb112fb92ba4d5e60657e0954 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=util -->
Return a prompt fragment instructing the model to emit a single `<<<PROSE>>>`-delimited summary section after the code block.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:new_deps_instructions fingerprint=7a6a8c48597490f1f561067d2c4b1be3b0198dc43a691cea7b0232eb953d8ded body_fp=fe4d9b86069d39129a081c398df2b74b3f9e8437633ac1629865aa370cae47c2 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=util -->
Return a prompt fragment instructing the model to list new external package names in a `<<<NEW-DEPS>>>` delimited section.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:module_remarks_instructions fingerprint=f44d200c75e44950ec057a69c7ae1f998de199cfe7ee7de97df92d0f55b8bd41 body_fp=3dcf2353c53aa45781c65a32069c0427adb43e0a4a8268df9ca27ec07283a1dd source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=util -->
Return the prompt fragment instructing the model to emit a `<<<MODULE-REMARKS>>>` section for any module-level changes the symbol body requires.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:multi_prose_instructions fingerprint=e53565afe364a42652546706aaa9245afb69c51c74897bec84c81458c524987f body_fp=5f4da67f3d17f30363c0abfbea3ff0a815d8e0f20a0009a667ad90302d02fb43 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=util -->
Return an instruction string containing one `<<<PROSE qname=...>>>` delimited template block per entry in `qnames`.

- `qnames`: qualified symbol names to include verbatim in each prose-section delimiter.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:parse_code fingerprint=3c8a1bd42ec496bf1c7de4de13bd50edf0d11bb491242bdba30f8795be0124d9 body_fp=a42892ebf1e31687ad3bab30d44b5ec4d83520d933ec295e6b451480f6754ebb source_ref=2920ec6006972c7096f62c8d592bc70268fd37ba role=parsing -->
Extract the first fenced code block from `text`, stripping trailing prose sections if no fence is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:parse_single_prose fingerprint=6cd31057b458853b19052473b7154a1cbf4ab3b93095af3cefa99ec88ab4140e body_fp=57f84c61189cd12dc7f0527949d09190971fba724f2ee75b6da4371bc451fd78 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Extract the single delimited prose section from `text`, returning an empty string if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:parse_qname_prose fingerprint=0819c9148d944626964faf465f10691d267c36d2e7101a996a7eade729ecfcdd body_fp=afcba8d35aff3d450060b4b80b9fc0d8e97b124792398df2f1ad9ed6300fea4a source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Extract all `<<<PROSE qname=...>>>` delimited sections from `text` into a `{qname: prose}` dict.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:parse_module_remarks fingerprint=424d06c50030efe6d89aa80d2e8f1768bd78f60a42bf579fbdf9131addae4d7d body_fp=6b9a8f8f7ea7c4be93a3fba315e8ea7eda0c2b1aae4afd36db50a4ee23afbb03 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Extract the module-level remarks block from model output, returning empty string if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/textgen:parse_new_deps fingerprint=4d00639a78bb09067b7a7b0588e0747c07d626bc1e5fc0c309f31a9fb90d821f body_fp=85e0f9388749065ca4a5edd69179079afd911979bd4f91a6bc7dffe718ae5fa0 source_ref=389ffb471cd812fe38fc8fd8bbc66a3c3516cd24 role=parsing -->
Extract bare package names from the `<<<NEW-DEPS>>>` block in `text`, stripping bullet/quote noise and skipping relative specifiers.

- Returns `[]` if the section is absent or contains no valid names.
<!-- trie:end -->