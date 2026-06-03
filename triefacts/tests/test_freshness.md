---
trie_version: 0.1.5
source: tests/test_freshness.py
file_fingerprint: c21306cc630617ff74b1c882b39215fb8d4332a944959c05fd891670ae6e8333
last_synced_at: '2026-06-03T20:55:39Z'
description: Tests for the turn-boundary freshness gate.
defines:
- kind: module
  qualified_name: tests/test_freshness:__module__
  lines: 1-388
- kind: function
  qualified_name: tests/test_freshness:_git
  lines: 45-47
- kind: function
  qualified_name: tests/test_freshness:_init_repo
  lines: 50-53
- kind: function
  qualified_name: tests/test_freshness:project
  lines: 57-78
- kind: function
  qualified_name: tests/test_freshness:test_stamp_round_trip
  lines: 86-89
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_when_missing
  lines: 92-93
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_malformed_json
  lines: 96-99
- kind: function
  qualified_name: tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema
  lines: 102-105
- kind: function
  qualified_name: tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind
  lines: 108-113
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only
  lines: 121-127
- kind: function
  qualified_name: tests/test_freshness:test_scan_mtimes_changes_after_file_edit
  lines: 130-138
- kind: function
  qualified_name: tests/test_freshness:test_ensure_fresh_raises_outside_git
  lines: 146-165
- kind: function
  qualified_name: tests/test_freshness:_run_before_turn
  lines: 173-189
- kind: function
  qualified_name: tests/test_freshness:_run_after_turn
  lines: 192-202
- kind: function
  qualified_name: tests/test_freshness:test_no_stamp_triggers_scan_without_llm
  lines: 205-218
- kind: function
  qualified_name: tests/test_freshness:test_unchanged_state_is_a_noop
  lines: 221-227
- kind: function
  qualified_name: tests/test_freshness:test_head_moved_triggers_scan_without_llm
  lines: 230-249
- kind: function
  qualified_name: tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm
  lines: 252-274
- kind: function
  qualified_name: tests/test_freshness:test_new_file_added_triggers_refresh
  lines: 277-286
- kind: function
  qualified_name: tests/test_freshness:test_removed_file_triggers_refresh
  lines: 289-296
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_picks_up_just_made_edit
  lines: 304-315
- kind: function
  qualified_name: tests/test_freshness:test_after_turn_noop_when_nothing_changed
  lines: 318-324
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_default_runs_after_turn
  lines: 332-349
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_before_and_after_mutex
  lines: 352-361
- kind: function
  qualified_name: tests/test_freshness:test_cli_refresh_outside_git_fails
  lines: 364-387
incoming_refs: 0
outgoing_refs: 36
---
<!-- trie:section symbol=tests/test_freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=0d8f18835c566684ced63f5625573cdaa9b0b9f48748937a9a7604aa146abc47 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests for the turn-boundary freshness gate across its four states: fresh, no_stamp, head_moved, and mtimes_moved.

- Tests stamp file round-trip serialization and malformed input handling
- Tests mtime scanning for in-scope files and change detection
- Tests git repository requirement with NotAGitRepoError outside git
- Tests freshness states: unchanged (noop), no_stamp (scan without LLM), head_moved (scan without LLM), mtimes_moved (sync with LLM)
- Tests CLI refresh command behavior and error handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_git fingerprint=f1eab105158bdbbcda4afb86a01403dc9d52b7dc85a1e29e9e9ed20abfc133db body_fp=70a3d0d03c0279ac345b9dc9b94d4b570b5c6753c45302bac4dbf7aff7178e3e source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Runs git commands with deterministic identity configuration for CI sandbox environments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=69851b3818cc870b5fc87d00e6d6f9c90fe97eaf65023b811be5d48c68fbb8f0 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Initialize a git repository at the given path with deterministic identity for CI environments.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:project fingerprint=e01c8f727530a5c7c7c2f8e977e16ddd4243b91299298f93efeff46d49c525b1 body_fp=4995a054918a5fc88037d6931fcd7d868a6e61850e82cf432f8b60229e72f4d0 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Creates a pytest fixture providing a temporary git repository with trie configuration and two Python modules.

