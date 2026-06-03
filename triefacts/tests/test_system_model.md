---
trie_version: 0.1.5
source: tests/test_system_model.py
file_fingerprint: 89134d74cd5363c67eb85753047d3381e5face58e9176f6ddc77037e662db052
last_synced_at: '2026-06-03T21:07:57Z'
defines:
- kind: module
  qualified_name: tests/test_system_model:__module__
  lines: 1-146
- kind: function
  qualified_name: tests/test_system_model:project
  lines: 14-48
- kind: function
  qualified_name: tests/test_system_model:_scanned_store
  lines: 51-55
- kind: function
  qualified_name: tests/test_system_model:test_decorator_marks_door
  lines: 58-63
- kind: function
  qualified_name: tests/test_system_model:test_pyproject_scripts_recognized
  lines: 66-71
- kind: function
  qualified_name: tests/test_system_model:test_exit_boundary_classifies_exit
  lines: 74-89
- kind: function
  qualified_name: tests/test_system_model:test_depth_propagates_from_doors
  lines: 92-99
- kind: function
  qualified_name: tests/test_system_model:test_orphan_detection
  lines: 102-108
- kind: function
  qualified_name: tests/test_system_model:test_salience_orders_doors_above_helpers
  lines: 111-116
- kind: function
  qualified_name: tests/test_system_model:test_role_flow_aggregation
  lines: 119-137
- kind: function
  qualified_name: tests/test_system_model:test_serialization_shape
  lines: 140-145
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_system_model:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b54d1f1f7d32f925a2b731b8b8161a8ced4032f17ca4eaed713262f7b1e7f6d7 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Tests the system model building and classification logic against a synthetic project fixture.

- Creates a mock project with various symbol types (door, exit, orphan, internal functions)
- Validates skeleton classification based on decorators, pyproject.toml scripts, and boundary annotations
- Tests depth calculation, salience ordering, and role flow aggregation
- Verifies serialization produces expected dictionary structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:project fingerprint=214c9d75dd3801a8af064ac91cff44a4630b666ac2c9808af55c7452037fcae1 body_fp=e327e5025ac3081166256b8db2b94c61b6aa55ea610a7615e5eea8f9b83e930e source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Creates a temporary Python project with files exercising different system model node classifications.

- Returns the project root directory path
- Creates `pyproject.toml`, `trie.toml`, and `app.py` with sample code
- Includes door, exit, internal, and orphan node types for comprehensive testing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=fa08654e0180cff489c930bb1c73217e035caf39413ca552462f166952144106 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Creates a Store with project symbols scanned and loaded from the given project path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_decorator_marks_door fingerprint=d969735cb040b76b08db1ef0a5eac50f10e09b0657e0b548aa39ff8f9c574813 body_fp=a81332dba60636e28396352b77dc2d0afc50a0d953331bdf1e06321e4b4764e6 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Tests that functions decorated with framework decorators are classified as 'door' nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_pyproject_scripts_recognized fingerprint=62241a0355b823c565c06c62e62c182c166330865d550992ed34cfa4586cd280 body_fp=b284e9a99a127da60c023fa2e2dad003be77eaebea76299df57b1aeec0f8c291 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Verifies that functions referenced in pyproject.toml scripts are classified as doors in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_exit_boundary_classifies_exit fingerprint=09dc50cb7490089404ecf80987d1d8ee401ee4df9aa465815f0806528936856b body_fp=7a985e9bb951cf25d4c6a64ba335d4faeee69c4210074707bb162d0c997ab3b8 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Verifies that symbols with boundary='exit' in triefact_sections are classified as 'exit' nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_depth_propagates_from_doors fingerprint=f43ce6f67659cb7ac6e061b251291ad012c253085683fe40a935ba28637f7f35 body_fp=c0583e56d8f724ac20690436c44ace5055ea852cd0fca26ed912da506ef005b7 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Verifies that system model nodes have depth calculated as call-chain distance from entry points.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_orphan_detection fingerprint=d518ca586a72fc27df24b7767a51d2b3f6847bd09d85f6122390738fe98674bb body_fp=6b2da0582def6e1a7858924effc857110fc840684c21239142ef4b34f7aa7cc7 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Tests that symbols with no incoming or outgoing references are classified as orphans in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_salience_orders_doors_above_helpers fingerprint=6ba8277f13ffe5ff28cbd3e605af1fdb5b06dfb44765d066c6ad013fee9642d5 body_fp=9d88a7f898cfb166270650f2d89d9aaf9565e34bc2dd480e59cd3af701006573 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Tests that door nodes receive higher salience scores than helper nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_role_flow_aggregation fingerprint=9c2fa0b40fc1724092643310da0bbe604a84de5821c06694c5b558e44ce24101 body_fp=15ffdb74d1663ce01da71a50a22555a2fc06dd3f153d57ef9aab5a783fe32eba source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Verifies system model aggregates role flows by tagging symbols with roles and asserting cross-role call edges appear in role_flows.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_serialization_shape fingerprint=a01f16af180e51665ef54138c1cf5bf0db4302db3d9b482d6f445d23f4f9f5b4 body_fp=41391bf66262a04f77818057248285b7ff6b9280fe8fb3ea2da82119de9fd3f2 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 -->
Verifies that `system_model_to_dict` produces a dictionary with expected keys and node structure.
<!-- trie:end -->