---
trie_version: 0.1.9
source: tests/test_system_model.py
file_fingerprint: a975006e4e09e3e3e7f6c43d81370995712cc49e55fa59e210e45dfcc036446b
last_synced_at: '2026-06-17T16:43:32Z'
defines:
- kind: module
  qualified_name: tests/test_system_model:__module__
  lines: 1-240
- kind: function
  qualified_name: tests/test_system_model:project
  lines: 18-58
- kind: function
  qualified_name: tests/test_system_model:_scanned_store
  lines: 61-65
- kind: function
  qualified_name: tests/test_system_model:_tag
  lines: 68-78
- kind: function
  qualified_name: tests/test_system_model:test_decorator_marks_door
  lines: 81-86
- kind: function
  qualified_name: tests/test_system_model:test_pyproject_scripts_recognized
  lines: 89-93
- kind: function
  qualified_name: tests/test_system_model:test_exit_boundary_classifies_exit
  lines: 96-102
- kind: function
  qualified_name: tests/test_system_model:test_depth_propagates_from_doors
  lines: 105-112
- kind: function
  qualified_name: tests/test_system_model:test_orphan_detection
  lines: 115-120
- kind: function
  qualified_name: tests/test_system_model:test_salience_orders_doors_above_helpers
  lines: 123-128
- kind: function
  qualified_name: tests/test_system_model:test_tests_excluded_by_default
  lines: 131-141
- kind: function
  qualified_name: tests/test_system_model:test_tests_do_not_pollute_door_classification
  lines: 144-150
- kind: function
  qualified_name: tests/test_system_model:test_module_nodes_dropped
  lines: 153-157
- kind: function
  qualified_name: tests/test_system_model:test_blind_spot_method_not_orphan
  lines: 160-185
- kind: function
  qualified_name: tests/test_system_model:test_role_axis_flow_aggregation
  lines: 188-196
- kind: function
  qualified_name: tests/test_system_model:test_subsystem_axis_present
  lines: 199-207
- kind: function
  qualified_name: tests/test_system_model:test_layout_positions_assigned
  lines: 210-216
- kind: function
  qualified_name: tests/test_system_model:test_serialization_shape
  lines: 219-225
- kind: function
  qualified_name: tests/test_system_model:test_cache_roundtrip_and_invalidation
  lines: 228-239
incoming_refs: 0
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_system_model:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b54d1f1f7d32f925a2b731b8b8161a8ced4032f17ca4eaed713262f7b1e7f6d7 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 role=test-infrastructure -->
Tests the system model building and classification logic against a synthetic project fixture.

- Creates a mock project with various symbol types (door, exit, orphan, internal functions)
- Validates skeleton classification based on decorators, pyproject.toml scripts, and boundary annotations
- Tests depth calculation, salience ordering, and role flow aggregation
- Verifies serialization produces expected dictionary structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:project fingerprint=ccc09e8766ed85a6c25e309cdab13eda5c19e8bb350d39beb0c314b2bea807c7 body_fp=b921787baf7480b2951d9b5e5e2d2a7b8b6260f47902b736042812cff942de60 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test-infrastructure -->
Creates a temporary Python project with files exercising different system model node classifications.

- Returns the project root directory path
- Creates `pyproject.toml`, `trie.toml`, `app.py`, and a `tests/` directory with test file
- Includes door, exit, internal, orphan, and test node types for comprehensive testing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=fa08654e0180cff489c930bb1c73217e035caf39413ca552462f166952144106 source_ref=d8a6f46b02bfead98ad5255d34aa189debcb1368 role=test-infrastructure -->
Creates a Store with project symbols scanned and loaded from the given project path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:_tag fingerprint=c3b0fa9e5e2f318fe028b1ed11a7dbbc6439b88e59a6d499ca9371c816b0798f body_fp=94a3d51e39f259611a8c6bc19d62a708a86b70a2f4ac7e9fe5c9d245cef3cd7d source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test-infrastructure -->
Inserts a triefact section record for a symbol with specified role and boundary tags.