- Returns path to the temporary project root
- Includes `trie.toml` with scope configuration targeting `src/**/*.py`
- Contains `src/alpha.py` and `src/beta.py` with import relationship
- Initializes git repo with single commit containing all files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_stamp_round_trip fingerprint=72338228aae6b7c3fdc3d86653fb22ccd8d2e9d0edaa7dbeef3aa073ef0033c2 body_fp=167f9c52b90246142c33eec8fe2150ab4d399822971bafd1caaf8967c29a84e3 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that writing a Stamp to disk and reading it back produces an identical object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_when_missing fingerprint=d1423324c130c11241ddaf7f21c5be495ca2ee4be0f4e16b370cba152baa9633 body_fp=3c7ed5a411131ecbd618622caaaa5c894a84463d8fea8d3e1402d6c9877ab8c3 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies read_stamp returns None when no stamp file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_malformed_json fingerprint=8794741dc828614cbf9d5e4293c991bf2ac68e37825cc9e9e666da058f8b36ee body_fp=919576352a7478460c2b6be54f30de1e093bd567fdb2bc6d8aba7f4a5b415875 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests that `read_stamp` returns `None` when the stamp file contains invalid JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_read_stamp_returns_none_on_wrong_schema fingerprint=1fb296b592032801dedae599ca493d8e2c74ea94764676276317ff8f0c20edb5 body_fp=6a981dc1b3a52beab201ad073202446b556ee69649d1067d4bad6fd775ba0d1f source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies read_stamp returns None when stamp file contains malformed JSON schema with invalid field types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_write_stamp_is_atomic_no_partial_files_left_behind fingerprint=c94b46ed64f02cf869ec7180ad85978df0d3147e948b402aa9937dcc93ee1df7 body_fp=b5ffb64d08103b4b67d7ff7ef0a3c8d83ef321b4885d6dc2513e3cd697ad97bd source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that `write_stamp` performs atomic file writes without leaving temporary files behind.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_returns_in_scope_files_only fingerprint=760fbeb3332ac39d1c385d18b69323e6eebe70c51abb9d4fab2dc47ab28b6e1d body_fp=4150f422c564df0a747e0ab1930129a0e3ed74b511bdef493fc3feee0c97733e source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies scan_mtimes returns only files matching the config scope, excluding out-of-scope files like trie.toml.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_scan_mtimes_changes_after_file_edit fingerprint=1b67abaef026c1ee9fb5fe6819e8e6f5e8c6d3d998b2dc360702895c4af0eda1 body_fp=6ab1a778ba6ac7a3173f35ba9fc884ef1d45abae404e41aa29f2fc877e95835b source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests that scan_mtimes detects file modification times changing after edits.

- Verifies edited file has different mtime before/after modification
- Confirms unedited files maintain unchanged mtimes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_ensure_fresh_raises_outside_git fingerprint=8367b6046047f80f7b6b3bb2170adbb3f445edbf63f301ce34d542c7e9a78532 body_fp=3597330e1a59a08972829bc29036ec2ce7f1d24d4183adefd8fbda3af9dc531d source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that `ensure_fresh_before_turn` raises `NotAGitRepoError` when called outside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_before_turn fingerprint=af1360c956ad404ceb854af6f7e6bdfff427769e8260556070de5da747ab5d3c body_fp=81c5bc50737e734561dfce57534050a38be8945aa89cb5a712e067a93f1bdcac source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Runs the pre-turn freshness gate on a test project, returning the FreshnessResult.

- `client`: Optional FakeTrieClient for inspecting LLM call counts; defaults to deterministic fake
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:_run_after_turn fingerprint=a442953cd9d0a2624b0fd4681c83c3af537c79593588ab97a22c7bd1a304db1b body_fp=7a60784f6d7e2630788328ba5663a809aed8f20cb6ad4760c75e25b1c9d1ad1f source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Runs the post-turn freshness gate with test configuration and optional mock client.

- `client`: Uses provided FakeTrieClient or creates default deterministic one
- Returns FreshnessResult from ensure_fresh_after_turn call
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_no_stamp_triggers_scan_without_llm fingerprint=b53a0383509dd6c81eb6710ee57bdbdb51f7358a5fc29aa5946076b4ae82c369 body_fp=c02acdd6d86fbdef441147e1d64e3d7be100d2457415b40ed8e500191b72bc95 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests that first run in a fresh checkout scans the graph without calling the LLM.

