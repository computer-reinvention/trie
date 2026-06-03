---
trie_version: 0.1.5
source: trie/parse/python.py
file_fingerprint: 6cc182c49cdbbec0046c0972db86bdad4bbbcfaa64c0c1ee1e6da2c2fa823edd
last_synced_at: '2026-06-03T21:14:11Z'
defines:
- kind: module
  qualified_name: trie/parse/python:__module__
  lines: 1-563
- kind: constant
  qualified_name: trie/parse/python:PY_LANGUAGE
  lines: 10-10
- kind: class
  qualified_name: trie/parse/python:Symbol
  lines: 14-28
- kind: function
  qualified_name: trie/parse/python:_make_parser
  lines: 31-34
- kind: function
  qualified_name: trie/parse/python:_node_text
  lines: 37-38
- kind: function
  qualified_name: trie/parse/python:_module_key
  lines: 41-44
- kind: function
  qualified_name: trie/parse/python:_signature_text
  lines: 47-52
- kind: function
  qualified_name: trie/parse/python:_extract_docstring
  lines: 55-65
- kind: function
  qualified_name: trie/parse/python:_normalize_body_tokens
  lines: 68-86
- kind: function
  qualified_name: trie/parse/python:_hash
  lines: 89-90
- kind: function
  qualified_name: trie/parse/python:_build_symbol
  lines: 93-128
- kind: function
  qualified_name: trie/parse/python:_extract_decorators
  lines: 131-144
- kind: function
  qualified_name: trie/parse/python:_undecorate
  lines: 147-153
- kind: function
  qualified_name: trie/parse/python:_walk_class
  lines: 156-202
- kind: function
  qualified_name: trie/parse/python:extract_module_docstring
  lines: 205-223
- kind: function
  qualified_name: trie/parse/python:strip_string_literal
  lines: 226-244
- kind: function
  qualified_name: trie/parse/python:_build_constant_symbol
  lines: 247-291
- kind: function
  qualified_name: trie/parse/python:_is_dunder
  lines: 294-301
- kind: function
  qualified_name: trie/parse/python:_module_level_constant
  lines: 304-327
- kind: function
  qualified_name: trie/parse/python:_build_module_body_symbol
  lines: 330-413
- kind: function
  qualified_name: trie/parse/python:extract_symbols
  lines: 416-562
incoming_refs: 82
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1d0b1eaee344de28ead43745e7b68d7058f187ab37abeaf153eec6b6f8fa3fc2 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Parses Python source files using tree-sitter to extract Symbol objects representing functions, classes, methods, constants, and module-level code.

- `Symbol`: Dataclass capturing qualified name, kind, signature, docstring, body text, location, and metadata
- `extract_symbols()`: Main entry point that returns list of Symbol objects from a Python file
- `extract_module_docstring()`: Extracts module-level docstring following PEP 257 conventions
- `strip_string_literal()`: Removes Python string literal delimiters and prefixes from raw text
- Module symbols include synthetic `__module__` entries for residual top-level code not captured by other symbol types
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PY_LANGUAGE fingerprint=0a5ea4e9caea43b2aff7986c2453aaf98a5439baa3303d103a6a59fb780f0c9c body_fp=3fe6717b1fd7c662c39252a40da125192e9545474f8c3da94e74c9ee74fc53d8 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Pre-configured Tree-sitter language parser for Python source code analysis.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:Symbol fingerprint=67410b76908def7ec7521baef1e77f8fa17f7b64e4da871a7c1b3eac081c35e0 body_fp=eb0ec699a60c1ddf6ccf923b499c2ff02441860f6dde5a64512b6aa790e648b5 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Represents a Python source symbol with metadata for documentation generation.

