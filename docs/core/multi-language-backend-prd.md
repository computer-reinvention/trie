# Multi-language backend — PRD

Status: **planned**. Realizes [EXT-9](./trie-tool-extensions.md) — the
"multi-language indexing" umbrella item, the last structural unlock on the
tool-extensions list.

This document is the spec for generalizing trie from a Python-only engine to a
**language-pluggable** one, with **TypeScript/TSX** as the first non-Python
backend. It covers the full chain — parse → graph (grep/read/trace) → prose
generation → patch/edit — and extends the symbol-kind vocabulary so TypeScript
constructs are represented faithfully rather than coerced onto Python shapes.

The testbed is this repository itself: it carries the Python core, a vendored
TypeScript opencode fork under `opencode/`, and a TypeScript Electron app under
`app/`. "We bootstrap trie with trie" (AGENTS.md) extends to TypeScript here.

---

## 1. Goals / Non-goals

### Goals

- A `LanguageBackend` registry keyed by file extension. Adding a language is
  one new module + one registration, not edits across the engine.
- A complete TypeScript/TSX backend: symbol extraction, reference (edge)
  extraction, prose generation, and patch/edit.
- Extend the symbol-kind vocabulary with `interface`, `type`, `enum`,
  `enum_member`, and `property` — applied consistently across the store, the
  agent surface (grep), prose generation, the system model, and the desktop.
- Index this repo's own TypeScript (`opencode/`, `app/src/`) so `.ts`/`.tsx`
  files are grep/read/trace/patch-able.
- **Zero regression** on the existing Python path: all current tests pass
  untouched through the refactor.

### Non-goals (this PRD)

- Languages beyond TypeScript/TSX. The registry makes Go/Rust/etc. additive;
  they are out of scope here.
- **Type-inference-based** reference resolution. The TS resolver is
  config-and-syntax driven (it reads `tsconfig.json` / `package.json` and the
  AST) but does **not** run type inference. Edges that require knowing a value's
  inferred type — instance-method dispatch on a typed value, conditional
  `exports` map branching, computed/dynamic `import()` specifiers — remain
  documented misses, the same honesty bar Python's resolver holds. This is the
  *only* remaining resolution non-goal; aliases, workspace packages, and
  first-party `.d.ts` are all in scope (§6).

---

## 2. Current architecture — the seams

Research established that trie already has a clean split between
language-neutral and Python-specific layers. The neutral layers are reused
as-is; the Python-specific layers get per-language siblings.

### Already language-neutral (reused unchanged)

| Layer                 | File                                              | Why it's neutral                                                                                                 |
| --------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| File discovery        | `trie/scope.py` (`discover_files`)                | pure glob, extension-agnostic                                                                                    |
| Graph store           | `trie/graph/store.py` (`Store`, schema, edges)    | stores generic `Symbol`/`Reference` keyed by string `kind`/`qualified_name`; no syntax knowledge                 |
| Edge existence filter | `trie/graph/store.py:replace_all_edges`           | resolves candidate qnames against the symbol table; drops unknowns. Stdlib/`node_modules` need no special-casing |
| Cascade               | `trie/sync/cascade.py` (`compute_cascade`)        | pure graph traversal                                                                                             |
| Triefact format       | `trie/sync/writer.py` (`TriefactFile`, sentinels) | Markdown serialization only                                                                                      |
| Source splicing       | `trie/edits/apply.py:_read_source_span`           | line-range based                                                                                                 |

### Python-specific (gets a per-language sibling or a dispatch point)