- `qname`: qualified name of the symbol to tag
- `role`: architectural role classification (defaults to empty string)
- `boundary`: system boundary classification (defaults to "internal")
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_decorator_marks_door fingerprint=d969735cb040b76b08db1ef0a5eac50f10e09b0657e0b548aa39ff8f9c574813 body_fp=a81332dba60636e28396352b77dc2d0afc50a0d953331bdf1e06321e4b4764e6 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Tests that functions decorated with framework decorators are classified as 'door' nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_pyproject_scripts_recognized fingerprint=62241a0355b823c565c06c62e62c182c166330865d550992ed34cfa4586cd280 body_fp=b284e9a99a127da60c023fa2e2dad003be77eaebea76299df57b1aeec0f8c291 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that functions referenced in pyproject.toml scripts are classified as doors in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_exit_boundary_classifies_exit fingerprint=bd0c5d9912986fe2b4354e35b207821d00f59a0a5eded51092ccd9a010f2607d body_fp=7a985e9bb951cf25d4c6a64ba335d4faeee69c4210074707bb162d0c997ab3b8 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that symbols with boundary='exit' in triefact_sections are classified as 'exit' nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_depth_propagates_from_doors fingerprint=f43ce6f67659cb7ac6e061b251291ad012c253085683fe40a935ba28637f7f35 body_fp=c0583e56d8f724ac20690436c44ace5055ea852cd0fca26ed912da506ef005b7 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that system model nodes have depth calculated as call-chain distance from entry points.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_orphan_detection fingerprint=d518ca586a72fc27df24b7767a51d2b3f6847bd09d85f6122390738fe98674bb body_fp=6b2da0582def6e1a7858924effc857110fc840684c21239142ef4b34f7aa7cc7 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Tests that symbols with no incoming or outgoing references are classified as orphans in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_salience_orders_doors_above_helpers fingerprint=6ba8277f13ffe5ff28cbd3e605af1fdb5b06dfb44765d066c6ad013fee9642d5 body_fp=9d88a7f898cfb166270650f2d89d9aaf9565e34bc2dd480e59cd3af701006573 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Tests that door nodes receive higher salience scores than helper nodes in the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_tests_excluded_by_default fingerprint=f044a1909ee97e408d439f9aa743a9b72d14343ff7285fd50cda9d4542f60f7d body_fp=9448f8d404407a4c892abf962ac95205163b591e168dc6850257d74dd9d7846a source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that test symbols are excluded from main model nodes but captured separately in test_nodes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_tests_do_not_pollute_door_classification fingerprint=abf96ebbb996ec53747cf85b08ef4fd5d8ec0ad8bace606118bed96badfa5976 body_fp=eed0c99b7b3c65b401dca8e34cc33b8bd7185105c796f4b6acfe802085ea0a14 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Ensures test functions are never classified as door nodes in the system model.

- Validates that test nodes with no production callers don't create false door classifications
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_module_nodes_dropped fingerprint=5f16c3908ca73237502cffb41baf5bf93799322685978ef9fe53530f7d1228f5 body_fp=9ca53d2ca32b0e367a9ab5758bed73bd66cc61596a5a8b71927e59ee6dcef466 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that build_system_model excludes module nodes from the system model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_blind_spot_method_not_orphan fingerprint=90ebc2846b4a6df39dcbaff54864db0665ab27ff803c37658a53c61884371af4 body_fp=7abea0f8c1e7017cc826e229eb08c2f29b1ec0a70b9f32531984ebcaef3a69ad source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that orphan classification considers class connectivity for methods with no resolved call edges.

- Creates test project with class method having no direct callers
- Asserts method is classified 'internal' when its class has connections
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_role_axis_flow_aggregation fingerprint=3e49751e4e4937d3cec082d89363da853109500242d95132c66af29cb4276e55 body_fp=d71dd6efb2e07a9a82a233dd9f38e3acbd4812e115cccab8ee4aa4abc65b7362 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that the system model aggregates call flows between architectural roles into weighted edges in the role axis.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_subsystem_axis_present fingerprint=ddc762939a836523614884a8f5649d2f6ad3ac74663ec4cd7e449d2e22ad09fd body_fp=7104debaa6842e2044d6d378287c23c8946a0e997e68329732f719f1ed482ce5 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that system model includes subsystem axis with expected groupings, excluding test files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_layout_positions_assigned fingerprint=0300ef42098ec4e84c001e9a8031be60e5a744201ee7d973a45a4de19c430461 body_fp=102ebf1b13b7bf2b402b9fa9a250397712cd32afffd3bf4780f74dfd980a36c8 source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that system model layout assigns y-coordinates based on call depth, with entry points at top.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_serialization_shape fingerprint=0ebe2a2b42746fc46b860a90c23166975a4a83e74f1d1ff6047ab4da0a010e5e body_fp=712951d050a7c56bede94397d68611708d7d5f939d38ba6afa08e1b07d4f4d8f source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that `system_model_to_dict` produces a dictionary with expected keys, axes structure, and node properties.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_system_model:test_cache_roundtrip_and_invalidation fingerprint=aa5974bad063bfc3e477edc92a4c40b069ba43195b0d38e9fd38e6b2aa906b2f body_fp=f78020187cc06fb9323e799eec112bdf2e480d24d4b5c6f6eb89e9ee01b4a25b source_ref=948ce1c63da732c958469a2bfbd07e092f4cb89c role=test -->
Verifies that build_system_model_cached creates a cache file, returns identical results on subsequent calls, and includes more nodes when include_tests=True.
<!-- trie:end -->