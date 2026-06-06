---
trie_version: 0.1.5
source: tests/test_check.py
file_fingerprint: 7c580b8c9143a2b2172cb5cc809adee8dfd121d71bda42e370ba4ac8b02b7b3e
last_synced_at: '2026-06-06T13:15:12Z'
defines:
- kind: module
  qualified_name: tests/test_check:__module__
  lines: 1-213
- kind: function
  qualified_name: tests/test_check:project
  lines: 16-28
- kind: function
  qualified_name: tests/test_check:_sync_all
  lines: 31-34
- kind: function
  qualified_name: tests/test_check:test_clean_after_fresh_sync
  lines: 37-41
- kind: function
  qualified_name: tests/test_check:test_missing_triefact_detected
  lines: 44-50
- kind: function
  qualified_name: tests/test_check:test_stale_section_detected
  lines: 53-60
- kind: function
  qualified_name: tests/test_check:test_missing_section_detected
  lines: 63-72
- kind: function
  qualified_name: tests/test_check:test_orphan_section_detected
  lines: 75-84
- kind: function
  qualified_name: tests/test_check:test_private_only_file_requires_a_triefact
  lines: 87-98
- kind: function
  qualified_name: tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact
  lines: 101-112
- kind: function
  qualified_name: tests/test_check:test_clean_when_all_in_sync_with_human_prose
  lines: 115-123
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_zero_when_clean
  lines: 126-132
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_nonzero_when_stale
  lines: 135-143
- kind: function
  qualified_name: tests/test_check:test_cli_verify_quiet_mode
  lines: 146-157
- kind: function
  qualified_name: tests/test_check:test_cli_verify_detects_tampered_body
  lines: 160-174
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_tampered_body
  lines: 177-191
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_legacy_section
  lines: 194-212
incoming_refs: 0
outgoing_refs: 34
---
<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=09ba3c3fe84ec31573178774b0922a88db7ce75e06177e612d1ead57df77e732 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests for the `check` module that validates triefact consistency against source code.

- `project` fixture: creates temporary project with test configuration and source files
- Tests cover missing triefacts, stale sections, orphaned sections, and tampering detection
- CLI verify command tests ensure proper exit codes and output formatting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=1a7240f36d25f490ba94141a932314b476780fe67b0309a713a0de5441a3b135 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Creates a temporary project directory with trie configuration and Python source files for testing.

- Returns the project root path containing `trie.toml`, `src/alpha.py`, and `src/beta.py`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=2319aaf7307a31aa136e06ddb84dd261f6ef7fdbb25fbcfbda6b959c3a11d06d body_fp=75f37536cf535d9ba1e783ec842c5f7c7fc3a32fbd6056587657be1e9163ad85 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Synchronizes all Python files in the project/src directory using FakeTrieClient for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=b87ba7edf9b4f592caebd54b5f8d252b786700dab9d601235c29bd1e68b66305 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies check_project reports clean status after syncing all project files with triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=ed6715e14dcba4dfbb788120e08c8f43538a2fbfb51ee965d10b68956c9505fd source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Verifies that check_project detects when no triefacts exist for source files that contain symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=dc67080b0b56738c7f23fd8a1d4180d362cd28f427a9a67202d3545731b478c6 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests that `check_project` detects when source code changes make existing triefact sections stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=9ee626c0e4396d8b17387cb5b79e66eccfb5a282123dd0cfa461ac34732eccea source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies that check_project detects newly added symbols missing triefact sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=5dc2aee4fbeeb5fbb2fdab400a32a765af740532888921c251ebd2adbda11ecc source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests that `check_project` detects orphaned documentation sections when source symbols are deleted but triefact sections remain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_private_only_file_requires_a_triefact fingerprint=98ffaaffbffb6147cea08a7a5a60f8def21a95b776735ea3669398bf858f7064 body_fp=6c12fd22a8b1725b50006ad7b8c85c6d8c94e2937caee5f934ff3ea516cd1df9 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies that files containing only underscore-prefixed symbols still require triefacts and trigger MISSING_TRIEFACT checks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact fingerprint=f2ee7c27204c5bcfe8fe822d998b2b04f3982ae52c32d3ce7f7fd297a92696e3 body_fp=bffd0a7fd7e5d1a92aa97d635c8bacf0b6a764818846cdc19be70e2324eaaaad source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies that files containing only imports generate no check items since they have no documentable symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=5c3e54d0002c624f008d51bf38d4d564a38dd531bc26f7167c5d0d3a8860c085 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies that check_project returns clean status when triefacts contain hand-written prose alongside generated sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=033e3d33e8c97ebb8e85255a4c9723cde35a48b69fd8a6b9d3818ae8957d6662 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Verifies that `trie verify` CLI command exits with code 0 when triefacts are in sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=e7b022f2b27148f10bce1643f78e9e74b1d5db0784ed00ed9ab736191f29da44 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests that the CLI verify command exits with code 1 when triefacts are stale.