- `qualified_name`: module-relative identifier like "src/foo:MyClass.method"
- `kind`: symbol type - "function", "class", "method", "constant", or "module"
- `file_path`: source-root-relative path like "src/foo.py"
- `signature`: function/class header text without body
- `body_normalized_hash`: hash of tokenized body for change detection
- `signature_hash`: hash of signature for change detection
- `parent_class`: unqualified class name for methods only
- `decorators`: decorator lines like ("@classmethod", "@property")
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_make_parser fingerprint=f081dfd6916c63e7cd485b9082a93717d76eda229f07a7d0259ca3c3aff9fcbc body_fp=bf6afebbbb4269abff875d323219427f345b7a6a47cbdbd624a9ad73de57fe51 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Creates a tree-sitter Parser configured for Python source code parsing.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=aa6d5ff4a8e0f8217d9664a5fc0765fbf8edce82e01d1b602a1ebc86730295e8 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts the UTF-8 text content from a tree-sitter Node by slicing the source bytes at the node's byte range.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_key fingerprint=547f506083bc19722953e055c01a3da5c50856bd4d4b3dff9592f71eefc0121b body_fp=a66d317f4bc8e659c83a4d53e01a02d272fc69353f8c7bd256963b914f29cb9d source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Converts a file path to a module key by removing the file extension and making it relative to the source root.

- Returns module key string used in qualified symbol names (e.g. "src/foo" for "src/foo.py")
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_signature_text fingerprint=70e588b1dfb009e89ea973b67e2c9a765a3e9957e8fe35814acf708586e52bd7 body_fp=47219f92871ee684fea73a8563924b94c6016832e46f8a73dd2ad1e47769c464 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts function/class header text from a tree-sitter node, excluding the body and trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_docstring fingerprint=776fa902c9dd74faa5590357a1f7ee2b3c2b6d355a41f01172c8db91ff0b127f body_fp=6540c18e155193bbdf70dd35cd5752b8987195ee21ee5f41361744dc9f04d694 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts the docstring from a function or class body node, returning the first string statement or None.

- Returns raw string literal text including quotes
- Only considers the very first statement per PEP 257
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_normalize_body_tokens fingerprint=ce7a5b27392e47868d004b637327812ae0ce542353d09513ad71e087b9dc6cae body_fp=322b713c357b0d6b4d0c8ff08e4754ea99ce16b17055879f9e77e3646e29c77c source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Concatenates all leaf tokens from a tree-sitter node into a normalized string for change detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=cab40cc7af18851f3b97395e7b72cb10a5be1a90b9cb9d0f1907aac65fed9681 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Computes SHA-256 hash of string as hex digest for content fingerprinting.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_symbol fingerprint=7d482d42fbd226f146d9fcf96ed152b3fc0ba990f0e8493c18fbbfca67db0119 body_fp=90bf4b51315de95d0c99dc15875a81ddb8fd16f2f0b33fdc909a5cf86bfcc3b3 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Constructs a Symbol from a tree-sitter node representing a function, class, or method definition.

- `node`: Tree-sitter AST node for the definition
- `module_key`: Module path without extension for qualified names  
- `rel_file`: Source-root-relative file path
- `parent`: Parent class name for methods, None for top-level symbols
- `kind`: Symbol type ("function", "class", "method", etc.)
- `parent_is_private`: Whether parent class is private (affects is_public)
- `decorators`: Tuple of decorator strings from source
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_decorators fingerprint=01ebd6355fccde3b490881e44d30de807fef73abe19e94670494a122c1dd4d18 body_fp=ec850183198f330c97f9b5a15f3de2b0c4987618391aa3a7b5d56e552200ee73 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extract decorator text lines from a tree-sitter `decorated_definition` node as a tuple of strings.

- Returns empty tuple for non-decorated nodes or nodes without decorator children
- Each decorator string has leading whitespace stripped but preserves full decorator syntax
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_undecorate fingerprint=b1cd6642b3e8e0609907b3d1832a68f8329945f8efb185e0fde9651547ddec76 body_fp=d2ce86dc14144039c1de9b6d8f8543d066cf33d621fcfc4c9bf66f1568de1984 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts the inner definition from a decorated_definition node, returning the node unchanged if it's not decorated.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_walk_class fingerprint=e926a23785fb4cbfc49fd08c397167580a455fd3f59e9f6993b28170cd7b360c body_fp=7b9e3c0c8c11b2d3869c82472cd35575c5250caddb968185e28313bc70fa7d44 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts Symbol objects for a class definition and all its methods from a tree-sitter AST node.