| Concern              | File / anchor                                                                                                         | Plan                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Symbol extraction    | `trie/parse/python.py` (`extract_symbols`, `Symbol`)                                                                  | sibling `trie/parse/typescript.py`; `Symbol` moves to neutral `types.py`           |
| Reference extraction | `trie/parse/references.py` (`extract_file_data`, `Reference`)                                                         | sibling `trie/parse/typescript_refs.py`; `Reference`/`FileData` move to `types.py` |
| Module resolution    | (none — Python uses dotted imports, resolved inline in `references.py`)                                               | new `trie/parse/ts_resolve.py` (tsconfig `paths`/`baseUrl`/`extends` + workspace `package.json` map + index/ext probing) |
| Generator prompt     | `trie/sync/generator.py:12` (`SYSTEM_PROMPT`, Python-worded)                                                          | becomes `backend.system_prompt()`                                                  |
| Edit diagnostics     | `trie/edits/apply.py:27,46,67` (pyright/ruff parsers, `_PARSERS`)                                                     | add `_parse_tsc_output`; register in `_PARSERS`                                    |
| Scratch overlay      | `trie/edits/pipeline.py:907` (`_overlay_package`, `rglob("*.py")`)                                                    | union of backend overlay globs + tsconfig/package.json                             |
| Hardcoded `.py`      | `mcp_server.py:378`, `cli.py:3118` (qname→file), `sync/reconcile.py:39` (triefact→source), `init.py` (project detect) | route through `backend.source_suffix()` / registry probing                         |

There is **no language abstraction today** — parse functions are imported by
name in `scan.py`, `check.py`, `sync/single_file.py`, `sync/roles.py`,
`edits/apply.py`. This PRD introduces the abstraction those call sites dispatch
through.

---

## 3. Design — the `LanguageBackend` registry

### 3.1 Neutral value types — `trie/parse/types.py` (new)

Move out of `parse/python.py` / `parse/references.py` so a non-Python backend
can produce the same types without importing the Python module:

