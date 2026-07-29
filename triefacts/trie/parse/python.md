---
trie_version: 0.1.9
source: trie/parse/python.py
file_fingerprint: 6ee963c33b59338b4ceb4458609cff112e33b3f4a00a9b11c49a4bc62df1528a
last_synced_at: '2026-07-28T23:33:51Z'
defines:
- kind: module
  qualified_name: trie/parse/python:__module__
  lines: 1-633
- kind: constant
  qualified_name: trie/parse/python:__all__
  lines: 13-13
- kind: constant
  qualified_name: trie/parse/python:PY_LANGUAGE
  lines: 15-15
- kind: function
  qualified_name: trie/parse/python:_make_parser
  lines: 18-21
- kind: function
  qualified_name: trie/parse/python:_node_text
  lines: 24-25
- kind: function
  qualified_name: trie/parse/python:_module_key
  lines: 28-31
- kind: function
  qualified_name: trie/parse/python:_signature_text
  lines: 34-39
- kind: function
  qualified_name: trie/parse/python:_extract_docstring
  lines: 42-52
- kind: function
  qualified_name: trie/parse/python:_normalize_body_tokens
  lines: 55-73
- kind: function
  qualified_name: trie/parse/python:_hash
  lines: 76-77
- kind: function
  qualified_name: trie/parse/python:_build_symbol
  lines: 80-115
- kind: function
  qualified_name: trie/parse/python:_extract_decorators
  lines: 118-131
- kind: function
  qualified_name: trie/parse/python:_undecorate
  lines: 134-140
- kind: function
  qualified_name: trie/parse/python:_walk_class
  lines: 143-189
- kind: function
  qualified_name: trie/parse/python:extract_module_docstring
  lines: 192-210
- kind: function
  qualified_name: trie/parse/python:strip_string_literal
  lines: 213-231
- kind: function
  qualified_name: trie/parse/python:_build_constant_symbol
  lines: 234-278
- kind: function
  qualified_name: trie/parse/python:_is_dunder
  lines: 281-288
- kind: function
  qualified_name: trie/parse/python:_module_level_constant
  lines: 291-314
- kind: function
  qualified_name: trie/parse/python:_build_module_body_symbol
  lines: 317-400
- kind: function
  qualified_name: trie/parse/python:extract_symbols
  lines: 403-549
- kind: class
  qualified_name: trie/parse/python:PythonBackend
  lines: 552-632
- kind: method
  qualified_name: trie/parse/python:PythonBackend.__init__
  lines: 569-571
- kind: method
  qualified_name: trie/parse/python:PythonBackend.extract_file_data
  lines: 573-599
- kind: method
  qualified_name: trie/parse/python:PythonBackend.resolver
  lines: 601-621
- kind: method
  qualified_name: trie/parse/python:PythonBackend.extract_symbols
  lines: 623-624
- kind: method
  qualified_name: trie/parse/python:PythonBackend.source_suffix
  lines: 626-627
- kind: method
  qualified_name: trie/parse/python:PythonBackend.system_prompt
  lines: 629-632
incoming_refs: 85
outgoing_refs: 4
---
<!-- trie:section symbol=trie/parse/python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1d0b1eaee344de28ead43745e7b68d7058f187ab37abeaf153eec6b6f8fa3fc2 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Parses Python source files using tree-sitter to extract Symbol objects representing functions, classes, methods, constants, and module-level code.