- Methods of private classes inherit the private flag and won't be documented
- Returns list starting with the class symbol followed by method symbols in source order
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=c67f9734208c01c790c451416601ffaf367f19ff87c58a9803d23bfb41267219 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Extracts the module-level docstring from a Python file, returning raw literal text with quotes or None.

- Returns the first string literal encountered as an expression statement per PEP 257
- Raw text includes quote marks — caller must strip them for plain content
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=c4fc1412dc160c59834d63fbbddc8628f4910204756161a1a4a51ccdb57e9fd0 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Removes Python string literal quotes and prefix characters, returning the raw content.

- Handles triple-quoted, single-quoted, and prefixed strings (f/r/b/u)
- Returns content with surrounding whitespace stripped
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_constant_symbol fingerprint=1144abec1cfbde2447fcc8744f55915888eacaecc5ff1cea5114b4e662d1b56e body_fp=fd354404658daeef0a060d4c8efcef86988fd8db801b7c6a5a767f919e846623 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Creates a Symbol for module-level variable assignments like `NAME = value` or `NAME: T = value`.

- `node`: wrapping expression_statement node for full line range
- `assignment_node`: inner assignment node containing the right-hand side
- `target_name`: variable name being assigned to
- Signature truncated at first newline to keep one-line summary
- Public status includes dunder names like `__version__` despite underscore prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_is_dunder fingerprint=81d0c40a6404dfb330a7b05e9d459cf47b4ea3d89ac0964b2792d40358fcc217 body_fp=00df44c40f20e6432b9b83be1cfea8be9a7c950b7dc0422152728295d4e31348 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Checks if identifier follows dunder pattern (`__name__`) to classify as public despite underscore prefix.

- Returns True for identifiers wrapped in double underscores with content between them
- Used to mark module constants like `__version__` and `__all__` as public API surface
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_level_constant fingerprint=1470a5b4b31cb494ecca61bdcf5be516af254dc79fde2fc404bbe5345a1d88f7 body_fp=4827a447dc4add5737783b534f9f37d0deba8393a7978c777c8708a7de1556fa source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Checks if a tree-sitter node represents a module-level single-identifier assignment and returns the assignment node and target name.

- Returns `None` for tuple unpacking, attribute assignments, or non-assignment statements
- Only captures `NAME = value` patterns to avoid cluttering the symbol table with ambiguous targets
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_module_body_symbol fingerprint=1910e1890486d83c8a17a98dabde20916177931683219cf50e4edebe4d8cfeab body_fp=449f39a367dff9f056ffe37aad8de7e0bf79019ac872a98f3273e428aafa8cb6 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Creates a synthetic `__module__` Symbol containing residual module-level code not captured by other symbols.

- `consumed_ranges`: line ranges already claimed by functions/classes/constants
- `noise_ranges`: lines with imports or module docstring (excluded from residual)
- Returns None if no interesting residual code remains after exclusions
- Signature summarizes residual line count and first statement preview
- Body contains all unclaimed non-comment, non-empty lines joined with newlines
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=7649dc31526e2e9955a047b483cf348d394b8861d4c34dc940800b91ac0f0ad3 body_fp=81960de6a9e4b1d7c735cb331c737c7db9e1e98e9bc31cac284ebe7b747f4147 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
Parse Python file and extract its top-level symbols: functions, classes, methods, constants, and module residuals.

- `file_path`: target Python file
- `source_root`: root for qualified names (defaults to file's parent)
- `source_text`: override file contents (used for diff-aware regeneration)
- Returns deduplicated symbols sorted by start line
- Creates synthetic `__module__` symbol for residual code not captured by other symbols
- Handles decorators, overloads, and property setter deduplication via last-wins strategy
<!-- trie:end -->