- Verifies `refreshed` is True with `reason` "no_stamp"
- Confirms LLM client receives zero calls and `incremental` is None
- Validates stamp file is created with current HEAD after refresh
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_unchanged_state_is_a_noop fingerprint=8a432c89b41adb3a659c54709a1d0a2f7012900505ba89d3cd2081611b3e0569 body_fp=4a8660a7bd93b50840d229c87632389c2c9c4348998300295570a82c394b7ecb source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that `ensure_fresh_before_turn` returns unchanged status when called twice without intervening modifications.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_head_moved_triggers_scan_without_llm fingerprint=7c7b6e6971abb581360e4fcb858cf34d7d6f853887f5f33cc6bf13ce11cf2f1b body_fp=9d4447226f5b52cc1a49420a36158c240b6d7ad251e24c9210a461b3811ecc8b source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests freshness gate behavior when git HEAD changes without affecting in-scope files.

- Creates commit with unrelated file to move HEAD without changing source files
- Verifies gate triggers scan refresh but skips LLM calls and incremental processing
- Confirms stamp updates to reflect new HEAD position
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_mtimes_moved_triggers_sync_with_llm fingerprint=b54352bc949a81fb06d57f78672a8214131cebf4b6604abd7fe5d999d8959db7 body_fp=369f4e698fce9540ea8ece3fbc14402367c630a553aa4e8d4b5991fc612893a5 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that editing a file without committing triggers LLM-based refresh with incremental resynchronization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_new_file_added_triggers_refresh fingerprint=72a4d16126c9c220e45e18f140acba2cf99435c57bad3b59f76c56bdbc95df22 body_fp=d75a7e8f4cee7f47bb4e1781df51e5178c07513c323e3bb0360d0e7b35124eed source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests that creating a new in-scope file triggers a freshness refresh with `mtimes_moved` reason.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_removed_file_triggers_refresh fingerprint=7a26a5e8a1330925f3391f5e47a09737745daef82abc9939ca1aedf5e82c41e1 body_fp=4811d1af926dace8783197e9d41a588760f50a46946939ea13d3ade10bd0490e source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that removing an in-scope source file triggers a freshness gate refresh due to changed mtime map keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_picks_up_just_made_edit fingerprint=f419a9fd19a9246b59a331ceb9c9351902e6dbad879171d26f57c9fb510e145d body_fp=019882dc48f0a2c4657ccd174ea1f0080fd9f14f9e34813e4e9e9a1062621dad source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Tests that `ensure_fresh_after_turn` detects file modifications and triggers a refresh with reason `mtimes_moved`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_after_turn_noop_when_nothing_changed fingerprint=9cfb3d3d7aec1e2b94374c89931394b3ad21096fa27413ad4e83b7f74ea4b5ca body_fp=e9b58ef9d000e7f248716500311286d23ed003ee9fa4ba76f819b8b8a99496e5 source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that after-turn freshness check returns unchanged when no source files were modified during the turn.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_default_runs_after_turn fingerprint=f22dd366b40ee69587e3e3da35085658d4520cad79261e3a630c6a948ee431b3 body_fp=94c8239a3c89fdfe7ba559505c68ab42d8c26cb8c108bb03e0bd112db9ba014b source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that `trie refresh` CLI command without flags defaults to after-turn behavior and exits successfully.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_before_and_after_mutex fingerprint=a656ec572aa7041e39940d696a533e02cb4eb833e3cc5e278199b18bccaadb99 body_fp=731b25667dbdabe86b7aa48dbd0eeef3a7ed3c1c08a4827451428d9bb534c11b source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies that passing both --before-turn and --after-turn flags to `trie refresh` returns exit code 1 with mutually exclusive error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_freshness:test_cli_refresh_outside_git_fails fingerprint=ae9d7e6fe8285a8be7c1bc4818e405388a351ffe08979820a130884f7b31210d body_fp=fe490be22a4976488516e33ef2aed1bf635e6967f365370573480e12fee8b72e source_ref=83ee0c7f20ba827538abaac9ac76f3991301821c -->
Verifies the CLI `refresh` command exits with status 1 outside a git repository.

- Creates a project directory with `trie.toml` but no git repo
- Mocks the client factory to avoid API key requirements
- Asserts the command fails with non-zero exit and git-related error message
<!-- trie:end -->