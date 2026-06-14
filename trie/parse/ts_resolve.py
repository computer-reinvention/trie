"""TypeScript module-specifier resolution — config + syntax, never type inference.

An import like `import { x } from "<spec>"` only produces a graph edge if we can
turn `<spec>` into the slash-form *module key* of a project file. This module
does exactly that, in layers (see docs/core/multi-language-backend-prd.md §6.1):

1. relative (`./`, `../`) against the importing file's directory
2. tsconfig `paths` aliases + `baseUrl` (walking up, following `extends`)
3. workspace package names (`package.json` `name` -> entry module key)
4. otherwise unresolved (the store drops the candidate edge)

Every layer ends in file probing: try `.ts` / `.tsx` / `.d.ts`, then
`<dir>/index.{ts,tsx,d.ts}`.

`TsResolver` is built once per scan against the source root, reads tsconfig and
workspace `package.json` files eagerly, memoizes resolution, and makes no LLM or
type-checker calls.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

_SOURCE_EXTS = (".ts", ".tsx", ".d.ts")
_INDEX_BASENAMES = ("index.ts", "index.tsx", "index.d.ts")


def _strip_jsonc(text: str) -> str:
    """Best-effort strip of `//` and `/* */` comments + trailing commas from a
    tsconfig (which is JSONC). Good enough for `compilerOptions` extraction."""
    # Remove block comments.
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    # Remove line comments (not inside strings — tsconfig rarely has // in strings).
    text = re.sub(r"(?m)//.*?$", "", text)
    # Remove trailing commas before } or ].
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def _load_jsonc(path: Path) -> dict | None:
    try:
        return json.loads(_strip_jsonc(path.read_text()))
    except (OSError, ValueError):
        return None


def _module_key(path: Path, source_root: Path) -> str | None:
    """Slash-form module key (path minus a recognised source suffix) for a file
    under `source_root`, or None if outside the root."""
    try:
        rel = path.resolve().relative_to(source_root)
    except ValueError:
        return None
    s = str(rel)
    for ext in sorted(_SOURCE_EXTS, key=len, reverse=True):
        if s.endswith(ext):
            return s[: -len(ext)]
    return rel.with_suffix("").as_posix()


@dataclass
class TsConfig:
    """The resolution-relevant slice of one tsconfig.json."""

    config_dir: Path
    base_url: Path | None
    paths: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class TsResolver:
    """Resolves TypeScript import specifiers to project module keys.

    Construct via `TsResolver.build(source_root)`; call `resolve(specifier,
    from_file)` per import.
    """

    source_root: Path
    tsconfigs: list[TsConfig]
    # package name -> absolute entry file path
    workspace_entries: dict[str, Path]
    _cache: dict[tuple[str, str], str | None] = field(default_factory=dict)

    @classmethod
    def build(cls, source_root: Path) -> TsResolver:
        source_root = source_root.resolve()
        tsconfigs = _collect_tsconfigs(source_root)
        workspace_entries = _collect_workspace_entries(source_root)
        return cls(
            source_root=source_root,
            tsconfigs=tsconfigs,
            workspace_entries=workspace_entries,
        )

    # -- public API -------------------------------------------------------

    def resolve(self, specifier: str, from_file: Path) -> str | None:
        """Module key for `specifier` imported from `from_file`, or None."""
        key = (specifier, str(from_file))
        if key in self._cache:
            return self._cache[key]
        result = self._resolve_uncached(specifier, from_file.resolve())
        self._cache[key] = result
        return result

    # -- layers -----------------------------------------------------------

    def _resolve_uncached(self, specifier: str, from_file: Path) -> str | None:
        if specifier.startswith("."):
            target = (from_file.parent / specifier).resolve()
            return self._probe(target)

        aliased = self._resolve_alias(specifier)
        if aliased is not None:
            return aliased

        return self._resolve_workspace(specifier)

    def _resolve_alias(self, specifier: str) -> str | None:
        for cfg in self.tsconfigs:
            for pattern, targets in cfg.paths.items():
                rewritten = _apply_path_pattern(pattern, targets, specifier)
                if rewritten is None:
                    continue
                base = cfg.base_url or cfg.config_dir
                key = self._probe((base / rewritten).resolve())
                if key is not None:
                    return key
            # baseUrl-relative bare specifier (no alias match).
            if cfg.base_url is not None:
                key = self._probe((cfg.base_url / specifier).resolve())
                if key is not None:
                    return key
        return None

    def _resolve_workspace(self, specifier: str) -> str | None:
        # Exact package name, or a subpath import `@scope/pkg/sub`.
        entry = self.workspace_entries.get(specifier)
        if entry is not None:
            return _module_key(entry, self.source_root)
        for name, ent in self.workspace_entries.items():
            if specifier.startswith(name + "/"):
                subpath = specifier[len(name) + 1 :]
                pkg_dir = ent.parent
                key = self._probe((pkg_dir / subpath).resolve())
                if key is not None:
                    return key
        return None

    def _probe(self, target: Path) -> str | None:
        """Resolve a filesystem target (possibly extension-less or a directory)
        to a concrete source file's module key."""
        # Exact file (already has a known extension).
        if (
            target.is_file()
            and any(str(target).endswith(e) for e in _SOURCE_EXTS)
            and _module_key(target, self.source_root) is not None
        ):
            return _module_key(target, self.source_root)
        # Extension probing: foo -> foo.ts / foo.tsx / foo.d.ts
        for ext in _SOURCE_EXTS:
            cand = target.with_name(target.name + ext)
            if cand.is_file():
                return _module_key(cand, self.source_root)
        # Directory / barrel: foo/ -> foo/index.{ts,tsx,d.ts}
        for base in _INDEX_BASENAMES:
            cand = target / base
            if cand.is_file():
                return _module_key(cand, self.source_root)
        return None