- `Symbol` (frozen dataclass — fields unchanged from today's definition).
- `Reference`, `FileData`.
- `KINDS` — the **single canonical** kind tuple. Every validator and doc
  imports this instead of hardcoding string lists.

```python
KINDS = (
    "function", "class", "method", "constant", "module",   # existing
    "interface", "type", "enum", "enum_member", "property", # new (§5)
)
```

The old modules re-export these names for one transition step, then call sites
migrate to `trie.parse.types`.

### 3.2 The backend protocol — `trie/parse/base.py` (new)

```python
class LanguageBackend(Protocol):
    name: str                      # "python" | "typescript"
    extensions: tuple[str, ...]    # (".py",) | (".ts", ".tsx")

    def extract_file_data(self, path, source_root, *, source_text=None) -> FileData: ...
    def extract_symbols(self, path, source_root, *, source_text=None) -> list[Symbol]: ...
    def module_key(self, rel_path) -> str: ...        # qname prefix (path minus ext)
    def source_suffix(self) -> str: ...               # ".py" | ".ts"
    def lsp_backends(self) -> list[LspBackend]: ...    # default checkers for patch-apply
    def overlay_globs(self) -> tuple[str, ...]: ...    # scratch-tree hardlink globs
    def overlay_extra_files(self) -> tuple[str, ...]: ...  # ("tsconfig.json", "package.json")
    def system_prompt(self) -> str: ...                # language-tuned generator prompt
```

### 3.3 The registry — `trie/parse/registry.py` (new)

- `get_backend_for_file(path) -> LanguageBackend | None` (by extension).
- `get_backend(name) -> LanguageBackend`.
- `source_suffixes() -> tuple[str, ...]` (all registered extensions — used to
  map a `.md` triefact back to whichever source file exists on disk).
- Free-function shims `extract_file_data(path, source_root)` /
  `extract_symbols(...)` that look up the backend and delegate — drop-in
  replacements for the functions `scan.py` / `check.py` import today.
- Registers `PythonBackend` and `TypeScriptBackend` at import.

### 3.4 `PythonBackend` — the reference implementation

A thin class in `trie/parse/python.py` that delegates to the existing free
functions. **Zero behavior change** — the Python suite is the regression guard
for the entire refactor.

---

## 4. Symbol-kind vocabulary

### 4.1 The governing rule

trie emits a construct as its own symbol **iff it can be an independent
reference target in the graph.** This is not a new rule — it is the rule that
makes Python emit `method` symbols one level deep inside a class
(`parse/python.py:189-201`): `Class.method` is independently callable, so it
earns a node, while the class body as a whole does not absorb it.

The reference resolver already resolves qualified member access via `(base,
attr)` pairs and rightmost-attribute call targets
(`parse/references.py:222-311`). In TypeScript, `Color.Red` and
`HttpStatus.OK` are exactly such accesses; the resolver will produce
`(Color, Red)` candidates. If enum members were folded into the enum body,
every such edge would collapse onto the enum node and the granularity Python
deliberately preserves for methods would be lost. Therefore enum members —
and class fields/properties — earn their own symbols, parented to their
container exactly as methods are.

### 4.2 The five new kinds

| Kind          | TS construct                     | Parent                         | `is_public`                            |
| ------------- | -------------------------------- | ------------------------------ | -------------------------------------- |
| `interface`   | `interface_declaration`          | none (top-level)               | `export` keyword                       |
| `type`        | `type_alias_declaration`         | none                           | `export` keyword                       |
| `enum`        | `enum_declaration`               | none                           | `export` keyword                       |
| `enum_member` | member inside an enum body       | the enum (via `parent_class`)  | inherits enum's public flag            |
| `property`    | class field / property signature | the class (via `parent_class`) | not `_`/`#`-prefixed and parent public |

`parent_class` (already on `Symbol`) carries the container name for
`enum_member` and `property`, mirroring how `method` uses it. No new `Symbol`
field is required.

### 4.3 Consumers that must change

Every place that enumerates the closed kind set, with the canonical fix being
"import `KINDS` from `trie.parse.types`":

- `trie/parse/types.py` — define `KINDS` (source of truth); `Symbol.kind` doc.
- `trie/graph/store.py:15` — bump `SCHEMA_VERSION` (forces a clean cache
  rebuild when TS enters scope; the `kind` column is free-text so **no schema
  migration is needed**, only a version bump). `GrepPredicate.kind` doc at
  `store.py:167`.
- `trie/mcp_server.py:1544-1556` — grep-kind validator allow-list + error
  message → import `KINDS`. `mcp_server.py:1002` — grep tool docstring kind
  enumeration.
- `trie/graph/system_model.py:184,423` — `module` is dropped; new kinds flow
  as ordinary nodes (logic is allow-by-default). Verify `_owning_class` and the
  method-grouping path handle `enum_member` / `property` parenting.
- `trie/sync/generator.py:89,95` — kind-specific prose hints; add hints for
  `interface` / `type` / `enum` (+ `property` as attribute, like `@property`).
- `trie/cli.py:2490` — help-text example (cosmetic).
- `app/src/api/types.ts:4` — widen the `SymbolKind` union to include
  `"interface" | "type" | "enum" | "enum_member" | "property"`. The graph view
  already filters only `module` (`app/src/store/graphStore.ts:276`), so new
  kinds render; extend the legend if it enumerates kinds.

---

## 5. TypeScript parse backend — `trie/parse/typescript.py`

Dependency: `tree-sitter-typescript` (added to `pyproject.toml`). Structure
mirrors `parse/python.py`.

### 5.1 Node-type → kind mapping

| tree-sitter node                                          | kind                    |
| --------------------------------------------------------- | ----------------------- |
| `function_declaration`                                    | `function`              |
| `const x = (…) => …` / `const x = function …` (top-level) | `function`              |
| `class_declaration`                                       | `class`                 |
| `method_definition` (in class body)                       | `method`                |
| class field / `public_field_definition`                   | `property`              |
| `interface_declaration`                                   | `interface`             |
| `type_alias_declaration`                                  | `type`                  |
| `enum_declaration`                                        | `enum`                  |
| enum member (in enum body)                                | `enum_member`           |
| top-level `const`/`let`/`var` non-function                | `constant`              |
| residual top-level statements (imports, side effects)     | `module` (`__module__`) |

### 5.2 Extraction details

- **Export unwrapping**: `export`, `export default`, `export const` wrappers are
  unwrapped to the underlying declaration, analogous to `_undecorate` for
  decorators. The `export` keyword sets `is_public`.
- **Docstrings**: leading JSDoc/TSDoc `/** … */` block → `docstring` field
  (replaces PEP 257 extraction).
- **Fingerprint**: reuse the exact `body_normalized_hash` token-normalization
  strategy (concatenate leaf tokens, skip `comment` nodes) so cascade and
  `verify` behave identically across languages.
- **qname form**: `module_key` is the source-root-relative path minus
  extension (slash form), identical to Python — `app/src/store/graphStore:foo`.

### 5.3 Declaration files (`.d.ts`) — first-class behavior

In a strongly-typed language a declaration **is** behavior: it is the contract
other symbols bind to. This repo proves the point — `import … from "lang-map"`
resolves to `interface MapReturn` declared in
`opencode/packages/web/src/types/lang-map.d.ts`; `global.d.ts` /
`custom-elements.d.ts` augment modules and namespaces that `.tsx` code depends
on. Skipping these orphans every edge that targets them. First-party `.d.ts`
are therefore indexed by the TypeScript backend.

| tree-sitter node                                   | kind                                |
| -------------------------------------------------- | ----------------------------------- |
| `interface_declaration`                            | `interface` (+ `property` members)  |
| `type_alias_declaration`                           | `type`                              |
| `enum_declaration`                                 | `enum` (+ `enum_member`)            |
| `declare function`                                 | `function`                          |
| `declare const` / `declare let` / `declare var`    | `constant`                          |
| `declare module "x" { … }` (ambient module)        | `module`, keyed by the declared module name `"x"` so `import … from "x"` resolves to it |
| `declare global` / `namespace` augmentation blocks | `module` / `type`; members that are independent reference targets become child symbols per the §4.1 rule |

Specifics:

- **No executable body**: a declaration's content *is* its signature, so
  `body_normalized_hash` is computed over the declaration text. A changed
  declaration correctly invalidates dependents through the same cascade/verify
  path as a changed function body.
- **`is_public`**: `export` / `declare` visibility.
- **Ambient module symbols** are keyed by the literal module name (`"lang-map"`,
  `"solid-js"`), not a file-relative qname, so the resolver (§6) can map a bare
  import specifier straight onto them.
- **Scope**: first-party `**/*.d.ts` are indexed; `node_modules/**` `.d.ts`
  stay excluded (third-party stubs are external and drop out via
  `replace_all_edges`, exactly like any other external reference).
- **Triefact mapping**: `.d.ts` is a distinct source suffix. The registry's
  `source_suffixes()` and `reconcile.py` triefact↔source round-trip must treat
  `foo.d.ts` as a unit (e.g. `foo.d.ts` ↔ `foo.d.md`) rather than splitting on
  the first dot. See §6.4 and the Phase-2 routing.

---

## 6. TypeScript reference heuristics — `trie/parse/typescript_refs.py`

Per-language resolver. Same permissive candidate model as Python: emit a
candidate edge for every plausible target qname; `store.replace_all_edges`
drops the ones the project doesn't define (so `node_modules` imports vanish
without special-casing).