- Creates stale content by modifying source after sync
- Verifies exit code 1 and presence of "stale" and symbol name in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=7ba0daf253e8d2fa4a0f0c644f992a437448770c1afc15410d1124cf2ab0b54d source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests that the CLI verify command's quiet mode suppresses per-symbol details but retains summary error output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=1dbf23489cb261c47fd1656de1b75154589a3dc4fe22bc186249539be86a15f1 body_fp=9712cb82c06ec26fc650535a2338b2f72a84fd5e5a86db400741607f4286221b source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Tests that CLI verify command detects hand-edited triefact content and exits with error code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=73497d814b012250d67621e3dd5ff6075add11f22f4e6c837fbdb9b4c4e0ef38 body_fp=1fe7f793031a0d8f26d3d659ffdc7d4072ce81b9aa53c2a2fa49d38f0241e0a2 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Verifies that check_project detects hand-edited content within section sentinels using body fingerprinting.

- Tampers with triefact content by replacing generated text with "DIFFERENT TEXT"
- Expects check_project to flag the modification as TAMPERED_BODY
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=2a295dad7d8e0da4d59c75da9ecd46b3aabf0defd4eee479cb7baf1649c9cf46 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=change-detection -->
Verifies that check_project detects sections without body_fp attributes as legacy sections requiring regeneration.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=97308f7817fb8c482d92ae937b7891d355b4fe238363f0ab657692b451bf851b source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Test suite for trie's check functionality that detects stale triefacts and synchronization issues.