def _apply_path_pattern(pattern: str, targets: list[str], specifier: str) -> str | None:
    """If `specifier` matches a tsconfig `paths` pattern, return the rewritten
    (baseUrl-relative) path using the first target, else None.

    Patterns use a single `*` wildcard, e.g. `"@/*": ["./src/*"]`.
    """
    if not targets:
        return None
    target0 = targets[0]
    if "*" in pattern:
        prefix, _, suffix = pattern.partition("*")
        if specifier.startswith(prefix) and specifier.endswith(suffix):
            middle = specifier[len(prefix) : len(specifier) - len(suffix) if suffix else None]
            return target0.replace("*", middle).lstrip("./") if "*" in target0 else target0
        return None
    if specifier == pattern:
        return target0.lstrip("./")
    return None


def _collect_tsconfigs(source_root: Path) -> list[TsConfig]:
    """Parse every tsconfig.json in scope, resolving `extends` chains.

    Returns inner (more specific) configs first so their aliases win.
    """
    configs: list[TsConfig] = []
    for path in sorted(source_root.rglob("tsconfig*.json")):
        if "node_modules" in path.parts:
            continue
        merged = _resolve_tsconfig_chain(path, seen=set())
        if merged is None:
            continue
        opts = merged.get("compilerOptions", {}) or {}
        config_dir = path.parent
        base_url = (config_dir / opts["baseUrl"]).resolve() if opts.get("baseUrl") else None
        paths = opts.get("paths") or {}
        if paths or base_url is not None:
            configs.append(TsConfig(config_dir=config_dir, base_url=base_url, paths=paths))
    # More deeply nested config dirs first (more specific).
    configs.sort(key=lambda c: len(c.config_dir.parts), reverse=True)
    return configs


def _resolve_tsconfig_chain(path: Path, *, seen: set[Path]) -> dict | None:
    """Load a tsconfig and shallow-merge it over what it `extends`."""
    path = path.resolve()
    if path in seen:
        return None
    seen.add(path)
    data = _load_jsonc(path)
    if data is None:
        return None
    extends = data.get("extends")
    base: dict = {}
    if isinstance(extends, str):
        ext_path = extends
        if ext_path.startswith("."):
            candidate = (path.parent / ext_path).resolve()
            if not candidate.name.endswith(".json"):
                candidate = candidate.with_name(candidate.name + ".json")
            parent = _resolve_tsconfig_chain(candidate, seen=seen)
            if parent is not None:
                base = parent
        # Non-relative extends (e.g. "@tsconfig/bun/tsconfig.json") live in
        # node_modules — out of scope; their compilerOptions rarely add paths.
    merged = dict(base)
    merged_opts = dict(base.get("compilerOptions", {}) or {})
    merged_opts.update(data.get("compilerOptions", {}) or {})
    merged.update(data)
    if merged_opts:
        merged["compilerOptions"] = merged_opts
    return merged


def _collect_workspace_entries(source_root: Path) -> dict[str, Path]:
    """Map every in-scope package.json `name` to its entry source file.

    Entry preference: `module` -> `main` -> `index.ts` -> `index.tsx` ->
    `src/index.ts`. Only entries that resolve to a real source file are kept, so
    a bare `import "@scope/pkg"` produces a resolvable target.
    """
    entries: dict[str, Path] = {}
    for path in sorted(source_root.rglob("package.json")):
        if "node_modules" in path.parts:
            continue
        data = _load_jsonc(path)
        if not data or not isinstance(data.get("name"), str):
            continue
        name = data["name"]
        pkg_dir = path.parent
        entry = _package_entry_file(pkg_dir, data)
        if entry is not None:
            entries[name] = entry
    return entries


def _package_entry_file(pkg_dir: Path, data: dict) -> Path | None:
    candidates: list[str] = []
    for field_name in ("module", "main", "types", "typings"):
        val = data.get(field_name)
        if isinstance(val, str):
            candidates.append(val)
    candidates += ["index.ts", "index.tsx", "src/index.ts", "src/index.tsx"]
    for rel in candidates:
        # A `main` may point at compiled `dist/foo.js`; remap to a source sibling.
        base = pkg_dir / rel
        for cand in (
            base,
            base.with_suffix(".ts"),
            base.with_suffix(".tsx"),
            base.with_suffix(".d.ts"),
        ):
            if cand.is_file() and any(str(cand).endswith(e) for e in _SOURCE_EXTS):
                return cand
    return None
