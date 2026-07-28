---
trie_version: 0.1.9
source: tests/conftest.py
file_fingerprint: a048fc1962f8fef1b800c53d083dcbcd3bab813d2df4737716ce36add193ab0a
last_synced_at: '2026-07-28T23:33:55Z'
description: Shared pytest configuration.
defines:
- kind: module
  qualified_name: tests/conftest:__module__
  lines: 1-29
- kind: function
  qualified_name: tests/conftest:pytest_configure
  lines: 19-22
- kind: function
  qualified_name: tests/conftest:enable_resolver
  lines: 26-28
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/conftest:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=593699a343db6beef2168327cca7f8bbccc77691a90b8f2f6b94ba39854c0e92 source_ref=726dda377d403d86f257162340d531cee3b0f814 role=test -->
Shared pytest session configuration that disables the LSP-backed reference resolver by default, keeping CI fast and free of language-server dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/conftest:pytest_configure fingerprint=7ee1777ea9aac0e8b630418630dd5575cf6e1bd562eea8b229812f4b56b43164 body_fp=dce78b0c81cce96b9a8ba7a9a6b1050a36be865f214ed099a310c0921e63ea21 source_ref=726dda377d403d86f257162340d531cee3b0f814 role=config -->
Set `TRIE_DISABLE_RESOLVER=1` for the entire pytest session unless already assigned.
<!-- trie:end -->
<!-- trie:section symbol=tests/conftest:enable_resolver fingerprint=0029afe05ab6b2e95ba51fa8c6a015d917a110d3e002fc0d1980eff5c7a2c6b7 body_fp=a37cab44264ddd6a180a676dfc8e87a4f8832ff97b4c62728024cff9d019d2eb source_ref=726dda377d403d86f257162340d531cee3b0f814 role=test -->
Pytest fixture that removes `TRIE_DISABLE_RESOLVER` from the environment, re-enabling the LSP resolver for one test.
<!-- trie:end -->