### 6.1 Specifier resolution — `trie/parse/ts_resolve.py`

The repo forces this to be real, not a `./`-only heuristic: `app/tsconfig.json`
declares `"@/*": ["./src/*"]`, so `app/src` imports its own modules via `@/…`;
opencode is a Bun **workspace monorepo** (`packages/*`) where cross-package
imports use the package name. Treating either as a miss would erase the bulk of
the testbed's call graph.

`TsResolver` is built once per scan from the project root and maps a module
specifier + importing-file path to a slash-form **module key** (or `None`),
trying layers in order:

1. **Relative** — `./`, `../` resolved against the importing file's directory.
2. **tsconfig `paths` / `baseUrl`** — load the nearest `tsconfig.json` (walking
   up, following `extends` chains), build the alias map (`@/*` → `src/*`), and
   rewrite the specifier to a project-relative path. `baseUrl` handles
   non-relative bare specifiers that resolve inside the project.
3. **Workspace packages** — parse workspace `package.json` `name` +
   `exports`/`module`/`main` to map a bare package specifier (`@scope/pkg`,
   `lang-map`) to that package's entry module key, including ambient module
   names declared in first-party `.d.ts` (§5.3).
4. **Drop** — anything still unresolved stays a candidate and is removed by
   `replace_all_edges` (so genuine `node_modules` libraries vanish, while
   first-party packages resolve).

Each layer ends in **module-file probing**: try `.ts`, `.tsx`, `.d.ts`, then
`<dir>/index.{ts,tsx,d.ts}` for directory/barrel imports. The resolver is
config-and-syntax driven, deterministic, cached, and LLM-free. tsconfig and
workspace maps are read once and memoized per scan.

### 6.2 Coverage

- `import { x } from "<spec>"` → resolve `<spec>` via §6.1 → bind `x` →
  `key:x`. Works for relative, `@/`-aliased, and workspace-package specifiers.