- **project**: Creates temporary project structure with trie.toml config and sample Python files
- **test_clean_after_fresh_sync**: Verifies freshly synced project reports clean status
- **test_missing_triefact_detected**: Checks detection when no triefacts exist for source files
- **test_stale_section_detected**: Validates identification of outdated triefact sections after source changes
- **test_missing_section_detected**: Tests detection of new symbols not yet documented
- **test_orphan_section_detected**: Confirms identification of triefact sections for deleted symbols
- **test_private_only_file_requires_a_triefact**: Ensures files with only underscore-prefixed symbols still need documentation
- **test_file_with_no_parser_surfaced_symbols_needs_no_triefact**: Verifies import-only files are excluded from checks
- **test_clean_when_all_in_sync_with_human_prose**: Confirms hand-written content doesn't trigger false positives
- **test_cli_verify_exits_zero_when_clean**: Tests CLI verify command success on clean projects
- **test_cli_verify_exits_nonzero_when_stale**: Tests CLI verify command failure on stale projects
- **test_cli_verify_quiet_mode**: Validates quiet flag suppresses detailed output while preserving summary
- **test_cli_verify_detects_tampered_body**: Tests detection of manually edited triefact content
- **test_check_project_detects_tampered_body**: Unit test for tampered body detection
- **test_check_project_detects_legacy_section**: Tests identification of pre-fingerprint triefact sections
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=2b898a92de2a4e464eabe2dfc7420ebb245b3b49bf51ce92cac069aa72afa39a source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Creates a temporary test project with configuration and sample Python files for trie functionality tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=2319aaf7307a31aa136e06ddb84dd261f6ef7fdbb25fbcfbda6b959c3a11d06d body_fp=4c05b2521d110655e765397e22f5091099cef2b91bd3d575835cb8e1761c9ea5 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Synchronizes all Python files in a test project's src directory using a fake client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=cc60077ebba067560a22b96aac66ddce0fd43efb8009cb03d6d7514ef76de613 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies that `check_project` reports clean status after synchronizing all files in a test project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=6f7e0825ead39f21201049a6566a61bad6330a5d64e7fcd7f992d44341f3a64b source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that `check_project` detects when no triefacts exist for source symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=851fa96e0419bb0547a88990af6416c1bcc90745ce4532224a20ae6c0d7b6b73 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies that `check_project` detects stale triefact sections after source code changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=3bcb391bfeb4edbcc505801d329f4f330d176f181e6785986850f4a2c6b7f3c4 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that `check_project` detects when a new symbol in source code lacks a corresponding triefact section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=aa008f9de2b932300b48d1776e83402b9aea3403282df4cae9daec46be00fc78 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that `check_project` detects orphan sections when source symbol is deleted but triefact section remains.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_private_only_file_requires_a_triefact fingerprint=98ffaaffbffb6147cea08a7a5a60f8def21a95b776735ea3669398bf858f7064 body_fp=2b1bb547a178e0a71dbbc9b350dddf1c4d1c53b10874bdb4ce0f45da453c4231 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies that files containing only underscore-prefixed symbols still trigger MISSING_TRIEFACT during check operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact fingerprint=f2ee7c27204c5bcfe8fe822d998b2b04f3982ae52c32d3ce7f7fd297a92696e3 body_fp=fead9196c2fb018d85a2e671e3f2743410cd102ab3170927def14c5a207fd2d0 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies that files containing only imports are excluded from staleness checks since they have no documentable symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=b26b061af68c378612327daf4ca7d38d79562892e9b72a6feb27538214b126ef source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies `check_project` remains clean when triefacts contain manually added prose outside generated sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=f47329ea59627aedec0032c1052ec09f249b54473dd6c82aa96142a30b5aa3d4 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Verifies that CLI `verify` command exits with code 0 when triefacts are coherent with source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=ace866d21bdee91f28bd453aa91eff487330d27c45cc331ac39486569a84398a source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that CLI verify command exits with code 1 when triefacts are out of sync with source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=b458aa54e6c5cd81226589e3d5bccdfeb6590ac81d26640d707d2f1bbfc52497 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that CLI verify command with --quiet flag suppresses per-symbol details while preserving error summary.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=1dbf23489cb261c47fd1656de1b75154589a3dc4fe22bc186249539be86a15f1 body_fp=29144214a932e322de74fe0a27a358e465dc9dba4abbf7c44b8e5e68d42f9a06 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that CLI verify command detects when triefact section body content has been manually edited and reports tampered body error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=73497d814b012250d67621e3dd5ff6075add11f22f4e6c837fbdb9b4c4e0ef38 body_fp=884442ebc008a1d7d851005b2c5386aef553da10358bff334de2d3feba595bc3 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that `check_project` detects manually edited content within triefact section sentinels via body fingerprint validation.

- Modifies generated triefact content by replacing the original text with "DIFFERENT TEXT"
- Verifies that `StaleReason.TAMPERED_BODY` is flagged for the modified section
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=b72bb69efd37fc5992d4d5384782c295f045a9bbdf55d9ce185ad28967d6ca7c source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
Tests that check_project detects sections missing body_fp attributes as legacy format requiring updates.
<!-- trie:end -->