- `Symbol`: Dataclass capturing qualified name, kind, signature, docstring, body text, location, and metadata
- `extract_symbols()`: Main entry point that returns list of Symbol objects from a Python file
- `extract_module_docstring()`: Extracts module-level docstring following PEP 257 conventions
- `strip_string_literal()`: Removes Python string literal delimiters and prefixes from raw text
- Module symbols include synthetic `__module__` entries for residual top-level code not captured by other symbol types
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:__all__ fingerprint=75f4b4761ab4154ef265cdd5b70ab9b67253b7c982e224ed1d987be1a574cd85 body_fp=4a013ef95899d51df3bd0d342fd0ba2c4709fe3292ba3b1b30ed181675a675f1 source_ref=c24423fc5755b20e2aa7c07664aecc657778685c role=model -->
Declares the public re-export surface of this module: `KINDS` and `Symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PY_LANGUAGE fingerprint=0a5ea4e9caea43b2aff7986c2453aaf98a5439baa3303d103a6a59fb780f0c9c body_fp=3fe6717b1fd7c662c39252a40da125192e9545474f8c3da94e74c9ee74fc53d8 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Pre-configured Tree-sitter language parser for Python source code analysis.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_make_parser fingerprint=f081dfd6916c63e7cd485b9082a93717d76eda229f07a7d0259ca3c3aff9fcbc body_fp=bf6afebbbb4269abff875d323219427f345b7a6a47cbdbd624a9ad73de57fe51 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Creates a tree-sitter Parser configured for Python source code parsing.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=aa6d5ff4a8e0f8217d9664a5fc0765fbf8edce82e01d1b602a1ebc86730295e8 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts the UTF-8 text content from a tree-sitter Node by slicing the source bytes at the node's byte range.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_key fingerprint=547f506083bc19722953e055c01a3da5c50856bd4d4b3dff9592f71eefc0121b body_fp=a66d317f4bc8e659c83a4d53e01a02d272fc69353f8c7bd256963b914f29cb9d source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Converts a file path to a module key by removing the file extension and making it relative to the source root.

- Returns module key string used in qualified symbol names (e.g. "src/foo" for "src/foo.py")
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_signature_text fingerprint=70e588b1dfb009e89ea973b67e2c9a765a3e9957e8fe35814acf708586e52bd7 body_fp=47219f92871ee684fea73a8563924b94c6016832e46f8a73dd2ad1e47769c464 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts function/class header text from a tree-sitter node, excluding the body and trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_docstring fingerprint=776fa902c9dd74faa5590357a1f7ee2b3c2b6d355a41f01172c8db91ff0b127f body_fp=6540c18e155193bbdf70dd35cd5752b8987195ee21ee5f41361744dc9f04d694 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts the docstring from a function or class body node, returning the first string statement or None.

- Returns raw string literal text including quotes
- Only considers the very first statement per PEP 257
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_normalize_body_tokens fingerprint=ce7a5b27392e47868d004b637327812ae0ce542353d09513ad71e087b9dc6cae body_fp=322b713c357b0d6b4d0c8ff08e4754ea99ce16b17055879f9e77e3646e29c77c source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Concatenates all leaf tokens from a tree-sitter node into a normalized string for change detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=cab40cc7af18851f3b97395e7b72cb10a5be1a90b9cb9d0f1907aac65fed9681 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Computes SHA-256 hash of string as hex digest for content fingerprinting.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_symbol fingerprint=7d482d42fbd226f146d9fcf96ed152b3fc0ba990f0e8493c18fbbfca67db0119 body_fp=90bf4b51315de95d0c99dc15875a81ddb8fd16f2f0b33fdc909a5cf86bfcc3b3 source_ref=fa9cbd6ec28228640aecb7c8b9e6c248cb8c9b38 role=parsing -->
Constructs a Symbol from a tree-sitter node representing a function, class, or method definition.

- `node`: Tree-sitter AST node for the definition
- `module_key`: Module path without extension for qualified names  
- `rel_file`: Source-root-relative file path
- `parent`: Parent class name for methods, None for top-level symbols
- `kind`: Symbol type ("function", "class", "method", etc.)
- `parent_is_private`: Whether parent class is private (affects is_public)
- `decorators`: Tuple of decorator strings from source
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_decorators fingerprint=01ebd6355fccde3b490881e44d30de807fef73abe19e94670494a122c1dd4d18 body_fp=ec850183198f330c97f9b5a15f3de2b0c4987618391aa3a7b5d56e552200ee73 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extract decorator text lines from a tree-sitter `decorated_definition` node as a tuple of strings.

- Returns empty tuple for non-decorated nodes or nodes without decorator children
- Each decorator string has leading whitespace stripped but preserves full decorator syntax
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_undecorate fingerprint=b1cd6642b3e8e0609907b3d1832a68f8329945f8efb185e0fde9651547ddec76 body_fp=d2ce86dc14144039c1de9b6d8f8543d066cf33d621fcfc4c9bf66f1568de1984 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts the inner definition from a decorated_definition node, returning the node unchanged if it's not decorated.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_walk_class fingerprint=e926a23785fb4cbfc49fd08c397167580a455fd3f59e9f6993b28170cd7b360c body_fp=7b9e3c0c8c11b2d3869c82472cd35575c5250caddb968185e28313bc70fa7d44 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts Symbol objects for a class definition and all its methods from a tree-sitter AST node.

- Methods of private classes inherit the private flag and won't be documented
- Returns list starting with the class symbol followed by method symbols in source order
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=c67f9734208c01c790c451416601ffaf367f19ff87c58a9803d23bfb41267219 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Extracts the module-level docstring from a Python file, returning raw literal text with quotes or None.

- Returns the first string literal encountered as an expression statement per PEP 257
- Raw text includes quote marks — caller must strip them for plain content
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=c4fc1412dc160c59834d63fbbddc8628f4910204756161a1a4a51ccdb57e9fd0 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Removes Python string literal quotes and prefix characters, returning the raw content.

- Handles triple-quoted, single-quoted, and prefixed strings (f/r/b/u)
- Returns content with surrounding whitespace stripped
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_constant_symbol fingerprint=1144abec1cfbde2447fcc8744f55915888eacaecc5ff1cea5114b4e662d1b56e body_fp=fd354404658daeef0a060d4c8efcef86988fd8db801b7c6a5a767f919e846623 source_ref=fa9cbd6ec28228640aecb7c8b9e6c248cb8c9b38 role=parsing -->
Creates a Symbol for module-level variable assignments like `NAME = value` or `NAME: T = value`.

- `node`: wrapping expression_statement node for full line range
- `assignment_node`: inner assignment node containing the right-hand side
- `target_name`: variable name being assigned to
- Signature truncated at first newline to keep one-line summary
- Public status includes dunder names like `__version__` despite underscore prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_is_dunder fingerprint=81d0c40a6404dfb330a7b05e9d459cf47b4ea3d89ac0964b2792d40358fcc217 body_fp=00df44c40f20e6432b9b83be1cfea8be9a7c950b7dc0422152728295d4e31348 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Checks if identifier follows dunder pattern (`__name__`) to classify as public despite underscore prefix.

- Returns True for identifiers wrapped in double underscores with content between them
- Used to mark module constants like `__version__` and `__all__` as public API surface
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_level_constant fingerprint=1470a5b4b31cb494ecca61bdcf5be516af254dc79fde2fc404bbe5345a1d88f7 body_fp=4827a447dc4add5737783b534f9f37d0deba8393a7978c777c8708a7de1556fa source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 role=source-parsing -->
Checks if a tree-sitter node represents a module-level single-identifier assignment and returns the assignment node and target name.

- Returns `None` for tuple unpacking, attribute assignments, or non-assignment statements
- Only captures `NAME = value` patterns to avoid cluttering the symbol table with ambiguous targets
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_module_body_symbol fingerprint=1910e1890486d83c8a17a98dabde20916177931683219cf50e4edebe4d8cfeab body_fp=449f39a367dff9f056ffe37aad8de7e0bf79019ac872a98f3273e428aafa8cb6 source_ref=fa9cbd6ec28228640aecb7c8b9e6c248cb8c9b38 role=parsing -->
Creates a synthetic `__module__` Symbol containing residual module-level code not captured by other symbols.

- `consumed_ranges`: line ranges already claimed by functions/classes/constants
- `noise_ranges`: lines with imports or module docstring (excluded from residual)
- Returns None if no interesting residual code remains after exclusions
- Signature summarizes residual line count and first statement preview
- Body contains all unclaimed non-comment, non-empty lines joined with newlines
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=7649dc31526e2e9955a047b483cf348d394b8861d4c34dc940800b91ac0f0ad3 body_fp=81960de6a9e4b1d7c735cb331c737c7db9e1e98e9bc31cac284ebe7b747f4147 source_ref=fa9cbd6ec28228640aecb7c8b9e6c248cb8c9b38 role=parsing -->
Parse Python file and extract its top-level symbols: functions, classes, methods, constants, and module residuals.

- `file_path`: target Python file
- `source_root`: root for qualified names (defaults to file's parent)
- `source_text`: override file contents (used for diff-aware regeneration)
- Returns deduplicated symbols sorted by start line
- Creates synthetic `__module__` symbol for residual code not captured by other symbols
- Handles decorators, overloads, and property setter deduplication via last-wins strategy
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend fingerprint=92565f7a817f7c1fc64667f924eda935ea5c40b0eb1c6ef55250e7303ba12d3f body_fp=f84c9b738b6f2b645ec1afe13b77c7b4b30e000d85a9837d6243485b56750dbe source_ref=c61fb4b47d6f26075dd5ddc521ed6df3b208ef33 role=domain -->
Python `LanguageBackend` implementation performing two-pass reference extraction: tree-sitter structural pass merged with an optional LSP resolver for type-dependent edges.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is supplied; lazily imports `trie.parse.references` to avoid circular imports; merges LSP resolver edges via `merge_references` when a resolver is available.
- `resolver`: returns a cached `LspResolver` instance (backed by pyright/basedpyright via `python_spec()`), or `None` if `TRIE_DISABLE_RESOLVER=1` or no Python language server is on PATH.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=df474718f375e356edb709d78a6ffcf106cf907fae9f3022426a748c7bd2a31d source_ref=6b18d027f2fde66b2f9c651f56ce26abd1f9a014 role=domain -->
Initialize `PythonBackend` with `_resolver` set to `None` and `_resolver_built` flag set to `False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.extract_file_data fingerprint=d899960d72f8d478f73c3ecda1347e57c2653a374bfb3a6ede3fad77ca5024e8 body_fp=4df1018f106a82029655912e778bb7dad692d57b7480b2ff71694d1e3c2f31f4 source_ref=6b18d027f2fde66b2f9c651f56ce26abd1f9a014 role=orchestration -->
Runs `PythonBackend.extract_file_data` via `trie.parse.references.extract_file_data`, then merges jedi-resolved reference edges via `merge_references` if a resolver is available.