- `import { x as y } from "<spec>"` → bind local `y` → `key:x`.
- `import * as ns from "<spec>"` + `ns.x()` → `key:x`.
- `import Foo from "<spec>"` (default) → bind `Foo` → `key:default` (and the
  module's default-exported symbol when resolvable).
- `export { x } from "<spec>"` re-exports → edge through the barrel.
- Directory / barrel import → `<dir>/index` module key (probing rule above).
- Bare workspace import (`@scope/pkg`) → the package's entry module key.
- Ambient module import (`from "lang-map"`) → the `module` symbol declared in
  the first-party `.d.ts` (§5.3).
- Intra-file: a symbol body referencing another top-level symbol's name → edge.
- Call-position (`x()`, `a.b.x()`) → `calls`; bare reference → `references`;
  `extends` → `inherits`; `implements` → `implements`. Same `_KIND_RANK`
  upgrade and class→method `contains` edges as Python.

### 6.3 Documented misses (v1)

Only edges that require **type inference** — knowing a value's inferred type —
remain out of reach. The resolver reads config and syntax, not types:

- Instance-method dispatch on a value whose type isn't locally evident
  (`obj.method()` where `obj`'s type comes from inference).
- Conditional `exports` map branching (`import`/`require`/`browser`
  conditions); the resolver takes the primary `import`/`module` entry.
- Computed / dynamic `import(expr)` and `require(expr)` with non-literal
  specifiers.
- Re-export wildcard chains (`export * from`) more than one hop deep.

These mirror the honesty bar Python's resolver documents at
`parse/references.py:25-31`; they close when a type-aware resolver replaces the
heuristic, with the `Reference` / `replace_all_edges` contract unchanged.

### 6.4 Triefact round-trip for `.d.ts`

`.d.ts` is a single source suffix, not `.ts` with a `.d` infix. The registry
`source_suffixes()` must list `.d.ts` ahead of `.ts` so the longest match wins,
and the triefact↔source mapping pairs `foo.d.ts` ↔ `foo.d.md` (suffix replaced
as a unit). `reconcile.py` probes `source_suffixes()` in longest-first order to
recover the source path for a given triefact.

---

## 7. Edit / patch backend (TypeScript)

- **Diagnostics**: add `_parse_tsc_output(stdout)` and register it in the
  `_PARSERS` table (`trie/edits/apply.py:67`) alongside `pyright`/`ruff`.
  Default TS `lsp_backends()` returns `tsc --noEmit` (and optionally
  `eslint --format json`, reusing a JSON parser shape).
- **Per-language backends**: `Edits.lsp_backends` (`config.py:74`) becomes the
  fallback; the backend's `lsp_backends()` supplies language-correct checkers.
  Backend selection for a patch is by the patched file's extension.
- **Scratch overlay**: `_overlay_package` (`pipeline.py:907`) currently
  hardlinks `*.py`. Generalize to the union of registered backends'
  `overlay_globs()`, plus `overlay_extra_files()` (`tsconfig.json`,
  `package.json`) so `tsc` resolves the import graph.
- **Splicing**: line-range splicing (`apply.py:_read_source_span`) is already
  language-neutral; TS symbols populate `start_line`/`end_line` the same way.
  The fingerprint-recompute path (`apply.py:573`) routes through the registry.

### 7.1 Post-implementation addendum — three missed spots (now fixed)

The first implementation pass covered diagnostics, `lsp_backends()`, and the
overlay (above) but left **three Python-hardcoded spots inside the edit
pipeline**, which made a real TS `trie_patch_apply` fail with
`syntax_error_after_retry_cap` and `file_not_found`. All three are now
backend-routed:

1. **Generation prompt** (`edits/infer.py`, `edits/backends/llm.py`). The
   prompt told the model it was editing *Python* and fenced old source as
   ` ```python `. Added `LanguageBackend.edit_system_prompt()` +
   `code_fence()` (Python + TS); the edit/infer/fixup paths resolve the
   backend by `file_path` and use the language-correct prompt and fence.
2. **Syntax gate** (`edits/apply.py:_compile_check`). It used Python's
   `compile(src, "exec")` for ALL languages, so every spliced TS file failed
   and the LSP-fixup loop discarded every TS fix. Added
   `LanguageBackend.validate_syntax(source, file_path)` — Python uses
   `compile`; TS runs `tsc --noEmit --noResolve` and fails only on **TS1xxx
   syntax** errors (TS2xxx resolution/type errors are expected in isolation;
   the overlay diagnostics pass is the real type gate). `_compile_check`
   takes an optional `file_path` and routes through the registry; it degrades
   to "accept" when no `tsc` is present so it never hard-blocks.
3. **Create-symbol file resolution** (`mcp_server.py`, `cli.py`,
   `registry.resolve_create_target`). `qname.split(":")[0] + ".py"` hardcoded
   `.py`. Now probes registered `source_suffixes()` for an existing module
   file, infers a new file's language from a sibling, and only then falls
   back to a default suffix.

Two robustness improvements landed alongside:

- **True new-file creation** (`pipeline.py`): a create targeting a
  non-existent file now scaffolds it (empty → generated body), `commit`
  `mkdir`s parents and the post-commit scan absorbs it; rollback unlinks new
  files. (Previously surfaced "new-file create not supported in v1".)
- **Class-method placement** (`pipeline._place_new_symbol` /
  `_insert_into_parent` / `_find_container_span`): a `Module:Class.method`
  create is inserted INSIDE the parent body (brace-matched for TS, indent for
  Python), re-indented to member level, with stale-span recovery for
  same-file modify+create batches.
- **`merge_notes` resilience** (`infer.py`): a single patch skips the merge
  LLM call; any merge failure/empty response degrades to the raw notes
  instead of aborting the whole apply on a `MergeNotesOutput` validation
  error.

Tests: `tests/test_edits_typescript.py` (fences, prompts, `validate_syntax`
TS1-vs-TS2 decision, create-target resolution, class-method placement,
merge_notes resilience) + `tests/test_edits_structural.py` (new-file create,
nested-dir create, method-into-class, same-file modify+create-method).

---

## 8. Config & scope

- `trie/config.py`: `Scope.include` default stays `["**/*.py"]` for existing
  projects. Optional `[languages]` section for per-language LSP overrides
  (else backend defaults apply).
- `pyproject.toml`: add `tree-sitter-typescript`.
- This repo's `trie.toml`: un-exclude `opencode/` and `app/`; add
  `**/*.ts`, `**/*.tsx`, **and first-party `**/*.d.ts`** to `include` (§5.3 —
  declarations are behavior); exclude `**/node_modules/**`, `**/dist/**`,
  `**/build/**`, and generated bundles. Note: `node_modules` `.d.ts` are
  excluded by the `node_modules` rule, so the `.d.ts` include is first-party
  only.
- **Resolver inputs**: the TS resolver (§6.1) discovers `tsconfig.json` (with
  `extends`) and workspace `package.json` files within scope; these are read
  for resolution but are not themselves indexed as symbols.
- First-sync cost is bounded by the existing `trie sync --limit` and the
  bootstrap budget ranking (`sync/bootstrap.py`) — **not** by narrowing graph
  scope, which would leave cross-file edges dangling at a slice boundary and
  produce a less-correct graph.

---

## 9. Desktop impact

- Widen `SymbolKind` (`app/src/api/types.ts:4`) to the full vocabulary.
- `app/src/store/graphStore.ts:276` already filters only `module`, so new
  kinds render without further change.
- Extend the graph legend / kind color map if it enumerates kinds (audit
  `GraphCanvas` during implementation).

The Python backend remains the source of truth for kinds; the desktop union
mirrors `KINDS`.

---

## 10. Testing strategy

- Fixtures under `tests/fixtures/tiny_ts_repo/` mirroring the existing
  `tests/fixtures/tiny_repo/` layout, exercising every new kind and each
  reference shape (relative import, barrel, re-export, `import * as`, default,
  intra-file, extends/implements). The fixture includes a `tsconfig.json` with
  a `paths` alias, a two-package workspace (`package.json` `workspaces`) with a
  cross-package import, and a first-party `.d.ts` declaring an `interface` and
  an ambient `declare module` that other fixture files import.
- New test modules: `tests/test_parse_typescript.py`,
  `tests/test_references_typescript.py`, `tests/test_ts_resolve.py`,
  `tests/test_registry.py`.
- New-kind assertions: interface/type/enum/enum_member/property emitted with
  correct parenting and `is_public`.
- Resolution assertions: `@/`-alias, workspace-package, and ambient-`.d.ts`
  imports each produce a resolved edge; an unresolvable bare specifier is
  dropped. `.d.ts` ↔ `.d.md` triefact round-trip.
- **Python regression guard**: the entire existing suite passes untouched.
- CI quad (AGENTS.md): `uv run pytest`, `uv run ruff check .`,
  `uv run ruff format --check .`.

---

## 11. Rollout (worktree)

Branch `feat/multi-language`, created from HEAD in a separate worktree. Phases
land as ordered commits; phases 0–2 are mechanical with zero behavior change
and a full test pass, de-risking the rest.

1. **Phase 0** — kind vocabulary across all consumers; `SCHEMA_VERSION` bump.
2. **Phase 1** — neutral `types.py` (+ `KINDS`), `base.py`, `registry.py`;
   `PythonBackend` wrapper.
3. **Phase 2** — route all parse call sites + `.py`-hardcoded spots through the
   registry.
4. **Phase 3** — `typescript.py` (symbols, 5 new kinds, `.d.ts` declarations);
   `ts_resolve.py` (tsconfig `paths`/`baseUrl`/`extends` + workspace package
   map + index/ext probing); `typescript_refs.py` (heuristics consuming the
   resolver).
5. **Phase 4** — TS edit/patch (`_parse_tsc_output`, `_PARSERS`,
   `lsp_backends()`, `_overlay_package` generalization).
6. **Phase 5** — `pyproject.toml` dep, `trie.toml` scope, `[languages]` config.
7. **Phase 6** — TS fixtures + tests; Python suite green; lint clean.
8. **Validation** — scan → `sync --limit` → grep/read/trace → patch a `.ts`
   symbol, on this repo's own TS.
9. **Desktop** — widen `SymbolKind` union + legend.

---

## 12. Risks & mitigations

| Risk                                 | Mitigation                                                                              |
| ------------------------------------ | --------------------------------------------------------------------------------------- |
| Refactor breaks the Python path      | Phases 0–2 are zero-behavior-change; Python suite is the gate before any TS code lands  |
| `SCHEMA_VERSION` bump wipes `.trie/` | Cache is regenerable by design; documented                                              |
| Heuristic TS resolution misses edges | Only type-inference cases miss; aliases/workspaces/`.d.ts` resolved via config + syntax; store filter drops the rest |
| tsconfig `extends` / monorepo complexity | Resolver walks `extends` chains and workspace `package.json`; memoized per scan; covered by fixtures incl. an aliased + multi-package case |
| Desktop union drifts from `KINDS`    | `KINDS` is the single source of truth; desktop mirrors it; legend audited in Phase 9    |
| First TS sync cost                   | `sync --limit` / bootstrap budget ranking bounds spend without narrowing scope          |

---

## 13. Acceptance criteria

- A `.ts`/`.tsx` file in scope is grep-able, read-able, trace-able, and
  patch-able via the same MCP/CLI surface as Python.
- `interface`, `type`, `enum`, `enum_member`, and `property` symbols appear in
  the graph with correct parenting, `is_public`, and prose.
- Cross-file TS edges resolve for relative imports, barrels, and re-exports;
  `node_modules` references are absent (dropped by the store filter).
- A `@/`-aliased import (per `app/tsconfig.json` `paths`) resolves to a
  first-party edge, not a dropped candidate.
- A cross-package workspace import (an `opencode/packages/*` package name)
  resolves to that package's entry symbol.
- A symbol that references an `interface` / `type` / ambient `declare module`
  declared in a first-party `.d.ts` produces a resolved edge; that `.d.ts` is
  itself grep/read-able and round-trips through its `.d.md` triefact.
- A TS patch passes `tsc --noEmit` through the edit pipeline and cascades to
  callers like a Python patch.
- Adding a hypothetical third language requires only a new backend module +
  registration — no edits to the engine call sites.
- The full pre-existing Python test suite passes unchanged; `ruff check` and
  `ruff format --check` are clean.