- `source_text`: unsupported; raises `NotImplementedError` if provided.
- Returns bare `file_data` if `resolver()` returns `None` or jedi produces no extra edges.
- Returns a new `FileData` with merged references when jedi edges are found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.resolver fingerprint=afacab7bcb91d87953934f526a1133b8e5ee75492fd91b87e207d3ad0bfc4a74 body_fp=89a087afebaa11b258fa640e5533e698aeeeb8deece3995ea07a58db2483116c source_ref=c61fb4b47d6f26075dd5ddc521ed6df3b208ef33 role=domain -->
Return the cached `LspResolver` instance for `PythonBackend`, or `None` if no Python language server is found on PATH or `TRIE_DISABLE_RESOLVER=1` is set.

- Returns `None` silently when `python_spec()` returns `None` (pyright/basedpyright absent) or when the env-var disables it.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=3c89957366e69d82e3b38164d495774b9d49d84739e58355516893cff57098b6 source_ref=c24423fc5755b20e2aa7c07664aecc657778685c role=api -->
Delegates `PythonBackend.extract_symbols` directly to the module-level `extract_symbols` function with identical arguments.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.source_suffix fingerprint=0d2413b04bff4ff328e1d5cc218a534ef60201576447af48787dbf1d882fe72b body_fp=cc01e93bc5637b54c4a9c52ceb57e1932db7cd312949caf7312156e0de87fc89 source_ref=c24423fc5755b20e2aa7c07664aecc657778685c role=util -->
Returns `".py"` as the `PythonBackend` source file extension suffix.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PythonBackend.system_prompt fingerprint=68b3879b22e142efeeb345e19a76ef40d2ca51ec128a736a06d639dcd6b839fe body_fp=96e4822f83a3fb892198a62f924d1246077f7a96ad1e2ddf2a3e8093f3b715c3 source_ref=c24423fc5755b20e2aa7c07664aecc657778685c role=config -->
Return the system prompt string for `PythonBackend` by importing and returning `SYSTEM_PROMPT` from `trie.sync.generator`.
<!-- trie:end -->